## Request

Evidence trace validation and research integrity grade for Brightstar Lottery PLC (issuer id brsl), as of 2026-11-05, pathway credit snapshot, run brsl-2026-11-05-credit_snapshot-host. Scope: the four upstream handoffs (source readiness, financial base, business and transaction context, fundamental credit synthesis), with the default scope of the five most material credit drivers plus the overall credit view. The quoted spans, locators and calculations of those handoffs were checked directly against the seven pinned issuer sources.

## Sources

### Issuer sources relied on

| Source ID | Source file (exact name) | sha256 |
| --- | --- | --- |
| S1 | 20-F_2025-12-31_igt-20251231.htm.jsonl | 1c18bf53e9995ce6c2aca12af6c18a64523551fba3492e8f989685fea08386fa |
| S2 | 6-K_2025-09-30_brightstar-9302025xform6k.htm.jsonl | d46e904b239bdfcdf629b7154b5f837586e94b09f3d9adb6cf2a3a22cad2c307 |
| S3 | 6-K_2026-03-31_brightstar-3312026xform6k.htm.jsonl | bd68ab805934e86ab47882d408ef93ab3b6ce1b76f45e4a9303ec66c324fbd07 |
| S4 | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 59ad2951e3fb4482f8541a5bd23eebbb988b008e57b642801a0675f3dc319de2 |
| S5 | 6-K-EX-99.2_2025-12-31_q425earningsslidedeck-fi.htm.jsonl | 52d9fd83276756c04d4933b539c2d599c1b0335f475eb7ae194b8d0285bb64ab |
| S6 | 6-K-EX-99.2_2026-03-31_q126earningsslidedeckfin.htm.jsonl | 904bf049bdca8cf2ecdea2a5b2e5271032b7a15662b32cecb7e8b6ac25de48c2 |
| S7 | 6-K-EX-99.2_2026-06-30_q226earningsslidedeck-fi.htm.jsonl | 2e4571f9e2637bd424291bf68428c53b010290fd8734caabd6c6df90116096fc |

### Run settings (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context | 5dec6fdc4bf237796c486a0095b8a59b71b216970050467cf9aed314b06e0f82 |

### Handoffs

| Module | Handoff | sha256 |
| --- | --- | --- |
| CP-0 | Source readiness for Brightstar Lottery PLC | 2272d9d74d9d7f19568da51f3a2c80f84dc9432a75a7be1a1d26161cd2bf1768 |
| CP-1 | Financial base for Brightstar Lottery PLC | 015c9f0c9127b25cc24bccb61512f935749a711ecf6358ec0969afa9d5638e98 |
| CP-1A | Business and transaction context for Brightstar Lottery PLC | bd41dca444592f424dda19a173946b1e08731a7ff8d270b7df85782fc76befe7 |
| CP-2 | Fundamental credit synthesis for Brightstar Lottery PLC | 039f8c28387a2721495bbf276cca2d5ac3fb036a8f8f33357da1a5407c27bdfb |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis is traceable enough for a draft snapshot: every checked quotation matches its source and every ratio recomputes. Five minor defects were found; none changes the credit view. | Low | Covenant levels, license agreements and filings after August 4, 2026 are not supplied, so the score stays low. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 130 quoted spans in the three handoffs that quote sources were found in the pinned sources; one was cited to the wrong page. | Figures can be relied on as quoted from filings and presentations. | High |
| Every derived ratio was recomputed from its inputs, including 3.24x, 4.48x and 6.09x, and all matched. | Leverage and cover figures are reproducible from stated inputs. | High |
| Adjusted EBITDA, net debt and net debt leverage rest on management presentations and not on filed statements. | Leverage conclusions carry management-measure risk. | Medium |
| The 9 difference in December 31, 2025 net debt comes from two carrying amounts in the annual report. | The 2.44x figure is unaffected at the stated precision. | High |
| Claims on covenant headroom, license renewal terms and distribution caps cannot be traced because the documents are not supplied. | These topics stay open until the documents are obtained. | High |

### Evidence trace view

