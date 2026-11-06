# CP-5 Evidence trace and research integrity QA for TripAdvisor, Inc. (trip), as of 2026-11-05

## Request

Issuer: TripAdvisor, Inc. (ticker TRIP). As-of date and evidence cutoff: 2026-11-05. Pathway: credit_snapshot, run trip-2026-11-05-credit_snapshot-host. Scope: Top 5 credit drivers traced in full, plus every other material conclusion in the four upstream handoffs (source readiness, financial base, business and transaction context, fundamental credit synthesis), each reopened against the pinned filings and releases. This is a governance layer: it does not change any credit conclusion, assign a rating or silently repair a citation. Currency USD; amounts in millions unless stated.

## Sources

### Upstream handoffs audited

| Module | sha256 | Run |
| --- | --- | --- |
| CP-0 | 11450ae719794e17a2469c6eb5fd603263c2713efb400c29bf944a61ffe15423 | trip-2026-11-05-credit_snapshot-host, accepted |
| CP-1 | 52dc3cd3371b0b989b27c5d8c2038a957dbe47bc633b57645cba56bfe8b410a1 | trip-2026-11-05-credit_snapshot-host, accepted on attempt 2 |
| CP-1A | 90268fe24a5e8556b4ec4598fb670803d14280bd3c48d425e5571a802456bf47 | trip-2026-11-05-credit_snapshot-host, accepted |
| CP-2 | 732246cf0aa78d6772a6de880751f85792ab8ebc08af374c06d9161ea899f19c | trip-2026-11-05-credit_snapshot-host, accepted |

### Issuer sources reopened for tracing

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_trip-20251231.htm.jsonl | 8885b42791d5e90823a0c9c46491e45285d32d010f68b9715cb0b383be7e31bf |
| 10-Q_2026-03-31_trip-20260331.htm.jsonl | 9289cc81c4291efc67a199ffd3d95096f8d91f0c627c0d49a15ca4c0525a91f8 |
| 10-Q_2026-06-30_trip-20260630.htm.jsonl | 358dea410a455694571e6fd8ed4ffb768fc6929fddacda37801383944ce9f7e1 |
| 10-Q_2026-09-30_trip-20260930.htm.jsonl | 37e12b49f799525884b2d1c8f8223439d80dbaee990e3c8305474f0abf40c5c7 |
| EX-99.1_2026-05-07_trip-ex99_1.htm.jsonl | 986da54f4628e6ef7caa0f060a29736fbe7ef71884de15f953b1b79776621916 |
| EX-99.1_2026-08-06_trip-ex99_1.htm.jsonl | 4b5f625f62e6af22d7ff5c0ad78ab3c67f22ed4bd26c03b70a227ec22f7f24b0 |
| EX-99.1_2026-11-05_trip-ex99_1.htm.jsonl | 08c99d197b1e28c92053c736e4c07c927f197a67f49f8aceaed0f5db801c0a1c |

Run context (settings only, not issuer evidence): 1fa2d7822828d80dbe527b9dde9239ab274e8339a7a989f9acc6255a06577c7a.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial base, business context and credit view trace to the filings and releases, and the key numbers recompute. Only minor locator, label and presentation defects were found; no claim is orphaned. | Medium | The credit agreement, sale agreements and covenant ratio are not supplied, so legal and covenant claims rest on filing summaries and cannot be traced to clauses. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Of 15 material claims, 5 are directly sourced, 6 are calculated from sourced parts, 3 are analyst inference and 1 has no evidence. | Most committee-facing numbers can be rebuilt from filings, so the credit view rests on checkable inputs. | High |
| LTM Adjusted EBITDA of 207.3 recomputes from filed nine-month figures plus a release-only Q4 2025 quarter, and a filed segment table agrees within rounding. | The central leverage and cover metrics are reproducible, but one quarter of the earnings base is management data. | Medium |
| Five minor defects were found: page slips, a debt basis difference, a mislabelled context fact, mismatched severity scales and a reliance on filing summaries for legal terms. | None changes a conclusion; fixing them improves auditability for committee use. | High |
| Covenant headroom cannot be traced: the 4.5 to 1.0 maximum appears only in the annual report and no reported ratio is printed for 2026. | No headroom conclusion should be drawn, and the leverage ratios shown are not the covenant ratio. | High |
| The post-sale cash position and the intent to repay debt trace only to management statements and an illustrative calculation. | Treat post-sale deleveraging as unproven until proceeds are applied to debt. | Medium |

