## Request

Evidence trace and research-integrity review of the CP-0, CP-1, CP-1A and CP-2 handoffs for Rithm Capital Corp. (issuer id ritm), as of 2026-11-05, information cutoff 2026-11-05, run ritm-2026-11-05-credit_snapshot-host, pathway credit_snapshot, reporting currency USD, periods Q3 2026 and FY2025. This is a self-review: the same host session wrote the four handoffs it checks, so shared blind spots are possible (see Gaps). It changes no upstream conclusion and repairs no handoff; accepted answers stay as they are and corrections are stated here.

## Sources

### Issuer sources (pack files, sha256 of the pinned text file)

| Source Document ID | Source name | sha256 |
| --- | --- | --- |
| S1 | 10-K_2025-12-31_nrz-20251231.htm.jsonl | 1c6dc6fc4ac22ec0f983aa2d74b8236f15d06cb3d694e11e9adbcc9895b8a598 |
| S2 | 10-Q_2026-03-31_nrz-20260331.htm.jsonl | 767e2e953064f6127dd3b7225c6f0b5f7530f4df6d8ed091932733330f9a34a9 |
| S3 | 10-Q_2026-06-30_nrz-20260630.htm.jsonl | 6daf210aa16182f6824c848a97ad4428da4dc1534373b7320d814299eab6f84f |
| S4 | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | fe67ca59ff02f150e9ee570dc94fbca4e7146def420f7701280eb0487eeda6c4 |
| S5 | EX-99.1_2026-04-28_ritm-2026331x8xkxexhibit991.htm.jsonl | 7f51477fb7c8b90bc73114496ecaaec4ef4c755e9b5be36834e7ff89e1e4f463 |
| S6 | EX-99.1_2026-07-28_ritm-2026630x8xkxexhibit991.htm.jsonl | 67986b436cacab7f9ff46416cb7f57062e1228ff3e0789e90880132c1b737079 |
| S7 | EX-99.1_2026-10-23_ritm-2026930x8xkxexhibit991.htm.jsonl | 7701308b9bdf89d27236cd23ca8f47f1dead7d427d8e354df0b2502bcac258f6 |

Context file (user settings, not evidence): 73b514b2c18312238fd1fbb7bdc629559e11381beb8e9b95dfc9d7b54bcabe9d. Locators are `page:N`, the retained text chunk number of the named pack file.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 48c6d7ae503045da1cae2c5c7a86ddde9f062574551bdb4f6c2d47743f9e2c09 |
| CP-1 | 83dd16196f7c0aeaace81c36303ff30cf269c7cb1ac71b4f21c26c24183eec6d |
| CP-1A | adef905b89513a990eb3b2cbfde2dd6e2734465afc9bc562cb1c8a9f79d8049f |
| CP-2 | ba83b152d542e76b3ea5afd0f46a86e7c5308cbf580be20b5e2a058d7d6ffbb2 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is mostly traceable: every checked quotation, total and ratio agreed with the filings. One material error was found in the business fact pack, so committee use is restricted until it is corrected. | Medium | The review was done by the same session that wrote the analysis, and no indentures or facility agreements were available to test legal terms. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The business fact pack says the use of proceeds of the 2031 notes is not stated, but the quarterly report says part repaid borrowings. | Liquidity gained from the issue is overstated in that fact pack. | High |
| Covenant headroom, committed liquidity and the legal ranking of the senior notes rest on filing summaries only. | These creditor protections cannot be verified beyond management statements. | High |
| Five smaller defects concern an unsupported gap, a definition difference on debt, a label, an informal phrase and missing envelope fields. | None changes a conclusion, but each should be corrected in a later run. | High |

### Evidence trace view

The four upstream handoffs rest on the pinned filings and release, and the trace holds. Every one of the 65 genuine quotations in CP-0, CP-1, CP-1A and CP-2 was found in a pack file, and the 53 that carry an exact page locator sit on the cited page. Every statement total, maturity table, borrowing-capacity table and cash roll-forward re-added to the printed figure, and every derived ratio in CP-1, CP-1A and CP-2 recomputed to the stated value. The trace also found defects. The most important is in CP-1A: it states that the use of proceeds of the 8.500% senior notes due 2031 is not stated and that the issue adds to cash, while the Q3 2026 10-Q says part of the net proceeds repaid outstanding borrowings (S4 page:59). CP-1A also lists employees as not supplied when the 10-K states the count (S1 page:41), and its segment debt total includes the tax receivable agreement liability that CP-1 excludes from debt. CP-1 labels the maturity table basis as net of issuance costs when its own arithmetic shows principal. None alters the credit conclusions in CP-2, which relies on figures that were verified, but the first affects the liquidity effect described for the 2031 issue and is graded Material. The analysis cannot be traced further on covenant definitions, the legal ranking of the notes or committed liquidity, because the indentures and facility agreements are not in the pack; those claims are carried as inferences or gaps and are labelled so.

