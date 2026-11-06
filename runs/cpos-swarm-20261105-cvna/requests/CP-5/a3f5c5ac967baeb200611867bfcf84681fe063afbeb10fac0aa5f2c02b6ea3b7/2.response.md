## Request

This module validates the evidence trace and research integrity of the CARVANA CO. analysis as of 2026-11-05 (pathway credit_snapshot, current period Q3 2026, prior period FY2025, USD). It checks whether each material claim in the source readiness, financial base, business context and credit synthesis handoffs rests on the evidence it names, and whether the handoffs tell one consistent story. It does not change the underlying credit conclusion.

## Sources

### Issuer sources re-opened for this validation

| Label | Exact source name | sha256 |
| --- | --- | --- |
| 10-K FY2025 | 10-K_2025-12-31_cvna-20251231.htm.jsonl | e28106ced83e487c2b18b6b610810086a1c332c7b8604f85efce9667b5e6a76a |
| 10-Q Q1 2026 | 10-Q_2026-03-31_cvna-20260331.htm.jsonl | 8d6ff7213869775e0ae3673fa4f3f8504cd246dbeeab2abdd24aff1860443100 |
| 10-Q Q2 2026 | 10-Q_2026-06-30_cvna-20260630.htm.jsonl | 4b43d425f11176a90828e0a1b668c0134d6d4d593beed8283823a525740b768c |
| 10-Q Q3 2026 | 10-Q_2026-09-30_cvna-20260930.htm.jsonl | 2940535c20dfe242e3d91621f5af16ca08b2dcda177838339ceb7be2805a2b78 |
| EX-99.1 Q1 2026 | EX-99.1_2026-04-29_ex99_1q12026.htm.jsonl | 7e7abd08434c84563cd9ee9bcfd3c51c356bc5d08b4e44ad4a2ea187eaea5514 |
| EX-99.1 Q2 2026 | EX-99.1_2026-07-29_ex99_1q22026.htm.jsonl | c4afe91551db432e6e87ceefff8a20a7648db1422c05df5d4cc9109c7c95c8e2 |
| EX-99.1 Q3 2026 | EX-99.1_2026-10-28_ex99_1q32026.htm.jsonl | 77eff687ed065288e545b6eb14e96f0cbf7ef280db37fa826fb72985e87a5e82 |

The run settings source (context, sha256 3b0d728dae64d48f4491be2af6d53653b4803495916d71df1f3f2f764a94f8be) holds dated settings only and is not issuer evidence.

### Supplied handoffs

| Module | sha256 | Scope reviewed |
| --- | --- | --- |
| CP-0 | 31dc2d6ecc7a5018db04d0b90efc3543deb94915148b1edcb8651234beedbcdf | Source readiness, entity roles, gap register |
| CP-1 | 4ef8f715c899f1915a393172033b3fb40237f7d9ecafdb8bce537094028ffbf3 | Financial base, chart tables, instrument and liquidity tables, calculations |
| CP-1A | a5ea306dff2d8225beff86753d4f17e13f65167966a1c42cb4f68ef5725ddd14 | Business and transaction context, ownership, governance behaviour |
| CP-2 | cf6d615563aa800f8ccd38de20222afd2c70bd755010da8cedd5cb359c11c9bd | Credit synthesis built on the above |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis traces well to the filings: all 248 cited quotes were found on their cited pages and every derived figure recomputed. Two material issues restrict committee use: a stale maturity chart and missing financing documents. | Medium | Quotes were checked as extracted text, not against filing images, and legal claims rest on issuer descriptions. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every quote and derived figure reproduced from the sources, and figures agree across the four handoffs. | The leverage, cover and liquidity figures can be relied on for the stated definitions. | High |
| The maturity chart uses the schedule printed for December 31, 2025, which still includes redeemed notes. | A committee reading the chart would see a 2030 maturity that no longer exists. | High |
| Ranking, guarantor, basket and control claims rest on issuer descriptions, not executed documents. | Protections and priming risk cannot be confirmed. | High |
| Five minor points: labels, a locator, the debt basis, one open conflict and text-only checking. None changes a figure. | Disclosure fixes only. | High |

