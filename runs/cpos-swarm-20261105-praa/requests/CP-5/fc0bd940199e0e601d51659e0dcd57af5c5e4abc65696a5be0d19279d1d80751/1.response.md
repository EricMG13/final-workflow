# CP-5 — Evidence trace and research integrity QA: PRA GROUP INC (praa)

## Request

PRA GROUP INC, as of 2026-11-05, pathway credit_snapshot: trace the claims of the CP-0, CP-1, CP-1A and CP-2 handoffs to the pinned filings, recompute every derived figure, check cross-module consistency, and grade research integrity. Scope is the four upstream handoffs of this run; no credit conclusion is changed here and no source lineage is silently repaired.

## Sources

Locators are `page:N` of the pinned text files (source chunks, not printed page numbers). sha256 values are those CP-OS pins.

### Issuer sources

| Source (exact name) | sha256 | Use in this module |
| --- | --- | --- |
| 10-K_2025-12-31_praa-20251231.htm.jsonl | acaea144d244584c3474f86549753d209ff125e0c5d293c88092a8b3609d005e | Opened to trace debt, covenants, cash flows, segments, ownership and policy claims |
| 10-Q_2025-09-30_praa-20250930.htm.jsonl | 929f20928dbfde158b90287ecb3f34f89e93248de03667dc981595cbc1f16f43 | Opened to trace September 30, 2025 balances, goodwill impairment, last-twelve-months Adjusted EBITDA |
| 10-Q_2026-03-31_praa-20260331.htm.jsonl | 5b8ee1fe62f8b0079ea63a2a1c4f92f69a59ebc645588dbcce6f190c45211b32 | Opened to trace March 31, 2026 balances, availability, amendment note |
| 10-Q_2026-06-30_praa-20260630.htm.jsonl | d7a354d31f5af038cbd610321c408a92f38ffbe0be4451883080ac13fa2cd5a8 | Opened to trace June 30, 2026 statements, borrowings, availability, ERC, market risk, subsequent event |
| EX-99.1_2026-02-26_q42025earningsrelease.htm.jsonl | ac28ac408106b5058aef5a7017ad24c9c2f1059768c1e80795f1a5ba0705218f | Opened to cross-check FY2025 and FY2024 Adjusted EBITDA |
| EX-99.1_2026-05-07_q12026earningsrelease.htm.jsonl | 0cafa2dd16d8fe170df8f95a181353ea848b2d370eaa0bad903e81ca9ab40ac1 | Opened to trace the last-twelve-months Adjusted EBITDA to March 31, 2026 |
| EX-99.1_2026-08-06_q22026earningsrelease.htm.jsonl | 90c4b9dc1bbbec8846231ce65b511117fe19795284263ee0dc2f0a68914940d4 | Opened to trace management commentary and the Adjusted EBITDA reconciliation to June 30, 2026 |

### Run settings (not issuer evidence)

| Source | sha256 | Role |
| --- | --- | --- |
| context (1185348-pra-group-inc-praa.json) | fb395d626a32c7d3e686eb338c55b901d79ab38a3782a023f0c732503b0056b3 | Dated user settings; blank fields are unknown, not zero. |

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | ad930b06ca8dfafbd7d05aa59918ec9f5ec7345e1f274cfd0ac40c5b9907cbbd | Source readiness; re-anchored for identity, as-of date and source hashes |
| CP-1 | f504ebf424f2b6080338462ae74293629fc8293218527f27a4fbeb97c3179884 | Financial base under review |
| CP-1A | 7ef973de3d6ffddb47e9f6283951b59270b39a7a5b808c9a73fc485a4265b73d | Business and transaction context under review |
| CP-2 | 0c84ce8694925e5a8959c3c5d9333637422c4152830c152b06a914e0284da6d3 | Credit synthesis under review |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial, business and synthesis work traces to the filings and every derived figure recomputes. One material framing defect and six minor citation or wording defects are logged; covenant and legal conclusions remain unsupported by supplied documents. | Medium | Executed debt documents and covenant ratio levels are not supplied, so ranking, guarantor and headroom statements cannot be traced to primary text. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every headline ratio, liquidity figure and maturity amount was recomputed from printed inputs and agreed. | Leverage, cover, liquidity and maturity conclusions can be relied on as stated, on the issuer's own EBITDA definition. | High |
| Investments of USD 145.5 million were described as held for the banking subsidiary, but the filing supports USD 144.1 million. | Minor wording defect; net debt is unaffected because investments are excluded either way. | High |
| Noteholders ranking behind secured lenders is stated as fact in the synthesis but rests on filing summaries, as the indentures and credit agreements are not supplied. | Treat ranking and guarantor conclusions as unverified until the executed documents are traced. | Medium |
| The June 30, 2026 maturity schedule is derived from instrument terms, with the Colombian facility of USD 0.245 million placed in 2028 by inference. | The 2028 and 2029 amounts are reliable to within that amount; the derivation should be confirmed with the issuer. | Medium |
| The European review is an ERC increase of USD 348.5 million, not income; the filing puts the income effect near USD 105 million, and all modules keep the distinction. | Earnings-quality conclusions are consistent across the work. | High |

