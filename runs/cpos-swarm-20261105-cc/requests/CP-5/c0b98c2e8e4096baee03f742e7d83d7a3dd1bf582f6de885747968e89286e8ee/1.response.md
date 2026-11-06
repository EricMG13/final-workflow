## Request

Chemours Co (The Chemours Company, issuer id cc), as of 2026-11-05, pathway credit_snapshot, USD. This module traces the claims of the four accepted handoffs (source readiness, financial base, business context, credit synthesis) to the seven supplied filings and releases, checks locators and calculations, logs conflicts and grades research integrity. It does not change the underlying credit conclusion and does not repair lineage silently.

## Sources

### Issuer sources traced

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_cc-20251231.htm.jsonl | adf80f4588f501b9f797e1b55a5853888465c5d9b30aef8ff07b3cd4340b3957 |
| 10-Q_2026-03-31_cc-20260331.htm.jsonl | 544e858f14516405499b0793277b117ab856893d213de4bfdfd312ae33ddb9fd |
| 10-Q_2026-06-30_cc-20260630.htm.jsonl | 5934bf743b44e940824956ac90d2979f28da0477a0f669044693e5e59c78b62f |
| 10-Q_2026-09-30_cc-20260930.htm.jsonl | f23013a765ad5943b395240230ccfbe7a0cca417e186c8a1a82b34a215485de7 |
| EX-99.1_2026-05-05_cc-ex99_1.htm.jsonl | cf37012a81481ef001a376d207312af6444e1ec5683c9d45ff930f84bd36dd4e |
| EX-99.1_2026-08-04_cc-ex99_1.htm.jsonl | 5e0a77f0453e40d6a00670f0f971f2e2c0487e12a68a0222858c84133578166e |
| EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | d716a94a423338ae97b02c515014fccad1457c8952131fe6a67cf2f82a22b1e0 |

The run context (sha256 e4e3509e830ce866831093e05761a30c7677098a166e3ae01f6bf5702202686d) holds dates and currency only and is not issuer evidence.

### Supplied handoffs audited

| Module | sha256 |
| --- | --- |
| CP-0 (source readiness) | 1ecb39c4a4880cffa7ae4a7043208842e01127188022f689018f652251f98699 |
| CP-1 (financial base) | 66c8382addeeb6334641b2106aad48df892e2b12eebe59c20cf662cd9c7c2735 |
| CP-1A (business and transaction context) | 68f3c23dab99b4b17ecaf3d393184950ee6d4db0592f5576f2a8e526977fa345 |
| CP-2 (credit synthesis) | c29b7415a9f188a6584a1c4d1bf77728d1fdc814ae3412bd485c11e0c554fdec |

The sources are text extractions in page-sized chunks; `page:N` is a chunk, not a printed page. Both the source pages and the handoffs were opened, not only the handoffs' own citations.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The figures in the four handoffs trace to filed sources with one wrong page reference and a few labelling slips. Committee use is restricted because covenant headroom and legal capacity cannot be traced to governing documents. | Medium | No credit agreement, indenture or settlement document is supplied, so covenant and structural claims rest on company statements. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of 18 material claims, 12 are directly sourced, 3 are calculated, 1 is assumption-based and 2 are analyst inference; all stated figures reproduced from the cited pages. | Debt, cash, liquidity and settlement figures can be relied on as filed facts. | High |
| Compliance with the revolver covenant is a management statement only; the tested level and the reported ratio are not printed. | Headroom on the revolver is unverified, which restricts any conclusion on revolver access. | High |
| Leverage on the carrying value of debt is 5.13x gross and 4.20x net, against 5.18x and 4.25x on principal. | The basis choice moves leverage by about 0.05x and does not change the view. | High |
| Eight minor defects were found, two of them wording errors already corrected downstream. | None changes a figure; they are logged for clean-up. | High |

### Evidence trace view

The traced evidence is sound for the stated purpose of a fundamental, filings-based credit screen. Every dollar figure in the financial base, the business context and the synthesis was found on the cited page of the cited filing or release, except one locator that points to the wrong page and one row whose composition is inferred rather than printed. Calculated figures reproduce from their printed inputs. The weaknesses are in what the sources cannot show: the covenant test, the guarantee and security structure, the status of the revolving tranche that matured on October 7, 2026, cash interest for 2026, and the executed settlement documents. Because those gaps bear on committee conclusions about revolver access and legal capacity, the research is graded Restricted, not Passed, and the synthesis confidence of Medium is appropriate.

### Traceability conclusion