### Traceability conclusion

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the indentures and facility agreements, which matters because covenant headroom, committed liquidity and the legal ranking of the senior notes rest on filing summaries, and implies that committee use stays restricted until those documents are read. One material defect needs correction: the business fact pack says the use of proceeds of the 2031 notes is not stated, but the quarterly report says part repaid borrowings. Every other checked quotation, tie-out and recomputed figure agreed.

| Traceability summary | Result |
| --- | --- |
| Genuine quotations checked against pack files | 65 found; 3 further spans were parser artifacts, not quotations |
| Quotations with an exact page locator | 53 of 53 on the cited page |
| Statement totals and tables re-added | 27 of 27 equal |
| Derived figures recomputed | 38 of 38 equal |
| Material claims by lineage | 5 Directly Sourced, 2 Calculated, 2 Analyst Inference, 1 Insufficient Information |
| Open findings | 1 MATERIAL, 5 MINOR |
| Confidence Score and status | 30; qa_status Restricted; committee_status Requires More Work |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_nrz-20251231.htm.jsonl | High: filed annual report with unqualified audit opinion | Year ended December 31, 2025 | Rithm Capital Corp. and subsidiaries, consolidated | Statements, debt note, business, employees, acquisitions | Text extraction; Part III incorporated by reference to an unsupplied proxy | CP-0, CP-1, CP-1A |
| S2 | 10-Q_2026-03-31_nrz-20260331.htm.jsonl | High: filed unaudited interim report | Quarter ended March 31, 2026 | Same | Interim statements | Not used for figures | CP-0 |
| S3 | 10-Q_2026-06-30_nrz-20260630.htm.jsonl | High: filed unaudited interim report | Quarter ended June 30, 2026 | Same | Interim statements | Not used for figures | CP-0 |
| S4 | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | High: filed unaudited interim report, signed October 30, 2026 | Quarter and nine months ended September 30, 2026 | Same | Statements, Note 17, maturities, capacity, covenants, segments, commitments | Text extraction; tables flattened | CP-0, CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-28_ritm-2026331x8xkxexhibit991.htm.jsonl | Medium: issuer earnings release | Q1 2026 | Same | Management narrative and non-GAAP measure | Management-attributed | CP-0 |
| S6 | EX-99.1_2026-07-28_ritm-2026630x8xkxexhibit991.htm.jsonl | Medium: issuer earnings release | Q2 2026 | Same | Management narrative and non-GAAP measure | Management-attributed | CP-0 |
| S7 | EX-99.1_2026-10-23_ritm-2026930x8xkxexhibit991.htm.jsonl | Medium: issuer earnings release | Q3 2026 with Q2 2026 comparison | Same | Highlights, balance sheet, non-GAAP reconciliation | Management-attributed; balance sheet comparative is June 30, 2026 | CP-0, CP-1A |