The analysis is traceable enough for a draft snapshot, with five minor defects and no material or critical one. Of 130 quoted spans in the three handoffs that quote the sources, every span was found in the pinned sources, and one locator pointed to the wrong page; every derived ratio was recomputed from its inputs and matched. The strongest support is that leverage inputs, liquidity, maturities and ownership come from filed statements. The weakest point is that Adjusted EBITDA, net debt and net debt leverage come only from management presentations. What decides committee use is whether covenant levels, license agreements and any filing after August 4, 2026 can be obtained, because the renewal, distribution-cap and covenant-headroom conclusions cannot be traced without them.

### Traceability conclusion

Confidence Score: 47 / 100 (band Low). qa_status: Passed. committee_status: Draft Only. Clearance decision: Pass with Remediation, with no unresolved Critical or Material issue. The score is script-computed from lineage counts of eight material claims (3 Directly Sourced, 3 Calculated, 2 Analyst Inference), a partial source gate because the source package is incomplete, all 17 required registers present and five Minor findings; its working is in the calculations section. The score is low because of the incomplete source package and not because of a traced defect. Ratings, covenant levels and later filings are the follow-ups that would raise it.

### Traceability summary

| Measure | Result |
| --- | --- |
| Quoted spans checked | 130, all found in the pinned sources |
| Locators wrong | 1 (CP-0) |
| Derived figures recomputed | 31, all matched |
| Cross-module conflicts logged | 5 |
| Issues | 0 Critical, 0 Material, 5 Minor |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register and module status

Module status: Ready with Limitations. All four upstream handoffs and the seven sources are available; the source package lacks covenant documents, license agreements and any filing after August 4, 2026. Entity key: issuer_id brsl is available. Traceability scope: Top 5 drivers plus the overall credit view.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 20-F_2025-12-31_igt-20251231.htm.jsonl | Filed annual report, audited | Year ended December 31, 2025 (with 2024 comparatives) | Brightstar Lottery PLC consolidated, US GAAP | Statements, debt note, leases, ownership, business and risk text | Exhibits and organization diagram not read | Financial base, business context, synthesis |
| S2 | 6-K_2025-09-30_brightstar-9302025xform6k.htm.jsonl | Filed interim report, unaudited | Quarter and nine months ended September 30, 2025 | Brightstar Lottery PLC consolidated | Interim statements and notes | No figure from it is used in the handoffs | Context only |
| S3 | 6-K_2026-03-31_brightstar-3312026xform6k.htm.jsonl | Filed interim report, unaudited | Quarter ended March 31, 2026 | Brightstar Lottery PLC consolidated | March 31, 2026 balance sheet, debt, liquidity, cash interest | Unaudited | Financial base, leverage at March 31, 2026 |
| S4 | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | Filed interim report, unaudited | Quarter and six months ended June 30, 2026 | Brightstar Lottery PLC consolidated | Latest statements, debt, liquidity, subsequent events | Unaudited; latest evidence is August 4, 2026 | All four handoffs |
| S5 | 6-K-EX-99.2_2025-12-31_q425earningsslidedeck-fi.htm.jsonl | Management presentation (text extract) | Q4 and FY2025 | Brightstar Lottery PLC continuing operations | FY2025 Adjusted EBITDA, geography | Management non-GAAP; charts not inspected | Leverage denominator, regional mix |
| S6 | 6-K-EX-99.2_2026-03-31_q126earningsslidedeckfin.htm.jsonl | Management presentation (text extract) | Q1 2026 | Brightstar Lottery PLC continuing operations | Q1 Adjusted EBITDA, Lotto share, pro forma leverage claim | Management non-GAAP; charts not inspected | LTM EBITDA at March 31, 2026 |
| S7 | 6-K-EX-99.2_2026-06-30_q226earningsslidedeck-fi.htm.jsonl | Management presentation (text extract) | Q2 and H1 2026 | Brightstar Lottery PLC continuing operations | H1 Adjusted EBITDA, net debt leverage, outlook | Management non-GAAP; forward-looking | LTM EBITDA at June 30, 2026, leverage check |

