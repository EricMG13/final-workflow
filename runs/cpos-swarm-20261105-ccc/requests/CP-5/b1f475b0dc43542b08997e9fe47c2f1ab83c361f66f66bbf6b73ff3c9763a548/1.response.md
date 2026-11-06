## Request

This is the evidence trace and research-integrity review of the CP-0, CP-1, CP-1A and CP-2 handoffs for CCC Intelligent Solutions Holdings Inc. as of 2026-11-05 (credit_snapshot pathway, host mode). Scope is the default Top 5 material credit drivers plus a statement-level lineage check of the handoffs against the seven pinned filings and releases; it changes no upstream conclusion and adds no credit analysis.

## Sources

Issuer sources checked against (exact name and sha256 pinned by CP-OS). Locators `page:N` are extracted chunks, not printed pages.

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_ccc-20251231.htm.jsonl | 59a1556351f7a7f353f0b9618ee7cf495b7ba17767f7cd6a5a0ded1621642fde |
| 10-Q_2026-03-31_ccc-20260331.htm.jsonl | 39b288dd8e81ee0fdda5870870b9bea592f01074d7af9763a85c294be03c88d4 |
| 10-Q_2026-06-30_ccc-20260630.htm.jsonl | eda11b6dbfa4719333004f220abf5cdc5bfe0e2df75fd21d1a6f0733cf5d331c |
| 10-Q_2026-09-30_ccc-20260930.htm.jsonl | 0c88b8b197fab954d1c3ff71345c0e05e9f10d1f3510025ad9548d8138ae8407 |
| EX-99.1_2026-04-30_ccc-ex99_1.htm.jsonl | ae3848deb91163ab500fd7932cb28c39aab5b44b52f0fa623f872d5f723093a6 |
| EX-99.1_2026-07-30_ccc-ex99_1.htm.jsonl | a2b1e7ba00fedac3bf32b37f93a1dd3c6ccb1a88c16f25d3354731a4f4c2fb7c |
| EX-99.1_2026-10-29_ccc-ex99_1.htm.jsonl | 6ea0ae7480d6fb5cada60e78aef6508a9d3b3ddbb6b2caecfdee6ff746b5c13f |

Run context: `context`, sha256 b5d08a6a26eac33af88a5d18c45e48ca178e243a383ecb998014ab0c163dd60f (settings only).

Supplied handoffs audited (module and exact sha256):

| Module | sha256 |
| --- | --- |
| CP-0 | 6b0d66d9bd08d88f5e3acbbee3edf3515d663baf1c742e23d09d59c87c891429 |
| CP-1 | e6ae04ecf3ddd225ddd9d25e538b38d2d5d6d7e26ef4c669fa8bd69c5b612bbe |
| CP-1A | 39d5f467142498a63ff95b65f165246c999c399dad7b123c4e09209e0d5ef4f2 |
| CP-2 | a103881051eef7679988be916b6ef6ff74b2d598ed1ddf93c7b2a8f389c71ccd |

Method of this audit: every number written with a thousands separator in the four handoffs was machine-checked for presence in the source text; the numbers not found there are all calculations and were recomputed independently from figures re-extracted from the sources by a script written for this audit (see `## Calculations`). Presence of a number is necessary but not sufficient, so the cell, period and locator of the Top 5 drivers and of the statements in the lineage register were read against the page. Not done: the original HTML files were not opened, so extraction fidelity of flattened tables is not independently reviewed; every handoff in this run was authored by the same host session as this review, so the review is not independent of the author, and a second reviewer should repeat the spot checks before the run is used.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four handoffs trace to the filings: every checked figure ties to a source and independent recomputation matches. Committee use should be restricted because covenant terms and post-merger financing rest on issuer summaries or are absent. | Medium | The credit agreement and merger agreement are not in the pack, the first handoff has an uncorrectable summary error, and the same session authored and reviewed the work. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Recomputing from the sources reproduces LTM Adjusted EBITDA of 484,946, cash interest of 72,448, cover of 6.69x and leverage of 2.64x gross and 2.22x net. | The headline credit metrics are reliable on the issuer's Adjusted EBITDA definition. | High |
| Covenant levels and the 35% revolver trigger come from issuer summaries because the credit agreement is not supplied. | Covenant headroom cannot be cleared for committee use. | High |
| The first handoff's summary calls the term loan and revolver the only debt, omitting a 27,562 non-recourse note shown elsewhere in it. | The debt perimeter is correct only in the later handoffs, which state the correction. | High |
| No supplied document supports the position after the merger closes. | Any credit view beyond the first quarter of 2027 is unsupported. | High |
| Minor slips: one wrong page for a cash figure, an incomplete guarantor-name comparison and a wrong statement that the dividend policy was not found. | No figure changes; locators and one statement need correcting when the report is assembled. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 are directly sourced, 3 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the absence of the 2021 Credit Agreement with its amendments and the Agreement and Plan of Merger, which matters because covenant capacity, the treatment of the term loan on a change of control and post-closing leverage all depend on them, and it implies that committee use is restricted to the pre-closing standalone view with covenant headroom and sponsor behaviour left unassessed. The calculated drivers all reproduce from the filings; the open defects concern wording and locators, not figures.