Module Status: Ready with Limitations (all four handoffs and all seven pack files available; legal documents, ratings and decks absent). Traceability Scope: Top 5, plus a ten-claim map used for the Confidence Score.

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Maturity profile and recourse split | CP-1, CP-2 | Contractual maturities of 37,877,221 thousand, recourse 19,680,259 thousand, Q4 2026 7,546,015 thousand, 2027 10,619,584 thousand | Rollover of short-dated secured lines drives default and liquidity risk | Sets refinancing risk and monitoring horizon | S4 page:57; page:169 | MD&A total debt of 38.1 billion unreconciled |
| 2 | Uncommitted capacity against modest cash | CP-1, CP-2 | Available financing 10,785,284 thousand stated uncommitted; unrestricted cash 1,708,750 thousand | Capacity can shrink when collateral values fall | Sets liquidity view | S4 page:57; page:44 | Committed amounts not supplied |
| 3 | Leverage on equity, total and recourse | CP-1, CP-2 | 4.39x and 2.28x on principal basis | Equity cushion against a large funding stack | Sets leverage tolerance | S4 page:7; page:57 | Not a covenant measure; no EBITDA |
| 4 | Earnings cover and segment results | CP-1, CP-1A, CP-2 | Cover of 1.54x; Origination and Servicing pre-tax 968,563 thousand; Asset Management (83,484) and Commercial Real Estate (74,855) thousand | Rate-sensitive earnings fund interest | Sets debt service view | S4 page:8; page:25 | Includes MSR fair value; acquisitions distort comparison |
| 5 | Structural position of the senior notes | CP-1A, CP-2 | Notes unsecured, not guaranteed at issuance; large secured and non-recourse debt | Residual value after other claims | Sets loss given default mechanic | S4 page:56; page:59 | Indentures not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Maturities and recourse split | CP-1 | S4 page:57 table of contractual maturities | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Uncommitted capacity and unrestricted cash | CP-1 | S4 page:57 note A; page:44 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Debt to equity 4.39x and 2.28x | CP-1 | S4 page:57 and page:7 inputs | Yes | High | Calculated | Supported | High | Committee-Ready |
| Earnings cover 1.54x | CP-1 | S4 page:8 inputs | Yes | High | Calculated | Supported | Medium | Committee-Ready |
| Origination and Servicing profit concentration | CP-1A | S4 page:24 to page:25 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Senior notes unsecured, not guaranteed at issuance | CP-1A | S4 page:59; page:60; page:62 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Covenant compliance statement | CP-1 | S4 page:57 | Yes | High; management statement | Directly Sourced | Supported as a statement | Medium | Committee-Ready |
| Structural subordination and recovery mechanic | CP-2 | S4 page:56; page:59 and CP-1 maturity split | Yes | High inputs | Analyst Inference | Supported by inference | Medium | Remediation Needed |
| Governance neutral on documented actions | CP-1A, CP-2 | S4 page:121 to page:123; page:111 | Yes | High inputs | Analyst Inference | Supported by inference | Medium | Committee-Ready |
| Legal capacity under the notes (priming, debt, payments) | CP-1A | Indentures not in the pack | No source exists in the set | Not available in the set | Insufficient Information | Open gap, correctly labelled | Low | Gap correctly labelled |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Contractual maturities total 37,877,221 thousand | /workspace/secdata/data/2026-11-05/packs/1556593-rithm-capital-corp-ritm-ritm-pf-ritm-pe | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:57, Maturities | CP-1 chart data | Sourced | High | Components re-added equal |
| Unrestricted cash 1,708,750 thousand | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:44, Note 12 | CP-1 liquidity | Sourced | High | Cash reconciliation re-added equal |
| Available financing 10,785,284 thousand, uncommitted | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:57, Borrowing Capacity | CP-1 liquidity | Sourced | High | Eight lines re-added equal |
| Net income nine months 2026 438,665 thousand | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:8, statement of operations | CP-1 financials | Sourced | High | Matches |
| Interest expense nine months 2026 1,395,011 thousand | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:8 | CP-1 financials | Sourced | High | Matches |
| Operating cash flow nine months 2026 (1,313,851) thousand | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:12 | CP-1 financials | Sourced | High | Matches |
| Segment pre-tax: O&S 968,563; AM (83,484); CRE (74,855) thousand | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:25, nine months 2026 | CP-1A segment table | Sourced | High | Segments sum to 760,219 |
| Senior notes 775,000, 500,000 and 500,000 thousand principal | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:58 to page:63; page:168 | CP-1 debt register | Sourced | High | Principal sum bridges to maturity table |
| Compliance with all debt covenants | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:57 | CP-1 covenants | Sourced | High | Management statement |
| MD&A total outstanding debt 38.1 billion | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:167 | CP-1 conflicts | Sourced | High | Conflicts with maturity table; logged by CP-0 and CP-1 |
| Crestline cash consideration 324,719 thousand | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:20 | CP-1A transaction summary | Sourced | High | Matches |
| Paramount total consideration about 1.8 billion | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:20 | CP-1A transaction summary | Sourced | High | Composition not stated |
| Use of proceeds: part repaid outstanding borrowings | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:59 | Not carried by CP-1A | Sourced | High | CP-1A says not supplied |
| Employees about 7,240, of which 5,630 in Origination and Servicing | same | 10-K_2025-12-31_nrz-20251231.htm.jsonl | S1 | page:41, Human Capital | Not carried by CP-1A | Sourced | High | CP-1A says not supplied |
| Series F preferred net proceeds about 242.1 million | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:111 | CP-1A transaction summary | Sourced | High | Matches |
| Segment debt 30,154,238 thousand | same | 10-Q_2026-09-30_nrz-20260930.htm.jsonl | S4 | page:25 | CP-1A segment table | Sourced | High | Includes tax receivable agreement 151,677 thousand |
| Total debt FY2025 maturities 35,443,392 thousand | same | 10-K_2025-12-31_nrz-20251231.htm.jsonl | S1 | page:314 | CP-1 financials | Sourced | High | Bridges to Note 17 plus principal |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Face to maturity-table bridge | CP-1 calculations 1; CP-2 | 36,102,221 and principal 775,000, 500,000, 500,000 thousand, Sep 30, 2026 | 36,102,221 + 1,775,000 = 37,877,221 | Calculated; recomputed equal | Supported | High | Refinancing, debt basis | S4 page:54; page:57; page:168 |
| Recourse share | CP-1 calculations 3 | 19,680,259 over 37,877,221 thousand | 19,680,259 / 37,877,221 = 0.5196 | Calculated; recomputed equal | Supported | High | LGD, structure | S4 page:57 |
| Near-term maturities | CP-1 calculations 4; CP-2 | 7,546,015 and 10,619,584 thousand; recourse 6,230,073 and 6,736,955 | Sum; share 18,165,599 / 37,877,221 = 0.4796 | Calculated; recomputed equal | Supported | High | Refinancing | S4 page:57 |
| Cash cover of nearest recourse maturity | CP-1 calculations 4; CP-2 | 1,708,750 and 6,230,073 thousand | 1,708,750 / 6,230,073 = 0.2743 | Calculated; recomputed equal | Supported | High | Liquidity | S4 page:44; page:57 |
| Debt to equity, principal basis | CP-1 calculations 6; CP-2 | 37,877,221 and 35,443,392 over equity 8,620,062 and 8,430,487 thousand | Total / equity; recourse 19,680,259 and 19,496,781 over the same equity | Calculated; recomputed 4.394, 4.204, 2.283, 2.313 equal | Supported | High | Leverage tolerance | S4 page:7; page:57; S1 page:314 |
| Earnings cover of interest | CP-1 calculations 7; CP-2 | Pre-tax income and interest expense, three periods | (pre-tax + interest) / interest = 1.485, 1.484, 1.545 | Calculated; recomputed equal | Supported with caveat | Medium | Debt service | S1 page:229; S4 page:8 |
| Effective tax rates and income change | CP-2 calculations 4 and 5 | Tax 257,819 over pre-tax 519,093; 321,554 over 760,219; net income 438,665 against 627,514 | Ratios 0.4967, 0.4230 and change -0.3009 | Calculated; recomputed equal | Supported | High | Earnings quality | S4 page:8 |
| EBITDA based leverage and cover | CP-1 chart data | No EBITDA reported | Not applicable by design | Not Calculable from Provided Materials | Correctly reported as Not supplied | High | Leverage and cover | S4 page:8 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial source gate, 1 MATERIAL, 5 MINOR | scripts/confidence_score.py formula | Script output 30 | Supported | High | QA envelope | Calculations Q4 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | Use of proceeds and liquidity effect of the 2031 notes | CP-1A says the use of proceeds is not stated and that the issue adds to cash; S4 page:59 says part of the net proceeds repaid outstanding borrowings | Conflicting | The net liquidity gain is lower than the headline proceeds, and the borrowings repaid are not named | State the repayment, keep the unnamed borrowings as the residual gap | CP-1A transaction summary and gaps |
| MINOR | Employee count | CP-1A lists employees as not supplied; S1 page:41 gives about 7,240 | Weak Lineage | A gap the sources can fill | Cite S1 page:41 in a later run | CP-1A company profile and gaps |
| MINOR | Segment debt total | 30,154,238 thousand includes the tax receivable agreement 151,677 thousand, which CP-1 keeps outside debt | Conflicting | Debt definitions differ across modules by 0.5 percent | Label the inclusion or restate on the CP-1 basis | CP-1A company and operating model |
| MINOR | Maturity table basis | CP-1 says the table includes senior notes net; the arithmetic shows principal | Weak Lineage | Mislabelled basis | Relabel as principal | CP-1 chart data, debt maturities |
| MINOR | Corporate category description | CP-1A says "no operating revenue to speak of" while the segment table shows 7,989 thousand of interest income | Analyst Inference | Informal, unquantified wording | Quote the figure | CP-1A company and operating model |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven pack files cover FY2025 and four quarters; no indentures, facility agreements, ratings or decks | Legal terms rest on filing summaries | Covenant and ranking claims stay inferences | Obtain the legal documents |
| Citation completeness | Ready with Remediation | 65 of 65 genuine quotations found; 2 gaps stated as not supplied are filled by the sources | A false gap can understate what is known | Use of proceeds and liquidity effect misstated | Correct in a later run |
| Calculation traceability | Committee-Ready | 38 of 38 derived figures and 27 of 27 tie-outs recomputed equal | Calculation errors would move leverage and liquidity | None found | None |
| Assumption transparency | Committee-Ready | No forward assumptions; inferences labelled Analyst Interpretation | Hidden assumptions would mislead | None found | None |
| Markdown and export artifact integrity | Committee-Ready | All four handoffs accepted at attempt 1 with the six required headings | A malformed handoff breaks the chain | None found | None |
| Reviewer independence | Not Committee-Ready | Same host wrote and checked the handoffs | Errors of omission are least likely to be found by the author | Residual defects may remain | Independent review |