The analysis is traceable enough for a fundamental credit screen but not for covenant, legal-structure or relative-value decisions. Supported claims dominate: the debt schedule, liquidity, maturity profile, segment results and settlement terms all reproduce from filed pages, and derived leverage and cover ratios recompute from printed inputs. Inference is confined to labelled interpretation, such as the earnings rotation and the supportive reading of issuer behaviour, and one labelled scenario for revolver availability. The most important provenance gap is the missing Credit Agreement: management states covenant compliance, but neither the tested level after the temporary relief nor the reported ratio can be traced. The remediation is to obtain the Credit Agreement, its amendments and the latest compliance certificate.

### Audit summary

| Field | Value |
| --- | --- |
| Committee status | Restricted: permitted for fundamental screening, liquidity and maturity review, with the limitations disclosed; not for covenant headroom, legal capacity or security-level conclusions |
| QA status | Restricted (one MATERIAL finding, no CRITICAL) |
| Confidence score and band | 54, Low (computed with the canon script: E 88.89, C 100, S pass 1.0, P 39) |
| Material claims by lineage | Directly Sourced 12, Calculated 3, Assumption-Based 1, Analyst Inference 2 |
| Findings | MATERIAL 1, MINOR 8 |
| Locator audit | 58 locator-and-value checks run against the source pages; 57 matched; the one miss is the dividends-paid page reference (issue I-02) |

### Analytical appendix — complete canonical registers

#### T5.1 Handoff register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 response 1; run cc-2026-11-05-credit_snapshot-host | Source readiness of seven sources, four consumers | High: filed statements and releases | Six H2 headings and readiness view present | Restricted | Two wording errors (I-06, I-07), corrected in CP-1; READY_WITH_LIMITATIONS verdicts consistent with later work |
| CP-1 | requests/CP-1 response 1; same run | Financial base: statements, leverage, interest cover, liquidity, maturities, claims outside debt | High | Six H2 headings, four chart tables and financial table present | Restricted | Issues I-02, I-03, I-04; leverage basis I-08, I-09 |
| CP-1A | requests/CP-1A response 1; same run | Business, ownership, transaction and governance context, fact register F1 to F30 | High | Six H2 headings, operating model and profile tables, transaction prose present | Restricted | Issue I-05; legal capacity and ownership correctly marked Insufficient Information |
| CP-2 | requests/CP-2 response 2; same run | Credit synthesis from CP-1 and CP-1A only | High for figures; synthesis is Analyst Interpretation | Six H2 headings, strengths-and-weaknesses and key-findings prose present | Restricted | Confidence Medium, below High as the method requires; inherits I-04 |

#### T5.2 Claim and section evidence issues

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-1A, CP-2 | Covenant compliance and headroom (I-01) | Management statement only: "we were in compliance with the applicable covenants under the Credit Agreement" (10-Q Q3 page:149) | The 2.00 to 1.00 maximum is printed in the 10-K (page:211); the raised level for tests through the quarter ended 2026-09-30 and the reported ratio are not | Obtain the Credit Agreement, Amendments 1 to 4 and the compliance certificate | Committee use restricted for revolver access and covenant conclusions |
| MINOR | CP-1 | Dividends paid in the financial table (I-02) | Figures verified: (39) and (63) | Locator cites 10-Q Q3 page:5; the line is on page:6 | Cite page:6 | None on values |
| MINOR | CP-1 | Debt maturities rows for 2028, 2029 and thereafter (I-03) | Totals verified against the Note 15 table (page:30) | The composition shown in the basis column (term loan, notes, amortization) is inferred; the table prints only senior debt totals | Label the composition as inferred | None on totals |
| MINOR | CP-1, CP-2 | North Carolina reserve of 205 (I-04) | Figure verified (page:116) | The reserve reflects both the settlement obligation and the settlement in principle with about 2,900 private well owners, so it is wider than the settlement alone | Relabel as legal reserve for the North Carolina settlement and private well matters | Obligation attributed to the settlement is slightly overstated |
| MINOR | CP-1A | Governance table, indemnification row (I-05) | The fact register F15 is accurate | The table says legal fees were advanced; the 10-K says requests for advances were received (page:49) | Reword to requests received | None |
| MINOR | CP-0 | Mechanism paragraph on the revolver (I-06) | Date verified (10-Q Q3 page:149) | Says the tranche expired five weeks after the balance-sheet date; it was one week (September 30 to October 7, 2026) | Already corrected in CP-1; none further | None; corrected downstream |
| MINOR | CP-0 | Gap 4 on depreciation and amortization (I-07) | Figures verified (release page:13; 10-Q Q3 page:133) | The sentence compares the release's 2025 figure with the 10-Q's 2026 and 2025 figures confusingly | Already restated in CP-1 | None; corrected downstream |

