## Request

Evidence trace and research-integrity grade for AMC ENTERTAINMENT HOLDINGS, INC. (issuer id amc), as of 2026-11-05, on the credit_snapshot pathway, run id amc-2026-11-05-credit_snapshot-host. It audits the four accepted upstream handoffs (source readiness, financial base, business and transaction context, credit synthesis) against the seven pinned issuer sources, in USD. It changes no credit conclusion and silently repairs no lineage.

## Sources

Locator convention: "S4 page:12" is the retained text chunk numbered 12 in source S4, not a printed page.

Issuer sources relied on:

| Label | Exact source name | sha256 |
| --- | --- | --- |
| S1 | 10-K_2025-12-31_amc-20251231x10k.htm.jsonl | 0ee36dfaa277d4be92a491f5b99adc1814801764434d8deab942cd5a2a5838d7 |
| S2 | 10-Q_2026-03-31_amc-20260331x10q.htm.jsonl | 60b4c5d601e7b9acdc0496904f66b9f655c90ba8205a7e0b8cfdb830abd7ba76 |
| S3 | 10-Q_2026-06-30_amc-20260630x10q.htm.jsonl | 952c4d205e8b900447956bd8caf30135da02e7444c27c71416edab4cbcf69ef9 |
| S4 | 10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | 4d74cb1c191d1b28823e0af713c0d425aa587b54390a0af45163d9f0bd9f73ed |
| S5 | EX-99.1_2026-05-05_amc-20260505xex99d1.htm.jsonl | 8c768557ab2991f52a8715d41145f36c5481fa9f34d8f76f8e3c17ac84833c6d |
| S6 | EX-99.1_2026-07-20_amc-20260720xex99d1.htm.jsonl | 7ae4adc015a7738b87280223fdf61d61080e8bd76f8462c8935a6d99aa02e8e6 |
| S7 | EX-99.1_2026-11-04_amc-ex99d1.htm.jsonl | 51a7c35ada2d95a83a44b3a8c877a5584b3fe836e069b2ff43e63ad3815eecda |

Supplied handoffs (each re-anchored to issuer name, as-of date and run id):

| Module | sha256 | Scope consumed |
| --- | --- | --- |
| CP-0 | c885c49c340c71764325303325dd98265ae7aba265448e22f72e309753261f9e | Source readiness, 7 sources, gaps G1 to G10 |
| CP-1 | 8e7bd6a403005e8737f70ed50dbc8a7e41cbf01bba720956efc8b944b9480302 | Financial base, charts, registers, calculations C1 to C11 |
| CP-1A | 3dc635c9d415eebd00632520a019d6eb70c35baba975237904827d7a7c9ba219 | Business and transaction context, behaviour record, timeline |
| CP-2 | a85c30285c515dc1db843ef716cacd8785144288b430eb217b739ea10febe5b4 | Credit synthesis, key findings, strengths and weaknesses, risks |

Context file (settings only, not issuer evidence): sha256 0cce4dad135405f8586147db90660063f1faeb01eb8ee14c36784567b5aeaa09.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The upstream analysis is traceable: all 23 material claims tested have identified support and every calculation reproduces from printed inputs. Committee use is restricted because debt terms and any undrawn facility rest on filing summaries, not executed documents. | Medium | Executed indentures and credit agreements are not supplied, so legal-structure and liquidity-backstop conclusions cannot be verified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of 23 material claims, 12 are directly sourced and 7 are calculated; every calculation reproduced exactly from printed inputs. | Headline leverage, cover and free cash flow can be relied on as arithmetic. | High |
| Three conclusions rest on analyst inference: no undrawn facility, creditor-adverse structuring and the overall credit view. | They shape liquidity and behaviour judgements and need executed documents to firm up. | Medium |
| Trailing Adjusted EBITDA mixes two definitions, disclosed with a sensitivity of 0.9. | Leverage and cover may be slightly misstated; the FY2025 effect is unknown. | Medium |
| Two earlier open items closed: the 97% refinancing claim ties to filed amounts at 96.9%, and the MD&A net loss item is an International segment figure. | No unresolved conflict remains between sources. | High |
| The confidence score is 56, band Low, quality status Restricted. | Committee use needs disclosure of the two material findings. | High |

