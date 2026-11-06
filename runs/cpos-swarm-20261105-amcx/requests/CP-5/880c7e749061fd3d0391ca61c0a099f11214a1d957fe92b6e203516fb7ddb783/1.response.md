## Request

AMC Global Media Inc. evidence trace review as of 2026-11-05 (pathway credit_snapshot; current period Q2 2026, prior period FY2025; reporting currency USD). It checks whether the four earlier handoffs (source readiness, financial base, business and transaction context, credit synthesis) rest on the filings they cite, re-checks cited figures against the filings, recomputes every derived figure, and grades committee use. It changes no earlier conclusion and silently repairs nothing.

## Sources

### Issuer sources relied on

Cited figures were re-checked against all seven sources for this review. Source quality for every filing is High (primary, dated, issuer-specific); earnings releases carry attributed management claims only.

| Source (exact name) | sha256 | Re-opened for |
| --- | --- | --- |
| 10-K_2025-12-31_amcx-20251231.htm.jsonl | 2eac087a9c91970955c65f61340e91bd48ad2f9f3f6c57f58dc32a71147af2c1 | Statements, debt note, control, commitments, litigation (cited pages checked) |
| 10-Q_2025-09-30_amcx-20250930.htm.jsonl | 36dd5126a4c9060458356b29d3eb4aa03633caa5f0871dc91ad5f4dc8adcd0a9 | Covenant context only; no earlier figure is cited to it |
| 10-Q_2026-03-31_amcx-20260331.htm.jsonl | 938a57939d24ffa99772ad28c4268837c8cd2e9d6c83313cdce5d4f6457a019b | March 31, 2026 cash, debt, cash interest, covenant text |
| 10-Q_2026-06-30_amcx-20260630.htm.jsonl | 709e51b6dc542ca6e875192527a94179627534ebb9b979b24ab34c983b10c21a | Q2 2026 statements, debt note, MD&A, liquidity, legal, Item 5 |
| EX-99.1_2026-02-11_amcx-21126xex991.htm.jsonl | d86abe17fb554149efdc3f1d1068cea9305b7eb4d0b53b4922cda0c2c6548e87 | FY2025 capitalization and adjusted operating income |
| EX-99.1_2026-05-08_amcx-50826ex991.htm.jsonl | baaebb0b7ed064d963f5f351d5426dc6837acb54bc54b02caebdf8169997d96e | March 31, 2026 capitalization, twelve-month adjusted operating income, covenant ratios |
| EX-99.1_2026-07-30_amcx-73026ex991.htm.jsonl | 2c28473b42400a7535aa74f85a20a041b1e3d1cc8d274b85c2e5db3c449c0a4b | June 30, 2026 capitalization, adjusted operating income, free cash flow, Netflix licence |

### Settings input (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context (run settings, 2026-11-05) | 95e365e5dede6bf5d3238dc431d8121ca3ba426646f866c4518f2a27b51f7e19 |

### Handoffs supplied

| Module | sha256 |
| --- | --- |
| CP-0 | 35f530dc59f7820bbe868f2a577800a555c15b2a5fcc5f7bfcb4e80bdce10420 |
| CP-1 | 746b970893dcbe57525284bb2a29c526ab69662e4945f1c9b86d2e2b0cceacb8 |
| CP-1A | 2e989982f8986cd3b9bca83e423ed4609a85d6ece2c247b7b18eb58c7e718ed2 |
| CP-2 | 1514d8ccb83323d74dcb053e0625536752c0f779b9f921d962b253e9ddfc1615 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The earlier work traces well to the filings: every source figure was found in the filings and every derived figure recomputed exactly. Two overstated phrases and the missing debt documents limit use for covenant, distribution and ranking questions. | Medium | Executed debt documents are not supplied, so covenant, restricted-payment and ranking claims cannot be traced beyond filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Source figures were found in the filings, and leverage, cover, free cash flow and coupon figures recomputed to the same values. | The financial base can be relied on within its stated definitions. | High |
| Leverage uses the company's adjusted operating income, not a defined EBITDA. | The 4.06x net and 5.54x total ratios are not comparable with covenant or market EBITDA ratios. | High |
| One credit summary says buybacks were made under the amended covenant, but the sources show the allowance and the purchases separately. | Restricted-payment capacity is not traced and should not be inferred. | High |
| Which notes rank first rests on instrument names, while the guarantee wording conflicts. | Any priority or recovery reading is unsupported. | Medium |
| Netflix cash, expected declines and the repurchase authorization are management statements. | They are supportive but unverified, not contracted receipts. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 1 is calculated, 0 are assumption-based, 1 is an analyst inference, and 1 is a weak-lineage, untraced, conflicting, or insufficient-information item. The most important provenance gap is the absence of the executed indentures, which matters because restricted-payment capacity, covenant headroom and note ranking decide creditor control and rest only on filing summaries, and it implies that the credit view may be used for financial and business questions but not for covenant, distribution or ranking conclusions. Committee status: Restricted for those three uses; usable with stated limits for the rest. The confidence score is Not calculable here because the scoring script is not run in host mode.