#### T5.3 Metric and logic issues

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Adjusted EBITDA is not printed as a consolidated filing total (I-08) | Calculated as segment Adjusted EBITDA plus other segment less corporate expenses; this is a defined, reproducible logic | Nine-month 2025: release 614 against components 619; three-month 2025: 189 against 190 (release page:13; 10-Q Q3 page:133); trailing totals differ by 3 to 6 | Keep both bases visible; do not average | Leverage differs by 0.02x between bases; no change to the view |
| MINOR | CP-1, CP-2 | Leverage is stated on total debt principal, not balance-sheet carrying value (I-09) | Principal 3,872 against carrying 3,833; the difference of 39 is unamortized discounts of 15 plus issuance costs of 24 (10-Q Q3 page:24) | None | State carrying-basis ratios beside principal-basis ratios (see Calculations) | 0.05x; no change to the view |
| MATERIAL (counted once under I-01) | CP-1 | Covenant EBITDA and senior secured net debt | Defined in the Credit Agreement, not supplied | None | Not calculable; obtain the Credit Agreement | Headroom cannot be reproduced |
| None | CP-1 | Interest cover uses cash interest for FY2024 and FY2025 and interest expense, net for 2025 and 2026 interim periods | Bases are labelled in each row | None | None | Mixed bases are disclosed, not hidden |

#### T5.4 Legal and structural claims

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL (counted once under I-01) | CP-1 | Term loans and revolver are senior secured by a first-priority lien on substantially all assets and guaranteed by material wholly-owned domestic subsidiaries (10-K page:211) | Credit Agreement and security documents | Company summary only | Obtain and review | Required before any security-level conclusion |
| None (disclosed gap) | CP-1, CP-1A | Notes are guaranteed by guarantor subsidiaries; the 2034 notes name "the guarantor named therein" (10-Q Q3 page:27) | Indentures and supplemental indentures | Guarantors not named | Obtain indentures and guarantor list | Required before assessing structural subordination |
| None (disclosed gap) | CP-1, CP-2 | Revolver springing maturity if the term loans or 2028 and 2029 notes are not refinanced within 91 days before maturity (10-Q Q3 page:25) | Credit Agreement | Company summary only | Obtain and review | Required before relying on the refinancing window |
| None (disclosed gap) | CP-1A, CP-2 | New Jersey settlement 875 over 25 years; North Carolina settlement 455 over 15 years; 2026 Consent Decree penalty 23 (10-Q Q3 page:91, page:116, page:111) | Executed judicial consent order, settlement agreement, consent decree | Company summaries only | Obtain executed documents | Required for payment timing and acceleration terms |
| None (disclosed gap) | CP-1A, CP-2 | Cost sharing with DuPont and Corteva up to 4,000, about 1,130 available (10-Q Q3 page:34-35) | MOU of January 2021 and the PFAS Insurance MOU | Company summaries only | Obtain the MOUs | Required before treating the sharing as enforceable recovery |

#### T5.5 Market and relative-value claims

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | CP-1A, CP-2 | Only issuer-reported ratings are used: Moody's B1 with stable outlook (July 17, 2026) and S&P BB- with negative outlook (April 16, 2025) | No quotes, spreads, valuation or peer inputs in the context | The S&P action is older than the other evidence; no agency report supplied | None for this run; relative value is outside the selected modules | No market or relative-value conclusion is made, so none can be relied on |

#### T5.6 Data and claim conflicts, and version issues

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR (I-08) | CP-0, CP-1, CP-1A, CP-2 | Nine-month 2025 Adjusted EBITDA 614 in the release against 619 from 10-Q components; logged and not reconciled in each handoff | 2025 comparatives are revised in the 2026 filings; originally reported 2025 filings are not supplied | Keep both visible | Trend precision only |
| MINOR (I-06) | CP-0, CP-1 | Revolver tranche timing: five weeks (CP-0) against one week (CP-1, source) | CP-0 cannot be edited; CP-1 states the correction | None further | None |
| None | CP-0, CP-1 | Release and 10-Q classify 23 of 2025 charges differently between depreciation and amortization and restructuring (release page:13; 10-Q Q3 page:133) | Different documents | Disclosed; Adjusted EBITDA is unaffected because both lines are added back | None |
| None | CP-1A | Kuan Yin consideration shown as about 360 (agreement, 10-K page:16), gross 300 plus 56 (10-Q Q3 page:22) and about 340 net (release Q3 page:1) | Different bases | Not a conflict; bases labelled | None |
| None | CP-1, CP-1A | North Carolina total of 455 is not stated as company share or all-party total (10-Q Q3 page:116) | Single source | Disclosed as a gap | Obligation sizing relies on the reserve |