### Evidence trace view

The analysis of Carvana is traceable enough for a restricted committee use but not for a clean one. The strongest support is mechanical: every cited quote was found verbatim on its cited page, the derived figures recomputed exactly, and the CP-1, CP-1A and CP-2 figures agree with one another. The weakest point is evidential: the maturity chart still shows the schedule printed before the August 2026 refinancing, including the 2030 Senior Secured Notes that were redeemed, and legal structure, guarantor perimeter, debt baskets and control limits are described only as the issuer describes them because no executed document is in the pack. Two issues are Material and five are Minor, with none Critical. Supplying the financing documents and rebuilding the maturity chart would lift the restriction.

### Traceability summary

| Area | Result | Basis |
| --- | --- | --- |
| Quotes and locators | 248 of 248 found on the cited page | Re-run against the source text |
| Derived figures | All recomputed, all match | Calculations below |
| Cross-module figures | Agree across four handoffs | Identity check below |
| Conflicts | One logged, unresolved, no figure effect | Accrued interest, 1 against 4 |
| Subsequent events | Flagged as dated, not blended | October 2026 extension |
| Legal and structural claims | Issuer description only | Issues I-02 |
| Material issues | 2 | I-01, I-02 |
| Minor issues | 5 | I-03 to I-07 |

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 5. Committee Use: Restricted.

The figures and quotes are sound, but the maturity chart is stale (I-01) and the legal and control claims lack executed documents (I-02), so committee use is restricted until those are disclosed or fixed. The Material issues must be disclosed with any committee use of the leverage, maturity or protection conclusions. committee_status: Restricted; qa_status: Restricted. No numeric confidence score is stated because the scoring script is not available in this run.

### Independent checks performed

1. Locators: all 248 bracket citations in the three source-citing handoffs (48 in CP-0, 119 in CP-1, 81 in CP-1A) were re-run as exact-substring searches on the cited page of the cited source; none failed. CP-2 cites no source text by design and relies on the other handoffs.
2. Claim support: for each material claim the cited quote was read for whether it states the claim, not just whether it exists. Weak cases are listed in the appendix (I-04).
3. Recalculation: every derived figure used in CP-2 was recomputed from the cited inputs; results are in `## Calculations`.
4. Identity: each figure repeated in CP-2 was compared with the same figure in CP-1 or CP-1A for value, unit, period and perimeter. All matched except for missing period or date labels (I-03).
5. Perimeter: the debt, EBITDA and cash figures are for Carvana Co. and subsidiaries consolidated. Carvana is a retailer rather than a finance company, but 1,125 of asset-based financing (floor plan, financing of retained securitization interests, real estate and fleet financing) is separated from corporate funded debt of 4,036 in CP-1 and used that way in CP-2.
6. Subsequent events: the October 2026 extension of one receivable facility is flagged as a subsequent event in CP-1 and CP-1A and is not blended into September 30 facts.

### Analytical appendix — complete canonical registers

