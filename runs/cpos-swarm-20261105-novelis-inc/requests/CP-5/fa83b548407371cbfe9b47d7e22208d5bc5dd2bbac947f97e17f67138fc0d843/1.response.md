## Request

Evidence trace and research-integrity review for Novelis Inc. (issuer id novelis-inc), as of 2026-11-05, credit snapshot pathway. Scope: the accepted source-readiness, financial-base, business-context and credit-synthesis handoffs, traced to the seven pinned filings. This review changes no credit conclusion and repairs no earlier handoff; defects are logged for the reader.

## Sources

### Issuer sources relied on

| Alias | Source name | sha256 |
| --- | --- | --- |
| AR | 10-K_2026-03-31_nvl-20260331.htm.jsonl | 630dfaef3a347b5bc90017d13c739e132a0efac3aeb6333b93d9aa9c3f125e30 |
| Q3R | 10-Q_2025-12-31_nvl-20251231.htm.jsonl | 7c3c815c655f1bd83efacf6827b6774b4b93e5d320aad458b7e7fc75e1ccd80b |
| Q1R | 10-Q_2026-06-30_nvl-20260630.htm.jsonl | ba8ddb9d46239114d2dd866f92530127628a312e217f01c622dff70805bd90cb |
| Q2R | 10-Q_2026-09-30_nvl-20260930.htm.jsonl | d32d6f8b1877bce87168ef75701298999272e2cc239c9328390eaafc7d40bcff |
| RQ4 | EX-99.1_2026-05-19_novelisq4fy26results.htm.jsonl | da5b2fe17bee59287d9273512c195f4d710d0a86a8be059e4808658cb30ef647 |
| RQ1 | EX-99.1_2026-08-05_novelisq1fy27results.htm.jsonl | 93f30ffce44ee10a450dca4f333141188846c86ffae4127361330647232321d7 |
| RQ2 | EX-99.1_2026-11-05_novelisq2fy27results.htm.jsonl | 33ba4aaebc2945cb7c0c06cf8f15a6d1a483e8561da72ad63830ee26f556284c |

Context source (settings, not issuer evidence): context, sha256 e98b858a20d2c069629867a63f74620ff3a26183f951dc5fd1ab64bb298a449a. A locator is the alias and the page chunk of the supplied extraction, for example Q2R page:16. AR is the fiscal 2026 annual report; Q3R, Q1R and Q2R are the quarterly reports for the quarters ended December 31, 2025, June 30, 2026 and September 30, 2026; RQ4, RQ1 and RQ2 are the releases of May 19, August 5 and November 5, 2026.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 787badb2d016843af79e07c22b3c2caac4fdffcb4864359dfe055d24dace3838 | Source readiness; gate for this review. |
| CP-1 | ac0e30aff72597e230e57d534438bf73c91f6af508951774174683b88a68ca6b | Financial base; figures and chart inputs traced and recomputed. |
| CP-1A | 47fdab844131914bbcbc04dcc287f97c0c12415fee526b73176a86b51999f851 | Business and transaction context; facts and categories traced. |
| CP-2 | 7caa543c981c8fce3e88f6828b22fc93eef535e61b7cabd6b62a7aee61647d83 | Credit synthesis; derived measures and structure statements traced. |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial, liquidity and business conclusions trace to the filings: 112 sampled figure and page pairs matched except six debt-table rows cited one page late, and every ratio recomputed. Guarantee, covenant and ratings conclusions cannot be traced. | Medium | No executed debt agreements or rating reports were supplied, so structure rests on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every derived figure recomputes exactly, including debt of 9,797, liquidity of 2,038 and net leverage of 4.7x. | The numbers in the credit view can be relied on as filed or as management defined. | High |
| Six debt-table rows were cited to page 17 but sit on page 16. | Locators need correcting; no figure changes. | High |
| The revolver drawn amount of 2,266 is derived by subtraction, not printed. | Treat it as an inference until the facility schedule and borrowing base are seen. | Medium |
| Guarantee scope, covenant capacity and ratings have no executed-document or rating-report support. | Structure conclusions stay restricted. | High |

