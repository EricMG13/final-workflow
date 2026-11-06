## Request

Evidence trace and research integrity QA (CP-5 with CP-5A) for Rocket Companies, Inc. (issuer id rkt), as of 2026-11-05, pathway credit_snapshot, run rkt-2026-11-05-credit_snapshot-host. Scope: the Top 5 material credit drivers across the four accepted handoffs (CP-0, CP-1, CP-1A, CP-2), traced to the pinned sources, with calculation, legal, market, cross-module and handoff checks and a clearance decision. This module changes no credit conclusion, repairs no lineage silently and writes no replacement value for another module's figure.

## Sources

### Issuer sources traced

| Alias | Exact source name | sha256 |
| --- | --- | --- |
| 10-K | 10-K_2025-12-31_rkt-20251231.htm.jsonl | 3f00d23a5a4d987299ba3ee372766fbda78de035096653b1d865a69d888922ae |
| Q1 10-Q | 10-Q_2026-03-31_rkt-20260331.htm.jsonl | 0a828436cfdb4cb6430873bcdf676f4a2758eb6f8aaf83bcd5c4c1bd9959be37 |
| Q2 10-Q | 10-Q_2026-06-30_rkt-20260630.htm.jsonl | 4ca13e8689778101de80b67ba6d799666890bfd97332aef7adca82c2e094e90b |
| Q3 10-Q | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | 59c56634da7bee8e5debdbfce480876851737d0b5ddf01b6f700d4f40ecd6bce |
| Q1 release | EX-99.1_2026-05-07_rkt-earningsrelease3312026.htm.jsonl | 7d218dea46aff3c8af9298dca5b852af49f0e5f073ef0f93c5f3b622d0854392 |
| Q2 release | EX-99.1_2026-08-06_rkt-063020268xkex991earnin.htm.jsonl | 6542f2db604c3ffa41383bd56c69d56492031f4ee91e3c42b828c315d7979477 |
| Q3 release | EX-99.1_2026-10-29_rkt-093020268xkex991earnin.htm.jsonl | 51281ba557de6ffcbe69b458cb58d0ccec82e27e457e960477651f50df28d346 |

### Run context

| Source | sha256 | Role |
| --- | --- | --- |
| context | 2c3b1fbba94f4a511900e452ab48c8c288b5d2472b9c175cb66b98c0de72d2ac | Dated run settings. Not issuer evidence. Ratings, quotes, peers, deal terms and legal documents are blank or none in it. |

### Handoffs audited

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | b5fd40886eeedd24c855cc4c21dd662543a58c822d0fb2b19a168fce8c895924 | Source readiness |
| CP-1 | 54e4775b2f314e2c41568ee11caf51c8cfb55f59fdffa205fe2c46e2c7684901 | Financial base |
| CP-1A | e6558750ba53fb9ab8d823530f1ce2e5fe08210dd9413d3fe50e52ac4c9c94b1 | Business and transaction context |
| CP-2 | c817b6713942c713c9a51b2457da9f6f31cab633c7adc99e0b702b5e44aae072 | Fundamental credit synthesis |

Locators are `<alias> page:N`, the extracted chunk number of the pinned text file, not the printed page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The earlier analyses trace well to the filings: every sampled figure matched its source page and every derived ratio recomputed. Two material gaps restrict committee use: incomplete owner distribution evidence and creditor-protection claims resting on summary notes. | Medium | No debt documents, governance letter or proxy statement are supplied, so ranking, restricted payment capacity and owner distributions cannot be traced to primary sources. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 136 sampled figures and 21 quotations match the cited pages, and every ratio recomputes, including leverage of 3.78x gross and 2.83x net. | The numbers a committee reads can be relied on as reported. | High |
| Leverage uses company-defined adjusted EBITDA and unsecured notes only, with fiscal 2025 and the 2025 quarters on different presentations. | The ratios are anchors, not covenant measures, and the earlier dates are overstated by perimeter. | Medium |
| Owner distributions in 2025 are understated: the special dividend of USD 120.1 million omits tax distributions of USD 114 million and an equity statement total of USD 143 million. | Sponsor behaviour evidence is thinner than presented; the mixed category may hold but needs restating. | Medium |
| Claims on ranking, guarantors and the revolver borrower rest on note summaries and exhibit lists, not executed documents. | Structure conclusions stay provisional until legal review. | High |
| Two locators in the financial base are wrong and several table rows lack cited pages. | A reviewer cannot check those rows from the page named; the figures themselves are correct. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 1 is calculated, 0 are assumption-based, 2 are analyst inferences, and 0 are weak-lineage, untraced, conflicting or insufficient-information items. A sample of 136 headline figures and 21 verbatim quotations from the four handoffs was found on the cited or expected source pages with no mismatch of value. The most important provenance gap is that the debt documents, the governance letter and the proxy statement are not in the pack, which matters because ranking, restricted payment capacity and owner behaviour can then only be stated on summary notes, so committee use is restricted until they are obtained.

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 6. Committee Use: Restricted.

