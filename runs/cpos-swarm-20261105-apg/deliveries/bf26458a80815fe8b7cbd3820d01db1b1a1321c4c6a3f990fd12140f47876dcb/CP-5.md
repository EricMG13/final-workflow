## Request

This is the evidence trace validation and research integrity grade for APi Group Corp (APG, issuer id apg) as of 2026-11-05, pathway credit_snapshot, current period Q3 2026 against FY2025, USD. Scope: Top 5 material credit drivers of the accepted CP-0, CP-1, CP-1A and CP-2 handoffs, traced to the seven pinned sources and checked for arithmetic, citation support, cross-module consistency and handoff integrity. This module changes no upstream conclusion and repairs nothing silently; the earlier handoffs are not edited, and corrections are stated here.

## Sources

### Issuer sources traced

| Source ID | Source (exact name) | sha256 |
| --- | --- | --- |
| S1 | 10-K_2025-12-31_apg-20251231.htm.jsonl | 85e734a169388fec4ab633a5bed87c9c814f23738d0e6cf5a912dd14edbbba4e |
| S2 | 10-Q_2026-03-31_apg-20260331.htm.jsonl | 4f2797670271476a95f9547a3540ae303edaa5e40f3e3f08829817127f41c878 |
| S3 | 10-Q_2026-06-30_apg-20260630.htm.jsonl | e90d6bf8c69051d7d18a0cfac2ae57b46434273469a8084102121b4455760a9f |
| S4 | 10-Q_2026-09-30_apg-20260930.htm.jsonl | 0f3c88ef7de625d84cef8d9062b4481840371b9e18740b974653c45bd1fc951f |
| S5 | EX-99.1_2026-04-30_apg-20260331xexx991.htm.jsonl | 1e2bb7155c93f1d7180c8420214b4e920240b52127bf64099c673d664920aca5 |
| S6 | EX-99.1_2026-07-30_apg-20260630xexx991.htm.jsonl | f112ae35c8090bbb1d28641903d8fabef87924332451d391abea2504360e0996 |
| S7 | EX-99.1_2026-10-29_apg-20260930xexx991.htm.jsonl | f776b9079a3057680b637f70cfc8304a121c49085a5098404f23ccab4852f2c3 |

### Handoffs supplied (all four opened and traced)

| Module | sha256 |
| --- | --- |
| CP-0 | d40ba3564c8793d91987b4dca76c3187df72cdc74c99584f6e488aad8f306a91 |
| CP-1 | f7db30806e7a98570fba7e4bc97f39d6f69658956a05590382766f0c4cdbcca8 |
| CP-1A | 49e3ff078b6908f3efb88a445708e93fc6e79232aec6b0d708d47eaa20df5368 |
| CP-2 | a2568d2b55f4d342a50cf09a2a91861829812b774ff26d6d56599a5a14683189 |

The run context (sha256 5361f531841cad8936701ac126679da0830e0b3a545fa6b1b9ab2f313f6dfc9d) holds dated settings only and is not issuer evidence. No external sources were used by this module.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The upstream analysis is largely traceable: key figures recompute from the filings, with no arithmetic errors found. Committee use is restricted because covenant and guarantor claims rest on filing summaries and one source conflict on 2025 acquisition consideration remains open. | Medium | Executed financing documents are not supplied, and no original-HTML check was possible, so covenant, guarantor and note-issuer claims cannot be traced beyond filing text. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Leverage, liquidity, interest cover and cash-flow figures were recomputed independently from the filings and match, including last-twelve-months adjusted EBITDA of 1,191 and total debt over EBITDA of 3.02x. | The core leverage and liquidity conclusions are reliable as arithmetic; remaining doubt is definitional, not numerical. | High |
| The springing covenant trigger (33.5% revolver usage against 30%) is inferred from summarised wording, and the covenant EBITDA is not in the sources. | Reported headroom cannot be independently confirmed, so covenant statements stay at filing-summary strength. | Medium |
| Filings give three totals for 2025 acquisition consideration (233, 235 and 225 million) with no explanation, and earlier modules log but do not resolve it. | Acquisition spend and accrued consideration should be cited by filing and date until resolved. | Medium |
| The credit synthesis says debt maturities begin in 2029, while the balance sheet shows 361 million of short-term and current debt at September 30, 2026. | Refinancing wording should note the revolver's short-term classification and term loan instalments, though contractual maturities remain 2029 or later. | Medium |
| One credit synthesis figure, the 34 million prior-year quarterly interest expense, is source-supported but not carried in any earlier handoff. | A minor lineage break; the figure is correct against the third quarter report. | High |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 1 is calculated, 0 are assumption-based, 1 is an analyst inference, and 1 is a weak-lineage, untraced, conflicting, or insufficient-information item. The most important provenance gap is the absence of the executed Credit Agreement and indentures, which matters because the covenant trigger, covenant EBITDA and guarantor scope rest on filing summaries and imply that committee use should be restricted until they are supplied. Figures in the upstream handoffs recompute from the cited filings; the defects found are wording, lineage and open-conflict items, not arithmetic errors.