#### T5.7 Other issues

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| None | All | Cutoff and subsequent events | All sources are dated on or before 2026-11-05; the Q3 10-Q was filed on the cutoff date. Subsequent events are flagged and kept out of period figures: revolver tranche maturity (October 7, 2026), first North Carolina payment (October 2026), factoring facility extension (October 31, 2026) | None | Treatment is correct |
| None | All | Extraction fidelity | Text extraction only; no chart or image inspected and no table-fidelity review beyond the checked cells | Record as a parse limit | Table cells outside the checked set are not independently reviewed |
| None | CP-1A, CP-2 | Management attribution | Strategy, guidance, liquidity horizon and the 4.3x ratio are labelled Management Language or attributed | None | Attribution is clear |
| None | CP-2 | Prohibited conclusions | No peer ranking, instrument recommendation or recovery conclusion appears | None | Compliant |

#### T5.8 Handoff component defects

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR (I-06, I-07) | CP-0 | Findings mechanism paragraph; Gaps row 4 | Wording errors | Corrected in CP-1 | None |
| MINOR (I-02, I-03, I-04) | CP-1 | Financial table locator; maturities basis column; claims table reserve label | Locator, inferred composition, scope label | Apply fixes in any rerun | CP-2 inherits I-04 |
| MINOR (I-05) | CP-1A | Governance table | Overstated advancement | Reword | None |
| None | CP-2 | Selector sections | Prose-only sections for strengths and weaknesses and for key findings are present; confidence is Medium | None | None |

#### T5.9 Issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | MATERIAL | CP-1, CP-1A, CP-2 | Unverifiable covenant and legal structure | Covenant compliance is a management statement; the temporary level, the reported ratio, guarantees, security and springing mechanics are not traceable to governing documents | Obtain Credit Agreement, amendments, compliance certificate, indentures | Restricts committee use | Open |
| I-02 | MINOR | CP-1 | Locator | Dividends paid cited at page:5; correct is page:6 | Correct locator | None | Open |
| I-03 | MINOR | CP-1 | Inferred composition | Maturity basis column infers composition not printed | Label as inferred | None | Open |
| I-04 | MINOR | CP-1, CP-2 | Scope label | North Carolina reserve of 205 includes private well matters | Relabel | Minor | Open |
| I-05 | MINOR | CP-1A | Overstatement | Advancement of fees stated where requests were received | Reword | None | Open |
| I-06 | MINOR | CP-0 | Wording | Five weeks stated; one week is correct | Corrected in CP-1 | None | Corrected downstream |
| I-07 | MINOR | CP-0 | Wording | Depreciation and amortization comparison muddled | Restated in CP-1 | None | Corrected downstream |
| I-08 | MINOR | CP-1, CP-2 | Basis conflict | No consolidated Adjusted EBITDA total; 614 against 619 | Keep both visible | 0.02x | Disclosed |
| I-09 | MINOR | CP-1, CP-2 | Debt basis | Principal used; carrying basis differs by 39 | Show carrying basis | 0.05x | Resolved here by calculation |

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_cc-20251231.htm.jsonl | High: filed, audited statements | FY2025, with FY2024 and FY2023 comparatives | The Chemours Company, consolidated | Statements, Note 20 debt, covenant text, segments, business description, risk factors | Text extraction; 2025 comparatives revised | All modules |
| S2 | 10-Q_2026-03-31_cc-20260331.htm.jsonl | High: filed, unaudited | Q1 2026 | Consolidated | Position at 2026-03-31, segment reconciliation | Text extraction | CP-1 |
| S3 | 10-Q_2026-06-30_cc-20260630.htm.jsonl | High: filed, unaudited | Q2 and first half 2026 | Consolidated | Position at 2026-06-30, six-month reconciliation | Text extraction | CP-1 |
| S4 | 10-Q_2026-09-30_cc-20260930.htm.jsonl | High: filed, unaudited | Q3 and nine months 2026 | Consolidated | Statements, Note 15, Note 17, segments, liquidity | Text extraction; filed on the cutoff date | All modules |
| S5 | EX-99.1_2026-05-05_cc-ex99_1.htm.jsonl | Medium: management release, attributed | Q1 2026 | Consolidated and segments | Adjusted EBITDA, trailing figures, debt principal | Management measures | CP-1 |
| S6 | EX-99.1_2026-08-04_cc-ex99_1.htm.jsonl | Medium: management release, attributed | Q2 2026 | Consolidated and segments | Same | Management measures | CP-1 |
| S7 | EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | Medium: management release, attributed | Q3 2026 | Consolidated and segments | Same, outlook, free cash flow | Management measures; guidance | CP-1, CP-1A, CP-2 |