### Evidence trace view

The analysis is traceable enough for a snapshot decision on the financial base, liquidity, maturities and business context, but not for conclusions about guarantees, covenant capacity or ratings. Of 112 figure and page pairs sampled from the four handoffs, all match the filings except six debt-table rows that sit on the page before the one cited, and every derived ratio recomputes. The weakest provenance points are the revolver drawn amount, derived by subtraction, and the debt structure, which rests on note summaries because no executed agreements were supplied. The decision that depends on this is whether leverage of 4.7x can return toward management's 3.5x goal: the filings support the starting position, while only management's statement supports the path. Committee use is permitted for the financial and business conclusions and restricted for the structural ones, as logged below.

### Traceability summary

| Coverage class | Count of top drivers | Note |
| --- | --- | --- |
| Directly sourced | 3 | Liquidity, Adjusted EBITDA definition, customer concentration |
| Calculated | 1 | Leverage against the management goal |
| Inferred or management-stated | 1 | Bay Minette start-up and the deleveraging path |
| Critical provenance gap | 0 | None; the structural gap is Material |

Committee status: Restricted. Financial base, liquidity and business-context conclusions may be used. Guarantee, covenant-capacity, distribution-capacity and ratings conclusions may not. The numeric confidence score is script-owned and was not computed in host mode; the band assessed here is Medium.

### Analytical appendix — complete canonical registers

#### Register T5B.1 source document register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2026-03-31_nvl-20260331.htm.jsonl | High: filed, audited annual report | Fiscal 2026, year ended March 31, 2026, with fiscal 2025 and 2024 comparatives | Novelis Inc. consolidated | Statements, debt note, segments, customers, liquidity, obligations, exhibit index | 10-K/A not supplied; text-flattened tables | Financial base, business context, synthesis |
| S2 | 10-Q_2025-12-31_nvl-20251231.htm.jsonl | High: filed, unaudited | Q3 fiscal 2026 and nine months to December 31, 2025 | Novelis Inc. consolidated | Statements, debt, liquidity, Adjusted EBITDA | Superseded for current terms by later filings | Discrete quarter, December 2025 data point |
| S3 | 10-Q_2026-06-30_nvl-20260630.htm.jsonl | High: filed, unaudited | Q1 fiscal 2027 | Novelis Inc. consolidated | Statements, debt, liquidity, ABL amendment | Comparatives only for Q1 fiscal 2026 | Discrete quarter, June 2026 data point |
| S4 | 10-Q_2026-09-30_nvl-20260930.htm.jsonl | High: filed, unaudited, latest | Q2 fiscal 2027 and six months to September 30, 2026 | Novelis Inc. consolidated | Statements, debt, liquidity, guarantors, Oswego, capital allocation | No September 30, 2025 balance sheet | Controlling source for current position |
| S5 | EX-99.1_2026-05-19_novelisq4fy26results.htm.jsonl | Medium: management release with reconciliations | Q4 and fiscal 2026 | Novelis Inc. consolidated | Adjusted EBITDA, net leverage, liquidity | Management measures | Q4 discrete data, definitions |
| S6 | EX-99.1_2026-08-05_novelisq1fy27results.htm.jsonl | Medium: management release | Q1 fiscal 2027 and trailing twelve months | Novelis Inc. consolidated | Adjusted EBITDA, net leverage | Management measures | June 2026 net debt |
| S7 | EX-99.1_2026-11-05_novelisq2fy27results.htm.jsonl | Medium: management release | Q2 fiscal 2027, six months and trailing twelve months | Novelis Inc. consolidated | Adjusted EBITDA, EBITDA, net leverage, segments | Management measures; slides not supplied | Trailing measures, definitions |
| C0 | context | Not issuer evidence | Run settings | Novelis Inc. | Dates, currency, empty ratings and quotes | Parent and guarantors left blank | Run scope only |