#### T5B.2 Top five material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Net leverage of 3.24x, or 4.48x without the license-fee add-back | CP-1, CP-2 | Debt and cash from S4; Adjusted EBITDA from S5 and S7 | Sets leverage tolerance and debt service capacity | Primary financial risk metric | S4 page:3, page:14; S5 page:10; S7 page:10 | EBITDA is a management measure; covenant EBITDA not supplied |
| 2 | Liquidity of USD 1,742 million and a first maturity of USD 228 million in 2027 | CP-1, CP-2 | Liquidity table and maturity table in S4 | Determines near-term refinancing risk | Shows two years of room | S4 page:14, page:27 | Letters of credit on the new revolver not stated |
| 3 | Cash flow after the Lotto license payments and partner distributions | CP-1, CP-2 | Cash flow statements in S1 and S4 | Determines debt reduction capacity | Free cash flow excluding Lotto payments of USD 387 million | S1 page:139; S4 page:5 | Last twelve months built from three periods |
| 4 | Italian license concentration and the Scratch and Win expiry in 2028 | CP-1A, CP-2 | Risk factor and business text in S1 | Revenue and refinancing event risk | About 37% of revenue under two licenses | S1 page:9, page:40, page:47 | Renewal terms not supplied |
| 5 | Control by De Agostini and partner claims on cash flow | CP-1A, CP-2 | Ownership and organization text in S1 | Distribution policy and cash leakage | 63.28% of votes; 61.5% ownership of the Lotto manager | S1 page:40, page:90, page:91; S4 page:5 | Distribution cap text after March 2026 not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net leverage 3.24x at June 30, 2026 | CP-1 | Debt 4,354 less cash 558 over LTM Adjusted EBITDA 1,170 | Yes | Filed statements plus management presentation | Calculated | Supported | High | Traced to S4 page:3, page:14 and S5, S7 page:10 |
| Liquidity of USD 1,742 million and no maturity before 2027 | CP-1 | Liquidity table and maturity table | Yes | Filed interim report | Directly Sourced | Supported | High | Traced to S4 page:14, page:27 |
| Free cash flow excluding Lotto payments of USD 387 million, last twelve months | CP-1, CP-2 | Operating cash flow, capex and Lotto payments | Yes | Filed statements | Calculated | Supported | Medium | Traced to S1 page:139 and S4 page:5 |
| Italian licenses about 37% of revenue; Scratch and Win expires September 2028 | CP-1A | Risk factor percentages and license term | Yes | Filed annual report | Directly Sourced | Supported | High | Traced to S1 page:9, page:40 |
| De Agostini 63.28% of votes; Lotto manager 61.5% owned | CP-1A | Ownership table and business text | Yes | Filed annual report | Directly Sourced | Supported | High | Traced to S1 page:40, page:90 |
| EBITDA quality: leverage without the license-fee add-back is 4.48x | CP-1, CP-2 | Add-back 323 and EBITDA 1,170 | Yes | Filed statements plus management presentation | Calculated | Supported | Medium | Traced to S4 page:5; S7 page:10 |
| Renewal funding could coincide with USD 798 million of 2028 maturities | CP-2 | Scratch and Win expiry, Lotto fee and 2028 maturity | Yes (basis rows) | Filed report plus analyst reading | Analyst Inference | Partially Supported | Low | Mechanic stated as a mechanic; renewal terms not in evidence |
| Overall view: adequate profile with limited headroom | CP-2 | Synthesis of the rows above | Yes (handoff references) | Analyst synthesis | Analyst Inference | Supported by the cited drivers | Medium | Rests on drivers 1 to 5 |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| "Long-term debt, less current portion 8 4,354 4,060" | source-text/6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | S4 | page:3 | CP-1 leverage | Source Fact | Filed, unaudited | Matches the handoff |
| "Cash and cash equivalents 558 1,446" | source-text/6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | S4 | page:3 | CP-1 leverage | Source Fact | Filed, unaudited | Matches the handoff |
| "Total debt 4,383 (29) 4,354 4,203 (25) 4,178" | source-text/6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | S4 | page:14 | CP-1 debt table | Source Fact | Filed, unaudited | Principal and carrying value |
| "Total principal amounts 1,500 2,883 4,383" | source-text/6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | S4 | page:14 | CP-1 maturities | Source Fact | Filed, unaudited | Currency split used in CP-2 |
| "Total Liquidity 1,742 3,036" | source-text/6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | S4 | page:27 | CP-1 liquidity | Source Fact | Filed, unaudited | Components sum to 1,743 by rounding |
| "Revolving Credit Facilities (1) 1,185 1,590" | source-text/6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | S4 | page:27 | CP-1 liquidity | Source Fact | Filed, unaudited | Undrawn committed facilities |
| "Adjusted EBITDA 286 274 573 524" | source-text/6-K-EX-99.2_2026-06-30_q226earningsslidedeck-fi.htm.jsonl | 6-K-EX-99.2_2026-06-30_q226earningsslidedeck-fi.htm.jsonl | S7 | page:10 | CP-1 EBITDA | Management Language | Management presentation | Not in any filed statement |
| "Adjusted EBITDA 304 290 1,121 1,170" | source-text/6-K-EX-99.2_2025-12-31_q425earningsslidedeck-fi.htm.jsonl | 6-K-EX-99.2_2025-12-31_q425earningsslidedeck-fi.htm.jsonl | S5 | page:10 | CP-1 EBITDA | Management Language | Management presentation | CP-0 cites page:8; the contiguous span is on page:10 |
| "Net debt leverage* 3.24x" | source-text/6-K-EX-99.2_2026-06-30_q226earningsslidedeck-fi.htm.jsonl | 6-K-EX-99.2_2026-06-30_q226earningsslidedeck-fi.htm.jsonl | S7 | page:6 | CP-1 leverage check | Management Language | Management presentation | Equals the recomputed ratio |
| "Interest paid 213 221 208" | source-text/20-F_2025-12-31_igt-20251231.htm.jsonl | 20-F_2025-12-31_igt-20251231.htm.jsonl | S1 | page:140 | CP-1 interest cover | Source Fact | Filed, audited | Continuing operations |
| "Interest paid 68 89" | source-text/6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | S4 | page:6 | CP-1 interest cover | Source Fact | Filed, unaudited | Six months 2026 and 2025 |
| "Italian Lotto License payment (1,675)" | source-text/6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | S4 | page:5 | CP-1 cash flow | Source Fact | Filed, unaudited | Operating cash flow line |
| "Capital increase - non-controlling interests 650 178" | source-text/6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | S4 | page:5 | CP-1A partner funding | Source Fact | Filed, unaudited | Link to the Lotto payment is an inference |
| "Lottoitalia is 61.5% owned by Brightstar Lottery S.p.A." | source-text/20-F_2025-12-31_igt-20251231.htm.jsonl | 20-F_2025-12-31_igt-20251231.htm.jsonl | S1 | page:40 | CP-1A, CP-2 ownership | Source Fact | Filed, audited year | Corrects CP-0 |
| "De Agostini S.p.A. 85,422,324 46.29% 85,422,324 63.28%" | source-text/20-F_2025-12-31_igt-20251231.htm.jsonl | 20-F_2025-12-31_igt-20251231.htm.jsonl | S1 | page:90 | CP-1A, CP-2 control | Source Fact | Filed, as of February 19, 2026 | Dec 31, 2025 figures differ by date |
| "approximately 18%, at both periods" | source-text/20-F_2025-12-31_igt-20251231.htm.jsonl | 20-F_2025-12-31_igt-20251231.htm.jsonl | S1 | page:9 | CP-1A concentration | Source Fact | Filed, audited year | Lotto share; Scratch and Win share is in the same passage |
| "for a term expiring in September 2028" | source-text/20-F_2025-12-31_igt-20251231.htm.jsonl | 20-F_2025-12-31_igt-20251231.htm.jsonl | S1 | page:40 | CP-1A, CP-2 renewal | Source Fact | Filed, audited year | Future date |
| "equal to approximately 92% of its total consolidated revenues" | source-text/20-F_2025-12-31_igt-20251231.htm.jsonl | 20-F_2025-12-31_igt-20251231.htm.jsonl | S1 | page:10 | CP-1A, CP-2 contract share | Source Fact | Filed, audited year | Share of FY2025 revenue |
| "The carrying amount of long-term debt was $4,169 million and $5,361 million" | source-text/20-F_2025-12-31_igt-20251231.htm.jsonl | 20-F_2025-12-31_igt-20251231.htm.jsonl | S1 | page:164 | CP-1A conflicts | Source Fact | Filed, audited | 9 below the debt note total of 4,178 |
| "The RCF Agreement contains a maximum net leverage ratio covenant" | source-text/6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | S4 | page:15 | CP-1 covenants | Source Fact | Filed, unaudited | No threshold printed |
| "limits the aggregate amount that the Parent can pay with respect to dividends and repurchases of ordinary shares in each year" | source-text/20-F_2025-12-31_igt-20251231.htm.jsonl | 20-F_2025-12-31_igt-20251231.htm.jsonl | S1 | page:171 | CP-1A, CP-2 distribution cap | Source Fact | Filed, audited year | Terms at December 31, 2025 only |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA, June 30, 2026 | CP-1, CP-2 | 1,121; 573; 524 | FY2025 + H1 2026 - H1 2025 = 1,170 | Recomputed, matches | Supported | Medium | Leverage and cover denominator | S5 page:10; S7 page:10 |
| LTM Adjusted EBITDA, March 31, 2026 | CP-1 | 1,121; 287; 250 | 1,121 + 287 - 250 = 1,158 | Recomputed, matches | Supported | Medium | Leverage at March 31, 2026 | S5 page:10; S6 page:7 |
| Net debt, June 30, 2026 | CP-1, CP-2 | Carrying debt 4,354; cash 558 | 4,354 - 558 = 3,796 | Recomputed, matches | Supported | High | Leverage numerator | S4 page:3, page:14 |
| Net debt / LTM Adjusted EBITDA, June 30, 2026 | CP-1, CP-2 | 3,796; 1,170 | 3,796 / 1,170 = 3.24x | Recomputed, matches the deck figure | Supported | Medium | Primary leverage metric | S7 page:6 |
| Net debt, December 31, 2025 | CP-1 | Carrying debt 4,178; cash 1,446 | 4,178 - 1,446 = 2,732 | Recomputed; deck prints 2,723 (4,169 - 1,446) | Supported with a logged conflict | Medium | Prior leverage point of 2.44x | S1 page:164, page:168 |
| Total debt / EBITDA, June 30, 2026 | CP-1, CP-2 | 4,354; 1,170 | 4,354 / 1,170 = 3.72x | Recomputed, matches | Supported | Medium | Gross leverage | S4 page:14 |
| LTM cash interest and cover, June 30, 2026 | CP-1, CP-2 | 213; 68; 89; 1,170 | (213 + 68 - 89) = 192; 1,170 / 192 = 6.09x | Recomputed, matches | Supported | Medium | Interest cover | S1 page:140; S4 page:6 |
| LTM license-fee add-back | CP-1, CP-2 | 223; 201; 101 | 223 + 201 - 101 = 323 | Recomputed, matches | Supported | High | EBITDA quality | S1 page:139; S4 page:5 |
| Leverage without the add-back | CP-1, CP-2 | 3,796; 1,170; 323 | 3,796 / (1,170 - 323) = 4.48x | Recomputed, matches; analyst sensitivity | Supported | Medium | Cash-oriented leverage | Derived from the rows above |
| LTM free cash flow excluding Lotto payments | CP-1, CP-2 | CFO -193, -1,174, 473; Lotto 926, 1,675; capex 316, 232, 174 | (733 + 501 - 473) - (316 + 232 - 174) = 387 | Recomputed, matches | Supported | Medium | Debt reduction capacity | S1 page:139; S4 page:5 |
| Free cash flow after partner distributions, last twelve months | CP-2 | 387; 163 | 387 - 163 = 224 | Recomputed, matches | Supported | Medium | Capacity after partners | S4 page:5 |
| Liquidity cover of 2027 and 2028 maturities | CP-2 | 1,742; 228; 798 | 1,742 / (228 + 798) = 1.70x | Recomputed, matches | Supported | High | Near-term refinancing cover | S4 page:14, page:27 |
| 2028 to 2030 principal | CP-2 | 798; 978; 1,025 | Sum = 2,801; 2,801 / 4,383 = 63.9% | Recomputed, matches | Supported | High | Refinancing window | S4 page:14 |
| Like-for-like leverage | CP-1, CP-2 | 2,732; 1,680; 1,121; 3,796; 1,170 | (2,732 + 1,680) / 1,121 = 3.94x; 3,796 / 1,170 = 3.24x | Recomputed, matches | Supported | Medium | Shows the headline rise is mostly settlement of a payable | S1 page:137; S4 page:3 |
| Revolver reconciliation | CP-1 | 650; 1,139; 604 | 650 + 1,139 - 604 = 1,185 | Recomputed; assumption that the euro term loan principal equals the dollar value of EUR 1.0 billion | Assumption-Based, labelled in CP-1 | Medium | Suggests no letters of credit deduction | S4 page:14, page:27 |
| Regional revenue shares FY2025 | CP-1A | 1,176; 1,018; 317; 2,511 | Each over 2,511 = 46.8%, 40.5%, 12.6% | Recomputed, matches | Supported | High | Geographic mix | S5 page:8; S1 page:138 |
| Brightstar share of final Lotto installment | CP-1A | 879; 1,430 | 879 / 1,430 = 61.5% | Recomputed, matches | Supported | High | Equals stated ownership | S6 page:6; S4 page:12 |
| Shareholder returns since July 1, 2025 | CP-1A, CP-2 | 770; 81; 271; 85; 45 | (770 - 81) + 271 + 85 + 45 = 1,090 | Recomputed, matches | Supported | Medium | Distribution pace | S1 page:139; S4 page:5 |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | Adjusted EBITDA FY2025 of 1,121 | CP-0 cites the contiguous span to the Q4 deck page:8; it appears on page:10 (page:8 holds the same figures with percentage changes between them) | Citation Gap | Wrong page weakens the trace | Cite page:10 | CP-0 source assessment; value unchanged |
| MINOR | Shareholder returns of USD 1,090 million funded by the sale | CP-2 calls the USD 600 million special dividend funded from the sale without labelling the 600 as a presentation figure or the funding link as an inference | Management Language carried without label | A management figure and an inferred funding link read as filed fact | Label as a deck figure and as Analyst Inference | CP-2 key findings |
| MINOR | Behaviour category | CP-1A states Supportive or Neutral or Mixed rather than one category | Classification imprecision | The scoring dimension cannot be set from a range | State one category: Neutral or Mixed on the documented behaviour | CP-1A governance table |
| MINOR | Chart cell of 0 for the remainder of 2026 | A dash in the maturity table is shown as 0 to satisfy the numeric chart cell; CP-1 annotates it as a printed dash | Null rendered as zero, annotated | A false zero breaks a chain unless annotated | Keep the annotation | CP-1 maturity chart data |
| MINOR | Leverage on Adjusted EBITDA | The ratio denominator comes only from presentations | Management Language, disclosed | Not a filed measure | Obtain covenant EBITDA | CP-1 leverage chart data |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Locator precision | Strong | Of 99 quoted spans with an adjacent locator, 98 sit on the cited page; one is on another page | A wrong page slows verification but not the figure | None on the credit view | Correct CP-0 locator |
| Quote fidelity | Strong | All 130 spans found verbatim in the pinned sources | None found | None | None |
| Calculation reproducibility | Strong | 31 derived figures recomputed from printed inputs | None found | Leverage and cover can be relied on as stated | None |
| Management versus filed lineage | Adequate | Adjusted EBITDA, net debt and leverage only in S5, S6 and S7 | A management measure could differ from covenant EBITDA | Leverage tolerance may differ from lender tests | Obtain covenant definitions |
| Cross-module consistency | Adequate | Five conflicts logged; none changes a conclusion | Earlier handoffs cannot be edited | Corrections carried in later handoffs | None beyond the log |
| Subsequent events and cut-off | Strong | Events after June 30, 2026 are dated and separated; nothing after August 4, 2026 is used | Blending would misstate period figures | None | None |
| Perimeter and period labels | Strong | Continuing operations, LTM construction and currency stated | Mixing discontinued operations would distort leverage | None | None |
| Legal and covenant claims | Limited | Covenant types named, no thresholds; no clause-level source | Headroom cannot be traced | Monitoring posture is limited | Obtain agreements |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant levels and covenant EBITDA | Revolver and term loan agreements | Headroom decides default risk | Headroom Not calculable | Source gate partial | Credit agreements |
| G2 | Filings after August 4, 2026 | Third-quarter 2026 report and deck | Latest leverage and liquidity | Balance sheet is June 30, 2026 | Source gate partial | Latest 6-K |
| G3 | Italian Lotto concession, consortium agreements, Scratch and Win renewal terms | License and shareholder agreements | Renewal funding and partner cash claims | 2028 mechanic remains an inference | Analyst Inference claims stay at Low | Issuer or registry |
| G4 | Distribution cap after the March 2026 amendment, guarantor list, indentures | Amended term loan, indentures | Creditor protection against distributions | Cap stated for December 31, 2025 only | Caps cannot be confirmed | Debt documents |
| G5 | Ratings after December 31, 2025 | Agency reports | Rating-linked pricing and caps | Ratings dated December 31, 2025 | Minor | Agency reports |
| G6 | Deck charts and the organization diagram not inspected | Images of slides and the structure chart | Chart-only content is untraced | Filed tables used instead | Minor | Source images |