#### T5B.2 Top credit drivers by materiality

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Legacy PFAS and environmental settlement cash calls | CP-1A, CP-1, CP-2 | New Jersey 875 over 25 years, North Carolina 455 over 15 years, reserves 176 and 205, environmental liabilities 116 and 689 | Fixed cash calls outside debt that Adjusted EBITDA excludes | Free cash flow after settlements is the coverage test | S4 pages 3, 91, 111, 116; S1 page:317 | Executed documents absent; I-04 |
| 2 | Leverage and thin equity | CP-1, CP-2 | Principal 3,872; cash 698; LTM Adjusted EBITDA 747; 5.18x and 4.25x; equity 156 | Little capacity for an earnings shortfall | Sets debt capacity | S4 pages 3, 4, 24, 133; S1 page:317 | EBITDA basis I-08; principal basis I-09 |
| 3 | Refinancing of 2028 and 2029 maturities | CP-1, CP-2 | 780 in 2028, 647 in 2029, 2,419 after 2030; springing revolver maturity | The first large funding event | Timing and market access | S4 pages 25, 30 | Credit Agreement absent |
| 4 | Liquidity and the revolver tranche | CP-1, CP-1A, CP-2 | Cash 698; availability 953; tranche of 220 matured October 7, 2026 | Headline liquidity includes a tranche that has since matured | Near-term resilience | S4 pages 25, 26, 149 | Extension status not stated |
| 5 | Earnings mix and cyclicality | CP-1A, CP-2 | Q3 2026 segment Adjusted EBITDA 136, 85 and 24 against 194, 25 and 14 | Rotation toward the more cyclical segment | Durability of cash flow | S4 page:133; S7 pages 3-4 | Channel-fill cause is management language |
| 6 | Titanium customer concentration | CP-1A, CP-2 | Ten largest customers over 44 percent, one over 20 percent | Single-customer volume risk | Revenue volatility | S1 page:20 | Customer names not supplied |
| 7 | Governance and disclosure history | CP-1A, CP-2 | 2024 audit committee review, 2023 material weaknesses remediated, revised prior periods | Possible further adjustments and regulatory cost | Monitoring posture | S1 pages 48-49, 71; S4 page:7 | Outcomes not quantified |

#### T5B.3 Claim traceability register

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt principal 3,872 at 2026-09-30 | CP-1 | S4 page:24 | Yes | High | Supported | Verified | High | Directly Sourced |
| Unrestricted cash 698 | CP-1 | S4 page:3, page:149 | Yes | High | Supported | Verified | High | Directly Sourced |
| Revolver availability 953 net of letters of credit 47 | CP-1 | S4 page:26, page:149 | Yes | High | Supported | Verified | High | Directly Sourced |
| Tranche of 220 matured October 7, 2026 | CP-1, CP-1A | S4 page:25, page:149 | Yes | High | Supported | Verified | High | Directly Sourced |
| Maturity table 26, 42, 780, 647, 23, 2,419 | CP-1 | S4 page:30 | Yes | High | Supported | Verified; composition inferred (I-03) | High | Directly Sourced |
| LTM Adjusted EBITDA 747, filing basis | CP-1 | S1 page:317; S4 page:133 | Yes | High | Derived | Reproduced | Medium | Calculated |
| Total debt / EBITDA 5.18x and net 4.25x | CP-1, CP-2 | Calculated from the rows above | Yes | High | Derived | Reproduced | Medium | Calculated |
| Interest cover 2.94x FY2024 and 2.99x FY2025 | CP-1, CP-2 | S1 page:163; S1 page:317 | Yes | High | Derived | Reproduced | High | Calculated |
| New Jersey 875 over 25 years; 100 paid; 176 recorded | CP-1, CP-1A | S4 page:91 | Yes | High | Supported | Verified | High | Directly Sourced |
| North Carolina 455 over 15 years; reserves 205; 51 paid in October 2026 | CP-1, CP-1A | S4 page:116 | Yes | High | Supported | Verified; scope of 205 (I-04) | Medium | Directly Sourced |
| Cost sharing 50 percent up to 4,000; about 1,130 available | CP-1A, CP-2 | S4 page:34-35 | Yes | High | Supported | Verified | High | Directly Sourced |
| Titanium customer concentration 44 percent and 20 percent | CP-1A, CP-2 | S1 page:20 | Yes | High | Supported | Verified | High | Directly Sourced |
| Q3 2026 segment Adjusted EBITDA comparison | CP-1A, CP-2 | S4 page:133 | Yes | High | Supported | Verified | High | Directly Sourced |
| Adjusted EBITDA excludes litigation 320 and environmental 93 (FY2025); 106 and 168 (nine months 2026) | CP-1, CP-2 | S1 page:317; S4 page:133 | Yes | High | Supported | Verified | High | Directly Sourced |
| Management states covenant compliance | CP-1, CP-2 | S4 page:149 | Yes | High (attributed) | Supported | Verified as a statement; not testable | Medium | Directly Sourced |
| Revolver availability 733 if the tranche lapsed | CP-1, CP-2 | Scenario: 780 less 47 | Yes | n/a | Inferred | Labelled scenario | Low | Assumption-Based |
| Earnings rotation from refrigerants to titanium | CP-1A, CP-2 | S4 page:133 and S7 page:3 | Yes | High | Inferred | Reasonable reading of verified figures | Medium | Analyst Inference |
| Issuer behaviour toward creditors is supportive | CP-1A, CP-2 | S1 page:162; S4 page:5; S1 page:16 | Yes | High | Inferred | Reasonable reading of documented actions | Medium | Analyst Inference |