### Evidence trace view

The credit work for PRA Group is traceable enough for committee use with restrictions, because every headline figure rests on filed statements and recomputes exactly. The strongest support is that leverage, cover, liquidity and maturity numbers all agree with printed inputs, and management claims are tagged as management language rather than fact. The weakest point is that no executed credit agreement or indenture is supplied, so covenant headroom, ranking and guarantor statements rest on filing summaries and cannot be traced to primary legal text. The outcome turns on whether those documents and any report for the quarter ended September 30, 2026 can be obtained; until then conclusions that depend on them stay restricted. One material framing defect and six minor defects are logged for correction.

### Traceability conclusion

Scope and method. Every numeric claim in the Reader summary rows and key tables of CP-1, CP-1A and CP-2 was opened at its cited page or located on a neighbouring page of the same source; every number in the CP-1 financial table was checked against the cited statements by search; and every derived figure (CP-1 C1 to C9, CP-2 K1 to K9) was recomputed from its printed inputs. Narrative sentences were traced where they carry a number, a date or a legal characterisation. Prose without figures (for example descriptive business text) was sampled and not exhaustively traced.

Result. No unsupported headline claim, no figure without a source and no arithmetic error was found. Identity, as-of date and source hashes in the upstream handoffs match the run. Management characterisations ("record ERC levels", competitive strengths, ability to slow purchases) are tagged Management Language. Two analyst constructs (illustrative cash bridge, cost-adjusted ERC cover) are labelled as such. Confidence score and band are not computed here because the scoring script is not available in this host run; the Medium confidence stated is a judgment.

### Top material credit drivers and their traceability

| Rank | Credit driver | Module | Basis | Traceability |
| --- | --- | --- | --- | --- |
| 1 | Forecast-dependent revenue, ERC and ERC-linked availability | CP-1, CP-1A, CP-2 | Q2 10-Q page:9, page:24, page:40 and page:41 | Fully traced; the income effect (approximately USD 105 million) and the ERC change (USD 348.5 million) are kept apart |
| 2 | Moderate leverage and strong cash interest cover on issuer Adjusted EBITDA | CP-1, CP-2 | Q2 10-Q page:11, page:35, page:5; 10-K page:71 | Fully traced and recomputed; definition limit carried |
| 3 | Debt-funded purchasing (shortfall after interest, taxes and capital expenditure) | CP-1, CP-2 | 10-K page:70, page:71; Q2 10-Q page:5 | Recomputed; an analyst construct, labelled |
| 4 | Maturity profile with a 2029 cluster and European extension to 2031 | CP-1, CP-2 | Q2 10-Q page:11, page:42; Q1 10-Q page:17 | Derived schedule recomputed; Colombian placement inferred |
| 5 | Covenant opacity and unsupplied legal documents | CP-0, CP-1, CP-1A, CP-2 | 10-K page:87 to page:89; Q2 10-Q page:11, page:48 | Correctly handled as Insufficient Information; ranking statement needs reframing |

### Analytical appendix — complete canonical registers