### Re-anchor of upstream datapoints

Run identifier amcx-2026-11-05-credit_snapshot-host; entity AMC Global Media Inc. (formerly AMC Networks Inc.); consolidated perimeter; USD; periods FY2025, six months to June 30, 2026, twelve months to June 30, 2026 and Q2 2026. Datapoints restated from the sources and matched: total debt principal 1,735,554 thousand and cash 463,996 thousand at June 30, 2026; twelve-month adjusted operating income 313,045 thousand; twelve-month cash interest paid 151,153 thousand; debt maturing 420,456 thousand in 2029 and 1,315,098 thousand in 2032. No upstream period or entity mismatch was found.

### Defects found, stated plainly

- The credit synthesis says buybacks of USD 30.0 million were made under the amended covenant (reader summary and risk table). The filings state the amendment (up to $50.0 million of equity repurchases, 10-Q Q2-26 page:17) and the purchase (treasury stock 30,000, page:6; accelerated share repurchase of $30 million, Rel Jul page:4) but not that one used the other. The business handoff keeps capacity and action in separate columns and is the correct wording.
- The credit synthesis calls the 4.25% notes "junior" to the secured notes while also saying ranking cannot be settled. The label rests on the instrument names (Senior Notes against Senior Secured Notes) and the 10-K description of the senior notes as guaranteed on a senior unsecured basis (10-K page:175); the guarantee wording for the secured notes is also "unsecured" (10-K page:112). The label is an Analyst Inference, not a traced ranking.
- The financial base labels its chart columns "EBITDA" while using adjusted operating income, a company non-GAAP measure that adds back share-based compensation, restructuring and impairment and adds the proportionate AOI of majority-owned equity investees (10-Q Q2-26 page:28). The handoff discloses this in every basis cell, so the defect is one of label drift, not of lineage.
- The business handoff attributes a 32.4% content licensing decline to delivery timing; 32.4% is the consolidated decline (10-Q Q2-26 page:42), and the timing explanation is given for the Domestic segment's 33.7% decline (page:44). Minor.
- The business handoff states that the accelerated share repurchase of $30 million is the same amount as the 30,000 of treasury stock bought; the filings do not state this, but the equity statement shows treasury stock acquired of 30,137 including excise tax (10-Q Q2-26 page:4), which is consistent. Minor Analyst Interpretation.

### Analytical appendix — complete canonical registers