#### T5.1 Module and handoff register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 response, sha256 2272d9d74d9d7f19568da51f3a2c80f84dc9432a75a7be1a1d26161cd2bf1768; run brsl-2026-11-05-credit_snapshot-host | Source readiness, seven sources | Filed statements and presentations | Six canonical H2 headings present; no YAML envelope under host transport | Passed with one Minor finding | One wrong page locator |
| CP-1 | requests/CP-1 response, sha256 015c9f0c9127b25cc24bccb61512f935749a711ecf6358ec0969afa9d5638e98; same run | Financial base, FY2024 to LTM June 30, 2026 | Filed statements, management EBITDA | Six canonical H2 headings present; no YAML envelope | Passed with one Minor finding | Net debt difference later explained |
| CP-1A | requests/CP-1A response, sha256 bd41dca444592f424dda19a173946b1e08731a7ff8d270b7df85782fc76befe7; same run | Business, ownership, transactions, timeline | Filed annual report, interim reports | Six canonical H2 headings present; no YAML envelope | Passed with one Minor finding | Behaviour category imprecise |
| CP-2 | requests/CP-2 response, sha256 039f8c28387a2721495bbf276cca2d5ac3fb036a8f8f33357da1a5407c27bdfb; same run | Fundamental credit synthesis | Handoffs only | Six canonical H2 headings present; no YAML envelope | Passed with one Minor finding | Unlabelled management figure |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 | Source assessment: FY2025 Adjusted EBITDA "Adjusted EBITDA 304 290 1,121 1,170" cited to Q4 deck page:8 | Partially Supported | The span is on page:10 | Cite page:10 | Formatting / Hygiene Only |
| MINOR | CP-2 | Key findings: shareholder returns of USD 1,090 million including the USD 600 million special dividend funded from the sale of the gaming business | Partially Supported | The 600 is a presentation figure and the funding link is an inference, neither labelled | Label as Management Language and Analyst Inference | Monitoring Follow-Up |
| MINOR | CP-1A | Governance table: stake rose between the two dates as shares were repurchased | Supported | Arithmetic supports it (85,422,324 shares over fewer outstanding shares) but the row does not mark it as an inference | Mark as Analyst Interpretation | Formatting / Hygiene Only |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Net debt at December 31, 2025 stated as 2,732 | Uses the debt note total of 4,178; the deck uses 4,169 from the fair value note | 20-F page:164 (4,169) against page:168 (4,178) | Keep the balance sheet basis and cite both | Monitoring Follow-Up |
| MINOR | CP-1 | Total debt / EBITDA on carrying value | Principal basis gives a slightly higher ratio (3.75x at June 30, 2026) | None | State the basis, as CP-1 does | Formatting / Hygiene Only |
| MINOR | CP-1 | LTM construction mixes FY2025 (S5) with H1 comparatives (S7) | Consistent: H1 2025 of 524 less Q1 2025 of 250 equals the Q2 2025 figure of 274 printed in S7 | None | None | Monitoring Follow-Up |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | Notes are senior secured, guaranteed by certain subsidiaries and secured on shares of Brightstar Lottery S.p.A.; no ranking or recovery view is stated | Indentures, credit agreements, security and intercreditor documents | Descriptions come from the notes to the statements, not from clauses | Keep to description; obtain documents before any ranking statement | Required before any ranking or recovery conclusion |