#### T5.1 Handoff register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1; praa-2026-11-05-credit_snapshot-host | Seven filings and releases, readiness | Filed statements and furnished releases, text conversion | Six H2 headings present; Reader summary then Readiness view | Accepted by CP-OS; traced | Identity, as-of date and hashes re-anchored |
| CP-1 | requests/CP-1 attempt 1; same run_id | Financial base to June 30, 2026 | Filed statements; issuer non-GAAP measures labelled | Six H2 headings; Reader summary, Financial base view and all five selectors present | Accepted by CP-OS; two minor wording defects | All C1 to C9 recomputed |
| CP-1A | requests/CP-1A attempt 2; same run_id | Business, ownership, transactions, governance | Filed text; management language tagged | Six H2 headings; the three selectors present | Accepted by CP-OS; traced | Attempt 2 corrected a number in the Reader summary |
| CP-2 | requests/CP-2 attempt 1; same run_id | Fundamental credit synthesis | Upstream handoffs plus filing pages opened | Six H2 headings; Credit view, Key findings, Strengths and weaknesses present | Accepted by CP-OS; one material framing defect | K1 to K9 recomputed |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Liquidity table and definition review: investments of 145,473 described as held for the banking subsidiary (Q2 10-Q page:43) | Partly supported | The filing says USD 117.6 million of Swedish treasury securities and USD 26.5 million of Finnish corporate notes, USD 144.1 million together, are held to meet the banking subsidiary's liquidity requirements; the balance sheet shows investments of USD 145.5 million | State only the USD 144.1 million as held for the banking subsidiary | None on ratios; investments are excluded from cash either way |
| Minor | CP-1 | Definition review: collections applied to principal of 1,099,148 in FY2025, cited to Q2 10-Q page:44 | Supported, citation imprecise | The figure is in the 10-K cash flow statement (page:70); Q2 10-Q page:44 supports only the classification in investing activities | Cite 10-K page:70 for the amount | None |
| Minor | CP-2 | Key findings: ERC-based availability "at advance rates of 35% for Core and 55% for Insolvency pools" (10-K page:87) | Partly supported | The rates are from the North American facility; the UK facility uses the same rates (10-K page:88) but the European facility is governed by an ERC ratio cap (10-K page:89), and the Q2 10-Q describes the range as 35-55% (page:41) | Say "advance rates of 35-55% of applicable ERC" | None |
| Minor | CP-2 | Secured share 56.5% treats the Colombian facility (245) as secured | Partly supported | Security of the Colombian facility is not stated | Footnote the exclusion; effect is below 0.01 of a percentage point | None |
| Minor | CP-1 | Maturity chart places the Colombian facility (USD 0.245 million) in 2028 | Supported by inference | Maturity of that facility is not stated; the 10-K year totals and the Q2 10-Q statement that other principal is due from February 2028 are consistent with 2028 | Keep the inference label; confirm with the issuer | None |
| Minor | CP-2 | Credit view and Reader summary: "adequate and stable" | Supported for the period covered | Latest data is June 30, 2026 and filings end August 7, 2026, 90 days before the as-of date; "stable" is an outlook word | Qualify as stable on data to June 30, 2026 | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Gross and net leverage (2.78x, 2.68x) and cash interest cover (5.36x) recomputed: 3,771,251 / 1,358,913; (3,771,251 − 132,431) / 1,358,913; 1,358,913 / 253,430 | Adjusted EBITDA is the issuer's non-GAAP measure and adds back collections applied to principal; it is not covenant EBITDA | No conflict between the 10-K, 10-Q and releases for Adjusted EBITDA | Keep the definition caveat wherever the ratios appear | Ratios cleared with the caveat; not comparable to covenant limits |
| Minor | CP-1 | Derived last-twelve-months cash interest (253,430, 256,029, 261,450) | Cash paid for interest from the cash flow supplemental line; composition not itemized | None | Keep the derivation visible | Cleared |
| Minor | CP-1, CP-2 | Illustrative cash bridge: FY2025 shortfall 190,676 and FY2024 shortfall 502,881 | Not an issuer measure; excludes noncontrolling distributions, repurchases and fees | None | Keep the construct label | Cleared as analyst construct |
| Minor | CP-2 | Cost-adjusted ERC cover 1.44x (8,894,515 x 61.2% / 3,771,251) | ERC is undiscounted and before interest, taxes and future purchases; the cost ratio is a Q2 2026 figure | None | Keep the construct label; do not present as coverage | Cleared as sensitivity |
| Minor | CP-1 | Derived maturity schedule sums to 3,771,251, equal to printed principal; the 10-K schedule at December 31, 2025 is reproduced by the same method (2028: 410,611; 2029: 1,800,695) | Revolvers shown in full at final maturity; Colombian placement inferred | The 10-K 2027 amount of 587,335 is superseded for the European facility by the April 30, 2026 amendment: sequential, not conflicting | None beyond the existing labels | Cleared |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-2 | Reader summary and Key findings: "Noteholders rank behind secured lenders on the collateral; guarantor coverage of European assets is not evidenced" | Indentures for the 2028, 2029, 2030 and 2032 notes; North American, UK and European credit agreements and security documents | Facility security is described in the 10-K (page:87 to page:89) and note guarantees in page:90 to page:92; the executed documents are not supplied, so ranking, intercreditor terms and guarantor reach are untraced | Present as Analyst Interpretation resting on filing summaries; keep guarantor coverage as unverified | Yes: executed documents |
| Minor | CP-1A, CP-2 | European facility amended to 2031 with ERC ratio cap cut to 40.0% and a EUR 100 million joint venture basket | Second Amended and Restated European credit agreement (Q2 10-Q Exhibit 10.1, page:48) | Terms are traced to summaries in Q1 10-Q page:17 and Q2 10-Q page:11; the agreement is not supplied | Keep the basket as unevidenced in use | Yes |
| Minor | CP-1, CP-2 | Covenant tests (3.50x total leverage, 2.50x senior secured leverage, 2.00x fixed charge coverage, dividends cap of 50.0 million) | Executed credit agreements | Levels traced to the 10-K (page:87 to page:89); ratio values and definitions not supplied | None; correctly handled as Not supplied | Yes |
| Minor | CP-1A | Governance: no priming, uptiering, drop-down or leakage "described in the supplied sources" | Credit agreements and indentures | Absence in summaries is not evidence of absence; CP-1A says so | None | Yes |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A, CP-2 | No market price, spread, peer or relative value claim is made in any handoff | Prices, spreads, ratings, peer data (context fields blank) | By design outside the minimum module set | None; keep ratings and market data as Not supplied | None for the fundamental view |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Debt principal 3,771,251, cash 132,431, availability 998,468, Adjusted EBITDA 1,358,913 and ERC 8,894,515 agree wherever stated across the four handoffs | One source set; same hashes in all four | None | Consistent |
| Minor | CP-1, CP-1A, CP-2 | European forecast review: ERC increase 348.5 million versus income effect of about 105 million versus the release's "approximately $349 million" ERC increase driving the rise in changes in expected recoveries | The release (August 6, 2026) and the 10-Q (August 7, 2026) describe different measures | Keep the distinction; use the filing for the income effect | Consistent |
| Minor | CP-0, CP-1 | CP-0 states the Q2 10-Q key metrics table prints the prior-year last-twelve-months Adjusted EBITDA; CP-1 uses it (1,240,092) | None | None | Consistent |
| Minor | CP-1, CP-2 | CP-2 states "no corrections to upstream handoffs"; this review finds the two minor wording points logged at T5.2 in CP-1 | CP-1 cannot be edited | Carry the corrections in this handoff | Downstream readers should apply the T5.2 corrections |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Duplication | The leverage, cover and liquidity figures are restated in CP-2; restatements match | None | None |
| Minor | CP-2 | Materiality | The ranking statement is material to a noteholder view but not to the fundamental credit view | Reframe at T5.4 | Restricts structural conclusions only |
| Minor | CP-1A | Readiness | Seller concentration, proxy statement and ownership detail are Insufficient Information by design | None | Governance scoring not possible |