#### T5B.4 Source locator register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales 1,540 (Q3 2026), 4,512 (nine months) | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:2, income statement | CP-1 financial table | Statement | High | Verified |
| Cash 698; total liabilities 7,137 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:3, balance sheet | CP-1, CP-2 | Statement | High | Verified |
| Total equity 156 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:4 | CP-1, CP-2 | Statement | High | Verified |
| Cash from operations 263; capital expenditure 144 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:5, cash flow | CP-1 financial table | Statement | High | Verified |
| Dividends paid 39 and 63 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:6, cash flow | CP-1 financial table | Statement | High | CP-1 cited page:5 (I-02) |
| Debt components and total principal 3,872 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:24, Note 15 | CP-1 debt schedule | Note | High | Verified |
| Letters of credit 47; revolver terms | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:25-26, Note 15 | CP-1 | Note | High | Verified |
| Maturities table, total payments 3,937 | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:30, Note 15 | CP-1 maturities chart | Note | High | Verified |
| Availability 953; foreign cash 410; compliance statement | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:149, liquidity | CP-1, CP-1A, CP-2 | MD&A | High | Verified |
| Segment reconciliation (Q3, nine months) | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:133, Note 23 | CP-1 EBITDA | Note | High | Verified |
| New Jersey terms | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:91, Note 17 | CP-1, CP-1A | Note | High | Verified |
| North Carolina terms | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | page:116, Note 17 | CP-1, CP-1A | Note | High | Verified; I-04 |
| Receivables and supplier finance | source-text/10-Q_2026-09-30_cc-20260930.htm.jsonl | 10-Q Q3 2026 | S4 | pages 23, 27-29, 150 | CP-1 claims table | Note | High | Verified |
| Net sales 5,808; Adjusted EBITDA components FY2025 | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K FY2025 | S1 | page:160, page:317 | CP-1 | Statement, Note 29 | High | Verified |
| Cash 670 and 713; equity 251 and 572 | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K FY2025 | S1 | page:161, balance sheet | CP-1 | Statement | High | Verified |
| Cash interest paid 251 and 267 | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K FY2025 | S1 | page:163, cash flow | CP-1 interest cover | Statement | High | Verified |
| Debt principal 4,182 and 4,156 | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K FY2025 | S1 | page:208, Note 20 | CP-1 | Note | High | Verified |
| Covenant maximum 2.00 to 1.00 | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K FY2025 | S1 | page:211, Note 20 | CP-1 | Note | High | Verified |
| Customer concentration | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K FY2025 | S1 | page:6, page:20, Item 1 | CP-1A | Business | High | Verified |
| Net sales by region and product | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K FY2025 | S1 | pages 187-188, Note 5 | CP-1A | Note | High | Verified |
| Trailing Adjusted EBITDA 744; debt principal 3,872; ratio 4.3x | source-text/EX-99.1_2026-11-02_cc-ex99_1.htm.jsonl | Q3 release | S7 | page:13, page:4 | CP-1 | Release | Medium | Verified; attributed |
| Trailing Adjusted EBITDA 746 and 733 | source-text/EX-99.1_2026-05-05_cc-ex99_1.htm.jsonl; source-text/EX-99.1_2026-08-04_cc-ex99_1.htm.jsonl | Q1 and Q2 releases | S5, S6 | page:12; page:13 | CP-1 | Release | Medium | Verified; attributed |
| Quarterly 2025 net sales | source-text/10-K_2025-12-31_cc-20251231.htm.jsonl | 10-K FY2025 | S1 | page:319, Note 30 | CP-0 | Note | High | Verified |