#### Register T5B.2 top five material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Net leverage of 4.7x against a management goal of about 3.5x | CP-1, CP-2 | Adjusted Net Debt 8,520 over trailing Adjusted EBITDA 1,831; goal stated in the capital allocation framework | Sets debt service capacity and refinancing room | Core of the credit view | RQ2 page:10; Q2R page:65 | Management EBITDA, not covenant EBITDA |
| 2 | Liquidity of 2,038 resting on a mostly drawn revolver | CP-1, CP-2 | Cash 1,277, committed availability 761, revolver availability 606, short-term borrowings 2,631 | A working capital shock hits liquidity before bonds | Drives near-term risk | Q2R page:61; Q2R page:19; Q2R page:16 | Revolver drawn amount derived; borrowing base not printed |
| 3 | Adjusted EBITDA definition | CP-1, CP-2 | Exclusions for metal price lag, fire losses and start-up costs; EBITDA before adjustments of 1,058 | Leverage depends on management adjustments | Needed to read every ratio | RQ2 page:8; RQ2 page:9; Q2R page:68 | Reconciliation is management's own |
| 4 | Bay Minette start-up and negative free cash flow | CP-1A, CP-2 | First coil in September 2026, commercial shipments targeted for Q1 fiscal 2028, capital spending guidance 2.1 to 2.4 billion | Decides whether deleveraging starts | Main catalyst | RQ2 page:2; Q2R page:48 | Management forecast; remaining cost not itemized |
| 5 | Customer concentration | CP-1A, CP-2 | Top 10 customers 57% of fiscal 2026 net sales; Ball 18% | One customer decision moves revenue | Revenue risk | AR page:33; AR page:188 | Fiscal 2026 data; later period not supplied |

#### Register T5B.3 traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt principal 9,797 and 1,819 rise in six months | CP-1 | Q2R page:17; AR page:145 | Yes | High | Directly Sourced; rise Calculated | Supported | High | Traced and recomputed |
| Net leverage 4.7x, gross 5.35x | CP-1, CP-2 | RQ2 page:10; Q2R page:17 | Yes | High and Medium | Reported by company; gross Calculated | Supported | High | Traced and recomputed |
| Liquidity 2,038 and availability 761 | CP-1 | Q2R page:61 | Yes | High | Directly Sourced | Supported | High | Traced |
| Revolver drawn about 2,266 | CP-2 | Q2R page:18; Q2R page:19 | Yes | High | Calculated by subtraction from stated parts | Supported by reconciliation to 606 | Medium | Traced; inference on composition |
| Customer concentration 57% and 18% | CP-1A, CP-2 | AR page:33; AR page:188 | Yes | High | Directly Sourced | Supported | High | Traced |
| Parent equity 950 | CP-1A | Q2R page:8; AR page:111 | Yes | High | Directly Sourced | Supported | High | Traced |
| Deleveraging toward end of fiscal 2027 | CP-1, CP-2 | RQ2 page:3 | Yes | Medium | Management Language | Management expectation | Low | Traced as attributed claim |
| Guarantee scope and security | CP-1, CP-1A, CP-2 | Q2R page:19; AR page:146 | Yes, summary only | Medium | Documentary Fact at summary level | Limited by missing agreements | Low | Restricted |
| Springing fixed charge test and trigger ceiling | CP-1, CP-2 | AR page:148; Q2R page:18 | Yes | Medium | Calculated indication | Indication only; amendment text missing | Low | Restricted |
| Oswego recoveries 519 | CP-1A, CP-2 | Q2R page:48; RQ2 page:1 | Yes | High | Directly Sourced | Supported | High | Traced |