### Traceability summary

| Item | Result |
| --- | --- |
| Committee status | Restricted |
| QA status | Restricted (3 Material, 5 Minor, 0 Critical open issues) |
| Confidence band | Low, capped by the Restricted status; the numeric score is Not calculable here because the scoring script is not available in this transport |
| Arithmetic recomputed | All upstream derived figures checked; no error |
| Orphan claims | None; each weakly traced claim carries a stated limitation |

### Top 5 material credit drivers (T5B.2)

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage increase from debt-funded acquisitions and buybacks | CP-1 | Total debt obligations 3,601 and cash 373 at September 30, 2026; derived last-twelve-months adjusted EBITDA 1,191 | Debt rose faster than trailing earnings, so cushion against a shock shrank | Drives leverage tolerance and monitoring posture | S4 pages 2, 23; S1 page 68; S7 page 11 | LTM is derived; no pro forma for acquired EBITDA; adjusted EBITDA is management-defined |
| 2 | Liquidity of 1,032 at September 30, 2026 | CP-1 | Cash 373 plus revolver availability 659 | Revolver is the buffer for seasonal cash flow and acquisitions | Drives debt-service and refinancing view | S4 pages 2, 24, 56 | Subsequent 100 revolver draw and about 143 repurchases not netted in the September 30 figure |
| 3 | Springing first lien covenant status and headroom | CP-1 | Reported ratio 1.6:1.0 against 3.75 to 1.00; revolver usage 335 of 1,000 | Test applies only above 30% usage, and usage is above that on the filing wording | Drives covenant headroom and default-risk view | S4 pages 24, 60 | Credit Agreement and covenant EBITDA definition not supplied |
| 4 | Acquisition programme and its funding | CP-1A | CertaSite, Onyx-Fire and WTech closed for 271, 532 and 394; 500 senior notes issued May 14, 2026 | Debt-funded growth precedes earnings contribution | Drives leverage path and integration risk | S4 pages 8, 9, 25, 60; S2 page 30 | Provisional purchase accounting; 2025 consideration totals conflict |
| 5 | Revenue durability and diversification | CP-1A | No customer above 5% of FY2025 net revenues; remaining performance obligations 4,863 | Determines stability of cash flow behind debt service | Drives business-risk view | S1 pages 14, 107; S4 page 12 | Recurring revenue share not disclosed in any source |

