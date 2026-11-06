# CP-5 evidence trace and research integrity: UBS Group AG (ubs)

## Request

- Issuer: UBS Group AG (issuer id `ubs`), as of 2026-11-05, information cutoff 2026-11-05, pathway credit_snapshot, reporting currency USD.
- Scope: Top 5 traceability of the credit drivers in the accepted handoffs for source readiness, financial base, business context and credit synthesis, with a research-integrity grade. Governance layer only: no substantive credit conclusion is changed and no lineage is repaired silently.
- Execution: host session. Every upstream locator and number was re-opened in the pinned sources; one table was also checked against the original filed HTML.

## Sources

Issuer sources (pinned `.jsonl` text; locators are `page:N` extraction chunks, not printed pages):

| Source | sha256 | Role |
| --- | --- | --- |
| 20-F_2025-12-31_ubs-20251231.htm.jsonl | c65ff0a03ee3c3df685c628425c6a0a7856867141560663149d32b58774d8f33 | Annual report on Form 20-F, fiscal year 2025 |
| 6-K_2026-03-31_edgarq1q26kubsgroupagc.htm.jsonl | 5ae425915ce6d8540a2dcbe4beb8ed52f974546cb1a0a776687e74bfb6a0ae6d | Capitalization table, 31.3.26 |
| 6-K_2026-03-31_investorpresotext2026.htm.jsonl | 84e6720eb0ad0ada288bec163d56547d8305bba53a01f71c7fcd5a3acd94f71a | First quarter 2026 call transcript |
| 6-K_2026-06-30_investorpresotext2026.htm.jsonl | 671f7dde67986089a1c17da85500334fa96b51697d1642480c22e2b5d6422aa1 | Second quarter 2026 call transcript |
| 6-K_2026-07-29_edgarq2q26kubsgroup.htm.jsonl | 88627f5322eed51bd548e2eb9daaa4bff0f8cc654e252b054c4865eeda3901ea | Capitalization table, 30.6.26 |
| 6-K_2026-09-30_edgar3q26kubsgroupc.htm.jsonl | faea893d4d4d07cf7975acc81d8e41156e0b136d2c529429a6c83f334ac28864 | Capitalization table, 30.9.26 |
| 6-K_2026-09-30_investorpresotext2026.htm.jsonl | 2ac25318ab8710edaece00656540a1c90de7efab36a24b488600ed02e222986e | Third quarter 2026 call transcript |
| context | a67d394ad1fe0320e0c68be1bf7ef2da619705355c7aa8f5e62b6171bbf4fb2d | Run settings; not issuer evidence |

Supplied handoffs (all four were accepted by CP-OS before this run):

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 2e54133f1b22d47b492e44c16bd40091878fdaaf285f1d8de08cc5d1ee03cf43 | Source readiness |
| CP-1 | 685fa8e5832878fa7692e257450c83b45286cefc7233978ce033b37754932207 | Reported financial base |
| CP-1A | 7fa4d371e764e1152820b84955958152894dccaa744ff170272babe7d2e99475 | Business and transaction context |
| CP-2 | 18d5ae29b71b4120b0d445bed97b442048fd215ff958c49281cf2ab5a33751df | Fundamental credit synthesis |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Most of the credit view traces cleanly to the annual report and recalculates within rounding. Evidence for 2026 is weaker, resting on spoken, rounded management statements, so committee use should be restricted for current-period and debt-ranking questions. | Medium | There are no 2026 interim statements and no instrument-level debt terms in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every capital, liquidity and balance sheet figure checked matched the filing, and calculated figures matched within 1 USD m of rounding. | The audited year-end base can be relied on for capital and funding questions. | High |
| The Swiss capital estimate of around USD 22bn is the company's own figure and is sourced, but the rule text and timing are not in the pack. | The largest identified risk cannot be sized or dated independently. | Medium |
| One liquidity comparison mixes bases and one litigation statement goes beyond the filing. | These two statements need caveats before committee use, though the ratios beside them stand. | Medium |
| Two timing statements about the Swiss rules are not reconciled. | The date from which the capital need bites is uncertain. | Low |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 2 are calculated, 0 are assumption-based, 1 is an analyst inference, and 1 is an insufficient-information item. The most important provenance gap is the absence of 2026 interim statements and instrument-level debt terms, which matters because every third-quarter 2026 figure is spoken, rounded management language and no ranking or maturity can be traced to a debt document; it implies that committee use is restricted to the audited year-end base. The audit found no wrong locator and no fabricated figure, and it flagged two statements needing caveats and one unreconciled timing difference. Module status is Ready with Limitations, scope Top 5, committee status Restricted. No numeric confidence score is computed or invented.

### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 20-F_2025-12-31_ubs-20251231.htm.jsonl | High: filed annual report, audited statements | FY2025 with FY2024 and FY2023 comparatives | UBS Group AG consolidated, IFRS, USD | Statements, notes, capital, liquidity, debt notes, maturity table, segments, regulation | Audit opinion text not in extracted text (page:371 gives a cross-reference only); chunk locators, not printed pages | CP-1, CP-1A, CP-2 |
| S2 | 6-K_2026-03-31_edgarq1q26kubsgroupagc.htm.jsonl | Medium: filed, unaudited extract | 31.3.26 and 31.12.25 | UBS Group AG consolidated, USD | Debt split short and long term, equity, 88% unsecured | Capitalization table only | CP-1 |
| S3 | 6-K_2026-03-31_investorpresotext2026.htm.jsonl | Low for figures: management speech, rounded | Q1 2026 | Group, divisions, UBS AG standalone | Results, capital ratios, capital rules, integration | Slides and quarterly report not supplied | CP-1, CP-1A |
| S4 | 6-K_2026-06-30_investorpresotext2026.htm.jsonl | Low for figures: management speech, rounded | Q2 2026 | Group, divisions, UBS AG standalone | Same as S3 | Same as S3 | CP-1, CP-1A |
| S5 | 6-K_2026-07-29_edgarq2q26kubsgroup.htm.jsonl | Medium: filed, unaudited extract | 30.6.26 and 31.3.26 | UBS Group AG consolidated, USD | Single debt issued line, equity, 88% unsecured | No short and long term split | CP-1 |
| S6 | 6-K_2026-09-30_edgar3q26kubsgroupc.htm.jsonl | Medium: filed, unaudited extract | 30.9.26 and 30.6.26 | UBS Group AG consolidated, USD | Single debt issued line, equity, 87% unsecured | No short and long term split | CP-1, CP-2 |
| S7 | 6-K_2026-09-30_investorpresotext2026.htm.jsonl | Low for figures: management speech, rounded | Q3 2026 | Group, divisions, UBS AG standalone | Q3 results, capital and liquidity ratios, capital returns, rules, litigation timing | Same as S3 | CP-1, CP-1A, CP-2 |
| H0 | CP-0 handoff | Medium: accepted, host-authored | As of 2026-11-05 | Source set | Readiness and limitations | Host-authored, not independently reviewed | All |
| H1 | CP-1 handoff | Medium: accepted, host-authored | FY2025, 2026 quarters | UBS Group AG consolidated | Financial base | Q3 2026 rows spoken and rounded | CP-1A, CP-2 |
| H1A | CP-1A handoff | Medium: accepted, host-authored | 2014 to 2029 timeline | UBS Group AG and subsidiaries | Business and transaction context | Management-language rows | CP-2 |
| H2 | CP-2 handoff | Medium: accepted, host-authored | As of 2026-11-05 | UBS Group AG | Credit synthesis | Inherits all upstream limits | CP-5 |

### Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Capital and loss-absorbing capacity above Swiss requirements at 31 December 2025 | CP-2, CP-1 | Eligible CET1 capital USD 71,262 million against a requirement of USD 52,448 million, and going concern and gone concern capital above their requirements | Capital absorbs losses first, so headroom lowers default risk and sets room for distributions | Anchors the credit view | S1 page:229, page:37 | Year-end 2025 only; 2026 ratios are spoken |
| 2 | Funding and liquidity: deposit-led balance sheet, large liquid assets, debt due within 12 months | CP-2, CP-1 | Customer deposits USD 788,367 million; liquidity coverage ratio 182.6%; liquid assets USD 331.6 billion; debt due within 12 months USD 113.7 billion undiscounted | Refinancing and run-off risk | Supports low near-term liquidity risk | S1 page:373, page:246, page:497 | Comparison of liquid assets with 12-month debt mixes bases |
| 3 | Swiss capital rules on foreign subsidiary investments | CP-2, CP-1A | Company estimate of around USD 22bn additional CET1 at UBS AG | Could trap capital and limit distributions | Largest identified risk | S1 page:88, page:89; S3 page:4; S7 page:3 | Rule text and timing not supplied |
| 4 | Credit Suisse legacy litigation and resolution mechanics | CP-2, CP-1A | Litigation provisions USD 2,200 million and contingent liabilities USD 531 million; AT1 case pending; single point of entry strategy | Cash and capital cost; loss-absorption path for holding-company instruments | Unquantified tail risk | S1 page:434, page:113, page:84; S7 page:14 | No claim amounts; no instrument terms |
| 5 | Earnings level and market sensitivity | CP-2, CP-1 | Operating profit before tax USD 8,853 million against USD 6,821 million; non-interest income about 84% of revenue | Capital generation depends on fees and trading | Supports earnings durability view | S1 page:371, page:409 | Market sensitivity is an inference; 2026 earnings are spoken |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Capital headroom above Swiss requirements | CP-2 | S1 page:229: CET1 required 52,448 and eligible 71,262 (USD m); recomputed difference 18,814 | Yes | High | Calculated | Supported | High | Committee-Ready |
| Liquidity and funding lower refinancing risk | CP-2 | S1 page:246 liquidity coverage ratio 182.6%; page:497 buckets; the 2.9x comparison is derived | Yes | High for inputs; the comparison mixes bases | Analyst Inference | Supported with caveat | Medium | Remediation Needed |
| Swiss package could need around USD 22bn extra CET1 at UBS AG | CP-2 | S1 page:89: "We currently estimate that UBS AG would be required to hold additional CET1 capital of around USD 22bn" | Yes | High for the existence of the estimate; it is the company's own | Directly Sourced | Supported | Medium | Committee-Ready |
| Litigation tail and resolution mechanics | CP-2 | S1 page:113 "may have material adverse consequences for the combined Group"; page:434 provisions; no claim amount | Partial | High for the filing; amounts missing | Insufficient Information | Partly supported | Low | Remediation Needed |
| Earnings improved and are market-sensitive | CP-2 | S1 page:371 (8,853 against 6,821) and page:409 (41,826 of 49,573 non-interest) | Yes | High | Calculated | Supported for the improvement; the market-sensitivity mechanism is an inference | Medium | Committee-Ready |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenues 49,573 USD m and operating profit before tax 8,853 USD m, FY2025 | Primary financial statements > Income statement | 20-F_2025-12-31_ubs-20251231.htm.jsonl | S1 | page:371 | CP-1 financial table | Sourced | High | Matches |
| Total assets 1,617,427 USD m; customer deposits 788,367 USD m | Balance sheet | same | S1 | page:373 | CP-1 financial table | Sourced | High | Matches |
| Debt issued at amortized cost 214,706 USD m and at fair value 113,794 USD m | Notes 15 and 16 | same | S1 | page:432, page:433 | CP-1 debt section | Sourced | High | Sum 328,500 against 328,501 in S2: rounding |
| Subordinated debt 17,878 USD m of which high-trigger AT1 17,551 USD m | Note 16 | same | S1 | page:433 | CP-1 debt section | Sourced | High | Matches |
| Guarantee of Credit Suisse (USA) LLC debt, USD 742 m maturing July 2032 | Note 16 | same | S1 | page:433 | CP-1 correction; CP-2 | Sourced | High | Matches; page:434 completes the guarantee wording |
| CET1 required 52,448 and eligible 71,262; going concern 73,955 and 91,176; gone concern 52,917 and 96,130 | Capital management | same | S1 | page:229 | CP-2 key findings | Sourced | High | Matches; headrooms recalculated |
| Key figures: CET1 ratio 14.4%, liquidity coverage ratio 182.6%, net stable funding ratio 116.1% | Our key figures | same | S1 | page:37 | CP-1 financial table | Sourced | High | Matches |
| High-quality liquid assets 331.6 USD bn and 51.8 USD bn excluded | Liquidity and funding | same | S1 | page:246 | CP-2 key findings | Sourced | High | Matches |
| Maturity buckets for debt at amortized cost and at fair value | Note 23b | same | S1 | page:497, page:498 | CP-1 chart; CP-2 | Sourced | High | Bucket positions confirmed from the original filed HTML tags |
| Company estimate around USD 22bn additional CET1; ratio to around 18.5% from around 14% | Regulatory developments | same | S1 | page:89 | CP-1A; CP-2 | Sourced | High | Company estimate |
| Phase-in from 2028 at the earliest, 65% rising by 5 points to 100% | Regulatory developments | same | S1 | page:88 | CP-1A; CP-2 | Sourced | High | Proposal, not law |
| Single point of entry strategy at UBS Group AG | Regulation and supervision | same | S1 | page:84 | CP-1A; CP-2 | Sourced | High | Description of the stated strategy |
| Segment revenue and profit by division | Note 2a | same | S1 | page:409 | CP-1A | Sourced | High | Segment profit sums to 8,853 |
| Revenue by region 36%, 16%, 17%, 32% | Note 2b | same | S1 | page:410 | CP-1A; CP-2 | Sourced | High | Matches |
| Holders above 3%: Norges Bank 4.90% and BlackRock Inc. 5.01% | Significant shareholders | same | S1 | page:262 | CP-1A | Sourced | High | BlackRock notice dated 2023; stale risk noted upstream |
| Debt issued 343,922, 343,551 and 324,981 USD m at the three 2026 quarter-ends | Capitalization of UBS Group AG | S2, S5, S6 | S2, S5, S6 | page:2, page:1, page:1 | CP-1 | Sourced | Medium | Matches; footnote definitions differ |
| Q3 2026 CET1 ratio 14.7%, leverage ratio 4.6%, liquidity coverage 179%, net stable funding 115%, loss-absorbing capacity 187 USD bn | Call remarks | 6-K_2026-09-30_investorpresotext2026.htm.jsonl | S7 | page:5 | CP-1; CP-2 | Management language | Low | Spoken and rounded; averaging basis not stated |
| Q3 2026 reported net profit 2.7 bn, underlying pre-tax profit 4.1 bn, underlying cost / income 68.7% | Call remarks | same | S7 | page:4 | CP-1; CP-2 | Management language | Low | Underlying measures not reconciled |
| Repurchased 4.8 bn year to date; 1.2 bn intended | Call remarks | same | S7 | page:3 | CP-1A; CP-2 | Management language | Low | Spoken |
| Credit Suisse AT1 appeal decision not before Q1 2027 | Q&A | same | S7 | page:14 | CP-1; CP-1A | Management language | Low | Spoken |
| Company estimate also given as around 22 billion plus 15 billion already required | Call remarks | 6-K_2026-03-31_investorpresotext2026.htm.jsonl | S3 | page:4 | CP-1 | Management language | Low | Consistent with S1 page:89 |
| Cumulative gross savings 10.7, 11.5, 12.6, 13.2 bn | Annual report and calls | S1, S3, S4, S7 | S1, S3, S4, S7 | page:41; page:5; page:4; page:4 | CP-1A; CP-2 | Management language | Low | Steps reconcile arithmetically |
| Cost-to-achieve of around 13.7 bn at 1.1 times, and total gross savings of around 13.7 bn | Call remarks | S3, S7 | S3, S7 | page:5; page:5 | CP-1A conflict | Conflicting | Low | Logged upstream, not reconciled |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| CET1 headroom, risk-weighted basis | CP-2 | 71,262 and 52,448 USD m | 71,262 - 52,448 = 18,814 USD m; ratio 14.44% less 10.63% | Calculated | Reproduced | High | PD, LGD | S1 page:229 |
| Going concern and gone concern headroom | CP-2 | 91,176 and 73,955; 96,130 and 52,917 | Differences 17,221 and 43,213 USD m | Calculated | Reproduced | High | PD, LGD | S1 page:229 |
| Leverage-basis headroom (added by this audit) | CP-2 statement that leverage-basis cushions are thinner | CET1 71,262 against 56,785; going concern 91,176 against 81,122 (USD m) | 14,477 and 10,054 USD m, both below 18,814 and 17,221 | Calculated | Direction confirmed | High | PD | S1 page:229 |
| Total loss-absorbing capacity ratio | CP-1 | 91,176 + 96,130 = 187,306 over 493,397 | 37.96%, printed 38.0% | Calculated | Reproduced | High | LGD | S1 page:229, page:37 |
| Debt issued FY2025 | CP-1 | 214,706 + 113,794 | 328,500 against printed 328,501 | Calculated | Reproduced within 1 | High | Leverage | S1 page:432, page:433; S2 page:2 |
| Debt issued FY2024 | CP-1 | 214,219 + 107,909 | 322,128 USD m | Calculated | Reproduced | High | Leverage | S1 page:432, page:433 |
| Debt issued changes in 2026 | CP-1 | 343,922; 343,551; 324,981; 328,501 | +15,421; -371; -18,570; -3,520 USD m | Calculated | Reproduced | High | Refinancing | S2, S5, S6 |
| Debt due within 12 months | CP-1 chart; CP-2 | Amortized cost 9.4, 9.1, 46.8; fair value 14.4, 10.6, 23.4 USD bn | 65.3 and 48.4; total 113.7 USD bn | Calculated | Reproduced; bases noted | Medium | Refinancing | S1 page:497; bucket positions checked in the filed HTML |
| Liquid assets against 12-month debt | CP-2 | 331.6 and 113.7 USD bn | 2.9 times | Calculated | Reproduced; bases differ | Low | Liquidity | S1 page:246, page:497 |
| Deposits share of assets; loans to deposits | CP-1; CP-2 | 788,367; 1,617,427; 653,846 | 48.7% and 82.9% | Calculated | Reproduced | High | Liquidity | S1 page:373 |
| Operating profit growth | CP-2 | 8,853 and 6,821 | 29.8% | Calculated | Reproduced | High | Debt service | S1 page:371 |
| Non-interest share of revenue | CP-1A; CP-2 | 41,826 and 49,573 | 84.4% | Calculated | Reproduced | High | Revenue durability | S1 page:409 |
| Company estimate against group RWA and CET1 | CP-2 | 22,000; 493,397; 71,262 | 4.46 points; 30.9% of CET1; 14 + 4.46 = 18.46 against around 18.5% stated | Calculated | Reproduced; consistent with the company's figure | High | PD | S1 page:89, page:37 |
| Income statement, balance sheet and capitalization footing | CP-1 | Printed totals | Differences of 1 USD m only (revenue lines 49,574 against 49,573; operating profit 8,852 against 8,853; equity 90,483 against 90,484; 31.12.25 capitalization 418,985 against 418,984) | Calculated | Rounding | High | Data quality | S1 page:371, page:373, page:374; S2 page:2 |
| Gross savings path; repurchase arithmetic | CP-1A; CP-2 | 10.7, 0.8, 1.1, 0.6; 3.0, 1.8, 1.2 (USD bn) | 13.2; 6.0 | Calculated | Reproduced; assumption that the first repurchase programme ran within 2026 | Low | Capital returns | S1 page:41; S3 page:5; S4 page:4; S7 page:3 |
| Cost-to-achieve multiple check | CP-1A | 11.5 x 1.1 | 12.65 against a stated 13.7 | Not Calculable | Multiple not defined in the pack | Low | Margin | S3 page:5 |
| EBITDA leverage, interest cover, net debt, facility liquidity | CP-1 | No EBITDA or committed facilities reported | Not applicable to this bank | Not Calculable | Correctly left as Not supplied | High | Not relevant | S1 |

### Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-2 risk table: litigation cash cost and capital use "could exceed provisions" | The filing says litigation effects "may have material adverse consequences"; it gives no amount above provisions, so the comparison with provisions is an inference | Analyst Inference | A reader may take it as a sized exposure; no claim amount exists in the pack, so loss given default cannot be sized | Restate as the filing's wording and keep amounts Not supplied | CP-2 Key credit risks |
| Material | CP-2 liquidity: liquid assets exceed 12-month debt by about 2.9 times | Average liquid assets (a quarterly average) are set against undiscounted contractual debt cash flows that include interest; deposits and other outflows are excluded; the Reader summary omits the caveat | Analyst Inference | Overstates comfort if read as a coverage ratio; refinancing risk is better supported by the liquidity coverage ratio itself | Present the comparison only with its basis, or drop it from the summary | CP-2 Key findings and Reader summary |
| Material | Timing of Swiss rules | The 20-F says ordinance-level changes are not expected to enter into force before January 2027 and foreign subsidiary changes in 2028 at the earliest (S1 page:88); the Q3 call says the ordinance will "start to affect our capital" from 1 January 2029 (S7 page:14). Entry into force and capital effect may differ, but the pack does not say | Conflicting | The date from which capital is needed drives distribution capacity | Keep both statements, with definitions, and ask for the final ordinance | CP-1, CP-2 |
| Minor | CP-1 interest cover note: interest paid in cash "includes deposit interest" | The cash flow line (S1 page:379, page:380) does not state its composition; the inclusion is an inference | Analyst Inference | Affects only a Not supplied metric | Label as inference | CP-1 chart data: interest cover |
| Minor | CP-2: leverage-basis cushions are "thinner" | No dollar amounts were shown; this audit recomputed 14,477 and 10,054 USD m against 18,814 and 17,221 USD m, so the direction holds | Calculated | Direction supported | None beyond adding the amounts | CP-2 Key findings |
| Minor | Q3 2026 liquidity coverage figure beside the fourth-quarter 2025 average | Averaging basis of the 2026 spoken ratios is not stated | Weak Lineage | Comparison of 179% with 182.6% is indicative only | Keep the caveat given in CP-1 | CP-1, CP-2 |
| Minor | Cost-to-achieve and headcount figures | Unreconciled between calls and with the annual report | Conflicting | Not used by CP-2 | Keep logged | CP-1A |
| Minor | Strength wording ("strong", "well-capitalized") | Generic adjectives, but each is tied to ratios in the same paragraph | Analyst Inference | Meets the support-by-evidence test | None | CP-2 Credit view |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Annual report complete in extraction apart from the audit-report pages; 2026 covered only by capitalization tables and call transcripts (S1 page:371; S2 to S7) | Missing interim statements mean 2026 values cannot be tied to statements | Current-period view is indicative only | Supply 2026 quarterly reports and slides |
| Citation completeness | Ready with Remediation | Every number checked appears in the sources; quotes verified verbatim; one table verified against the filed HTML | Residual risk is in the few inferences listed above, not in missing locators | Low impact on committee use | Fix the Material flags |
| Calculation traceability | Committee-Ready | All recomputed; differences of 1 USD m rounding only | Reproducible | No impact | None |
| Assumption transparency | Ready with Remediation | Undiscounted maturity comparison, repurchase programme assumption and management targets are labelled upstream, with one omission in a summary | Reader may over-read a summary line | Minor | Add caveats |
| Markdown and export artifact integrity | Committee-Ready | Four accepted handoffs, hash links match, required headings and selectors present | None observed | No impact | None |