### Evidence trace view

The upstream analysis is traceable enough for a bounded credit snapshot, and its central numbers can be rebuilt from filed documents. Of 15 material claims, 5 are directly sourced, 6 are calculated from sourced components, 3 are analyst inference and 1 lacks evidence. The strongest trace is the Q3 2026 10-Q for debt, cash and nine-month earnings. The weakest is the Q4 2025 quarter inside LTM Adjusted EBITDA, which comes from a management release, although a filed 10-K segment table agrees within rounding once re-allocated stranded costs are considered. The most important provenance gap is the missing credit agreement, so covenant and collateral claims cannot be traced to clauses. The decision affected is any reliance on covenant headroom or lender protections.

### Traceability conclusion

Auditability is Ready with Remediation. Every material conclusion has either a located source, a shown calculation that reproduces, or an explicit limitation flag, so no conclusion meets the orphan-claim test. The remediation is cosmetic and presentational (locator pages, a carrying-basis leverage ratio, one category label, one severity mapping) plus one substantive follow-up that CP-5 cannot perform: obtain the credit agreement and amendments so that covenant, collateral and asset-sale claims can be traced to clauses. Committee status is Draft Only: the snapshot is fit to frame a discussion but not to support a covenant, collateral or recovery decision. Sources outrank the management releases where they overlap; no release figure overrides a filing in the upstream work.

### Traceability summary

| Lineage class | Material claims | Example |
| --- | --- | --- |
| Directly Sourced | 5 | Term Loan B of 833.9 with no financial covenant |
| Calculated | 6 | LTM Adjusted EBITDA of 207.3 |
| Analyst Inference | 3 | Debt reduction from sale proceeds |
| Insufficient Information | 1 | Covenant headroom |

### Confidence and QA status

Computed with the repository's confidence script, not by hand: lineage counts Directly Sourced 5, Calculated 6, Analyst Inference 3, Insufficient Information 1 (15 claims); required envelope fields present 8 of 10 (the filename convention and invocation digest are replaced by the launcher's hashes under host transport); source gate pass (every traced claim has its source in the pack); findings MINOR 5. Result: E = 77.33, C = 80.0, S = 1.0, P = 15; score = clamp((0.6 x 77.33 + 0.4 x 80) x 1.0 - 15, 0, 100) = 63.4, reported as 63. Confidence band Medium; QA status Passed; committee status Draft Only. The automated validator and completeness scripts named in the method are not present in the repository, so structural validation is left to the launcher's own acceptance check.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_trip-20251231.htm.jsonl | High: audited annual report | FY2025 (year ended December 31, 2025) | Tripadvisor, Inc. consolidated including TheFork | Debt terms, covenant maximum, security, contractual obligations, business description, segment tables | Whole USD millions; old perimeter | Debt and covenant terms; business context |
| S2 | 10-Q_2026-03-31_trip-20260331.htm.jsonl | High: unaudited filing | Q1 2026 | Consolidated including TheFork | Cash interest, Q1 balance sheet, debt, cooperation agreement exhibit | Old perimeter; no continuing-operations Q1 | Cash interest and liquidity series; governance |
| S3 | 10-Q_2026-06-30_trip-20260630.htm.jsonl | High: unaudited filing | Q2 2026, six months | Continuing operations (TheFork discontinued) | Q2 balance sheet, six-month cash flow, debt | Unaudited | Liquidity and interest series |
| S4 | 10-Q_2026-09-30_trip-20260930.htm.jsonl | High: unaudited filing | Q3 2026, nine months | Continuing operations (TheFork discontinued) | Latest statements, debt note, goodwill, liquidity, sale of TheFork, subsequent events | Unaudited | Primary source for the current position |
| S5 | EX-99.1_2026-05-07_trip-ex99_1.htm.jsonl | Medium: management release | Q1 2026 | Consolidated including TheFork | Management narrative on portfolio simplification | Supporting claims only; old perimeter | Management language only |
| S6 | EX-99.1_2026-08-06_trip-ex99_1.htm.jsonl | Medium: management release | Q2 2026 | Continuing operations | Management narrative on asset value; pending sale | Supporting claims only | Management language only |
| S7 | EX-99.1_2026-11-05_trip-ex99_1.htm.jsonl | Medium: management release with reconciliations | Q3 2026 with 2025 quarterly continuing series | Continuing operations | Quarterly 2025 and 2026 continuing series, restructuring and savings claims | Unaudited, non-GAAP measures | Q4 2025 leg of LTM Adjusted EBITDA; segment series |
| C0 | 1526520-tripadvisor-inc-trip.json | Run context only | As of 2026-11-05 | Tripadvisor, Inc. | Dates, currency, identity labels | Not issuer evidence | Identity and scope |
| M0 | CP-0 handoff | Upstream analysis | 2026-11-05 | Tripadvisor, Inc. | Readiness, perimeter, gap register | Analysis, not source | Scope and authority ranking |
| M1 | CP-1 handoff | Upstream analysis | Q3 2026, LTM, FY2025 | Continuing operations | Financial base | Analysis with calculations | Audited here |
| M1A | CP-1A handoff | Upstream analysis | 2026-11-05 | Tripadvisor, Inc. | Business, transaction, governance | Analysis with tags | Audited here |
| M2 | CP-2 handoff | Upstream analysis | 2026-11-05 | Tripadvisor, Inc. | Credit synthesis | Upstream-only synthesis | Audited here |