### Traceability map (T5B.3)

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 3.02x total and 2.71x net on last-twelve-months adjusted EBITDA | CP-1 | Debt and cash printed in S4; adjusted EBITDA printed in S1 and S7; LTM built from them | Yes | High (filed statements) with management-defined EBITDA | Calculated | Supported | Medium | Committee-Ready |
| Liquidity of 1,032 | CP-1 | S4 page 56 states the figure | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Covenant trigger exceeded and headroom 2.15x | CP-1, CP-2 | Ratio and threshold wording in S4 page 60; usage computed from S4 page 24 | Partial | Medium (summary of unseen agreement) | Analyst Inference | Partly supported | Low | Remediation Needed |
| Named acquisitions total 1,197 and 500 note issue | CP-1A | S4 pages 8 and 60 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| 2025 acquisition consideration | CP-1A | S1 page 99 (233), S2 page 8 (235), S3 page 9 and S4 page 9 (225) | Yes | High but conflicting | Conflicting | Open conflict | Low | Remediation Needed |
| Revenue durability supported by diversification and inspection demand | CP-1A, CP-2 | Concentration in S1 page 14; durability is management language; recurring share absent | Partial | Medium | Insufficient Information | Partly supported | Low | Remediation Needed |
| Debt maturities start in 2029 | CP-2 | S4 page 22 maturity dates; S4 page 2 short-term and current debt 361 | Partial | High | Analyst Inference | Partly supported | Medium | Remediation Needed |
| Cash interest cover 9.23x flatters run-rate | CP-1, CP-2 | LTM cash interest 129 built from S1 page 88 and S4 page 5; Q3 interest expense 45 from S4 page 3 | Yes | High | Calculated | Supported (mechanism inferred) | Medium | Remediation Needed |

### Source lineage register (T5B.4)

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Liquidity of USD 1,032 million | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:56 Liquidity and Capital Resources | CP-1 Covenant, liquidity and refinancing position | Sourced | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:56: "$1,032 million of total liquidity") |
| Revolver 335 drawn; 659 available after 6 letters of credit | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:24 Note 10 | CP-1 liquidity table | Sourced | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:24: "the Company had $335 and $0 outstanding under the Revolving Credit Facility") |
| First lien net leverage ratio 1.6:1.0 | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:60 MD&A | CP-1 covenant section | Sourced | Medium | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:60: "Our first lien net leverage ratio as of September 30, 2026 was 1.6:1.0") |
| 30% usage trigger and 60 letter of credit exclusion | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:60 MD&A | CP-1 covenant section | Sourced | Medium | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:60: "excluding undrawn letters of credit up to $60 million") |
| Total debt obligations 3,601 | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:23 Note 10 | CP-1 leverage table | Sourced | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:23: "Total debt obligations 3,601 2,776") |
| Cash and cash equivalents 373 | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:2 balance sheet | CP-1 leverage table | Sourced | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:2: "Cash and cash equivalents $ 373 $ 912") |
| Adjusted EBITDA FY2025 1,041 | source-text | 10-K_2025-12-31_apg-20251231.htm.jsonl | S1 | page:68 MD&A reconciliation | CP-1 financials table | Sourced | Medium (non-GAAP) | (10-K_2025-12-31_apg-20251231.htm.jsonl page:68: "Adjusted EBITDA $ 1,041 $ 893") |
| Adjusted EBITDA nine months 2026 896 and 2025 746 | source-text | EX-99.1_2026-10-29_apg-20260930xexx991.htm.jsonl | S7 | page:11 reconciliation | CP-1 financials table | Sourced | Medium (management release) | (EX-99.1_2026-10-29_apg-20260930xexx991.htm.jsonl page:11: "Adjusted EBITDA $ 350 $ 281 $ 896 $ 746") |
| 5.750% Senior Notes issued May 14, 2026 | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:60 MD&A | CP-1A transaction summary | Sourced | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:60: "On May 14, 2026, APi Group DE completed a private offering of $500 million aggregate principal amount of 5.750% Senior Notes due 2034") |
| CertaSite, Onyx-Fire and WTech closing dates and consideration | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:8 Note 3 | CP-1A transaction summary | Sourced | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:8: "Consideration transferred of $532 for Onyx-Fire") |
| No customer above 5% of net revenues | source-text | 10-K_2025-12-31_apg-20251231.htm.jsonl | S1 | page:14 Item 1 | CP-1A company profile | Sourced | High | (10-K_2025-12-31_apg-20251231.htm.jsonl page:14: "no single customer accounting for more than 5% of our total net revenues for 2025") |
| Remaining performance obligations 4,863 | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:12 Note 5 | CP-1A operating model | Sourced | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:12: "was $4,863") |
| 2025 acquisition consideration 233 | source-text | 10-K_2025-12-31_apg-20251231.htm.jsonl | S1 | page:99 Note 4 | CP-1A conflicts | Conflicting | High | (10-K_2025-12-31_apg-20251231.htm.jsonl page:99: "completed 14 acquisitions for total net consideration transferred of $233") |
| 2025 acquisition consideration 225 | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:9 Note 3 | CP-1A conflicts | Conflicting | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:9: "completed 14 acquisitions for total net consideration transferred of $225") |
| Prior-year third-quarter interest expense, net, 34 | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:3 statement of operations | CP-2 key findings | Sourced (no upstream carrier) | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:3: "Interest expense, net 45 34 111 109") |
| Series A converts into 6,000,000 shares on the last day of 2026 | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:29 Note 15 | CP-1A transaction summary | Sourced (future contract term) | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:29: "will be convertible into 6,000,000 shares of common stock upon conversion on the last day of 2026") |
| Subsequent 100 revolver draw and 143 repurchase (dated after September 30, 2026) | source-text | 10-Q_2026-09-30_apg-20260930.htm.jsonl | S4 | page:24 and page:37 | CP-1, CP-1A | Sourced (subsequent event, kept apart from period figures) | High | (10-Q_2026-09-30_apg-20260930.htm.jsonl page:37: "Subsequent to September 30, 2026, the Company repurchased 3,604,478 shares of common stock for approximately $143 under the 2025 SRP") |