Overall auditability is the lowest of the five: Ready with Remediation.

### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | No 2026 interim statements | Quarterly reports for the first three quarters of 2026 | Current-period earnings, capital and liquidity cannot be tied to statements, so default and liquidity views for 2026 rest on spoken figures | CP-1 Q3 column; CP-2 credit view | High impact | The three quarterly reports |
| CP-5-GAP-002 | No instrument-level debt terms | Prospectus supplements, capital instrument lists, tender documents | Ranking, maturity wall and treatment of the Q3 liability management cannot be traced | CP-2 risks; any ranking statement | High impact | Debt documents |
| CP-5-GAP-003 | Swiss rule text and timing | Proposals, ordinance, parliamentary outcome | The size and date of the capital need rest on the company estimate | CP-2 largest risk | High impact | Rule documents |
| CP-5-GAP-004 | Litigation amounts | Claim amounts, 2026 provision movements | Cash cost beyond provisions unknown | CP-2 risks | Medium impact | Litigation notes and filings |
| CP-5-GAP-005 | Ratings in force | Agency reports | Funding cost and collateral triggers | CP-2 | Medium impact | Rating agency reports |
| CP-5-GAP-006 | Audit opinion text absent from extraction | Auditor reports (S1 page:371) | Opinion wording cannot be quoted | CP-1 | Low impact | Full filed document |
| CP-5-GAP-007 | Underlying measure reconciliations | Quarterly reports and slides | Underlying ratios are not comparable with reported ratios | CP-1, CP-2 | Medium impact | Quarterly reports and slides |
| CP-5-GAP-008 | Events 30 October to 5 November 2026 | Later filings | Latest source is dated 29 October 2026 | All | Low impact | Later 6-Ks |

