# CP-5 — Evidence trace and research-integrity QA: Bally's Corp (baly)

## Request

- Issuer: Bally's Corp (the filings name "Bally’s Corporation", issuer id `baly`), as of 2026-11-05, information cutoff 2026-11-05, pathway `credit_snapshot`, reporting currency USD, run `baly-2026-11-05-credit_snapshot-host`.
- Scope: CP-5 traces the claims of CP-0, CP-1, CP-1A and CP-2 to the pinned sources and grades them (absorbed CP-5A phase). Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- Execution: host session. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.
- QA envelope: `qa_status` Passed; Confidence Score 43, band Low (from `confidence_score.py`, see Calculations); `committee_status` Requires More Work.
- Locators: `page:N` is the pinned source chunk, not the printed page.

## Sources

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_baly-20251231.htm.jsonl | 2416bb6463c147a405baaa3764d6b99dd0f04403aa6bd66a1af2136569a6e954 |
| 10-Q_2025-09-30_baly-20250930.htm.jsonl | 56bb4ccb0d42545489eded0e33ef5cc1b6e43986515a8c8a0964234c0c5a1ad2 |
| 10-Q_2026-03-31_baly-20260331.htm.jsonl | 4cf63f6c58a65fd25da3815352379f245d409f7447d9868c7381e2ae8ff65e16 |
| 10-Q_2026-06-30_baly-20260630.htm.jsonl | 972ae065bf1c6675d8214b94858dd8284ab57f02cd1acc546c671e0cb75a811b |
| EX-99.1_2026-03-16_ex991q42025earningsrelease.htm.jsonl | 409058f48783e9f5b7a8a00d5cc7ac8351ce41c9bc84bcf81e7c679d11a21bfd |
| EX-99.1_2026-05-18_ex991q12026earningsrelease.htm.jsonl | 7a189d9a918a76f21f04890e1c9f027b4cb34b6b08652098f8604b464b20f405 |
| EX-99.1_2026-08-14_ex991q22026earningsrelease.htm.jsonl | d7b82a85199a3932febed54513d2e10fb96188bb07713475fd80698b0568c17c |
| context | 49e5852827798fdbde43be3fcd478e45f6e9875c774c07cb1f9810d5a929f053 |

Supplied handoffs:

| Module | sha256 |
| --- | --- |
| CP-0 | e78906951f2c40cb4061b9e3feea4b5ce91ea92011923fb2276960d5a3adc0a6 |
| CP-1 | b0d407b2a44a391d85b9c2d55e319b7bcd4286ee61c05f22cd3ec3d9834794e8 |
| CP-1A | 1386e40b2e065e18f9281c455fe4927011fc9b3e45afc363833febc4176b895b |
| CP-2 | a16d8095b72e19deab06a7c6b32d23631d50397bd31499150e9fecd63e6ebf02 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The credit work is traceable to the filings for the position at June 30, 2026: recomputed figures match and no quotation is wrong. It is not traceable for covenant headroom or events after August 14, 2026. | Medium | The same reviewer wrote the work it checks, and the credit agreement, waiver and later filings are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 18 statement tie-outs and the recomputed last-twelve-month figures match the cited filings. | Leverage of 9.57x and interest cover of 1.15x can be relied on as arithmetic from filed figures. | High |
| Of 76 quoted spans, none is misquoted, and 70 sit on the cited page. | Reviewers can find the evidence; the rest carry minor locator slips. | High |
| Parent-level leverage and the October 2026 revolver headroom rest on inference, not on a reported figure. | Treat both as indicative signals until the credit agreement and later filings are supplied. | Medium |
| Five minor defects were found: wrong or missing page numbers, an overstated cash-access sentence and a warrant attribution. | None changes a conclusion, but each should be corrected in a rerun. | High |

### Evidence trace view