#### T5.8 Structured export and handoff components

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Required headings and selectors | None found; each handoff has the six H2 headings, a Reader summary followed by its view section, and the report selectors named in its method | None | Report sections can be populated |
| Minor | CP-1 | Chart data tables | Value cells are plain numbers with unit, one row per period; maturities are derived, with limitation text in every row | None | Charts can be drawn; show the derivation note |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I1 | Minor | CP-1 | Citation support | Investments described as held for the banking subsidiary; filing supports USD 144.1 million of USD 145.5 million | Reword | None | Open |
| I2 | Minor | CP-1 | Citation locator | 1,099,148 cited to page:44 instead of 10-K page:70 | Re-cite | None | Open |
| I3 | Material | CP-2 | Legal and structural claim | Ranking behind secured lenders stated as fact on summaries | Reframe as Analyst Interpretation | Restricts structural conclusions | Open |
| I4 | Minor | CP-2 | Generalisation | Advance rates of 35% and 55% applied to all ERC-based availability | Say 35-55% of applicable ERC | None | Open |
| I5 | Minor | CP-2 | Perimeter | Colombian facility included in secured share without stated security | Footnote | None | Open |
| I6 | Minor | CP-1 | Inference | Colombian facility placed in 2028 by inference | Confirm with the issuer | None | Open |
| I7 | Minor | CP-2 | Outlook wording | "Stable" used with data ending June 30, 2026 | Qualify | None | Open |