### Evidence trace view

The upstream analysis is traceable enough for restricted committee use, and the main provenance gap is the absence of executed financing documents. Of 23 material claims, 12 are directly sourced from filed statements, 7 are calculated and each reproduced exactly when recomputed from the printed inputs, 1 is assumption-based and 3 are analyst inference. Those three, the absence of an undrawn facility, the creditor-adverse reading of earlier transactions and the overall credit view, depend on indentures and credit agreements that are not supplied. Two earlier gaps are closed: management's refinancing share ties to filed principal, and an unexplained net loss figure belongs to the International segment. Two material findings and two minor findings remain open, giving a score of 56, a Low band and Restricted status.

### Traceability summary

| Module | Claims tested | Directly sourced or calculated | Inference or assumption | Open issues |
| --- | --- | --- | --- | --- |
| CP-0 | Source coverage and gap statements | All located | None | 0 |
| CP-1 | Statements, ratios, registers | All except the facility absence and pro forma net cash | 2 | 4 |
| CP-1A | Business facts, timeline, behaviour | Facts yes; behaviour reading no | 1 | 1 |
| CP-2 | Synthesis | Figures yes; view no | 1 | 3 |

### Top credit drivers and their traceability

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Earnings-led deleveraging: trailing Adjusted EBITDA 840.4 and total debt to Adjusted EBITDA 4.50x | CP-1 | Filed statements and release reconciliation; calculated | Sets debt service capacity and refinancing access | Leverage tolerance and monitoring posture | S1 page:77; S7 page:10; S4 page:12 | Two Adjusted EBITDA definitions mixed; effect on FY2025 not supplied |
| 2 | Liquidity is cash of 751.9 with no committed facility described | CP-1, CP-2 | Cash is filed; facility absence is a keyword search result | Cash is the only backstop to seasonal cash flow | Liquidity and default risk | S4 page:3; S1 page:161 | Executed credit agreements not supplied |
| 3 | October 5, 2026 refinancing: principal 4,086.1 with 2,816.0 due in 2031 and 1,120.0 later | CP-1, CP-1A | Note 11 and printed pro forma maturity table | Moves refinancing risk out but raises debt and adds a second lien layer | Refinancing, loss given default mechanics | S4 page:33-38 | Pro forma interest not computable; subsequent event to the balance sheet |
| 4 | Fixed charges and film-supply dependence: operating leases 3,761.9, fixed-charge cover 1.35x, seven distributors with 83% | CP-1, CP-1A, CP-2 | Filed lease note, risk factor, calculated cover | Operating leverage cuts both ways | Cash flow durability | S4 page:9; S1 page:41 | Fixed-charge cover is an analyst measure the issuer does not define |
| 5 | Creditor-behaviour record: July 2024 transfer of 175 theatres, partial 2025 exchange, share-paid fees | CP-1A, CP-2 | Filed descriptions of transactions | Priming and asset separation risk for lenders | Monitoring posture and legal review | S1 page:100; S1 page:95; S1 page:142; S4 page:15 | Characterization is inference; indentures and exchange terms not supplied |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Principal debt 3,782.6 at September 30, 2026 | CP-1 | S4 page:12 "Total principal amount of corporate borrowings" | Yes | High (filed, unaudited interim) | Directly Sourced | Supported | High | Committee-Ready |
| FY2025 Adjusted EBITDA 387.5; 9M 2026 707.2; 9M 2025 254.3 | CP-1 | S1 page:77; S7 page:10 | Yes | High; non-GAAP, management-defined | Directly Sourced | Supported | High | Committee-Ready |
| Cash 751.9 | CP-1, CP-2 | S4 page:3 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Pro forma principal 4,086.1 and its maturities by year | CP-1 | S4 page:38 | Yes | High (filed, pro forma table printed by issuer) | Directly Sourced | Supported | High | Committee-Ready |
| Operating lease liabilities 3,761.9 | CP-1, CP-2 | S4 page:9 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Seven distributors supplied about 83% of U.S. box office revenue | CP-1A, CP-2 | S1 page:41 | Yes | High (risk factor, audited filing) | Directly Sourced | Supported | High | Committee-Ready |
| Adjusted EBITDA margin 20.3% against 9.4% in Q3 | CP-1A, CP-2 | S7 page:10 | Yes | Medium (release, management non-GAAP reconciliation) | Directly Sourced | Supported | Medium | Committee-Ready |
| July 22, 2024 transfer of 175 theatres and intellectual property to unrestricted subsidiaries | CP-1A, CP-2 | S1 page:100 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| 590.0 of 950.0 Existing 7.5% Notes exchanged in 2025 | CP-1A, CP-2 | S1 page:95; S1 page:142 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| October 2026 refinancing: 2,000.0 first lien notes, 850.0 first lien and 1,120.0 second lien term loans with stated rates and maturities | CP-1, CP-1A | S4 page:33-36 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Covenant compliance as of September 30, 2026 | CP-1 | S4 page:17 | Yes | Medium (issuer belief) | Directly Sourced | Supported as issuer assertion | Medium | Committee-Ready |
| 892,604,638 shares; 99.75% in street name | CP-1A | S4 page:1; S4 page:44 | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| LTM Adjusted EBITDA 840.4 | CP-1 | C1 from S1 page:77, S7 page:10 | Yes | High inputs | Calculated | Supported with definition limitation | Medium | Committee-Ready |
| Total debt to Adjusted EBITDA 4.50x; net 3.61x | CP-1 | C3 from S4 page:12, page:3 | Yes | High inputs | Calculated | Supported | High | Committee-Ready |
| Adjusted EBITDA to cash interest 2.14x | CP-1 | C2, C4 from S1 page:116; S4 page:4 | Yes | High inputs | Calculated | Supported | High | Committee-Ready |
| Trailing free cash flow 168.0 | CP-1 | C1, C5 from S1 page:115; S4 page:4 | Yes | High inputs | Calculated | Supported | High | Committee-Ready |
| Pro forma total debt to Adjusted EBITDA 4.86x | CP-1 | C3 from S4 page:38 | Yes | High inputs | Calculated | Supported | Medium | Committee-Ready |
| Fixed-charge cover 1.35x | CP-2 | C1 from CP-1 inputs (rent S4 page:2, S1 page:113) | Yes | High inputs; analyst-defined measure | Calculated | Supported | Medium | Committee-Ready |
| Management's 97% refinancing share is about 96.9% of filed principal | CP-1A | 3,666.5 / 3,782.6 from S4 page:12, page:38 | Yes | High inputs | Calculated | Supported | High | Committee-Ready |
| Pro forma net debt to Adjusted EBITDA 4.01x | CP-1 | Cash less the 32.7 used at closing (S4 page:38); later fees unknown | Yes | Medium | Assumption-Based | Partially supported | Low | Remediation Needed |
| No committed undrawn facility exists | CP-1, CP-2 | Absence from keyword search of seven sources; S1 page:161 mentions only a revolver with a stated maturity of April 22, 2024 | Partial | Medium | Analyst Inference | Partially supported | Low | Remediation Needed |
| Creditor-adverse reading of the 2024 transfer and 2025 exchange | CP-1A, CP-2 | S1 page:100; S1 page:95; S4 page:16 | Partial | Medium (summaries of legal documents) | Analyst Inference | Partially supported | Medium | Remediation Needed |
| Overall view: recovering but thinly cushioned | CP-2 | Synthesis of rows above | Yes | Medium | Analyst Inference | Supported by cited basis | Medium | Committee-Ready |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total principal amount of corporate borrowings 3,782.6 | source-text/10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | 10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | S4 | page:12 / Note 5 | Debt register | Sourced | High | Components add to the total |
| Pro forma principal 4,086.1 | source-text/10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | 10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | S4 | page:38 / Note 11 | Debt after refinancing | Sourced | High | Components 2,000.0, 850.0, 1,120.0 and 116.1 add to it |
| FY2025 Adjusted EBITDA 387.5 | source-text/10-K_2025-12-31_amc-20251231x10k.htm.jsonl | 10-K_2025-12-31_amc-20251231x10k.htm.jsonl | S1 | page:77 / Item 7 | Financials table | Sourced | High | Earlier definition |
| Adjusted EBITDA 347.5, 122.5, 707.2, 254.3 | source-text/EX-99.1_2026-11-04_amc-ex99d1.htm.jsonl | EX-99.1_2026-11-04_amc-ex99d1.htm.jsonl | S7 | page:10 / reconciliation | Adjusted EBITDA reconciliation | Sourced | Medium | Same figures in S4 page:28 |
| Cash 751.9 and restricted cash 39.6 | source-text/10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | 10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | S4 | page:3 / balance sheet | Liquidity | Sourced | High | Restricted cash excluded |
| Cash interest paid 406.9 and 401.6 | source-text/10-K_2025-12-31_amc-20251231x10k.htm.jsonl | 10-K_2025-12-31_amc-20251231x10k.htm.jsonl | S1 | page:116 / cash flow supplemental | Interest cover | Sourced | High | Nine months 270.9 and 285.5 at S4 page:4 |
| Operating cash flow and capital expenditures | source-text/10-K_2025-12-31_amc-20251231x10k.htm.jsonl | 10-K_2025-12-31_amc-20251231x10k.htm.jsonl | S1 | page:115 / cash flow | Free cash flow | Sourced | High | Nine months at S4 page:4 |
| Operating lease liabilities 3,761.9 | source-text/10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | 10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | S4 | page:9 / Note 2 | Claims outside debt | Sourced | High | Cash paid for operating leases 704.7 on the same chunk |
| Seven distributors 83% | source-text/10-K_2025-12-31_amc-20251231x10k.htm.jsonl | 10-K_2025-12-31_amc-20251231x10k.htm.jsonl | S1 | page:41 / Item 1A | Film supply concentration | Sourced | High | Risk factor wording |
| Transfer of 175 theatres to Muvico and Centertainment | source-text/10-K_2025-12-31_amc-20251231x10k.htm.jsonl | 10-K_2025-12-31_amc-20251231x10k.htm.jsonl | S1 | page:100 / Item 7 | Timeline | Sourced | High | Indenture text not supplied |
| Existing 7.5% Notes 950.0 to 360.0 | source-text/10-K_2025-12-31_amc-20251231x10k.htm.jsonl | 10-K_2025-12-31_amc-20251231x10k.htm.jsonl | S1 | page:142 / Note 7 | Governance table | Sourced | High | Offer terms to holders not supplied |
| Subsequent event terms and rates | source-text/10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | 10-Q_2026-09-30_amc-20260930x10q.htm.jsonl | S4 | page:33-38 / Note 11 | Transaction summary | Sourced | High | Executed documents referenced at S4 page:96-97 |
| No undrawn facility described | source-text/10-K_2025-12-31_amc-20251231x10k.htm.jsonl | 10-K_2025-12-31_amc-20251231x10k.htm.jsonl | S1 | page:161 / Note 7 | Liquidity | Inference | Medium | Absence of evidence; [Source Not Provided] for executed agreements |
| Management claims: market leader, October box office up about 35% | source-text/EX-99.1_2026-11-04_amc-ex99d1.htm.jsonl | EX-99.1_2026-11-04_amc-ex99d1.htm.jsonl | S7 | page:3 | Operating model | Sourced | Low (promotional) | Tagged Management Language upstream |