Overall auditability follows the lowest dimension: Not Committee-Ready on independence, Ready with Remediation on the content dimensions.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Indentures and facility agreements not in the pack | The 2029, 2030 and 2031 indentures and warehouse and repurchase agreements | Covenant levels, Total Unencumbered Assets and legal ranking cannot be verified; headroom unknown | Governance, structural position, covenant rows | High impact | Indentures dated March 19, 2024, June 20, 2025, May 14, 2026 and the facility agreements |
| CP-5-GAP-002 | Committed undrawn liquidity not supplied | Committed amounts by lender | True liquidity headroom cannot be measured | Liquidity assessment | High impact | Facility agreements and lender schedules |
| CP-5-GAP-003 | No EBITDA or adjusted EBITDA | Issuer definition | Conventional leverage and cover ratios cannot be reported | Leverage and cover charts | Medium impact | Management bridge, labelled external |
| CP-5-GAP-004 | Credit ratings not in the pack | Agency ratings and dates | No external view of default risk | Assessment confidence | Medium impact | Agency publications, labelled external |
| CP-5-GAP-005 | Ownership and control not supplied | 2026 proxy statement | Alignment and control unassessed | Governance row | Medium impact | Definitive proxy statement |
| CP-5-GAP-006 | Borrowings repaid from the 2031 note proceeds not named | Name and amount of repaid borrowings | Net liquidity effect of the issue cannot be sized | Liquidity effect of the 2031 issue | Medium impact | Offering memorandum or 8-K |
| CP-5-GAP-007 | Composition of the Paramount consideration not read | Cash, equity and assumed debt split | Cash and leverage effect of the acquisition cannot be tied to the headline | Acquisition row | Low impact | 10-K Note 3 in full, merger documents |
| CP-5-GAP-008 | Self-review only | Independent reviewer | Shared blind spots may remain | Whole run | High impact | Second agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / ritm-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted; no front matter under Markdown transport | Passed with no content defect | All quotations found; one sentence refined later by CP-1 |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, debt, maturities, liquidity, covenants | High | Six headings; accepted | Passed with two MINOR defects, one shared with CP-1A | All derived figures and tie-outs equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, segments, transactions, governance | High | Six headings; accepted | Restricted: one MATERIAL and three MINOR defects | Two false gaps, one definition difference, one wording |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted | Passed with no content defect | Figures all found in CP-1 or CP-1A |

