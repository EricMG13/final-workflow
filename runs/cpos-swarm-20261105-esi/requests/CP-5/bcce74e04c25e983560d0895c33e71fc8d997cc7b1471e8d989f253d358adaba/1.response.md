# CP-5 — Evidence trace and research-integrity QA: Element Solutions Inc (esi)

## Request

- Issuer: Element Solutions Inc (issuer id `esi`, NYSE: ESI), as of 2026-11-05, information cutoff 2026-11-05.
- Run: `esi-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, `minimum` module set. CP-5 checks CP-0, CP-1, CP-1A and CP-2 against the pinned sources and grades the result (absorbed CP-5A phase).
- Execution: host session. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.
- Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- QA envelope: `qa_status` Passed; Confidence Score 46, band Low (from `scripts/confidence_score.py`, see Calculations); `committee_status` Requires More Work.

## Sources

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_esi-20251231.htm.jsonl | e419be4a34b86cf3946781c81c9cf5167d1ce55ea947acb2e97a22e3ec33fbdc |
| 10-Q_2026-03-31_esi-20260331.htm.jsonl | 71ffb0652af7e069b88fd66093decc7d627d9409b00bd185ac2a68db72c238da |
| 10-Q_2026-06-30_esi-20260630.htm.jsonl | 9e356702c38010063835ed61e96bcc033abb0f0a3a4b5a9a1845d764f0bcd2b7 |
| 10-Q_2026-09-30_esi-20260930.htm.jsonl | 1efce58ae7d1707b81e096f97ecf01dbf0104d1e81a25b95db794dfd861b04fe |
| EX-99.1_2026-04-28_aearningsreleaseex99120263.htm.jsonl | cb75b2ab3988a8e0ad3f68546b2df2a55172fd4900de7f7f14ec3436aa37dbbf |
| EX-99.1_2026-07-27_aearningsreleaseex99120266.htm.jsonl | c0a4eea4343eb189f65a5cb896e49cd67b1e5c372bfce79bfb18a89241f92f7e |
| EX-99.1_2026-10-21_aearningsreleaseex99120269.htm.jsonl | b36d51c2a20c56990c8361f520b238bac0611bf5a7dab66ba03c7922169d0001 |
| context | 1920ec84f7b9710e00bbaac803890d2695813e40c10637e35f2e7d8eaaf0285a |

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | cdece14e2edef04df25761198b67e4d3c88f681db7a403c096bd0cf0d6bf17b7 |
| CP-1 | 0b784e0bff14bdc1d3f4b3894b4edcc8e5b0011eb0edb677c3ca72eb727a1ab8 |
| CP-1A | 422555478447d0a1f1c0dd50ad2be4b03b7ccdf29dc45553ba61539020c648b5 |
| CP-2 | 73a2b0bd7cfca0a7d83efa2e6771597ab4df56fd44df515e48023dd2bb9efc37 |

Locators are page chunks (`page:N`) of the pinned `.jsonl` files, written as a tag and page: K25 (10-K), Q1-26, Q2-26 and Q3-26 (10-Qs), R1, R2 and R3 (earnings releases).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis traces well to the filings: every recomputed figure matched and 145 of 146 quotations were on the cited page. Four minor defects were found. | Low | The same author wrote and checked the work, and credit documents and termination terms are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 28 headline leverage, cover and cash flow figures recomputed from the filings matched, and 21 of 21 statement tie-outs held. | Debt, liquidity and cover figures can be relied on as reported-basis numbers. | High |
| One citation points to the wrong page, one revolver availability figure does not add up from its parts, and one maturity phrase overstates. | None changes a conclusion; each should be corrected in a later run. | High |
| Covenant headroom, any termination payment and pro forma acquisition EBITDA remain unsupported by the supplied sources. | Leverage and covenant comfort cannot be verified beyond the reported basis. | Medium |

### Evidence trace view

The analysis is traceable enough for a view of Element Solutions' reported capital structure at September 30, 2026, and not for covenant headroom or the cost of the terminated Solstice merger. Every figure that CP-1 reports reproduces from the pinned pages, every CP-2 figure is found in CP-1 or CP-1A, and 145 of 146 quotations sit on the page they cite. Coverage of the 13 material claims: 4 Directly Sourced, 6 Calculated and 3 Insufficient Information. The provenance gaps that matter most are the missing Credit Agreement, indenture and Termination Agreement and the absence of pro forma EBITDA for the 2026 acquisitions; CP-2's Medium confidence and the covenant finding rest on them. The affected decision is any view of covenant protection or liquidity after a possible termination payment. Remediation owner: the sourcing step, which must add the credit documents and the August 27, 2026 Form 8-K exhibit. Four minor locator and wording defects need no change to any conclusion.

| Traceability summary | Result |
| --- | --- |
| Quotations checked against cited pages | 146 in four handoffs; 145 on the cited page; 1 on a different page (CP-0, glossary on page 2 cited as page 16); 20 further quoted spans were headings, labels or markers and are not counted |
| Figures recomputed from the pinned pages | 28 of 28 equal to CP-1 |
| Statement totals, reconciliations and roll-forwards re-added | 21 of 21 equal |
| CP-2 and CP-1A numeric tokens found upstream | CP-2: 53 of 53 in CP-1 or CP-1A; CP-1A: 68 of 68 in CP-1 or the sources |
| Material claims by lineage | 4 Directly Sourced, 6 Calculated, 3 Insufficient Information |
| Open findings | 4 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_esi-20251231.htm.jsonl | High: filed, audited annual report | Years ended December 31, 2025, 2024 and 2023 | Element Solutions Inc, consolidated | Statements, debt note, segments, Adjusted EBITDA reconciliation, business | Text extraction of the filed HTML | CP-0, CP-1, CP-1A |
| S2 | 10-Q_2026-03-31_esi-20260331.htm.jsonl | High: filed, unaudited interim | Three months ended March 31, 2026 | Same | Interim statements, debt, availability, Adjusted EBITDA | Text extraction; unaudited | CP-1 |
| S3 | 10-Q_2026-06-30_esi-20260630.htm.jsonl | High: filed, unaudited interim | Three and six months ended June 30, 2026 | Same | Interim statements, debt, merger terms as signed, termination fee risk | Text extraction; unaudited | CP-1, CP-1A |
| S4 | 10-Q_2026-09-30_esi-20260930.htm.jsonl | High: filed, unaudited interim | Three and nine months ended September 30, 2026 | Same | Statements, debt, covenant, liquidity, termination, acquisitions | Text extraction; unaudited | CP-0, CP-1, CP-1A |
| S5 | EX-99.1_2026-04-28_aearningsreleaseex99120263.htm.jsonl | Medium: issuer press release | Q1 2026 | Same | Net debt table, interest paid | Issuer non-GAAP presentation | CP-1 |
| S6 | EX-99.1_2026-07-27_aearningsreleaseex99120266.htm.jsonl | Medium: issuer press release | Q2 2026 | Same | Net debt table, interest paid | Issuer non-GAAP presentation | CP-1 |
| S7 | EX-99.1_2026-10-21_aearningsreleaseex99120269.htm.jsonl | Medium: issuer press release | Q3 2026 | Same | Capital structure, discrete-quarter cash flows, interest paid, guidance | Issuer non-GAAP presentation | CP-1, CP-1A, CP-2 |
| S8 | context | User settings, not evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency | Not issuer evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage raised by debt-funded 2026 acquisitions: total debt 2,082.1 against 1,625.9 | CP-1, CP-2 | Debt note and cash flow statement | Sets leverage tolerance and the starting point for deleveraging | Core leverage metric | S4 pages 7, 15; S1 page 112 | LTM EBITDA not pro forma |
| 2 | Coverage of 7.85x on cash interest paid | CP-1, CP-2 | LTM Adjusted EBITDA 673.1 over interest paid 85.7 | Debt-service capacity | Core coverage metric | S1 pages 85, 124; S4 pages 5, 27; S7 page 9 | Interest paid assumed to be the same measure as cash paid for interest |
| 3 | 2028 notes of 800.0 against liquidity of 702.9 | CP-1, CP-2 | Release capital structure and revolver text | First large maturity | Refinancing monitoring point | S7 page 9; S4 pages 15, 18, 44 | Term loan installments not scheduled by year |
| 4 | Electronics and pass-through metals dependence | CP-1A, CP-2 | Segment and metals tables | Earnings, margin and working capital move with demand and metals | Concentration risk | S4 pages 26, 27; S7 page 8 | Price against volume not disclosed |
| 5 | Terminated Solstice merger and unquantified cost | CP-1A, CP-2 | Q2 and Q3 10-Q notes | Possible fee or cost of up to the disclosed 376,000,000 | Liquidity and governance | S3 pages 12, 50; S4 pages 3, 12 | Termination Agreement not supplied |
| 6 | Springing first lien test of 5.0 to 1.0 | CP-1, CP-2 | Credit Agreement note | Only financial covenant located | Covenant protection | S4 page 17; S1 page 113 | Definitions not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt / LTM Adjusted EBITDA 3.09x and net 2.76x | CP-1 | S1, S4 statements and debt note | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Adjusted EBITDA / cash interest paid 7.85x | CP-1 | S1 page 85; S4 page 27; S7 page 9 | Yes | High inputs; releases for interest paid | Calculated | Supported with label caveat | Medium | Recomputed equal |
| Cash plus unused revolver 702.9 | CP-1 | S4 pages 6, 15, 18, 46 | Yes | High | Calculated | Supported | High | Recomputed equal |
| 800.0 senior notes due September 1, 2028 | CP-1, CP-2 | S4 page 18; S7 page 9 | Yes | High | Directly Sourced | Supported | High | Traced |
| Springing 5.0 to 1.0 first lien net leverage test above 30% revolver use | CP-1, CP-2 | S4 page 17 | Yes | High | Directly Sourced | Supported | High | Traced |
| Compliance with covenants at September 30, 2026 | CP-1, CP-2 | S4 pages 18, 46 | Yes | High; management statement | Directly Sourced | Supported as a statement | Medium | Traced |
| Merger signed July 6, 2026 and terminated August 27, 2026 | CP-1A, CP-2 | S3 pages 12, 50; S4 pages 3, 12 | Yes | High | Directly Sourced | Supported | High | Traced |
| Electronics 78.3% of Q3 2026 net sales; pass-through metals 40.9% of Electronics sales | CP-1A, CP-2 | S4 page 26; S7 page 8 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Operating cash flow 35.8% of Adjusted EBITDA for nine months 2026 against 48.3% | CP-1, CP-2 | S4 pages 7, 27 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Termination fee or cost actually incurred | CP-1A, CP-2 | No source in the set | No source exists in the set | Not available | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Covenant headroom | CP-1, CP-2 | Definitions not in the set | No source exists in the set | Not available | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Leverage on a pro forma basis for EFC and Micromax | CP-1, CP-2 | No pro forma EBITDA in the set | No source exists in the set | Not available | Insufficient Information | Open gap | Low | Gap correctly labelled |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales FY2025 2,551.2 | runs/cpos-swarm-20261105-esi/source-text | 10-K_2025-12-31_esi-20251231.htm.jsonl | S1 | Page 82, statements of operations | CP-1 metrics table | Reported | High | Matches |
| Total debt 2,082.1 at September 30, 2026 | runs/cpos-swarm-20261105-esi/source-text | 10-Q_2026-09-30_esi-20260930.htm.jsonl | S4 | Page 15, Note 6 | CP-1 debt register | Reported | High | Components re-added equal |
| Face debt 2,094.7 | runs/cpos-swarm-20261105-esi/source-text | EX-99.1_2026-10-21_aearningsreleaseex99120269.htm.jsonl | S7 | Page 9, capital structure | CP-1 debt register | Issuer presentation | Medium | Components re-added equal; differs from carrying value by 12.6 stated discounts and costs |
| Adjusted EBITDA nine months 2026 536.8 | runs/cpos-swarm-20261105-esi/source-text | 10-Q_2026-09-30_esi-20260930.htm.jsonl | S4 | Page 27, reconciliation | CP-1 C1 | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| Interest paid nine months 2026 76.2 | runs/cpos-swarm-20261105-esi/source-text | EX-99.1_2026-10-21_aearningsreleaseex99120269.htm.jsonl | S7 | Page 9, selected financial data | CP-1 C3 | Issuer presentation | Medium | Label differs from the 10-K "Cash paid for interest" |
| Unused revolver capacity 478 | runs/cpos-swarm-20261105-esi/source-text | 10-Q_2026-09-30_esi-20260930.htm.jsonl | S4 | Page 18, Note 6 | CP-1 liquidity | Reported | High | Equals 500.0 less 15.0 less 7.0 |
| Merger terminated August 27, 2026 | runs/cpos-swarm-20261105-esi/source-text | 10-Q_2026-09-30_esi-20260930.htm.jsonl | S4 | Pages 3, 12 | CP-1A transaction summary | Reported | High | Matches |
| Possible termination fee 376,000,000 | runs/cpos-swarm-20261105-esi/source-text | 10-Q_2026-06-30_esi-20260630.htm.jsonl | S3 | Page 50, risk factor | CP-1A transaction summary | Reported risk | High | Conditional, not an incurred amount |
| Springing covenant 5.0 to 1.0 | runs/cpos-swarm-20261105-esi/source-text | 10-Q_2026-09-30_esi-20260930.htm.jsonl | S4 | Page 17, Note 6 | CP-1 covenant table | Reported description | High | Matches |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM figures | CP-1 C1; CP-2 findings 1 to 4 | FY2025 and both nine-month periods | FY2025 + nine months 2026 − nine months 2025 | Recomputed from parsed pages: equal | Supported | High | Basis of every ratio | S1 pages 82, 84, 85, 124; S4 pages 5, 7, 27; S7 page 9 |
| LTM at Q1 and Q2 2026 | CP-1 C2, C3 | Q1 and six-month figures | Same build with Q1 and six-month columns | Recomputed: 581.5, 629.0, 72.3, 79.5 equal | Supported | High | Leverage trend | S2 page 23; S3 page 28; S5 page 9; S6 page 11 |
| Leverage | CP-1 C4; CP-2 finding 1 | Carrying debt, cash, LTM Adjusted EBITDA | Debt / EBITDA; (debt − cash) / EBITDA | Recomputed: 3.09x, 2.76x, 2.97x, 1.83x, 3.71x, 3.40x, 3.37x, 3.07x, 3.41x, 2.74x equal | Supported | High | Leverage tolerance | S1 pages 83, 112; S2 pages 5, 13; S3 pages 6, 16; S4 pages 6, 15 |
| Coverage | CP-1 C5; CP-2 finding 2 | Interest paid assumed to equal cash paid for interest | Adjusted EBITDA / cash interest; / net interest | Recomputed: 7.85x, 8.29x, 7.98x, 10.25x, 8.04x, 7.91x, 8.25x equal | Supported with label caveat | Medium | Debt service | S1 page 85; S5 page 9; S6 page 11; S7 page 9 |
| Free cash flow | CP-1 C6 | Operating cash flow less capital expenditures | Subtraction | Recomputed: 182.9 and 227.6 equal | Supported | High | Cash generation | S1 page 84; S4 page 7 |
| Indicative first lien net leverage | CP-1 C12 | First lien debt 1,294.7 less cash over LTM Adjusted EBITDA | Division | Recomputed: 1.59x equal; not the covenant ratio | Supported as indicative | Medium | Covenant context | S7 page 9 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial gate, 4 MINOR | Script formula | 46, band Low | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 identity and perimeter | The borrowers phrase "among, inter alia, Element Solutions and MacDermid, Incorporated, as borrowers" is cited to Q3-26 page 16 but sits in the glossary on Q3-26 page 2; page 16 holds a different sentence naming the borrowers | Wrong page locator | A reader checking page 16 will not find the phrase, although the fact is true | Cite Q3-26 page 2 in a later run | CP-0 handoff |
| MINOR | CP-0 readiness view | States that none of the sources has blocked preparation; no preparation catalog was supplied to the host, so the statement means only that the pages were readable | Unsupported statement | Overstates a check that was not performed | Say "pages readable" in a later run | CP-0 handoff |
| MINOR | CP-1 liquidity chart | Q2 2026 undrawn revolver is the printed 441; the printed components give 500 less 50.0 drawn less 6.9 of letters of credit, that is 443.1, and CP-1 does not flag the 2.1 difference | Unflagged source arithmetic gap | The Q2 liquidity point is 2.1 lower than components imply | Flag the difference or cite the components | CP-1 handoff |
| MINOR | CP-2 credit view and strengths | Says there is no maturity before September 2028; CP-1 shows current installments of 27.9, of which 12.9 are scheduled term loan installments and 15.0 is revolver borrowing | Overstated wording | Scheduled installments exist, though small | Say "no large final maturity" | CP-2 handoff |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves by cover text and period | A wrong document would change every figure | None found | None |
| Locator precision | Strong | 145 of 146 quotations on the cited page; one wrong page | Slower checks; risk of a misplaced citation | None on conclusions | Correct the one locator |
| Calculation reproducibility | Strong | 28 of 28 figures and 21 of 21 tie-outs recomputed equal | Calculation errors would move leverage | None found | None |
| Cross-module consistency | Strong | All CP-2 and CP-1A numeric tokens found upstream; CP-1A and CP-2 cite the current upstream hashes | Inconsistent figures mislead a committee | None found | None |
| Reviewer independence | Weak | Host wrote and checked the handoffs | Shared blind spots go undetected, as the earlier TDG pilot showed | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Credit Agreement and indenture not supplied | Executed agreements | Covenant headroom, incurrence and restricted-payment capacity unknown | Covenant finding, governance table | Covenant view rests on note summaries | Credit Agreement, amendments, indenture |
| G2 | Termination Agreement and any payment | Form 8-K of August 27, 2026 and exhibit | A possible fee or cost is unquantified | Liquidity and governance reading | Holds the merger view to the filing summary | The August 27, 2026 Form 8-K |
| G3 | Pro forma EBITDA for EFC and Micromax | Management pro forma or compliance certificate | LTM leverage is on a reported basis | Leverage findings | Lowers precision of leverage | Management or compliance certificate |
| G4 | Events after October 22, 2026 | Later Form 8-Ks and filings | Position at the as-of date may differ | Monitoring posture | Lowers currency of the view | EDGAR filings to the cutoff date |
| G5 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / esi-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed with two MINOR findings | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, debt, liquidity, covenants | High | Six headings; accepted | Passed with one MINOR finding | All figures recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, merger, governance | High | Six headings; accepted | Passed with no findings | Quotations on cited pages |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Passed with one MINOR finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 | Identity and perimeter, borrowers phrase | Supported | Page 16 cited; phrase is on page 2 | Cite page 2 | None |
| MINOR | CP-0 | Readiness view, blocked preparation | Unsupported statement | No preparation catalog was supplied | Reword | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Q2 2026 unused revolver | Printed 441 against components giving 443.1 | Source arithmetic gap of 2.1, not flagged | Flag in a later run | None |
| MINOR | CP-1 | Cash interest label | Releases print "Interest paid"; the 10-K prints "Cash paid for interest" | Label difference, assumed same measure and disclosed | Keep cover ratio labelled approximate, as CP-1 does | None |
| MINOR | CP-1 | Adjusted EBITDA as leverage denominator | Adds back acquisition-related costs and share grants; LTM not pro forma | None | Keep the caveats beside the ratios, as CP-1 does | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Springing 5.0 to 1.0 first lien test above 30% revolver use | Executed Credit Agreement | Description in the note only | Supply agreement | Required for headroom |
| MINOR | CP-1A | Change of control as a Credit Agreement default | Credit Agreement and indenture | Note lists "change of control provisions"; terms not supplied | Supply documents | Required for post-event analysis |
| MATERIAL as a gap, not a defect | CP-1A, CP-2 | Effect of the terminated merger, any fee, and guarantor and security detail | Termination Agreement, Credit Agreement, indenture | Documents not supplied; claims correctly marked Insufficient Information | Supply documents; add CP-4 | Required before any covenant or fee conclusion |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; the release's market capitalization is outside the credit findings | Bond prices, spreads and ratings are not in the minimum pack | Recorded by design | Add CP-3D or CP-2H only with sourced market data | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | CP-2 says no maturity before September 2028 while CP-1 shows current installments | None; all four handoffs are attempt 1 and later modules cite the current upstream hashes | Reword CP-2 in a later run | None |
| MINOR | CP-0, CP-1, CP-1A | EFC and Micromax prices differ between the 10-K and the Q3 10-Q; logged by CP-0 and CP-1A and resolved by using the later filing | None | None; conflict correctly logged, not silently chosen | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | The reported-basis view is traceable; covenant headroom, any termination cost and pro forma leverage are not; the review is a self-review | Supply credit documents and the Termination Agreement; add an independent review | Committee status Requires More Work |
| MINOR | CP-1, releases | Duplication | The releases repeat the 10-Q statement figures; CP-0 and CP-1 treat the 10-Q as controlling and use the releases only for net debt, interest paid and discrete-quarter cash flow | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| NONE | All | Section headings, report selectors and tables | None found; all four accepted at attempt 1 | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-0 | Locator | Borrowers phrase cited to page 16; it is on page 2 | Cite page 2 in a later run | None | Open |
| QA-2 | MINOR | CP-0 | Unsupported statement | "No blocked preparation" with no preparation catalog | Reword | None | Open |
| QA-3 | MINOR | CP-1 | Source arithmetic | Q2 2026 undrawn revolver 441 against 443.1 from components, unflagged | Flag the 2.1 difference | None | Open |
| QA-4 | MINOR | CP-2 | Wording | "No maturity before September 2028" ignores scheduled installments | Say no large final maturity | None | Open |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each double-quoted phrase in the four handoffs searched on the page its sentence cites; phrases shorter than 8 characters ignored | 166 quoted spans parsed, of which 20 were headings, labels or markers; of 146 quotations, 145 are on the cited page and 1 is on a different page (CP-0, page 2 not page 16) |
| Q2 | Figure recomputation | Values parsed from the pinned pages by label, not retyped: LTM net sales, operating profit, interest expense, Adjusted EBITDA, operating cash flow, capital expenditures, cash interest paid and EBITDA; ratios at Q3 2026, FY2025, Q1 2026, Q2 2026 and FY2024; free cash flow | 28 of 28 equal to CP-1 |
| Q3 | Tie-outs | Quarterly sums for net sales, Adjusted EBITDA, operating cash flow and capital expenditures; Adjusted EBITDA reconciliations for FY2025, nine months 2026, nine months 2025 and Q3 2026; Q3 2026 assets and liabilities; debt carrying and face totals; cash roll-forwards for nine months 2026 and FY2025; gross profit and operating profit; segment sums; liquidity; debt change | 21 of 21 equal |
| Q4 | Numeric consistency | Decimal, thousands, percentage and ratio tokens in CP-2 searched in CP-1 and CP-1A, and in CP-1A searched in CP-1 and the sources | 53 of 53 and 68 of 68 found |
| Q5 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:4,Calculated:6,Insufficient Information:3" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:4` | score = clamp((0.6 × 72.31 + 0.4 × 100) × 0.7 − 12) = 46.37, rounded to 46; band Low; qa_status Passed |

## Gaps

- G1 Material for covenant work: the Credit Agreement and indenture are not supplied.
- G2 Material: the Termination Agreement and any payment are not supplied.
- G3: pro forma EBITDA for the 2026 acquisitions is not supplied.
- G4: events after October 22, 2026 are not supplied.
- G5: no independent review; this CP-5 was written by the same host.

## Next module

- Report delivery: carry `qa_status` Passed, Confidence Score 46 (Low), committee status Requires More Work, and gaps G1 and G2.
- Swarm review step: an independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: fetch the Credit Agreement, the indenture, and the August 27, 2026 Form 8-K with the Termination Agreement, then rerun the modules in a new run folder.