### Calculation and assumption register

Each calculation was recomputed independently by parsing the printed inputs from the retained source text of S1, S4 and S7, not from the upstream handoff text.

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA | CP-1 C1; CP-2 | FY2025 387.5; 9M 2026 707.2; 9M 2025 254.3 (USD m) | FY2025 + 9M 2026 - 9M 2025 = 840.4; recomputed 840.4 | Calculated | Reproduced | Medium (definitions mixed) | Leverage, cover | S1 page:77; S7 page:10 |
| LTM cash interest paid | CP-1 C2 | FY2025 406.9; 9M 2026 270.9; 9M 2025 285.5 | 406.9 + 270.9 - 285.5 = 392.3; recomputed 392.3 | Calculated | Reproduced | High | Debt service | S1 page:116; S4 page:4 |
| LTM operating cash flow, capital expenditures and free cash flow | CP-1 C1, C5 | FY2025 (119.8) and 246.1; 9M 2026 283.5 and 158.8; 9M 2025 (246.5) and 162.7 | 410.2 - 242.2 = 168.0; recomputed 168.0 | Calculated | Reproduced | High | Liquidity | S1 page:115; S4 page:4 |
| Total debt / Adjusted EBITDA | CP-1 C3 | Principal 3,782.6; 4,024.2; 4,134.5 | 3,782.6 / 840.4 = 4.50; 4,024.2 / 387.5 = 10.39; 4,134.5 / 343.9 = 12.02; recomputed 4.50 and 10.39 | Calculated | Reproduced | High | Leverage | S4 page:12; S1 page:142 |
| Net debt / Adjusted EBITDA | CP-1 C3 | Cash 751.9; 428.5; 632.3 | (3,782.6 - 751.9) / 840.4 = 3.61; 9.28; 10.18; recomputed 3.61 | Calculated | Reproduced | High | Leverage | S4 page:3; S1 page:114 |
| Adjusted EBITDA / cash interest | CP-1 C4 | 840.4 / 392.3; 387.5 / 406.9; 343.9 / 401.6 | 2.14; 0.95; 0.86; recomputed 2.14 and 0.95 | Calculated | Reproduced | High | Coverage | S1 page:116; S4 page:4 |
| Pro forma total debt / Adjusted EBITDA | CP-1 C3 | 4,086.1 and 840.4 | 4.86; recomputed 4.86 | Calculated | Reproduced | Medium | Refinancing | S4 page:38 |
| Pro forma net debt / Adjusted EBITDA | CP-1 C3 | Cash 751.9 less assumed closing use 32.7 | (4,086.1 - 719.2) / 840.4 = 4.01 | Assumption-Based | Reproduced arithmetic; assumption partial | Low | Refinancing | S4 page:38 |
| Fixed-charge cover | CP-2 C1 | Adjusted EBITDA + rent; cash interest + rent (rent 891.6, 887.3, 873.6) | 1,732.0 / 1,283.9 = 1.35; 1,274.8 / 1,294.2 = 0.99; 1,217.5 / 1,275.2 = 0.95 | Calculated | Reproduced by hand | Medium | Coverage | S4 page:2; S1 page:113 |
| Lease-adjusted leverage | CP-1 C8 | Debt, finance leases, operating leases, EBITDA, rent | 7,595.2 / 1,732.0 = 4.39 | Calculated | Reproduced by hand | Medium | Leverage | S4 page:9, page:12 |
| Refinancing share | CP-1A | 3,666.5 repaid or discharged; 3,782.6 principal | 3,666.5 / 3,782.6 = 96.9% | Calculated | Reproduced by hand | High | Refinancing | S4 page:12, page:38 |
| Fixed coupons on new notes and second lien loans | CP-1 C7; CP-2 C4 | 2,000.0 at 8.875%; 1,120.0 at 11.25% | 177.5 + 126.0 = 303.5 | Calculated | Reproduced by hand | High | Debt service | S4 page:34, page:36 |

### Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | No committed undrawn facility | Inferred from absence in a keyword search | Analyst Inference | Liquidity is understated if one exists | Read the executed credit agreements | Liquidity chart, credit view, key risks |
| MATERIAL | Creditor-adverse reading of the 2024 transfer and 2025 exchange | Legal capacity and offer terms rest on filing summaries | Analyst Inference | Priming and rights conclusions need clause-level support | Add the indentures and 2025 transaction documents; legal review | Governance table, credit view |
| MINOR | Pro forma net debt 4.01x | Cash after closing is an estimate | Assumption-Based | Net ratio is a floor | Replace with reported cash after fees | Leverage chart |
| MINOR | Trailing leverage and cover | Two Adjusted EBITDA definitions mixed | Calculated | Basis difference unquantified for FY2025 | Obtain recast FY2025 | Leverage and cover charts |
| MINOR | Credit view | Synthesis is judgment | Analyst Inference | Tagged as such upstream | None beyond the above | Credit view |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identification | Strong: every figure carries a source label and chunk locator | All upstream tables cite S1 to S7 pages | A reader can open the cited chunk | Low risk of orphan claims | None |
| Locator precision | Adequate: chunk numbers, not printed pages | Locator convention stated in each handoff | Chunk numbers differ from printed page numbers | Slows manual checks | State chunk-to-page mapping if exported |
| Calculation reproducibility | Strong: 12 of 12 register items reproduced | Calculation register above | Errors would change leverage or cover | None found | None |
| Separation of management claims from fact | Strong: tagged upstream | Management Language rows at S7 page:3, S1 page:9 | Promotional wording could be mistaken for fact | Handled | None |
| Version and subsequent-event control | Adequate: refinancing kept separate from the September 30, 2026 balance sheet; Adjusted EBITDA definition change disclosed | S4 page:27, page:38 | Mixing dates or definitions would misstate leverage | One unquantified FY2025 effect | Obtain recast FY2025 |
| Legal-document support | Weak: summaries only | S4 page:96-97 references exhibits not supplied | Rights and ranking claims cannot be clause-checked | Restricts legal conclusions | Add executed documents |

### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| TG-1 | Executed indentures and credit agreements | Form 8-K exhibits referenced at S4 page:96-97 | Rights, ranking, priming and covenant claims need clause support | Governance table, key risks | Caps status at Restricted | Form 8-K filed October 6, 2026 exhibits |
| TG-2 | Existence of a committed undrawn facility | Executed credit agreements | Liquidity backstop | Liquidity chart, credit view | Lowers confidence | Same exhibits |
| TG-3 | Recast FY2025 Adjusted EBITDA | Company recast figure | Trailing ratios mix definitions | Leverage and cover | Minor reduction | Company disclosure |
| TG-4 | Pro forma interest | First lien margin and toggle terms | Post-refinancing cover is unknown | Pro forma interest cover | Limits forward view | Credit agreement |
| TG-5 | Terms of the 2025 exchange offer | Offer documents | Pro-rata treatment of holders is unknown | Behaviour assessment | Keeps the reading as inference | 2025 transaction documents |
| TG-6 | Ownership and beneficial holders | Annual meeting proxy statement | Control cannot be assessed | Governance view | Minor reduction | Proxy statement |

### Research integrity audit

Lane results. Unsupported claims: two findings, both about inference that goes beyond the sources (F-02 and the legal reading in F-01). Calculation: no error found; definition drift in Adjusted EBITDA disclosed (F-03). Legal and covenant: summary-only support (F-01). Market and relative value: no market or relative value claim exists in the upstream handoffs, and the context leaves quotes, ratings and valuation blank. Cross-module consistency: the shared datapoints agree. Evidence trace: no orphan claim found. Handoff envelope: all four handoffs carry the six required headings and anchors.

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1, CP-2 | No committed undrawn facility (F-02) | Partially Supported | Absence inferred from a keyword search of seven sources; executed agreements not supplied | Confirm in the credit agreements | Restricts Committee Use |
| MINOR | CP-1A, CP-2 | Management Language rows | Supported | Tagged correctly; wording not adopted | None | Formatting / Hygiene Only |
| None | CP-1, CP-1A, CP-2 | Figures cited to S1 to S7 | Supported | 23 claims traced; none unsupported | None | Monitoring Follow-Up |

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | LTM Adjusted EBITDA 840.4 reproduced | FY2025 earlier definition with 2026 revised definition | None between sources; basis differs, sensitivity 0.9 (F-03) | Obtain recast FY2025 | Monitoring Follow-Up |
| None | CP-1 | Leverage, cover and free cash flow reproduced | Principal as total debt; finance leases shown separately; operating leases excluded and disclosed | None | None | Monitoring Follow-Up |
| None | CP-2 | Fixed-charge cover reproduced | Analyst measure using the statement rent line, disclosed | None | None | Monitoring Follow-Up |

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1A, CP-2 | The Muvico Group is unrestricted under the Existing 7.5% Notes indenture and the 2024 transfer was creditor-adverse (F-01) | Executed 7.5% Notes indenture, Muvico Credit Agreement | Only the filing summary at S1 page:100 | Add documents; legal review | Legal Review Required |
| MATERIAL | CP-1, CP-1A | Ranking, guarantees and collateral groups for the 2031 Notes, first lien and second lien term loans (F-01) | Executed 2031 Notes indenture, credit agreements, intercreditor agreements | Only the Note 11 summary at S4 page:33-37 | Add documents; legal review | Legal Review Required |

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None | All upstream modules | No market, spread, price or relative value claim is made | None required for the claims made | Context leaves quotes and valuation blank | None | Monitoring Follow-Up |

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| None | CP-1, CP-1A, CP-2 | Principal 3,782.6, trailing Adjusted EBITDA 840.4, leverage 4.50x, cash 751.9, pro forma principal 4,086.1 agree across modules | None | None | Consistent |
| MINOR (resolved, F-05) | CP-0, CP-1A | CP-0 recorded that the 97% refinancing share had no filing counterpart; CP-1A showed it ties to 96.9% | CP-0 cannot be edited; this audit records the correction | None further | CP-0 gap G8 is closed |
| MINOR (resolved, F-06) | CP-0 | CP-0 left an MD&A net loss figure of 96.3 and 90.1 unconfirmed against the consolidated net loss | S1 page:91 to page:94 form the International markets discussion, whose revenue increase is 49.8, and the consolidated increase of 211.7 equals the U.S. 161.9 plus International 49.8 | None further | CP-0 gap G10 is closed on the evidence of section order (S1 page:81 consolidated, page:86 U.S., page:91 onward International) and an income tax figure of 1.8 at S1 page:93 that differs from the consolidated 4.5, so the 96.3 and 90.1 are read as International segment net loss |
| None | CP-0, CP-1, CP-1A | Shares outstanding 892,604,638 and share change used consistently | None | None | Consistent |

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Presentation | The financial base view is one long paragraph | None needed for the report; split if exported | Formatting / Hygiene Only |
| None | CP-1A, CP-2 | Duplication | Repeated ratios (4.50x, 2.14x, 1.35x) appear in several sections for different purposes | None | None |

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| None | CP-0, CP-1, CP-1A, CP-2 | Six required headings, reader summary and opening view | None | None | Accepted by CP-OS |
| None | CP-1 | Chart tables | Headers and plain-number cells meet the report selectors | None | Charts populate |
| None | CP-1A, CP-2 | Prose-only sections | No tables under prose-only headings | None | Report sections populate |

#### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| F-01 | MATERIAL | CP-1A, CP-2, CP-1 | Legal Support Gap | Legal and structural claims rest on filing summaries; executed documents not supplied | Add documents; legal review | Requires Legal Review | Open |
| F-02 | MATERIAL | CP-1, CP-2 | Partially Supported Claim | No committed undrawn facility inferred from a keyword search | Confirm in the credit agreements | Restricts Committee Use | Open |
| F-03 | MINOR | CP-1, CP-2 | Formula / Definition Drift | Trailing Adjusted EBITDA mixes two definitions; sensitivity 0.9 | Obtain recast FY2025 | Monitoring Follow-Up | Open |
| F-04 | MINOR | CP-1 | Duplicative / Immaterial Content | Dense single-paragraph view | Split if exported | Formatting / Hygiene Only | Open |
| F-05 | MINOR | CP-0, CP-1A | Cross-Module Inconsistency | 97% claim recorded as lacking support, then supported | None further | Monitoring Follow-Up | Resolved |
| F-06 | MINOR | CP-0 | Citation Gap | MD&A net loss item left unconfirmed | None further | Monitoring Follow-Up | Resolved |

#### Remediation priority

First, add the executed financing documents from the Form 8-K exhibits (closes F-01, F-02, TG-1, TG-2, TG-4). Second, obtain the recast FY2025 Adjusted EBITDA (F-03). Third, add the proxy statement and the 2025 exchange documents (TG-5, TG-6).