### Calculation and assumption register (T5B.5)

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM adjusted EBITDA 1,191 | CP-1, CP-1A, CP-2 | FY2025 1,041; nine months 2026 896; nine months 2025 746; period FY2025 and nine months | 1,041 + 896 - 746; no normalisation or pro forma | Calculated | Verified | High | Leverage, coverage | S1 p68; S7 p11 |
| Total debt / adjusted EBITDA 3.02x | CP-1, CP-2 | Debt 3,601; LTM adjusted EBITDA 1,191 | 3,601 / 1,191 = 3.024 | Calculated | Verified | Medium (EBITDA basis) | Leverage | S4 p23 |
| Net debt / adjusted EBITDA 2.71x | CP-1, CP-2 | Debt 3,601 less cash 373 = 3,228; EBITDA 1,191 | 3,228 / 1,191 = 2.710 | Calculated | Verified | Medium | Leverage | S4 p2, p23 |
| Adjusted EBITDA / cash interest 9.23x | CP-1, CP-2 | LTM cash interest 129 = 136 + 98 - 105 | 1,191 / 129 = 9.233 | Calculated | Verified | Medium (net of interest income; run-rate not reflected) | Coverage | S1 p88; S4 p5 |
| Liquidity 1,032 and change of 625 | CP-1, CP-2 | 373 + 659; 912 + 745 | 1,032; 1,657; 1,657 - 1,032 = 625 | Calculated | Verified | High | Liquidity | S4 p56; S1 p122 |
| Revolver usage 33.5% against 30% trigger | CP-1, CP-2 | 335 drawn; 1,000 commitments; letters of credit excluded up to 60 | 335 / 1,000 | Calculated on summarised wording | Verified arithmetic; definition unverified | Low | Covenant | S4 p24, p60 |
| Indicative covenant EBITDA about 1,318 | CP-1, CP-2 | (2,147 + 335 - 373) / 1.6, bounds 1.55 and 1.65 | 2,109 / 1.6 = 1,318 | Assumption-Based (assumes first lien debt is term loan plus revolver and full cash netting) | Labelled inference upstream | Low | Covenant headroom | S4 p60 |
| Free cash flow 317 (nine months 2026) | CP-1, CP-2 | Operating cash flow 393 less capex 76 | 393 - 76 | Calculated | Verified; matches the release's printed 317 | High | Cash conversion | S4 p5; S7 p15 |
| Run-rate cover 6.62x | CP-1, CP-2 | LTM adjusted EBITDA 1,191; Q3 2026 interest expense, net, 45 | 1,191 / (45 x 4) | Assumption-Based (simple annualisation) | Labelled indicative upstream | Low | Coverage | S4 p3 |
| Adjusted EBITDA growth 20.1% and revenue growth 17.2% | CP-2 | Nine months 896 and 746; 6,790 and 5,794 | 896 / 746 - 1; 6,790 / 5,794 - 1 | Calculated | Verified | High | Earnings momentum | S4 p3; S7 p11 |