Module Status: Ready with Limitations.

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A | Transaction summary: use of proceeds of the 2031 notes not stated; liquidity effect "adds to cash" | Conflicting | S4 page:59 states "The Company used a portion of the net proceeds from issuance to repay certain outstanding borrowings." The same page also states a 101% repurchase right for the 2031 notes, which CP-1A lists only for the 2029 and 2030 notes | State the repayment; keep the borrowings repaid as the residual gap | Restricts Committee Use |
| MINOR | CP-1A | Company profile and gaps: employees not supplied | Unsupported | S1 page:41 states "we employed approximately 7,240 employees, of which 5,630 employees were in Origination and Servicing" | Add the count and its locator | Monitoring Follow-Up |
| MINOR | CP-1A | Company and operating model: corporate category "no operating revenue to speak of" | Partially Supported | The segment table shows 7,989 thousand of interest income for the corporate category (S4 page:24) | Quote the figure | Formatting / Hygiene Only |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Maturity chart basis says the table includes senior unsecured notes net | The source footnote says "unsecured notes, net of issuance costs" (S4 page:57), but 36,102,221 + 1,775,000 = 37,877,221 equals the table total, so the table carries principal; net would be 1,755,476 | Footnote wording against arithmetic | Relabel the basis as principal | Formatting / Hygiene Only |