Module status: Ready with Limitations. All four upstream handoffs are present and accepted, so CP-5 is not blocked.

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Earnings decline concentrated in Hotels and Other | CP-1, CP-2 | LTM Adjusted EBITDA 207.3 against 294.7 for FY2025; Hotels and Other 143.6 of 207.3 | Debt service depends on the shrinking segment | Sets the direction of every credit ratio | S4 page:47, page:34; S7 page:13, page:16; S1 page:186 | Q4 2025 quarter is release data |
| 2 | Leverage and interest cover on Adjusted EBITDA | CP-1, CP-2 | Gross 4.02x, net 0.61x, net of operator payables 2.53x, cover 3.50x | Defines debt tolerance | Frames the leverage discussion | S4 page:3, page:62, page:7; S3 page:6; S1 page:110 | Management EBITDA adds back stock-based compensation; not the covenant ratio |
| 3 | Liquidity net of operator float and seasonal cash flow | CP-1, CP-1A, CP-2 | Cash 706.8, undrawn revolver 497.7, deferred merchant payables 396.8, LTM free cash flow -17.5 | Cash overstates usable liquidity in the second half | Determines the real liquidity cushion | S4 page:3, page:61, page:64, page:6; S7 page:14 | Seasonal low not tested at year end |
| 4 | Debt structure and covenant | CP-1, CP-1A, CP-2 | Term Loan B 833.9 due 2031 with no financial covenant; revolver maximum 4.5 to 1.0 | Fixes maturities and creditor protections | Shows no near-term maturity wall | S4 page:62, page:25; S1 page:161, page:163 | Credit agreement not supplied |
| 5 | Use of TheFork sale proceeds | CP-1A, CP-2 | Net cash of about 741.0 received November 1, 2026; management expects to prioritise debt reduction | Could cut leverage sharply | Key swing factor for the outcome | S4 page:11, page:65 | Intent, not commitment; prepayment terms unknown |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C1 LTM Adjusted EBITDA 207.3 against 294.7 for FY2025 | CP-1 | S4 page:47 (nine months 163.9 and 251.3); S7 page:13 (quarters, Q4 2025 43.4); S1 page:186 cross-check | Yes | Filing plus management release | Calculated | Reproduced; Q4 2025 leg release-sourced | Medium | Committee-Ready |
| C2 Hotels and Other is about 69% of LTM Adjusted EBITDA and shrinking | CP-1, CP-2 | S7 page:16, page:14; S4 page:34 | Yes | Filing plus management release | Calculated | Reproduced | High | Committee-Ready |
| C3 Gross leverage 4.02x, net 0.61x, net of float 2.53x | CP-1, CP-2 | S4 page:62, page:3 | Yes | Filing | Calculated | Reproduced; carrying-basis ratio missing | Medium | Remediation Needed |
| C4 LTM interest cover 3.50x | CP-1, CP-2 | S4 page:7; S3 page:6; S1 page:110 | Yes | Filing, FY input in whole millions | Calculated | Reproduced | Medium | Committee-Ready |
| C5 Liquidity of 1,204.5 | CP-1, CP-2 | S4 page:3, page:61 | Yes | Filing | Calculated | Reproduced | High | Committee-Ready |
| C6 Term Loan B of 833.9 due 2031 with no financial covenant | CP-1, CP-2 | S4 page:62, page:25 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| C7 Revolver maximum total net leverage 4.5 to 1.0 | CP-1 | S1 page:161 | Yes | Audited filing | Directly Sourced | Verified | High | Committee-Ready |
| C8 Covenant headroom cannot be measured | CP-1, CP-2 | None: ratio not printed in 2026 filings | No | Absent | Insufficient Information | Gap logged, not adverse | Low | Not Traceable |
| C9 LTM free cash flow of -17.5 and Q3 operating cash flow of -122.0 | CP-1, CP-2 | S7 page:14; S4 page:6 | Yes | Filing plus release | Calculated | Reproduced | High | Committee-Ready |
| C10 TheFork sale closed for about 741.0 against a 700.0 headline | CP-1A, CP-2 | S4 page:11 | Yes | Filing | Directly Sourced | Verified; both figures logged as a conflict | High | Committee-Ready |
| C11 Proceeds will reduce debt | CP-1A, CP-2 | S4 page:65 states an expectation only | Yes | Filing, management statement | Analyst Inference | Intent, not commitment | Low | Remediation Needed |
| C12 Search-traffic dependency and Booking plus Expedia about 21% of FY2025 revenue | CP-1A, CP-2 | S1 page:23, page:26; S4 page:41 | Yes | Audited filing | Directly Sourced | Verified | High | Committee-Ready |
| C13 No controlling stockholder; cooperation agreement and activism costs | CP-1A, CP-2 | S1 page:59; S2 page:52, page:24 | Yes | Filing | Directly Sourced | Verified; agreement terms absent | Medium | Committee-Ready |
| C14 Governance behaviour is Neutral or Mixed with no documented creditor-adverse action | CP-1A | Derived from C10, C13 and 2025 flows | Partial | Filing facts, analyst reading | Analyst Inference | Tagged Analyst Interpretation | Low | Remediation Needed |
| C15 Overall credit view: comfortable liquidity, cautious on earnings direction | CP-2 | CP-1 and CP-1A rows | Yes | Upstream analysis | Analyst Inference | Tagged Analyst Interpretation | Medium | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Nine-month 2026 Adjusted EBITDA 163.9 and nine-month 2025 251.3 | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:47 | CP-1 Financials and credit metrics | Sourced | High | Reopened and matched |
| Quarterly Adjusted EBITDA 46.3, 97.2, 107.8, 43.4, 16.4, 76.4, 71.1 | runs/cpos-swarm-20261105-trip/source-text/ | EX-99.1_2026-11-05_trip-ex99_1.htm.jsonl | S7 | page:13 | CP-1 LTM build | Sourced | Medium | Management release; quarters sum to filed nine-month totals |
| Segment Adjusted EBITDA FY2025: Experiences 91, Hotels and Other 207, TheFork 21, total 319 | runs/cpos-swarm-20261105-trip/source-text/ | 10-K_2025-12-31_trip-20251231.htm.jsonl | S1 | page:186 | CP-5 cross-check | Sourced | High | Old perimeter, whole millions |
| Stranded costs re-allocated to continuing segments, 2.7 for nine months 2025 | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:34 | CP-5 cross-check | Sourced | High | Explains the gap between 298 and 294.7 |
| Term Loan B principal 833.9; short-term 8.5 and long-term 825.4 | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:62, page:24 | CP-1 Capital structure | Sourced | High | Reopened and matched |
| No financial covenants on the Term Loan B | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:62 | CP-1, CP-2 | Sourced | High | Direct statement |
| Maximum total net leverage ratio 4.5 to 1.0 solely for the Credit Facility | runs/cpos-swarm-20261105-trip/source-text/ | 10-K_2025-12-31_trip-20251231.htm.jsonl | S1 | page:161 | CP-1 Gaps | Sourced | High | Not repeated in 2026 filings |
| Cash 706.8 and undrawn capacity 497.7 | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:3, page:61 | CP-1 Liquidity | Sourced | High | Reopened and matched |
| Deferred merchant payables 396.8 | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:3 | CP-1 Capital structure | Sourced | High | Operator float |
| Cash paid for interest 43.1 (nine months 2026), 42.9 (nine months 2025) | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:7 | CP-1 Interest cover | Sourced | High | Consolidated line |
| Cash paid for interest FY2025 59 | runs/cpos-swarm-20261105-trip/source-text/ | 10-K_2025-12-31_trip-20251231.htm.jsonl | S1 | page:110 | CP-1 Interest cover | Sourced | High | Whole millions |
| Goodwill impairment 369.5 on Hotels and Other | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:22 | CP-1, CP-1A, CP-2 | Sourced | High | Reopened and matched |
| TheFork sale: 700.0 headline, 741.0 net cash at closing, 487.0 expected gain | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:11 | CP-1A Transaction summary | Sourced | High | Final amounts subject to adjustment |
| Management expects to prioritise reduction of long-term debt | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:65 | CP-1A, CP-2 | Sourced | Medium | Management statement of intent |
| Annualized savings of about $40 million for the November 2026 plan | runs/cpos-swarm-20261105-trip/source-text/ | EX-99.1_2026-11-05_trip-ex99_1.htm.jsonl | S7 | page:3 | CP-1A | Sourced | Medium | Release-only management claim, not in the 10-Q |
| Booking and Expedia about 21% and 22% of consolidated revenue | runs/cpos-swarm-20261105-trip/source-text/ | 10-K_2025-12-31_trip-20251231.htm.jsonl | S1 | page:26 | CP-1A Company and operating model | Sourced | High | Old perimeter |
| Google as a significant traffic source that promotes competing products | runs/cpos-swarm-20261105-trip/source-text/ | 10-K_2025-12-31_trip-20251231.htm.jsonl | S1 | page:23 | CP-1A | Sourced | High | Risk factor wording |
| No controlling stockholder since the LTRIP merger | runs/cpos-swarm-20261105-trip/source-text/ | 10-K_2025-12-31_trip-20251231.htm.jsonl | S1 | page:59, page:72 | CP-1A Company profile | Sourced | High | Reopened and matched |
| Cooperation Agreement dated March 22, 2026 | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-03-31_trip-20260331.htm.jsonl | S2 | page:52 | CP-1A Governance | Sourced | Medium | Exhibit listing only; terms absent |
| Hotels and Other revenue down 23% in Q3 2026; Experiences down 3% | runs/cpos-swarm-20261105-trip/source-text/ | EX-99.1_2026-11-05_trip-ex99_1.htm.jsonl | S7 | page:1 | CP-1, CP-2 | Sourced | Medium | Matches the filed figures on S4 page:34 |
| Term Loan B fair value 795.8 (September 30, 2026) and 811.1 (December 31, 2025) | runs/cpos-swarm-20261105-trip/source-text/ | 10-Q_2026-09-30_trip-20260930.htm.jsonl | S4 | page:20 | CP-1 Capital structure | Sourced | High | The 10-K prints 821 for December 31, 2025 |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA | CP-1 leverage, cover; CP-2 | Quarters 43.4, 16.4, 76.4, 71.1 | 43.4 + 16.4 + 76.4 + 71.1 = 207.3; also 294.7 - 251.3 + 163.9 = 207.3 | Recomputed, agrees | Reproduced | High | Denominator of every ratio | S7 page:13; S4 page:47 |
| FY2025 continuing Adjusted EBITDA cross-check | CP-5 | 10-K segments 91 and 207; release 294.7; stranded costs 2.7 for nine months 2025 | 91 + 207 = 298; 298 - 294.7 = 3.3, consistent in direction and size with re-allocated stranded costs (full-year amount not printed) | Recomputed, agrees within rounding | Corroborated | Medium | Supports release-only Q4 2025 leg | S1 page:186; S4 page:34 |
| Gross leverage | CP-1 chart; CP-2 | Principal 833.9 and 1,185; LTM and FY2025 EBITDA | 833.9 / 207.3 = 4.02; 1,185 / 294.7 = 4.02 | Recomputed, agrees | Reproduced | High | Debt tolerance | S4 page:62; S1 page:90 |
| Net leverage | CP-1 chart; CP-2 | Cash 706.8 and 978.0 | (833.9 - 706.8) / 207.3 = 0.61; (1,185 - 978.0) / 294.7 = 0.70 | Recomputed, agrees | Reproduced | High | Net debt tolerance | S4 page:3 |
| Net leverage net of operator float | CP-1; CP-2 | Deferred merchant payables 396.8 | (833.9 - (706.8 - 396.8)) / 207.3 = 523.9 / 207.3 = 2.53 | Recomputed, agrees | Reproduced | Medium | Usable-cash view | S4 page:3 |
| Carrying-basis gross leverage | CP-5 | Carrying 822.9 (8.5 + 814.4) and 1,172.2 (353.2 + 819.0) | 822.9 / 207.3 = 3.97; 1,172.2 / 294.7 = 3.98 | New CP-5 calculation | Reproduced | High | Canonical debt basis; difference to principal basis 0.05x | S4 page:3, page:20 |
| LTM cash interest and cover | CP-1 chart; CP-2 | 59, 42.9, 43.1 | 59 - 42.9 + 43.1 = 59.2; 207.3 / 59.2 = 3.50 | Recomputed, agrees | Reproduced | Medium | Debt service | S1 page:110; S4 page:7 |
| After stock-based compensation | CP-1; CP-2 | LTM SBC 19.7 + 50.5 = 70.2 | 207.3 - 70.2 = 137.1; 833.9 / 137.1 = 6.08; 137.1 / 59.2 = 2.32 | Recomputed, agrees | Reproduced | Medium | Earnings quality | S7 page:12; S4 page:2 |
| LTM free cash flow | CP-1; CP-2 | Operating cash flow 27.4, capex 44.9 | -103.0 + 130.4 = 27.4; 13.1 + 31.8 = 44.9; 27.4 - 44.9 = -17.5 | Recomputed, agrees | Reproduced | High | Cash conversion | S7 page:14; S4 page:6 |
| Liquidity | CP-1; CP-2 | Cash 706.8, undrawn 497.7, payables 396.8 | 706.8 + 497.7 = 1,204.5; 1,204.5 - 396.8 = 807.7 | Recomputed, agrees | Reproduced | High | Liquidity cushion | S4 page:3, page:61 |
| Maturity profile | CP-1 chart | Principal 833.9; 1.00% annual amortisation; 10-K table 9, 17, 17, 797 | 2.1 + 4 x 8.5 + 797.8 = 833.9 | Recomputed, agrees; assumption: quarterly installments of 0.25% of 850.0 | Reproduced | Medium | Refinancing wall | S4 page:62; S1 page:95 |
| Hotels and Other share | CP-1; CP-2 | 143.6 and 207.3 | 143.6 / 207.3 = 69.3% | Recomputed, agrees | Reproduced | High | Earnings concentration | S7 page:16 |
| Illustrative post-sale cash | CP-1; CP-2 | Cash 706.8, proceeds 741.0, principal 833.9 | 706.8 + 741.0 - 833.9 = 613.9 | Recomputed, agrees; labelled illustrative | Reproduced | Low | Size of deleveraging option | S4 page:3, page:11 |
| Nine-month Adjusted EBITDA bridge | CP-1 | -321.6, 56.5, 369.5, 50.5, 7.8, 1.9, 4.1, -4.8 | -321.6 + 56.5 + 369.5 = 104.4; plus 50.5 + 7.8 + 1.9 + 4.1 - 4.8 = 163.9 | Recomputed, agrees | Reproduced | High | Definition review | S4 page:2; S7 page:12 |