Module Status: Ready with Limitations. Traceability Scope: Top 5.

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_amcx-20251231.htm.jsonl | High (audited annual report) | FY2025 and FY2024 comparatives | AMC Networks Inc. (now AMC Global Media Inc.), consolidated | Statements, debt note, control, commitments, litigation (cited pages checked) | Old company name; text-only extraction | Financial base, business context, control |
| S2 | 10-Q_2025-09-30_amcx-20250930.htm.jsonl | High (unaudited interim) | Q3 2025 and nine months | Same registrant, old name | Covenant context | No earlier figure cited to it | Context only |
| S3 | 10-Q_2026-03-31_amcx-20260331.htm.jsonl | High (unaudited interim) | Q1 2026 | AMC Global Media Inc., consolidated | March 31, 2026 cash and debt, cash interest, covenant text | Text-only extraction | Liquidity and leverage rows |
| S4 | 10-Q_2026-06-30_amcx-20260630.htm.jsonl | High (unaudited interim) | Q2 2026 and six months | AMC Global Media Inc., consolidated | Statements, debt note, MD&A, liquidity, legal, subsequent events | Latest periodic report; text-only extraction | All modules |
| S5 | EX-99.1_2026-02-11_amcx-21126xex991.htm.jsonl | Medium (management release, attributed) | Q4 and FY2025 | AMC Networks Inc., consolidated | Capitalization, adjusted operating income, covenant ratios | Non-GAAP measures defined by management | Leverage inputs |
| S6 | EX-99.1_2026-05-08_amcx-50826ex991.htm.jsonl | Medium (management release, attributed) | Q1 2026 | AMC Global Media Inc., consolidated | Capitalization, twelve-month adjusted operating income, covenant ratios | Same | Leverage inputs |
| S7 | EX-99.1_2026-07-30_amcx-73026ex991.htm.jsonl | Medium (management release, attributed) | Q2 2026 | AMC Global Media Inc., consolidated | Capitalization, adjusted operating income, free cash flow, Netflix licence | Same | Leverage, liquidity, subsequent events |
| S8 | context (run settings) | Settings, not issuer evidence | As of 2026-11-05 | Run | Sector, country, blank ratings and deal fields | Blank fields are not zero | Identity only |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Falling adjusted operating income raising leverage to 4.06x net and 5.54x total | CP-1 | Twelve-month adjusted operating income 313,045 thousand against 411,874 thousand; net debt 1,271,558 thousand | Earnings, not debt, moved the ratio; further declines weaken cover of 2.07x | Drives debt service capacity and refinancing access | S4 page:3, 28; S7 page:11; S1 page:134 | Adjusted measure is not EBITDA |
| 2 | Cash-only liquidity after the revolver and Term Loan A ended on May 12, 2026 | CP-1 | Cash 463,996 thousand; revolver terminated | No committed back-up; part of the cash is held abroad | Liquidity buffer for shocks and litigation | S4 page:2, 17, 55 | No letters of credit data after search; cash is point-in-time |
| 3 | Maturity ordering: 420,456 thousand of 4.25% notes due 2029 ahead of 1,315,098 thousand of secured notes due 2032 | CP-1, CP-1A, CP-2 | Debt table and instrument names | Earlier maturity is the unsecured instrument by name; refinancing depends on capital markets | Refinancing risk and priority | S4 page:16, 55-56; S1 page:112, 171, 175 | Ranking not settled by sources |
| 4 | Shareholder distributions under family control | CP-1A, CP-2 | Treasury stock 30,000 thousand in six months 2026; amended buyback allowance; 79% voting power outside director elections | Cash can leave the credit group within indenture capacity | Restricted-payment monitoring | S4 page:6, 17; S1 page:72-73; S7 page:4 | Indentures not supplied |
| 5 | Damages claim above USD 200 million with trial set for October 27, 2026 | CP-1A, CP-2 | Legal note | Unquantified cash call against 463,996 thousand of cash | Event risk on liquidity | S4 page:24-25 | Outcome not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 4.06x net, 5.54x total; cover 2.07x | CP-1 | Figures on S4 page:16 and S7 page:10-11; formulas in CP-1 calculations | Yes | High | Calculated | Verified by recomputation | High | Committee-Ready |
| Cash-only liquidity | CP-1 | "terminated its revolving credit facility" S4 page:17; cash S4 page:2 | Yes | High | Directly Sourced | Verified | High | Committee-Ready |
| Maturity ordering and ranking of 2029 and 2032 notes | CP-1, CP-1A, CP-2 | Amounts S4 page:16; "on an unsecured basis" S1 page:112 against first-priority lien S1 page:171 | Yes | High for amounts, Low for ranking | Conflicting | Open: wording tension preserved | Medium | Remediation Needed |
| Distributions and control | CP-1A, CP-2 | Treasury stock S4 page:6; amendment S4 page:17; voting power S1 page:72-73 | Yes | High | Analyst Inference | Facts verified; creditor effect is interpretation | Medium | Remediation Needed |
| Damages claim and trial date | CP-1A, CP-2 | "damages in excess of $200 million" and trial date S4 page:24 | Yes | High | Directly Sourced | Verified; outcome absent | High | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt principal 1,735,554 thousand at June 30, 2026 | source-text | 10-Q_2026-06-30_amcx-20260630.htm.jsonl | S4 | page:16, Note 9 | CP-1 financial table | Sourced | High | Lines add to the printed total |
| Cash 463,996 thousand at June 30, 2026 | source-text | 10-Q_2026-06-30_amcx-20260630.htm.jsonl | S4 | page:2, balance sheet | CP-1 liquidity | Sourced | High | |
| Twelve-month AOI 313,045 thousand | source-text | EX-99.1_2026-07-30_amcx-73026ex991.htm.jsonl | S7 | page:11 | CP-1 leverage | Sourced | Medium | Also rebuilt from FY2025 and six-month figures |
| FY2025 AOI 411,874 thousand | source-text | EX-99.1_2026-02-11_amcx-21126xex991.htm.jsonl | S5 | page:11 | CP-1 leverage | Sourced | Medium | |
| Cash interest paid FY2025 156,563 thousand | source-text | 10-K_2025-12-31_amcx-20251231.htm.jsonl | S1 | page:196, Note 19 | CP-1 cover | Sourced | High | |
| Cash interest paid six months 2026 and 2025 | source-text | 10-Q_2026-06-30_amcx-20260630.htm.jsonl | S4 | page:27, Note 17 | CP-1 cover | Sourced | High | 78,984 and 84,394 thousand |
| Revolver and Term Loan A ended May 12, 2026 | source-text | 10-Q_2026-06-30_amcx-20260630.htm.jsonl | S4 | page:17, Note 9 | CP-1, CP-1A | Sourced | High | $3.1 million charge |
| Exchange offer terms and settlement | source-text | 10-Q_2026-06-30_amcx-20260630.htm.jsonl | S4 | page:17-19 | CP-1A transactions | Sourced | High | Amounts are "approximately" in the filing |
| Indenture consent allowing up to $50.0 million of buybacks | source-text | 10-Q_2026-06-30_amcx-20260630.htm.jsonl | S4 | page:17 | CP-1A governance | Sourced | High | Terms of the indenture not seen |
| Treasury stock purchased 30,000 thousand in six months 2026 | source-text | 10-Q_2026-06-30_amcx-20260630.htm.jsonl | S4 | page:6 | CP-1, CP-1A | Sourced | High | |
| $87 million repurchase authorization remaining | source-text | EX-99.1_2026-07-30_amcx-73026ex991.htm.jsonl | S7 | page:4 | CP-1, CP-1A | Sourced | Medium | Management release |
| Dolan Family Group owns all Class B and about 79% of voting power outside director elections | source-text | 10-K_2025-12-31_amcx-20251231.htm.jsonl | S1 | page:72-73, Item 1A | CP-1A ownership | Sourced | High | At December 31, 2025 |
| Guarantees "on an unsecured basis" | source-text | 10-K_2025-12-31_amcx-20251231.htm.jsonl | S1 | page:112; S4 page:60 | CP-1A conflicts | Conflicting | High | Against first-priority lien at S1 page:171 |
| Damages claim above $200 million; trial October 27, 2026 | source-text | 10-Q_2026-06-30_amcx-20260630.htm.jsonl | S4 | page:24, Note 14 | CP-1A, CP-2 | Sourced | High | |
| Netflix licence $500 million and expected cash timing | source-text | 10-Q_2026-06-30_amcx-20260630.htm.jsonl | S4 | page:10, 68; S7 page:4 | CP-1A subsequent events | Sourced as management expectation | Medium | Contract not supplied |
| Credit-agreement ratios 5.11x and 1.85x at March 31, 2026 | source-text | EX-99.1_2026-05-08_amcx-50826ex991.htm.jsonl | S6 | page:10 | CP-1 covenant rows | Sourced | Medium | Facility ended later |
| Maximum net leverage 5.75x through March 31, 2026 | source-text | 10-Q_2026-03-31_amcx-20260331.htm.jsonl | S3 | page:14 | CP-1 calculation C9 | Sourced | High | |
| Run-rate coupon 155,955 thousand | calculation in CP-1 | Not applicable: derived | S4 | page:16 inputs | CP-1 calculation C8 | Calculated | Medium | Uses printed rates and principal |
| Cash 502,379 thousand at December 31, 2025 | source-text | 10-K_2025-12-31_amcx-20251231.htm.jsonl | S1 | page:133 | CP-1 liquidity | Sourced | High | |
| Cash 552,137 thousand at March 31, 2026 | source-text | 10-Q_2026-03-31_amcx-20260331.htm.jsonl | S3 | page:2 | CP-1 liquidity | Sourced | High | |
| AMC reached approximately 55 million subscribers; streaming 10.4 million | source-text | 10-K_2025-12-31_amcx-20251231.htm.jsonl | S1 | page:9, 13 | CP-1A profile | Sourced | High | Nielsen estimate and company count |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Twelve-month AOI to June 30, 2026 | CP-1 chart rows, CP-2 | 411,874 + 115,042 - 213,871 | FY2025 plus six months 2026 less six months 2025 = 313,045 thousand | Calculated | Recomputed, equals printed | High | Leverage, refinancing | S5 page:11; S7 page:11 |
| Net debt | CP-1, CP-2 | Principal less cash | 1,735,554 - 463,996 = 1,271,558; 1,778,251 - 502,379 = 1,275,872 | Calculated | Recomputed, equals printed | High | Leverage | S4 page:2, 16; S7 page:11 |
| Total debt and net debt to AOI | CP-1, CP-2 | Above | 5.54x and 4.06x (June 2026); 4.32x and 3.10x (FY2025) | Calculated | Recomputed | High | Leverage | CP-1 C3 |
| AOI to cash interest paid | CP-1, CP-2 | AOI over twelve-month cash interest paid | 313,045 / 151,153 = 2.07x; 411,874 / 156,563 = 2.63x | Calculated | Recomputed | High | Debt service | CP-1 C2, C4 |
| Twelve-month free cash flow | CP-1, CP-2 | Operating cash flow less capital expenditures | 218,733 - 28,210 = 190,523 thousand | Calculated | Recomputed | High | Liquidity, cash conversion | S1 page:136; S4 page:5 |
| Run-rate contractual coupon and cover | CP-1 C8, CP-2 | Assumes principal at June 30, 2026 held for a year, excludes discount amortization and interest income | 138,085 + 11,760 + 6,109 = 155,954.7 thousand; 313,045 / 155,955 = 2.01x | Assumption-Based | Assumptions disclosed | Medium | Debt service | S4 page:16 |
| Reported-basis EBITDA ratios | CP-1 C7 | Operating income plus depreciation and amortization with no add-backs | 137,067 thousand twelve months; 12.66x total, 9.28x net, 0.91x cover | Calculated | Recomputed; includes non-cash impairment of 97,784 thousand | Medium | Definition sensitivity | S7 page:11; S1 page:134 |
| Covenant-style headroom at March 31, 2026 | CP-1 C9 | Reported ratios and printed limits | 5.75 - 5.11 = 0.64x; 1.85 - 1.50 = 0.35x | Calculated | Recomputed; limits stale after May 12, 2026 | Medium | Covenant history only | S6 page:10; S3 page:14 |
| Debt principal reduction | CP-1A, CP-2 | 2,369,385; 1,778,251; 1,735,554 | 633,831 thousand since December 31, 2024 | Calculated | Recomputed | High | Deleveraging behaviour | S1 page:167; S4 page:16 |
| Content cash spend against amortization | CP-1A | 415,429 less 343,056; 409,631 less 331,534 | 72,373 and 78,097 thousand | Calculated | Indicator only | Medium | Cash conversion | S4 page:5 |
| Exchange principal reconciliation | CP-1A | 830.6 + 30.7; 884 + 31.1; 875 - 861.3 | 861.3, 915.1 and 13.7 million; premium 53.8 million equals printed | Calculated | Recomputed | High | Refinancing | S4 page:18-19 |
| Netflix cash remainder | CP-1 C10 | 500 - 25 - 4 x 100 | About 75 million in 2031 | Assumption-Based | Management expectation | Low | Liquidity support | S4 page:68; S7 page:4 |

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Buybacks made under the amended covenant | Sources show the allowance and the purchase separately; the link is not stated | Analyst Inference | Overstates restricted-payment compliance evidence and could mislead on covenant capacity | Read as capacity and action separately; obtain the indenture | CP-2 reader summary and risk table |
| Material | 4.25% notes are junior to the secured notes | Label rests on instrument names; guarantee wording conflicts | Weak Lineage | Ranking drives loss given default reasoning | Remove the ranking label until the indentures are read | CP-2 key findings and weaknesses |
| Material | Leverage on "EBITDA" | Adjusted operating income used under an EBITDA label | Calculated | Definition drift against covenant and market EBITDA | Keep the AOI label in every downstream use | CP-1 chart rows, CP-2 |
| Minor | Content licensing fall explained by delivery timing | Percentage and explanation relate to different scopes | Analyst Inference | Slightly overstates the explained share | Cite the Domestic percentage with the explanation | CP-1A credit translation 1 |
| Minor | Accelerated share repurchase equals the six-month treasury purchase | Not stated by the filing; consistent with the equity statement | Analyst Inference | Avoids double counting of cash returned | Keep as interpretation | CP-1A calculations |
| Material | Ranking and collateral of the 2032 notes | Filing wording conflicts | Conflicting | Recovery mechanics depend on it | Obtain the indenture and security documents | CP-0, CP-1, CP-1A, CP-2 |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings cover FY2025 to June 30, 2026; no debt contracts or later filings | Missing indentures leave covenant and ranking claims on summaries | Covenant, distribution and ranking uses are restricted | Add indentures and any filing to 2026-11-05 |
| Citation completeness | Ready with Remediation | All source figures found on cited pages; two overstated phrases found | Overstatement lets an inference read as a fact | Wording defects can mislead a committee on covenant use | Correct the two phrases when the work is next revised |
| Calculation traceability | Committee-Ready | Every derived figure recomputed to the same value | Formulas are shown with inputs | Ratios can be relied on within their definitions | None beyond definition labels |
| Assumption transparency | Ready with Remediation | Run-rate coupon and Netflix timing assumptions are labelled; adjusted operating income label drifts | Unlabelled definition shifts distort comparison | Leverage cannot be compared with covenant ratios | Keep AOI naming and the stated bases |
| Markdown artifact integrity | Committee-Ready | Required headings, selectors and tables present in all four handoffs; sha256 hashes match | Structural defects would break delivery | No delivery risk found | None |