#### T5.5 Market and relative value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A, CP-2 | No price, spread, yield or relative value is claimed; ratings at December 31, 2025 are quoted from the annual report | Current prices, spreads and ratings | None for the claims made | None for this snapshot | No effect on this snapshot; required before relative value work |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A | Net debt at December 31, 2025: 2,732 against the deck figure 2,723 | CP-1 left it unexplained; CP-1A explains it with the annual report carrying amount of 4,169 | None; correction carried in CP-1A | None on 2.44x at the stated precision |
| MINOR | CP-0, CP-1A | Lotto manager ownership: CP-0 said not located; CP-1A found 61.5% | Earlier handoff cannot be edited | None; correction carried in CP-1A | CP-2 uses 61.5% correctly |
| MINOR | CP-1, CP-1A | Final Lotto installment shown as 1,680, 1,675, USD 1.68 billion and USD 1.67 billion | Different dates and translation rates; each figure is used for its own date | None | None |
| MINOR | CP-1A | De Agostini stake 62.7% of votes at December 31, 2025 and 63.28% at February 19, 2026 | Different dates, not a restatement | None | CP-2 uses 63.28% with the date implied |
| MINOR | CP-1, CP-1A | Co-issuer of the 5.750% notes named two ways in the annual report | Source naming conflict preserved in both handoffs | Resolve with the indenture | None on figures |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Duplicative content | The credit view, reader summary and key findings repeat the leverage and liquidity figures | Keep; the reader summary is required to restate | None |
| MINOR | CP-1, CP-1A | Duplicative content | The Italian Lotto payment history appears in both handoffs | Keep; each serves its own consumer | None |
| MINOR | CP-1A | Promotional language | Deck statements are tagged Management Language | None | None |

