# CP-5 — Evidence trace and research integrity QA: Caesars Entertainment, Inc. (czr)

## Request

Caesars Entertainment, Inc. (issuer id `czr`), as of 2026-11-05, pathway `credit_snapshot`. Scope: trace the top five credit drivers of the earlier handoffs (CP-0, CP-1, CP-1A, CP-2) to the seven pinned filings and releases, recompute every derived number, and grade the research for committee use. Run `czr-2026-11-05-credit_snapshot-host`; a host session, no provider call.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_czr-20251231.htm.jsonl | bc64a6b58a2e5481a0cfade7eea5b0ab2abc3801003c4d6cb677785a5aa59468 | Audited FY2025; lease schedule, debt note, segment note |
| 10-Q_2026-03-31_czr-20260331.htm.jsonl | 5678521031e1645ef46bac311c4cabf43977488c6d11dfa25cc00a4f23b2d8a8 | Q1 2026 comparatives and liquidity |
| 10-Q_2026-06-30_czr-20260630.htm.jsonl | c1584ea1247740f06c0dd4b0a8964b1753f8cc5c74266698804a67fd5a8dafb5 | Q2 2026 comparatives and liquidity |
| 10-Q_2026-09-30_czr-20260930.htm.jsonl | 020dbbd4c466f93db126b9e9ea0f09672470d3e5caa33fd667f739807400c48f | Q3 2026 debt, covenants, liquidity, merger |
| EX-99.1_2026-04-28_ex991-2026q1ceiearningsrel.htm.jsonl | 7471385a5ad76519a93a6fc4a1f0048a88c7bfb7676d6a0b6e78c8e1a9e19c13 | Q1 2026 release |
| EX-99.1_2026-07-28_ex991-2026q2ceiearningsrel.htm.jsonl | 89cd5ad8c7a0d45cdf4a8f6462fc3964a9e7d04aae46811b1f50bebeb80c1762 | Q2 2026 release |
| EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm.jsonl | 72e92043d95db7701dbaee10509a03094dd97f5a7811f25a956ad12661393bcd | Q3 2026 release |
| context | fb12b9963cea633059e88f881abb925ca379a0e095eca4255a6e391fb14bd7dc | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | c01a0b9e9e4166e7f52e7361ee900e87238ecbbd00650638eadf7c06ae6c64f6 | Audited: source readiness |
| CP-1 | 6f42bc51c5bc5a08912d413aa5d25707c1ac86c243459556cabc2f214da86103 | Audited: financial base |
| CP-1A | d8c3812ab1cbd44380e397ef49c9c4d183e8a7183258fd41e4491f94ed87bb42 | Audited: business and transaction context |
| CP-2 | 01ebbb131aa9d4ccb1b967b635c2508afd11f577bb243b5be26705aa4ec46e44 | Audited: credit synthesis |

Locators are `page:N` of the pinned `.jsonl` text of each source. Consistency with upstream: this answer re-anchors on all four handoffs, which share run `czr-2026-11-05-credit_snapshot-host`, issuer, as-of date and period labels. It finds two statements in CP-2 that must be corrected by reading this answer (CP5-001 and CP5-002); the earlier handoff cannot be edited. All other figures re-computed here match.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The research is traceable to the filings and its numbers recompute, with two statements in the credit synthesis to correct. Committee use is restricted until merger financing and debt treatment are supplied. | Low | The Merger Agreement, proxy statement, covenant ratios and executed debt documents are not in the sources. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every recomputed ratio matched, including 3.26x debt-only leverage, 6.95x lease-inclusive leverage and 1.69x cash interest cover. | The leverage and cover figures can be relied on as arithmetic from company Adjusted EBITDA. | High |
| The synthesis blamed the rise from 6.90x to 6.95x on lease growth, but debt plus lease obligations fell by 154 and lower EBITDA caused the rise. | Lease-inclusive leverage deteriorated because earnings fell, not because the obligations grew. | High |
| The synthesis said no derivatives are held, but the filing says only that there are no cash flow hedges and no trading derivatives. | The 58 interest sensitivity is gross and may overstate exposure. | Medium |
| Merger financing and the treatment of existing debt have no source evidence. | The change-of-control effect on the notes and loans cannot be traced or assessed. | Low |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the missing merger financing and debt-treatment evidence, which matters because the post-closing capital structure decides whether the existing notes and loans survive, and it implies committee use stays restricted until the Merger Agreement, proxy statement and financing papers are supplied. Two statements in the credit synthesis need correction when read: the cause of the change in lease-inclusive leverage and the claim about derivatives.

### Traceability summary