#### Clearance and score

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 2. Committee Use: Restricted.

No claim in the upstream handoffs is unsupported or miscalculated; committee use is restricted because two material findings (F-01 and F-02) limit legal-structure and liquidity-backstop conclusions to what the filings summarise. The two resolved minor issues (F-05 and F-06) are not counted as open.

Confidence score, from the script confidence_score.py with 23 material claims (12 Directly Sourced, 7 Calculated, 1 Assumption-Based, 3 Analyst Inference), all 17 required registers present, source gate pass, open findings 2 MATERIAL and 2 MINOR: E = 86.96, C = 100.0, S = 1.0, P = 36, score = clamp((0.6 x 86.96 + 0.4 x 100) x 1.0 - 36, 0, 100) = 56.17, rounded 56. Band Low. qa_status Restricted. committee_status Restricted.

## Calculations

C1. Independent recomputation. Inputs were parsed from the retained text of S1 (pages 77, 115, 116), S4 (pages 3, 4, 12) and S7 (page 10), not copied from the handoffs: FY2025 Adjusted EBITDA 387.5 and FY2024 343.9; Adjusted EBITDA 347.5, 122.5, 707.2 and 254.3; principal 3,782.6 and 4,024.2; cash interest paid 270.9, 285.5, 406.9 and 401.6; operating cash flow 283.5, (246.5), (119.8) and (50.8); capital expenditures 158.8, 162.7, 246.1 and 245.5; cash 751.9 and 428.5.
- LTM Adjusted EBITDA: 387.5 + 707.2 - 254.3 = 840.4.
- LTM cash interest: 406.9 + 270.9 - 285.5 = 392.3.
- LTM free cash flow: (-119.8 + 283.5 + 246.5) - (246.1 + 158.8 - 162.7) = 410.2 - 242.2 = 168.0.
- Total debt to Adjusted EBITDA: 3,782.6 / 840.4 = 4.50; 4,024.2 / 387.5 = 10.39.
- Net: (3,782.6 - 751.9) / 840.4 = 3.61.
- Cash interest cover: 840.4 / 392.3 = 2.14; 387.5 / 406.9 = 0.95.
- Pro forma: 4,086.1 / 840.4 = 4.86.
All reproduce the figures in the financial base.

