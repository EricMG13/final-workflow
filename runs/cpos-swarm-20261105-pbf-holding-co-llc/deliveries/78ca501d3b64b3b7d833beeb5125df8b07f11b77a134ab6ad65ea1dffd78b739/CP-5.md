## Request

Issuer: PBF Holding Co LLC (issuer id pbf-holding-co-llc, filed as PBF Holding Company LLC), as of 2026-11-05, evidence cutoff 2026-11-05, pathway credit_snapshot, run `pbf-holding-co-llc-2026-11-05-credit_snapshot-host`, minimum module set. This module checks the four accepted handoffs (CP-0, CP-1, CP-1A, CP-2) against the pinned filings and against each other, and grades the result (absorbed CP-5A phase). Execution is a host session; the same host wrote the handoffs it checks, so this is a self-review and not an independent one. No provider was called.

Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most? QA envelope: `qa_status` Passed; Confidence Score 38, band Insufficient Information (from `scripts/confidence_score.py`, see Calculations); `committee_status` Requires More Work.

## Sources

### Issuer sources relied on

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_pbfh-20251231.htm.jsonl | d8cc408b78dbd581d058811f04c883343b35aff7d41a81cb7f7c9a865d63578a |
| 10-Q_2026-03-31_pbf-20260331.htm.jsonl | 5a4242ec4ab0800289f99b8fb8f699b2f54c974b4153ae81aa21ea53d5f7dce3 |
| 10-Q_2026-06-30_pbf-20260630.htm.jsonl | 179cd47014072a6b74de2a12abf4417faacecc8413b4c8273ab1ec0f832d5c10 |
| 10-Q_2026-09-30_pbf-20260930.htm.jsonl | aa31b84f94b1c47f81c70abbb0ff7efeca9bcb80852596ec5368223e7eac72e3 |
| EX-99.1_2026-04-30_a991pressreleaseq1-26.htm.jsonl | 104828cb4c23629fde92b78b0620cad588c64bcdee91586fe5ba497364c7f993 |
| EX-99.1_2026-07-30_a991pressreleaseq2-26.htm.jsonl | a7bd74033edd0eddbe8e027b1ef6a171c22d27094099293d640917935e8f4118 |
| EX-99.1_2026-10-29_a991pressreleaseq3-26.htm.jsonl | ceaca5528b0d3a91964868e4bbffe0689397a5fd5afc2bb6cfc13e308a461219 |
| context | e3f25603b3db519b8b37c6f17fae4507d987050b491cc8f2ad5a0c098cf08361 |

Locators in this handoff are chunk numbers of the pinned text files (`page:N`, the extraction unit), not printed page numbers.

### Supplied handoffs

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | 6020d636d6339bed5f8cdb468a645c0df4a718ccb14e552b1c95eaddfd75b108 |
| CP-1 | 1cdf760fd0e4e56b00e2ceeb3b00667f06f1fcb79b2ec9bbcb2c8c93d195788e |
| CP-1A | c6d0ac40c5f183e0890ff97f5acfc2102adbd41f9178d8d21e1106b1d5ee320d |
| CP-2 | 88eb723a8c38ca4a5e02e0add04a25839745f9e6cd34dea88be3e0fb1a47983f |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The earlier analysis is traceable to the filings for the issuer's reported position and structure, and the checked quotations, metrics and tie-outs agree. It does not yet support a through-the-cycle view or any reading of the legal terms. | Medium | One reviewer wrote and checked every handoff, and the executed financing documents and hydrogen plants terms are missing. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 172 checked quotations sit on their cited text, and 42 of 42 recomputed metrics and 45 of 45 tie-outs agree with the filings. | The reported figures can be relied on for the issuer's position at 30 September 2026. | High |
| Of nine material claims, three are directly sourced, three calculated, one an analyst inference and two correctly labelled as gaps. | Conclusions on earnings durability and event risk rest on inference or open gaps, not on filings. | Medium |
| Six minor defects were found and none changes a conclusion; the most important is a covenant inference that should read not calculable. | Wording should be tightened before committee use, since covenant capacity is not supported. | Medium |
| The confidence score is 38 and committee use requires more work. | Treat the pack as a working draft until the legal documents and an independent review are added. | Medium |

### Evidence trace view