| Rank | Credit driver | Classification | Traceability status | Most important gap |
| --- | --- | --- | --- | --- |
| 1 | Liquidity and maturity profile | Directly Sourced | Committee-Ready | Revolver reserves and regulatory commitments are company defined |
| 2 | Lease financing obligations and all-in fixed-charge cover | Calculated | Remediation Needed | Lease schedule only at December 31, 2025; cause statement to correct |
| 3 | Earnings trend and segment mix | Directly Sourced | Committee-Ready | Adjusted EBITDA is a management measure |
| 4 | Pending acquisition and effect on existing debt | Insufficient Information | Not Traceable | No merger financing or debt treatment evidence |
| 5 | Refinancing concentration in 2029 and 2030 and floating-rate exposure | Calculated | Remediation Needed | Derivatives statement overstated; hedging detail missing |

### Audit summary and clearance

Confidence Score: 18 / 100 (Band: Insufficient Information). qa_status: Restricted. committee_status: Restricted. The score is the canon formula run with the retained script: score = clamp((0.6 x 76 + 0.4 x 100) x 0.7 - 42, 0, 100) = 17.92, rounded to 18. The inputs are lineage of the five material drivers (two Directly Sourced, two Calculated, one Insufficient Information, so E is 76), all 17 required registers present (C is 100), a partial source gate because executed agreements and merger papers are missing (S is 0.7), and findings of 2 Material and 4 Minor (P is 42). The low band reflects the missing evidence on the central open item and the penalty for six defects; it does not mean the recomputed arithmetic is unreliable.

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 4. Committee Use: Restricted.

No finding changes a ratio or the direction of the credit view, but two committee-facing statements in CP-2 misstate a cause or overstate a fact (CP5-001 and CP5-002), so committee use is restricted until those are read with the corrections in this answer and the merger evidence gap is closed.

### Remediation priority map