Overall auditability is the lowest dimension: Ready with Remediation.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed indentures and security documents | Indenture text for the 2032, 4.25% senior and convertible notes | Restricted-payment capacity, covenants and ranking decide creditor control | Covenant, distribution and ranking statements remain summaries | High impact | Indentures and supplemental indentures |
| CP-5-GAP-002 | Filings after July 30, 2026 | Any 10-Q or 8-K to the as-of date | Trial outcome, refinancing and third-quarter results unknown | All findings are to June 30, 2026 | Medium impact | EDGAR filings to 2026-11-05 |
| CP-5-GAP-003 | Ratings and market data | Ratings and trading levels | Refinancing access cannot be judged | No relative or market statement is made | Medium impact | Rating agency reports, quotes |
| CP-5-GAP-004 | Netflix agreement | Contract terms | Cash timing is a management expectation | Support from the licence is unverified | Medium impact | Agreement or its summary |
| CP-5-GAP-005 | Customer in Chapter 11 | Identity and exposure | Counterparty loss cannot be sized | Concentration risk unquantified | Low impact | Later filings |
| CP-5-GAP-006 | Streaming unit economics | Churn, revenue per user, acquisition cost | Streaming durability rests on reported counts and price increases | Revenue durability judgment is bounded | Medium impact | Company disclosures |
| CP-5-GAP-007 | Page-level fidelity of extracted tables | Original filing layout | Text extraction can misalign rows and columns | Figures rechecked here against totals and printed values | Low impact | Original filing documents |