#### T5B.1 Source lineage register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_praa-20251231.htm.jsonl | Filed, audited statements (Ernst & Young LLP, March 2, 2026) | Years ended December 31, 2025, 2024, 2023 | PRA Group, Inc. consolidated | Statements, borrowings, covenants, segments, legal, ERC | Text conversion; exhibits not supplied | CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2025-09-30_praa-20250930.htm.jsonl | Filed, unaudited | Quarter and nine months to September 30, 2025 | PRA Group, Inc. consolidated | Balance sheet, goodwill impairment, borrowings, LTM Adjusted EBITDA | Single-segment basis | CP-1 liquidity and leverage rows |
| S3 | 10-Q_2026-03-31_praa-20260331.htm.jsonl | Filed, unaudited, signed May 8, 2026 | Quarter to March 31, 2026 | PRA Group, Inc. consolidated | Balance sheet, borrowings, availability, amendment note | Text conversion | CP-1, CP-1A |
| S4 | 10-Q_2026-06-30_praa-20260630.htm.jsonl | Filed, unaudited, signed August 7, 2026 | Quarter and six months to June 30, 2026 | PRA Group, Inc. consolidated | Statements, borrowings, availability, ERC, market risk | Cash flows year-to-date only | All modules |
| S5 | EX-99.1_2026-02-26_q42025earningsrelease.htm.jsonl | Furnished release, unaudited | Q4 and full year 2025 | PRA Group, Inc. consolidated | Cash collections by source, reconciliations | Management presentation | Cross-check |
| S6 | EX-99.1_2026-05-07_q12026earningsrelease.htm.jsonl | Furnished release, unaudited | Q1 2026 | PRA Group, Inc. consolidated | LTM Adjusted EBITDA to March 31, 2026 | Management presentation | CP-1 leverage rows |
| S7 | EX-99.1_2026-08-06_q22026earningsrelease.htm.jsonl | Furnished release, unaudited | Q2 2026 | PRA Group, Inc. consolidated | Commentary, LTM reconciliation | Management presentation | CP-1, CP-1A |

#### T5B.2 Top five material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Forecast-dependent revenue, ERC and ERC-linked availability | CP-1A, CP-2 | Revisions recognised in changes in expected recoveries; availability partly based on current ERC | Earnings and liquidity move together on a revision | Monitor each quarterly assessment | S4 page:9, page:24, page:40, page:41 | Model inputs not visible |
| 2 | Moderate leverage and strong cash interest cover | CP-1, CP-2 | Debt principal over issuer Adjusted EBITDA | Core debt-service capacity measure | Compare quarter by quarter | S4 page:11, page:35; S1 page:71 | Not covenant EBITDA |
| 3 | Debt-funded purchasing | CP-1, CP-2 | Purchases exceed EBITDA after cash interest and taxes | Drives leverage direction | Watch purchase pace against EBITDA growth | S1 page:70, page:71; S4 page:5 | Analyst construct |
| 4 | 2029 maturity cluster and 2031 European maturity | CP-1, CP-2 | Instrument maturities | Refinancing concentration | Track market access before 2029 | S4 page:11, page:42 | Derived schedule |
| 5 | Covenant opacity | CP-1, CP-2 | Levels printed, ratios not | Headroom unobservable | Obtain agreements and certificates | S1 page:87 to page:89 | Documents not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gross debt 2.78x and net 2.68x LTM Q2 2026 | CP-1, CP-2 | S4 page:11 (debt), page:2 (cash), page:35 (EBITDA) | Yes | Filed | Calculated | Supported; recomputed | High | Fully traced |
| Cash interest cover 5.36x | CP-1, CP-2 | S1 page:71; S4 page:5 | Yes | Filed | Calculated | Supported; recomputed | High | Fully traced |
| Liquidity cover of the next 12 months 4.57x | CP-2 | S4 page:2, page:40, page:42 | Yes | Filed | Calculated | Supported; letters of credit not deducted | Medium | Traced with a stated gap |
| Funding shortfall after interest and taxes | CP-1, CP-2 | S1 page:70, page:71 | Yes | Filed | Analyst Inference | Supported arithmetic; construct | Medium | Traced |
| 48.7% of principal due in 2029 | CP-1, CP-2 | S4 page:11, page:42 | Yes | Filed | Calculated | Supported; Colombian inferred | Medium | Traced with inference |
| European facility extended to April 30, 2031 | CP-1A, CP-2 | S3 page:17; S4 page:11 | Yes | Filed | Directly Sourced | Supported | High | Fully traced |
| Changes in expected recoveries 63.2% of income from operations | CP-1, CP-2 | S4 page:3 | Yes | Filed | Calculated | Supported; recomputed | High | Fully traced |
| Secured facilities 56.5% of principal; notes rank behind | CP-2 | S4 page:11; S1 page:87 to page:92 | Yes | Filed summary | Analyst Inference | Partly supported (legal documents absent) | Medium | Traced to summaries (issue I3) |
| Neutral or Mixed capital allocation | CP-1A, CP-2 | S1 page:38, page:37; S4 page:15, page:21 | Yes | Filed | Analyst Inference | Supported by documented actions | Medium | Traced |
| About 60% of debt fixed or converted; USD 7.8 million per 50 basis points | CP-2 | S4 page:46 | Yes | Filed | Directly Sourced | Supported | High | Fully traced |
| Management ability to slow purchases; "record ERC levels"; competitive strengths | CP-1A, CP-2 | S1 page:55, page:10; S7 page:2 | Yes | Management statements in filings and release | Weak Lineage as fact; tagged Management Language | Correctly tagged | Medium | Traced as management claims |