- Must-fix before committee: CP5-001 (read CP-2's account of the 6.90x to 6.95x move as caused by lower last-twelve-months Adjusted EBITDA, with debt plus financing obligations down by 154) and CP5-002 (re-cite the derivatives statement to the Q3 10-Q and restate it as no cash flow hedges and no trading derivatives; treat the 58 sensitivity as gross).
- Must-fix before the handoff is consumed downstream: None. The two corrections above travel with this answer.
- Monitoring follow-up: CP5-003 (log debt on balance sheet carrying value 11,558 beside face value 11,659; delta 101) and CP5-006 (tag governance rows with evidence quality).
- Formatting and hygiene: CP5-004 (relabel the liquidity chart column) and CP5-005 (replace unbenchmarked adjectives and repeated caveats).

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

Module Status: Ready with Limitations. Traceability Scope: Top 5. Files used: seven pack sources and four handoffs. Missing required inputs: executed credit agreement, indentures, VICI and GLPI leases, Merger Agreement, proxy statement. External sources: none used by the upstream handoffs or by this answer. Entity key: issuer_id czr available.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_czr-20251231.htm.jsonl | Audited filing, primary | FY2025 | Caesars Entertainment, Inc. consolidated | Statements, debt note, lease schedule, segments, covenants | Text extraction only | CP-1 base, CP-2 lease schedule |
| S2 | 10-Q_2026-03-31_czr-20260331.htm.jsonl | Unaudited filing, primary | Q1 2026 | Consolidated | Statements, debt, liquidity | Pre-merger; unaudited | LTM and quarterly figures |
| S3 | 10-Q_2026-06-30_czr-20260630.htm.jsonl | Unaudited filing, primary | Q2 2026 and six months | Consolidated | Statements, debt, liquidity, first merger note | Unaudited | LTM and quarterly figures |
| S4 | 10-Q_2026-09-30_czr-20260930.htm.jsonl | Unaudited filing, primary | Q3 2026 and nine months | Consolidated | Statements, debt, covenants, liquidity, merger | Unaudited; no lease note | Current-period base |
| S5 | EX-99.1_2026-04-28_ex991-2026q1ceiearningsrel.htm.jsonl | Management release, supporting | Q1 2026 | Consolidated | Net debt, segment tables | Management prepared; duplicates the 10-Q | Net debt check |
| S6 | EX-99.1_2026-07-28_ex991-2026q2ceiearningsrel.htm.jsonl | Management release, supporting | Q2 2026 | Consolidated | Net debt, merger wording | Management prepared | Net debt check; acquirer name |
| S7 | EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm.jsonl | Management release, supporting | Q3 2026 | Consolidated | Net debt, liquidity table | Management prepared | Liquidity check; acquirer name |
| S8 | context | Run settings, not evidence | 2026-11-05 | Run | As-of date, currency, periods | Not issuer evidence | Scope |
| H0 | CP-0 handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Source readiness | Host authored | Scope and limits |
| H1 | CP-1 handoff | Analyst handoff | FY2025 to Q3 2026 | Consolidated | Financial base | Host authored | Audited here |
| H1A | CP-1A handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Business and transaction | Host authored | Audited here |
| H2 | CP-2 handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Credit synthesis | Host authored | Audited here |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Liquidity of 2,947 and maturity profile with no notes due before 2029 | CP-1, CP-2 | Company liquidity table and debt maturity table | Liquidity funds the 2028 revolver and term loan maturity and rent while earnings soften | Near-term default risk is low on liquidity; refinancing timing matters | S4 page:50 and page:16; S7 page:2 | Reserves and regulatory commitments are company defined |
| 2 | Lease financing obligations of 13,188 and all-in cash interest cover of 1.69x | CP-1, CP-2 | Balance sheet, cash interest lines, Adjusted EBITDA | Rent is a fixed claim ahead of debt service and outside the debt figure | Lease-inclusive leverage of 6.95x and thin cover drive risk | S4 page:2, page:5, page:34; S1 page:117 | Lease detail by landlord only at December 31, 2025 |
| 3 | Adjusted EBITDA of 2,672 for nine months 2026 against 2,723, Las Vegas weaker | CP-1, CP-1A | Reconciliation and segment tables | Falling earnings against stable fixed charges compress cover | Direction of the credit trend | S4 page:31 to page:34 | Management-defined measure |
| 4 | Pending acquisition and the unknown treatment of existing debt | CP-1A, CP-2 | Merger note and risk factors | Financing and debt treatment decide post-closing leverage and creditor position | Largest open item for committee | S4 page:6 to page:10, page:57 | No Merger Agreement, proxy or financing papers |
| 5 | Maturities of 1,574 in 2029 and 3,962 in 2030, about half of debt floating | CP-1, CP-2 | Debt maturity table, market risk text | Concentrated refinancing and rate exposure | Refinancing capacity depends on market access | S4 page:16 and page:54 | Hedging detail and floors not supplied |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Liquidity 2,947 (cash 864, availability 2,083) | CP-1 | `Total $ 2,947` (S4 page:50; S7 page:2) | Yes | Filing and release agree | Directly Sourced | Verified | High | Committee-Ready |
| No notes due before 2029; 28, 114, 646 before 2029 | CP-1, CP-2 | Maturity table, S4 page:16 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Debt-only leverage 3.26x | CP-1 | 11,659 (S4 page:16) over 3,573 (S1 page:78; S4 page:34) | Yes | Filing, company non-GAAP EBITDA | Calculated | Recomputed | Medium | Remediation Needed |
| Lease-inclusive leverage 6.95x and cover 1.69x | CP-1, CP-2 | Balance sheet and cash interest lines | Yes | Filing | Calculated | Recomputed | Medium | Remediation Needed |
| Cause of the rise from 6.90x to 6.95x stated as financing obligation growth | CP-2 | Arithmetic: numerator 25,001 to 24,847 | Partial | Contradicted by the filed figures | Conflicting | Corrected here | High | Not Traceable |
| Adjusted EBITDA 2,672 against 2,723; Las Vegas 1,179 against 1,281 | CP-1, CP-1A | S4 page:34, page:31 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Merger terms: USD 31.00, September 22, 2026 vote, fees of 200 and 450 | CP-1A | S4 page:7 to page:9 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Merger financing and treatment of existing debt | CP-1A, CP-2 | None in the sources | No | No source | Insufficient Information | Gap flagged, not adverse | Low | Not Traceable |
| Acquirer is Fertitta Gaming Holdco, LLC or Fertitta Entertainment, Inc. | CP-1A | S4 page:6; S7 page:4 | Yes | Two spans differ | Conflicting | Logged by CP-1A, not reconciled | Low | Remediation Needed |
| Compliance with financial covenants at September 30, 2026 | CP-1, CP-2 | S4 page:21 | Yes | Filing statement | Directly Sourced | Verified | Medium | Committee-Ready |
| Covenant headroom | CP-1, CP-2 | Levels printed, ratios and definitions absent | Yes | Filing | Insufficient Information | Correctly marked Not Calculable | Low | Remediation Needed |
| Variable-rate borrowings of 5.8 billion, about half of debt | CP-2 via CP-1 | S4 page:54 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| No derivatives held | CP-2 | Cited to CP-1, which has no such text; S4 page:12 says no cash flow hedges and no trading derivatives | Partial | Overstated | Weak Lineage | Corrected here | Medium | Remediation Needed |
| Interest rate sensitivity of 58 for a 1.00% move | CP-2 | 5,800 x 1.00% | Yes | Illustrative | Assumption-Based | Recomputed, gross | Low | Remediation Needed |
| Governance behaviour Supportive or Neutral | CP-1A | Absence of dividends, repurchases stopped, debt repaid | Yes | Filings | Analyst Inference | Labelled interpretation | Medium | Committee-Ready |
| Segment shares 50.1% and 35.3% and margins | CP-1A | S1 page:148 | Yes | Audited | Calculated | Recomputed | High | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents 864 at September 30, 2026 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:2 balance sheet | CP-1 liquidity table | Sourced | Filing | Opened and confirmed |
| Total liquidity 2,947 | pack/EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm | EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm.jsonl | S7 | page:2 | CP-1 liquidity | Sourced | Release | Matches S4 page:50 |
| CEI revolver 2,250 commitment, matures January 31, 2028 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:17 | CP-1, CP-2 debt | Sourced | Filing | Confirmed |
| Letters of credit 96, regulatory 56, reserves 40 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:19 and page:50 | CP-1, CP-2 liquidity | Sourced | Filing | Confirmed |
| Total debt face value 11,659; book value 11,563 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:16 | CP-1, CP-2 debt | Sourced | Filing | Balance sheet carrying value 11,558 not stated in CP-1 |
| Long-term financing obligations 13,188 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:2 | CP-1, CP-2 leases | Sourced | Filing | Confirmed |
| GLPI 1,284 and VICI 11,705 financing obligations at December 31, 2025 | pack/10-K_2025-12-31_czr-20251231.htm | 10-K_2025-12-31_czr-20251231.htm.jsonl | S1 | page:117 | CP-1 leases | Sourced | Audited | 107 of the 13,096 balance not itemised |
| Lease payments 1,392 in 2027, 1,424 in 2028, 1,446 in 2029 | pack/10-K_2025-12-31_czr-20251231.htm | 10-K_2025-12-31_czr-20251231.htm.jsonl | S1 | page:117 | CP-2 key findings | Calculated | Audited | Sums of GLPI and VICI rows |
| Cash interest paid for debt 580 for nine months 2026 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:5 | CP-1 coverage | Sourced | Filing | Confirmed |
| Cash interest paid for rent, GLPI and VICI 1,030 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:5 | CP-1 coverage | Sourced | Filing | Other financing obligations line 7 added by CP-1 |
| FY2025 cash interest for debt 813 and rent 1,349 | pack/10-K_2025-12-31_czr-20251231.htm | 10-K_2025-12-31_czr-20251231.htm.jsonl | S1 | page:101 | CP-1 coverage | Sourced | Audited | Rent 1,349 equals GLPI 113 plus VICI 1,236 on page:117 |
| Adjusted EBITDA 2,672 and 2,723 for nine months | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:34 | CP-1 financials | Sourced | Filing | Reconciliation foots |
| Adjusted EBITDA FY2025 3,624 | pack/10-K_2025-12-31_czr-20251231.htm | 10-K_2025-12-31_czr-20251231.htm.jsonl | S1 | page:78 | CP-1 financials | Sourced | Audited, EBITDA unaudited | Reconciliation foots |
| Maturities 28, 114, 646, 1,574, 3,962, 5,335 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:16 | CP-1, CP-2 maturities | Sourced | Filing | Sums to 11,659 |
| Covenant levels 6.50:1, 2.0:1, 4:1, 1.05:1, 1.20:1 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:20 to page:21, page:52 | CP-1, CP-2 covenants | Sourced | Filing summary | Executed agreements not supplied |
| Variable-rate borrowings 5.8 billion, about 50% of debt | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:54 | CP-2 refinancing | Sourced | Filing | Confirmed |
| No cash flow hedges and no trading derivatives | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:12 and page:54 | CP-2 refinancing | Sourced, narrower than CP-2 states | Filing | Text says derivatives used "on occasion" (page:54) |
| Merger consideration USD 31.00 and ticking fee after June 26, 2027 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:7 | CP-1A transaction | Sourced | Filing | Confirmed |
| Stockholder approval September 22, 2026 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:7 | CP-1A transaction | Sourced | Filing | Confirmed |
| Termination fee 200 and reverse fee 450; end dates | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:8 and page:9 | CP-1A, CP-2 | Sourced | Filing | Confirmed |
| Acquirer named Fertitta Entertainment, Inc. | pack/EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm | EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm.jsonl | S7 | page:4 | CP-1A conflict log | Sourced | Release | Differs from S4 page:6 |
| Las Vegas Adjusted EBITDA 1,179 against 1,281 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:31 | CP-1, CP-1A segments | Sourced | Filing | Confirmed |
| FY2025 segment revenues 4,049, 5,756, 1,408, 279 | pack/10-K_2025-12-31_czr-20251231.htm | 10-K_2025-12-31_czr-20251231.htm.jsonl | S1 | page:148 | CP-1A profile | Sourced | Audited | Foots to 11,486 |
| Lease payment of about 345 for the remainder of 2026 | pack/10-Q_2026-09-30_czr-20260930.htm | 10-Q_2026-09-30_czr-20260930.htm.jsonl | S4 | page:51 | CP-1 leases | Sourced | Management estimate | Estimate, not a commitment |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA Q3 2026 | CP-1 leverage and cover | 3,624; 2,672; 2,723 (USD m) | 3,624 + 2,672 - 2,723 = 3,573; LTM to September 30, 2026; company non-GAAP, not pro forma | Calculated | Recomputed, matches | High | Leverage, cover | S1 page:78; S4 page:34 |
| Total debt / Adjusted EBITDA | CP-1, CP-2 | Face debt 11,659; EBITDA 3,573 | 11,659 / 3,573 = 3.26x; numerator face value, denominator LTM; no normalisation | Calculated | Recomputed, matches | High | Leverage | S4 page:16 |
| Net debt / Adjusted EBITDA | CP-1 | Net debt 10,795; EBITDA 3,573 | 10,795 / 3,573 = 3.02x; net debt = face debt less unrestricted cash 864 | Calculated | Recomputed, matches | High | Leverage | S7 page:2 |
| (Debt + financing obligations) / Adjusted EBITDA | CP-1, CP-2 | 11,659; 13,188; 3,573 | (11,659 + 13,188) / 3,573 = 6.95x; EBITDA is before this rent | Calculated | Recomputed, matches | High | Leverage including leases | S4 page:2 |
| Same ratio at FY2025 | CP-2 change statement | 11,905; 13,096; 3,624 | 25,001 / 3,624 = 6.90x; numerator down 154 to 24,847; 24,847 / 3,624 = 6.86x at constant EBITDA | Calculated | Recomputed; cause in CP-2 corrected | High | Direction and cause | S1 page:99; S4 page:2 |
| LTM cash interest on debt | CP-1 cover | 813 + 580 - 652 | = 741 | Calculated | Recomputed, matches | High | Coverage | S1 page:101; S4 page:5 |
| LTM rent cash interest | CP-1 cover | 1,349 + 1,037 - 1,015 | = 1,371; 2026 and 2025 interim figures include other financing obligations 7 and 6 while FY2025 holds GLPI and VICI only | Calculated | Recomputed; basis difference of 1 disclosed | Medium | Coverage | S1 page:117; S4 page:5 |
| EBITDA / all cash interest | CP-1, CP-2 | 3,573; 741; 1,371 | 3,573 / 2,112 = 1.69x; debt only 3,573 / 741 = 4.82x | Calculated | Recomputed, matches | High | Coverage | as above |
| EBITDA less capex over all cash interest | CP-2 | 3,573; 664; 2,112 | (3,573 - 664) / 2,112 = 1.38x; capex is purchase of property and equipment LTM 805 + 507 - 648 | Calculated | Recomputed, matches | High | Coverage after capex | S1 page:101; S4 page:4 |
| Liquidity and availability | CP-1, CP-2 | 864; 2,250; 25; 96; 40; 56 | 864 + 2,250 + 25 - 96 - 40 - 56 = 2,947; availability 2,083 | Calculated | Recomputed, matches | High | Liquidity | S4 page:50 |
| 2029 and 2030 maturity share | CP-2 | 1,574; 3,962; 11,659 | 5,536 / 11,659 = 47.5% | Calculated | Recomputed, matches | High | Refinancing | S4 page:16 |
| Rate sensitivity | CP-2 | 5,800 variable debt; assumed 1.00% move | 5,800 x 1.00% = 58 per year; gross, before floors, hedges not supplied | Assumption-Based | Recomputed; qualifier added | Low | Interest burden | S4 page:54 |
| Free cash flow proxy and ratio | CP-1 | CFO 1,246; purchases 664; debt 11,659 | 582; 582 / 11,659 = 4.99% | Calculated | Recomputed, matches | High | Cash conversion | S1 page:101; S4 page:4 |
| Quarterly derivations | CP-1 | Year-to-date reports | Q2 operating cash flow 675 - 204 = 471; Q3 942 - 675 = 267 | Calculated | Recomputed, matches | High | Cash flow trend | S2 page:4; S3 page:4; S4 page:4 |
| Segment shares and margins | CP-1A | 4,049; 5,756; 1,408; 279; 11,486 | 35.3%, 50.1%, 12.3%, 2.4%; margins 42.7%, 31.1%, 16.8%, 24.0% | Calculated | Recomputed, matches | High | Concentration | S1 page:148 |
| Debt on balance sheet carrying value | Not used in CP-1 | Current 114; long-term 11,444 | 114 + 11,444 = 11,558; delta to face 101; ratio 11,558 / 3,573 = 3.23x | Calculated | New in this audit | High | Definition basis | S4 page:2 and page:16 |
| Covenant headroom | CP-1, CP-2 | Levels only | Needs covenant EBITDA and fixed charge definitions | Not Calculable (definitions not supplied) | Correctly not computed | Low | Covenant risk | S4 page:20 |

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Lease-inclusive leverage rose because the financing obligation grew | Cause contradicted by the filed figures (CP5-001) | Conflicting | A wrong cause misleads on trend: lower earnings, not lease growth, drove the rise, so earnings sensitivity is the driver of the 6.95x | Read as corrected | CP-2 Key findings |
| Material | No derivatives held | Cited to CP-1 which lacks it; source narrower (CP5-002) | Weak Lineage | Unhedged exposure drives the 58 sensitivity and cash interest risk | Re-cite and narrow | CP-2 Key findings and Calculations |
| Minor | Debt of 11,659 as leverage numerator | Canon basis is carrying value (CP5-003) | Calculated | Basis choice moves the ratio by 0.03x | Log both bases | CP-1 chart data and ratios |
| Minor | Governance rows | No evidence-quality tag (CP5-006) | Directly Sourced | Reader cannot grade each governance source | Add High tags | CP-1A governance table |

Orphan claim check (VE-015): the claim that merger financing and debt treatment cannot be assessed is Insufficient Information but carries a limitation flag in all four handoffs, so it is not an orphan claim.

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases with page text; no agreements or merger papers | Terms of debt, leases and merger cannot be verified from summaries | Covenant and change-of-control conclusions stay restricted | Supply agreements and merger papers |
| Citation completeness | Ready with Remediation | Almost every figure has a page locator; derivatives claim cited to the wrong handoff | A mis-cited claim hides narrower source wording | Interest sensitivity overstated | Correct citation (CP5-002) |
| Calculation traceability | Ready with Remediation | All 16 derived items recomputed and one marked Not Calculable; formulas and inputs shown; one cause statement wrong | A wrong cause can mislead on trend | Direction of the trend in lease-inclusive leverage misread | Read CP5-001 correction |
| Assumption transparency | Committee-Ready | Rate sensitivity labelled calculated and gross; LTM not pro forma disclosed | Assumptions are visible | Sensitivity treated as indicative | None beyond CP5-002 wording |
| Markdown and export artifact integrity | Committee-Ready | Six CP-OS headings, reader summaries and tables present in all four handoffs | Structure supports downstream use | None | None |

Overall auditability is Ready with Remediation, the lowest of the five dimension assessments.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Merger financing and treatment of existing debt | Merger Agreement, proxy statement, financing commitments | Post-closing leverage and who bears it decide creditor position | CP-1A transaction summary, CP-2 credit view | High impact | Form 8-K Exhibit 2.1 of May 28, 2026; proxy statement of August 26, 2026 |
| CP-5-GAP-002 | Covenant ratio values and definitions | Compliance certificates, executed CEI Credit Agreement | Headroom cannot be measured | CP-1 covenant table, CP-2 key finding seven | High impact | CEI Credit Agreement and certificates |
| CP-5-GAP-003 | Executed indentures and VICI and GLPI leases | Lease remedies, cross-defaults, change-of-control terms | Lessor and noteholder rights unknown | CP-2 structure and claims | High impact | Indentures and lease agreements |
| CP-5-GAP-004 | Lease schedule after December 31, 2025; 107 not itemised | Later lease note | Fixed charge forecast uses year-end schedule | CP-2 lease figures | Medium impact | Later filing or lease schedule |
| CP-5-GAP-005 | Acquirer identity conflict | Merger Agreement signature pages | Obligor and support analysis | CP-1A conflict, CP-2 | Medium impact | Merger Agreement |
| CP-5-GAP-006 | Nothing after October 27, 2026; approvals status unknown | Later Form 8-K filings | Closing timing | Event calendar | Medium impact | Form 8-K filings to 2026-11-05 |
| CP-5-GAP-007 | Hedging position beyond two sentences | Interest rate hedge disclosures, floors | Interest sensitivity of 58 is gross | CP-2 refinancing finding | Medium impact | Debt note or Item 7A detail |
| CP-5-GAP-008 | Guarantor names and restricted group | Subsidiary guarantor exhibit | Structural claims | CP-2 inventory | Medium impact | Exhibit 22 or indentures |
| CP-5-GAP-009 | Pro forma Adjusted EBITDA for Windsor and Grand Bazaar | Pro forma schedules | LTM EBITDA understates or misstates run rate | CP-1 ratios | Low impact | Management bridge |
| CP-5-GAP-010 | Text extraction not compared with filed HTML or XBRL | Original documents | Table-layout errors undetected | All figures | Low impact | Filed HTML or XBRL |

#### T5.1 Input module register

Module Status: Ready with Limitations (all four handoffs present with the six CP-OS headings; no YAML front matter, which this transport does not use; executed documents absent).

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/8ebff89b.../1.response.md; czr-2026-11-05-credit_snapshot-host | Source readiness for four consumers | Seven filings and releases | Six headings present; reader summary and readiness view present | Not previously graded; passed the launcher's structure check | No defect found |
| CP-1 | requests/CP-1/4470731c.../1.response.md; same run | Financial base FY2025 to Q3 2026 | Filings with company non-GAAP measures | Six headings, reader summary, chart tables and one metrics table present | Not previously graded | Two Minor findings (CP5-003, CP5-004) |
| CP-1A | requests/CP-1A/6de66690.../1.response.md; same run | Business, transaction, governance | Filings and releases | Six headings, three selector sections present | Not previously graded | One Minor finding (CP5-006) |
| CP-2 | requests/CP-2/18edd1b3.../1.response.md; same run | Credit synthesis | CP-1 and CP-1A plus the lease schedule | Six headings, key findings and strengths sections present | Not previously graded | Two Material findings (CP5-001, CP5-002), one Minor (CP5-005) |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-2 | Key findings, fifth finding and Calculations: variable-rate borrowings with "no derivatives held" cited to CP-1 | Partially Supported | CP-1 contains no derivatives text. The Q3 10-Q says it held no cash flow hedges and no derivatives for trading purposes (page:12) and that it has "on occasion" used derivatives to manage interest rate risk (page:54). "No derivatives held" is broader than the source, so the 58 sensitivity may overstate exposure. | Re-cite to the 10-Q; restate as no cash flow hedges and no trading derivatives; treat 58 as gross and unhedged | Restricts Committee Use |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-2 | Key findings, third finding: lease-inclusive leverage moved from 6.90x to 6.95x because the financing obligation grew by 92 and EBITDA fell (paraphrase of the CP-2 sentence) | Debt plus financing obligations fell from 25,001 to 24,847 (debt down 246, obligation up 92). At the FY2025 EBITDA of 3,624 the ratio would have been 6.86x. The rise comes entirely from EBITDA falling to 3,573. | None between sources; the error is in the explanation | Read the cause as lower last-twelve-months Adjusted EBITDA | Restricts Committee Use |
| Minor | CP-1 | Debt used in leverage is face value 11,659 | Canon basis is balance sheet carrying value (current 114 plus long-term 11,444 = 11,558); delta to face 101 is not logged in CP-1; carrying basis gives 3.23x against 3.26x | S4 page:2 against page:16 | Show both bases and the delta | Monitoring Follow-Up |
| Minor | CP-1 | Liquidity chart column "Undrawn committed facilities" | Values (1,946; 1,893; 1,963; 2,083) are net of letters of credit, reserves and regulatory commitments, not undrawn commitments; net of letters of credit only they are 2,032; 1,979; 2,059; 2,179 | Basis is stated in each row, label differs | Relabel the column or show both | Formatting / Hygiene Only |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| None - lane clear | CP-1, CP-2 | Security, ranking and guarantee statements for the CEI and CVA debt, covenant levels and lease terms | Executed credit agreement, indentures, lease agreements | Rest on the 10-Q and 10-K summaries; every handoff states the executed documents are not supplied and draws no covenant capacity, recovery or ranking conclusion | None; keep the Source Limitation tag | Legal review needed before any covenant capacity or recovery use |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None - lane clear | CP-2 | No price, spread, yield, rating, peer or relative-value claim is made | Market quotes and comparables are not in the pack and not needed for this scope | Marked Not supplied in the gaps | None for this scope | Market Data Not Provided; no relative-value use is permitted from these handoffs |

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| None - lane clear | CP-0, CP-1, CP-1A, CP-2 | Compared issuer name, run, period labels, Adjusted EBITDA definition, face debt 11,659, liquidity 2,947, maturities, covenant levels, lease balances, merger terms: all agree. The acquirer name difference is logged by CP-1A and carried by CP-2 | One version of each source; no draft or superseded document | None; keep the logged conflict open | None beyond CP-5-GAP-005 |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Promotional or Non-Credit Language | Judgement words such as thin, adequate, moderate and low for the leverage carry no stated threshold, and the caveat that computed ratios are not covenant ratios is repeated in several sections | Tie each word to a stated reference or drop it; state the caveat once | Slight dilution; no effect on figures |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Governance and sponsor behaviour table | Rows carry a category and a locator but no evidence-quality grade (High, Medium, Low, Insufficient) that the method asks for; all rows rest on dated primary filings and would grade High | Add the grade | None for consumers; grades inferred from the sources |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-2 | Formula / Definition Drift | Cause of the move in lease-inclusive leverage misstated; EBITDA decline, not obligation growth, raised 6.90x to 6.95x | Read as corrected here | Restricts Committee Use | Open |
| CP5-002 | Material | CP-2 | Partially Supported Claim | "No derivatives held" cited to CP-1, absent there and broader than the 10-Q | Re-cite and narrow; treat 58 as gross | Restricts Committee Use | Open |
| CP5-003 | Minor | CP-1 | Formula / Definition Drift | Face value used as debt basis; carrying value 11,558 and delta 101 not logged | Show both bases | Monitoring Follow-Up | Open |
| CP5-004 | Minor | CP-1 | Formula / Definition Drift | Liquidity chart label differs from the amounts shown | Relabel or show both | Formatting / Hygiene Only | Open |
| CP5-005 | Minor | CP-1, CP-2 | Promotional or Non-Credit Language | Unbenchmarked judgement words and repeated caveats | Tie to references; state once | Formatting / Hygiene Only | Open |
| CP5-006 | Minor | CP-1A | Evidence Trace Defect | No evidence-quality grade on governance rows | Add grades | Monitoring Follow-Up | Open |

## Calculations

All inputs in USD millions from the cited pages or from CP-1 and CP-2. Every upstream derived number was recomputed; the results are in T5B.5. New calculations made in this audit:

- Debt plus financing obligations: FY2025 11,905 + 13,096 = 25,001; Q3 2026 11,659 + 13,188 = 24,847; change 24,847 - 25,001 = -154 (debt -246, obligation +92).
- Lease-inclusive ratio at constant FY2025 EBITDA: 24,847 / 3,624 = 6.86x. Reported ratios: 25,001 / 3,624 = 6.90x and 24,847 / 3,573 = 6.95x. The change comes from the denominator: 3,573 - 3,624 = -51.
- Balance sheet carrying value of debt, September 30, 2026: 114 + 11,444 = 11,558; face 11,659 - 11,558 = 101 (unamortised discounts and deferred finance charges, 101 on the debt note). Leverage on carrying value: 11,558 / 3,573 = 3.23x. Net of cash 864: (11,558 - 864) / 3,573 = 2.99x. Lease-inclusive on carrying value: (11,558 + 13,188) / 3,573 = 6.93x.
- Liquidity availability net of letters of credit only: 2,250 + 25 - 96 = 2,179 at Q3 2026, against 2,083 on the company basis.
- Confidence score: lineage of the five material drivers: 2 Directly Sourced (weight 1.0), 2 Calculated (0.9), 1 Insufficient Information (0.0), E = (2 x 1.0 + 2 x 0.9 + 0) / 5 x 100 = 76. C = 17 of 17 required registers present = 100. S = 0.7 (partial source gate). P = 2 x 15 + 4 x 3 = 42. Score = (0.6 x 76 + 0.4 x 100) x 0.7 - 42 = 17.92, rounded to 18; the retained script gives the same result, band Insufficient Information and qa_status Restricted.
- Recomputed and matching, no change: LTM Adjusted EBITDA 3,573; 3.26x; 3.02x; 6.95x; 1.69x; 4.82x; 1.38x; 741; 1,371; 2,947; 2,083; 47.5%; 4.99%; 35.3%, 50.1%, 12.3% and 2.4%.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Merger financing and treatment of existing debt not in the sources (CP-5-GAP-001) | High | Committee, CP-2 users | Supply the Merger Agreement exhibit, proxy statement and financing commitments |
| Covenant ratios and executed agreements missing (CP-5-GAP-002, CP-5-GAP-003) | High | Committee, CP-2 users | Supply compliance certificates, credit agreement, indentures and leases |
| CP5-001 and CP5-002 corrections live only in this answer | Medium | Anyone reading CP-2 alone | Read CP-2 with this answer; the earlier handoff cannot be edited |
| Lease schedule dated December 31, 2025; acquirer identity; events after October 27, 2026 (CP-5-GAP-004 to CP-5-GAP-006) | Medium | Committee | Supply later filings and the Merger Agreement |
| Hedging detail, guarantor names, pro forma EBITDA, extraction check (CP-5-GAP-007 to CP-5-GAP-010) | Low to Medium | Committee | Supply as listed in the gaps ledger |

## Next module

- Report assembly: use the corrected statements. Say that lease-inclusive leverage rose from 6.90x to 6.95x because last-twelve-months Adjusted EBITDA fell from 3,624 to 3,573 while debt plus financing obligations fell by 154, and say that the filing shows no cash flow hedges and no trading derivatives, not that no derivatives are held.
- Committee use stays restricted until the Merger Agreement, proxy statement and financing papers, the covenant compliance evidence and the executed debt and lease documents are supplied; then rerun CP-1A, CP-2 and CP-5.