#### T5B.6 Missing citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 liquidity, capital structure and debt rows | Locator slips: the FY2025 liquidity row cites page 61 for the 500.0 commitment and 3.6 of letters of credit (printed on page 62) and page 3 for 1,034.9 (printed on page 6); carrying values 8.5 and 814.4 are cited to page 20 (printed on page 3); 345.4 is cited to pages 25 to 26 (printed on page 62); the original principal 850.0 is not on the cited pages (printed in the 10-K market-risk text). | Directly Sourced, locator imprecise | A reviewer following the cited page will not find the number | Correct the five locators in a later revision | CP-1 chart data: liquidity; Capital structure table |
| MINOR | CP-1A Company profile, country and sector | The row is tagged Documentary Fact though its own text says the labels come from the run context, not issuer evidence | Category label | Mislabels the evidence class | Re-tag as context label or Insufficient Information | CP-1A Company profile |
| MINOR | CP-1 leverage | Ratios use principal; the canonical debt basis is balance sheet carrying value; the difference (11.0) is shown in the capital table but no carrying-basis ratio is given; printed nil balances are shown as 0.0 | Presentation | A reader cannot see the canonical-basis ratio of 3.97x without calculating it | Add the carrying-basis ratio and show printed nil as a dash | CP-1 chart data: leverage |
| MINOR | CP-1A and CP-2 gap severities | Gap severities use High, Medium and Low rather than CRITICAL, MATERIAL and MINOR | Version issue | Scales differ across modules | Map to the three-level scale (credit agreement gap would map to MATERIAL) | CP-1A Gaps; CP-2 Gaps |
| MINOR | CP-1A, CP-2 legal and structural statements | Security over substantially all assets, the 4.5 to 1.0 maximum and the absence of creditor-adverse action rest on 10-K summaries; the credit agreement is not in the pack | Insufficient Information on clause detail | Clause-level terms decide sale-proceeds use and priming risk | Keep clause detail tagged as gap; obtain the credit agreement | CP-1A governance table; CP-2 risks |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage and readiness | Ready with Remediation | All seven filings and releases retained in full; credit agreement and sale agreements absent | Missing legal text blocks clause-level tracing | Covenant, collateral and asset-sale terms cannot be relied on | Obtain the agreements |
| Claim-to-source lineage | Ready with Remediation | 15 claims traced; five locator slips and one mislabelled row | A reader following a cited page may not find a figure | Weakens reviewer confidence, not the conclusions | Correct locators and the label |
| Calculation reproducibility | Committee-Ready | Fourteen calculation items recomputed and agreeing; inputs and formulas shown | A hand error would mis-state leverage | None found | Add carrying-basis ratio |
| Conflict and version handling | Committee-Ready | Sale size, fair value, HMRC range and rate differences logged and not reconciled; subsequent events kept out of period figures | Silent reconciliation would hide disagreement | None found | None |
| Committee readiness and handoff integrity | Ready with Remediation | No orphan claims; analyst inference tagged; severity scales differ | Inference could be read as fact | Draft Only until legal terms are traced | Map severities |