### Missing citation and weak-lineage flags (T5B.6)

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Covenant trigger exceeded; headroom 2.15x | Trigger and ratio taken from MD&A summary; Credit Agreement and covenant EBITDA absent; stated more firmly in the credit synthesis reader summary than in CP-1 | Analyst Inference | Headroom drives default-risk view; a different definition changes the trigger result | Obtain the Credit Agreement; until then label as filing-wording inference | CP-1 covenant section; CP-2 reader summary and key findings |
| Material | 2025 acquisition consideration | Three different totals across filings; not recorded in the readiness handoff | Conflicting | Accrued consideration is a claim outside debt and a sign of purchase accounting movement | Cite by filing and period; seek explanation | CP-1A conflicts; CP-2 key findings |
| Material | Debt maturities start in 2029 | Omits current-portion classification and term loan instalments carried in CP-1 | Analyst Inference | Refinancing and liquidity timing | Restate with the 361 current debt note | CP-2 reader summary, credit view, strengths |
| Minor | Prior-year interest expense 34 | Figure used in CP-2 not carried upstream | Weak Lineage | Breaks upstream-only rule | Carry in CP-1 or cite filing | CP-2 key findings |
| Minor | Revenue durability | Recurring share undisclosed; durability is qualitative | Insufficient Information | Sizing of revenue stability | Add revenue by service type | CP-1A, CP-2 |
| Minor | New notes and revolver "only partly reached cash interest" | Mechanism inferred; coupon dates not in sources | Analyst Inference | Coverage interpretation | Soften to "may not yet" | CP-2 key findings |

Orphan Claim Protocol: no claim is both weakly traced and presented without a limitation, so VE-015 is not triggered.

### Auditability assessment (T5B.7)

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | All seven sources used with page locators; executed financing documents absent | Legal terms cannot be verified | Covenant and guarantor claims stay at summary strength | Add Credit Agreement, amendments, indentures |
| Citation completeness | Ready with Remediation | CP-1 and CP-1A cite exact quotes with page locators; CP-2 cites modules by design; one CP-2 figure lacks an upstream carrier | A figure outside the upstream chain breaks lineage | Minor | Carry or cite the 34 figure |
| Calculation traceability | Committee-Ready | Every derived figure recomputed from printed inputs and matched | None identified | None | None |
| Assumption transparency | Ready with Remediation | Indicative covenant EBITDA, run-rate cover and LTM are labelled | Assumption-based figures could be read as reported | Moderate if unlabelled in committee material | Keep labels in committee extracts |
| Markdown/export artifact integrity | Ready with Remediation | Six H2 headings present in each handoff; no YAML front matter or Evidence Trace headings under this transport | Downstream tools expecting the canonical envelope may not parse | Hygiene | None under this run |

Overall auditability is the lowest of the five: Ready with Remediation.

### Gaps ledger (T5B.8)

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed financing documents absent | Credit Agreement, Ninth Amendment, three indentures | Covenant tests, baskets, security and note issuer cannot be traced | Covenant, guarantor and permitted-payment statements | High impact | Executed documents |
| CP-5-GAP-002 | Covenant EBITDA and letter-of-credit exclusion definition | Definition text | Trigger and headroom cannot be recomputed | Covenant section | High impact | Credit Agreement |
| CP-5-GAP-003 | Guarantor list and issuer of record of notes | Indenture signature pages; exhibit | Structural position and note issuer unresolved | Capital structure statements | Medium impact | Indentures |
| CP-5-GAP-004 | Recurring revenue share | Revenue by service type | Durability cannot be sized | Business-risk view | Medium impact | Segment or investor disclosure |
| CP-5-GAP-005 | Beneficial ownership and control | Proxy statement | Alignment cannot be assessed | Governance view | Medium impact | Proxy statement |
| CP-5-GAP-006 | Explanation for 2025 acquisition consideration changes | Measurement-period explanation | Accrued consideration uncertainty | Acquisition statements | Medium impact | Later filings |
| CP-5-GAP-007 | Maturity schedule and current-debt composition at September 30, 2026 | Debt maturity table; breakdown of 361 | Refinancing timing | Maturity chart | Low impact | Next quarterly report |
| CP-5-GAP-008 | Composition of 795 long-term borrowing proceeds and 310 repayments | Debt roll-forward | Funding sources beyond the 500 notes | Cash flow narrative | Low impact | Debt roll-forward |
| CP-5-GAP-009 | Original-HTML and XBRL fidelity check | Original filings | Extraction success is not a fidelity review | All figures | Low impact | Original filings |