### Verification performed

- Locators: every `page:N` cited in the four handoffs was opened in the pinned text and the cited figure or wording found there. No wrong locator was found.
- Numbers: every comma-formatted number and every decimal in the three analytical handoffs was searched in the sources. The only numbers not found were derived values: a sum of two reported debt lines (322,128), 12-month fair value sums (48,400 and 51,900), a combined 12-month sum (113.7), headroom differences (17,221 and 43,213), an increase in assets (52,399) and a per-share figure spoken as cents (0.85). This audit recomputed each of them.
- Quotes: every quoted phrase in the handoffs was matched verbatim to the sources after whitespace and apostrophe normalisation.
- Flattened table risk: the fair value debt row in the maturity table (page:497, page:498) has six buckets printed for seven columns, so the position of each number is not visible in the extracted text. The original filed HTML marks each figure with its maturity context; this confirmed 14.4, 10.6 and 23.4 for up to one month, one to three months and three months to one year, and 12.1, 11.7 and 28.1 for FY2024. The 12-month sums used upstream are therefore correct.
- Cross-module: the CP-1 correction of CP-0 on the Credit Suisse (USA) LLC guarantee is supported (S1 page:433). CP-1A and CP-2 use CP-1 figures consistently. Handoff hashes are correct in each Sources section.