qa_status is Restricted and committee_status is Restricted. The confidence script in the CP-5 skill folder was run with these inputs: lineage Directly Sourced 2, Calculated 1, Analyst Inference 2; required fields present 6 of 6 (the six transport headings, because CP-OS owns the envelope fields); source gate partial (CP-0 judged every consumer READY_WITH_LIMITATIONS); findings Material 2 and Minor 6. It returned a confidence score of 11 and the band Insufficient Information, with qa_status Restricted. The low score follows from the penalty arithmetic and the partial source gate, not from any figure mismatch, and it is separate from the Medium confidence given in the reader summary to this traceability conclusion. The completeness and handoff validation scripts named in the skill are not in the repository folder and were not run.

### Source register

Module status: Ready with Limitations. Traceability scope: Top 5.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_rkt-20251231.htm.jsonl | Filed, audited annual report | Fiscal year ended December 31, 2025 | Rocket Companies, Inc. consolidated | Statements, borrowings, adjusted EBITDA, business, risk factors, governance, exhibits | Pre-2026 interest captions; Mr. Cooper for one quarter | FY2025 base for all handoffs |
| S2 | 10-Q_2026-03-31_rkt-20260331.htm.jsonl | Filed, unaudited interim report | Quarter ended March 31, 2026 | Rocket Companies, Inc. | Statements, borrowings, liquidity, two-segment disclosure | Old segment basis; cash interest not printed | Quarterly balances and LTM construction |
| S3 | 10-Q_2026-06-30_rkt-20260630.htm.jsonl | Filed, unaudited interim report | Quarter and six months ended June 30, 2026 | Rocket Companies, Inc. | Statements, borrowings, revolver amendment note, recast segments | Cash interest not printed | Quarterly balances and LTM construction |
| S4 | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | Filed, unaudited interim report | Quarter and nine months ended September 30, 2026 | Rocket Companies, Inc. | Statements, debt tables, MD&A, legal, regulatory, acquisitions, exhibits | Covenant levels, guarantors and cash interest not printed | Current-period base for all handoffs |
| S5 | EX-99.1_2026-05-07_rkt-earningsrelease3312026.htm.jsonl | Furnished management release | First quarter 2026 | Rocket Companies, Inc. | Adjusted measures, liquidity, outlook | Management language | Quarterly adjusted EBITDA |
| S6 | EX-99.1_2026-08-06_rkt-063020268xkex991earnin.htm.jsonl | Furnished management release | Second quarter 2026 | Rocket Companies, Inc. | Adjusted measures, liquidity, notes issuance, outlook | Management language | Quarterly adjusted EBITDA, 2026 notes |
| S7 | EX-99.1_2026-10-29_rkt-093020268xkex991earnin.htm.jsonl | Furnished management release | Third quarter 2026 and outlook | Rocket Companies, Inc. | Adjusted reconciliations, liquidity, fourth-quarter revenue outlook | Management language; outlook is a forecast | Adjusted EBITDA, guidance |
| S8 | context | Run settings, not evidence | As of 2026-11-05 | Rocket Companies, Inc. | Currency, periods, blank ratings, quotes and legal documents | Not issuer evidence | Scope only |

### Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Moderate trailing unsecured leverage: senior notes of 10,743 over LTM adjusted EBITDA of 2,843 gives 3.78x gross and 2.83x net of cash of 2,699 | CP-1, CP-2 | Debt table, balance sheet, adjusted EBITDA reconciliations | Sets the leverage anchor and the debt service view | Headline credit metric | Q3 10-Q page:30, page:4; 10-K page:104; Q3 release page:8 | Company-defined EBITDA; unsecured debt only; FY2025 and 2025 quarters on different presentations; not a forward run-rate |
| 2 | Secured funding of 14,187 against committed secured lines of 7,400, mostly maturing in 2027 and 2028, with cross default terms | CP-1, CP-2 | Secured financing table and covenant note | Recurring renewal and margin call exposure | Liquidity and refinancing risk | Q3 10-Q page:27, page:28, page:29 | Collateral by facility and availability not printed |
| 3 | Liquidity: cash 2,699 and undrawn revolver 2,500 tie to filings; stated 11.4 billion includes 6.2 billion of availability that does not tie | CP-1, CP-2 | Balance sheet, debt table, MD&A liquidity paragraph | Near-term safety and the quality of stated liquidity | Sizing of buffers | Q3 10-Q page:4, page:30, page:67, page:28 | Availability basis and cash composition not printed |
| 4 | Rate-sensitive earnings: adjusted revenue 2,822, 2,761 and 2,574 across 2026, fourth-quarter guide 2.1 to 2.3 billion, 30-year rate 7.28% | CP-1, CP-1A, CP-2 | Release summaries, outlook, MD&A business trends | Trailing leverage may not persist | Forward earnings risk | Q1 release page:1; Q2 release page:1; Q3 release page:1, page:3; Q3 10-Q page:49 | Outlook is management guidance; no forecast supplied |
| 5 | Founder control and unseen creditor protections; documented owner actions read as Neutral or Mixed | CP-1A, CP-2 | Risk factors, equity statement, cash flow, exhibits | Owner behaviour and protective terms decide creditor control | Monitoring posture | 10-K page:83, page:86, page:95, page:137, page:138, page:222; Q3 10-Q page:68 | Governance letter, indentures, credit agreements and proxy not supplied; distribution evidence incomplete in CP-1A |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Moderate trailing unsecured leverage | CP-1, CP-2 | Notes 10,743 (Q3 10-Q page:30); cash 2,699 (page:4); adjusted EBITDA 1,281 (10-K page:104), 2,252 and 690 (Q3 release page:8) | Yes | Filed note and statements; furnished reconciliation | Calculated | Reproduced by recomputation; adjective "moderate" has no benchmark | Medium | Remediation Needed |
| Secured funding and renewal risk | CP-1, CP-2 | Totals 14,187 and 7,400 (Q3 10-Q page:29); maturity dates by line (page:27 to page:29); cross default wording (page:27) | Yes | Filed note | Directly Sourced | Verified on page; by-year sums recomputed | High | Committee-Ready |
| Liquidity quality | CP-1, CP-2 | "total liquidity of $11.4 billion" (Q3 10-Q page:67); revolver 2,500 outstanding nil (page:30); cash 2,699 (page:4) | Yes | Filed note and MD&A | Directly Sourced | Components verified; availability of 6.2 billion not reproducible and attributed to management | Medium | Remediation Needed |
| Rate-sensitive earnings and guided decline | CP-1, CP-1A, CP-2 | Adjusted revenue by quarter (releases page:1); outlook (Q3 release page:3); rates (Q3 10-Q page:49) | Yes | Furnished release and filed MD&A | Analyst Inference | Facts verified; forward reading is interpretation | Medium | Committee-Ready |
| Founder control and unseen protections | CP-1A, CP-2 | Control and exemptions (10-K page:86); opportunities renounced (page:83); dividend 120.1 (page:95); equity statement 143 (page:137); cash distributions 241 (page:138); tax distributions 114 (Q3 10-Q page:68) | Yes | Filed | Analyst Inference | Control verified; behaviour category rests on partial distribution evidence | Medium | Remediation Needed |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Senior notes principal 10,743; premium 39; issuance costs 66; carrying 10,716 | packs/1805284-rocket-companies-inc-rkt/10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:30, Note 6 | CP-1 Debt stack | Sourced | Filed | Foots; weighted average rate 5.43% on page:31 |
| Senior notes principal 10,455 at December 31, 2025 | packs/1805284-rocket-companies-inc-rkt/10-K_2025-12-31_rkt-20251231.htm | 10-K_2025-12-31_rkt-20251231.htm.jsonl | S1 | page:180, Note 7 | CP-1 Chart data: leverage | Sourced | Filed, audited | Maturity table foots on page:181 |
| FY2025 adjusted EBITDA 1,281; bond interest add-back 335 | packs/1805284-rocket-companies-inc-rkt/10-K_2025-12-31_rkt-20251231.htm | 10-K_2025-12-31_rkt-20251231.htm.jsonl | S1 | page:103, page:104 | CP-1 Chart data: leverage | Sourced (management) | Filed MD&A | Non-GAAP; caption differs from 2026 |
| Adjusted EBITDA 738, 766, 748; nine months 2,252 and 690; bond interest 139, 142, 154, 435, 195 | packs/.../EX-99.1 releases | EX-99.1_2026-05-07, EX-99.1_2026-08-06, EX-99.1_2026-10-29 | S5, S6, S7 | S5 page:8; S6 page:9; S7 page:8 | CP-1 Financials | Sourced (management) | Furnished | Quarters tie to nine months |
| Cash 2,699; restricted cash 240 | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:4, page:11 | CP-1 Liquidity | Sourced | Filed | Cash includes buy-down and margin cash, not quantified |
| Revolver 2,500 committed, nil outstanding, maturing July 16, 2029 | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:30 | CP-1 Liquidity | Sourced | Filed | Q2 10-Q page:28 footnote on the upsizing |
| Secured financing 14,187; line amount 37,525; committed 7,400 | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:27 to page:29 | CP-1 Debt stack | Sourced | Filed | Foots by type |
| Total liquidity 11.4 billion with 2.7, 2.5 and 6.2 billion components | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:67 | CP-1 Liquidity | Sourced (management statement in filing) | Filed MD&A | 6.2 billion not reproducible from page:28 |
| Cash paid for interest 596 for FY2025 | packs/.../10-K_2025-12-31_rkt-20251231.htm | 10-K_2025-12-31_rkt-20251231.htm.jsonl | S1 | page:138 | CP-1 Chart data: interest cover | Sourced | Filed, audited | Single figure, not split by type |
| Fair value of senior notes 10,258 against carrying 10,716; December 2025 10,502 and 10,423 | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:23 | CP-1 Liquidity, covenants | Sourced | Filed | Aggregate, observable bond prices |
| Adjusted revenue 2,822, 2,761, 2,574 and outlook 2.1 to 2.3 billion | packs/.../EX-99.1 releases | EX-99.1_2026-05-07, EX-99.1_2026-08-06, EX-99.1_2026-10-29 | S5, S6, S7 | S5 page:1; S6 page:1; S7 page:1, page:3 | CP-1 Financial base view | Sourced (management) | Furnished | Outlook is a forecast |
| 30-year rate 6.43% to 7.28%; smaller market | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:49 | CP-1 Financial base view; CP-1A | Sourced | Filed MD&A | Market commentary by the company |
| Servicing UPB 2,007,176; servicing fee income 3,181 | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:62, page:5 | CP-1A Company and operating model | Sourced | Filed | Foots 1,201,476 plus 805,700 |
| Consideration 1,742 (Redfin) and 16,973 (Mr. Cooper) | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:16, page:17 | CP-1A Transaction summary | Sourced | Filed | Components foot |
| Mr. Gilbert holds more than a majority of voting power; controlled company | packs/.../10-K_2025-12-31_rkt-20251231.htm | 10-K_2025-12-31_rkt-20251231.htm.jsonl | S1 | page:86, page:83 | CP-1A Ownership | Sourced | Filed risk factor | Percentage not disclosed |
| Special dividend 120.1 paid April 3, 2025 | packs/.../10-K_2025-12-31_rkt-20251231.htm | 10-K_2025-12-31_rkt-20251231.htm.jsonl | S1 | page:95 | CP-1A Governance; CP-2 | Sourced | Filed | Equity statement shows 143 including 22 non-controlling interest (page:137) |
| Tax distributions of 114 to holders of Holdings LLC Units other than Rocket Companies, nine months 2025 | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:68, page:34 | Not carried into CP-1A | Sourced | Filed | Omitted from CP-1A governance table |
| FY2025 distributions to unit holders and Class A shareholders 241 | packs/.../10-K_2025-12-31_rkt-20251231.htm | 10-K_2025-12-31_rkt-20251231.htm.jsonl | S1 | page:138 | Not carried into CP-1A | Sourced | Filed, audited | Combined line |
| Legal reserves 216 against 74; verdict 175; Chapter 11 filing by plaintiff | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:41, page:38 | CP-1 Claims outside funded debt | Sourced | Filed | Reserve coverage of the verdict not stated |
| Note offering date: October 2025 in footnote against June 2025 elsewhere | packs/.../10-K and 10-Q | 10-K_2025-12-31 and 10-Q_2026-09-30 | S1, S4 | 10-K page:181, page:222; Q3 10-Q page:67 | CP-1A Source conflicts | Sourced, conflict logged | Filed | Quotes verified verbatim |
| Revolver borrower: Rocket Mortgage, LLC (April 30, 2025) against Rocket Companies, Inc. (July 16, 2026) | packs/.../10-K and 10-Q | 10-K_2025-12-31 and 10-Q_2026-09-30 | S1, S4 | 10-K page:222; Q3 10-Q page:71 | CP-1A Source conflicts; CP-1 Debt stack | Sourced, conflict logged | Filed exhibit lists | Quotes verified verbatim |
| Covenant types and compliance; no levels | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:27 | CP-1 Liquidity, covenants | Sourced | Filed | Levels Not supplied |
| Regulatory minimums: net worth about 3,500, liquidity about 1,500, ratio 6% | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:42 | CP-1 Liquidity, covenants | Sourced | Filed | Applies to Rocket Mortgage |
| Interest reclassification amounts for 2025 quarters; segment recast | packs/.../10-Q_2026-09-30_rkt-20260930.htm | 10-Q_2026-09-30_rkt-20260930.htm.jsonl | S4 | page:10, page:42 | CP-1 Perimeter, comparability | Sourced | Filed | FY2025 not recast |
| Agencies may terminate servicing on little notice | packs/.../10-K_2025-12-31_rkt-20251231.htm | 10-K_2025-12-31_rkt-20251231.htm.jsonl | S1 | page:29 | CP-1A Company and operating model | Sourced | Filed risk factor | Qualitative |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM adjusted EBITDA to September 30, 2026 | CP-1, CP-2 | 1,281; 2,252; 690 | 1,281 + 2,252 - 690 = 2,843, USD million, no normalization | Calculated | Reproduced exactly | Medium | Leverage, coverage | 10-K page:104; Q3 release page:8 |
| LTM adjusted EBITDA to March 31 and June 30, 2026 | CP-1 | 1,281; 738 and 169; 1,504 and 342 | 1,850 and 2,443 (quarter sum 2,444 from printed rounding) | Calculated | Reproduced exactly | Medium | Leverage trend | Q1 release page:8; Q2 release page:9 |
| Total debt / LTM EBITDA | CP-1, CP-2 | 10,455 / 1,281; 10,455 / 1,850; 10,805 / 2,443; 10,743 / 2,843 | 8.16, 5.65, 4.42, 3.78; unsecured principal only | Calculated | Reproduced exactly | Medium | Leverage | 10-K page:180; Q1 10-Q page:27; Q2 10-Q page:29; Q3 10-Q page:30 |
| Net debt / LTM EBITDA | CP-1, CP-2 | Notes less cash: 7,759; 7,768; 7,702; 8,044 | 6.06, 4.20, 3.15, 2.83; cash and cash equivalents only | Calculated | Reproduced exactly | Medium | Leverage | 10-K page:135; Q1 10-Q page:3; Q2 10-Q page:4; Q3 10-Q page:4 |
| LTM bond interest and accrual cover | CP-1, CP-2 | 335; 139 and 38; 281 and 84; 435 and 195 | 436, 532, 575; cover 3.82, 4.24, 4.59, 4.94 | Calculated | Reproduced exactly | Medium | Coverage | 10-K page:103; Q1 release page:8; Q2 release page:9; Q3 release page:8 |
| FY2025 adjusted EBITDA / cash interest | CP-1, CP-2 | 1,281; 596 | 2.15 on a mixed basis | Calculated | Reproduced; basis disclosed | Low | Coverage | 10-K page:104, page:138 |
| All balance sheet financing / LTM EBITDA | CP-1 | 24,903 over 2,843 and earlier dates | 8.76 at September 30, 2026; 22.14, 14.22, 11.22 earlier; reference only | Calculated | Reproduced exactly | Low | Context only | Q3 10-Q page:4 |
| Equity less goodwill and intangibles | CP-1, CP-2 | 24,311 less 10,686 less 1,880 | 11,745 consolidated proxy, not the covenant measure | Calculated | Reproduced exactly | Low | Capital cushion | Q3 10-Q page:4 |
| Secured outstanding by line maturity | CP-1, CP-2 | 38 lines on page:27 to page:29 | 9, 10,295, 3,462 and 421 evergreen; foots to 14,187 | Calculated | Reproduced exactly | Medium | Refinancing | Q3 10-Q page:27 to page:29 |
| Unsecured maturities by year | CP-1, CP-2 | 14 note lines on page:30 | 0, 503, 0, 1,500, 2,076, 2,214, 1,000, 2,850, 600; foots to 10,743 | Calculated | Reproduced exactly | High | Refinancing | Q3 10-Q page:30 |
| Quarterly cash from operations | CP-1 | 645; 1,857; 2,550 | Q2 -1,212; Q3 1,905 | Calculated | Reproduced exactly | Medium | Cash flow | Q1 10-Q page:6; Q2 10-Q page:6; Q3 10-Q page:7 |
| Derived fourth quarter 2025 adjusted EBITDA | CP-1 | 1,281; 690 | 591; valid only if the FY2025 and 2025 quarter measures share a basis | Calculated | Reproduced; basis assumption disclosed | Low | Trend | 10-K page:104; Q3 release page:8 |
| Liquidity as stated | CP-1, CP-2 | 2.7; 2.5; 6.2 billion | 11.4 billion; 6.2 not reproducible: 7,024 and 2,674 are the nearest note-based figures | Calculated | Reproduced; one component not reproducible | Medium | Liquidity | Q3 10-Q page:28, page:67 |

### Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Documented sponsor distributions are a 2025 special dividend of 120.1 and none in 2026 | The sources show more owner-linked cash out in 2025: tax distributions of 114 to holders of Holdings LLC Units other than Rocket Companies in nine months 2025 (Q3 10-Q page:68), an equity statement special dividend of 143 of which 22 is charged to non-controlling interest (10-K page:137), and combined FY2025 distributions to unit holders and Class A shareholders of 241 (10-K page:138). Before the Up-C Collapse, RHI held economic interests in the operating partnership and controlled the company (10-K page:140), so those holders were owner-linked (Analyst Inference) | Analyst Inference | The Neutral or Mixed behaviour category and the Key finding on owner actions rest on a partial distribution picture, which matters because distributions to the controlling holder are the main extraction signal available | Restate the distribution row with all four figures and their scope; keep the category only if the fuller picture supports it | CP-1A Governance and sponsor behaviour; CP-1A Reader summary; CP-2 Key findings and Strengths and weaknesses |
| Material | Ranking, guarantor, restricted payment and borrower statements across the handoffs | Statements about guarantors, structural ranking, the revolver borrower and the legal capacity for distributions rest on note summaries and exhibit lists; no indenture, credit agreement, governance letter or proxy is supplied | Analyst Inference | Creditor rights and loss given default depend on terms the pack cannot show | Obtain the documents; present structure statements as interpretation until legal review | CP-1 Debt stack; CP-1A Transaction summary and Governance; CP-2 Key credit risks |
| Minor | Operating lease liabilities 334 and MSR-related liabilities 325 | CP-1 cites 10-K page:184 for the lease figure and Q3 10-Q page:25 for the MSR liabilities; the figures are on 10-K page:183 and Q3 10-Q page:24. CP-0 cites Q3 10-Q page:4 for the Class L tie whose conversion figure is on page:46 | Directly Sourced | A reviewer following the cited page would not find the figure | Correct the locators | CP-1 Claims outside funded debt and Gaps; CP-0 Source conflicts |
| Minor | Financials and credit metrics table rows for expenses, net income, adjusted net income, bond interest, interest expense and unsecured financing | Quarterly values for the first and second quarters are shown with locators for other periods only; the pages are in Q1 10-Q page:4, Q2 10-Q page:4 and page:5, Q1 release page:7 and page:8 and Q2 release page:7 and page:9 | Directly Sourced | Values are correct (checked) but not traceable from the row | Add the missing locators | CP-1 Financials and credit metrics |
| Minor | "Moderate" unsecured leverage and use of 5.65x as a headroom reference | CP-2 calls 3.78x moderate without a benchmark (peers are not supplied) and says leverage could reach the 5.65x seen at March 31, 2026, a ratio CP-1 labels as overstated by perimeter | Analyst Inference | Adjective and reference level may be read as calibrated | State that no peer benchmark is supplied and drop 5.65x as a headroom reference | CP-2 Credit view; Strengths |
| Minor | EBITDA basis alignment | CP-1 records that FY2025 adjusted EBITDA and the 2025 quarters are on different presentations and that alignment is not confirmed; CP-2 Gaps does not carry this | Directly Sourced | The leverage anchor depends on it | Add the gap to CP-2 | CP-2 Gaps |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | 7 filed or furnished sources cover statements, debt, liquidity, segments and governance risk factors; no debt documents, ratings or proxy | Missing primary legal evidence leaves ranking and protections on summaries | Committee use restricted for structure and owner behaviour conclusions | Obtain debt documents, governance letter, proxy, rating publications |
| Citation completeness | Ready with Remediation | 136 of 136 headline figures found at the expected pages and 21 of 21 quotations verbatim; 2 wrong locators and several rows with partial locators | Reader cannot check some rows from the cited page | Low | Correct locators |
| Calculation traceability | Committee-Ready | 13 calculation items reproduced with formula, inputs, period and unit | Definition and presentation basis is disclosed in CP-1 | Medium, covered by the Minor flag | Carry the basis gap into CP-2 |
| Assumption transparency | Committee-Ready | Mixed-basis cash interest cover, derived fourth quarter, reference ratios all labelled | Assumptions visible and bounded | Low | None |
| Markdown artifact integrity | Ready with Remediation | Six transport headings present in all handoffs; no YAML envelope | Envelope fields are owned by CP-OS | Limited | None needed in this run |