The analysis is traceable enough for a view of Bally’s financial position at June 30, 2026, and not for covenant headroom or anything after August 14, 2026. Every recomputed figure ties to the filings: last-twelve-month Adjusted EBITDA of USD 512.8 million, cash interest of USD 444.6 million, debt principal of USD 4,910.1 million, and 18 of 18 statement tie-outs. Of 76 quoted spans, none is misquoted. Of 12 material claims, 4 are Directly Sourced, 4 Calculated, 1 Assumption-Based, 1 Analyst Inference and 2 Insufficient Information. The critical provenance gap is the credit agreement, waiver and later filings: the waiver conditions and the October 2026 revolver reduction rest on one filing description. Remediation owner: the sourcing step. Five minor defects need no change to any conclusion.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_baly-20251231.htm.jsonl | High: filed annual report, audited; adverse internal control opinion | Successor February 8 to December 31, 2025; Predecessor January 1 to February 7, 2025; year 2024 | Bally’s Corporation, consolidated | Statements, debt note, Adjusted EBITDA reconciliation, business, ownership, risk factors | Text extraction; Successor and Predecessor periods not comparable | CP-0, CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2025-09-30_baly-20250930.htm.jsonl | High: filed interim report, unaudited | Quarter and nine months to September 30, 2025 | Same | September 30, 2025 balance sheet, debt, Q3 2025 Adjusted EBITDA | Predates the Intralot transaction | CP-1 |
| S3 | 10-Q_2026-03-31_baly-20260331.htm.jsonl | High: filed interim report, unaudited | Quarter to March 31, 2026 | Same | March 31, 2026 balance sheet, debt, waiver first described | Text extraction | CP-1 |
| S4 | 10-Q_2026-06-30_baly-20260630.htm.jsonl | High: filed interim report, unaudited | Quarter and six months to June 30, 2026 | Same | Statements, debt, going concern, waiver, liquidity, segments | Text extraction; unaudited | CP-0, CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-03-16_ex991q42025earningsrelease.htm.jsonl | Medium: issuer press release, preliminary | Q4 and full year 2025 | Same | Preliminary results, 10-K extension notice | Preliminary; the 10-K controls | CP-0, CP-1A |
| S6 | EX-99.1_2026-05-18_ex991q12026earningsrelease.htm.jsonl | Medium: issuer press release | Q1 2026 | Same | Q1 2026 segment results | Management characterisation | CP-1A |
| S7 | EX-99.1_2026-08-14_ex991q22026earningsrelease.htm.jsonl | Medium: issuer press release | Q2 2026 | Same | Segment results, strategy, rent cash payments | Management characterisation | CP-1, CP-1A, CP-2 |
| S8 | context | Run settings, not issuer evidence | As of 2026-11-05 | Run identity | Pathway, currency, dates | Not evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Going concern doubt and conditional covenant waiver | CP-0, CP-1, CP-1A, CP-2 | Filing states substantial doubt; lenders waived the covenant conditionally | Sets default risk and the horizon of the view | Decides whether any further analysis is current | S4 page:11, page:38, page:74 | Waiver terms and minimum liquidity level not supplied |
| 2 | Leverage 9.57x gross and 8.81x net; cover 1.15x | CP-1, CP-2 | Calculated from filed Adjusted EBITDA, cash interest, debt and cash | Debt service rests on refinancing | Core leverage and coverage metrics | S1 page:80, page:110; S4 page:37, page:60, page:6 | Perimeter and period mix; non-GAAP numerator |
| 3 | Liquidity trajectory and October 2026 revolver reduction | CP-1, CP-2 | Cash 390.2 and revolver availability 195.8 (USD million); commitments fall to about 319 | Runway is measured in quarters | Near-term default horizon | S4 page:2, page:5, page:33 | Events after August 14, 2026 not supplied; interpretation of the 319 figure |
| 4 | Two borrower groups and controlling sponsor | CP-1A, CP-2 | Intralot does not guarantee parent debt; sponsor holds 67.1% | Access to cash and support is uncertain | Structural position of creditors | S4 page:11, page:8; S1 page:66 | Guarantor list and intercompany restrictions not supplied |
| 5 | Fixed rent and uncommitted projects | CP-1, CP-1A, CP-2 | Sale-leaseback added rent; Bronx project funding not committed | Competes with debt service | Capital call risk | S4 page:39, page:70, page:44; S7 page:2 | Project funding terms not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Going concern doubt and waiver conditions | CP-0, CP-1, CP-2 | S4 page:11, page:38 | Yes | High | Directly Sourced | Supported | High | Traced, quotes on cited pages |
| Debt by instrument and principal total | CP-1 | S4 page:31, page:37 | Yes | High | Directly Sourced | Supported | High | Traced; total ties to printed schedule |
| Controlling sponsor ownership 67.1% | CP-1A | S1 page:66 | Yes | High | Directly Sourced | Supported | High | Traced |
| Intralot does not guarantee parent debt | CP-1A, CP-2 | S4 page:11 | Yes | High | Directly Sourced | Supported | High | Traced |
| Gross and net leverage | CP-1, CP-2 | S1 page:80, S4 page:37, page:60, page:2 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Interest cover and fixed charge cover | CP-1, CP-2 | S1 page:110, S4 page:6, page:48 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Liquidity and six-month free cash outflow | CP-1, CP-2 | S4 page:2, page:5, page:33 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Sale-leaseback rent yield | CP-1A | S4 page:39 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Revolver headroom after October 2026 | CP-2 | S4 page:33 | Yes | High; wording of the 319 figure | Assumption-Based | Supported as arithmetic | Low | Labelled arithmetic by CP-2 |
| Parent-level leverage 19.4x and 23.8x | CP-2 | S4 page:48 segment rows | Yes | High inputs; mapping to entities not stated | Analyst Inference | Supported as indicative | Low | Labelled indicative by CP-2 |
| Covenant headroom against the credit agreement | CP-1, CP-2 | Definitions and level not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Events after August 14, 2026 | CP-0, CP-1A, CP-2 | No source in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt principal 4,910,068 thousand at June 30, 2026 | /workspace/secdata/data/2026-11-05/packs/1747079-bally-s-corp-baly | 10-Q_2026-06-30_baly-20260630.htm.jsonl | S4 | page:37, Debt Maturities | CP-1 leverage chart | Reported | High | Sum of eleven instruments equals the printed total |
| Adjusted EBITDA six months 2026 247,318 thousand | same | 10-Q_2026-06-30_baly-20260630.htm.jsonl | S4 | page:60, MD&A reconciliation | CP-1 financials table | Issuer non-GAAP | Medium | Equals Q1 plus Q2 |
| Adjusted EBITDA FY2025 478,009 and 24,390 thousand | same | 10-K_2025-12-31_baly-20251231.htm.jsonl | S1 | page:80 | CP-1 financials table | Issuer non-GAAP | Medium | Successor plus Predecessor stub |
| Cash paid for interest six months 2026 220,037 thousand | same | 10-Q_2026-06-30_baly-20260630.htm.jsonl | S4 | page:6, supplemental cash flow | CP-1 interest cover | Reported | High | Matches |
| Going concern and waiver | same | 10-Q_2026-06-30_baly-20260630.htm.jsonl | S4 | page:11 and page:38, Notes 2 and 12 | CP-1, CP-1A, CP-2 | Reported | High | Quotes verified |
| Cash 390,184 thousand and revolver availability 195.8 million | same | 10-Q_2026-06-30_baly-20260630.htm.jsonl | S4 | page:2 and page:33 | CP-1 liquidity chart | Reported | High | Matches |
| Standard General 67.1% at February 28, 2026 | same | 10-K_2025-12-31_baly-20251231.htm.jsonl | S1 | page:66, risk factors | CP-1A company profile | Reported | High | Matches |
| Sale-leaseback consideration 700.0 million and added rent 56.0 million | same | 10-Q_2026-06-30_baly-20260630.htm.jsonl | S4 | page:39, Note 13 | CP-1A transaction summary | Reported | High | Matches |
| UK gaming tax 21% to 40% from April 1, 2026 | same | EX-99.1_2026-08-14_ex991q22026earningsrelease.htm.jsonl | S7 | page:3 | CP-1A operating model | Management claim | Medium | Labelled Management Language |
| Rhode Island leverage trigger 5.50 to 1.00 | same | 10-K_2025-12-31_baly-20251231.htm.jsonl | S1 | page:16, Item 1 | CP-1A company profile | Reported | High | Definition not supplied |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Last-twelve-month Adjusted EBITDA | CP-1 charts; CP-2 | FY2025 Successor and Predecessor, six months 2026, six months 2025 | FY2025 + six months 2026 − six months 2025 | Recomputed from parsed source rows: 512,810 equal | Supported | High | Denominator of every ratio | S1 page:80; S4 page:60 |
| Last-twelve-month cash interest | CP-1 charts; CP-2 | Same periods | Same | Recomputed: 444,640 equal | Supported | High | Cover | S1 page:110; S4 page:6 |
| Leverage and cover at four dates | CP-1 charts | Principal totals, unrestricted cash, LTM EBITDA | Debt / EBITDA; (debt − cash) / EBITDA; EBITDA / cash interest | Recomputed all 12 ratios equal | Supported | High | Core metrics | S1 page:170; S2 page:38; S3 page:48; S4 page:37 |
| Liquidity with Intralot revolver at an implied euro rate | CP-1 liquidity chart | Euro principal and USD carrying amount of the Intralot revolver and Greek Retail Bond | Euro amount × (USD / euro) | Recomputed equal; the rate is implied, not reported | Supported with assumption | Medium | Undrawn facilities | S4 page:31, page:37; S3 page:80 |
| Borrower-group split | CP-2 | Instrument principal | Parent 2,898,268; Intralot 2,011,800 | Recomputed equal | Supported | High | Structure | S4 page:31 |
| Indicative parent-level leverage | CP-2 | Segment EBITDAR; assumes Intralot-linked segments equal the Intralot group | Parent debt / (Adjusted EBITDA − B2B − B2C EBITDAR) | Recomputed 19.4x and 23.8x equal; assumption not verifiable from the set | Supported as indicative | Low | Structure risk | S4 page:48, page:60 |
| First lien sensitivity | CP-2 | First lien debt, consolidated cash, two EBITDA perimeters | (303,750 + 1,109,518 − 390,184) / EBITDA | Recomputed 2.0x and 8.4x equal; not a covenant test | Supported as sensitivity | Low | Covenant risk | S4 page:31, page:65 |
| Add-back share of Adjusted EBITDA | CP-2 | Five add-back rows | Sum / Adjusted EBITDA | Recomputed 43.0% and 53.5% equal | Supported | High | Earnings quality | S4 page:48 |
| Revolver after October 2026 | CP-2 | 319 commitments (interpreted), 303.75 drawn, 19.75 other usage | 319 − 303.75 − 19.75 | Recomputed (4.5) equal; interpretive | Supported as arithmetic | Low | Liquidity | S4 page:33 |
| Merger cash consideration check | CP-1A | 22,804,384 shares, USD 18.25 | Shares × price | Recomputed 416,180 equal | Supported | High | Sponsor behaviour | S4 page:4, page:5, page:8 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial source gate, 5 MINOR | Script formula | 43, band Low | Script output | High | QA envelope | confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 locators | Chicago master lease terms cited at page:69 (they are at page:70, with the 940.0 million also at page:40); segment revenue rows cited at page:48 (they are at page:47); three cash balances used in the leverage basis cells carry no locator of their own (S2 page:2, S3 page:2, S4 page:2) | Imprecise locator | A reader checking the page misses the figure; no misquotation | Cite exact pages in a rerun | CP-1 handoff |
| MINOR | CP-1A locators | Revenue streams and segment revenue cited at page:19 and page:48 (the disaggregation table is at page:20 and segment rows at page:47); 42.1% non-controlling interest cited at page:11 (it is at page:8); 555,751 thousand Queen consideration uncited in the governance bullet (page:6) | Imprecise locator | Slower verification; figures are correct | Cite exact pages | CP-1A handoff |
| MINOR | CP-1 liquidity row | States that Intralot cash and facilities are "not available to the parent group by guarantee"; page:11 says only that Bally’s Intralot does not guarantee the parent’s debt, and access to Intralot cash by the parent is not described | Overstated inference | Could understate group liquidity or mislead on cash access | Replace with: access not supplied | CP-1 handoff; CP-2 hedges it |
| MINOR | CP-1A dilution row | Attributes all 11,619,725 penny warrants to the Sinclair Framework Agreement; the 10-K shows 4,915,726 Sinclair penny warrants, 384,536 further penny warrants and 3,279,337 performance warrants, leaving part unattributed | Overstated attribution | Dilution source misdescribed | Attribute only what the 10-K shows | CP-1A handoff |
| MINOR | CP-1, CP-1A, CP-2 revolver | The filing says total availability "will be further reduced to approximately $319 million"; the handoffs read it as commitments, because current availability is 195.8 million; CP-2 labels the headroom arithmetic as indicative | Interpretation of source wording | The headroom of about zero depends on this reading | Confirm in the credit agreement | CP-1, CP-1A, CP-2 handoffs |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves on the cover and in the period labels | A wrong document would change every figure | None found | None |
| Quotation accuracy | Strong | 76 quoted spans parsed; 70 on the cited page; none misquoted; 6 not tied to a locator in the same sentence (4 registrant-name phrases, 1 search term, 1 correct capitalised locator) | A misquote would misstate a covenant or going concern fact | None found | None |
| Locator precision | Adequate | Five MINOR findings across two handoffs | Slower checks; risk of a misplaced citation | None on conclusions | Exact page locators |
| Calculation reproducibility | Strong | Inputs re-parsed from source text: 4 of 4 LTM EBITDA values and 4 of 4 LTM cash interest values equal; 12 of 12 ratios equal; 18 of 18 tie-outs equal | Calculation errors would move leverage | None found | None |
| Cross-module consistency | Strong | Figures in CP-1A and CP-2 equal CP-1; the euro revolver conflict is preserved, not smoothed; CP-1A states the CP-1 page correction | Inconsistent figures mislead a committee | None found | None |
| Inference labelling | Adequate | Parent-level leverage, first lien sensitivity and revolver headroom are labelled indicative | Unlabelled inference would pass as fact | Low-confidence signals drive the structure view | Obtain entity-level data |
| Reviewer independence | Weak | The host wrote and checked the handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Credit agreement, amendments, conditional waiver and minimum liquidity level | Executed documents and compliance certificate | Covenant headroom and the point of waiver failure cannot be tested | CP-2 top risk and covenant view | Holds the view to the filing description; first lien sensitivity swings between 2.0x and 8.4x | Credit Agreement, Amendments No. 3 to No. 5, Conditional Waiver |
| G2 | Events after August 14, 2026 | Later 8-Ks, the Fifth Amendment terms, the Q3 2026 report if filed | The October 2026 revolver reduction, financings and equity sale outcomes are unknown | Currency of the whole view | Lowers confidence in any statement about the as-of date | EDGAR filings to 2026-11-05 |
| G3 | Parent group versus Bally’s Intralot cash, earnings and intercompany restrictions | Guarantor list, entity-level accounts | Parent-level leverage and cash access are indicative only | CP-2 structure risk | Caps lineage at Analyst Inference | Guarantor schedules, Intralot accounts |
| G4 | Rhode Island regulatory leverage definition and status | Regulatory Agreement, compliance certificate | Payment and incurrence limits may apply | CP-1A and CP-2 regulatory risk | Moderate | Regulatory Agreement |
| G5 | Sponsor intentions | Sponsor statements, proxy statement | Decisive for the outcome | CP-2 credit view | Moderate | Proxy statement, sponsor disclosures |
| G6 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / baly-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed, no defect found | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 2 / same run | Statements, LTM, debt, liquidity, maturities | High | Six headings; attempt 1 refused for three reader-summary figures not found in the body, attempt 2 accepted | Passed with three MINOR findings | All metrics recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, ownership, transactions, governance | High | Six headings; accepted | Passed with two MINOR findings | States the CP-1 locator correction |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Passed with one MINOR finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Chicago lease terms, segment revenue rows, cash balances | Supported | Wrong page or missing locator | Cite page:70, page:47 and the balance sheet pages | None |
| MINOR | CP-1A | Revenue streams, segment revenue, 42.1%, 555,751 thousand | Supported | Wrong page or missing locator | Cite page:20, page:47, page:8, page:6 | None |
| MINOR | CP-1A | Penny warrants attribution | Partly supported | Overstated attribution to Sinclair | Attribute only what the 10-K shows | None |
| MINOR | CP-1 | Intralot cash not available to the parent by guarantee | Partly supported | Inference beyond page:11 | Say access is not supplied | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None found as a defect | CP-1 | LTM sums add a Predecessor stub to Successor periods | Stated in CP-1 as not like-for-like | Not a value conflict | Keep labels | None |
| None found as a defect | CP-1, CP-2 | Adjusted EBITDA is after rent; operating leases excluded from debt | Consistent with the issuer definition; fixed charge cover shown separately | None | Keep both views | None |
| None found as a defect | CP-1 | Dec 31, 2025 Intralot undrawn: 10-K says 190.0 million euros, Q1-26 10-Q says 160.0 million euros | CP-1 used 160.0 and disclosed the alternative | Preserved, not reconciled | Confirm commitments | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1, CP-2 | Waiver conditions, covenant levels and reinstatement mechanics | Credit Agreement, Amendments, Conditional Waiver | Described in a 10-Q note only; claims correctly marked | Supply executed documents | Required before any covenant view |
| MINOR | CP-1A | Rhode Island 5.50 to 1.00 trigger | Regulatory Agreement | Definition not supplied | Supply the agreement | Required to judge restriction |
| MINOR | CP-1A, CP-2 | Intralot does not guarantee parent debt; guarantor list | Indentures, guarantor schedules | Only the 10-Q statement is available | Supply schedules | Required for structure view |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None found as a defect | All modules | No market or relative-value claim is made in this run | Prices, spreads and ratings are not in the minimum pack | Recorded by design | Add market work only with sourced data | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | The 319 million reading and the headroom arithmetic are used in three handoffs | CP-1 attempt 2, CP-1A attempt 1 and CP-2 attempt 1 are the accepted versions and CP-2 cites their hashes | Confirm in the credit agreement | Revolver headroom statement stays indicative |
| MINOR | CP-1, CP-1A | CP-1A corrects the CP-1 page for the Chicago terms in its own Request | The CP-1 handoff cannot be edited | Fix in a rerun | None on figures |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | The June 30, 2026 position is traceable; covenant headroom and anything after August 14, 2026 are not; review is self-review only | Supply the credit documents and later filings, and add an independent review | Committee status Requires More Work |
| MINOR | CP-1, release | Duplication | The Q2 release repeats the 10-Q debt table; CP-0 and CP-1 treat the 10-Q as controlling | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Reader summary, attempt 1 | Three figures (792.2, 124.0, 129.2) were not in the handoff body; refused by the adapter and repaired in attempt 2 | Keep summary figures in the body | Resolved; attempt 2 accepted |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-1 | Locator | Chicago terms page:69 should be page:70; segment revenue page:48 should be page:47; cash balances lack locators | Cite exact pages | None | Open |
| QA-2 | MINOR | CP-1A | Locator | Revenue streams page:19 and segment revenue page:48 should be page:20 and page:47; 42.1% at page:8; 555,751 uncited | Cite exact pages | None | Open |
| QA-3 | MINOR | CP-1 | Overstated inference | Intralot cash "not available to the parent group by guarantee" | Say access is not supplied | None | Open |
| QA-4 | MINOR | CP-1A | Attribution | Penny warrants attributed wholly to Sinclair | Attribute only what the 10-K shows | None | Open |
| QA-5 | MINOR | CP-1, CP-1A, CP-2 | Interpretation | 319 million read as commitments; headroom arithmetic indicative | Confirm in the credit agreement | None | Open |
| QA-6 | MINOR | CP-1 | Export | Reader summary figures not in body (attempt 1) | Repaired in attempt 2 | None | Closed |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each double-quoted phrase in the four handoffs searched in the pinned page files, on the pages cited in its sentence | 76 quoted spans: 70 on the cited page, 6 not tied to a locator in the same sentence (4 registrant-name phrases, 1 search term, 1 correct locator written as Page:31), 0 misquoted, 0 not found |
| Q2 | Metric recomputation | Adjusted EBITDA, cash interest and cash re-parsed from the source text rows CP-1 cites and LTM sums and ratios recomputed independently; principal sums compared with the printed schedule totals (the September 30, 2025 sum has no printed total) | LTM Adjusted EBITDA 478,853; 502,399; 518,022; 512,810 and LTM cash interest 340,494; 379,808; 407,534; 444,640 (thousands) equal; 12 of 12 ratios equal |
| Q3 | Tie-outs | Reconciliations and totals re-added: Q2 Adjusted EBITDAR to loss from operations; six-month reconciliation to income from operations 57,592; Q1 plus Q2 Adjusted EBITDA; segment revenue and EBITDAR sums; cash roll-forward 906,686 − 418,915 = 487,771; debt instruments to printed totals at June 30, 2026, March 31, 2026 and December 31, 2025; carrying value 4,910,068 − 51,969 − 351,399; maturity schedules at December 31, 2025 and June 30, 2026; lease liabilities; FY2025 revenue; undiscounted lease payments 4,123,283; cash plus restricted cash; FY2025 Adjusted EBITDAR less rent; merger consideration 22,804,384 × 18.25 | 18 of 18 equal |
| Q4 | Confidence Score | `confidence_score.py --lineage "Directly Sourced:4,Calculated:4,Assumption-Based:1,Analyst Inference:1,Insufficient Information:2" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:5` | E = 70.83, C = 100, S = 0.7, P = 15: score = (0.6 × 70.83 + 0.4 × 100) × 0.7 − 15 = 42.75, rounded to 43; band Low; qa_status Passed |

The source gate is partial because the executed agreements and filings after August 14, 2026 are not in the set. Material claims are the 12 rows of T5B.3. The five MINOR findings group repeated locator slips under their module.

## Gaps

- G1 Critical for the decision: the credit agreement, amendments, conditional waiver and minimum liquidity level are not supplied, so covenant headroom is Not calculable.
- G2 Critical for currency: nothing after August 14, 2026 is supplied, including the October 2026 revolver reduction and the Fifth Amendment terms.
- G3: parent versus Bally’s Intralot cash, earnings and intercompany restrictions are not supplied; parent-level leverage is indicative.
- G4: the Rhode Island regulatory leverage definition and status are not supplied.
- G5: sponsor intentions are not documented.
- G6: no independent review; this CP-5 was written by the same host that wrote the handoffs it checks.

## Next module

- Report delivery: carry `qa_status` Passed, Confidence Score 43 (Low), committee status Requires More Work, and gaps G1 and G2.
- Swarm review step: an independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Rerun: after the credit documents and later filings are supplied, rerun CP-1, CP-1A, CP-2 and CP-5 in a new run folder with the locator corrections listed in T5.9.