#### T5.8 Handoff envelope and export integrity

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | YAML front matter, filename convention, run fields | Not carried because host mode transports plain Markdown with six H2 headings | None; transport is defined by CP-OS | None; CP-OS owns identity, hashes and ordering |
| MINOR | CP-1, CP-1A | Selector sections | Required selector headings are present once each | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MINOR | CP-0 | Citation Gap | Adjusted EBITDA reconciliation cited to Q4 deck page:8; it is on page:10 | Cite page:10 | Formatting / Hygiene Only | Open |
| CP5-002 | MINOR | CP-1 | Conflicting Evidence | December 31, 2025 net debt difference of 9 unexplained in CP-1 | None; explained in CP-1A from the annual report | Monitoring Follow-Up | Resolved by later handoff |
| CP5-003 | MINOR | CP-0 | Version Conflict | Lotto manager ownership said not located; 61.5% is stated in the annual report | None; corrected in CP-1A | Monitoring Follow-Up | Resolved by later handoff |
| CP5-004 | MINOR | CP-2 | Partially Supported Claim | Special dividend figure and funding link carried without labels | Label as Management Language and Analyst Inference | Monitoring Follow-Up | Open |
| CP5-005 | MINOR | CP-1A | Formula / Definition Drift | Behaviour category given as a range | State one category | Formatting / Hygiene Only | Open |