Overall auditability: Ready with Remediation.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G-1 | Credit agreement and amendments | Text of the Amended Credit Agreement, three amendments and Security Documents | Defines covenant, collateral, guarantors, asset-sale and prepayment terms | Legal capacity stays untested | High | Exhibits listed in the 10-K exhibit index |
| G-2 | Covenant ratio | Issuer-reported total net leverage ratio for 2026 | Needed to measure headroom | Headroom not calculable | High | Compliance certificate |
| G-3 | Filed continuing-operations base | Q4 2025 and FY2025 continuing interest, operating income, cash flow statement | The Q4 2025 leg of LTM comes from a release | Medium trace weakness, mitigated by the segment cross-check | Medium | Recast annual or 8-K |
| G-4 | Sale agreements | Equity Purchase Agreement, Put Option Agreement, Transition Services Agreement | Final consideration and proceeds usage | Post-sale position illustrative | Medium | Filed exhibits |
| G-5 | Ownership and cooperation agreement | Beneficial ownership table and agreement terms | Activism and control risk | Governance view partial | Medium | Proxy statement, March 22, 2026 filing |
| G-6 | Ratings, prices and guidance | Any credit rating, quote or forward guidance | No market cross-check | No relative-value claim is made | Low | External sources, labelled external |
| G-7 | Experiences unit economics | Commission rate, retention, operator concentration | Tests margin resilience of the growth segment | Growth thesis only partly testable | Medium | None in public filings supplied |
| G-8 | Automated QA scripts | The validator and completeness scripts named in the method are not in the repository | Mechanical register checks were done by hand | Structural validation left to the launcher | Low | Method owner |