#### T5.1 QA source gate and input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/.../1.response.md, sha256 35f530dc; run amcx-2026-11-05-credit_snapshot-host | Source readiness for seven filings | High | Six headings and readiness view present | Accepted by CP-OS structural gate; analytical review here | READY_WITH_LIMITATIONS; limitations L1 to L11 |
| CP-1 | requests/CP-1/.../1.response.md, sha256 746b9708; same run | Financial base to June 30, 2026 | High | Six headings, four chart selectors and one table present | Accepted by CP-OS structural gate; analytical review here | Adjusted operating income used as the earnings base |
| CP-1A | requests/CP-1A/.../1.response.md, sha256 2e989982; same run | Business, control, transactions | High | Six headings, two tables and prose selector present | Accepted by CP-OS structural gate; analytical review here | Indentures not supplied |
| CP-2 | requests/CP-2/.../1.response.md, sha256 1514d8cc; same run | Credit synthesis | Medium | Six headings and two prose selectors present | Accepted by CP-OS structural gate; analytical review here | Two overstated phrases found |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-2 | Buybacks made under the amended covenant (reader summary, risk table) | Partly supported | Allowance and purchase are both cited but their link is not stated in the sources | Use the capacity and action wording of the business handoff | Restricts covenant and distribution uses |
| Material | CP-2 | 4.25% notes are junior (key findings, weaknesses) | Inference | Rests on instrument names against conflicting guarantee wording | Treat as unsupported ranking | Restricts ranking and recovery uses |
| Minor | CP-1A | Content licensing decline explained by delivery timing | Partly supported | Percentage and timing explanation are for different scopes | Cite the Domestic percentage | None |
| Minor | CP-1A | Accelerated share repurchase equals treasury purchase | Inference | Consistent with the equity statement, not stated | Label as interpretation | None |
| Minor | CP-1 | Debt maturity years in chart rows | Supported by instrument labels | No maturity schedule in the 10-Q; years read from labels | Keep the stated basis | None |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Leverage and cover use adjusted operating income | Not EBITDA: it adds back share-based compensation, restructuring and impairment and adds equity-investee AOI | Company ratio of 4.1x uses net debt and finance leases; covenant ratios use credit-agreement definitions (4.41x and 5.11x) | Keep the AOI label and the stated bases | Ratios not comparable with covenant or market figures |
| Minor | CP-1 | Net debt excludes lease liabilities of 88,600 thousand and program rights obligations of 381,698 thousand | Definition choice, disclosed | None | None | None |
| Minor | CP-1 | Reported-basis ratios include a non-cash impairment of 97,784 thousand | Distorts run-rate, disclosed | None | None | None |
| Minor | CP-1 | Covenant headroom at March 31, 2026 uses limits that ended with the facility | Stale after May 12, 2026, disclosed | None | None | Headroom is history only |