#### T5B.1 Source document register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_cvna-20251231.htm.jsonl | High: audited filing | FY2025 | Carvana Co. and subsidiaries, consolidated | Statements, debt note with maturities, liquidity, related parties, risk factors | Text extraction, no fidelity review | CP-1, CP-1A |
| S2 | 10-Q_2026-03-31_cvna-20260331.htm.jsonl | High: unaudited filing | Q1 2026 | Same | Quarter statements, debt, liquidity, EBITDA reconciliation | Cash flow year-to-date only | CP-1 |
| S3 | 10-Q_2026-06-30_cvna-20260630.htm.jsonl | High: unaudited filing | Q2 2026 and six months | Same | Same plus post-split share data | Same | CP-1 |
| S4 | 10-Q_2026-09-30_cvna-20260930.htm.jsonl | High: unaudited filing | Q3 2026 and nine months | Same | Full debt, liquidity, refinancing, swap, related parties, claims outside debt | No post-refinancing maturity table | CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-29_ex99_1q12026.htm.jsonl | Medium: management letter | Q1 2026 | Same | Narrative, statements, liquidity table | Management Language in narrative | CP-1 |
| S6 | EX-99.1_2026-07-29_ex99_1q22026.htm.jsonl | Medium: management letter | Q2 2026 | Same | Same | Same | CP-1 |
| S7 | EX-99.1_2026-10-28_ex99_1q32026.htm.jsonl | Medium: management letter | Q3 2026 | Same | Same plus outlook and 2027 reporting change | Forecast items unreconciled | CP-1, CP-1A |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage of 1.91x on LTM Adjusted EBITDA, net 0.80x | CP-1 | Debt note, finance lease table, EBITDA reconciliation, cash | Sets debt capacity on the company measure | Core leverage reading | [10-Q Q3 2026, page:21, "Total debt 5,161 4,976"]; [10-Q Q3 2026, page:77, "Adjusted EBITDA $ 800 $ 637 $ 2,241 $ 1,726"] | Company-defined EBITDA; LTM derived |
| 2 | Earnings quality: loan sale gains 48.4% of nine-month Adjusted EBITDA | CP-1, CP-2 | Cash flow statement gain line and reconciliation | Gains depend on loan buyers; cash conversion lags | Key weakness | [10-Q Q3 2026, page:6, "Gain on loan sales (1,084) (878)"] | Gain is recognised at sale; cash arrives via proceeds |
| 3 | Liquidity of cash plus borrowing-base availability with short-dated lines | CP-1 | Liquidity table and facility paragraphs | Availability is collateral-limited; most commitments mature within twelve months | Funding risk | [10-Q Q3 2026, page:78, "Availability under short-term revolving facilities 2,071 2,052"] | No letters of credit found; renewals not supplied |
| 4 | Control and related-party dependence | CP-1A | Risk factor, related-party note | Control over debt incurrence and distributions; revenue chain through DriveTime | Governance and leakage risk | [10-K FY2025, page:55, "approximately 83% of the voting power of our outstanding capital stock"] | Agreements not supplied; voting date is December 31, 2025 |
| 5 | August 2026 refinancing and rate exposure | CP-1, CP-1A | Debt note, swap note | Debt-neutral swap of notes for floating-rate loan; hedge ends July 31, 2028 | Refinancing and cost | [10-Q Q3 2026, page:52, "terminates on July 31, 2028"] | Post-refinancing maturity table not printed |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt including finance leases 5,261 and leverage 1.91x | CP-1 | Debt note total, lease table, reconciliation | Yes | High | Derived | Supported | High | Traced and recomputed |
| Interest cover 5.88x on LTM cash interest 468 | CP-1 | Supplemental cash flow notes in four filings | Yes | High | Derived | Supported | High | Traced and recomputed |
| Liquidity: cash 3,049, availability 2,071, commitments 5,600 | CP-1 | Liquidity table and facility paragraphs | Yes | High | Supported | Supported | High | Traced |
| Maturity chart for 2026 to thereafter | CP-1 | 10-K principal maturities table | Yes | High | Supported | Supported but stale | Medium | Traced; stale (I-01) |
| Loan sale gains 48.4% of Adjusted EBITDA | CP-1, CP-2 | Cash flow statement line and EBITDA reconciliation | Yes | High | Derived | Supported | High | Traced and recomputed |
| DriveTime commissions 21.2% of other revenue and 8.4% of gross profit | CP-1A, CP-2 | Related-party note and income statement | Yes | High | Derived | Supported | Medium | Traced and recomputed |
| Ally 41.0% of principal sold | CP-1A, CP-2 | Note 7 sale volumes in rounded billions | Yes | High | Derived | Supported, approximate | Medium | Traced and recomputed |
| Garcia Parties about 83% of voting power | CP-1A, CP-2 | 10-K risk factor | Yes | High | Supported | Supported, date missing in CP-2 | Medium | Traced (I-03) |
| Creditor-adverse behaviour not found since 2023 | CP-1A | Absence in documents read | No quote possible | Medium | Inferred | Partly supported | Low | Gap: 2023 terms not supplied |
| Fundamental credit view: sound but market-dependent | CP-2 | CP-1 and CP-1A rows | Yes: handoff basis | Medium | Inferred | Supported with limits | Medium | Traced to handoff rows |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt note total | runs/cpos-swarm-20261105-cvna/source-text | 10-Q_2026-09-30 | S4 | page:21, Note 9 | CP-1 Financials | Table figure | High | Ties to balance sheet within 1 |
| Adjusted EBITDA reconciliation | same | 10-Q_2026-09-30 | S4 | page:77, MD&A | CP-1 Financials | Table figure | High | Company-defined |
| Prior-year Adjusted EBITDA | same | 10-K_2025-12-31 | S1 | page:80, MD&A | CP-1 chart tables | Table figure | High | FY2025 |
| Principal maturities | same | 10-K_2025-12-31 | S1 | pages 140 to 141, Note 9 | CP-1 maturities chart | Table figure | High | Stale after refinancing |
| Term loan terms | same | 10-Q_2026-09-30 | S4 | pages 26 to 27, Note 9 | CP-1 instruments | Narrative | High | Issuer description |
| Swap terms | same | 10-Q_2026-09-30 | S4 | page:52, Note 17 | CP-1 instruments | Narrative | High | Partial-term hedge |
| Liquidity table | same | 10-Q_2026-09-30 | S4 | page:78, MD&A | CP-1 liquidity | Table figure | High | Availability, not commitment |
| Related-party commissions | same | 10-Q_2026-09-30 | S4 | page:15, Note 6 | CP-1A calculations | Narrative figure | High | Nine months |
| Control and voting | same | 10-K_2025-12-31 | S1 | page:55, Item 1A | CP-1A ownership | Narrative | High | As of December 31, 2025 |
| Outlook and 2027 reporting change | same | EX-99.1_2026-10-28 | S7 | page:3 | CP-1A governance | Narrative | Medium | Management Language |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA 2,752 | CP-1, CP-2 | FY2025 2,237; nine months 2,241 and 1,726 | 2,237 + 2,241 - 1,726 | Recomputed, matches | Supported | High | Leverage denominator | [10-Q Q3 2026, page:77, "Adjusted EBITDA $ 800 $ 637 $ 2,241 $ 1,726"] |
| Total debt 5,261 and net debt 2,212 | CP-1, CP-2 | Debt note 5,161; finance leases 100; cash 3,049 | 5,161 + 100; less 3,049 | Recomputed, matches | Supported | High | Leverage numerator | [10-Q Q3 2026, page:43, "Total lease liabilities $ 100 $ 9 $ 460 $ 469 $ 569"] |
| Leverage 1.91x and net 0.80x | CP-1, CP-2 | Above | 5,261 / 2,752; 2,212 / 2,752 | Recomputed, matches | Supported | High | Headline metric | See Calculations |
| LTM cash interest 468; cover 5.88x | CP-1, CP-2 | 336 + 443 - 311 | 2,752 / 468 | Recomputed, matches | Supported | High | Coverage | [10-Q Q3 2026, page:54, "Cash payments for interest $ 443 $ 311"] |
| Undrawn commitments 5,529 | CP-1 | Commitments 5,600; drawn 71 | 1,500 - 71 + 4,100 | Recomputed, matches | Supported | High | Liquidity | [10-Q Q3 2026, page:23, "$71 million outstanding under the Floor Plan Facility"] |
| Loan sale gains 48.4% | CP-1, CP-2 | 1,084; 2,241 | 1,084 / 2,241 | Recomputed, matches | Supported | High | Earnings quality | [10-Q Q3 2026, page:6, "Gain on loan sales (1,084) (878)"] |
| Operating cash flow 40.2% of EBITDA; free cash flow 734 | CP-1, CP-2 | 900; 2,241; 166 | 900 / 2,241; 900 - 166 | Recomputed, matches | Supported | High | Cash conversion | [10-Q Q3 2026, page:6, "Purchases of property and equipment (166) (96)"] |
| DriveTime 21.2% and 8.4%; Ally 41.0% | CP-1A, CP-2 | 349; 1,646; 4,176; 5.7, 3.7, 4.5 billion | 349 / 1,646; 349 / 4,176; 5.7 / 13.9 | Recomputed, matches (Ally approximate) | Supported | Medium | Concentration | [10-Q Q3 2026, page:15, "the nine months ended September 30, 2026 and 2025, the Company recognized $349 million"] |
| Debt on balance sheet carrying basis 5,228 | This module | 71 + 283 + 4,874 | Sum | Computed here | Supported | High | Canonical debt basis | See Calculations |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Maturity profile | Chart shows the December 31, 2025 schedule, whose 2030 bucket includes the 2030 Senior Secured Notes redeemed in August 2026, and excludes the term loan | Supported but stale | Misstates the post-refinancing wall | Rebuild from instrument terms or a post-refinancing table | CP-1 chart table |
| Material | Pari passu ranking, guarantors, baskets, control limits | Rest on issuer descriptions; no executed document | Inferred from description | Protections cannot be confirmed | Obtain indentures and credit agreement | CP-1, CP-1A, CP-2 |
| Minor | Garcia Parties voting share | CP-2 omits the December 31, 2025 date; Ally share omits nine months 2026 | Supported, label missing | Period mixing risk | Add period labels | CP-2 |
| Minor | Auditor identity | CP-1A row cites one page for the firm name and the PCAOB identifier (on page:96) | Supported, locator imprecise | Citation precision | Cite both pages | CP-1A profile |
| Minor | Creditor-adverse history | Absence of an action in documents read is not a source quote | Inferred | Cannot prove a negative | Keep as Insufficient Information for 2023 | CP-1A, CP-2 |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Locator traceability | Strong | 248 of 248 quotes found on the cited page | A reviewer can open each span | Facts are checkable | None |
| Calculation reproducibility | Strong | Every derived figure shows formula and inputs and recomputed | Errors would surface on recompute | Ratios can be relied on for the stated definitions | None |
| Definition consistency | Adequate | Principal basis used in CP-1 against balance sheet carrying value as the canonical basis; delta 33, ratios differ by 0.01x at most | Basis choice could shift ratios | No change to conclusions | Disclose both bases (I-05) |
| Conflict handling | Adequate | Accrued interest 1 against 4 logged in three handoffs, unresolved | Unreconciled figure could leak | No figure uses it | Resolve with the issuer if needed |
| Subsequent events | Strong | October 2026 extension flagged with date | Blending would misstate September 30 liquidity | None | None |
| Legal evidence | Weak | No executed documents | Protections unverified | Priming and basket risk unmeasured | Supply documents |
| Management language | Strong | Letter statements tagged and not adopted | Promotional text could be read as fact | None | None |
| Period labelling | Adequate | Two missing labels in CP-2 | Mixed periods in one sentence | Minor misread risk | Add labels (I-03) |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| GL-1 | Executed financing documents | Indentures, term loan agreement, floor plan agreement | Ranking, baskets, covenants, guarantors | Legal claims restricted | Caps confidence at Medium | Filed exhibits |
| GL-2 | Post-refinancing maturity schedule | Table after August 2026 | Maturity wall | Chart stale | Material issue | Next filing or issuer |
| GL-3 | Covenant levels and headroom | Floor plan and notes covenants | Headroom test | Not calculable | Limits liquidity conclusion | Credit agreements |
| GL-4 | Ratings and market data | Ratings, quotes | Relative value, not this run | None for this run | None | Ratings and market sources |
| GL-5 | 2023 exchange terms | FY2023 filing | Creditor-adverse history | Governance row | Low confidence on that row | FY2023 10-K |
| GL-6 | Related-party and tax receivable agreements | Agreements | Leakage capacity | Governance rows | Medium confidence | Filed exhibits |