C2. Hand recomputation of other items: fixed-charge cover (840.4 + 891.6) / (392.3 + 891.6) = 1,732.0 / 1,283.9 = 1.35; (387.5 + 887.3) / (406.9 + 887.3) = 1,274.8 / 1,294.2 = 0.99; refinancing share 3,666.5 / 3,782.6 = 96.9%; fixed coupons 2,000.0 x 8.875% + 1,120.0 x 11.25% = 177.5 + 126.0 = 303.5; pro forma maturities 8.5 + 8.5 + 8.5 + 124.6 + 2,816.0 + 1,120.0 = 4,086.1; principal components 1,979.2 + 423.9 + 903.4 + 116.1 + 360.0 = 3,782.6.

C3. Consolidation check for F-06: consolidated revenue increase 4,848.9 - 4,637.2 = 211.7; U.S. markets 161.9 plus International markets 49.8 = 211.7 (S1 pages 81, 86 and 91).

C4. Claim counts: 12 + 7 + 1 + 3 = 23 material claims.

## Gaps

- Executed indentures, credit agreements and intercreditor agreements are not supplied; legal-structure, ranking, covenant and facility claims rest on filing summaries (F-01, F-02, TG-1 and TG-2).
- Recast FY2025 Adjusted EBITDA is not supplied (F-03, TG-3).
- Pro forma interest, the 2025 exchange terms and ownership are not supplied (TG-4 to TG-6).
- Chunk locators are not printed page numbers, and no image, chart or XBRL content was inspected, so presentation-only content could not be traced.
- The confidence script was run with the analyst's lineage classification and severity judgments; the arithmetic is script-owned, the classifications are not.

## Next module

This is the last module in the minimum set. The report should carry the Restricted status and the two material findings (F-01 and F-02) alongside the key findings, financial charts and transaction summary, and the remediation list above is the follow-up needed to lift the restriction.