## Calculations

| Id | Calculation | Inputs | Result | Check |
| --- | --- | --- | --- | --- |
| C1 | CET1 headroom, risk-weighted basis | 71,262 - 52,448 | 18,814 USD m | Matches CP-2 |
| C2 | Going concern headroom, risk-weighted basis | 91,176 - 73,955 | 17,221 USD m | Matches CP-2 |
| C3 | Gone concern headroom | 96,130 - 52,917 | 43,213 USD m | Matches CP-2 |
| C4 | CET1 headroom, leverage basis | 71,262 - 56,785 | 14,477 USD m | Not shown upstream; below C1 |
| C5 | Going concern headroom, leverage basis | 91,176 - 81,122 | 10,054 USD m | Not shown upstream; below C2 |
| C6 | Total loss-absorbing capacity ratio | (91,176 + 96,130) / 493,397 | 37.96% | Matches printed 38.0% |
| C7 | Debt due within 12 months, FY2025 | 9.4 + 9.1 + 46.8 + 14.4 + 10.6 + 23.4 | 113.7 USD bn | Matches CP-2 |
| C8 | Liquid assets against that debt | 331.6 / 113.7 | 2.92 times | Matches CP-2; bases differ |
| C9 | Company estimate in ratio terms | 22,000 / 493,397 | 4.46 points | 14 + 4.46 = 18.46, consistent with around 18.5% |
| C10 | Debt issued FY2025 and FY2024 | 214,706 + 113,794; 214,219 + 107,909 | 328,500 and 322,128 USD m | Matches CP-1 |
| C11 | Q3 2026 change in debt issued | 324,981 - 343,551 | -18,570 USD m | Matches CP-1 |
| C12 | Operating profit growth | (8,853 - 6,821) / 6,821 | 29.8% | Matches CP-2 |
| C13 | Non-interest share | 41,826 / 49,573 | 84.4% | Matches CP-1A and CP-2 |

Not calculable: a numeric confidence score (scoring script not part of this run), any EBITDA-based metric, and any recovery measure.

## Gaps

| Gap | Severity | Affected modules | Remediation |
| --- | --- | --- | --- |
| 2026 interim statements and slides not supplied; third-quarter figures are spoken and rounded | Critical for any decision relying on 2026 figures | CP-1, CP-2 | Supply the three quarterly reports and slides |
| Instrument-level debt terms and Q3 2026 liability management terms not supplied | Critical for ranking and maturity questions | CP-2 | Supply debt documents |
| Swiss rule text and the timing difference between the 20-F and the Q3 call | Material | CP-1, CP-2 | Supply the proposals and ordinance; keep both statements |
| Two caveats missing in CP-2 (litigation comparison, liquidity comparison) | Material | CP-2 | Add caveats; the ratios beside them are unaffected |
| Ratings in force, litigation amounts, audit opinion text, events after 29 October 2026 | Material to Minor | CP-1, CP-2 | See the gaps ledger |

Committee status: Restricted. The audited year-end 2025 base, the capital and funding figures and the company's Swiss capital estimate may be used with their stated limits. Current-period earnings, debt ranking, maturity wall and litigation exposure beyond provisions may not.

## Next module

- No further module is selected in this run. For the report, carry the Restricted committee status, the two Material caveats, the unreconciled timing difference and the critical gaps ledger entries, and label every third-quarter 2026 figure as spoken and rounded.