Overall auditability follows the lowest dimension: Ready with Remediation.

### Audit lane results

#### Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | rkt-2026-11-05-credit_snapshot-host; sha256 b5fd40886eeedd24... | Source readiness for 7 sources | Filed and furnished | Six transport headings present; no YAML envelope | Passed | One minor locator (Class L tie) |
| CP-1 | rkt-2026-11-05-credit_snapshot-host; sha256 54e4775b2f314e2c... | Financial base, FY2025 to September 30, 2026 | Filed statements and notes; furnished reconciliations | Six transport headings present; selectors present | Restricted | Two wrong locators; partial row locators; no value mismatch |
| CP-1A | rkt-2026-11-05-credit_snapshot-host; sha256 e6558750ba53fb9a... | Business and transaction context | Filed and furnished | Six transport headings present; selectors present | Restricted | Material: distribution evidence incomplete |
| CP-2 | rkt-2026-11-05-credit_snapshot-host; sha256 c817b6713942c713... | Credit synthesis | Upstream only | Six transport headings present; selectors present | Restricted | Material: inherits the distribution omission; minor wording and gap items |

#### Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Claims outside funded debt: lease liabilities and MSR-related liabilities | Partially Supported | Pages cited are one page off | Correct to 10-K page:183 and Q3 10-Q page:24 | Monitoring Follow-Up |
| Minor | CP-1 | Financials and credit metrics rows with partial locators | Partially Supported | First and second quarter values lack their pages | Add pages | Monitoring Follow-Up |
| Minor | CP-0 | Class L tie | Partially Supported | Conversion figure is on page:46 not page:4 | Add Q3 10-Q page:46 | Formatting / Hygiene Only |

#### Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Leverage and cover on company-defined adjusted EBITDA | The measure is after secured-financing interest and before bond interest, so the numerator must be unsecured debt (done); FY2025 caption differs from 2026 and basis alignment is not confirmed | None between sources; the company states net income is unaffected by the reclassification (Q3 10-Q page:10) | Carry the gap into CP-2; label basis at first use | Monitoring Follow-Up |
| Minor | CP-2 | 5.65x used as a headroom reference | The ratio is perimeter-distorted per CP-1 | None | Remove the reference | Monitoring Follow-Up |

#### Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A, CP-2 | Two-layer funding with unsecured notes and secured lines; guarantor and borrower roles; legal capacity for owner distributions and absence of creditor-adverse actions | Indentures, revolving credit agreement, repurchase agreements, governance letter agreement, proxy statement | None of these is in the pack; context states legal documents none; the guarantors are not named | Obtain documents; keep statements as interpretation | Legal review required; the analyst interpretation is separate from the contractual terms, which are not seen |

#### Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | CP-0, CP-1, CP-1A, CP-2 | No spread, yield, price or relative-value claim and no peer ranking; only an aggregate fair value of the notes is cited as a source fact | Context quotes and peers are blank | Not required because no such claim is made | None | No effect on committee use |

#### Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A | CP-1 states the revolver borrower as Rocket Companies, Inc. from the exhibit list; CP-1A logs the borrower as an open distinction between the 2025 and 2026 agreements | None; same sources | Align wording: the 2026 agreement names Rocket Companies, Inc.; whether it replaces the 2025 agreement is not stated | None on figures |

Other shared data points agree across the four handoffs: senior notes principal 10,743, cash 2,699, revolver 2,500, secured financing 14,187, committed secured lines 7,400, LTM adjusted EBITDA 2,843, ratios 3.78x and 2.83x, legal reserves 216 and 74, verdict 175, servicing UPB 2,007,176, and the two logged source differences (the note offering date and the revolver borrower). An automated comparison found every number in CP-2 present in an upstream handoff. Issuer name, as-of date, run id and currency are the same in all four.

#### Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Source tag | Sector label "Mortgage Bankers and Loan Correspondents" comes from the run context but is tagged Documentary Fact, while the context is not issuer evidence | Tag as context setting | Low |

#### Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A, CP-2 | YAML front matter | Absent; the Markdown transport requires six headings and CP-OS owns envelope fields. This CP-5 handoff is in the same position | None needed in this run | None; each handoff was consumed by the next module with hashes matching |

### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-1A, CP-2 | Partially Supported Claim | Sponsor distribution evidence is incomplete: 120.1 special dividend cited, while tax distributions of 114, an equity statement total of 143 and combined FY2025 distributions of 241 are in the sources | Restate the distribution evidence and re-test the behaviour category | Restricts Committee Use | Open |
| CP5-002 | Material | CP-1, CP-1A, CP-2 | Legal Support Gap | Ranking, guarantor, borrower and distribution-capacity statements rest on summary notes; no executed documents | Obtain documents; treat as interpretation | Requires Legal Review | Open |
| CP5-003 | Minor | CP-0, CP-1 | Citation Gap | Wrong or partial locators (lease, MSR liabilities, Class L tie, partial table rows) | Correct and complete locators | Monitoring Follow-Up | Open |
| CP5-004 | Minor | CP-2 | Unsupported Characterisation | "Moderate" without benchmark; 5.65x used as headroom reference | Remove or qualify | Monitoring Follow-Up | Open |
| CP5-005 | Minor | CP-2 | Gap Propagation | EBITDA basis alignment gap in CP-1 not carried into CP-2 Gaps | Add the gap | Monitoring Follow-Up | Open |
| CP5-006 | Minor | CP-1, CP-1A | Cross-Module Inconsistency | Revolver borrower stated plainly in CP-1 and as an open distinction in CP-1A | Align wording | Formatting / Hygiene Only | Open |
| CP5-007 | Minor | CP-1A | Source tag | Context-derived sector tagged Documentary Fact | Retag | Formatting / Hygiene Only | Open |
| CP5-008 | Minor | CP-0, CP-1, CP-1A, CP-2 | canonical Markdown Handoff Integrity Defect | No YAML envelope under the transport | None needed in this run | Formatting / Hygiene Only | Open |

### Remediation priority map

Must-fix before committee: CP5-001 restate the 2025 owner distribution evidence in full and re-test the behaviour category; CP5-002 obtain the indentures, revolving credit agreement, repurchase agreements, governance letter agreement and proxy statement, and treat structure and distribution-capacity statements as interpretation until legal review.

Must-fix before canonical Markdown handoff is consumed downstream: None.

Monitoring follow-up: CP5-003 correct and complete the locators; CP5-004 qualify the adjective and drop the 5.65x reference; CP5-005 add the EBITDA basis gap to the synthesis; re-audit when documents or filings dated after October 30, 2026 arrive.

Formatting / hygiene: CP5-006 align borrower wording; CP5-007 retag the sector; CP5-008 none needed.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 6. Committee Use: Restricted.

No finding changes the credit conclusion, and every sampled figure traces to its source page. The two Material issues (CP5-001 and CP5-002) must be disclosed for committee use: owner distribution evidence in the business and synthesis handoffs is incomplete, and creditor structure and protection statements cannot be tested without debt documents.

## Calculations

Independent recomputation from the pinned sources (inputs read from the cited pages, not from the handoffs):