All eleven C-numbered calculations in CP-1 and the calculations in CP-1A were recomputed from the cited inputs; no arithmetic differences were found.

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A, CP-2 | 2032 notes are secured on a first-priority basis, and guarantees are "on an unsecured basis" | 2032 notes indenture and security documents | Filing wording conflicts | Obtain documents before any ranking statement | Required before ranking or recovery use |
| Material | CP-1A | Amended indenture allows up to $50.0 million of equity repurchases | Indenture and supplemental indenture | Only a summary is supplied; other baskets unknown | Read the restricted-payment covenant | Required before distribution capacity use |
| Minor | CP-1A | Convertible notes carry a holder put on a fundamental change | Convertible notes indenture | Filing risk factor only | Read the indenture | Low |
| Minor | CP-1 | Credit agreement and revolver ended May 12, 2026 | Payoff or termination notice | Filing statement only | None for financial use | Low |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | All | No market, spread or relative-value claim is made in any handoff | Ratings, prices, spreads and peer data | Run settings leave them blank | Add market data before any relative-value step | None for the present modules |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-1A, CP-2 | Buyback capacity (CP-1A, separate columns) against buybacks made under the covenant (CP-2) | Later module overstates the earlier one | Use the CP-1A wording | Distribution capacity must not be inferred |
| Material | CP-1A, CP-2 | CP-1A holds ranking open; CP-2 labels the 4.25% notes junior | Later module narrows an open item | Hold ranking open | Ranking and recovery uses restricted |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Figures agree across modules (net debt, AOI, leverage, cover, maturities, cash); no numeric conflict found | Old and new company names across sources | Map the name change when citing | None |
| Minor | CP-1, CP-2 | CP-1 amounts in USD thousands, CP-2 in USD millions | Unit style differs, values match after conversion | Show conversion | None |
| Minor | CP-1A | MFN trial date moved from March 26, 2026 to April 21, 2026 and to October 27, 2026 | Dates change over time, not a conflict | Cite the latest filing | None |

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | Duplication | The indenture limitation recurs in each handoff | State once in the committee note | Readability only |
| Material | CP-2 | Materiality | Two overstated phrases sit in the reader summary and risk table, the places a committee reads first | Correct before committee circulation | Could mislead on covenant and ranking |
| Minor | CP-1 | Materiality | Reported-basis ratios (12.66x total) are shown beside adjusted ratios and could be read as run-rate | Present adjusted ratios first with the impairment caveat | Low |
| Material | All | Committee readiness | Covenant, restricted-payment and ranking questions cannot be answered from the supplied sources | Restrict those uses | Committee status Restricted for them |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | Reader summary tables | No module codes or hashes in the reader summaries; word limits met; no defect in headings, selectors or table shape found | None | None |
| Minor | CP-1, CP-2 | Unit and period labels | Thousands and millions used in different modules; labels present in every table | Keep conversion note | None |
| Minor | CP-1A | Citations | Credit translations cite pages in brackets rather than in a table | Acceptable under the presentation rules | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP-5-ISS-001 | Material | CP-2 | Overstated claim | Buybacks described as made under the amended covenant | Use capacity and action wording | Restricts distribution uses | Open |
| CP-5-ISS-002 | Material | CP-2 | Weak lineage | 4.25% notes called junior to the secured notes | Hold ranking open | Restricts ranking uses | Open |
| CP-5-ISS-003 | Material | CP-1, CP-2 | Definition drift | EBITDA label on adjusted operating income | Keep the AOI label | Ratios not comparable with covenant figures | Open |
| CP-5-ISS-004 | Material | CP-1, CP-1A, CP-2 | Conflict | Guarantee "unsecured" wording against first-priority lien description | Obtain indentures | Restricts ranking and recovery uses | Open |
| CP-5-ISS-005 | Material | All | Evidence gap | Executed indentures not supplied | Obtain indentures | Restricts covenant uses | Open |
| CP-5-ISS-006 | Minor | CP-1A | Scope mismatch | Licensing decline percentage and explanation relate to different scopes | Cite the Domestic percentage | None | Open |
| CP-5-ISS-007 | Minor | CP-1A | Inference | Accelerated share repurchase equated to the treasury purchase | Label as interpretation | None | Open |
| CP-5-ISS-008 | Minor | CP-1 | Basis | Maturity years read from instrument labels | Keep the stated basis | None | Open |