### QA issue findings (T5.1 to T5.8)

#### T5.1 Module and handoff register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/8f04cb8198444f19c3d2b57a44a3dbbf3377a990e3f1dead8e0cdaa265c64a42/1.response.md; run apg-2026-11-05-credit_snapshot-host | Source readiness for seven sources | High (filed statements) | Six H2 headings; no YAML front matter | Clear with remarks | Did not log the 2025 acquisition consideration difference |
| CP-1 | requests/CP-1/8c9438003737d77ae8450b7338a72304dbb5e7e5dad4ed38ccec69cddb11cc90/1.response.md; same run | Financial base, USD millions | High; EBITDA management-defined | Six H2 headings plus report selectors; no YAML front matter | Restricted | Covenant trigger on summarised wording; arithmetic verified |
| CP-1A | requests/CP-1A/8819ee1e4327c45a6f36cd9e326aaa824b4f5e47a12100cc34d5dbad7db3ed88/1.response.md; same run | Business, transaction, governance | High for facts; Low for management language | Six H2 headings plus report selectors; no YAML front matter | Clear with remarks | Open acquisition consideration conflict logged |
| CP-2 | requests/CP-2/871f8d6cbef7f51c16444d40274f1f67b35cb95efedf2223287dc7c1e81e9e17/2.response.md; same run (second attempt) | Credit synthesis from upstream only | Derived | Six H2 headings plus report selectors; no YAML front matter | Restricted | Maturity wording and one non-upstream figure |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Key findings: prior-year Q3 interest expense of USD 34 million | Supported by S4 page 3; not in upstream | Lineage break to the upstream-only rule | Carry in CP-1 or cite filing | Formatting / Hygiene Only |
| Minor | CP-2 | Key findings: new notes and revolver draw "have only partly reached cash interest" | Partly supported | Mechanism inferred; CP-1 said "may not yet" | Soften wording | Formatting / Hygiene Only |
| Minor | CP-1 | Cash flow: 795 proceeds and 310 repayments | Supported, composition unexplained | Funding sources beyond the notes not itemised | Flag as unitemised | Monitoring follow-up |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | LTM figures built as FY2025 plus nine months 2026 less nine months 2025 | Acquired EBITDA only from closing dates; no pro forma; labelled derived | None | Keep the derived label | Formatting / Hygiene Only |
| Material | CP-1, CP-2 | Indicative covenant EBITDA about 1,318 against adjusted EBITDA 1,191 | Covenant EBITDA includes pro forma and cost-saving adjustments per the release; adjusted EBITDA does not | Definitions differ between S7 page 7 and the adjusted measure | Keep labelled as inference; obtain definition | Restricts Committee Use |
| Minor | CP-1, CP-2 | Interest cover uses cash interest net of interest income | Not gross interest paid | None | State basis in committee extracts | Formatting / Hygiene Only |

