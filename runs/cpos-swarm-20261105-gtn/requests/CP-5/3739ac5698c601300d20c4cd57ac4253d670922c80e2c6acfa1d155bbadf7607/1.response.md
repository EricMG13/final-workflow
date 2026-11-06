# CP-5 evidence trace and research-integrity QA: GRAY MEDIA, INC (gtn)

## Request

This handoff checks the evidence trace behind the CP-0, CP-1, CP-1A and CP-2 handoffs for GRAY MEDIA, INC (ticker GTN) as of 2026-11-05, on the credit_snapshot pathway, and grades the result (the absorbed CP-5A phase). Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most. The same host session wrote the four handoffs it checks, so this is a self-review, not an independent one. QA envelope: qa_status Restricted; Confidence Score 25, band Insufficient Information (from `scripts/confidence_score.py`, see Calculations); committee_status Restricted.

## Sources

### Issuer sources behind the checked handoffs

| Exact source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_gtn20251231_10k.htm.jsonl | 88cd2be27d00e9908e881a07fffdbfb7e9fbcb182cd4daa7213df1b4b5f00737 |
| 10-Q_2025-09-30_gtn20250930_10q.htm.jsonl | b62445e5fe4a163fa362c47bf83e36bde2a987867496619de6fe27a40edfa171 |
| 10-Q_2026-03-31_gtn20260331_10q.htm.jsonl | 3356f048b1cdb10c04c5b80b0d02babf79237e5dc24d851924643abb820dcebd |
| 10-Q_2026-06-30_gtn20260630_10q.htm.jsonl | e96d90052b60b94fa2a12b7f9024364ed7aff9961690c651cc002284f695a02b |
| EX-99.1_2026-02-26_ex_924265.htm.jsonl | 178b7bc5710105291e494cc784bd65c8c9bce375e1552cc63408e1853ff6a993 |
| EX-99.1_2026-05-07_ex_956963.htm.jsonl | b04f43ebe7b79436fed34dc07bcf8f9f9fb0c9fac32a39299a3e02ac7ae325d8 |
| EX-99.1_2026-08-07_ex_998938.htm.jsonl | 1120ddd52748c4fbbc1c17f2a7297d8e7f38db5b861bb6f5b9064b68dbae4a0d |

The run context (sha256 457b491e723cfaa80de6921ac6aa99b1d24251f7cfebd35fd33b60ef8d3cb70e) supplies identity and period labels only and is not issuer evidence. Locators are `page:N` chunks of the pinned text files, not printed pages.

### Handoffs supplied

| Module | sha256 |
| --- | --- |
| CP-0 | e77a699cb806587c5833b538af86a669d2f7b40e236fe396a25b387c082542af |
| CP-1 | a5ba76a02d9bf3a11ff3c18cbb17b33ee63a8d295903f868edffbbc7e544712a |
| CP-1A | 8f6aed0d9aef7292573fab42193a9c269238361033f8ea127bc6b36df2c75a02 |
| CP-2 | 1506103a7ec410c2f6206a76b3137cde546f490f8ed028d31fd403044ef1af5e |

CP-2 attempt 2 is the accepted version; attempt 1 was refused and is not checked.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial, debt and liquidity figures trace to the filings and recompute exactly, but the ownership view does not: the 10-K names an influential family that two handoffs call unidentified. Committee use is restricted. | Low | One session wrote and checked every module, so omissions are the likeliest remaining defects; legal documents and post-June data are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 54 recomputed figures equal the handoffs, and all 83 checked quotations sit on their cited pages. | The leverage, cover, liquidity and debt figures behind the credit view can be relied on as sourced. | High |
| The 10-K says the Howell-Robinson Family can exert significant influence over policies and management, while two handoffs say holders are unidentified. | Control and alignment risk is understated; creditors should treat family influence as a documented governance risk. | High |
| The 14 gap between consideration and cash paid for 2026 closings, called unexplained, is explained by 13 of timing on one station plus 1 of rounding. | The false gap does not change leverage or liquidity but weakens the acquisition cost trace. | High |
| Covenant terms, the revolver draw after July 2026 and the quarter ended September 2026 remain unsupplied. | Headroom and post-June liquidity stay issuer-described or unseen. | High |

### Evidence trace view