#### Register T5B.4 source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 9,797 and maturity table | source-text/10-Q_2026-09-30_nvl-20260930.htm.jsonl | Q2R | S4 | page:17, Note 6 | CP-1 chart data debt maturities | Table | High | Matches |
| Short-term borrowings 2,631 and note rows to 6.875% notes | source-text/10-Q_2026-09-30_nvl-20260930.htm.jsonl | Q2R | S4 | page:16, Note 6 | CP-1 debt by instrument; CP-2 key findings | Table | High | Cited as page:17 in CP-1 and CP-2; actual page:16 |
| Revolver availability 606 and letters of credit 128 | source-text/10-Q_2026-09-30_nvl-20260930.htm.jsonl | Q2R | S4 | page:19, Note 6 | CP-1, CP-2 liquidity | Text | High | Matches |
| Liquidity table 1,277 and 761 | source-text/10-Q_2026-09-30_nvl-20260930.htm.jsonl | Q2R | S4 | page:61, MD&A | CP-1 chart data liquidity | Table | High | Matches |
| Net leverage 4.7x, Adjusted Net Debt 8,520 | source-text/EX-99.1_2026-11-05_novelisq2fy27results.htm.jsonl | RQ2 | S7 | page:10 | CP-1, CP-2 | Table | Medium | Matches |
| Trailing Adjusted EBITDA 1,831, EBITDA 1,058, start-up 69 | source-text/EX-99.1_2026-11-05_novelisq2fy27results.htm.jsonl | RQ2 | S7 | page:8 and page:9 | CP-1, CP-2 | Table | Medium | Matches |
| Interest paid 242 and 247 | source-text/10-K_2026-03-31_nvl-20260331.htm.jsonl | AR | S1 | page:112 | CP-1 chart data interest cover | Table | High | Matches |
| Net sales, net income, interest expense FY2025 and FY2026 | source-text/10-K_2026-03-31_nvl-20260331.htm.jsonl | AR | S1 | page:110 | CP-1 financials table | Table | High | Matches |
| Fixed charge test 1.25 to 1.0 | source-text/10-K_2026-03-31_nvl-20260331.htm.jsonl | AR | S1 | page:148 | CP-1, CP-2 | Text | High | Matches; pre-amendment wording |
| Customer concentration | source-text/10-K_2026-03-31_nvl-20260331.htm.jsonl | AR | S1 | page:33 and page:188 | CP-1A, CP-2 | Text and table | High | Matches |
| Management leverage goal about 3.5x | source-text/10-Q_2026-09-30_nvl-20260930.htm.jsonl | Q2R | S4 | page:65 | CP-2 | Text | Medium | Management Language; matches |
| Non-guarantor shares 20%, 18%, 11% | source-text/10-Q_2026-09-30_nvl-20260930.htm.jsonl | Q2R | S4 | page:64 | CP-1, CP-2 | Table | High | Matches |
| Parent subscriptions 750 and 200 | source-text/10-Q_2026-09-30_nvl-20260930.htm.jsonl | Q2R | S4 | page:8 | CP-1A | Text | High | Matches |
| 6.875% notes proceeds repaid 738 of revolver | source-text/10-K_2026-03-31_nvl-20260331.htm.jsonl | AR | S1 | page:151 | CP-1A | Text | High | Matches |