#### T5B.5 Calculation register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Adjusted EBITDA FY2025 | CP-1, CP-2 | 923, 8, (181) | Segment plus other less corporate: 750 | Reproduced | Verified | Medium | Leverage denominator | S1 page:317 |
| Adjusted EBITDA FY2024 | CP-1 | 1,032, 8, (256) | 784 | Reproduced | Verified | Medium | Leverage denominator | S1 page:317 |
| LTM Adjusted EBITDA Q3 2026 | CP-1, CP-2 | 750, 616, 619 | FY2025 plus nine months 2026 less nine months 2025: 747 | Reproduced | Verified | Medium | Leverage denominator | S1 page:317; S4 page:133 |
| LTM Q1 and Q2 2026 | CP-1 | 750, 169, 167; 750, 416, 429 | 752; 737 | Reproduced | Verified | Medium | Chart rows | S2 page:112; S3 page:121 |
| Total debt / EBITDA and net debt / EBITDA | CP-1, CP-2 | 3,872, 698, 747 | 5.18x; 4.25x | Reproduced | Verified | Medium | Leverage | S4 pages 3, 24 |
| FY2025 leverage | CP-1, CP-2 | 4,182, 670, 750 | 5.58x; 4.68x | Reproduced | Verified | Medium | Leverage trend | S1 pages 161, 208 |
| Interest cover FY2024 and FY2025 | CP-1, CP-2 | 784, 267; 750, 251 | 2.94x; 2.99x | Reproduced | Verified | High | Cover | S1 page:163 |
| Liquidity 2026-09-30 | CP-1 | 698, 953 | 1,651, against 1.7 billion stated | Reproduced | Verified | High | Liquidity | S4 page:149 |
| Availability scenario | CP-1, CP-2 | 780, 47 | 733 | Reproduced | Labelled scenario | Low | Liquidity stress | S4 pages 25, 26 |
| Debt principal change | CP-1, CP-2 | 3,872, 4,182 | Negative 310 | Reproduced | Verified | High | Deleveraging | S4 page:24; S1 page:208 |
| Expense block to pre-tax income | CP-1 | Printed lines, FY2025, nine months 2026, Q3 2026 | Reconciles to (277), 200, 222 | Reproduced | Verified | High | Earnings quality | S1 page:160; S4 page:2 |
| Net sales by region and segment | CP-1A | 2,654, 1,243, 1,163, 748; 2,066, 2,429, 1,263, 50 | Each sums to 5,808 | Reproduced | Verified | High | Revenue mix | S1 pages 187-188 |
| Notes refinancing | CP-1A | 188, 495, 700 | 683 redeemed against 700 issued; net 17 | Reproduced | Verified | High | Maturity profile | S4 page:27 |
| Euro term loan balance | CP-1A | EUR 415 million less EUR 280 million | EUR 135 million | Reproduced | Verified | High | Secured debt | S4 pages 24, 26 |
| Confidence score | CP-5 | 12, 3, 1, 2 claims by lineage; 1 MATERIAL, 8 MINOR | Canon formula | Run with the canon script | Verified | High | QA | See Calculations |

#### T5B.6 Weak, inferred or untraced items

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | Availability of 733 if the tranche lapsed | Scenario, not reported | Assumption-Based | It is the only liquidity figure not printed | Obtain post-quarter facility status | CP-1 liquidity calculation; CP-2 key finding |
| MINOR | Earnings rotation toward titanium | Interpretation of verified figures | Analyst Inference | Frames business risk | None beyond labelling | CP-2 |
| MINOR | Supportive issuer behaviour | Reading of documented actions; legal capacity not assessable | Analyst Inference | Informs creditor alignment | Obtain debt documents | CP-1A governance table; CP-2 |
| MINOR | Thin equity gives no cushion | Reading of book values | Analyst Inference | Frames asset-value support | None | CP-2 |
| MINOR | Maturity row composition | Inferred, not printed (I-03) | Analyst Inference | Detail beyond printed totals | Label as inferred | CP-1 chart basis column |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Locator accuracy | Strong, one slip | 57 of 58 checks matched | A wrong page slows verification but not the figure | None on values | Fix I-02 |
| Calculation reproducibility | Strong | All derived figures recompute | Reproducible inputs prevent silent drift | Leverage and cover can be relied on within stated bases | None |
| Perimeter consistency | Consistent | All figures consolidated | A guarantor perimeter would differ | Structural subordination unassessed | Obtain guarantor data |
| Period labelling | Consistent | LTM, nine months and fiscal years labelled | Mixed periods distort ratios | Comparisons are valid | None |
| Subsequent events | Correct | October 7, 2026 maturity and October payment flagged | Blending would overstate liquidity | Liquidity is flagged, not blended | Await post-quarter status |
| Management against filing | Clear | Release figures attributed; filings control | A management ratio could override a filing | 4.3x is shown beside 4.25x | None |
| Conflict handling | Adequate | 614 against 619 logged, not reconciled | Smoothing would hide basis risk | Trend precision limited | Keep both |
| Currency and units | Consistent | USD millions throughout | Unit slips distort ratios | None | None |