The run is traceable for its financial, debt and liquidity facts and only partly for its ownership and control view, so committee use is restricted. The strongest support is arithmetic: all 54 metrics and tie-outs recompute from the source pages to the handoffs' values, and no quotation is misplaced. The weakest point is that the handoffs declared holders unidentified and an acquisition cash difference unexplained when the filings answer both, which is a gap the sources could fill. What would change the view is the executed credit agreement and indentures, the proxy statement, the purchase agreements and the September 30, 2026 balance sheet. The critical provenance gap for the decision is control: the Howell-Robinson Family influence and the revolver position after July 21, 2026. Remediation owner: the sourcing step, then a rerun of CP-1A, CP-2 and CP-5.

### Traceability summary

| Check | Result |
| --- | --- |
| Quotations checked against cited pages | 83 in the four handoffs; none misplaced |
| Metrics and tie-outs recomputed from the source pages | 54 of 54 equal |
| CP-2 figures found in CP-1 or CP-1A | All found |
| Material claims by lineage | 3 Directly Sourced, 5 Calculated, 1 Analyst Inference, 2 Weak Lineage, 2 Insufficient Information |
| Open findings | 1 MATERIAL, 5 MINOR |
| Independent review | None; self-review |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S-10K | 10-K_2025-12-31_gtn20251231_10k.htm.jsonl | High: filed, audited annual report | Years ended December 31, 2025, 2024 and 2023 | Gray Media, Inc., consolidated | Statements, debt note, covenant schedule, business, regulation, risk factors, equity, preferred stock | Text extraction; Part III incorporated from a proxy statement not supplied | CP-0, CP-1, CP-1A, CP-2 |
| S-Q3-25 | 10-Q_2025-09-30_gtn20250930_10q.htm.jsonl | High: filed, unaudited interim report | Three and nine months ended September 30, 2025 | Same | Q3 2025 statements and leverage schedule | Text extraction; unaudited | CP-0, CP-1 |
| S-Q1-26 | 10-Q_2026-03-31_gtn20260331_10q.htm.jsonl | High: filed, unaudited interim report | Three months ended March 31, 2026 | Same | Debt table, leverage schedule, pending transactions | Text extraction; unaudited | CP-0, CP-1, CP-1A |
| S-Q2-26 | 10-Q_2026-06-30_gtn20260630_10q.htm.jsonl | High: filed, unaudited interim report | Three and six months ended June 30, 2026 | Same | Statements, debt note, covenants, acquisitions, subsequent events | Text extraction; unaudited | CP-0, CP-1, CP-1A, CP-2 |
| S-R-Feb | EX-99.1_2026-02-26_ex_924265.htm.jsonl | Medium: issuer earnings release | Fourth quarter and year ended December 31, 2025 | Same | Adjusted EBITDA reconciliation, debt summary | Management non-GAAP presentation | CP-1, CP-1A |
| S-R-May | EX-99.1_2026-05-07_ex_956963.htm.jsonl | Medium: issuer earnings release | Quarter ended March 31, 2026 | Same | Q1 2026 results and financing events | Management non-GAAP presentation | CP-1, CP-1A |
| S-R-Aug | EX-99.1_2026-08-07_ex_998938.htm.jsonl | Medium: issuer earnings release | Quarter and six months ended June 30, 2026 | Same | Q2 2026 results, financing, guidance | Management non-GAAP presentation; forward guidance | CP-1, CP-1A, CP-2 |
| CTX | context | User settings, not issuer evidence | Run date 2026-11-05 | Run identity | Currency, period labels | Not issuer evidence | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage on actual earnings: principal debt 5,867 over LTM Adjusted EBITDA 709 is 8.28x, against covenant total net leverage of 5.73x | CP-1, CP-2 | Debt table and covenant schedule in the 10-Q; Adjusted EBITDA reconciliations in the releases | Sets leverage tolerance and covenant optics | Core leverage metric | S-Q2-26 page:15, page:37; S-R-Aug page:12; S-R-Feb page:11 | Adjusted EBITDA is release-only |
| 2 | Thin coverage: cash interest cover 1.84x and free cash flow after dividends of 59 | CP-1, CP-2 | Interest paid and cash flow statements | Little cash for debt reduction | Debt-service capacity | S-10K page:75, page:94; S-Q2-26 page:5, page:16 | Cash interest timing is semiannual |
| 3 | Back-ended maturities: nothing before December 2028, then 3,872 to 2031 | CP-1, CP-2 | Maturity table | Refinancing concentration | Monitoring horizon | S-Q2-26 page:16 | Revolver draw after July 21, 2026 unseen |
| 4 | Retransmission erosion and election-year earnings swing | CP-1A, CP-2 | Revenue mix and drivers | Fee income shrinking, political income cyclical | Earnings durability | S-10K page:49; S-Q2-26 page:28, page:31 | Contract terms not supplied |
| 5 | Control by the Howell-Robinson Family and Class A voting | CP-1A, CP-2 | Risk factors and share counts | Alignment with creditors and decision rights | Governance view | S-10K page:38, page:45, page:97; S-Q2-26 page:2 | Holdings not quantified; proxy statement not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 5,867 and maturities by year | CP-1 | S-Q2-26 page:15, page:16 | Yes | High | Directly Sourced | Supported | High | Traced and recomputed equal |
| Covenant ratios 5.73x, 3.71x and 2.55x with denominator 994 | CP-1, CP-2 | S-Q2-26 page:37 | Yes | High; issuer calculation | Directly Sourced | Supported as an issuer statement | Medium | Traced |
| Retransmission 46% of FY2025 revenue and political cycle | CP-1A, CP-2 | S-10K page:49; S-Q2-26 page:28 | Yes | High | Directly Sourced | Supported | High | Traced |
| LTM Adjusted EBITDA 709 and leverage 8.28x | CP-1, CP-2 | S-10K page:73; S-R-Feb page:11; S-R-Aug page:12 | Yes | High inputs; release-only measure | Calculated | Supported | Medium | Recomputed equal |
| Cash interest cover 1.84x | CP-1, CP-2 | S-10K page:94; S-Q2-26 page:16 | Yes | High | Calculated | Supported | High | Recomputed equal |
| Liquidity 921 | CP-1, CP-2 | S-Q2-26 page:2, page:15 | Yes | High | Calculated | Supported at June 30, 2026 | High | Recomputed equal |
| Secured share 65.8% of principal | CP-1A, CP-2 | S-Q2-26 page:37; S-R-Feb page:3; S-10K page:57 | Yes | High | Calculated | Supported | High | Recomputed equal |
| Class A holds 51.5% of votes | CP-1A, CP-2 | S-Q2-26 page:2; S-10K page:45 | Yes | High | Calculated | Supported at July 31, 2026 | High | Recomputed equal; 52.2% at February 20, 2026 |
| First lien 4.25x cap triggered by revolver draw or letters of credit above 50 | CP-1, CP-2 | S-Q2-26 page:35, page:37 | Yes | High; issuer description of two passages | Analyst Inference | Supported as an inference | Medium | Inference flagged in the handoffs |
| Revolver draw and liquidity after July 21, 2026 | CP-1, CP-2 | No source in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Covenant headroom under executed terms | CP-1, CP-2 | Executed credit agreement not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Holders and controlling influence "not identified" | CP-1A, CP-2 | S-10K page:38 names the Howell-Robinson Family | Citation contradicts the claim | High | Weak Lineage | Unsupported as stated | Low | Gap overstated (QA-1) |
| Acquisition consideration 278 against cash paid 264 "not explained" | CP-1A, CP-2 | S-Q2-26 page:11 explains it | Citation contradicts the claim | High | Weak Lineage | Unsupported as stated | Low | Gap overstated (QA-2) |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 5,867 at June 30, 2026 | /workspace/secdata/data/2026-11-05/packs/43196-gray-media-inc-gtn-gtn-a | 10-Q_2026-06-30_gtn20260630_10q.htm.jsonl | S-Q2-26 | page:15, Note 4 | CP-1 debt register | Reported | High | Components re-added equal |
| Covenant total net leverage 5.73x | /workspace/secdata/data/2026-11-05/packs/43196-gray-media-inc-gtn-gtn-a | 10-Q_2026-06-30_gtn20260630_10q.htm.jsonl | S-Q2-26 | page:37, MD&A | CP-1 covenants | Issuer calculation | High | Net debt over denominator equal |
| Adjusted EBITDA 214 for Q2 2026 and 368 for six months | /workspace/secdata/data/2026-11-05/packs/43196-gray-media-inc-gtn-gtn-a | EX-99.1_2026-08-07_ex_998938.htm.jsonl | S-R-Aug | page:12, reconciliation | CP-1 reconciliation | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| Adjusted EBITDA 670 for FY2025 and 1,162 for FY2024 | /workspace/secdata/data/2026-11-05/packs/43196-gray-media-inc-gtn-gtn-a | EX-99.1_2026-02-26_ex_924265.htm.jsonl | S-R-Feb | page:11, reconciliation | CP-1 metrics | Issuer non-GAAP | Medium | Reconciliation re-added equal |
| Cash interest paid 393 in FY2025 and 394 in FY2024 | /workspace/secdata/data/2026-11-05/packs/43196-gray-media-inc-gtn-gtn-a | 10-K_2025-12-31_gtn20251231_10k.htm.jsonl | S-10K | page:94, Note 4 | CP-1 interest cover | Reported | High | Matches |
| Series A preferred 600 at June 30, 2026 | /workspace/secdata/data/2026-11-05/packs/43196-gray-media-inc-gtn-gtn-a | 10-Q_2026-06-30_gtn20260630_10q.htm.jsonl | S-Q2-26 | page:3 and page:18, Note 7 | CP-1 claims outside debt; CP-1A ownership | Reported | High | Matches |
| Howell-Robinson Family influence | /workspace/secdata/data/2026-11-05/packs/43196-gray-media-inc-gtn-gtn-a | 10-K_2025-12-31_gtn20251231_10k.htm.jsonl | S-10K | page:38, Item 1A | Missing from CP-1A and CP-2 | Risk factor | High | Omitted (QA-1) |
| WBBJ consideration 25 plus 2 of working capital, 15 paid in Q4 2025 | /workspace/secdata/data/2026-11-05/packs/43196-gray-media-inc-gtn-gtn-a | 10-Q_2026-06-30_gtn20260630_10q.htm.jsonl | S-Q2-26 | page:11, Note 3 | Missing from CP-1A C1 | Reported | High | Omitted (QA-2) |
| Per-instrument deferred loan costs | /workspace/secdata/data/2026-11-05/packs/43196-gray-media-inc-gtn-gtn-a | 10-Q_2026-06-30_gtn20260630_10q.htm.jsonl | S-Q2-26 | page:15, Note 4 | CP-1 debt register | Reported | High | Printed by instrument (QA-3) |
| 117 full-power markets at August 2026 | /workspace/secdata/data/2026-11-05/packs/43196-gray-media-inc-gtn-gtn-a | EX-99.1_2026-08-07_ex_998938.htm.jsonl | S-R-Aug | page:6, company description | CP-1A profile and conflict K-3 | Issuer description | Medium | K-3 cites page:7 (QA-4) |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM figures | CP-1 C1; CP-2 findings | FY2025 plus six months 2026 less six months 2025 | Revenue, Adjusted EBITDA, operating income, interest, net loss, cash flow, capex, cash interest, dividends | Recomputed from source pages: equal | Supported | High | Basis of every ratio | S-10K page:73, page:75, page:94; S-Q2-26 page:3, page:5, page:16; S-R-Feb page:11; S-R-Aug page:12 |
| Leverage and cover ratios | CP-1 C4, C5; CP-2 | Principal debt, cash, LTM Adjusted EBITDA, interest | Debt over EBITDA; net debt over EBITDA; EBITDA over cash interest and over interest expense | Recomputed: equal for LTM, FY2025 and FY2024 | Supported | High | Leverage and coverage | S-Q2-26 page:15; S-10K page:92 |
| Covenant sensitivity | CP-1 C9; CP-2 | Denominator 994, net debt, caps | Required denominator at 4.25x; cushions; net debt over LTM Adjusted EBITDA | Recomputed: equal (40.0%, 1,691.5, 18.1%, 8.03x) | Supported with the inference on the cap | Medium | Covenant headroom | S-Q2-26 page:37 |
| Debt and carrying value | CP-1 C10 | Principal by instrument, deferred loan costs, premium | Principal less costs plus premium | Recomputed: 5,808 equal | Supported | High | Debt perimeter | S-Q2-26 page:14 to page:16 |
| Secured share | CP-1A C3; CP-2 | First lien, second lien and total principal | Secured over total at three dates | Recomputed: 55.2%, 65.4%, 65.8% equal | Supported | High | Structure | S-R-Feb page:3; S-10K page:57; S-Q2-26 page:37 |
| Voting share | CP-1A C2 | Share counts at July 31, 2026 | Class A shares times 10 over total votes | Recomputed: 51.5% equal; 52.2% at February 20, 2026 | Supported | High | Control | S-Q2-26 page:2; S-10K page:45 |
| Acquisition consideration versus cash | CP-1A C1; CP-2 D7 | Stated consideration and cash flow line | 278 less 264 | Arithmetic equal, but treated as unexplained | Partially supported | Low | Cost of 2026 deals | S-Q2-26 page:5, page:11 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial source gate, 1 MATERIAL and 5 MINOR findings | Script formula | 25, band Insufficient Information | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A ownership and control; CP-2 weaknesses and Reader summary | Holders called unidentified although the 10-K names the Howell-Robinson Family as able to exert significant influence "potentially in a manner which may not be consistent with the interests of our other stockholders" | Gap the sources can fill | Control and alignment are a core creditor risk; the handoffs understate a documented governance risk | State the family influence, with holdings Not supplied | CP-1A Ownership and control; CP-2 Key findings, Strengths and weaknesses |
| MINOR | CP-1A K-4 and C1; CP-2 D7 | Difference of 14 between stated consideration and cash paid called unexplained; the 10-Q says 15 of the WBBJ price was paid in Q4 2025 and 2 of working capital in Q2 2026 | Gap the sources can fill | Overstates acquisition cash in the half; the 332 total consideration omits the 2 | Use cash of 265 for the half and consideration of 27 for WBBJ | CP-1A Conflicts; CP-2 Calculations |
| MINOR | CP-1 debt register and gaps | Per-instrument carrying amounts called Not supplied; deferred loan costs are printed by instrument | Gap the sources can fill | Facility-level book values can be derived | Show principal less cost by instrument | CP-1 Debt register, Gaps |
| MINOR | CP-1A conflict K-3 | Cites S-R-Aug page:7 for the 117 markets; the statement is on page:6 | Wrong locator | A reader checking page:7 does not find it | Cite page:6 | CP-1A Conflicts |
| MINOR | CP-1A Company and operating model | Cites S-10K page:4 for the 39% national cap; page:4 gives 37% reach and the cap is on page:14 and page:39 | Wrong locator | The cap claim is unverifiable at the page cited | Cite page:39 | CP-1A Company and operating model |
| MINOR | CP-1 liquidity and maturity charts | Cash cells cite the revolver pages (S-10K page:92, S-Q2-26 page:15); cash is on S-10K page:72 and S-Q2-26 page:2; the 2028 amount cites page:92 rather than S-Q2-26 page:16 | Imprecise locator | Slower verification; no misstatement | Cite the page that holds each figure | CP-1 Chart data tables |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves on their cover pages | A wrong document would change every figure | None found | None |
| Quotation accuracy | Strong | 83 quotations in four handoffs, none misplaced | Misquotation would mislead on terms | None found | None |
| Calculation reproducibility | Strong | 54 of 54 recomputed equal | Calculation errors would move leverage | None found | None |
| Gap discipline | Moderate | Two gaps declared that the sources could fill (QA-1, QA-2) and one overstated (QA-3) | Declared gaps hide available facts | Control and acquisition cost understated | Search sources before declaring Not supplied |
| Locator precision | Adequate | Three locator defects (QA-4, QA-5, QA-6), none changes a figure | Slower checks | None on conclusions | Exact page locators |
| Reviewer independence | Weak | One session wrote and checked the handoffs | Shared blind spots go undetected, as QA-1 and QA-2 show | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Executed credit agreement, indentures and collateral documents | Documents as amended March 31, 2026 | Maintenance trigger, baskets and creditor control are issuer-described only | Covenant rows in CP-1, CP-1A, CP-2 | Caps committee use | Credit agreement, indentures, exhibit indexes |
| G2 | Revolver borrowing used from July 21, 2026 and the quarter ended September 30, 2026 | September 30, 2026 10-Q and release | Post-June liquidity and covenant trigger unseen | Liquidity and leverage at the as-of date | Lowers currency of the view | Third-quarter 2026 filings |
| G3 | Holdings of the Howell-Robinson Family, Class A holders and the Series A preferred holder | 2026 proxy statement | Quantifies control and alignment | CP-1A ownership, CP-2 weaknesses | Caps the control view | 2026 proxy statement |
| G4 | Retransmission and network affiliation terms | Contract summaries | Renewal price risk to 2028 cannot be sized | Revenue durability | Moderate | Company disclosures |
| G5 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / gtn-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted | Passed with the G5 ownership statement slightly overstated | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, debt, liquidity, covenants | High | Six headings; accepted | Passed with two MINOR findings | Metrics recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, ownership, transactions, governance | High | Six headings; accepted | Restricted: one MATERIAL and three MINOR findings | Ownership gap overstated |
| CP-2 | requests/CP-2 attempt 2 / same run | Credit synthesis | High inputs | Six headings; attempt 1 refused, attempt 2 accepted | Restricted: inherits the ownership gap | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A, CP-2 | Holders and controlling influence | Contradicted by S-10K page:38 | Holders called unidentified; the family named in the 10-K is omitted | Add the family and its stated influence | Restricts the control view |
| MINOR | CP-1A | K-3 locator and 39% cap locator | Supported on other pages | Wrong pages cited | Cite S-R-Aug page:6 and S-10K page:39 | None |
| MINOR | CP-1 | Chart data cash and 2028 amount | Supported on other pages | Cash and amount cited to neighbouring pages | Cite S-10K page:72, S-Q2-26 page:2 and page:16 | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A, CP-2 | Acquisition consideration 278 and total 332 | Stated consideration used where cash paid in the period is needed; WBBJ price of 25 omits 2 of working capital and 15 paid in Q4 2025 | The 10-Q explains the 14 difference (13 of timing plus 1 rounding against the cash flow line of 264) | Use 265 of cash for the half and 27 for WBBJ | None on leverage or liquidity |
| MINOR | CP-1 | Per-instrument book value | Deferred loan costs are printed by instrument, so principal less cost is calculable | None | Show carrying amount by instrument | None |
| MINOR | CP-1, CP-2 | First lien 4.25x cap read with the 50 letters-of-credit trigger | Two issuer passages combined; handoffs label it inference | Wording differs between the 10-K and the 10-Q | Keep labelled as inference | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1, CP-1A, CP-2 | Maintenance covenant trigger and 4.25x cap; baskets for dividends and repurchases | Executed credit agreement as amended March 31, 2026 | Issuer descriptions only; 10-K and 10-Q wording differ | Supply the agreement | Required before any headroom statement |
| MINOR | CP-1A, CP-2 | Series A preferred change-of-control redemption and ranking | Articles of incorporation and preferred terms | Described in the 10-K note only | Supply the terms | Needed for change-of-control analysis |
| MINOR | CP-1, CP-1A | Guarantees and security over substantially all assets excluding real estate; unrestricted subsidiaries | Indentures, collateral documents, subsidiary list | Issuer description; no list of unrestricted subsidiaries | Supply the documents | Needed for structure and recovery work |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made in this run | Bond prices, spreads, ratings and peers are not part of the minimum source pack | Recorded by design | Add market modules only with sourced market data | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-0, CP-1A, CP-2 | CP-0 gap G5 and CP-1A and CP-2 say holders are not identified; the 10-K names the Howell-Robinson Family | CP-2 attempt 2 cites CP-1A hash 8f6aed0d and CP-1 hash a5ba76a0 | Correct in a rerun | Control view understated |
| MINOR | CP-1A, CP-2 | CP-1A K-4 and CP-2 D7 carry the unexplained 14 and the total of 332 | Same | Use cash of 265 and consideration of 27 for WBBJ | Acquisition cost trace only |
| MINOR | CP-1, CP-2 | All CP-2 figures found in CP-1 or CP-1A with identical values | No version mismatch | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | Run | Committee readiness | Financial view traceable; control view understated; review is self-review only | Rerun CP-1A, CP-2 and CP-5 with the family statement and an independent reviewer | Committee status Restricted |
| MINOR | CP-1, releases | Duplication | The releases repeat 10-Q figures; CP-0 and CP-1 treat the filings as controlling and use the releases only for Adjusted EBITDA | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Reader summary, attempt 1 | A number in the Reader summary did not appear elsewhere in the handoff; refused by the report adapter and repaired in attempt 2 | Check that every Reader summary number is repeated in the body | Resolved; attempt 2 accepted |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MATERIAL | CP-0, CP-1A, CP-2 | Gap the sources can fill | Holders called unidentified; 10-K names the Howell-Robinson Family | Add family influence; holdings Not supplied | Restricts committee use | Open |
| QA-2 | MINOR | CP-1A, CP-2 | Gap the sources can fill | 14 difference called unexplained; WBBJ timing explains 13 | Use cash of 265 for the half | None | Open |
| QA-3 | MINOR | CP-1 | Gap overstated | Per-instrument carrying amounts called Not supplied | Derive by instrument | None | Open |
| QA-4 | MINOR | CP-1A | Locator | K-3 cites page:7; text on page:6 | Cite page:6 | None | Open |
| QA-5 | MINOR | CP-1A | Locator | 39% cap cited to page:4; on page:14 and page:39 | Cite page:39 | None | Open |
| QA-6 | MINOR | CP-1 | Locator | Chart cash and 2028 amount cited to neighbouring pages | Cite exact pages | None | Open |
| QA-7 | MINOR | CP-2 | Export | Reader summary number absent from body in attempt 1 | Repaired in attempt 2 | None | Closed |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each double-quoted phrase with a page locator on the same line, in CP-0, CP-1, CP-1A and CP-2, searched on the cited pages after normalising whitespace and quote marks | 83 quotations (47, 22, 14 and 0); none misplaced |
| Q2 | Metric recomputation | A script read inputs from the source pages (LTM statement lines, cash interest, debt, cash, Adjusted EBITDA, covenant schedule) and recomputed LTM figures, leverage and cover ratios, covenant sensitivity, reconciliations, debt and balance sheet totals and cash roll-forwards | 54 of 54 equal to the handoffs |
| Q3 | Locator test on table rows | Numbers in table rows compared with the pages cited in the same row; the test flagged 33 cells in CP-1A, 98 in CP-1 and 8 in CP-0 | After triage, flagged cells were derived values, page-range locators the parser cannot read and number-format artefacts, except the locator defects QA-4, QA-5 and QA-6 |
| Q4 | Acquisition cash | WBBJ 25 + 2 − 15 paid in Q4 2025 = 12; 12 + 56 + 115 + 80 + 2 = 265; against cash flow 264; stated consideration 25 + 56 + 115 + 80 + 2 = 278; 278 − 265 = 13; 265 − 264 = 1 | 265; 13 of timing and 1 of rounding explain the 14 |
| Q5 | Vote share at February 20, 2026 | Class A 10,212,436 × 10 = 102,124,360; common 93,563,703; total 195,688,063; 102,124,360 / 195,688,063 | 52.2% (51.5% at July 31, 2026) |
| Q6 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:3,Calculated:5,Analyst Inference:1,Weak Lineage:2,Insufficient Information:2" --fields-present 17 --fields-total 17 --source-gate partial --findings "MATERIAL:1,MINOR:5"` | score = clamp((0.6 × 65.38 + 0.4 × 100) × 0.7 − 30) = 25.46, rounded to 25; band Insufficient Information; qa_status Restricted |

## Gaps

- QA-1 is the critical provenance gap for the decision: the controlling family influence stated in the 10-K is missing from the control view.
- G1 and G2: executed debt documents and the September 30, 2026 balance sheet are not supplied, so covenant headroom and post-June liquidity stay issuer-described or unseen.
- G3: holdings of the family and of the Series A preferred holder are not quantified in the pack.
- G5: no independent review; this CP-5 was written by the same host that wrote the modules.

## Next module

- Report delivery: carry qa_status Restricted, Confidence Score 25 (band Insufficient Information), committee status Restricted and issue QA-1.
- Rerun step: in a new run folder, rerun CP-1A, CP-2 and CP-5 with the family influence stated (S-10K page:38), the WBBJ cash timing (S-Q2-26 page:11) and corrected locators.
- Sourcing and review: add the credit agreement, indentures, 2026 proxy statement and the third-quarter 2026 filings, and have an independent agent repeat this check, starting with omissions.