#### Register T5B.5 calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt / EBITDA, five dates | CP-1 chart; CP-2 | Principal 6,212; 7,029; 7,978; 8,970; 9,797; Adjusted EBITDA 1,802; 1,659; 1,645; 1,745; 1,831 | Division | Recomputed: 3.45, 4.24, 4.85, 5.14, 5.35 | Verified | High | Leverage trend | AR page:145; Q3R page:17; Q1R page:15; Q2R page:17 |
| Net debt / EBITDA, five dates | CP-1 chart; CP-2 | Net debt 5,176; 6,204; 6,724; 7,865; 8,520 | Division | Recomputed: 2.87, 3.74, 4.09, 4.51, 4.65 against printed 2.9, 4.1, 4.5 and 4.7 | Verified | High | Leverage trend | RQ4 page:10; RQ1 page:10; RQ2 page:10 |
| December 2025 trailing Adjusted EBITDA | CP-1 | 1,802 + 1,186 - 1,329 | Fiscal year plus nine months less prior nine months | Recomputed: 1,659 | Verified | High | Q3 fiscal 2026 leverage | RQ4 page:9; Q3R page:43 |
| Trailing net sales, net income, interest expense, cash flow, capital expenditure, Adjusted Free Cash Flow | CP-1 financials table | Fiscal 2026 less six months to September 2025 plus six months to September 2026 | Roll-forward | Recomputed: 20,708; 130; 280; -1,022; -2,973; -3,682 | Verified | High | Trailing base | AR pages 110 and 111; Q2R pages 3 and 4; RQ2 page:9 |
| Interest cover FY2025 and FY2026 | CP-1 chart | 1,802 / 247; 1,645 / 242 | Division | Recomputed: 7.30 and 6.80 | Verified | High | Cash coverage | AR page:112 |
| Q4 fiscal 2026 net sales | CP-1 | 18,434 - 13,647 | Subtraction | Recomputed: 4,787; discrete quarters sum to 18,434 | Verified | High | Discrete series | AR page:110; Q3R page:3 |
| Revolver drawn | CP-2 | 2,631 - 350 - 15; commitment 3,000, letters of credit 128 | Subtraction; check 3,000 - 2,266 - 128 | Recomputed: 2,266 and 606; assumes short-term borrowings consist only of the three named parts | Verified with assumption | Medium | Liquidity dependence | Q2R page:18; Q2R page:19 |
| Definition sensitivities | CP-2 | 8,520 / 1,762 and 8,520 / 1,058 | Division | Recomputed: 4.84x and 8.05x; second figure includes fire losses and lag gains | Verified | Medium | Definition risk | RQ2 page:8; RQ2 page:9 |
| Excess over 3.5x | CP-2 | 3.5 x 1,831; 8,520 - 6,409 | Multiplication, subtraction | Recomputed: 6,409 and 2,111 after rounding 6,408.5 | Verified | High | Distance to goal | Q2R page:65 |
| Implied second-half capital spending | CP-2 | 2,100 - 1,543 and 2,400 - 1,543 | Subtraction | Recomputed: 557 and 857 | Verified | High | Funding need | Q2R page:48; Q2R page:4 |
| Secured, note and bond subtotals | CP-2 | 1,231 + 2,266; 13 + 568 + 1,600 + 750 + 750 + 750; 400 + 100 + 225 | Addition | Recomputed: 3,497; 4,431; 725 | Verified | High | Structure | Q2R page:16; Q2R page:17 |
| ABL springing trigger ceiling | CP-1, CP-2 | Greater of 150 and 10% of the lesser of commitment 3,000 and borrowing base | Maximum 300 | Recomputed; indication only | Assumption: pre-amendment wording | Low | Covenant headroom | AR page:148; Q2R page:18 |

#### Register T5B.6 missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | Debt by instrument rows | Six rows cited to page 17 sit on page 16 | Citation accuracy | A reader opening the cited page will not find the row | Cite page 16 and page 17 | CP-1 debt by instrument; CP-2 key findings |
| Minor | Revolver drawn about 2,266 | Derived by subtraction | Calculated, composition assumed | Used for the liquidity dependence argument | Confirm from a facility schedule | CP-2 liquidity and structure |
| Minor | Floating rate sensitivity of about 15 per 100 bp | The filing says the sensitivity includes term loan debt net of swaps and does not say whether revolver borrowings are included | Source ambiguity | Could understate exposure if the revolver is excluded | Query scope with the company or the market risk note | CP-2 weaknesses and risks |
| Minor | Country and sector row | Sector comes from the run context but the row is tagged Documentary Fact | Category tag | Context is not issuer evidence | Retag as context | CP-1A company profile |
| Material | Guarantee, security and covenant capacity | Summary-level text only | Weak lineage | Controls ranking and creditor protection | Obtain executed agreements | CP-1, CP-1A, CP-2 |

#### Register T5B.7 auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Locator precision | Good with one repeated slip | 112 sampled pairs; six rows one page late | A late page costs the reader time but does not change a figure | None for amounts | Correct locators |
| Calculation reproducibility | Strong | Every derived figure recomputed from cited inputs | Reproducibility prevents silent error | Ratios may be relied on | None |
| Definition transparency | Strong | Adjusted EBITDA exclusions listed with amounts and the TTM construction explained | Disclosed definitions let the reader adjust | Leverage is shown under three definitions | None |
| Attribution of management claims | Strong | Deleveraging and capital spending guidance tagged Management Language | Keeps forecasts out of fact | Path to lower leverage is not treated as evidence | None |
| Legal and structural evidence | Weak | No executed agreements; guarantor list absent | Summary text can omit baskets and release conditions | Structure conclusions restricted | Obtain documents |
| Perimeter discipline | Good | Issuer is the consolidated registrant; parent figures not used; issuer entities named per instrument | Mixing perimeters would misstate debt | Debt figure is consolidated | None |
| Period discipline | Good | Quarter, six-month, trailing and fiscal-year figures labelled | Mixed periods distort ratios | Ratios use matching dates | None |