#### T5.1 Module register and input gate

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/.../1.response.md; run trip-2026-11-05-credit_snapshot-host | Source readiness for four consumers | Analysis of seven sources | Six H2 headings present; reader summary and readiness view present | Passed | Perimeter break and gap register confirmed against the sources |
| CP-1 | requests/CP-1/.../2.response.md; run trip-2026-11-05-credit_snapshot-host | Financial base, four chart tables, metrics table | Filings plus release series | Six H2 headings; report selectors present once each | Passed | Accepted on attempt 2 after a word-count rejection; five locator slips found |
| CP-1A | requests/CP-1A/.../1.response.md; run trip-2026-11-05-credit_snapshot-host | Business, transaction, governance | Filings plus releases | Six H2 headings; company, profile and transaction selectors present once each | Passed | One mislabelled row |
| CP-2 | requests/CP-2/.../1.response.md; run trip-2026-11-05-credit_snapshot-host | Credit synthesis | Upstream only | Six H2 headings; key findings and strengths selectors prose only | Passed | Every figure traces to CP-1 or CP-1A |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Liquidity chart and capital structure table locators | Figures supported; page numbers wrong in five places | See locator slips in the weak-lineage register; the figures themselves match the sources | Correct locators | Formatting Only |
| MINOR | CP-1A | Company profile, country and sector row | Supported by the run context only | Tagged Documentary Fact though it is a context label | Re-tag the row | Formatting Only |