| Check | Inputs and locators | Result | Handoff value | Outcome |
| --- | --- | --- | --- | --- |
| LTM adjusted EBITDA | 1,281 (10-K page:104) + 2,252 - 690 (Q3 release page:8) | 2,843 | 2,843 | Reproduced |
| LTM to March and June 2026 | 1,281 + 738 - 169 (Q1 release page:8); 1,281 + 1,504 - 342 (Q2 release page:9) | 1,850; 2,443 | 1,850; 2,443 | Reproduced |
| Net debt | 10,455 - 2,696; 10,455 - 2,687; 10,805 - 3,103; 10,743 - 2,699 | 7,759; 7,768; 7,702; 8,044 | Same | Reproduced |
| Total debt / EBITDA | 10,455 / 1,281; 10,455 / 1,850; 10,805 / 2,443; 10,743 / 2,843 | 8.16; 5.65; 4.42; 3.78 | Same | Reproduced |
| Net debt / EBITDA | 7,759 / 1,281; 7,768 / 1,850; 7,702 / 2,443; 8,044 / 2,843 | 6.06; 4.20; 3.15; 2.83 | Same | Reproduced |
| LTM bond interest and cover | 335 + 139 - 38; 335 + 281 - 84; 335 + 435 - 195; 1,281 / 335; 1,850 / 436; 2,443 / 532; 2,843 / 575 | 436; 532; 575; 3.82; 4.24; 4.59; 4.94 | Same | Reproduced |
| FY2025 cash interest cover | 1,281 / 596 (10-K page:138) | 2.15 | 2.15 | Reproduced |
| All balance sheet financing ratio | (14,187 + 10,716) / 2,843; (17,936 + 10,423) / 1,281; (15,882 + 10,430) / 1,850; (16,639 + 10,772) / 2,443 | 8.76; 22.14; 14.22; 11.22 | Same | Reproduced |
| Debt tables foot | Notes 10,743; carrying 10,743 + 39 - 66; secured 12,042 + 1,801 + 344 (Q3 10-Q page:28 to page:30) | 10,743; 10,716; 14,187 | Same | Reproduced |
| Maturities and line-year sums foot | 0 + 503 + 0 + 1,500 + 2,076 + 2,214 + 1,000 + 2,850 + 600; 9 + 10,295 + 3,462 + 421 | 10,743; 14,187 | Same | Reproduced |
| Adjusted EBITDA quarters tie | 738 + 766 + 748; 169 + 172 + 349 | 2,252; 690 | 2,252; 690 | Reproduced |
| Equity less goodwill and intangibles | 24,311 - 10,686 - 1,880; 22,898 - 10,611 - 2,224 | 11,745; 10,063 | Same | Reproduced |
| Liquidity as stated and note-based figures | 2.7 + 2.5 + 6.2; 8,825 - 1,801; 4,475 - 1,801 | 11.4 billion; 7,024; 2,674 | 6.2 billion not reproducible | Reproduced; one component not reproducible |
| Servicing UPB and consideration | 1,201,476 + 805,700; 1,466 + 24 + 252; 13,667 + 193 + 3,113 | 2,007,176; 1,742; 16,973 | Same | Reproduced |
| Sampled figures and quotations found on the expected pages | 136 headline figures matched by whole-number text search against the page expected for each source, and 21 verbatim quotations including the two logged source differences | 136 of 136 and 21 of 21 found | Not applicable | No mismatch of value |
| Locator test of cited pages | Numbers in each cited cell tested against the pages named in the handoff | Wrong or partial locators found: lease 334, MSR liabilities 325, first and second quarter values in table rows, Class L tie | Not applicable | Logged as CP5-003 |

The 136 figure checks and 21 quotation checks are a sample and not an exhaustive check of every figure; every derived number in the registers above was recomputed. The comparison of every CP-2 number with the upstream handoffs found none missing.

## Gaps

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Debt documents, governance letter, proxy and guarantor lists | Indentures, revolving credit agreement, repurchase agreements, governance letter agreement of March 31, 2025, proxy statement | Ranking, covenant definitions, restricted payment capacity and control strength decide creditor protection and loss given default | Structure and owner behaviour statements in CP-1, CP-1A and CP-2 are interpretation | High impact | Executed documents and proxy statement |
| CP-5-GAP-002 | Covenant levels and reported headroom | Compliance certificates or facility-level covenant terms | Headroom cannot be measured | Covenant section is compliance statements and regulatory minimums only | Medium impact | Facility compliance information |
| CP-5-GAP-003 | Rating levels, outlooks and tranche prices | Agency publications and bond quotes | Market and agency views cannot be compared with the fundamental view | Credit view is fundamental only | Medium impact | Rating agency reports and quotes |
| CP-5-GAP-004 | Cash paid for interest in 2026 | Quarterly cash flow supplement | Cash interest cover exists for FY2025 only, on a mixed basis | Coverage is an accrual proxy for 2026 | Medium impact | Company supplemental data |
| CP-5-GAP-005 | Basis of 6.2 billion secured availability and cash composition | Availability calculation, buy-down and margin cash amounts | Usable liquidity may be lower than stated | Liquidity ties only for cash and revolver | Medium impact | Company disclosure |
| CP-5-GAP-006 | Fiscal 2025 on the 2026 presentation and a fourth quarter 2025 release | Recast fiscal 2025 interest captions and segments; fourth quarter 2025 earnings release | EBITDA basis alignment and revenue comparability cannot be confirmed | Leverage anchor depends on an unconfirmed alignment | Medium impact | Fourth quarter 2025 release and recast tables |
| CP-5-GAP-007 | Filings after October 30, 2026 | Filing list to November 5, 2026 | Late events, facility changes and the HouseCanary judgment are unverified | No source in the pack is dated after October 30, 2026 | Medium impact | Filing list to November 5, 2026 |
| CP-5-GAP-008 | Bridge Facility amount and any drawing | Credit agreement or note disclosure | Cannot confirm no bridge balance existed at any reporting date | Low | Low impact | Debt documents |
| CP-5-GAP-009 | Charts or images in earnings releases not inspected; no call transcript | Original release exhibits and transcript | Content outside text is unseen | None on figures cited | Low impact | Original exhibits |
| CP-5-GAP-010 | Completeness and handoff validation scripts | The scripts named in the skill are not in the repository folder; only the confidence script was available and was run | Mechanical register and envelope checks were done by hand and by search | Confidence score stated with disclosed inputs | Low impact | Run the validation scripts in the CP-OS toolchain |

## Next module

This is the last module in the requested set, so the report can be assembled from the accepted handoffs. Before committee use, apply the two Material remediations (restate the 2025 owner distribution evidence in full; obtain the debt documents, governance letter and proxy statement) and re-run this audit when those documents or any filing dated after October 30, 2026 arrive.