The analysis is traceable enough for a view of PBF Holding Company LLC's reported position and structure at 30 September 2026, and not for a through-the-cycle credit conclusion. Of nine material claims, three are directly sourced, three calculated, one an analyst inference and two correctly labelled Insufficient Information. All 172 quotations in the three handoffs that carry them sit on their cited chunks, and 42 of 42 metrics and 45 of 45 tie-outs recompute equal from the source text. The critical provenance gap is the hydrogen plants consideration together with the executed financing documents, which no pinned source supplies. The affected decision is any view on collateral, restricted payments and covenant headroom, and the remediation owner is the sourcing step. Six minor defects change no conclusion.

| Traceability summary | Result |
| --- | --- |
| Quotations checked against cited chunks | 172 spans in three handoffs; all present; one parser artifact checked by hand |
| Metrics recomputed from source text | 42 of 42 equal |
| Statement tie-outs re-added | 45 of 45 equal |
| Cross-module figure check | Every CP-2 figure found in CP-1 or CP-1A or in its own calculations |
| Material claims by lineage | 3 Directly Sourced, 3 Calculated, 1 Analyst Inference, 2 Insufficient Information |
| Open findings | 6 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_pbfh-20251231.htm.jsonl | High: filed, audited annual report | Years ended 2025-12-31, 2024-12-31 and 2023-12-31 | PBF Holding Company LLC and PBF Finance Corporation, consolidated | Statements, debt note, Adjusted EBITDA reconciliation, business, guarantors, commitments, pension | Text extraction; tables flattened | CP-0, CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_pbf-20260331.htm.jsonl | High: filed, unaudited interim report | Quarter ended 2026-03-31 | Same | Statements, debt, liquidity, EBITDA reconciliation | Unaudited; text extraction | CP-0, CP-1 |
| S3 | 10-Q_2026-06-30_pbf-20260630.htm.jsonl | High: filed, unaudited interim report | Three and six months ended 2026-06-30 | Same | Statements, debt, liquidity, hydrogen plants subsequent event | Unaudited; text extraction | CP-0, CP-1, CP-1A |
| S4 | 10-Q_2026-09-30_pbf-20260930.htm.jsonl | High: filed, unaudited interim report | Three and nine months ended 2026-09-30 | Same | Statements, debt notes, fair values, liquidity, subsequent events, guarantors | Unaudited; text extraction | CP-0, CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-30_a991pressreleaseq1-26.htm.jsonl | Medium: issuer-group press release, non-GAAP | First quarter 2026 | PBF Energy Inc., the parent | Parent results and Martinez update | Different perimeter from the issuer | CP-0 context only |
| S6 | EX-99.1_2026-07-30_a991pressreleaseq2-26.htm.jsonl | Medium: issuer-group press release, non-GAAP | Second quarter 2026 | PBF Energy Inc. | Parent results | Different perimeter | CP-0 context only |
| S7 | EX-99.1_2026-10-29_a991pressreleaseq3-26.htm.jsonl | Medium: issuer-group press release, non-GAAP | Third quarter 2026 | PBF Energy Inc. | Parent results, debt, guidance, turnaround statements | Different perimeter; management statements | CP-0, CP-1, CP-1A context |
| S8 | context | User settings, not issuer evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency | Ratings, quotes, deal terms and valuation inputs blank | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Net cash and low reported leverage at 2026-09-30 | CP-1, CP-2 | Debt principal 1,850.0 and cash 2,510.6 against LTM Adjusted EBITDA 3,505.2 | Sets near-term default and refinancing risk | Core of the sound-balance-sheet view | S4 chunks 7 and 17; S4 chunk 59, S1 chunk 123 | Principal basis, not carrying value; trailing EBITDA built on two quarters |
| 2 | Earnings swing from trough to very high and their concentration | CP-1, CP-2 | Adjusted EBITDA 29.5 in FY2025 and 3,505.2 LTM; 3,278.6 from Q2 and Q3 2026 | Debt capacity follows margins | Decides how far the balance sheet strength can be relied on | S1 chunk 123; S3 chunk 49; S4 chunk 59 | Company-defined measure; no forecast supplied |
| 3 | 2026 refinancing and maturity profile | CP-1, CP-1A, CP-2 | 2034 and 2032 notes issued, 2028 and 2030 notes redeemed, revolver to 2031-09-30 | Removes near-term maturities | Refinancing risk view | S4 chunks 17 to 24 and 33 | Executed documents not supplied |
| 4 | Claims outside debt and event exposures | CP-1, CP-1A, CP-2 | Leases 712.3, pension deficits 89.8 and 16.4, commitments 642.9, emissions 486.5, environmental 148.4, unquantified investigations | Compete with debt service in a downside | Excluded from leverage ratios | S4 chunks 7, 14, 16, 27; S1 chunks 188, 198, 206 | Pension and commitments dated 2025-12-31 |
| 5 | Parent cash flows and the hydrogen plants parent note | CP-1A, CP-2 | Contributions and distributions; Q2 and Q3 descriptions of the plants purchase differ | Cash leakage and possible lien on issuer assets | Sponsor behaviour and collateral view | S4 chunks 9, 13, 33; S3 chunk 26 | Consideration and security not described in the Q3 report |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net cash 660.6 and 0.5x total debt to LTM Adjusted EBITDA | CP-1, CP-2 | S4 chunks 7 and 17; S1 chunk 123; S2 chunk 38; S3 chunk 49; S4 chunk 59 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| LTM Adjusted EBITDA 3,505.2 and concentration in two quarters | CP-1, CP-2 | Same EBITDA reconciliations | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| 2026 refinancing sequence and maturities | CP-1, CP-1A, CP-2 | S4 chunks 17 to 24, 33 | Yes | High | Directly Sourced | Supported | High | Traced |
| Claims outside debt | CP-1, CP-2 | S4 chunks 7, 14, 16, 27; S1 chunks 188, 198, 206 | Yes | High | Directly Sourced | Supported | High | Traced |
| Liquidity of about 3,100 availability and 2,510.6 cash | CP-1, CP-2 | S4 chunk 66 | Yes | High; rounded narrative | Directly Sourced | Supported with limitation | Medium | Traced; build not reproducible |
| Parent net cash flows by period | CP-1A, CP-2 | S1 chunk 155; S4 chunk 9 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Hydrogen plants parent note and lien position | CP-1A, CP-2 | S3 chunk 26 against S4 chunk 13 | Quoted on both sides | High; the two reports differ | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Martinez and Chalmette impact | CP-1A, CP-2 | S4 chunks 5, 14, 27 | Existence cited; amount absent | High for existence | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Fundamental credit view: sound but cyclical | CP-2 | CP-1 and CP-1A rows | Yes, by handoff reference | Derived | Analyst Inference | Supported by cited basis | Medium | Traced to handoffs |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt principal 1,850.0 at 2026-09-30 | /workspace/secdata/data/2026-11-05/packs/1566011-pbf-holding-co-llc | 10-Q_2026-09-30_pbf-20260930.htm.jsonl | S4 | Chunk 17, Note 4 | CP-1 debt table | Reported | High | Components re-added equal |
| Cash 2,510.6 at 2026-09-30 | Same | Same | S4 | Chunk 7, balance sheet | CP-1 financials | Reported | High | Matches |
| Adjusted EBITDA 29.5 for FY2025 | Same | 10-K_2025-12-31_pbfh-20251231.htm.jsonl | S1 | Chunk 123, reconciliation | CP-1 financials | Reported, company-defined | Medium | Matches |
| Adjusted EBITDA 3,284.3 for nine months 2026 | Same | 10-Q_2026-09-30_pbf-20260930.htm.jsonl | S4 | Chunk 59, reconciliation | CP-1 financials | Reported, company-defined | Medium | Re-added equal |
| Cash interest paid 155.5 for nine months 2026 | Same | Same | S4 | Chunk 10, supplemental cash flow | CP-1 interest cover | Reported | High | Matches |
| Revolver amended to 4,000.0 through 2031-09-30 | Same | Same | S4 | Chunk 24, Note 4 | CP-1 and CP-1A | Reported | High | Matches |
| Operational liquidity over 5.6 billion | Same | Same | S4 | Chunk 66, Liquidity | CP-1 liquidity | Reported narrative | High | Rounded |
| Hydrogen plants contributed with property of about 388.4 | Same | Same | S4 | Chunk 13, Note 1 | CP-1A transaction summary | Reported | High | Q2 description differs |
| Secured promissory note issued by PBF LLC, 320.0 to 340.0 estimate | Same | 10-Q_2026-06-30_pbf-20260630.htm.jsonl | S3 | Chunk 26, subsequent events | CP-1A conflicts | Reported estimate | High | Not repeated in Q3 report |
| Pension funded status -89.8 and -16.4 at 2025-12-31 | Same | 10-K_2025-12-31_pbfh-20251231.htm.jsonl | S1 | Chunk 206, Note 14 | CP-1 claims outside debt | Reported | High | No interim update |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA | CP-1 table and charts; CP-2 | FY2025, nine months 2026 and 2025 and similar for Q1, Q2 | FY2025 + year-to-date 2026 - year-to-date 2025 | Recomputed from source text: 327.9, 1,457.4, 3,505.2 equal | Supported | High | Basis of every ratio | S1 chunk 123; S2 chunk 38; S3 chunk 49; S4 chunk 59 |
| Leverage on principal | CP-1; CP-2 | Principal and cash at each date | Principal / LTM Adjusted EBITDA; (principal - cash) / LTM Adjusted EBITDA | Recomputed equal: 74.6, 8.7, 1.2, 0.5 and 57.6, 7.2, 0.6, -0.2 | Supported with definition caveat | Medium | Leverage tolerance | S4 chunks 7, 17; S1 chunk 173; S2 chunk 15; S3 chunk 16 |
| Cash interest cover | CP-1; CP-2 | Cash interest paid year to date | LTM Adjusted EBITDA / (FY2025 + year-to-date 2026 - year-to-date 2025 cash interest) | Recomputed equal: 0.2, 1.8, 7.8, 21.6 | Supported with caveat | Medium | Debt service | S1 chunk 156; S2 chunk 9; S3 chunk 10; S4 chunk 10 |
| Operating cash flow less capital outlay | CP-1; CP-2 | Three investing capital lines and operating cash flow | Operating cash flow - (PP&E + turnaround + other assets) | Recomputed equal for six periods and LTM | Supported | High | Cash generation | S1 chunk 156; S2 chunk 9; S3 chunks 9 and 10; S4 chunks 9 and 10 |
| Net parent flows | CP-1A; CP-2 | Equity statements | Contributions - distributions | Recomputed equal: 199.6, -306.0, -424.0, 29.6, -60.9 | Supported | High | Sponsor behaviour | S1 chunk 155; S4 chunk 9 |
| Pro forma after October 2026 redemption | CP-1; CP-2 | Principal, cash, redemption price | 1,850.0 - 800.0; 2,510.6 - 853.4 | Illustrative; recomputed equal | Supported as illustration | Medium | Post-period position | S4 chunks 17, 33 |
| Cash coverage of a repeat of FY2025 outcome | CP-2 | Pro forma cash and FY2025 operating cash flow less outlay | 1,657.2 / 1,418.3 | Recomputed equal: 1.2x | Illustrative only | Low | Stress cushion | CP-1, CP-2 calculations |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial source gate, 6 MINOR | Script formula | 38, band Insufficient Information | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 financials table | About twenty rows cite a chunk but carry no row-level quotation; the values were verified here against the chunks | Weak lineage in the handoff, not in the evidence | A reader must open the chunk to verify | Add a short quotation per row in a later run | CP-1 handoff |
| OBSERVATION | All handoffs | Locators are extraction chunks, not printed pages | Locator convention | Page numbers differ from the filing | State the convention, as the handoffs do | All handoffs |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Seven sources pinned by sha256; registrants named on each cover | A wrong document would change every figure | None found | None |
| Locator precision | Adequate | 172 quotations all on cited chunks; table rows cite chunks without quotes | Slower verification | None on conclusions | Row-level quotations |
| Calculation reproducibility | Strong | 42 of 42 metrics and 45 of 45 tie-outs recomputed equal from source text | A calculation error would move leverage | None found | None |
| Cross-module consistency | Adequate | Every CP-2 figure found upstream; CP-1 corrected a CP-0 wording | Inconsistent figures mislead a committee | None found | Keep corrections stated |
| Perimeter discipline | Strong | Issuer and parent figures kept apart in every handoff | Parent figures could be mislabelled as issuer figures | None found | None |
| Subsequent events and cutoff | Strong | October 2026 events labelled; nothing after 2026-11-05 used as fact | Blending would misstate 30 September balances | None found | None |
| Reviewer independence | Weak | One host wrote and checked every handoff | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Executed indentures, credit agreement and covenant definitions | The documents listed as exhibits in the Q3 report | Collateral, restricted payments and covenant headroom cannot be read | Structure and cash leakage risks | Limits legal and covenant conclusions | Exhibits of the 8-Ks incorporated by reference |
| G2 | Hydrogen plants consideration, security and any issuer guarantee | Agreement and later filings | Possible lien on issuer assets | Parent behaviour and collateral view | Holds the view to current evidence | Q4 2026 filings or the agreement |
| G3 | Liquidity cannot be rebuilt from the rounded narrative | Borrowing base report | Cushion known approximately | Liquidity view | Moderate | Borrowing base certificate |
| G4 | No forecast or through-the-cycle earnings case | Normalised-margin case | Trailing EBITDA built on two quarters | Credit view durability | Caps confidence | Later module with sourced assumptions |
| G5 | Martinez and Chalmette outcomes unquantified | Later filings | Possible penalties, outage costs | Event risk rating | Moderate | Next 10-K and 10-Qs |
| G6 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/d29c2eb7c70f740d252e701958b6b93d39e5854c0f2da5835925b6cfcd7adf54 attempt 1 / pbf-holding-co-llc-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted attempt 1 | Passed with no open defect | Wording on covenants corrected by CP-1 |
| CP-1 | requests/CP-1/de2ef560f4ada2a9c6f2a404c4b373cd9dfdd48dcf565b2a4385da024d45f21e attempt 1 / same run | Statements, LTM, debt, claims outside debt, liquidity, covenants | High | Six headings and selectors; accepted attempt 1 | Passed with four MINOR findings | All metrics recomputed equal |
| CP-1A | requests/CP-1A/256937177ca0edbe0ce106a569b4c8e5aaf7a9bc7ab90ce5fbea681018b1da72 attempt 1 / same run | Business, transactions, behaviour, conflicts | High | Six headings and selectors; accepted attempt 1 | Passed with one MINOR finding | 92 quotations all present |
| CP-2 | requests/CP-2/3d5b924719f12ba411303c5a3e9b59be89cd5c00e1b3ef1613e64741e6bef3b0 attempt 1 / same run | Credit synthesis | High inputs | Six headings and selectors; accepted attempt 1 | Passed with one MINOR finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Financials and credit metrics table rows | Supported | Rows cite a chunk without a quotation | Add short quotations | None |
| MINOR | CP-1 | Liquidity statement that no facility expires within twelve months | Partly supported | Verified only for the committed revolver; the receivables and premium financing facilities state no expiry | Restrict the sentence to committed facilities | None |
| MINOR | CP-1A | Per-consumer readiness judgments and per-row evidence quality | Not provided | The method asks for each; only the behaviour table carries evidence quality | Add in a later run | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Leverage denominators use debt principal 1,850.0 | Canon asks for balance-sheet carrying value with the gross delta logged; the 237.0 delta (deferred costs 63.0, discount 174.0) is logged. On carrying value 1,613.0 the ratios are 0.5x total and -0.3x net against 0.5x and -0.2x, and for FY2025 72.8x and 55.8x | None; both bases printed | Show both bases in the table | None |
| MINOR | CP-1 | Covenant reading | CP-1 says the springing fixed charge test appears not to be in effect, from rounded availability and an undefined term | Excess Availability is defined in an unsupplied agreement | Present as Not Calculable and keep only the availability facts | None |
| MINOR | CP-2 | Cash coverage of a repeat of FY2025 outcome (1.2x) | Single-point illustration, not causal or time-aware; FY2025 figure is before insurance proceeds in investing | None | Keep labelled illustrative or replace with a time-aware downside | None |
| OBSERVATION | CP-1 | Adjusted EBITDA as the leverage denominator | Company definition; deducts the unrealized derivative loss and excludes insurance gains | Reported EBITDA differs materially | Keep EBITDA and Adjusted EBITDA side by side, as CP-1 does | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1A, CP-2 | Hydrogen plants parent note and its security | Purchase agreement, note and security documents | Q2 and Q3 reports describe the transaction differently | Supply the documents; keep as a gap | Required before any collateral view |
| GAP | CP-1, CP-1A | Ranking of the revolver, the unsecured notes and non-guarantor subsidiaries | Indentures and credit agreement | Described in the notes only | Supply the documents | Required for any legal reading |
| GAP | CP-1 | Springing covenant 1.0x fixed charge coverage below an availability trigger | Executed credit agreement | Definitions not supplied | Supply the agreement | Required for headroom |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| OBSERVATION | All modules | No market, ranking or relative-value claim is made; no instrument recommendation or recovery conclusion appears | Prices, spreads, current ratings | Outside the minimum source pack by design | Add market modules only with sourced market data | The committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR (closed) | CP-0, CP-1 | CP-0 listed only rates, fees, defaults and indemnification as consistent with the prior revolver agreement; the Q3 sentence also covers covenants | CP-1 states the correction; CP-0 is unchanged | Keep the correction stated | None; resolved |
| MINOR (closed) | CP-0, CP-1 | CP-0 recorded no borrowing base figure supplied; the 10-K prints a facility table with availability 2,296.6 | CP-1 states the correction | None further | None; resolved |
| OBSERVATION | CP-1, CP-2 | Issuer principal 1,850.0 against parent total debt 2,118.4 remains unexplained | All handoffs keep the perimeters apart | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | Reported position and structure are traceable; legal terms, the hydrogen plants note and a through-the-cycle view are not; review is a self-review | Supply the documents and an independent review | Committee status Requires More Work |
| OBSERVATION | CP-1, CP-1A, CP-2 | Duplication | The same refinancing facts appear in three handoffs; figures agree and each use is cited | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A | Consumer readiness judgments and per-row evidence quality | Not provided as a separate section | Add in a later run | CP-2 recorded the omission and capped confidence below High |
| OBSERVATION | All | Selector headings and reader summaries | All present; every accepted on attempt 1 | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-1 | Overstatement | Twelve-month facility expiry statement covers only committed facilities | Restrict wording | None | Open |
| QA-2 | MINOR | CP-1 | Definition | Leverage on principal rather than carrying value; both bases printed | Show both bases | None | Open |
| QA-3 | MINOR | CP-1 | Covenant inference | Springing test reading from rounded availability | Present as Not Calculable | None | Open |
| QA-4 | MINOR | CP-1A | Method duty | No readiness judgments or per-row evidence quality | Add later | None | Open |
| QA-5 | MINOR | CP-1 | Lineage | Table rows cite chunks without quotations | Add quotations | None | Open |
| QA-6 | MINOR | CP-2 | Illustration | Cash coverage illustration not time-aware | Keep labelled or replace | None | Open |
| QA-7 | MINOR | CP-0, CP-1 | Consistency | Covenant wording and borrowing base statement corrected by CP-1 | None further | None | Closed |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Every double-quoted phrase after a source label in CP-0, CP-1 and CP-1A was searched on the chunk it cites; CP-2 carries no quotation | 172 spans parsed (55, 25 and 92); all present; one span was split by a quotation mark inside the quoted sentence and was checked by hand |
| Q2 | Metric recomputation | Inputs parsed from the cited chunks of the source text, not retyped; LTM, discrete quarters, ratios, net debt, cash interest and capital outlay recomputed | 42 of 42 equal to CP-1 and CP-2 |
| Q3 | Tie-outs | Debt tables re-added at five dates and carrying value rebuilt, EBITDA and Adjusted EBITDA reconciliations re-added for six periods, income statement bridges, quarter sums, cash roll-forwards, balance sheet totals, lease sums, insurance and parent flow sums | 45 of 45 equal, with each input found on its cited chunk |
| Q4 | Figure consistency | Every number in CP-2 searched in CP-1, CP-1A or CP-2's own calculations; every number in each reader summary searched in its handoff body | No number found missing |
| Q5 | Non-derived figures | Every decimal figure in CP-1 and CP-1A outside Calculations searched in the source text | Only derived or restated amounts were absent, for example sums, LTM values and rounded narrative amounts |
| Q6 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:3,Calculated:3,Analyst Inference:1,Insufficient Information:2" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:6` | score = clamp((0.6 x 67.78 + 0.4 x 100) x 0.7 - 18) = 38.47, rounded to 38; band Insufficient Information; qa_status Passed |

The score is low because two of nine material claims are correctly labelled gaps, one is an inference, the source gate is partial and six minor findings are open. It does not indicate a defect in the reported figures.

## Gaps

- G1 Critical for any collateral or covenant view: the executed financing documents and the hydrogen plants note terms are not supplied.
- G2: liquidity is a rounded narrative and cannot be rebuilt.
- G3: no through-the-cycle or forward earnings case, so the trailing earnings cannot be read as run-rate.
- G4: Martinez and Chalmette outcomes are unquantified.
- G5: no independent review; this module was written by the host that wrote the handoffs.
- QA state: `qa_status` Passed, Confidence Score 38, band Insufficient Information, `committee_status` Requires More Work.

## Next module

Report delivery: carry `qa_status` Passed, Confidence Score 38, committee status Requires More Work, and the critical gap on the legal documents and the hydrogen plants note. An independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find. Sourcing: fetch the executed indentures, the amended revolving credit agreement and the hydrogen plants agreement and note, then rerun the affected modules in a new run folder.