## Calculations

Recomputation was done from printed inputs in the sources; every value in the calculation register above matched the handoff value. The checks counted 130 quoted spans (CP-0: 42, CP-1: 10, CP-1A: 78; CP-2 quotes no source) and 31 derived figures.

| Calculation | Inputs | Result |
| --- | --- | --- |
| Confidence score | E = (3 x 1.0 + 3 x 0.9 + 2 x 0.4) / 8 x 100 = 81.25; C = 17 / 17 x 100 = 100; S = 0.7 (partial source gate); P = 5 x 3 = 15 | (0.6 x 81.25 + 0.4 x 100) x 0.7 - 15 = 47.12, rounded to 47; band Low; qa_status Passed (no Critical or Material finding) |
| Principal basis leverage, June 30, 2026 | 4,383 / 1,170 | 3.75x, against 3.72x on carrying value |
| Net debt on the fair value note carrying amount, December 31, 2025 | 4,169 - 1,446 | 2,723, equal to the deck figure |

## Gaps

| Gap | Severity | Effect |
| --- | --- | --- |
| Covenant levels and covenant EBITDA not supplied | MATERIAL for monitoring, not a defect | Headroom claims cannot be traced; none was made |
| Filings after August 4, 2026 not supplied | MATERIAL for currency, not a defect | Latest balance sheet is June 30, 2026 |
| License, consortium and debt documents not supplied | MATERIAL for legal claims, not a defect | Renewal, partner and distribution-cap conclusions stay inferences or descriptions |
| Charts and diagrams not inspected | MINOR | Filed tables used instead |

## Next module

No further module is selected in this minimum run; the report is assembled from the accepted handoffs. Follow-ups that would raise the confidence score: obtain the revolver and term loan agreements, the latest filing and deck if published by 2026-11-05, current ratings and the Italian license agreements; correct the CP-0 locator and label the CP-2 special dividend figure in the next revision.