#### T5B.4 Source path and locator register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Debt principal 3,771,251 at June 30, 2026 | packs/1185348-pra-group-inc-praa | 10-Q_2026-06-30_praa-20260630.htm.jsonl | S4 | page:11, Note 5 | CP-1 Debt by instrument | Statement note | Filed | Agrees |
| Cash and cash equivalents 132,431 | packs/1185348-pra-group-inc-praa | 10-Q_2026-06-30_praa-20260630.htm.jsonl | S4 | page:2, balance sheet | CP-1 liquidity | Statement | Filed | Agrees |
| Total availability 998,468 (733,096 and 265,372) | packs/1185348-pra-group-inc-praa | 10-Q_2026-06-30_praa-20260630.htm.jsonl | S4 | page:40 and page:41 | CP-1 liquidity table | MD&A table | Filed | Agrees; sums by facility agree |
| LTM Adjusted EBITDA 1,358,913 and prior year 1,240,092 | packs/1185348-pra-group-inc-praa | 10-Q_2026-06-30_praa-20260630.htm.jsonl | S4 | page:25 and page:35 | CP-1 EBITDA table | Non-GAAP | Filed | Agrees; release page:11 agrees |
| FY2025 Adjusted EBITDA 1,315,474 | packs/1185348-pra-group-inc-praa | 10-K_2025-12-31_praa-20251231.htm.jsonl | S1 | page:45 and page:46 | CP-1 leverage | Non-GAAP | Filed | Agrees; Q4 release page:11 agrees |
| Cash paid for interest 259,061 (FY2025), 224,099 (FY2024) | packs/1185348-pra-group-inc-praa | 10-K_2025-12-31_praa-20251231.htm.jsonl | S1 | page:71 | CP-1 interest cover | Cash flow supplemental | Filed | Agrees |
| Cash paid for interest 126,959 and 132,590 for six months | packs/1185348-pra-group-inc-praa | 10-Q_2026-06-30_praa-20260630.htm.jsonl | S4 | page:5 | CP-1 interest cover | Cash flow supplemental | Filed | Agrees |
| Euro facility amended: maturity April 30, 2031, ERC ratio cap 40.0% | packs/1185348-pra-group-inc-praa | 10-Q_2026-03-31_praa-20260331.htm.jsonl | S3 | page:17, Note 15 | CP-1A transaction summary | Subsequent event | Filed | Agrees; Q2 10-Q page:11 repeats |
| European ERC increase 348.5 million; about 105 million income effect | packs/1185348-pra-group-inc-praa | 10-Q_2026-06-30_praa-20260630.htm.jsonl | S4 | page:24 and page:9 | CP-1A, CP-2 | MD&A | Filed | Agrees |
| Q2 2026 changes in expected recoveries 96,924; income from operations 153,282 | packs/1185348-pra-group-inc-praa | 10-Q_2026-06-30_praa-20260630.htm.jsonl | S4 | page:3 | CP-1 financial table | Statement | Filed | Agrees |
| 2032 notes: EUR 300.0 million, 6.250%, September 30, 2032, issuer PRA Group Europe Holding II S.à r.l. | packs/1185348-pra-group-inc-praa | 10-K_2025-12-31_praa-20251231.htm.jsonl | S1 | page:90 | CP-1 debt table; CP-1A | Note | Filed | Agrees |
| Covenant tests and levels | packs/1185348-pra-group-inc-praa | 10-K_2025-12-31_praa-20251231.htm.jsonl | S1 | page:87 to page:89 | CP-1 covenant table | Note | Filed summary | Agrees; ratios not printed |
| 44 holders of record; no dividends in three years | packs/1185348-pra-group-inc-praa | 10-K_2025-12-31_praa-20251231.htm.jsonl | S1 | page:36 and page:37 | CP-1A profile | Item 5 | Filed | Agrees |
| Segment reorganization in Q4 2025 after new CEO | packs/1185348-pra-group-inc-praa | 10-K_2025-12-31_praa-20251231.htm.jsonl | S1 | page:103 | CP-1A, CP-1 | Note 16 | Filed | Agrees |
| About 60% fixed or converted; USD 7.8 million per 50 basis points | packs/1185348-pra-group-inc-praa | 10-Q_2026-06-30_praa-20260630.htm.jsonl | S4 | page:46 | CP-2 | Item 3 | Filed | Agrees |
| USD 247.7 million estimated interest, unused fees and principal for 12 months | packs/1185348-pra-group-inc-praa | 10-Q_2026-06-30_praa-20260630.htm.jsonl | S4 | page:42 | CP-2 | MD&A | Filed | Agrees |
| Goodwill impairment 412,611 in Q3 2025 | packs/1185348-pra-group-inc-praa | 10-Q_2025-09-30_praa-20250930.htm.jsonl | S2 | page:3 and page:12 | CP-1, CP-1A | Statement and note | Filed | Agrees |
| New repurchase program up to 150 million, August 3, 2026 | packs/1185348-pra-group-inc-praa | 10-Q_2026-06-30_praa-20260630.htm.jsonl | S4 | page:21, Note 15 | CP-1A | Subsequent event | Filed | Agrees |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Gross and net debt over Adjusted EBITDA (five periods) | CP-1 C1, C2; CP-2 | Debt principal, cash, Adjusted EBITDA | Debt / EBITDA; (debt − cash) / EBITDA | Recomputed by CP-5; agrees (2.934, 2.862, 2.821, 2.812, 2.775 gross) | Supported | High | Leverage | S1 page:86; S2 page:12; S3 page:8; S4 page:11 |
| Derived last-twelve-months cash interest and cover | CP-1 C3, C4 | FY2025 cash interest less prior year-to-date plus current year-to-date | As stated | Recomputed; agrees (253,430; 256,029; 261,450; cover 5.362, 5.267, 4.840) | Supported | High | Coverage | S1 page:71; S2 page:6; S3 page:4; S4 page:5 |
| Tie-outs of printed totals | CP-1 C5 | Reconciliation columns, LTM net loss, availability sums, borrowings | Sum checks | Recomputed; agrees | Supported | High | Data quality | S4 page:25, page:35, page:40, page:11 |
| Liquidity (cash plus availability) six dates | CP-1 C6 | Cash and total availability | Sum | Recomputed; agrees | Supported | High | Liquidity | S1 page:40, page:54, page:68; S2 page:26; S3 page:32; S4 page:25, page:40 |
| Derived maturity schedule at June 30, 2026 | CP-1 C7 | Instrument maturities and principal; term loan 2.5 million quarterly | Allocation by year | Recomputed; sums to 3,771,251; December 2025 method reproduces the 10-K totals | Supported with inference (Colombian) | Medium | Refinancing | S4 page:11, page:42; S1 page:86 |
| Illustrative cash bridge | CP-1 C8, CP-2 K8 | EBITDA, cash interest, cash taxes, portfolio purchases, capital expenditure | Subtraction | Recomputed; agrees (−190,676; −502,881; net debt cash flows 253,814 and 465,858) | Supported; analyst construct | Medium | Funding gap | S1 page:70, page:71 |
| Other ratios: ERC to debt, growth rates, share of income | CP-1 C9, CP-2 K7, K9 | ERC, debt, EBITDA, revenue lines | Division | Recomputed; agrees (2.36x, 2.32x, 2.24x; 13.0%; 19.5%; 63.2%; 54.9%) | Supported | High | Context | S4 page:3, page:25, page:37 |
| Maturity concentration, secured share, ERC-based share | CP-2 K1, K2, K3 | Derived schedule, borrowings note, availability table | Division | Recomputed; agrees (48.7%, 11.2%, 56.5%, 43.5%, 73.4%) | Supported; Colombian caveats | Medium | Refinancing and structure | S4 page:11, page:40 |
| Liquidity cover and rate sensitivity | CP-2 K4, K5 | Cash, availability, 247,700, 7,800, cash interest | Division | Recomputed; agrees (4.57x, 4.03x, 3.1%) | Supported | Medium | Liquidity, rate risk | S4 page:42, page:46 |
| Cost-adjusted ERC cover | CP-2 K6 | ERC, Q2 2026 cash efficiency 61.2% (Q2 10-Q page:25), debt principal | ERC x ratio / debt | Recomputed; agrees (5,443,443; 1.44x) | Analyst construct | Low | Sensitivity only | S4 page:25, page:37 |

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Noteholders rank behind secured lenders | Rests on summaries; no executed documents | Analyst Inference | Structural conclusions need primary text | Reframe; obtain documents | CP-2 Reader summary and Key findings |
| Minor | Investments held for the banking subsidiary | Overstated by USD 1.4 million of investments not described | Partly supported | Perimeter wording | Reword | CP-1 liquidity and definition review |
| Minor | Collections applied to principal of 1,099,148 | Locator points to page:44 | Citation imprecise | Traceability | Re-cite 10-K page:70 | CP-1 definition review |
| Minor | Ability to slow purchases | Management claim, tagged | Management Language | Not independent evidence | Keep tag | CP-2 strengths |
| Minor | Colombian facility maturity and security | Not stated | Inference | Small amount | Confirm | CP-1, CP-2 |
| Minor | "Stable" outlook wording | Data end June 30, 2026 | Analyst Inference | Currency of view | Qualify | CP-2 |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Locator precision | Strong; two imprecise cites | Page locators on nearly every figure | A wrong locator slows verification but does not change a figure | None on conclusions | Fix I1 and I2 |
| Calculation reproducibility | Strong | All derived figures recompute from stated inputs | Hidden steps would undermine ratios | Ratios reliable | None |
| Definition consistency (EBITDA) | Adequate | Issuer non-GAAP measure used consistently; covenant definition absent | Mixing definitions would overstate headroom | Ratios not comparable to covenant limits | Carry the caveat |
| Period and perimeter alignment | Strong | LTM, fiscal year and point-in-time rows are labelled; consolidated perimeter throughout | Mixed periods would distort ratios | None | None |
| Management versus fact | Strong | Management Language tagged in CP-1A and CP-2 | Adopting management claims would bias the view | None | None |
| Subsequent events | Strong | April 30, 2026 amendment and August 3, 2026 buyback labelled as such | Blending events into period figures | None | None |
| Legal lineage | Weak | Executed documents absent | Ranking and capacity claims untraceable | Structural conclusions restricted | Obtain documents |
| Currency and units | Strong | USD thousands; US$m conversions exact; euro notes translated at printed rates | Unit errors | None | None |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Executed credit agreements and indentures | Documents not in the pack | Covenant definitions, ranking, guarantors | Structural conclusions restricted | Caps confidence at Medium | Issuer filings (exhibits) |
| G2 | Covenant ratio levels | Not printed in the filings read | Headroom | Headroom not assessable | Caps confidence | Compliance certificates |
| G3 | Events after August 7, 2026 | No later filing | Currency of the view | View as of June 30, 2026 data | Reduces confidence in outlook wording | Later 8-K and 10-Q filings |
| G4 | Letters of credit drawn on the North American facility | Only a sub-limit is stated | Liquidity net of usage | Liquidity slightly overstated if drawn | Minor | Facility usage disclosure |
| G5 | Colombian facility maturity and security | Not stated | Maturity and secured share | Immaterial amount | Minor | Issuer |
| G6 | Interest-bearing deposit maturities | Not supplied | Debt perimeter | Net debt sensitivity only | Minor | Issuer |
| G7 | Seller concentration; accrued amount of the Attorneys General matter | Not disclosed in the pages read | Supply and litigation risk | Qualitative risk only | Minor | Issuer disclosure |
| G8 | Confidence score script output | Scoring script not run in this host session | Formal band and score | Band stated as judgment | Not computed | Re-run with the scoring script |