Coverage: 26 of the 27 quoted spans in CP-1A were found verbatim in the pinned sources (the 27th is the run-context sector label); every figure in CP-1 and CP-1A with a cited page was reopened, and every figure in CP-2 appears in CP-1 or CP-1A.

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Gross and net leverage use principal (833.9, 1,185) rather than carrying value (822.9, 1,172.2) | Canonical debt basis is carrying value; no carrying-basis ratio shown (3.97x and 3.98x here) | Principal 833.9 against carrying 822.9; difference 11.0 shown in the capital table | Add carrying-basis ratios | Monitoring Follow-Up |

Other checks passed: LTM construction uses consistent quarters; interest cover denominators are labelled consolidated cash interest with rounded FY input; net debt FY2025 mixes 10-K principal with continuing cash, and the mix is disclosed; the 0.2 difference between the nine-month 2025 operating cash flow in the 10-Q (337.5) and the release quarters (337.7) is disclosed.

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-1A, CP-2 | Term loan has no financial covenant; revolver carries a 4.5 to 1.0 maximum; obligations secured by substantially all assets; no creditor-adverse action documented | Amended Credit Agreement, three amendments, Security Documents | Clause text not in the pack; claims rest on filing summaries and are tagged accordingly | Keep tagged; obtain the documents | Legal review required before any reliance on covenant headroom, collateral scope, guarantor reach or sale-proceeds use |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None found | CP-1, CP-1A, CP-2 | No relative-value, spread, yield, price or ranking claim appears in any module; fair values of the term loan are reported as Level 2 estimates only | Ratings, bond or loan quotes, valuation inputs | Not applicable to claims made | None | No market claim to clear; relative value cannot be supported from this pack |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A, CP-2 | No numeric or categorical conflict found: leverage, liquidity, sale and governance figures agree across modules | Gap severities use High, Medium and Low; the audit scale is CRITICAL, MATERIAL and MINOR | Map the scales | None on conclusions |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| None found | CP-2 | Duplication | Key findings and strengths and weaknesses repeat figures by design of the report selectors; limitations are restated mainly in the gaps table; no promotional language found | None | Draft Only because legal documents are absent, not because of duplication |