Every derived figure in the upstream handoffs that was checked was recomputed and matches; none is an arithmetic defect.

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A | Notes guaranteed on a senior unsecured basis by the parent and certain subsidiaries | Indentures and guarantor schedule | Guarantors not enumerated | Obtain indentures | Yes |
| Material | CP-1, CP-1A | Issuer of record of the 4.125% and 4.750% notes is APi Group DE | Indentures | MD&A and exhibit index name different parties | Obtain indentures | Yes |
| Material | CP-1 | Term loan security and first lien status | Credit Agreement | Security not stated for the term loan in the supplied text | Obtain Credit Agreement | Yes |
| Material | CP-1, CP-2 | Springing covenant and permitted-payment capacity | Credit Agreement and indentures | Definitions and baskets absent | Obtain documents | Yes |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Issuer-reported fair values of the three note series are below carrying value | Traded prices or spreads | Fair values are issuer discounted-cash-flow estimates (Level 2), not market quotes | Keep the issuer-estimate label; no RV conclusion drawn | Informational; no relative value claim made |

No peer ranking, instrument recommendation or recovery conclusion appears in any module.

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-0, CP-1A, CP-2 | 2025 acquisition consideration 233 (S1), 235 (S2), 225 (S3 and S4); CP-0 omitted it, CP-1A logged it, CP-2 repeated it | Later reports restate the accrued component; S4 is the latest | Cite by filing and date; keep as open conflict | Acquisition spend narrative |
| Material | CP-1, CP-2 | CP-1 notes 361 short-term and current debt (revolver appears classified short-term; instalments unitemised); CP-2 states maturities begin in 2029 | None | Restate CP-2 maturity wording | Refinancing view |
| Material | CP-0, CP-1, CP-2 | CP-0 said the 30% trigger could not be confirmed; CP-1 computed 33.5% with a stated limitation; CP-2 states the test applies | CP-1 refines CP-0 on summarised wording | Treat as inference until the agreement is supplied | Covenant view |
| Minor | CP-1, CP-1A, CP-2 | Locations: over 500 (S1) and more than 600 (S7) | Different dates, management release | None beyond dating | Business profile |

Version control: the Q3 2026 report controls debt terms, covenant wording and availability in every module; the 10-K terms (term loan January 3, 2029, revolver 750) are correctly treated as superseded by the Ninth Amendment.

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Omitted material content | The synthesis does not carry claims outside debt that CP-1 lists (leases of 101 current and 218 noncurrent, contingent consideration of 84 and 2, insurance letters of credit of about 153 at December 31, 2025) | Add a one-line caveat to the leverage statement | Leverage may be read as complete debt-like claims |
| Minor | CP-1, CP-1A, CP-2 | Duplicative content | Reader summaries and key findings repeat figures by design | None | Formatting / Hygiene Only |

#### T5.8 Structured handoff and export integrity

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Envelope | No YAML front matter, Evidence Trace or Source Registry headings; the Markdown transport uses six H2 headings | None under this run | Downstream tools expecting the canonical envelope need an adapter |
| Minor | CP-2 | Second attempt accepted | First attempt rejected for a figure missing from the body; the accepted file is attempt 2 | None | Record only |

### Consolidated issue log (T5.9)

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-2 | Unsupported claim | Debt maturities described as starting in 2029 while 361 of short-term and current debt exists and term loan instalments apply | Restate with current-portion note | Restricts Committee Use | Open |
| CP5-002 | Material | CP-1, CP-2 | Unsupported claim | Covenant trigger status and headroom inferred from summarised wording; stated more firmly in the synthesis | Label as inference; obtain agreement | Restricts Committee Use | Open |
| CP5-003 | Material | CP-1A, CP-2 | Source conflict | 2025 acquisition consideration totals differ by filing (233, 235, 225) | Cite by filing and date; seek explanation | Restricts Committee Use | Open |
| CP5-004 | Minor | CP-2 | Lineage | Prior-year interest expense of 34 not carried upstream | Carry or cite | Formatting / Hygiene Only | Open |
| CP5-005 | Minor | CP-2 | Wording | New notes and revolver "only partly reached" cash interest is inferred | Soften | Formatting / Hygiene Only | Open |
| CP5-006 | Minor | CP-1 | Unitemised funding | 795 long-term proceeds and 310 repayments not itemised | Flag as gap | Monitoring follow-up | Open |
| CP5-007 | Minor | CP-2 | Omission | Claims outside debt not carried into the synthesis | Add caveat | Monitoring follow-up | Open |
| CP5-008 | Minor | CP-0 to CP-2 | Envelope | No YAML front matter or Evidence Trace headings under this transport | None | Formatting / Hygiene Only | Open |