### Remediation priority map

First, reframe the structural ranking statement in CP-2 (issue I3) as an Analyst Interpretation resting on filing summaries, and obtain the executed credit agreements, security documents and indentures; this removes the only material defect and lifts the legal restriction. Second, correct the two CP-1 wording and locator points (I1, I2) and the CP-2 generalisation of advance rates (I4). Third, confirm the Colombian facility maturity and security (I5, I6) and qualify "stable" (I7). Fourth, obtain any filing after August 7, 2026, including the report for the quarter ended September 30, 2026, and refresh leverage, liquidity and ERC.

### Clearance decision

Committee status: Restricted. The fundamental credit view and the financial base may be used, with the stated definition limits, as a view on data to June 30, 2026. Conclusions on covenant headroom, ranking, guarantor reach and legal capacity may not be used until the executed documents are traced. Research QA status: Restricted. Prohibited conclusions respected: no change to the underlying credit conclusion and no silent repair of source lineage; corrections are carried here because the earlier handoffs cannot be edited.

## Calculations

CP-5 recomputed every upstream derived figure and made no new credit calculation. Recomputation results are recorded at T5B.5 with inputs and agree to the upstream values. The only figures introduced here are quotations: USD 144.1 million is the sum of USD 117.6 million and USD 26.5 million of securities held for the banking subsidiary (Q2 10-Q page:43), compared with investments of USD 145.5 million on the balance sheet (Q2 10-Q page:2); the difference is USD 1.4 million, rounded from 145,473 less 144,100.

## Gaps

Gaps are in the ledger at T5B.8 (G1 to G8). The two that restrict the clearance decision are G1, the executed credit agreements and indentures, and G2, the covenant ratio levels. G3, nothing after August 7, 2026, limits the currency of every conclusion.

## Next module

This is the last module in the minimum set. Reviewers should apply the corrections at T5.2 and T5.9 when reading CP-1 and CP-2, treat the ranking statement as an Analyst Interpretation, and obtain the executed debt documents and any filing after August 7, 2026 before relying on covenant, structural or current-position conclusions.