#### T5.1 Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/2fa90fb0.../1.response.md; run cvna-2026-11-05-credit_snapshot-host | Source readiness | High | Six H2 headings in order; entity and date present | Passed | Gap G10 and G9 updated by CP-1 |
| CP-1 | requests/CP-1/df96103f.../1.response.md; same run | Financial base | High | Six H2 headings; selectors present | Restricted | Stale maturity chart (I-01) |
| CP-1A | requests/CP-1A/5ba02de5.../1.response.md; same run | Business and transaction | High | Six H2 headings; selectors present | Restricted | Legal capacity unverified (I-02) |
| CP-2 | requests/CP-2/2216d2a6.../1.response.md; same run | Credit synthesis | Medium | Six H2 headings; selectors present | Restricted | Period labels (I-03) |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Auditor row in Company profile | Supported | One locator for two facts | Cite page:96 for the PCAOB identifier | None |
| Minor | CP-2 | Voting share and Ally share | Supported | Period labels missing | Add December 31, 2025 and nine months 2026 | None |
| Minor | CP-1A | Governance table, tax receivable payments | Supported | Cites the 2026 payment only for a 2025 and 2026 statement | Cite the FY2025 cash flow line | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Leverage uses principal plus finance leases (5,261) | Canonical basis is balance sheet carrying value (5,228); delta 33 | None | Show both bases | None; ratios 1.91x and 1.90x |
| Minor | CP-1, CP-1A, CP-2 | Accrued interest on 2026 redemption | Not used in any figure | 1 in Note 9 against 4 in MD&A | Resolve with issuer | None |
| Minor | CP-1 | Adjusted EBITDA includes loan sale gains and excludes tax receivable expense | Company definition, disclosed | None | None beyond disclosure | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A | Term loan ranks pari passu with 2031 secured notes on first-priority collateral | Credit agreement, indenture, intercreditor terms | Only the Note 9 description | Obtain documents | Required before any lien conclusion |
| Material | CP-1, CP-1A | Guarantors are domestic restricted subsidiaries; ADESA excluded for unsecured notes only | Guarantor schedule, indentures | No named guarantors | Obtain schedule | Required |
| Material | CP-1A, CP-2 | Control group's capacity to incur debt or distribute is not constrained | Indenture covenants, charter | Baskets not supplied | Obtain documents | Required |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | CP-0, CP-1, CP-1A, CP-2 | No market or relative value claim is made, as required | Ratings and quotes are outside this run | Context fields empty | None for this run | Relative value belongs to a later module |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1 | CP-0 left the ADESA treatment under secured indentures as not stated; CP-1 states the guarantor wording | CP-1 says plainly that it corrects this | None; handoffs are immutable | Follow CP-1 |
| Minor | CP-0, CP-1 | CP-0 asked to recheck the tax receivable balances; CP-1 tied the Q3 roll-forward only | Q1 and Q2 not rolled forward | Roll forward in a later run | None for figures |
| Minor | CP-1, CP-1A, CP-2 | Accrued interest conflict carried unresolved | Same wording in each | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-1 | Materiality | Stale maturity chart would be read first | Rebuild or footnote | Restrict use of the maturity view |
| Material | CP-1, CP-1A, CP-2 | Committee readiness | Legal and control claims unverified | Disclose with any committee use | Restricted |
| Minor | CP-2 | Duplication | Key findings repeat CP-1 figures as intended | None | None |