### Source register (T5B.1)

Module Status: Ready with Limitations. Traceability Scope: Top 5. Missing required inputs: the credit agreement and amendments, the merger agreement and any proxy statement. Entity key: issuer_id ccc available. Citation limitation: handoffs cite `page:N` chunks of extracted text.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_ccc-20251231.htm.jsonl | High: audited annual report (auditor's report at page:125) | FY2025 with FY2024 and FY2023 | CCC Intelligent Solutions Holdings Inc. consolidated | Statements, Note 15 debt, Adjusted EBITDA reconciliation, business, risk factors, related parties, capital stock | Credit agreement only described, not supplied | CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_ccc-20260331.htm.jsonl | Medium-High: unaudited filed quarterly report | Q1 2026 | Same | Statements, debt, Adjusted EBITDA | Unaudited | CP-1 |
| S3 | 10-Q_2026-06-30_ccc-20260630.htm.jsonl | Medium-High: unaudited filed quarterly report | Q2 and six months 2026 | Same | Statements, debt, Adjusted EBITDA | Unaudited | CP-1 |
| S4 | 10-Q_2026-09-30_ccc-20260930.htm.jsonl | Medium-High: unaudited filed quarterly report | Q3 and nine months 2026 | Same; Parent and Merger Sub for the merger | Statements, debt, Note 25 merger, risk factors, KPIs, non-GAAP | Merger agreement summarised, exhibit omitted | CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-30_ccc-ex99_1.htm.jsonl | Medium: furnished release, management narrative | Q1 2026 | Same | Free cash flow, total debt statement | Management attribution | CP-1 tie-out |
| S6 | EX-99.1_2026-07-30_ccc-ex99_1.htm.jsonl | Medium: furnished release | Q2 2026 | Same | Free cash flow, total debt statement | Total debt basis differs from the 10-Q | CP-1 tie-out |
| S7 | EX-99.1_2026-10-29_ccc-ex99_1.htm.jsonl | Medium: furnished release | Q3 2026 | Same; consortium named | Merger summary, enterprise value, AI run-rate, free cash flow | Management claims | CP-1A, CP-2 |

### Top five material credit drivers (T5B.2)

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage and cash interest cover on issuer Adjusted EBITDA: 2.64x gross, 2.22x net, 6.69x cover | CP-1 | Term Loan principal 1,281,216, cash 202,926, LTM Adjusted EBITDA 484,946, LTM cash interest 72,448 | Sets default risk and debt service capacity | Primary leverage statement in the credit view | S4 pages:4, 19, 43, 8; S1 pages:111, 132 | Issuer-defined EBITDA, not covenant EBITDA |
| 2 | Share-based pay add-back sensitivity: 3.58x gross and 3.01x net after deducting 126,687 | CP-1, CP-2 | Add-back of 97,359 for 9M 2026 and 181,285 for FY2025 less 151,957 for 9M 2025 | Shows how much of headline EBITDA is non-cash pay and so how large the true leverage range is | Defines the gap between headline and strict leverage | S4 page:43; S1 page:111 | Analyst construct, lender definition unknown |
| 3 | Liquidity and maturity profile: 451.9 million liquidity, 13.0 million annual amortisation, 1,212.8 million balloon in 2032 | CP-1 | Cash 202,926; revolver undrawn with 249.0 million available; term loan due 2032-01-23 | Governs refinancing and liquidity risk | No near-term wall under the existing structure | S4 pages:4, 18, 19 | Revolver use is subject to the merger agreement's debt limits |
| 4 | Revenue durability: 96% subscription, three to five year insurer contracts, 1,808 million of backlog | CP-1A | Revenue by type and remaining performance obligations | Drives revenue visibility and debt service capacity | Supports the standalone view | S4 pages:12, 34, 35; S1 pages:25, 29, 103, 149 | Renewals excluded from backlog; customer-level data not supplied |
| 5 | Post-closing credit position under the merger | CP-1A, CP-2 | Merger terms are issuer summaries; financing, term loan treatment and covenants are not in any source | Sets leverage, ranking and covenants after the first quarter of 2027 | Decisive for any forward view | S4 pages:29, 30, 51; S7 page:2 | Insufficient Information |

### Traceability map (T5B.3)

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 2.64x gross, 2.22x net; cover 6.69x | CP-1 | Principal, cash, Adjusted EBITDA and cash interest recomputed from S1 and S4 (calculation A1 to A4) | Yes | High | Calculated | Verified by recomputation | High | Committee-Ready |
| Leverage after share-based pay 3.58x and 3.01x | CP-1, CP-2 | Adjusted EBITDA less 126,687 (A5) | Yes | High for inputs; analyst construct | Calculated | Verified by recomputation; definition labelled analyst measure | Medium | Committee-Ready with disclosure |
| Liquidity 451.9 million; maturities | CP-1 | Cash 202,926 plus availability 249,000; amortisation derived from stated terms (A6, A7) | Yes | High | Calculated | Verified; maturity derived from stated terms and tied to the 10-K table | High | Committee-Ready |
| Revenue durability | CP-1A | Subscription 281,466 of 294,093 in Q3 2026; backlog 1,808 million; contract tenors | Yes | High | Directly Sourced | Supported | High | Committee-Ready |
| Post-closing credit position | CP-1A, CP-2 | Merger summary only; no financing or credit agreement text | Partial | Medium | Insufficient Information | Unsupported beyond the issuer summary | Low | Remediation Needed |

### Source lineage register (T5B.4)

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Term Loan principal 1,281,216 at 2026-09-30 | Long-term debt table | 10-Q_2026-09-30_ccc-20260930.htm.jsonl | S4 | page:19 | CP-1 debt register | Sourced | High | Verified |
| Cash and cash equivalents 202,926 at 2026-09-30 | Balance sheet | 10-Q_2026-09-30_ccc-20260930.htm.jsonl | S4 | page:4 | CP-1 liquidity | Sourced | High | CP-0 cites page:5, which is wrong (CP5-005) |
| Revolver 250.0 million undrawn, 249.0 million available | Note 14 | 10-Q_2026-09-30_ccc-20260930.htm.jsonl | S4 | page:18 | CP-1 liquidity | Sourced | High | Verified |
| LTM Adjusted EBITDA 484,946 | FY2025 plus 9M 2026 less 9M 2025 | S1 and S4 | S1; S4 | S1 page:111; S4 page:43 | CP-1 financials | Calculated | High | Recomputed |
| Cash paid for interest 57,637 (9M 2026) and 66,704 (FY2025) | Cash flow statements | S4 and S1 | S4; S1 | S4 page:8; S1 page:132 | CP-1 cover | Sourced | High | Verified |
| Share-based pay add-back 97,359 (9M 2026) and 181,285 (FY2025) | Adjusted EBITDA reconciliations | S4 and S1 | S4; S1 | S4 page:43; S1 page:111 | CP-1 sensitivity | Sourced | High | Verified |
| Term Loan matures 2032-01-23 with quarterly payments of about 3.3 million | Note 14 | 10-Q_2026-09-30_ccc-20260930.htm.jsonl | S4 | page:18 | CP-1 maturities | Sourced | High | Verified |
| 10-K principal maturities 13,033 for 2026 to 2029 and 1,238,858 for 2030 | Note 15 | 10-K_2025-12-31_ccc-20251231.htm.jsonl | S1 | page:161 | CP-1 maturities | Sourced | High | Ties to 13,033 + 13,033 + 1,212,792 |
| Swaps fix 750.0 million notional at about 3.94% through 2027-07-31 | Note 14 | 10-Q_2026-09-30_ccc-20260930.htm.jsonl | S4 | page:19 | CP-1, CP-2 | Sourced | High | Verified |
| Springing covenant: leverage ratio not above 6.25 to 1.00 if revolver borrowings exceed 35% of commitments | Note 15 and Note 14 | S1 and S4 | S1; S4 | S1 page:161; S4 page:18 | CP-1 covenants, CP-2 | Sourced (issuer summary) | Medium | Credit agreement not supplied; wording varies (S1 page:81 "a minimum of 35.0%") |
| Remaining performance obligations 1,808 million (806 million in twelve months) and 1,891 million (780 million) | Note 4 | S4 and S1 | S4; S1 | S4 page:12; S1 page:149 | CP-1A operating model | Sourced | High | Verified |
| Software subscriptions 96% of revenue; billing monthly | MD&A and Note 4 | 10-K_2025-12-31_ccc-20251231.htm.jsonl | S1 | page:103 | CP-1A | Sourced | High | Verified |
| Net dollar retention 108% and gross dollar retention 98% for Q3 2026 | KPI tables | S4 | S4 | pages:34, 35 | CP-1A | Sourced (company-defined KPI) | Medium | Verified |
| Insurer contracts average about three to five years; repair facilities about three years | Business | S1 | S1 | page:25 | CP-1A | Sourced | High | Verified |
| No customer above 10% of FY2025 revenue | Risk factors | S1 | S1 | page:29 | CP-1A | Sourced | High | Verified |
| Merger at 7.75 US dollars per share, expected close first quarter of 2027, no financing condition | Note 25 | S4 | S4 | pages:29, 30 | CP-1A, CP-2 | Sourced (issuer summary of the agreement) | Medium | Agreement not supplied |
| Termination fees of 149.52 million and about 313.99 million | Risk factors | S4 | S4 | page:51 | CP-1A, CP-2 | Sourced (issuer summary) | Medium | Verified |
| Enterprise value of approximately 6.1 billion US dollars; consortium led by GTCR with Elliott | Release | S7 | S7 | page:2 | CP-1A | Sourced (management claim) | Medium | Not named in the 10-Q pages searched |
| 300.0 million incremental term loans funded the accelerated share repurchase | Notes 15 and 19 | S1 and S4 | S1; S4 | S1 page:159; S4 page:23 | CP-1A, CP-2 | Sourced | High | Verified |
| Repurchases from the principal equity owner of 328.5 million (2023) and 72.3 million (2025) | Related parties | S1 | S1 | page:176 | CP-1A | Sourced | High | Owner not named |
| Note payable of 27,562 at CCCIS Cayman Holdings Limited, non-recourse | Notes 15 and 16 | S4 | S4 | pages:19, 20 | CP-1, CP-1A | Sourced | High | Verified |
| About 2,185 employees at 2025-12-31 | Human capital | S1 | S1 | page:26 | CP-1A | Sourced | High | Verified |
| Dividend policy: no current plans to pay cash dividends | Item 5 | S1 | S1 | page:91 | CP-1A | Sourced | High | CP-1A says the policy text was not located (CP5-006) |
| Purchase obligations 164,515 at 2025-12-31 | Note 23 | S1 | S1 | page:174 | CP-1, CP-1A | Sourced | High | Verified |
| Goodwill 1,955,551 and intangible assets 942,018 at 2026-09-30 | Balance sheet | S4 | S4 | page:4 | CP-2 | Sourced | High | Verified |
| LTM free cash flow 311,375 | Release reconciliation and 10-K | S7 and S1 | S7; S1 | S7 page:12; S1 page:112 | CP-1, CP-2 | Calculated from issuer free cash flow | High | Recomputed |

### Calculation and assumption register (T5B.5)

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA | CP-1 chart data and metrics; CP-2 | FY2025 436,043; 9M 2026 366,217; 9M 2025 317,314 | 436,043 + 366,217 − 317,314 = 484,946 (USD thousands, LTM to 2026-09-30) | Calculated | Recomputed, matches | High | Leverage, cover | S1 page:111; S4 page:43 |
| LTM cash paid for interest | CP-1; CP-2 | FY2025 66,704; 9M 2026 57,637; 9M 2025 51,893 | 66,704 + 57,637 − 51,893 = 72,448 | Calculated | Recomputed, matches | High | Debt service | S1 page:132; S4 page:8 |
| Gross and net leverage, five dates | CP-1 leverage chart | Term Loan principal and cash at each date; LTM Adjusted EBITDA | Principal / EBITDA; (principal − cash) / EBITDA | Calculated | Recomputed for all five dates, matches | High | Leverage | S1; S2; S3; S4 |
| Cash interest cover, five dates | CP-1 interest cover chart | Adjusted EBITDA; cash paid for interest | EBITDA / cash interest | Calculated | Recomputed, matches | High | Debt service | S1; S2; S3; S4 |
| Share-based pay sensitivity | CP-1; CP-2 | Add-back 126,687 LTM | (Adjusted EBITDA − add-back) = 358,259; 1,281,216 / 358,259 = 3.58x | Calculated (analyst construct) | Recomputed, matches; not issuer-defined | Medium | Earnings quality | S1 page:111; S4 page:43 |
| Liquidity 451.926 US$m | CP-1; CP-2 | Cash 202,926; availability 249,000 | Sum | Calculated | Recomputed | High | Liquidity | S4 pages:4, 18 |
| Debt maturities by year | CP-1 chart data | Current portion 13,033; 9M payments 9,774; principal 1,281,216 | Q4 2026 = 3,259; 2027 to 2031 = 13,033 each; 2032 = 1,212,792 | Calculated from stated terms | Recomputed; ties to the 10-K table | Medium | Refinancing | S4 pages:18, 19; S1 page:161 |
| Fixed-charge, rate sensitivity and headroom (illustrations) | CP-2 | LTM figures; swap notional 750,000 | 417,693 / 85,481 = 4.89x; 531,216 x 1% = 5,312; EBITDA fall to 4.0x gross = 34.0% | Calculated (illustration) | Recomputed; labelled not covenant | Medium | Sensitivity | CP-1 |
| Merger arithmetic | CP-1A | 591,041,172 shares; 7.75; net debt 1,078,290 | 4,580.6 + 1,078.3 = 5,658.9 million US dollars against approximately 6,100 | Calculated | Recomputed; difference of 441.1 million unexplained and disclosed | Medium | Transaction sizing | S4 page:1; S7 page:2 |
| Covenant headroom | CP-1, CP-2 | Covenant ratio definition | Not Calculable: definition not supplied | Not Calculable | Correctly withheld in all modules | High | Covenant risk | S1 page:161; S4 page:18 |

### Missing-citation and weak-lineage flags (T5B.6)

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-0 summary: the only debt is the term loan and revolver | Omits the 27,562 non-recourse note that CP-0's own entity table lists | Weak Lineage | A reader of the summary alone understates funded obligations at the China subsidiary parent, though the note is outside the funded debt figure by design | CP-0 cannot be edited; carry CP-1's correction into any report text | CP-0 reader summary |
| Material | Covenant levels and trigger | Issuer summary only; agreement not supplied | Weak Lineage | Headroom and default risk cannot be tested | Add the executed agreement | CP-1, CP-2 |
| Material | Post-closing credit position | No source for financing or treatment of the term loan | Insufficient Information | Any forward leverage view is unsupported | Add the merger agreement and financing disclosure | CP-1A, CP-2 |
| Material | Leverage on issuer Adjusted EBITDA | Lender definition unknown | Assumption-Based | Headline may differ from lender leverage | Add covenant definitions | CP-1, CP-2 |
| Minor | Cash balance locator | CP-0 cites page:5 for cash of 202,926; it is on page:4 | Directly Sourced | Reviewer cannot open the cited page | Correct the locator | CP-0 |
| Minor | Dividend policy | CP-1A says not located; stated at S1 page:91 | Weak Lineage | A searchable fact was missed | Cite page:91 | CP-1A |

### Auditability assessment (T5B.7)

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | All seven filings and releases are pinned and addressable; credit agreement and merger agreement absent | Missing governing documents force reliance on issuer summaries | Covenant and post-closing views stay unassessed | Add the two documents |
| Citation completeness | Ready with Remediation | Top 5 drivers and 26 statements trace to pages; two locator errors and one wrong "not located" found | Wrong locators slow review but do not change values | Low credit impact | Correct CP-0 locators and the dividend statement |
| Calculation traceability | Committee-Ready | Every derived number was recomputed from re-extracted source figures and matched | None found | Metrics reliable on issuer definitions | None |
| Assumption transparency | Ready with Remediation | Issuer Adjusted EBITDA is used as EBITDA; the sensitivity is shown but the lender definition is unknown | Definition drift between issuer and lender | Leverage could read 2.64x or 3.58x | Add covenant definitions |
| Markdown artifact integrity | Committee-Ready | Each handoff has the six required headings and nonempty tables; checked by CP-OS | None | None | None |

Overall auditability: Ready with Remediation (lowest of the dimensions).

### Gaps ledger (T5B.8)

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Covenant terms and capacity | 2021 Credit Agreement and Amendments 1 to 5 | Headroom, change-of-control and distribution capacity cannot be tested, so default risk and leverage tolerance are unsupported | CP-1, CP-2 | High impact | Executed credit agreement |
| CP-5-GAP-002 | Post-closing financing and term loan treatment | Agreement and Plan of Merger, buyer financing documents | Refinancing and ranking after closing cannot be assessed | CP-1A, CP-2 | High impact | 8-K of 2026-10-15 with exhibit 2.1 |
| CP-5-GAP-003 | Customer concentration | Top-customer revenue share and renewal calendar | Loss of a large insurer cannot be sized | CP-1A, CP-2 | Medium impact | Company data |
| CP-5-GAP-004 | Principal equity owner and holdings | Proxy statement or beneficial ownership table | Sponsor alignment cannot be assessed | CP-1A | Medium impact | Proxy statement when filed |
| CP-5-GAP-005 | Q4 2025 as a discrete quarter | FY2025 fourth-quarter release | Only difference-based quarter possible | CP-1 | Low impact | Q4 2025 release |
| CP-5-GAP-006 | Bridge from offer price to enterprise value | Dilutive securities and costs | 441.1 million difference unexplained | CP-1A | Low impact | Proxy or 8-K |
| CP-5-GAP-007 | Extraction fidelity and reviewer independence | Original HTML tables; second reviewer | Flattened tables could hide a cell error | All | Medium impact | HTML spot check by a second reviewer |

### Module register (T5.1)

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0 response, run ccc-2026-11-05-credit_snapshot-host | Source readiness for the four consumers | High | Six required headings present; host transport, no YAML envelope | Restricted | Material summary omission and locator slips; reader summary cannot be corrected |
| CP-1 | requests/CP-1 response, same run | Statements, LTM metrics, chart data | High | Six headings and the required selectors present; five chart and metric tables with exact headers | Restricted | Figures recomputed and matched; restricted only by the shared definition issue CP5-004 and the missing agreements |
| CP-1A | requests/CP-1A response, same run | Business, transaction, governance | High | Six headings and the three selectors present | Restricted | Wrong dividend-policy statement; merger terms are issuer summaries |
| CP-2 | requests/CP-2 response, same run | Credit synthesis | Medium-High | Six headings; key findings and strengths and weaknesses are prose | Restricted | Inherits the gaps; adjectives flagged |

### Citation and evidence support audit (T5.2)

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-0 | Reader summary: "The only debt is one senior secured term loan and an undrawn revolver" | Partially Supported | The same handoff lists a 27,562 note at CCC Cayman, non-recourse, in its entity table; the note is outside funded debt by design but the summary does not say so | Use CP-1's debt register in the report; do not quote the CP-0 summary row | Disclose for committee use (CP5-001) |
| Material | CP-1A, CP-2 | Credit position after the merger closes | Insufficient Information | No source describes the buyer financing or the term loan's fate; the modules say so, but the committee must not read a view beyond the first quarter of 2027 | Add the merger agreement and financing disclosure | Restricts committee use to the pre-closing view (CP5-003) |
| Minor | CP-0 | Cash of 202,926 cited to 10-Q Q3 page:5 and statements to pages:5-8 | Supported (value), locator wrong | The balance sheet assets, including cash, are on page:4; the release balance sheet is on release page:8 | Correct locators | Hygiene (CP5-005) |
| Minor | CP-1A | "The 10-K dividend policy text was not located" | Unsupported | S1 page:91 states "We have no current plans to pay cash dividends" | Cite page:91; the cash flow evidence of no dividends is consistent | Hygiene (CP5-006) |

### Math, logic and definition audit (T5.3)

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Leverage, cover and every "EBITDA" ratio use issuer Adjusted EBITDA, which adds back share-based pay and related payroll tax | The governing definition for lender metrics is the credit agreement's, which is not supplied; CP-1 and CP-2 disclose the issuer basis and show the stricter sensitivity | None between sources; definition gap only | Add the credit agreement definitions before any covenant statement | Disclose; restricts covenant use (CP5-004) |
| None found | CP-1 | Formula, numerator, denominator, period, units and sign for each ratio | Recomputed from the sources for five dates; all match | None | None | None |

### Legal and structural claim audit (T5.4)

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A, CP-2 | Springing leverage test at 6.25 to 1.00 above 35% revolver use; mandatory prepayment above 3.5 leverage; guarantor and security package; merger closing conditions and fees | 2021 Credit Agreement with Amendments 1 to 5; executed Agreement and Plan of Merger | Only issuer summaries; wording varies across filings ("minimum of 35.0%" in S1 page:81, "exceeds 35%" in S1 page:161); each module states these as issuer descriptions | Add the executed documents; keep the "issuer summary" label | Legal review required before covenant or change-of-control conclusions (CP5-002) |

### Market and relative-value claim audit (T5.5)

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Implied 12.6x LTM Adjusted EBITDA and 17.0x after the add-back, from management's approximate enterprise value of 6.1 billion US dollars | Fully diluted share count and the enterprise value bridge | 441.1 million difference to the arithmetic enterprise value is unexplained | Keep the "arithmetic on management's approximate figure" label; do not use as a valuation (CP5-008) | Low: no recommendation or ranking is made; no market prices, spreads or ratings are used in any module |

### Cross-module consistency and version control (T5.6)

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A | Guarantor intermediate holding company name: CP-0 compares the 10-K spelling with the Q2 and Q3 10-Qs only; the Q1 10-Q uses the 10-K spelling (S2 page:20) | CP-1 and CP-1A record the Q1 spelling; CP-0 cannot be edited | Quote both spellings as printed; resolve from the credit agreement | None for figures (CP5-007) |
| None found | CP-0, CP-1, CP-1A, CP-2 | Issuer, period, Term Loan principal, cash, Adjusted EBITDA, liquidity, maturities, merger terms and fees agree across modules; CP-2 rounds CP-1 thousands to one decimal in millions consistently | None | None | None |

### Duplication, materiality and committee-readiness audit (T5.7)

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Unsupported adjectives | "Sound", "strong cash conversion" and "ample liquidity" appear in the reader summary and strengths text; each is backed by figures in the same handoff but the adjectives are not quantified at the point of use (CP5-009) | Tie each adjective to its figure in the report text | Low |
| None found | CP-1A, CP-1 | Duplication | Repeated corrections to CP-0 appear once in CP-1 and are referenced, not repeated, elsewhere | None | None |

### Handoff envelope and evidence trace audit (T5.8)

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| None (informational) | CP-0, CP-1, CP-1A, CP-2 | YAML front matter, filename pattern and the full-method H2 set | The host transport replaces these with the six CP-OS headings and the module-specific selectors; all are present and ordered, so this is not a defect of the run | None | None |

### Consolidated issue log (T5.9)

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-0 | Evidence support | Reader summary says the only debt is the term loan and revolver; omits the 27,562 non-recourse note | Do not quote the summary row; use the CP-1 debt register | Disclose | Open |
| CP5-002 | MATERIAL | CP-1, CP-1A, CP-2 | Legal source | Covenant and structure claims rest on issuer summaries | Add the credit agreement and merger agreement | Restricts covenant and change-of-control use | Open |
| CP5-003 | MATERIAL | CP-1A, CP-2 | Evidence gap | Post-closing credit position unsupported | Add merger and financing documents | Restricts committee use to pre-closing view | Open |
| CP5-004 | MATERIAL | CP-1, CP-2 | Definition drift | Issuer Adjusted EBITDA used for leverage and cover; lender definition unknown | Add covenant definitions | Disclose; no covenant statement | Open |
| CP5-005 | MINOR | CP-0 | Locator | Cash cited to page:5 instead of page:4; statements range omits page:4 | Correct locators | None | Open |
| CP5-006 | MINOR | CP-1A | Unsupported statement | Dividend policy "not located" but stated at S1 page:91 | Cite page:91 | None | Open |
| CP5-007 | MINOR | CP-0 | Version control | Guarantor-name comparison omits the Q1 10-Q spelling | Quote both spellings | None | Open |
| CP5-008 | MINOR | CP-1A | Market claim | Implied EV/EBITDA on management's approximate enterprise value | Keep the label; no valuation use | None | Open |
| CP5-009 | MINOR | CP-2 | Promotional language | Adjectives not quantified at point of use | Tie to figures | None | Open |

### Remediation priority map

1. Must-fix before committee: CP5-002, CP5-003 and CP5-004 are gaps that cannot be fixed from the pack; add the credit agreement, merger agreement and financing disclosure, or restrict committee use to the pre-closing standalone view without covenant headroom or sponsor behaviour. CP5-001: use the CP-1 debt register for the debt perimeter.
2. Must-fix before the handoffs are consumed downstream: none beyond CP5-001; the report assembly must take debt and liquidity figures from CP-1 and not from the CP-0 summary.
3. Monitoring follow-up: CP5-008 (label for the arithmetic enterprise value multiple); a second reviewer to spot check flattened tables against the HTML (CP-5-GAP-007).
4. Formatting and hygiene: CP5-005, CP5-006, CP5-007, CP5-009.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 4. Minor Issues: 5. Committee Use: Restricted.

The numbers reproduce and nothing is Critical, but the credit agreement and merger agreement are absent, so covenant and post-closing statements are issuer summaries; qa_status is Restricted under the severity engine because four Material issues are open. The Confidence band is Medium; a numeric confidence score is not computed here because the scoring script is not part of this host transport.

## Calculations

Independent recomputation. Inputs were re-extracted from the source text by a script written for this audit, not copied from the handoffs. USD thousands unless stated; LTM to 2026-09-30 unless stated.

| Check | Re-extracted inputs | Result | Matches |
| --- | --- | --- | --- |
| A1 LTM Adjusted EBITDA | 10-K 436,043; 10-Q Q3 366,217 and 317,314 | 436,043 + 366,217 − 317,314 = 484,946 | Yes |
| A2 LTM cash paid for interest | 10-K 66,704; 10-Q Q3 57,637 and 51,893 | 72,448 | Yes |
| A3 Cash interest cover | 484,946 / 72,448 | 6.69x | Yes |
| A4 Leverage at 2026-09-30 | Principal 1,281,216; cash 202,926; EBITDA 484,946 | 2.64x gross; 2.22x net | Yes |
| A4b Leverage at 2026-03-31 and 2026-06-30 | Q1 and Q2 principal, cash and LTM EBITDA 457,164 and 464,527; LTM cash interest 69,354 and 71,168 | Q1 2.82x gross, 2.74x net, 6.59x cover; Q2 2.77x, 2.52x, 6.53x | Yes |
| A4c Leverage at FY2024 and FY2025 | Principal 776,000 and 1,290,990; cash 398,983 and 111,192; EBITDA 397,377 and 436,043; cash interest 62,898 and 66,704 | FY2024 1.95x, 0.95x, 6.32x; FY2025 2.96x, 2.71x, 6.54x | Yes |
| A5 Share-based pay LTM and sensitivity | 181,285 + 97,359 − 151,957 = 126,687; 484,946 − 126,687 = 358,259 | 1,281,216 / 358,259 = 3.58x; 1,078,290 / 358,259 = 3.01x | Yes |
| A6 Liquidity | 202,926 + 249,000 | 451,926 | Yes |
| A7 Maturities | 13,033 current; 9,774 paid; 1,281,216 principal | 3,259; 13,033 x 5 = 65,165; 1,212,792; 10-K bucket 13,033 + 13,033 + 1,212,792 = 1,238,858 | Yes |
| A8 Free cash flow LTM | Release: 9M 2026 206,498 and 9M 2025 149,631; 10-K 254,508 | 311,375 | Yes |
| A9 Merger arithmetic | 591,041,172 x 7.75 | 4,580.6 million US dollars | Yes |
| A10 Presence check | All comma-formatted numbers in the four handoffs | Absent from sources only where derived (LTM builds, ratios, sums); no unexplained number | Yes |

## Gaps

The gaps that limit committee use are listed in the gaps ledger above (CP-5-GAP-001 to CP-5-GAP-007). The two that matter most are the missing credit agreement (covenant headroom Not calculable) and the missing merger agreement and financing (post-closing leverage Not calculable). Reviewer independence is also limited: this review was written by the session that authored the audited handoffs.

## Next module

No further CP-OS module follows CP-5 in this run. The report should be assembled from CP-1 for figures and CP-1A and CP-2 for narrative, carrying the open issues CP5-001 to CP5-009 and the Restricted committee-use status, and a second reviewer should repeat the spot checks against the original filings before the report is used.