## Calculations

The review recomputed every derived figure in the earlier handoffs from the cited source values; results match the earlier values exactly.

- Twelve-month builds: revenue 2,311,801 + 1,089,622 - 1,155,257 = 2,246,166; operating income 133,322 + 47,115 - 128,666 = 51,771; depreciation and amortization 94,425 + 38,243 - 47,372 = 85,296; interest expense 172,353 + 84,012 - 85,852 = 170,513; adjusted operating income 411,874 + 115,042 - 213,871 = 313,045 and 411,874 + 68,974 - 104,485 = 376,363; operating cash flow 305,670 + 124,659 - 211,596 = 218,733; capital expenditures 33,303 + 16,577 - 21,670 = 28,210; free cash flow 218,733 - 28,210 = 190,523. All in USD thousands.
- Cash interest paid: 156,563 + 78,984 - 84,394 = 151,153 (June 2026) and 156,563 + 77,983 - 76,736 = 157,810 (March 2026).
- Net debt: 1,778,251 - 502,379 = 1,275,872; 1,829,284 - 552,137 = 1,277,147; 1,735,554 - 463,996 = 1,271,558. Debt tables add to printed totals: 276,706 + 143,750 + 1,315,098 = 1,735,554.
- Ratios (adjusted operating income basis): total debt 4.32x, 4.86x, 5.54x; net debt 3.10x, 3.39x, 4.06x; cover 2.63x, 2.38x, 2.07x for FY2025, March 2026 and June 2026. Company-style check with finance leases: 1,285,440 / 313,045 = 4.11x, matching the printed 4.1x.
- Run-rate coupon: 1,315,098 x 10.50% = 138,085; 276,706 x 4.25% = 11,760; 143,750 x 4.25% = 6,109; total 155,955; 313,045 / 155,955 = 2.01x.
- Reported-basis ratios: 227,747, 195,308 and 137,067 thousand earnings give total debt 7.81x, 9.37x and 12.66x; net debt 5.60x, 6.54x and 9.28x; cover 1.45x, 1.24x and 0.91x.
- Headroom at March 31, 2026: 5.75 - 5.11 = 0.64x; 1.85 - 1.50 = 0.35x.
- Debt principal reduction: 2,369,385 - 1,778,251 = 591,134; 1,778,251 - 1,735,554 = 42,697; 2,369,385 - 1,735,554 = 633,831 thousand. Exchange: 830.6 + 30.7 = 861.3; 884 + 31.1 = 915.1; 915.1 - 861.3 = 53.8; 875 - 861.3 = 13.7 million. Content cash spend: 415,429 - 343,056 = 72,373 and 409,631 - 331,534 = 78,097 thousand.
- Source-figure search: every comma-formatted figure in the financial base, business and synthesis handoffs was searched in the source text; all figures not found verbatim are the derived values listed above. Every amount in the financial base table with a page locator was found on the cited page, except that the contractual obligations are printed as $590.3 million, equal to the 590,300 thousand shown.

## Gaps

- Not supplied: executed indentures, supplemental indentures and security documents; covenant, restricted-payment and ranking claims stay at summary level (CP-5-GAP-001).
- Not supplied: any filing after July 30, 2026, ratings, market data, the Netflix agreement, and the identity and exposure of the customer in Chapter 11 (CP-5-GAP-002 to 005).
- Not disclosed in the pages searched: streaming churn, revenue per user and acquisition cost (CP-5-GAP-006).
- Confidence score and band: Not calculable here; the scoring script is not part of host mode, so the status is stated as Restricted for covenant, distribution and ranking uses and Ready with Remediation for the rest.
- The review cannot repair earlier handoffs; the corrections above stand as this review's statement of what the earlier text should have said.
- Text-only extraction: page-level table alignment was checked against printed totals, not against original filing layouts (CP-5-GAP-007).

## Next module

The run ends here for the minimum set. Anyone using the report should carry the two corrections: buyback capacity and buybacks made are separate facts, and note ranking is open; and should restrict covenant, distribution and ranking conclusions until the indentures and any filing to 2026-11-05 are added.