All other CP-1, CP-1A and CP-2 calculations show formula, inputs, period and unit and recompute equal (T5B.5).

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A, CP-2 | Senior notes unsecured, not guaranteed by subsidiaries at issuance, structurally behind other claims | 2029, 2030 and 2031 indentures | Filing summary only; the structural ranking is an analyst reading of it and is labelled so | Obtain the indentures before relying on ranking | Required before any recovery or ranking use |
| MINOR | CP-1 | 120% Total Unencumbered Assets test and compliance statement | 2029, 2030 and 2031 indentures | Definition and Total Unencumbered Assets not supplied; headroom correctly reported as Not calculable | Obtain the indentures | Required for headroom |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No bond price, spread, yield, peer set or relative-value claim is made; none appears in the handoffs | Prices, spreads and ratings are outside the minimum source pack | Absent by design and stated | Add a market module only with sourced market data | The committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | Debt definitions differ: CP-1A segment debt total 30,154,238 thousand includes the tax receivable agreement 151,677 thousand; CP-1 carrying debt excluding consolidated entities is 30,002,561 thousand (14,235,647 + 14,011,438 + 1,755,476) | Both cite the same 10-Q pages; no version conflict | Label the inclusion in CP-1A or restate on the CP-1 basis | None on conclusions; CP-2 uses the CP-1 basis |

Cross-module checks that agreed: issuer name and period in all four handoffs; the three totals on debt (CP-0 listed them as unreconciled, CP-1 bridged two and left the MD&A figure open, CP-2 and CP-1A use the CP-1 basis); cash scopes; senior note terms; segment figures; maturities and ratios in CP-2 against CP-1.

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A | Unsupported wording | "no operating revenue to speak of" is informal and unquantified (see T5.2) | Quote the figure | None |
| MINOR | CP-1, CP-1A, CP-2 | Repetition | The absence of indentures, ratings and committed liquidity is restated in each handoff's gaps; useful for a stand-alone reader, repetitive for a committee pack | Keep one statement per report | None |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Envelope fields | The method's canonical envelope lists confidence score, qa_status and limitation flags in front matter; the four handoffs carry none, because the Markdown transport of this run uses six headings and a run manifest instead | None for this run; the manifest carries run identity and hashes | None for CP-OS; a consumer expecting front matter must read the manifest |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-1A | Conflicting Evidence | Use of proceeds of the 2031 notes stated as not supplied, and liquidity effect stated as adding to cash, against S4 page:59; 101% put for the 2031 notes also omitted | State the partial repayment of borrowings; keep the residual gap | Restricts Committee Use | Open |
| CP5-002 | MINOR | CP-1A | Citation Gap | Employees stated as not supplied; S1 page:41 gives about 7,240 | Add the count | Monitoring Follow-Up | Open |
| CP5-003 | MINOR | CP-1, CP-1A | Formula / Definition Drift | Segment debt includes the tax receivable agreement, CP-1 debt does not | Label or restate | Requires Source Reconciliation | Open |
| CP5-004 | MINOR | CP-1 | Source Quality Limitation | Maturity table labelled net of issuance costs; arithmetic shows principal | Relabel | Formatting / Hygiene Only | Open |
| CP5-005 | MINOR | CP-1A | Promotional or Non-Credit Language | Informal wording on corporate category revenue | Quote the figure | Formatting / Hygiene Only | Open |
| CP5-006 | MINOR | All | canonical Markdown Handoff Integrity Defect | Front-matter envelope fields absent under the Markdown transport | None for this run | Formatting / Hygiene Only | Open |