#### Register T5B.8 gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Executed debt agreements and guarantor list | Indentures, credit agreements, bond loan agreements | Guarantee scope, collateral and covenant baskets | Structure and capacity statements are summary-level | Caps confidence at Medium | Company filings on EDGAR exhibits |
| G2 | Ratings and market data | Rating reports, quotes | Pricing and relative value cannot be tested | Out of scope here | Not assessable | Rating agencies, market data |
| G3 | Interim cash interest | Cash interest paid for quarters | Cash coverage trend | Trailing cover is accrual based | Lowers coverage confidence | Cash flow statement supplemental disclosure |
| G4 | Revolver borrowing base and June 2026 amendment text | Facility schedule | Headroom to the springing test | Trigger indicated only | Lowers covenant confidence | ABL amendment |
| G5 | Factoring volume | Factored receivables | Off-balance sheet claim | Size unknown | Lowers liquidity confidence | Company disclosure |
| G6 | Scope of floating rate sensitivity | Market risk note detail | Interest exposure | May understate | Minor | Company disclosure |

### Register T5.1 module and handoff register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 1.response.md; run novelis-inc-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six H2 headings present; readiness view follows reader summary | Accepted, ready with limitations | Gates this review |
| CP-1 | requests/CP-1 1.response.md; same run | Financial base, charts, definitions | High | Six H2 headings; four chart tables and one financials table present | Accepted | Locator slips logged |
| CP-1A | requests/CP-1A 2.response.md; same run | Business, ownership, transactions, governance | High | Six H2 headings; company and operating model table, company profile table and transaction prose present | Accepted on attempt 2 | Category tag slip logged |
| CP-2 | requests/CP-2 1.response.md; same run | Credit synthesis | High | Six H2 headings; key findings and strengths and weaknesses are prose | Accepted | Derived inputs logged |

### Register T5.2 citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Debt by instrument and maturity paragraph | Supported on the adjacent page | Six rows cited to Q2R page:17 are on Q2R page:16 | Correct locators | None for amounts |
| Minor | CP-1 | 3.375% notes of 568 | Supported | Euro denomination of 500 million is not stated although the amount is a dollar translation | Add the denomination | None for the total |
| Minor | CP-2 | Revolver drawn 2,266 | Derived | Composition of short-term borrowings assumed | Confirm | None |
| Minor | CP-1A | Country and sector row | Context-based | Tagged Documentary Fact | Retag | None |
| Info | CP-1, CP-1A, CP-2 | 112 sampled figure and page pairs | Supported | Six mismatches, all the page issue above | None | None |

### Register T5.3 math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Net debt on unadjusted EBITDA of 8.05x | Unadjusted EBITDA includes fire losses and metal price lag gains, so it is a bound, not a leverage measure | None | Keep labelled as a bound | None |
| Minor | CP-1, CP-2 | Trailing interest cover of 6.54x uses accrual interest | Cash interest not available for trailing periods | None | Keep the label | None |
| Info | CP-1 | Printed net leverage 4.7x against calculated 4.65x | Rounding of the company ratio | None | None | None |
| Info | CP-1, CP-2 | All other recomputed ratios and sums | Match | None | None | None |

### Register T5.4 legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Notes guaranteed by Novelis Inc. and certain subsidiaries; secured bank debt ahead | Indentures, guaranty agreements, credit agreements | Guarantor list and release terms absent | Obtain documents | Required before ranking statements are relied on |
| Material | CP-1, CP-2 | Springing fixed charge test and trigger ceiling | June 2026 ABL amendment and credit agreement | Amended wording and borrowing base absent | Obtain amendment | Required for covenant headroom |
| Minor | CP-1A | Distribution capacity under the notes | Indenture restricted payments covenant | Baskets absent | Obtain indenture | Required for distribution capacity |