#### T5.8 Handoff structure and export audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| None | CP-0 to CP-2 | Headings, sources and handoff hashes | None found: six H2 headings in order, issuer named, as-of date stated, sources with hashes, handoffs with hashes | None | None |
| None | CP-1 | Chart selector tables | Present once each with required headers | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | Material | CP-1 | Stale evidence | Maturity chart is the pre-refinancing schedule; its 2030 bucket still holds the redeemed 2030 Senior Secured Notes | Rebuild or disclose | Restricts maturity use | Open |
| I-02 | Material | CP-1, CP-1A, CP-2 | Legal evidence | Ranking, guarantor, basket and control claims rest on descriptions | Obtain executed documents | Restricts protection use | Open |
| I-03 | Minor | CP-2 | Period label | Voting share and Ally share lack dates | Add labels | None | Open |
| I-04 | Minor | CP-1A | Locator | Auditor row cites one page for two facts | Cite page:96 | None | Open |
| I-05 | Minor | CP-1 | Definition | Principal basis against carrying basis, delta 33 | Show both | None | Open (both shown here) |
| I-06 | Minor | CP-1, CP-1A, CP-2 | Conflict | Accrued interest 1 against 4 unresolved | Resolve with issuer | None | Open |
| I-07 | Minor | All | Extraction fidelity | Text extraction with no image check of tables | Spot-check images | None | Open |