#### Remediation priority map

Must-fix before committee: CP5-001. Correct the CP-1A statement on the use of proceeds and the liquidity effect of the 2031 notes, citing S4 page:59.

Must-fix before the Markdown handoff is consumed downstream: CP5-003. Make the debt definition used in the segment table explicit so CP-2 and later modules use the CP-1 basis.

Monitoring follow-up: CP5-002 and the gaps CP-5-GAP-001 to CP-5-GAP-008. Add the employee count; obtain the indentures, facility agreements, ratings, proxy statement and an independent review.

Formatting and hygiene: CP5-004, CP5-005 and CP5-006. Relabel the maturity basis, quote the corporate revenue figure, and note the envelope divergence.

#### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 1. Minor Issues: 5. Committee Use: Restricted.

No finding changes a credit conclusion, so there is no Critical issue. The Material issue, CP5-001, misstates the liquidity effect and the known use of proceeds of the 2031 notes in the business fact pack, and it must be disclosed to any committee that reads that fact pack; the severity engine sets qa_status to Restricted. The Confidence Score is 30 (band Insufficient Information) because of the partial source gate, one Material and five Minor findings; committee_status is Requires More Work.

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Every double-quoted span of at least 12 characters in the four handoffs was searched in all pages of all seven pack files; those written with a page locator were searched on the cited page | 68 spans parsed, 3 were parser artifacts (text between two quotations); 65 genuine quotations all found; 53 with a page locator all on the cited page |
| Q2 | Derived figure recomputation | Inputs read from the cited pages; each figure recomputed with exact arithmetic: 27 in CP-1 (bridges, carrying totals, recourse shares, near-term sums and shares, cash cover, capacity sums, four debt to equity ratios, three earnings covers, cash difference, two cash reconciliations), 5 in CP-1A (segment sums), 6 in CP-2 (cash cover, notes share, two tax rates, two changes) | 38 of 38 equal to the handoff values |
| Q3 | Tie-outs | Balance sheet totals (assets, liabilities, equity) at Sep 30, 2026 and Dec 31, 2025 (6); statements of operations Q3 2026, nine months 2026 and FY2025 to pre-tax income and net income (6); maturity tables non-recourse, recourse and total at both dates (6); borrowing capacity and outstanding totals (2); net change in cash for nine months 2026 and FY2025 (2); Note 17 face and carrying subtotals and total (5) | 27 of 27 equal |
| Q4 | Confidence Score | `python3 confidence_score.py --lineage "Directly Sourced:5,Calculated:2,Analyst Inference:2,Insufficient Information:1" --fields-present 17 --fields-total 17 --source-gate partial --findings MATERIAL:1,MINOR:5` | score = clamp((0.6 × 76 + 0.4 × 100) × 0.7 − 30) = 29.92, rounded to 30; band Insufficient Information; qa_status Restricted |
| Q5 | Segment debt against CP-1 debt | 30,154,238 − (14,235,647 + 14,011,438 + 1,755,476) = 151,677, equal to the tax receivable agreement liability | Definition difference confirmed |

## Gaps

- CP-5-GAP-001 (high impact): the indentures and facility agreements are not in the pack, so covenant levels, Total Unencumbered Assets, legal ranking and committed liquidity cannot be verified.
- CP-5-GAP-002 and CP-5-GAP-003: committed undrawn liquidity and any EBITDA definition are not supplied.
- CP-5-GAP-004 and CP-5-GAP-005: credit ratings and the proxy statement are not in the pack.
- CP-5-GAP-006 and CP-5-GAP-007: the borrowings repaid from the 2031 note proceeds and the composition of the Paramount consideration are not named in the text read.
- CP-5-GAP-008 (high impact): this review is a self-review by the host that wrote the handoffs; an independent check should start with omissions.

## Next module

- Report delivery: carry qa_status Restricted, Confidence Score 30 (band Insufficient Information), committee_status Requires More Work, issue CP5-001 and gap CP-5-GAP-001, and the corrections stated here (use of proceeds, employee count, segment debt definition, maturity basis) alongside the business fact pack and financial base.
- Independent review: another agent or model should repeat this check, checking claims of absence first.
- Sourcing: fetch the three indentures, the facility agreements, the 2026 proxy statement and any agency ratings, then rerun in a new run folder.
