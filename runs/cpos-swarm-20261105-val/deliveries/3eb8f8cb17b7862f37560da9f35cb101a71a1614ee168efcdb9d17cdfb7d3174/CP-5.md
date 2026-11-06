# CP-5 — Evidence trace and research-integrity QA: Valaris Ltd (val)

## Request

- Issuer: Valaris Ltd (issuer id `val`), as of 2026-11-05, information cutoff 2026-11-05. Run `val-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, `minimum` module set. CP-5 checks CP-0, CP-1, CP-1A and CP-2 against the seven pinned filings and grades the result (absorbed CP-5A phase).
- Execution: host session. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.
- Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- QA envelope: `qa_status` Passed; Confidence Score 45, band Low (from `scripts/confidence_score.py`, see Calculations); `committee_status` Requires More Work.

## Sources

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_val-20251231.htm.jsonl | b0f40796936a513fe6362c5f87d6a2a2819cd2f6e423112bfcf4a7c94647ac50 |
| 10-Q_2026-03-31_val-20260331.htm.jsonl | 856b19f20ceb9a456e4cf71dc5d1f96d12072575504148e1684cf5301164037f |
| 10-Q_2026-06-30_val-20260630.htm.jsonl | d045ec4aa0f0c5450f1ffc05520139072532c8f88ec1804bd561ac63d9d380b7 |
| 10-Q_2026-09-30_val-20260930.htm.jsonl | 73a1a96ecd1c9340e41638f2528ea86ae030d4c896022c1e422144610c8461ec |
| EX-99.1_2026-05-04_a03312026ex991pressrelease.htm.jsonl | fb13914842f3e3a58a0b5ccdbd3cb04d0eb99161ae6d4b18bdfd3afa295e84b5 |
| EX-99.1_2026-08-05_a06302026ex991pressrelease.htm.jsonl | 21077052c215c76afaa6a29e3ea89e20e01ee6140be558608fa94290eaa87b1f |
| EX-99.1_2026-11-02_a09302026ex991pressrelease.htm.jsonl | 649e9df09c58fc28e42170873dd9e204e4698e7b6a16ba8868ab909251dcc271 |
| context | 630c8480b8c6896f51051152fc8ca75c81e04a78fc5ea8aebca9a62a14a6fd8f |

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | f373f490427bdb136b51b89f68fd080fb20b9ef4328505ea7636662606abf930 |
| CP-1 | 553419305d3d0840e45db8a53a4ea08f11150ae95be0ecddbcfd829bc1c4363f |
| CP-1A | 61a5beb986ccdfab9790deef0d84544f4320e760e0bdde73d67cc33d45dcc986 |
| CP-2 | b770d9dca1a6706c0ecd8eda37b4dbf8e9f86a42afdd512c6615cd7c14f98828 |

Locators are `page:N` chunks of the pinned `.jsonl` files, not printed pages. "Q3 release" is the November 2, 2026 release; "10-Q Q3" is the September 30, 2026 Form 10-Q.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial and business facts trace to the filings and every recomputed figure matched. The credit view cannot be traced past the Transocean closing because the combination terms and covenant levels are not in the sources. | Medium | The same author wrote and checked every module, and five minor defects remain open. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 29 statement tie-outs and all 65 recomputed figures matched the filings. | Leverage, liquidity and cash flow figures can be relied on as reported. | High |
| All 63 checked quotations appear in the filings; 4 of 59 with page locators cite the wrong page. | A reader may need to look one page away; no conclusion changes. | High |
| Combination terms, the treatment of the notes, and covenant headroom are correctly marked as not supplied. | The post-closing credit view is not traceable and stays open. | High |
| One claim about backlog concentration in the credit synthesis has no source. | The wording overstates; the revenue concentration claim is supported. | Medium |

### Evidence trace view

The run is traceable enough for a standalone view of Valaris, and not for the question that matters most, the credit after the Transocean combination closes. Every figure in the financial base view reproduces from the filings, every checked quotation is in the sources, and the business and credit syntheses use only those figures plus two flagged source checks. Of twelve material claims, six are directly sourced, three are calculated, one is analyst inference and two are Insufficient Information. The critical provenance gap is the Business Combination Agreement: no supplied source says what happens to the notes or the revolver, and the credit synthesis rests its Critical risk and Medium confidence on that silence. Remediation owner: the sourcing step. Five minor defects need no change to any conclusion.

| Traceability summary | Result |
| --- | --- |
| Quotations checked against the sources | 63 found verbatim; 59 with page locators, of which 55 on the cited page and 4 on a neighbouring page |
| Statement tie-outs re-added | 29 of 29 equal |
| Derived figures recomputed (financial base view and credit synthesis) | 65 of 65 equal |
| Credit synthesis figures found upstream | All but two, which it flags as source checks |
| Material claims by lineage | 6 Directly Sourced, 3 Calculated, 1 Analyst Inference, 2 Insufficient Information |
| Open findings | 5 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_val-20251231.htm.jsonl | High: filed, audited annual report (KPMG LLP) | Years ended December 31, 2025, 2024 and 2023 | Valaris Limited and subsidiaries, consolidated | Statements, debt note, cash interest and tax paid, ARO notes, combination agreement summary, risk factors | Text extraction of the filed HTML | CP-0, CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_val-20260331.htm.jsonl | High: filed, unaudited interim report | Quarter ended March 31, 2026 | Same | Interim statements, revolver and letter of credit text | Text extraction; unaudited | CP-0, CP-1 |
| S3 | 10-Q_2026-06-30_val-20260630.htm.jsonl | High: filed, unaudited interim report | Quarter ended June 30, 2026 | Same | Interim statements, revolver and letter of credit text | Text extraction; unaudited | CP-0, CP-1 |
| S4 | 10-Q_2026-09-30_val-20260930.htm.jsonl | High: filed, unaudited interim report | Quarter and nine months ended September 30, 2026 | Same | Statements, debt, liquidity, ARO, fleet, backlog, combination status | Text extraction; unaudited | All modules |
| S5 | EX-99.1_2026-05-04_a03312026ex991pressrelease.htm.jsonl | Medium: issuer press release | Q1 2026 and four prior quarters | Same | Five-quarter statements, Adjusted EBITDA | Management-prepared; non-GAAP | CP-1 |
| S6 | EX-99.1_2026-08-05_a06302026ex991pressrelease.htm.jsonl | Medium: issuer press release | Q2 2026 and four prior quarters | Same | Five-quarter statements, Adjusted EBITDA | Management-prepared; non-GAAP | CP-1 |
| S7 | EX-99.1_2026-11-02_a09302026ex991pressrelease.htm.jsonl | Medium: issuer press release | Q3 2026 and four prior quarters | Same | Five-quarter statements, Adjusted EBITDA, backlog, segments, commentary | Management-prepared; non-GAAP | All modules |
| S8 | context | User settings, not evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency | Not issuer evidence; blank fields are not zero | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Pending Transocean combination with undisclosed treatment of the notes and revolver | CP-1A, CP-2 | Agreement terms, ratio, conditions, dates, termination fee | Can change leverage, ranking, covenants and control | Sets the post-closing credit view | S4 page:11, page:12; S1 page:22, page:24, page:127 | Agreement and Transocean financials not supplied |
| 2 | Liquidity of 900.1 and no principal before 2030 | CP-1, CP-2 | Cash 525.1, undrawn revolver 375.0, one note series | Sets near-term default and refinancing risk | Monitoring horizon | S4 page:9, page:21, page:22, page:51 | Cash after September 30, 2026 not supplied |
| 3 | Leverage 2.68x gross and 1.40x net on a last-twelve-months basis | CP-1, CP-2 | Principal 1,100.0 over Adjusted EBITDA 410.8 | Core leverage metric, higher than FY2025 | Leverage tolerance | S5, S6, S7 Adjusted EBITDA rows; S4 page:21 | Company-defined EBITDA |
| 4 | Capital expenditure above operating cash flow | CP-1, CP-2 | Free cash flow -206.8 last twelve months | Cash is falling while upgrades proceed | Liquidity trend | S1 page:107; S4 page:10, page:52; S7 page:10 | Guidance is management's |
| 5 | Covenant headroom | CP-1, CP-2 | Three tests named, no levels | Revolver availability under stress | Cannot be sized | S1 page:129 | Credit agreement not supplied |
| 6 | ARO funding and notes receivable | CP-1A, CP-2 | Commitment up to about 1.1 billion; notes receivable 363.4 | Contingent call on cash | Liquidity risk outside debt | S4 page:17, page:54, page:55, page:56 | ARO statements not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Liquidity 900.1 | CP-1, CP-2 | S4 page:9, page:22, page:26, page:51 | Yes | High | Calculated | Supported | High | Recomputed equal |
| One note series, no principal before 2030 | CP-1 | S4 page:21, page:51; S1 page:91, page:127 | Yes | High | Directly Sourced | Supported | High | Traced |
| Leverage 1.71x to 2.68x gross, 0.78x to 1.40x net | CP-1, CP-2 | S5, S6, S7 Adjusted EBITDA rows; S1 page:106; S4 page:9 | Yes | High inputs, company-defined EBITDA | Calculated | Supported | High | Recomputed equal |
| Free cash flow -206.8 last twelve months | CP-1, CP-2 | S7 page:10; S4 page:10 | Yes | High | Calculated | Supported | High | Recomputed equal |
| Combination terms: ratio, conditions, fee, dates | CP-1A | S4 page:11, page:12; S1 page:8, page:22 | Yes | High | Directly Sourced | Supported | High | Traced |
| Effect of the combination on the notes and revolver | CP-1A, CP-2 | No source in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Covenant headroom | CP-1, CP-2 | Levels not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| ARO notes receivable, funding commitment, ARO cash | CP-1A, CP-2 | S4 page:17, page:54, page:55, page:56 | Yes | High | Directly Sourced | Supported | High | Traced |
| Backlog 4,750.1 and customer revenue concentration | CP-1A, CP-2 | S4 page:35; S1 page:11, page:153 | Yes | High; backlog is a management measure | Directly Sourced | Supported for revenue concentration; backlog by customer not supplied | Medium | Traced with one wording defect (QA-5) |
| Middle East impact of about 62.0 for nine months | CP-1A, CP-2 | S4 page:34 | Yes | High | Directly Sourced | Supported | High | Traced |
| Backlog and Adjusted EBITDA available only from the releases | CP-0, CP-1 | S4 page:35; S1 page:76 | Yes | High | Directly Sourced | Not supported as worded for backlog | Medium | Contradicted by the 10-Q and 10-K (QA-4) |
| Overall standalone credit view: moderate risk, Medium confidence | CP-2 | CP-1 and CP-1A rows | Yes | Medium | Analyst Inference | Supported by cited basis | Medium | Traced |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Revenues FY2025 2,207.9; operating income 477.0 | runs/cpos-swarm-20261105-val/source-text | 10-K_2025-12-31_val-20251231.htm.jsonl | S1 | page:105, page:106 statements of operations | CP-1 financials table | Reported | High | Matches; equals nine months 2025 plus Q4 2025 |
| Cash 525.1; long-term debt 1,088.5 at September 30, 2026 | runs/cpos-swarm-20261105-val/source-text | 10-Q_2026-09-30_val-20260930.htm.jsonl | S4 | page:9 balance sheet | CP-1 liquidity chart, financials table | Reported | High | Matches |
| 8.375% notes, April 30, 2030; revolver 375.0 to April 3, 2028 | runs/cpos-swarm-20261105-val/source-text | 10-Q_2026-09-30_val-20260930.htm.jsonl | S4 | page:21, Note 8 | CP-1 debt table | Reported | High | Matches; revolver pricing matches 10-K page:129 |
| Adjusted EBITDA quarterly 181.3, 200.7, 163.2, 97.0, 66.7, 96.5, 150.6 | runs/cpos-swarm-20261105-val/source-text | EX-99.1 releases of May 4, August 5 and November 2, 2026 | S5, S6, S7 | page:10 or page:11, operating statistics | CP-1 calculations item 1 | Issuer non-GAAP | Medium | Overlapping quarters agree across the three releases |
| Cash interest paid FY2025 90.5 | runs/cpos-swarm-20261105-val/source-text | 10-K_2025-12-31_val-20251231.htm.jsonl | S1 | page:153 | CP-1 interest cover | Reported | High | Matches |
| Letters of credit and surety bonds 113.7, none under the revolver | runs/cpos-swarm-20261105-val/source-text | 10-Q_2026-09-30_val-20260930.htm.jsonl | S4 | page:26, page:55 | CP-1 liquidity | Reported | High | Matches |
| Exchange ratio 15.235; 53% and 47%; fee 173.0 | runs/cpos-swarm-20261105-val/source-text | 10-Q_2026-09-30_val-20260930.htm.jsonl | S4 | page:11, page:12 | CP-1A transaction summary | Reported | High | Matches 10-K page:8 and page:22 |
| Notes receivable from ARO principal 400.7, carrying 363.4 | runs/cpos-swarm-20261105-val/source-text | 10-Q_2026-09-30_val-20260930.htm.jsonl | S4 | page:17 | CP-1 claims outside debt; CP-1A ARO table | Reported | High | Matches |
| Fleet of 41 rigs: 13 floaters, 21 jackups, 7 leased to ARO | runs/cpos-swarm-20261105-val/source-text | 10-Q_2026-09-30_val-20260930.htm.jsonl | S4 | page:28, page:42 | CP-1A operating model | Reported | High | Totals add |
| Three financial covenants named without levels | runs/cpos-swarm-20261105-val/source-text | 10-K_2025-12-31_val-20251231.htm.jsonl | S1 | page:129 | CP-1 covenants | Reported description | High | Matches; no level in any source |
| Backlog 4,750.1 at November 2, 2026 | runs/cpos-swarm-20261105-val/source-text | 10-Q_2026-09-30_val-20260930.htm.jsonl | S4 | page:35 | CP-1A operating model | Management measure | Medium | Matches release page:11 |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Quarterly and last-twelve-months Adjusted EBITDA | CP-1 calculations 1 to 4; CP-2 | Seven quarterly values from three releases | Sum of four quarters | Recomputed from parsed release rows: 642.2, 527.6, 423.4, 410.8 equal | Supported | High | Basis of leverage and cover | S5, S6, S7 |
| Adjusted EBITDA recomputed from reported lines | CP-1 calculations 5 | Operating income, depreciation, merger costs, other operating loss, ARO equity result | Operating income + depreciation + merger costs + other operating loss - equity in ARO | Equal for Q3 2026, nine months 2026, FY2025 and last twelve months | Supported | High | Confirms the company definition | S7 page:8; S4 page:8; S1 page:105, page:106 |
| Leverage, net debt | CP-1 chart data; CP-2 | Principal 1,100.0; cash at four dates | Principal / EBITDA; (principal - cash) / EBITDA | Recomputed: 1.71, 2.09, 2.60, 2.68 and 0.78, 0.99, 1.32, 1.40 equal | Supported | High | Leverage tolerance | S4 page:9, page:21; S7 page:8 |
| Interest cover | CP-1 chart data | FY2025 EBITDA 642.2; cash interest 90.5; accrual interest 98.8 and 98.0 | EBITDA / interest | Recomputed: 7.10, 6.50, 4.19 equal | Supported | High | Debt service | S1 page:106, page:153; S7 page:8 |
| Last-twelve-months sums | CP-1 financials table | Q4 2025 plus nine months 2026 | Sum | Recomputed from parsed release rows: 1,990.2; 2,135.6; 191.8; 175.2; 98.0; 68.3; 792.5; 227.5; 434.3; 104.2 equal | Supported | High | Basis of ratios | S7 page:8, page:9, page:10 |
| Free cash flow | CP-1; CP-2 | Operating cash flow and capital expenditure | Operating cash flow - capital expenditure | 202.7, -172.7, -54.4, -206.8 equal | Supported | High | Cash generation | S1 page:107; S4 page:10; S7 page:10 |
| Q4 2026 cash outlay | CP-2 calculation 1 | Guidance 445.0 to 470.0, spend 328.0, coupon 46.1, cash 525.1, revolver 375.0 | Guidance - spend + coupon; cash - outlay; + revolver | Recomputed: 163.1 to 188.1, 362.0 to 337.0, 737.0 to 712.0 equal; indicative, excludes operating inflows | Supported with caveat | Medium | Stress on liquidity | S4 page:52, page:21 |
| Equity to total assets and deferred tax share | CP-2 calculation 6 | 3,271.0 / 5,482.5; 3,169.6 / 5,304.8; 1,298.9 / 5,482.5 | Ratio | Recomputed: 59.7%, 59.7%, 23.7% equal; not in upstream figures | Supported with caveat | Medium | Covenant context | S4 page:9; S1 page:106 |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | Reclassification of prior amounts (CP-0, CP-1) | The quotation "Certain previously reported amounts have been reclassified to conform to the current year presentation" is cited to 10-Q Q3 page:11 and is on page:12 | Wrong page locator | A reader checking page:11 does not find it | Cite page:12 | CP-0 and CP-1 handoffs |
| MINOR | Cover-text quotations (CP-0) | The quotations "For the quarterly period ended March 31, 2026" and "For the quarterly period ended June 30, 2026" sit in lists that cite statement pages; the text is on page:1 of each 10-Q | Imprecise locator | Slower verification; no misquotation | Cite page:1 | CP-0 handoff |
| MINOR | Exact figures with rounded or neighbouring page locators (CP-1, CP-1A) | The Q3 versus Q2 bullet cites release page:2 and page:8 for Adjusted EBITDA 150.6 and 96.5, tax expense 54.7 and cash 541.2 and 525.1: page:2 prints rounded figures and the exact ones are on page:4, page:8 and page:11. The revolver commitment 375.0 is cited to 10-Q Q3 page:22 and 10-K page:129 and page:146 but is on page:21 and page:128. Drillship average daily revenue 469,000 is cited to release page:12 and is on page:11 | Imprecise locator | Slower verification; values agree | Cite the page that prints the exact figure | CP-1 and CP-1A handoffs |
| MINOR | Source of backlog (CP-0, CP-1) | CP-0 says the release alone supplies backlog; CP-1 says Adjusted EBITDA and backlog appear only in the releases. Backlog is also printed in 10-Q Q3 page:35 and 10-K page:76, which CP-1A cites | Cross-module inconsistency | Understates the filed support for backlog; backlog stays a management measure | Say backlog is in the 10-Q and 10-K as well as the releases | CP-0 and CP-1 handoffs |
| MINOR | Backlog concentration (CP-2) | A key finding says backlog was "concentrated in a few customers"; no source gives backlog by customer. Revenue concentration is sourced: the five largest customers were 49% of FY2025 revenues | Unsupported wording | Overstates what the backlog evidence shows | Say revenue, not backlog, is concentrated | CP-2 handoff |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves by cover text and dates; releases agree with the 10-Qs | A wrong document would shift every figure | None found | None |
| Locator precision | Adequate | 55 of 59 page-located quotations on the cited page; several exact figures cited to a neighbouring page | Slower checks; risk of a misplaced citation | None on conclusions | Exact page locators |
| Calculation reproducibility | Strong | 65 of 65 derived figures and 29 of 29 tie-outs recomputed equal | Calculation errors would move leverage | None found | None |
| Cross-module consistency | Strong with one exception | Credit synthesis figures found in the financial base view or business context, except two flagged source checks; backlog source statement differs between modules | Inconsistent statements mislead a committee | None on conclusions | Correct the backlog source statement |
| Reviewer independence | Weak | The host wrote and checked all four handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Treatment of the notes, revolver and change-of-control provision in the Transocean combination | Business Combination Agreement, scheme document, Transocean filings | Post-closing leverage, ranking and covenants unknown | Credit synthesis Critical risk and Medium confidence | Holds the view to the standalone structure | Business Combination Agreement and Transocean filings |
| G2 | Covenant levels, definitions and reported figures | 2028 Credit Agreement and compliance disclosures | Revolver availability under stress cannot be tested | Covenant risk row | Compliance rests on a management statement | Credit agreement and amendments |
| G3 | Events and cash after September 30, 2026 | Later 8-Ks and filings | Cash after the October 30, 2026 coupon and the combination status at the as-of date are unknown | Liquidity and monitoring posture | Lowers currency of the view | EDGAR filings to the cutoff date |
| G4 | ARO standalone statements | ARO financial statements and debt documents | ARO exposure described from Valaris disclosure only | ARO exposure rows | Moderate | ARO statements |
| G5 | Cash interest paid for 2026 | Cash flow disclosure for 2026 | Cash interest cover on a last-twelve-months basis not available | Interest cover chart | Accrual basis used and labelled | Next annual report |
| G6 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / val-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted first attempt | Passed with three MINOR findings | READY_WITH_LIMITATIONS for all consumers |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, last twelve months, debt, liquidity, covenants | High | Six headings; accepted first attempt | Passed with three MINOR findings | All recomputed figures equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, combination, ARO, governance | High | Six headings; accepted first attempt | Passed with one MINOR finding | Differences between sources logged, not reconciled |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted first attempt | Passed with one MINOR finding | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1 | Reclassification quotation | Supported | Cited to page:11, located on page:12 | Cite page:12 | None |
| MINOR | CP-0 | Cover-text quotations | Supported | Located on page:1, cited with statement pages | Cite page:1 | None |
| MINOR | CP-1, CP-1A | Exact figures with neighbouring or rounded locators | Supported | Page cited does not print the exact figure | Cite the printing page | None |
| MINOR | CP-2 | Backlog concentration wording | Partly supported | No source gives backlog by customer | Reword to revenue concentration | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Observation, no defect | CP-1, CP-2 | Leverage on principal 1,100.0 rather than carrying value 1,088.5 | Both bases disclosed; carrying value gives 2.65x at Q3 2026 | None | None | None |
| Observation, no defect | CP-1 | Adjusted EBITDA is company-defined and excludes the ARO equity result and merger costs | Definition quoted; recomputation from reported lines equals the issuer figure in four periods | None | Keep the label as issuer measure, as CP-1 does | None |
| Observation, no defect | CP-1 | Interest cover on cash interest for FY2025 only | 2026 cash interest paid is not printed; accrual cover shown separately and labelled | None | None | None |
| Observation, no defect | CP-2 | Indicative Q4 2026 outlay excludes operating inflows | Stated as indicative and not a forecast | None | None | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Gap, not a defect | CP-1A, CP-2 | Effect of the combination on the notes, revolver and change-of-control offer | Business Combination Agreement, Indenture, 2028 Credit Agreement | Documents not supplied; claims correctly marked as not supplied | Supply documents | Required before any post-closing view |
| Gap, not a defect | CP-1, CP-2 | Covenant tests and compliance | 2028 Credit Agreement | Levels not printed; compliance is a management statement | Supply the agreement | Required for headroom |
| Observation, no defect | CP-1 | Guarantor and collateral description | Executed Indenture and credit agreement | Described from filing summaries and flagged as such | None for this scope | Required for legal work |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Observation, no defect | CP-2 | Notes fair value above principal does not point to market stress | Independent price data and ratings | The claim rests on the filing's Level 1 fair value of 1,125.2 against principal 1,100.0, not on market data in the context | Add sourced prices only if relative value is needed | Committee cannot judge value from this run; no relative-value claim is made |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1 against CP-1A | Backlog is described as available only from the releases, while CP-1A cites it from the 10-Q and 10-K | CP-1A cites current CP-1 hash 553419305d3d | Align the statement | None on figures |
| Observation, no defect | CP-1A, CP-2 | Figures repeated from CP-1 match exactly (for example 4,750.1, 1,100.0, 900.1, 2.68x) | CP-2 cites CP-1A hash 61a5beb986cc and CP-1 hash 553419305d3d | None | None |
| Observation, no defect | CP-1, CP-1A | The VALARIS 111 purpose differs between the Q3 release and the 10-Q; both modules quote both and choose neither | None | None | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Readiness limit | Run | Committee readiness | The standalone view is traceable; the post-combination view is not; review is a self-review | Supply the combination documents and an independent review | Committee status Requires More Work |
| Observation, no defect | CP-1, CP-0 | Duplication | Releases repeat 10-Q statement figures; CP-0 and CP-1 treat the 10-Q as controlling and do not count releases as corroboration | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Observation, no defect | CP-0, CP-1, CP-1A, CP-2 | Required headings, Reader summary, view heading and report selectors | None found; all four were accepted on the first attempt | None | None |
| Observation, no defect | CP-1 | Chart data tables | Four chart tables and one financials table each carry a basis and limitation; unsupplied cells state a reason | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-0, CP-1 | Locator | Reclassification quotation cited to page:11, on page:12 | Cite page:12 | None | Open |
| QA-2 | MINOR | CP-0 | Locator | Cover-text quotations cited with statement pages, on page:1 | Cite page:1 | None | Open |
| QA-3 | MINOR | CP-1, CP-1A | Locator | Exact figures cited to pages that print rounded or different values | Cite the printing page | None | Open |
| QA-4 | MINOR | CP-0, CP-1 | Cross-module inconsistency | Backlog said to appear only in releases; also in 10-Q page:35 and 10-K page:76 | Align the statement | None | Open |
| QA-5 | MINOR | CP-2 | Unsupported wording | Backlog described as concentrated in a few customers | Reword to revenue concentration | None | Open |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each double-quoted phrase of 12 or more characters in the four handoffs searched in the normalized text of all seven sources; where the same line cites pages, searched on those pages | 69 spans parsed, of which 6 are search terms, parser artifacts or a context label; of 63 quotations all are found verbatim, 59 carry page locators, 55 are on the cited page and 4 are not |
| Q2 | Adjusted EBITDA recomputation | Quarterly values parsed from the Adjusted EBITDA row of each release; fiscal year and last-twelve-months sums | 642.2, 527.6, 423.4 and 410.8, equal to CP-1; overlapping quarters agree across the three releases |
| Q3 | Last-twelve-months sums | Q4 2025 plus nine months 2026, and four-quarter sums, parsed from the Q3 release page:8 to page:10 | 10 of 10 equal to CP-1 (share repurchases of 25.0 read from the Q4 2025 column) |
| Q4 | Tie-outs | Nine months 2026 against the sum of three quarters (10 lines); FY2025 against nine months 2025 plus Q4 2025 (10 lines); balance sheet totals and note principal (3); Adjusted EBITDA bridges (4); segment Adjusted EBITDA to consolidated (2) | 29 of 29 equal |
| Q5 | Derived figures | Net debt, leverage, cover, free cash flow, liquidity, sensitivities, leases and coupon in CP-1, and the outlay, EBITDA less capital expenditure, fair value and ratio calculations in CP-2, recomputed from their cited inputs | 65 of 65 equal |
| Q6 | Cross-module figure identity | Every number in the CP-2 findings searched in CP-0, CP-1 and CP-1A | All found except 1,298.9 (flagged by CP-2 as a source check) |
| Q7 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:6,Calculated:3,Analyst Inference:1,Insufficient Information:2" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:5` | score = clamp((0.6 x 75.83 + 0.4 x 100) x 0.7 - 15) = 44.85, rounded to 45; band Low; qa_status Passed |

## Gaps

- G1, Critical for the decision: the Business Combination Agreement is not supplied, so the treatment of the notes, the revolver and the change-of-control offer after the Transocean closing is unknown. The credit synthesis relies on this gap for its Critical risk and its Medium confidence.
- G2: covenant levels and definitions are not supplied, so headroom is Not calculable.
- G3: events and cash after September 30, 2026 are not supplied, including whether the October 30, 2026 coupon was paid.
- G4: ARO standalone statements are not supplied.
- G5: cash interest paid for 2026 is not supplied; accrual cover is labelled as a different basis.
- G6: no independent review; this CP-5 was written by the same host that wrote the four handoffs.

## Next module

- Report delivery: carry `qa_status` Passed, Confidence Score 45 (Low), committee status Requires More Work, and gap G1.
- Swarm review step: an independent agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: obtain the Business Combination Agreement, the scheme document and Transocean's filings, plus any filings after November 3, 2026, then rerun CP-1A, CP-2 and CP-5 in a new run folder.
