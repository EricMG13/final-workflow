# CP-5 evidence trace and research-integrity QA: TENET HEALTHCARE CORP (thc)

## Request

- Issuer: TENET HEALTHCARE CORP (issuer id `thc`), as of 2026-11-05, information cutoff 2026-11-05 (context). Run `thc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, `minimum` module set, reporting currency USD.
- Scope: CP-5 traces the evidence behind CP-0, CP-1, CP-1A and CP-2 against the seven pinned filings and grades the result (absorbed CP-5A phase). CP-0 is the source-readiness gate.
- Execution: host session. The same host wrote the four handoffs it checks, so this is a self-review, not an independent one. No provider was called.
- Reader question: is the analysis traceable enough for the decision, and which provenance gap matters most?
- QA envelope: `qa_status` Passed; Confidence Score 42, band Low (from `scripts/confidence_score.py`, see Calculations); `committee_status` Requires More Work.

## Sources

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_thc-20251231.htm.jsonl | f11b8c51ccd0de901ead39554fe597e277a823a504d6f5879743322f2e033f67 |
| 10-Q_2026-03-31_thc-20260331.htm.jsonl | ae2f3d08760ee554a01678cce38fd15c1f6dcfb4f1eb937aa8f7c46189f0123b |
| 10-Q_2026-06-30_thc-20260630.htm.jsonl | a8d86c65c6d20d928c4d4325b82f5d466ad3837698345b3d3bc00c8145f3cd72 |
| 10-Q_2026-09-30_thc-20260930.htm.jsonl | e79732f4107be2e25480e8b1b80ad38188b6eb8362209287bd06381751951a29 |
| EX-99.1_2026-04-30_thc-20260331ex991earningsr.htm.jsonl | 5ea4e9008424f03304d19bf4ecd566569d118ac8a64e8cca9032f7ad6a5e6de8 |
| EX-99.1_2026-07-23_thc-20260630ex991earningsr.htm.jsonl | 03d054c86dcde38802e070349b77939f6a497570e6b4a7e4537e884b4aff9ae1 |
| EX-99.1_2026-10-29_thc-20260930ex991earningsr.htm.jsonl | de8966425c6d51c46fec7968d415d855247be5599cd3f04bbba535aedb3bc95d |
| context | 0ee21d145e164a59cd564e90c45b59adffc7b68df2c1b6fb4dcb72027505ffb5 |

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | 7380c434050643b1a54d0163daac1ad648692a43ba1556324f37ec4ffc476d9e |
| CP-1 | 7b6f055847726910c3eaf6ffe5f0c19c7c490df99bdf5c479f4eef99e9429c40 |
| CP-1A | 57baef9c0e5d3db00610a8bdff368b9f4392f9b98b8c9231e48dd9b203cd384c |
| CP-2 | ef357f02ab385cb074b2c08f2bcec77bd5bb98ccc21771632a478ba6febaae9e |

Locators are `page:N`, the chunk number in the pinned `.jsonl` text, not the printed page.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The earlier work traces well to the filings: every checked quotation and figure was found, and every derived number recomputed equal. Findings are minor. Distribution capacity and covenant headroom stay unproven. | Medium | The same analyst wrote and checked everything, and the executed credit documents are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 68 checked figure strings matched the cited pages and all 55 recomputed values matched. | The leverage, cover and liquidity numbers can be relied on as stated. | High |
| Five minor issues: one missing page reference, an earlier statement that the net-debt ratio could not be rebuilt, two restated figures and one scope detail. | None changes the credit view. | High |
| The filings describe the limits on dividends and buybacks inconsistently. | Capacity for shareholder payouts cannot be sized until the executed documents are read. | Medium |
| The size of the Conifer revenue lost after 2026 is not disclosed. | The earnings effect of the CommonSpirit exit cannot be sized. | High |

### Evidence trace view

The analysis is traceable enough for a view of Tenet's current leverage, liquidity and debt structure, and not yet for distribution capacity, covenant headroom or the earnings effect of losing the CommonSpirit contract. Every quotation and figure checked was found on its cited page, and every derived number recomputed equal. Coverage of material claims: four directly sourced, four calculated, three with insufficient information. The critical provenance gap is the executed credit agreement and indentures: they decide covenant headroom and shareholder-payout capacity, and the filings describe that capacity inconsistently. The affected decision is any view of buyback sustainability or covenant cushion. Remediation owner: the sourcing step, which must supply those documents and the CommonSpirit agreement.

| Traceability summary | Result |
| --- | --- |
| Source quotations checked in the four handoffs | 43 found in source text; 42 on the cited page, 1 without a page locator |
| Figure strings checked against cited pages | 68 of 68 matched |
| Derived values recomputed | 55 of 55 equal |
| CP-2 figures found in CP-1 or CP-1A | All; six are new derived figures shown in CP-2's own calculations |
| Material claims by lineage | 4 Directly Sourced, 4 Calculated, 3 Insufficient Information |
| Open findings | 5 MINOR |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_thc-20251231.htm.jsonl | High: filed, audited annual report | Years ended December 31, 2025, 2024 and 2023 | Tenet Healthcare Corporation and subsidiaries, consolidated | Statements, debt note, covenants, leases, segment Adjusted EBITDA, business, history | Text conversion of the filed HTML | CP-0, CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_thc-20260331.htm.jsonl | High: filed, unaudited interim report | Three months ended March 31, 2026 | Same | Interim statements, revolver availability, Omnibus Agreement | Text conversion; unaudited | CP-0, CP-1, CP-1A |
| S3 | 10-Q_2026-06-30_thc-20260630.htm.jsonl | High: filed, unaudited interim report | Three and six months ended June 30, 2026 | Same | Interim statements, debt table, six-month Adjusted EBITDA and cash flow | Text conversion; unaudited | CP-1 |
| S4 | 10-Q_2026-09-30_thc-20260930.htm.jsonl | High: filed, unaudited interim report; controlling for September 30, 2026 | Three and nine months ended September 30, 2026 | Same | Statements, debt note, liquidity, maturity table, segments, payer mix, regulation | Text conversion; unaudited; interim notes condensed | CP-0, CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-30_thc-20260331ex991earningsr.htm.jsonl | Medium: issuer press release | Q1 2026 | Same | Management results and outlook | Management non-GAAP | CP-0 context |
| S6 | EX-99.1_2026-07-23_thc-20260630ex991earningsr.htm.jsonl | Medium: issuer press release | Q2 2026 | Same | Management results and raised outlook | Management non-GAAP | CP-0 context |
| S7 | EX-99.1_2026-10-29_thc-20260930ex991earningsr.htm.jsonl | Medium: issuer press release | Q3 2026 and nine months | Same | Adjusted EBITDA definition, reported net-debt ratio, transition benefit, outlook | Management non-GAAP; statements repeat the 10-Q | CP-1, CP-1A, CP-2 |
| S8 | context | User settings, not issuer evidence | Run date 2026-11-05 | Run identity | Pathway, dates, currency, sector, ticker | Ratings, deal terms, guarantors blank | All modules |

#### T5B.2 Top material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Moderate leverage and strong liquidity: 2.65x total, 2.11x net, cover 6.03x, liquidity 4,574 | CP-1, CP-2 | Debt note, balance sheet, segment note, cash-flow statement | Sets default and refinancing risk | Core leverage view | S4 page:2, page:4, page:12, page:13, page:24; S1 page:174, page:121; S3 page:26 | Adjusted EBITDA is a management measure |
| 2 | Earnings quality: 147 transition benefit and 540 settlement receipt | CP-1, CP-2 | Release page:2 and 10-Q page:49 | Headline earnings exceed run rate | Sensitivity 2.73x and 2.18x | S7 page:2; S4 page:49 | Split is a management attribution |
| 3 | Partner leakage: 838 distributions, 2,179 redeemable noncontrolling interests | CP-1, CP-1A, CP-2 | Cash-flow statements and note 12 | Consolidated EBITDA is partly owned by others | Partner-adjusted 3.18x total | S1 page:120; S4 page:4, page:20 | Put terms not supplied |
| 4 | Payer mix and policy risk | CP-1A, CP-2 | Payer tables, regulatory text | Drives margin and supplemental payments | Largest unsized risk | S4 page:34, page:35, page:36, page:37, page:39 | Management says it cannot estimate the effect |
| 5 | CommonSpirit exit and September 2026 refinancing | CP-1A, CP-1, CP-2 | Note 1, note 5, release | Changes revenue base, receivable and maturity wall | Maturities and non-recurring earnings | S4 page:5, page:10, page:13; S7 page:2 | Agreements and indenture not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 13,243, cash 2,674, net debt 10,569 | CP-1 | S4 page:2, page:12 | Yes | High | Documentary Fact | Supported | High | Traced |
| LTM Adjusted EBITDA 5,004 and leverage 2.65x and 2.11x | CP-1, CP-2 | S1 page:174; S4 page:24, page:25 | Yes | High inputs; management measure | Calculated | Supported | High | Recomputed equal |
| Cash interest cover 6.03x | CP-1, CP-2 | S1 page:121; S4 page:4 | Yes | High inputs | Calculated | Supported | High | Recomputed equal |
| Liquidity 4,574 with revolver undrawn | CP-1, CP-2 | S4 page:2, page:13 | Yes | High | Calculated | Supported | High | Recomputed equal |
| Maturity profile through 2030 and thereafter | CP-1, CP-2 | S4 page:52 | Yes | High | Documentary Fact | Supported | High | Traced |
| September 2026 refinancing of 2,000 | CP-1, CP-1A, CP-2 | S4 page:13; S7 page:2 | Yes | High; release is management | Documentary Fact | Supported | High | Traced |
| CommonSpirit agreement terms and note receivable | CP-1A, CP-2 | S4 page:5, page:10, page:20 | Yes | High | Documentary Fact | Supported | High | Traced |
| Payer mix and Medicaid supplemental revenue | CP-1A, CP-2 | S4 page:34, page:37, page:39 | Yes | High | Documentary Fact | Supported | High | Traced |
| Sensitivities 2.73x and 3.18x | CP-1, CP-2 | S7 page:2; S1 page:120; S4 page:4 | Yes | Inputs high; split management | Calculated | Supported | Medium | Recomputed equal |
| Covenant headroom | CP-1, CP-2 | Executed agreements not in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |
| Shareholder-payout capacity | CP-1A, CP-2 | S1 page:50 against page:148 | Yes, both | High | Insufficient Information | Conflict logged and unresolved | Low | Conflict preserved, not reconciled |
| Earnings effect of the lost Conifer contract | CP-1A, CP-2 | Not disclosed in the set | No source exists in the set | Not available in the set | Insufficient Information | Open gap | Low | Gap correctly labelled |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total long-term debt 13,243 | runs/cpos-swarm-20261105-thc/source-text | 10-Q_2026-09-30_thc-20260930.htm.jsonl | S4 | page:12, Note 5 | CP-1 Financials and credit metrics | Reported | High | Debt table re-added equal |
| Adjusted EBITDA FY2025 4,566 | runs/cpos-swarm-20261105-thc/source-text | 10-K_2025-12-31_thc-20251231.htm.jsonl | S1 | page:174, Note 23 | CP-1 leverage chart | Management non-GAAP in a filed note | High | Re-added from revenue and expenses, equal |
| Adjusted EBITDA nine months 2026 3,821 and 2025 3,383 | runs/cpos-swarm-20261105-thc/source-text | 10-Q_2026-09-30_thc-20260930.htm.jsonl | S4 | page:24 and page:25, Note 17 | CP-1 leverage chart | Management non-GAAP in a filed note | High | Matches release table |
| Cash interest paid 865, 464 and 499 | runs/cpos-swarm-20261105-thc/source-text | 10-K_2025-12-31_thc-20251231.htm.jsonl and 10-Q_2026-09-30_thc-20260930.htm.jsonl | S1, S4 | S1 page:121; S4 page:4 | CP-1 interest cover chart | Reported | High | Net of capitalized interest |
| Revolver availability 1,900 and letters of credit | runs/cpos-swarm-20261105-thc/source-text | 10-Q_2026-09-30_thc-20260930.htm.jsonl | S4 | page:13, Note 5 | CP-1 liquidity chart | Reported | High | Under 1 of letters of credit not netted, as disclosed |
| Maturity table 13,341 | runs/cpos-swarm-20261105-thc/source-text | 10-Q_2026-09-30_thc-20260930.htm.jsonl | S4 | page:52, Item 3 | CP-1 maturities chart | Reported | High | Equals debt table plus discounts |
| Covenants 4.00 to 1.00 and 4.25 to 1.00 | runs/cpos-swarm-20261105-thc/source-text | 10-K_2025-12-31_thc-20251231.htm.jsonl | S1 | page:148 and page:149, Note 8 | CP-1 covenants | Reported description | High | Dated December 31, 2025 |
| Omnibus Agreement terms | runs/cpos-swarm-20261105-thc/source-text | 10-Q_2026-09-30_thc-20260930.htm.jsonl | S4 | page:5, Note 1 | CP-1A transaction summary | Reported | High | Also page:175 of the 10-K |
| Payer mix 9M 2026 | runs/cpos-swarm-20261105-thc/source-text | 10-Q_2026-09-30_thc-20260930.htm.jsonl | S4 | page:34 | CP-1A operating model | Reported | High | Matches |
| Net-debt ratios 2.25x, 2.33x, 2.11x | runs/cpos-swarm-20261105-thc/source-text | EX-99.1_2026-10-29_thc-20260930ex991earningsr.htm.jsonl | S7 | page:2 | CP-1 correction note | Management claim | Medium | Reproduced from carrying debt less cash |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM figures | CP-1; CP-2 | FY2025 and both nine-month periods | FY2025 + 9M 2026 - 9M 2025 | Recomputed: equal | Supported | High | Basis of every ratio | S1 page:118 to page:121, page:174; S4 page:2 to page:4, page:24, page:25 |
| Leverage ratios | CP-1; CP-2 | Carrying debt, cash, LTM Adjusted EBITDA | Debt / EBITDA; (debt - cash) / EBITDA | Recomputed: 3.30x, 2.88x, 2.65x and 2.54x, 2.25x, 2.11x equal | Supported | High | Leverage tolerance | S1 page:118, page:144, page:174; S4 page:2, page:12 |
| Net-debt check against issuer | CP-1 | Releases give 2.25x, 2.33x, 2.11x | Same formula at three dates | Recomputed: equal, including June 30, 2026 | Supported | High | Confirms issuer ratio arithmetic | S7 page:2; S3 page:2, page:13, page:26, page:27 |
| Cash interest cover | CP-1; CP-2 | Adjusted EBITDA and interest paid | EBITDA / cash interest | Recomputed: 4.69x, 5.28x, 6.03x equal | Supported | High | Debt service | S1 page:121; S4 page:4 |
| Sensitivities | CP-1; CP-2 | 147 benefit; 838 distributions | EBITDA - 147; EBITDA - 838 | Recomputed: 2.73x, 2.18x, 3.18x, 2.54x equal | Supported with label caveat | Medium | Underlying leverage | S7 page:2; S1 page:120; S4 page:4 |
| Free cash flow and payouts | CP-1; CP-2 | LTM operating cash flow, capex, distributions, buybacks | 3,328 - 838 - 1,813; same less 540 | Recomputed: 677 and 137 equal | Supported | High | Cash buffer | S1 page:120; S4 page:4 |
| Liquidity cover of maturities | CP-2 | Liquidity and maturities through 2029 | 4,574 / 3,579 | Recomputed: 1.28x equal | Supported | High | Refinancing capacity | S4 page:52 |
| Confidence Score | This handoff | Lineage counts, 17 of 17 registers, partial gate, 5 MINOR | Script formula | 42, band Low | Script output | High | QA envelope | scripts/confidence_score.py |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 reporting unit | The quotation about amounts being expressed in millions carries no page locator; it is on page:6 of the Q3 10-Q | Missing locator | A reader cannot find it without searching | Add the page in a later run | CP-0 handoff, Identity and perimeter |
| MINOR | CP-0 and CP-1 net-debt ratio | CP-0 says the ratio cannot be rebuilt; CP-1 reproduces it at three dates and states the correction | Cross-module inconsistency, corrected downstream | Reader of CP-0 alone is misled | Prefer CP-1; reword CP-0 in a later run | CP-0 Findings; CP-1 correction note |
| MINOR | CP-1A operating model | Equity earnings of 180 is the group total; Ambulatory Care is 179 (S4 page:24) | Scope imprecision | Overstates the ambulatory share by 1 | State the segment figure | CP-1A Company and operating model |
| MINOR | CP-2 narrative | 1.107 billion and 1.360 billion in CP-1A are restated as 1,107 million and 1,360 million | Restated figure | Not a literal copy; values agree | Keep the original scale | CP-2 Key findings |
| MINOR | CP-2 calculations | Six derived figures (3,579; 1.28x; 281; 438; 677; 137) are new in CP-2 | New figure | Not in CP-1; shown with inputs and recomputed equal | Fold into CP-1 in a later run | CP-2 Calculations |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source identity | Strong | Every source pinned by sha256; filings identify themselves by cover text | A wrong document would change every figure | None found | None |
| Locator precision | Strong | 42 of 43 source quotations on the cited page; 1 without locator | Slower checks | None on conclusions | Add the missing page |
| Figure reproducibility | Strong | 68 of 68 figure strings matched; 55 of 55 derived values equal | An error would move leverage | None found | None |
| Cross-module consistency | Strong | CP-2 figures all found upstream or shown with calculations; one corrected statement between CP-0 and CP-1 | Inconsistent figures mislead a committee | None on conclusions | Align CP-0 wording |
| Definition risk | Adequate | Adjusted EBITDA, net debt and cash interest labelled; net debt reproduced, not issuer-defined | A different definition shifts net leverage | Low | Supply supplemental disclosures |
| Reviewer independence | Weak | Host wrote and checked the handoffs | Shared blind spots go undetected | Errors of omission may remain | Independent review by another agent or model |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Executed credit agreement, LC facility and indentures, including the September 2026 supplemental indenture | Executed documents | Covenant headroom and shareholder-payout capacity unproven | CP-1 covenants; CP-2 risk rows | Holds confidence at Medium or below | EDGAR exhibits and 8-K of September 22, 2026 |
| G2 | CommonSpirit Omnibus Agreement and the 8-K of February 2, 2026; recurring Conifer revenue | Agreements and segment disclosure | Earnings effect of the exit cannot be sized | CP-1A, CP-2 revenue durability | Lowers confidence in forward earnings | 8-K and exhibits |
| G3 | Proxy statement and Part III information | Board, holders, control rights | Ownership and governance not assessable | CP-1A ownership rows | Governance view limited | Proxy statement |
| G4 | Put terms of redeemable noncontrolling interests | Partnership terms | Possible cash calls not sized | Liquidity view | Moderate | Note disclosure or agreements |
| G5 | Events from October 30, 2026 to the cutoff | Later filings | Status at the as-of date unknown | Monitoring posture | Lowers currency of the view | EDGAR filings to the cutoff |
| G6 | Independent review | A second reviewer | Self-review only | Whole run | Caps committee status | Independent agent or model |

#### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 attempt 1 / thc-2026-11-05-credit_snapshot-host | Source readiness for four consumers | High | Six headings; accepted attempt 1 | Passed with one MINOR locator finding | READY_WITH_LIMITATIONS for all consumers; bound as gate, not evaluated for credit claims |
| CP-1 | requests/CP-1 attempt 1 / same run | Statements, LTM, debt, liquidity, maturities, covenants | High | Six headings and required selectors; accepted attempt 1 | Passed | All metrics recomputed equal |
| CP-1A | requests/CP-1A attempt 1 / same run | Business, CommonSpirit, refinancing, behaviour | High | Six headings and required selectors; accepted attempt 1 | Passed with one MINOR scope finding | One conflict logged and preserved |
| CP-2 | requests/CP-2 attempt 1 / same run | Credit synthesis | High inputs | Six headings; accepted attempt 1 | Passed with two MINOR findings | Confidence Medium |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-0 | Identity and perimeter, units sentence | Supported | No page locator; the sentence is on page:6 of the Q3 10-Q | Add the page | None |
| MINOR | CP-1A | Company and operating model, equity earnings row | Supported with scope caveat | Group total used for an ambulatory statement | Use the segment figure 179 | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Net debt | Issuer does not print a definition; CP-1 uses carrying debt less cash and reproduces the issuer ratio at three dates | None | Keep the label "reproduced", as CP-1 does | None |
| MINOR | CP-1 | LTM Adjusted EBITDA includes a 147 benefit and the Q3 2026 transition effect | Management attribution | None | Keep the sensitivity beside the headline, as CP-1 does | None |
| MINOR | CP-1 | Operating cash flow includes 540 settlement receipt offset in financing | Presentation of an offset | None | Keep the ex-receipt figure beside the headline, as CP-1 does | None |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL as a gap, not a defect | CP-1A, CP-2 | Capacity for dividends and buybacks | Executed credit agreement and indentures | Filings describe restrictions inconsistently; conflict logged, not reconciled | Supply documents | Required before any distribution view |
| MINOR | CP-1 | Covenant levels 4.00 to 1.00, 4.25 to 1.00 and the 150 fixed-charge trigger | Executed documents | Description only, dated December 31, 2025 | Supply agreements | Required for headroom |
| MINOR | CP-1 | Revolver springing maturity reading | Executed credit agreement | CP-1 flags the clause as relevant and defers to the document | Supply agreement | Required before relying on the revolver beyond 2028 |

#### T5.5 Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | All modules | No market or relative-value claim is made; no peer ranking, instrument recommendation or recovery conclusion appears in CP-2 | Prices, spreads and ratings are outside the minimum source pack | Recorded by design | Add market modules only with sourced market data | Committee cannot judge value from this run |

#### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1 | CP-0 says the net-debt ratio cannot be rebuilt; CP-1 reproduces it and says so | CP-1 is the later module and cites CP-0 hash 7380c434 | Prefer CP-1; reword CP-0 later | None on conclusions |
| MINOR | CP-1A, CP-2 | CP-2 restates two CP-1A figures at a different scale; values agree | CP-2 cites CP-1A hash 57baef9c | Keep original scale | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL as a readiness limit | Run | Committee readiness | Current leverage and liquidity view is traceable; distribution capacity, covenant headroom and the lost Conifer earnings are not; review is self-review only | Supply executed documents and an independent review | Committee status Requires More Work |
| MINOR | CP-1, releases | Duplication | The releases repeat 10-Q statement figures; CP-0 and CP-1 treat the 10-Q as controlling | None | None |

#### T5.8 Structured export and handoff audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| No finding | CP-0, CP-1, CP-1A, CP-2 | Envelope: six headings, source and handoff hashes, Reader summary and view subsection order, selectors | None found in structure; all four accepted on attempt 1 | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| QA-1 | MINOR | CP-0 | Locator | Units quotation without page locator | Add page:6 in a later run | None | Open |
| QA-2 | MINOR | CP-0, CP-1 | Cross-module | Net-debt ratio rebuildability stated differently; CP-1 corrects | Reword CP-0 in a later run | None | Open |
| QA-3 | MINOR | CP-1A | Scope | Group equity earnings used for an ambulatory statement | Use segment figure | None | Open |
| QA-4 | MINOR | CP-2 | Restatement | Two figures restated at a different scale | Keep original scale | None | Open |
| QA-5 | MINOR | CP-2 | New figure | Six derived figures new in CP-2 | Fold into CP-1 later | None | Open |

## Calculations

| ID | What | Method | Result |
| --- | --- | --- | --- |
| Q1 | Quotation trace | Each double-quoted phrase in the four handoffs searched in the pinned source text and on the pages its line cites | 44 quoted spans parsed, of which 1 is a handoff label; of 43 source quotations all are present, 42 are on the cited page, 1 has no page locator |
| Q2 | Figure trace | 68 figure strings from CP-1, CP-1A and CP-2 searched on the cited page of the pinned source | 68 of 68 matched |
| Q3 | Recomputation | Sums, LTM figures, net debt, ratios, margins and CP-2 derived figures recomputed from the cited inputs | 55 of 55 equal; including leverage 3.30x, 2.88x, 2.65x and 2.54x, 2.25x, 2.11x |
| Q4 | Cross-module figure identity | Numbers in CP-2 searched in CP-0, CP-1 and CP-1A text | All found except six derived figures shown in CP-2 calculations and two restated at a different scale |
| Q5 | Confidence Score | `scripts/confidence_score.py --lineage "Directly Sourced:4,Calculated:4,Insufficient Information:3" --fields-present 17 --fields-total 17 --source-gate partial --findings MINOR:5` | score = clamp((0.6 x 69.09 + 0.4 x 100) x 0.7 - 15) = 42.02, rounded to 42; band Low; qa_status Passed |

## Gaps

- G1 Critical for the decision: executed credit agreement, LC facility and indentures not supplied; covenant headroom and shareholder-payout capacity unproven.
- G2: CommonSpirit agreements not supplied; the earnings effect of the lost Conifer contract cannot be sized.
- G3 and G4: proxy statement and put terms of redeemable noncontrolling interests not supplied.
- G5: events from October 30, 2026 to the cutoff not supplied.
- G6: no independent review; this CP-5 was written by the same host that wrote the four handoffs.

## Next module

- Report delivery: carry `qa_status` Passed, Confidence Score 42 (Low), committee status Requires More Work, and gap G1.
- Independent review: a second agent or model should repeat this check, starting with omissions, which a self-review is least likely to find.
- Sourcing: fetch the credit agreement and indentures, the Omnibus Agreement and the proxy statement, then rerun CP-1A, CP-2 and CP-5 in a new run folder.