#### T5.8 Handoff envelope and structure audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| None found | CP-0, CP-1, CP-1A, CP-2 | Six canonical headings, reader summary, opening view, report selectors | None: all required headings and selectors appear exactly once and in order; module hashes are listed in each Sources section | None | Handoffs are consumable by CP-5 and delivery |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-1 | MINOR | CP-1 | Citation | Five locator slips | Correct locators | Formatting Only | Open |
| I-2 | MINOR | CP-1A | Category label | Context label tagged Documentary Fact | Re-tag | Formatting Only | Open |
| I-3 | MINOR | CP-1 | Definition | Principal basis used; carrying-basis ratio and dash for nil missing | Add ratios | Monitoring Follow-Up | Open |
| I-4 | MINOR | CP-1A, CP-2 | Version | Severity scales differ from the audit scale | Map scales | Formatting Only | Open |
| I-5 | MINOR | CP-1, CP-1A, CP-2 | Legal | Clause detail not traceable without the credit agreement | Obtain documents | Requires Legal Review | Open |

## Calculations

All derived figures in the upstream handoffs were recomputed independently from the cited components; the full list with formulas is in the calculation register above. Results: every upstream calculation agreed to the precision shown. The only new calculations made here are the carrying-basis leverage (822.9 / 207.3 = 3.97x at September 30, 2026 and 1,172.2 / 294.7 = 3.98x at December 31, 2025, using carrying values of 8.5 + 814.4 and 353.2 + 819.0) and the segment cross-check (91 + 207 = 298 for FY2025 old-perimeter Experiences and Hotels and Other Adjusted EBITDA, against 294.7 on the continuing perimeter, a difference of 3.3). The confidence score was computed by the repository script and reproduced above.

## Gaps

The gaps are in the register above (G-1 to G-8). The two that govern use of this work are G-1 and G-2: without the credit agreement and a reported covenant ratio, the legal, collateral and headroom conclusions cannot be traced to clauses, and confidence stays at Medium at best. The Q4 2025 earnings leg (G-3) is a smaller trace weakness, mitigated by the segment cross-check.

## Next module

This is the last module in the requested set. Deliver the published report with committee status Draft Only. A reviser of the upstream handoffs should apply the five minor fixes (locators, label, carrying-basis ratio, severity mapping, legal clause tagging) and obtain the credit agreement and amendments before any committee decision on covenants, collateral or the use of sale proceeds.