## Calculations

All inputs are quoted figures from the cited handoffs or sources, in US$ millions.

- Balance sheet carrying basis for debt (short-term revolving facilities plus current portion plus long-term debt): December 31, 2025, 58 + 227 + 4,830 = 5,115; September 30, 2026, 71 + 283 + 4,874 = 5,228. Inputs: [10-Q Q3 2026, page:2, "Short-term revolving facilities 71 58"]; [10-Q Q3 2026, page:2, "Current portion of long-term debt 283 227"]; [10-Q Q3 2026, page:2, "Long-term debt, excluding current portion 4,874 4,830"].
- Gross delta to the principal basis used in CP-1: 5,133 - 5,115 = 18 at December 31, 2025 and 5,261 - 5,228 = 33 at September 30, 2026.
- Leverage on the carrying basis: December 31, 2025, 5,115 / 2,237 = 2.29x and net (5,115 - 2,327) / 2,237 = 1.25x; September 30, 2026, 5,228 / 2,752 = 1.90x and net (5,228 - 3,049) / 2,752 = 0.79x. These agree with CP-1 within 0.01x (1.91x and 0.80x), so the basis does not change any conclusion.
- Recomputation of CP-1 and CP-1A figures: LTM Adjusted EBITDA 2,421, 2,589 and 2,752; total debt 5,133, 5,170, 5,251 and 5,261; ratios 2.29x, 2.14x, 2.03x and 1.91x; cover 6.66x, 6.13x, 6.55x and 5.88x; commitments 5,529; loan sale gains 48.4%; operating cash flow 40.2% of Adjusted EBITDA; free cash flow after property purchases 734; DriveTime 21.2% and 8.4%; Ally 41.0%. All matched the handoffs.

## Gaps

- Executed financing, related-party and tax receivable documents are Not supplied; legal and structural claims are issuer descriptions (I-02). Covenant levels and headroom are Not calculable.
- No post-refinancing maturity schedule; the chart is stale (I-01).
- Quotes were verified against extracted text; no filing image or table fidelity review was done (I-07).
- The numeric confidence score is not stated because the scoring script is not available in this run; the qualitative status is Restricted.
- Ratings and market data are Not supplied and are outside this run.

## Next module

No further module is requested in this run. A reader using the report should apply the two Material disclosures (stale maturity chart; unverified legal and control claims) and request the financing documents and a post-refinancing maturity table before relying on protection or maturity conclusions.