### Remediation priority map

Must-fix before committee: CP5-001 (maturity wording), CP5-002 (label covenant status as inference and obtain the agreement), CP5-003 (cite acquisition totals by filing). Must-fix before the handoff is consumed downstream: none beyond these. Monitoring follow-up: CP5-006 and CP5-007. Formatting and hygiene: CP5-004, CP5-005 and CP5-008.

### Clearance decision

CLEARANCE DECISION: Restricted. Critical issues: 0. Material issues: 3. Minor issues: 5. Committee use: Restricted. The analysis may inform committee discussion with the covenant, maturity and acquisition-consideration statements qualified as above; no upstream conclusion is changed by this review. Corrections stated here do not edit the earlier handoffs: the credit synthesis maturity wording (CP5-001) should be read with the balance sheet short-term and current debt of 361 and the readiness handoff's omission of the acquisition consideration difference should be read with the business handoff's conflict log.

## Calculations

Independent recomputation from printed filing values (not from the handoffs), USD millions.

| Check | Inputs (source) | Result | Matches upstream |
| --- | --- | --- | --- |
| LTM net revenues | 7,911 (S1 p86) + 6,790 - 5,794 (S4 p3) | 8,907 | Yes |
| LTM adjusted EBITDA | 1,041 (S1 p68) + 896 - 746 (S7 p11) | 1,191 | Yes |
| LTM cash interest | 136 (S1 p88) + 98 - 105 (S4 p5) | 129 | Yes |
| Total debt / EBITDA | 3,601 / 1,191 | 3.02x | Yes |
| Net debt / EBITDA | (3,601 - 373) / 1,191 | 2.71x | Yes |
| Adjusted EBITDA / cash interest | 1,191 / 129 | 9.23x | Yes |
| Liquidity | 373 + 659; 912 + 745 | 1,032; 1,657 | Yes |
| Quarterly adjusted EBITDA path | 235 (S5) + 311 (S6) + 350 (S7) | 896, equals nine-month figure | Yes |
| Revolver usage | 335 / 1,000 | 33.5% | Yes |
| Nine-month growth | 896 / 746 - 1; 6,790 / 5,794 - 1 | 20.1%; 17.2% | Yes |
| Acquisition consideration | 271 + 532 + 394 | 1,197 | Yes |
| Debt tie-out | 2,147 + 335 + 337 + 277 + 500 + 5 | 3,601, equals printed total | Yes |

A further set of derived figures in CP-1 (net debt, free cash flow, reported EBITDA-based leverage, interest-based cover, fair value percentages, segment shares in CP-1A) was recomputed and agrees; none is listed above for brevity.

## Gaps

| Gap | Effect on confidence | Follow-up |
| --- | --- | --- |
| Executed Credit Agreement, Ninth Amendment and indentures not supplied | Covenant, guarantor and issuer-of-record claims stay at filing-summary strength; caps confidence | Obtain documents |
| Covenant EBITDA and letter-of-credit exclusion definitions not supplied | Trigger status and headroom unverified | Credit Agreement |
| No original-HTML or XBRL fidelity check was possible | Extraction fidelity untested; all figures traced to extracted text | Spot-check key tables |
| Recurring revenue share and beneficial ownership not supplied | Business-risk and governance statements qualitative | Add disclosures |
| No scoring script available in this transport | Numeric confidence score Not calculable; band set by the Restricted status cap | Run the scoring script when available |
| Full ledger | See the gaps ledger above (CP-5-GAP-001 to CP-5-GAP-009) | As listed |

## Next module

No further module is selected in this run. The report should be read with committee use restricted until the three Material issues (maturity wording, covenant status as inference, and the open 2025 acquisition consideration conflict) are addressed and the executed financing documents are obtained. A later run on the next quarterly report should supply a debt maturity table, the breakdown of short-term and current debt, and, if available, the Credit Agreement definitions.