#### T5B.8 Gap register

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant level, ratio and definitions | Credit Agreement, amendments, compliance certificate | Governs revolver access | Headroom Not calculable | Restricts committee use (I-01) | Credit Agreement |
| G2 | Guarantors, collateral, note terms | Indentures, guarantor list | Structural ranking | Ranking column unverified | Lowers confidence on structure | Indentures |
| G3 | Revolver after October 7, 2026 | Post-quarter facility status | Liquidity headline | Scenario only | Medium | Later filing (after cutoff, not usable) |
| G4 | Cash interest paid for 2026 | Interim supplemental cash flow | Cash interest cover | Not supplied | Medium | Issuer data |
| G5 | Executed settlement documents | JCO, North Carolina settlement, 2026 Consent Decree, MOUs | Payment timing, acceleration | Company summaries only | Medium | Court and agency documents |
| G6 | Release-basis Adjusted EBITDA for FY2024 and FY2025 | Fourth-quarter 2025 release | Basis comparability | Not supplied | Low | Q4 2025 release |
| G7 | Ownership register | Proxy statement | Alignment | Not assessable | Low | Proxy statement |
| G8 | Presentations and chart content | Decks | Visual content not reviewed | Parse limit | Low | Issuer presentations |

## Calculations

All amounts in USD millions. Inputs are from the cited pages; results were recomputed in this module.

### Debt basis check

Balance-sheet carrying debt at 2026-09-30 is current maturities 50 plus long-term debt 3,783, giving 3,833 (10-Q Q3 page:3). Total debt principal is 3,872, so the gap is 39, equal to unamortized discounts of 15 plus issuance costs of 24 (page:24). On carrying value, total debt over LTM Adjusted EBITDA of 747 is 5.13x and net debt (3,833 less 698, or 3,135) over 747 is 4.20x. At 2025-12-31: carrying debt 42 plus 4,099 equals 4,141, against principal of 4,182, a gap of 41 (discounts 21 plus costs 20); 4,141 over 750 is 5.52x and (4,141 less 670, or 3,471) over 750 is 4.63x.

### Adjusted EBITDA basis check

On the release trailing figure of 744 for Q3 2026, principal over EBITDA is 3,872 over 744, or 5.20x, and net is 3,174 over 744, or 4.27x, against 5.18x and 4.25x on the filing basis; the basis moves each ratio by 0.02x.

### Locator audit

Fifty-eight locator-and-value checks were run on the source text: page and figure for debt, cash, equity, letters of credit, segment reconciliations, settlement terms, ratings, release reconciliations and the Q1 and Q2 positions. Fifty-seven matched. The one miss is the dividends-paid line, on page:6 and not page:5 (I-02).

### Confidence score

Formula: score equals (0.6 times E plus 0.4 times C) times S less P, clamped to 0 to 100. E is the mean strongest lineage weight over 18 material claims: 12 Directly Sourced at 1.0, 3 Calculated at 0.9, 1 Assumption-Based at 0.5 and 2 Analyst Inference at 0.4, giving 88.89. C is 17 required registers present of 17, giving 100. S is 1.0 (source gate pass). P is 15 for one MATERIAL finding plus 24 for eight MINOR findings, giving 39. Score equals (0.6 times 88.89 plus 40) times 1.0 less 39, or 54.33, rounded to 54. A MATERIAL finding caps the score at 59 and sets Restricted; 54 is below the cap and falls in the Low band (40 to 59).

## Gaps

The open gaps are G1 to G8 in the gap register above. The ones that decide committee use are the Credit Agreement and compliance certificate (G1), the post-quarter status of the revolver tranche that matured on October 7, 2026 (G3) and the executed settlement documents (G5). Gaps G3 and any later facility information are dated after the evidence in hand and cannot be used in this run if dated after 2026-11-05. The nine defects (one material, eight minor) are listed in the issue log (I-01 to I-09); only I-01 restricts use.

## Next module

This is the last selected module; CP-OS assembles the report from the accepted handoffs. Before relying on the report for covenant, legal-structure or security conclusions, obtain the Credit Agreement with Amendments 1 to 4, the latest compliance certificate, the indentures with the guarantor list and the executed settlement documents, and apply fixes I-02 to I-05 in any rerun of the financial base and business context.