### Register T5.5 market and relative value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Info | CP-1, CP-1A, CP-2 | No spread, price, rating or peer claim is made | Ratings, quotes, peer data | None needed for the claims made | None | Relative value is outside this run |

### Register T5.6 cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A | Series 2026A bonds are labelled due June 2033 in the annual report table and March 2033 in the quarterly report; CP-1A logged it, CP-1 did not | Annual report versus later quarterly report | Note in CP-1 consumers | None: maturity buckets use the quarterly table |
| Info | CP-1A, CP-1 | Total shipments of 3,731 kt and rolled product shipments of 3,557 kt | Different measures | None | None |
| Info | CP-1, CP-2 | Revolver "about 2.3 billion" in CP-1 and 2,266 in CP-2 | Rounding | None | None |
| Info | CP-0, CP-1, CP-2 | Facility split of the remaining 155 of committed availability stays open in all three | Same gap carried | None | Carried in gaps |
| Info | All | Debt, liquidity, leverage and Adjusted EBITDA figures are identical across CP-1 and CP-2 | None | None | None |

### Register T5.7 duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Repetition | The gaps on agreements and ratings are repeated in several sections | Acceptable; stated where each changes a conclusion | None |
| Info | CP-1, CP-2 | Materiality | The top five drivers are all carried into the credit view | None | Ready for use |

### Register T5.8 handoff structure and consistency

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Info | All | Reader summary and opening view | Present and in order in all four handoffs | None | None |
| Info | CP-1 | Chart selectors | Four chart tables and one financials table present with numeric cells or Not supplied | None | Report charts populated |
| Info | CP-1A | Selectors | Company and operating model, company profile and transaction prose present | None | Report sections populated |
| Info | CP-2 | Selectors | Key findings and strengths and weaknesses are prose | None | Report sections populated |

### Register T5.9 consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | Material | CP-1, CP-1A, CP-2 | Legal and structural | Guarantee, security and covenant statements rest on filing summaries | Obtain executed agreements | Restricts structural conclusions | Open |
| I-02 | Minor | CP-1, CP-2 | Locator | Six debt-table rows cited to page 17 sit on page 16 | Correct locators | None for amounts | Open, cannot edit accepted handoffs |
| I-03 | Minor | CP-1 | Omission | Euro denomination of the 3.375% notes not stated | State denomination | None | Open |
| I-04 | Minor | CP-2 | Derived input | Revolver drawn amount derived by subtraction | Confirm from facility schedule | None | Open |
| I-05 | Minor | CP-2 | Source ambiguity | Scope of the floating rate sensitivity unclear | Query scope | None | Open |
| I-06 | Minor | CP-1A | Category tag | Sector tagged Documentary Fact though context based | Retag | None | Open |
| I-07 | Minor | CP-1 | Cross-module | Series 2026A date inconsistency logged only in CP-1A | Note in CP-1 | None | Open |
| I-08 | Minor | CP-1, CP-2 | Data gap | Interim cash interest not supplied | Use annual cover | Lowers coverage confidence | Open |

## Calculations

This review recomputed the derived figures in the earlier handoffs; the inputs, formulas and results are in the calculation register above and all agree with the handoffs. The sample count is 112 figure and page pairs: 76 from the first pass and 36 from the second pass. The first pass produced six mismatches, all the page 16 and page 17 issue, and the second pass produced none.

## Gaps

The open gaps are listed in the gaps ledger above (G1 to G6). The one that limits committee use is the absence of executed debt agreements and a guarantor list. Ratings and market data are outside the evidence supplied. No source in the pack is dated after the cutoff of 2026-11-05.

## Next module

This is the last module of the minimum set for this run. The issue log should go with the delivered report so a reader can see the open items. If the run is extended, obtain the executed agreements and the June 2026 revolver amendment first, then correct the locators listed in the issue log.
