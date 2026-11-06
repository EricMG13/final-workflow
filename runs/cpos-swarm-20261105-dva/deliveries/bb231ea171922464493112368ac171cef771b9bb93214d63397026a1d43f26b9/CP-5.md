# CP-5 — Evidence trace and research integrity QA: DAVITA INC. (dva)

## Request

DAVITA INC. (issuer id `dva`), as of 2026-11-05, pathway `credit_snapshot`. Scope: trace the top five credit drivers of the earlier handoffs (CP-0, CP-1, CP-1A, CP-2) to the seven pinned filings and releases, recompute every derived number, and grade the research for committee use. Run `dva-2026-11-05-credit_snapshot-host`; a host session, no provider call.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_dva-20251231.htm.jsonl | e8c363b79225d32d92e8856c1234363883b84595e0f356cf12128301c572a94b | Audited FY2025; covenant text, amortisation terms, contractual obligations, payor and ownership text |
| 10-Q_2026-03-31_dva-20260331.htm.jsonl | 7063ac673c62a3a12d361c8ab9f216c83e6406eb95937f85ad2f6c47a221fe01 | Q1 2026 statements, debt note, liquidity |
| 10-Q_2026-06-30_dva-20260630.htm.jsonl | 5aed5931f3b50f8efc4d5398264cb7a317623aeb269a49968c33246ed0273365 | Q2 2026 statements, debt note, maturities, liquidity |
| 10-Q_2026-09-30_dva-20260930.htm.jsonl | 99b4bb0c8f87c03db2290c95cfd812d4622509e8fdbcdce46d84afcedef79236 | Q3 2026 statements, debt note, maturities, caps, payor mix, share repurchases |
| EX-99.1_2026-05-05_dva33126ex991.htm.jsonl | c5727d9383becddd69bf1cd80efadc8ee72012f8313405a8b1414b2f74143fa7 | Q1 2026 release: leverage ratio, net debt (supporting) |
| EX-99.1_2026-08-04_dva63026ex991.htm.jsonl | e55a9fe053fe9f69274156863d81212ffe989a931913bc64dfc65b70fd8151a2 | Q2 2026 release: leverage ratio, net debt (supporting) |
| EX-99.1_2026-10-29_dva93026ex991.htm.jsonl | b062a4dfa0aa9b3cce4ee385c1a8aad8546180810a3acbc585a968f93eadfc64 | Q3 2026 release: leverage ratio, covenant maximum, guidance (supporting) |
| context | 888318ae2603a71d9f443112e6d0298861b2ea95d8c8a8118da68f80c88bfe70 | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 3ecf1492bb810c2e90133183ed7699bad1c56c1780a9f8736f0e2c4391db50f2 | Audited: source readiness |
| CP-1 | 3cfbf98d548042fd31ec6ebfe100057e48caebe480e0597af9abd9a0b0ee8fc9 | Audited: financial base |
| CP-1A | 9451150fe7d243d9c2cc5ebdabe9029317cc1a59d7b1fd0e9903edffd39634aa | Audited: business and transaction context |
| CP-2 | 5da0a080bf686de8cf4f951492968f92b13b32d4f2632603f8d6dbe58b7b1055 | Audited: credit synthesis |

Locators are `page:N` of the pinned `.jsonl` text of each source. Source tags: S1 annual report, S2 to S4 the three quarterly reports in date order, S5 to S7 the three earnings releases in date order. Consistency with upstream: this answer re-anchors on all four handoffs, which share run `dva-2026-11-05-credit_snapshot-host`, issuer, as-of date and period labels. It finds one statement that must be corrected by reading this answer (CP5-001) and seven smaller defects; the earlier handoffs cannot be edited. All other recomputed figures match.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The research traces to the filings and its numbers recompute, with one correction: the bank debt that springs to March 2, 2030 is overstated. Committee use is restricted until that correction is read and the credit agreement is supplied. | Low | The credit agreement, indentures, guarantor list and covenant certificates are not supplied, so covenant headroom and Consolidated EBITDA cannot be checked. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every recomputed figure matched, including covenant-basis leverage of 3.38x, total debt of 10,832.2 and liquidity of 1,915.6. | The headline ratios and balances can be relied on as arithmetic from the filings. | High |
| The 2,042.5 of bank debt said to spring to March 2, 2030 uses September 30, 2026 balances; scheduled amortisation leaves about 1,780.0. | The springing refinancing exposure was overstated by 262.5. | High |
| Buyback totals appear as 862.5, 870.2 and 863 on different bases without a bridge. | Capital-return figures need one stated basis before committee use. | Medium |
| Covenant definitions and Consolidated EBITDA add-backs have no source evidence beyond the company's printed ratio. | Headroom of 1.62x is a company-basis figure and cannot be verified. | Low |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 1 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the missing credit agreement and covenant evidence, which matters because the 5.00:1.00 test, the 4.00:1.00 relief threshold and the Consolidated EBITDA add-backs decide how much room exists for buybacks and for an earnings decline, and it implies committee use stays restricted until the agreement and compliance certificates are supplied. One statement in the financial base and the credit synthesis needs correction when read: the size of the debt that springs to March 2, 2030.

### Traceability summary

| Rank | Credit driver | Classification | Traceability status | Most important gap |
| --- | --- | --- | --- | --- |
| 1 | Covenant-basis leverage of 3.38x against a 5.00x maximum | Directly Sourced | Committee-Ready | Ratio and maximum are printed by the company; the agreement is not supplied |
| 2 | Buybacks of 870.2 exceed free cash flow of 672, with debt up | Calculated | Remediation Needed | Three buyback bases (CP5-006) |
| 3 | Liquidity of 1,915.6 and the 2030 to 2031 maturity wall | Calculated | Remediation Needed | Springing exposure overstated (CP5-001) |
| 4 | Commercial-payor profit dependence and U.S. dialysis at 97.3% of segment margin | Directly Sourced | Committee-Ready | Payor shares carry mixed periods (CP5-005) |
| 5 | Covenant headroom and Consolidated EBITDA quality | Insufficient Information | Not Traceable | Definitions and add-backs sit in an unsupplied agreement |

### Audit summary and clearance

Confidence Score: 24 / 100 (Band: Insufficient Information). qa_status: Restricted. committee_status: Restricted. The score is the canon formula run with the retained script: score = clamp((0.6 x 76 + 0.4 x 100) x 0.7 - 36, 0, 100) = 23.92, rounded to 24. The inputs are lineage of the five material drivers (two Directly Sourced, two Calculated, one Insufficient Information, so E is 76), all 17 required registers present (C is 100), a partial source gate because the executed debt agreements are missing (S is 0.7), and findings of 1 Material and 7 Minor (P is 36). The low band reflects the penalty for eight defects and the unverifiable covenant driver; it does not mean the recomputed arithmetic is unreliable.

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 1. Minor Issues: 7. Committee Use: Restricted.

No finding changes a ratio or the direction of the credit view, but one committee-facing figure (the bank debt that springs to March 2, 2030) overstates the exposure by 262.5, so committee use is restricted until it is read with the correction in this answer. The Material issue to disclose for committee use is CP5-001.

### Remediation priority map

- Must-fix before committee: CP5-001 (read the springing exposure as about 1,780.0 at March 2, 2030 on scheduled amortisation, made up of about 1,700.0 of Term Loan A-2 and the revolver balance, not 2,042.5).
- Must-fix before the handoff is consumed downstream: None. The correction travels with this answer.
- Monitoring follow-up: CP5-003 (log leverage on carrying value beside principal), CP5-004 (state that the rate sensitivity covers only debt above the cap strikes and that the SOFR level is not supplied), CP5-006 (use one buyback basis and bridge the others), CP5-007 (grade the evidence quality of governance rows).
- Formatting and hygiene: CP5-002 (limit the notes covenant text to the 6.75% series), CP5-005 (label FY2025 shares and use all-commercial 31.9% and non-hospital 26% consistently), CP5-008 (tie judgement words to references and state each caveat once).

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

Module Status: Ready with Limitations. Traceability Scope: Top 5. Files used: seven pack sources and four handoffs. Missing required inputs: credit agreement and amendments, indentures, Exhibit 21.1 guarantor list, covenant compliance certificates, Berkshire and Elara agreements, proxy statement. External sources: none used by the upstream handoffs or by this answer. Entity key: issuer_id dva available.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_dva-20251231.htm.jsonl | Audited filing, primary | FY2025 | DaVita Inc. consolidated | Statements, debt and lease notes, covenant text, segments, payor and ownership text | Text extraction only | CP-1 base, CP-1A business, CP-2 covenant and amortisation terms |
| S2 | 10-Q_2026-03-31_dva-20260331.htm.jsonl | Unaudited filing, primary | Q1 2026 | Consolidated | Statements, debt, liquidity | Unaudited; no maturity schedule | Quarterly and LTM figures |
| S3 | 10-Q_2026-06-30_dva-20260630.htm.jsonl | Unaudited filing, primary | Q2 2026 and six months | Consolidated | Statements, debt, maturities, liquidity | Unaudited | Quarterly and LTM figures |
| S4 | 10-Q_2026-09-30_dva-20260930.htm.jsonl | Unaudited filing, primary | Q3 2026 and nine months | Consolidated | Statements, debt, maturities, caps, payor mix, share repurchases, legal matters | Unaudited; no cash interest paid | Current-period base |
| S5 | EX-99.1_2026-05-05_dva33126ex991.htm.jsonl | Management release, supporting | Q1 2026 | Consolidated | Leverage ratio, Consolidated EBITDA, net debt | Management prepared; non-GAAP | Leverage history |
| S6 | EX-99.1_2026-08-04_dva63026ex991.htm.jsonl | Management release, supporting | Q2 2026 | Consolidated | Leverage ratio, Consolidated EBITDA, net debt | Management prepared; non-GAAP | Leverage history |
| S7 | EX-99.1_2026-10-29_dva93026ex991.htm.jsonl | Management release, supporting | Q3 2026 | Consolidated | Leverage ratio, covenant maximum, guidance, segment data | Management prepared; non-GAAP | Current leverage and covenant check |
| S8 | context | Run settings, not evidence | 2026-11-05 | Run | As-of date, currency, periods | Not issuer evidence | Scope |
| H0 | CP-0 handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Source readiness | Host authored | Scope and limits |
| H1 | CP-1 handoff | Analyst handoff | FY2025 to Q3 2026 | Consolidated | Financial base | Host authored | Audited here |
| H1A | CP-1A handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Business and ownership context | Host authored | Audited here |
| H2 | CP-2 handoff | Analyst handoff | As of 2026-11-05 | Consolidated | Credit synthesis | Host authored | Audited here |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Covenant-basis leverage of 3.38x, up from 3.26x, against a 5.00x maximum | CP-1, CP-2 | Company calculation of Consolidated net debt over Consolidated EBITDA and the printed maximum | Leverage sets the margin grid, the restriction-relief threshold and the headroom to the maintenance test | Headroom of 1.62x frames default risk and buyback capacity | S7 page:15 to page:16; S1 page:183 | Company-computed; agreement not supplied |
| 2 | Buybacks of 870.2 exceed free cash flow of 672 while debt rises 487.7 | CP-1, CP-1A, CP-2 | Cash-flow statement, free cash flow and debt note | Cash returned to holders rather than applied to debt moves leverage up | Capital allocation is the main controllable driver of leverage | S4 page:4, page:11, page:18, page:44 | Three buyback bases; free cash flow is non-GAAP |
| 3 | Liquidity of 1,915.6 and 77% of debt maturing in 2030 and 2031 | CP-1, CP-2 | Balance sheet, revolver text, maturity table | Light near-term maturities, then a concentrated wall with a springing date | Refinancing capacity and timing | S4 page:3, page:12, page:14; S1 page:181 | Springing exposure overstated (CP5-001) |
| 4 | Commercial payors generate nearly all profit; U.S. dialysis earns 97.3% of segment margin | CP-1A, CP-2 | 10-K payor text and segment note | Profit rests on a minority of patients and on rate setting | Earnings sensitivity to mix and policy | S1 page:15; S4 page:7 to page:8, page:23 to page:24 | Payor shares from different periods |
| 5 | Covenant headroom and Consolidated EBITDA quality | CP-1, CP-2 | Reconciliation of Consolidated EBITDA in the release | Add-backs and pro forma adjustments are set by an agreement not supplied | Headroom cannot be verified | S7 page:15; S1 page:183 | No agreement or compliance certificate |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage ratio 3.38x and 3.26x; maximum 5.00x | CP-1, CP-2 | `Leverage ratio 3.38x 3.37x`; `Maximum leverage ratio permitted under the Credit Agreement 5.00x` (S7 page:15 to page:16) | Yes | Release, supporting; ratio recomputes from printed net debt and EBITDA | Directly Sourced | Verified | Medium | Committee-Ready |
| Headroom 1.62x; EBITDA cushion 988.2 (32.5%); 4.00x cushion 474.8 (15.6%) | CP-1, CP-2 | 10,269 and 3,042 (S7 page:15); levels (S1 page:183) | Yes | Company basis | Calculated | Recomputed | Medium | Remediation Needed |
| Total debt 10,832.2; up 487.7 from 10,344.6; cash 495.6 from 676.4 | CP-1, CP-2 | S4 page:11 and page:3; S1 page:179 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Buybacks 870.2 against free cash flow 672; net debt issuance 490 | CP-1, CP-2 | S4 page:4 and page:44 | Yes | Filing and company free cash flow | Calculated | Recomputed | Medium | Remediation Needed |
| Buyback totals 862.5, 870.2 and 863 | CP-1, CP-1A, CP-2 | S4 page:18, page:4; S7 page:13 | Yes | Three bases | Conflicting | Different bases, not bridged (CP5-006) | Medium | Remediation Needed |
| Liquidity 1,915.6 (cash 495.6 plus undrawn revolver 1,420.0) | CP-1, CP-2 | S4 page:3 and page:14 | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |
| Maturities: 31.4, 113.0, 160.4, 146.9, 4,570.3, 3,765.1, 2,045.1; 77% in 2030 and 2031 | CP-1, CP-2 | S4 page:12 | Yes | Filing | Calculated | Recomputed (sums to 10,832.2) | High | Committee-Ready |
| Springing exposure of 2,042.5 at March 2, 2030 | CP-1, CP-2 | S4 page:11 footnote; S1 page:181 amortisation terms | Partial | Current balances, not scheduled balances | Calculated | Corrected here: about 1,780.0 (CP5-001) | High | Remediation Needed |
| Operating lease liabilities 2,623.3; puts 1,484.3; letters of credit 184.8 | CP-1, CP-2 | S4 page:3 and page:14 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| U.S. dialysis 97.3% of segment margin and 84.9% of segment revenue | CP-1A, CP-2 | S4 page:23 to page:24 | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |
| Commercial payors 26% of revenue, 11% of patients, nearly all profit | CP-1A, CP-2 | S1 page:15 (FY2025) | Yes | Audited | Directly Sourced | Verified; period unlabelled in CP-2 (CP5-005) | High | Committee-Ready |
| Payor mix 9M 2026: Medicare and Medicare Advantage 57.7%, commercial 31.9% | CP-1A, CP-2 | S4 page:7 to page:8 | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |
| Revenue per treatment up 2.7%; costs per treatment up 3.0% | CP-1A, CP-2 | S4 page:36 to page:37 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Rate exposure: 894.5 not covered by caps; 8.9 per point | CP-1, CP-2 | S4 page:12 to page:13 | Yes | Filing statement; sensitivity illustrative | Assumption-Based | Recomputed; qualifier added (CP5-004) | Low | Remediation Needed |
| Covenant compliance and Consolidated EBITDA definition | CP-1, CP-2 | No compliance statement found; add-backs listed in S7 page:15 | Partial | Company presentation | Insufficient Information | Correctly marked unverified | Low | Not Traceable |
| Berkshire held to 45.0% by agreement; standstill; obligation settled October 27, 2026 | CP-1A | S1 page:200, page:202; S4 page:19 | Yes | Audited and filing | Directly Sourced | Verified | High | Committee-Ready |
| CMS 2027 rule described as final and as proposed | CP-1A | S4 page:37 | Yes | Two spans differ | Conflicting | Logged by CP-1A, not reconciled | Low | Remediation Needed |
| Governance behaviour Neutral or Mixed leaning Extraction-Oriented | CP-1A | Buybacks, net debt issuance, leverage range | Yes | Filings | Analyst Inference | Labelled interpretation | Medium | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents 495.6 at September 30, 2026 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:3 balance sheet | CP-1 liquidity | Sourced | Filing | Confirmed |
| Total debt principal 10,832.2; carrying 10,769.1; discount 63.1 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:11 debt note | CP-1, CP-2 debt | Sourced | Filing | Components sum to 10,832.2 |
| Revolver 1,420.0 available and 80.0 drawn; no letters of credit on it | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:14 and page:47 | CP-1, CP-2 liquidity | Sourced | Filing | Confirmed |
| Letters of credit about 184.8 under a separate bilateral facility | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:14 | CP-1, CP-2 claims | Sourced | Filing | Capacity not stated |
| Scheduled maturities 31.4 / 113.0 / 160.4 / 146.9 / 4,570.3 / 3,765.1 / 2,045.1 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:12 | CP-1 chart, CP-2 | Sourced | Filing | Sum equals total principal |
| Term Loan A-2 amortisation 12.5 per quarter to December 31, 2027, then 25.0 | pack/10-K_2025-12-31_dva-20251231.htm | 10-K_2025-12-31_dva-20251231.htm.jsonl | S1 | page:181 | CP-1 debt table (not used in the springing figure) | Sourced | Audited | Basis of the CP5-001 correction |
| Term Loan A-2 and revolver due March 2, 2030 if 4.625% notes remain | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:11 footnote 2 | CP-1, CP-2 | Sourced | Filing | Date is 91 days before June 1, 2030 |
| Maximum leverage ratio 5.00:1.00 through December 31, 2028, then 4.50:1.00; relief below 4.00:1.00 | pack/10-K_2025-12-31_dva-20251231.htm | 10-K_2025-12-31_dva-20251231.htm.jsonl | S1 | page:183 | CP-1, CP-2 covenants | Sourced | Audited | Summary of the agreement, not the agreement |
| Leverage ratio 3.38x; Consolidated EBITDA 3,042; Consolidated net debt 10,269; maximum 5.00x | pack/EX-99.1_2026-10-29_dva93026ex991.htm | EX-99.1_2026-10-29_dva93026ex991.htm.jsonl | S7 | page:15 to page:16 | CP-1, CP-2 | Sourced | Release | Non-GAAP; recomputes |
| Net debt 10,337; total debt 10,832; free cash flow 276, 256, 672 | pack/EX-99.1_2026-10-29_dva93026ex991.htm | EX-99.1_2026-10-29_dva93026ex991.htm.jsonl | S7 | page:13 | CP-1 | Sourced | Release | Net debt is cash-only |
| Revenue 10,547.8 and operating income 1,560.1 for nine months 2026 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:2 | CP-1 | Sourced | Filing | Quarters tie to nine months |
| Operating cash flow 1,329.7; additions of property and equipment 431.3 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:4 | CP-1 | Sourced | Filing | Confirmed |
| Free cash flow 672 and 716; debt issuances, net 490 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:44 | CP-1, CP-2 | Sourced | Filing | Company non-GAAP |
| Share repurchases: 5,837 thousand shares for 862.5; Berkshire 3,062 thousand for 419.3 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:18 | CP-1A governance | Sourced | Filing | Excludes commissions and excise tax |
| Cash paid for treasury stock 419.3 and 450.9 (870.2) | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:4 | CP-1, CP-2 | Sourced | Filing | Cash basis |
| Operating lease liabilities 438.1 and 2,185.2; puts 1,484.3 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:3 | CP-1, CP-2 claims | Sourced | Filing | Outside debt |
| Segment revenues and margins; U.S. dialysis 1,588.1 of 1,632.4 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:23 to page:24 | CP-1, CP-1A | Sourced | Filing | Ties to consolidated |
| Non-hospital commercial 26% of revenue, 11% of patients; nearly all profits | pack/10-K_2025-12-31_dva-20251231.htm | 10-K_2025-12-31_dva-20251231.htm.jsonl | S1 | page:15 | CP-1A, CP-2 | Sourced | Audited | FY2025 |
| U.S. dialysis patient service revenue by payor, nine months 2026 and 2025 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:7 to page:8 | CP-1A | Sourced | Filing | Totals tie to 8,984.4 and 8,698.4 |
| Revenue and patient care costs per treatment 416.22 / 405.15 and 279.24 / 271.23 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:36 to page:37 | CP-1A, CP-2 | Sourced | Filing | Confirmed |
| Cash paid for interest, net 515.5 for FY2025 | pack/10-K_2025-12-31_dva-20251231.htm | 10-K_2025-12-31_dva-20251231.htm.jsonl | S1 | page:213 | CP-1 chart | Sourced | Audited | Interim not printed |
| Interest rate caps: 3,500.0 notional through 2028; 894.5 floating uncovered | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:12 to page:13 | CP-1, CP-2 | Sourced | Filing | SOFR level not supplied |
| Berkshire 45.0% agreement; standstill | pack/10-K_2025-12-31_dva-20251231.htm | 10-K_2025-12-31_dva-20251231.htm.jsonl | S1 | page:200 and page:202 | CP-1A governance | Sourced | Audited | Berkshire's current holding not read |
| Berkshire obligation of 54.7 settled October 27, 2026 for 69.0 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:19 | CP-1, CP-1A | Sourced | Filing | Subsequent event |
| China impairment 62.2; goodwill remaining 42.9 | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:2, page:10 to page:11 | CP-1, CP-1A | Sourced | Filing | Confirmed |
| 2027 CMS rule called final and proposed | pack/10-Q_2026-09-30_dva-20260930.htm | 10-Q_2026-09-30_dva-20260930.htm.jsonl | S4 | page:37 | CP-1A conflicts | Conflicting | Filing | Logged by CP-1A |
| FY2025 audit opinion unqualified | pack/10-K_2025-12-31_dva-20251231.htm | 10-K_2025-12-31_dva-20251231.htm.jsonl | S1 | page:148 | CP-1 quality | Sourced | Audited | Confirmed |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM revenue and operating income Q3 2026 | CP-1 | 13,643.1 + 10,547.8 - 10,023.3; 2,043.6 + 1,560.1 - 1,482.5 | 14,167.5 and 2,121.2; LTM to September 30, 2026 | Calculated | Recomputed, matches | High | Earnings base | S1 page:153; S4 page:2 |
| Discrete quarters tie to nine months | CP-1 | Q1 + Q2 + Q3 revenue and operating income | 3,415.5 + 3,554.1 + 3,578.1 = 10,547.8; 481.9 + 579.0 + 499.3 = 1,560.1 | Calculated | Recomputed, matches | High | Quarterly trend | S2 to S4 page:2 |
| LTM operating cash flow and additions | CP-1 | 1,886.5 + 1,329.7 - 1,345.8; 575.9 + 431.3 - 430.4 | 1,870.5 (release prints 1,870) and 576.8 | Calculated | Recomputed, matches | High | Cash conversion | S1 page:155; S4 page:4; S7 page:2 |
| Operating cash flow less additions | CP-1, CP-2 | 1,329.7; 431.3 | 898.4 for nine months 2026; 1,293.7 LTM | Calculated | Recomputed, matches | High | Cash conversion | S4 page:4 |
| Total debt / Consolidated EBITDA | CP-1, CP-2 | 10,832.2; 3,042 | 3.56x; numerator principal, denominator LTM company EBITDA | Calculated | Recomputed, matches | High | Leverage | S4 page:11; S7 page:15 |
| Covenant-basis ratio | CP-1, CP-2 | 10,269; 3,042 | 3.38x (printed); FY2025 9,648 / 2,960 = 3.26x | Calculated | Recomputed, matches printed ratio | High | Covenant | S7 page:15; S5 page:16 |
| Net debt (cash only) / EBITDA | CP-1 | 10,336.6; 3,042 | 3.40x; net debt = principal less cash 495.6 | Calculated | Recomputed, matches | High | Leverage | S4 page:3, page:11 |
| Sensitivity EBITDA and leverage | CP-1, CP-2 | 2,121.2 + 697.5 + 62.2 = 2,880.9 | 10,832.2 / 2,880.9 = 3.76x; no add-backs | Calculated | Recomputed, matches | High | Leverage sensitivity | S4 page:2 |
| Expense-basis cover | CP-1, CP-2 | 3,042; 593.7 | 5.12x; debt expense LTM = 579.9 + 445.4 - 431.7 | Calculated | Recomputed, matches | High | Coverage | S1 page:153; S4 page:2 |
| FY2025 cash interest cover | CP-1 | 2,960; 515.5 | 5.74x | Calculated | Recomputed, matches | High | Coverage | S1 page:213; S5 page:15 |
| Liquidity | CP-1, CP-2 | 495.6; 1,420.0 | 1,915.6; FY2025 2,176.4; change -260.8 | Calculated | Recomputed, matches | High | Liquidity | S4 page:3, page:14 |
| Liquidity cover of scheduled principal to 2029 | CP-2 | 1,915.6; 31.4 + 113.0 + 160.4 + 146.9 | 451.7; 1,915.6 / 451.7 = 4.2x | Calculated | Recomputed, matches | High | Refinancing | S4 page:12 |
| Maturity concentration | CP-1, CP-2 | 4,570.3 + 3,765.1; 10,832.2 | 8,335.4; 77.0% | Calculated | Recomputed, matches | High | Refinancing | S4 page:12 |
| Springing exposure | CP-1, CP-2 | 1,962.5 + 80.0 | 2,042.5 at September 30, 2026 balances; scheduled balance at March 2, 2030 is 1,962.5 - 262.5 = 1,700.0 plus the revolver | Calculated | Corrected here (CP5-001) | High | Refinancing | S4 page:11; S1 page:181 |
| Refinancing illustration | CP-2 | 2,750.0 x (6.75% - 4.625%); 1,500.0 x (6.75% - 3.75%) | 58.4 + 45.0 = 103.4; 17.4% of 593.7 | Assumption-Based | Recomputed; labelled illustration | Medium | Interest burden | S4 page:11; S1 page:184 |
| Covenant headroom and cushions | CP-1, CP-2 | 5.00; 3.38; 10,269; 3,042 | 1.62x; 10,269 / 5.00 = 2,053.8, cushion 988.2 (32.5%); at 4.00x 2,567.3, cushion 474.8 (15.6%) | Calculated | Recomputed, matches | Medium | Covenant | S7 page:15 to page:16 |
| Buybacks relative to cash generation | CP-1, CP-2 | 870.2; 898.4; 672 | 870.2 / 898.4 = 96.9%; 672 - 870.2 = -198.2 | Calculated | Recomputed, matches | Medium | Capital allocation | S4 page:4, page:44 |
| Segment shares | CP-1A, CP-2 | 9,004.0; 10,610.1; 1,588.1; 1,632.4 | 84.9%; 97.3%; FY2025 2,084.2 / 2,176.6 = 95.8% | Calculated | Recomputed, matches | High | Concentration | S4 page:23 to page:24; S1 page:212 |
| Payor shares and growth | CP-1A | 5,180.8; 667.9; 271.7; 2,863.9 over 8,984.4 | 57.7%, 7.4%, 3.0%, 31.9%; 9M 2025 57.3%, 7.3%, 2.8%, 32.5%; growth 4.0% and 1.2% | Calculated | Recomputed, matches | High | Mix trend | S4 page:7 to page:8 |
| Per-treatment growth | CP-1A, CP-2 | 416.22 / 405.15; 279.24 / 271.23 | 2.7% and 3.0% | Calculated | Recomputed, matches | High | Unit margin | S4 page:36 to page:37 |
| Rate sensitivity | CP-2 | 894.5 uncovered | 894.5 x 1.00% = 8.9 pre-tax; ignores capped debt below the strikes | Assumption-Based | Recomputed; qualifier added (CP5-004) | Low | Interest burden | S4 page:12 to page:13 |
| Debt on carrying value | Not used in ratios | 112.5 + 10,656.6 = 10,769.1 | Principal 10,832.2 less 63.1 = 10,769.1; 10,769.1 / 3,042 = 3.54x | Calculated | New in this audit | High | Definition basis | S4 page:3, page:11 |
| Interest sensitivity of the 10-K | CP-2 | 5.3 net of tax and caps for 2025 | Reported figure, not recomputed | Not Calculable | Not recomputed (SOFR level not supplied) | Low | Rate risk | S1 page:142 |
| Covenant compliance and Consolidated EBITDA add-backs | CP-1, CP-2 | Add-backs printed; definitions absent | Needs the agreement | Not Calculable (definitions not supplied) | Correctly not verified | Low | Covenant risk | S7 page:15 |

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | USD 2,042.5 million of Term Loan A-2 and revolver balances spring to March 2, 2030 | Uses September 30, 2026 balances; scheduled amortisation leaves 1,700.0 of Term Loan A-2 plus the revolver at that date (CP5-001) | Calculated | The springing date moves bank maturities ahead of the notes; overstating the amount overstates the near-wall refinancing need by 262.5 | Read as about 1,780.0 on scheduled amortisation and an unchanged revolver | CP-1 interpretation; CP-2 key findings, risks and calculations |
| Minor | Senior Notes carry restrictive covenants on liens, sale/leaseback and mergers | Source describes the 6.75% series only (CP5-002) | Weak Lineage | A general statement hides series that are not described | Limit the statement to the 6.75% series | CP-1 covenants table |
| Minor | Rate sensitivity of 8.9 per point on uncovered floating debt | Capped debt below the strikes also floats; SOFR level not supplied (CP5-004) | Assumption-Based | Interest exposure is understated if SOFR is below the strikes | State the qualifier | CP-2 key finding eight and calculations |
| Minor | Buybacks 862.5, 870.2 and 863 | Three bases without a bridge (CP5-006) | Conflicting | The central capital-allocation figure appears with different values | Use cash 870.2 and bridge the others | CP-1A governance; CP-1; CP-2 |

Orphan claim check (VE-015): the claim that covenant definitions and headroom cannot be verified is Insufficient Information but carries a limitation flag in all four handoffs, so it is not an orphan claim.

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases with page text; no credit agreement, indentures or guarantor list | Debt terms and covenant definitions cannot be verified from summaries | Covenant and priming conclusions stay restricted | Supply the agreements and certificates |
| Citation completeness | Ready with Remediation | Almost every figure has a page locator; the notes covenant statement generalises one series | A broad statement hides unseen series | Notes covenant terms uncertain | Correct citation (CP5-002) |
| Calculation traceability | Ready with Remediation | All 24 derived items recomputed or marked Not Calculable; one overstated exposure | An overstated springing amount misstates the near-wall need | Refinancing exposure misread by 262.5 | Read CP5-001 correction |
| Assumption transparency | Committee-Ready | Refinancing illustration, sensitivity and company basis all labelled | Assumptions are visible | Indicative use only | State qualifier for CP5-004 |
| Markdown and export artifact integrity | Committee-Ready | Six CP-OS headings, reader summaries and tables present in all four handoffs | Structure supports downstream use | None | None |

Overall auditability is Ready with Remediation, the lowest of the five dimension assessments.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Credit agreement, amendments and covenant definitions | Executed agreement, Ninth Amendment, compliance certificates | Headroom, Consolidated EBITDA add-backs and restricted-payment baskets cannot be tested | CP-1 covenants, CP-2 key finding six | High impact | Credit Agreement of August 12, 2019 and amendments |
| CP-5-GAP-002 | Indentures and guarantor list | Note indentures; Exhibit 21.1 | Ranking, guarantees and change-of-control terms unknown | CP-2 inventory | High impact | Indentures; Exhibit 21.1 |
| CP-5-GAP-003 | Interim cash interest paid | Supplemental cash-flow data for 2026 | Cash interest cover shown for FY2025 only | CP-1 interest cover chart | Medium impact | Later filing with supplemental data |
| CP-5-GAP-004 | Events after October 29, 2026; Q4 2026 results date | Later 8-Ks | Last week before the cutoff unknown | Event calendar | Medium impact | Form 8-K filings to 2026-11-05 |
| CP-5-GAP-005 | Quantification of legal and regulatory matters | Litigation estimates | Downside to earnings and cash unquantified | CP-2 risks | Medium impact | Later 10-Q or 8-K |
| CP-5-GAP-006 | SOFR level and cap detail beyond the table | Rate level at September 30, 2026 | Exposure of capped debt below strikes not sizable | CP-2 rate finding | Low impact | Item 3 market risk detail |
| CP-5-GAP-007 | Berkshire holding percentage; Berkshire and Elara agreements; proxy | Beneficial ownership table | Owner influence quantified only by agreement terms | CP-1A governance | Low impact | Proxy statement and agreements |
| CP-5-GAP-008 | Ratings, market prices and peers | Rating reports, prices | No market view of the credit | Out of scope | Low impact | Not required for this scope |
| CP-5-GAP-009 | Operating lease cost for the last twelve months | Lease note in later filing | Lease-adjusted leverage not shown | CP-2 inventory | Low impact | Next annual report |
| CP-5-GAP-010 | Text extraction not compared with filed HTML or XBRL | Original documents | Table-layout errors undetected | All figures | Low impact | Filed HTML or XBRL |

#### T5.1 Input module register

Module Status: Ready with Limitations (all four handoffs present with the six CP-OS headings; no YAML front matter, which this transport does not use; executed documents absent).

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/ee98afea.../1.response.md; dva-2026-11-05-credit_snapshot-host | Source readiness for four consumers | Seven filings and releases | Six headings present; reader summary and readiness view present | Not previously graded; accepted by the launcher | No defect found |
| CP-1 | requests/CP-1/32902eb6.../1.response.md; same run | Financial base FY2025 to Q3 2026 | Filings with company non-GAAP measures | Six headings, reader summary, four chart tables and one metrics table present | Not previously graded | Five findings (CP5-001 Material; CP5-002, CP5-003, CP5-006, CP5-008 Minor) |
| CP-1A | requests/CP-1A/ed89150e.../1.response.md; same run | Business, ownership, governance, timeline | Filings and releases | Six headings, three selector sections present | Not previously graded | Two Minor findings (CP5-006, CP5-007) |
| CP-2 | requests/CP-2/3286c7b5.../1.response.md; same run | Credit synthesis | CP-1 and CP-1A plus filing pages | Six headings, key findings and strengths sections present | Not previously graded | One Material (CP5-001) and five Minor (CP5-003, CP5-004, CP5-005, CP5-006, CP5-008) |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Covenants table, Senior Notes row: restrictive covenants on liens, sale/leaseback and mergers, "Not a financial maintenance test" | Partially Supported | The cited page (S1 page:184) describes covenants of the 6.75% Senior Notes only. Other series (4.625%, 3.75%, 6.875%) are not described in the pages read. | Limit the statement to the 6.75% series and mark the others Not supplied | Formatting / Hygiene Only |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Springing exposure of 2,042.5 (Term Loan A-2 1,962.5 plus revolver 80.0) described as falling due on March 2, 2030 | The figure uses September 30, 2026 balances. Term Loan A-2 amortises 12.5 per quarter through December 31, 2027 and 25.0 per quarter from March 31, 2028 (S1 page:181), so five quarterly payments of 12.5 and eight of 25.0 (262.5) fall before March 2, 2030, leaving 1,700.0; with the revolver at 80.0 the exposure is about 1,780.0 | None between sources; the error is in the framing | Read the exposure as about 1,780.0 on scheduled amortisation and an unchanged revolver | Restricts Committee Use |
| Minor | CP-1, CP-2 | Leverage numerator is principal (10,832.2) | Canon basis is balance sheet carrying value (current 112.5 plus long-term 10,656.6 = 10,769.1); CP-1 shows both amounts but computes ratios on principal; carrying value gives 3.54x against 3.56x | S4 page:3 against page:11 | Show both bases and the delta of 63.1 | Monitoring Follow-Up |
| Minor | CP-2 | Rate sensitivity of 8.9 per point on the 894.5 not covered by caps | Capped debt still floats below the strike rates (4.32% to 5.25%); the SOFR level is not supplied, so total sensitivity is Not Calculable; the 10-K reports 5.3 net of tax and caps for FY2025, which CP-2 cites | None | State that 8.9 covers only the uncovered amount, that capped debt floats below the strikes and that the SOFR level is not supplied (CP-2 already cites the 10-K estimate of 5.3) | Monitoring Follow-Up |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| None - lane clear | CP-1, CP-1A, CP-2 | Security, ranking, guarantee and covenant statements for the credit facilities and senior notes; Berkshire agreement and standstill terms | Executed credit agreement, indentures, Berkshire agreements | Rest on 10-K and 10-Q summaries; every handoff states the executed documents are not supplied and draws no covenant capacity, priming or recovery conclusion. The notes covenant generalisation is logged under CP5-002 | None; keep the Source Limitation tag | Legal review needed before any covenant capacity or recovery use |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None - lane clear | CP-2 | No price, spread, yield, rating, peer or relative-value claim is made; the refinancing illustration uses the issuer's own May 2025 coupon, not a market quote | Market quotes and comparables are not in the pack and not needed for this scope | Marked Not supplied in the gaps | None for this scope | Market Data Not Provided; no relative-value use is permitted from these handoffs |

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A, CP-1, CP-2 | Share repurchases appear as 862.5 (CP-1A governance row, repurchase table excluding commissions and excise), 870.2 (CP-1, CP-2, cash-flow statement) and 863 (release spend) without a bridge (CP5-006) | One version of each source; three statement bases | State cash 870.2 as the basis and bridge the others | None on ratios; capital-return figure needs one basis |
| Minor | CP-2 | Payor and international shares carry mixed periods and definitions: 26% and 11% are non-hospital commercial for FY2025; 31.9% is all commercial for nine months 2026; "about 10% of revenue" for international is FY2025 and is 11.0% for nine months 2026 (CP5-005) | FY2025 and nine months 2026 | Label the periods and definitions | None on conclusions |
| None - lane clear | CP-0, CP-1, CP-1A, CP-2 | Compared issuer name, run, period labels, total debt 10,832.2, leverage 3.38x, liquidity 1,915.6, maturities, covenant levels, lease and put balances, Berkshire terms: all agree | One version of each source; no draft or superseded document; the 2027 CMS rule status conflict is logged by CP-1A, the 6.875% and 6.785% naming conflict is logged by CP-1A | None; keep the logged conflicts open | None |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2, CP-1 | Promotional or Non-Credit Language | Words such as moderate, adequate, ample, wide and heavy carry no stated threshold in several places, and the caveat that the credit agreement is not supplied is repeated in the summary, key findings, strengths and weaknesses, risks and gaps (CP5-008) | Tie each word to a stated reference; state the caveat once where it changes a conclusion | Slight dilution; no effect on figures |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Ownership, governance and sponsor behaviour table | Rows carry a category and a locator but no evidence-quality grade (High, Medium, Low, Insufficient) that the method asks for; all rows rest on dated primary filings and would grade High, except the creditor-adverse row (Insufficient) (CP5-007) | Add the grade | None for consumers; grades inferred from the sources |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-1, CP-2 | Formula / Definition Drift | Springing exposure stated at September 30, 2026 balances (2,042.5); scheduled amortisation leaves about 1,780.0 at March 2, 2030 | Read as corrected here | Restricts Committee Use | Open |
| CP5-002 | Minor | CP-1 | Partially Supported Claim | Notes covenant text generalised from the 6.75% series | Limit to that series | Formatting / Hygiene Only | Open |
| CP5-003 | Minor | CP-1, CP-2 | Formula / Definition Drift | Principal used as debt basis; carrying value 10,769.1 and delta 63.1 not logged beside the ratios (3.54x on carrying value) | Show both bases | Monitoring Follow-Up | Open |
| CP5-004 | Minor | CP-2 | Assumption Not Qualified | Rate sensitivity of 8.9 omits capped debt floating below the strikes; SOFR level not supplied | State the qualifier | Monitoring Follow-Up | Open |
| CP5-005 | Minor | CP-2 | Period / Definition Drift | FY2025 shares of 26%, 11% and 10% sit beside nine-month 2026 data and an all-commercial 31.9% | Label periods and definitions | Formatting / Hygiene Only | Open |
| CP5-006 | Minor | CP-1A, CP-1, CP-2 | Cross-Module Inconsistency | Buybacks shown as 862.5, 870.2 and 863 without a bridge | Use cash 870.2 and bridge the others | Monitoring Follow-Up | Open |
| CP5-007 | Minor | CP-1A | Evidence Trace Defect | No evidence-quality grade on governance rows | Add grades | Monitoring Follow-Up | Open |
| CP5-008 | Minor | CP-2, CP-1 | Promotional or Non-Credit Language | Unbenchmarked judgement words and repeated caveats | Tie to references; state once | Formatting / Hygiene Only | Open |

## Calculations

All inputs in USD millions from the cited pages or from CP-1, CP-1A and CP-2. Every upstream derived number was recomputed; the results are in T5B.5. New calculations made in this audit:

- Springing exposure at March 2, 2030: Term Loan A-2 at September 30, 2026 is 1,962.5. Scheduled payments before March 2, 2030: December 31, 2026 (12.5); four quarters of 2027 (4 x 12.5 = 50.0); four quarters of 2028 (4 x 25.0 = 100.0); four quarters of 2029 (4 x 25.0 = 100.0); total 262.5. Balance 1,962.5 - 262.5 = 1,700.0. The March 31, 2030 payment falls after the date. With the revolver unchanged at 80.0, the exposure is 1,780.0, against 2,042.5 reported (difference 262.5, or 12.9% of 2,042.5). The amortisation terms are in [S1] page:181 and the March 2, 2030 date in [S4] page:11. Cross-check against the 2030 maturities of 4,570.3: 2,750.0 of 4.625% notes + 1,700.0 of Term Loan A-2 (75.0 of 2030 amortisation plus 1,625.0 at maturity) + 80.0 of revolver + about 23.8 of Term Loan B-2 amortisation (4 x 5.95, from 2,357.9 at June 30 to 2,352.0 at September 30) = 4,553.8, leaving about 16.5 for other debt (calculated approximation, assuming the revolver is unchanged).
- Debt on carrying value, September 30, 2026: 112.5 + 10,656.6 = 10,769.1; principal 10,832.2 - 10,769.1 = 63.1. Leverage on carrying value 10,769.1 / 3,042 = 3.54x against 3.56x on principal. Net of cash 495.6: (10,769.1 - 495.6) / 3,042 = 3.38x.
- Share of international in revenue, nine months 2026: 1,156 / 10,547.8 = 11.0% (CP-2 cites about 10% for FY2025, [S1] page:142).
- Buyback bases, nine months 2026: repurchase table 862.5 ([S4] page:18); cash paid for treasury stock 419.3 + 450.9 = 870.2 ([S4] page:4); release spend 863 ([S7] page:13); difference 870.2 - 862.5 = 7.7.
- Confidence score: lineage of the five material drivers: 2 Directly Sourced (weight 1.0), 2 Calculated (0.9), 1 Insufficient Information (0.0), E = (2 x 1.0 + 2 x 0.9 + 0) / 5 x 100 = 76. C = 17 of 17 required registers present = 100. S = 0.7 (partial source gate). P = 1 x 15 + 7 x 3 = 36. Score = (0.6 x 76 + 0.4 x 100) x 0.7 - 36 = 23.92, rounded to 24; the retained script gives band Insufficient Information and qa_status Restricted (a Material finding also caps the score at 59).
- Recomputed and matching, no change: LTM revenue 14,167.5 and operating income 2,121.2; 3.56x; 3.40x; 3.38x; 3.76x; 5.12x; 5.74x; 1,915.6 and 2,176.4; 4.2x; 77.0%; 1.62x, 988.2 and 474.8; 96.9%; 84.9% and 97.3%; payor shares; 2.7% and 3.0%.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreement, amendments, covenant definitions and compliance certificates missing (CP-5-GAP-001) | High | Committee, CP-2 users | Supply the executed agreement, the Ninth Amendment and compliance certificates |
| Indentures and guarantor list missing (CP-5-GAP-002) | High | Committee, CP-2 users | Supply the indentures and Exhibit 21.1 |
| CP5-001 correction lives only in this answer | Medium | Anyone reading CP-1 or CP-2 alone | Read those handoffs with this answer; the earlier handoffs cannot be edited |
| Interim cash interest, events after October 29, 2026, legal quantification (CP-5-GAP-003 to CP-5-GAP-005) | Medium | Committee | Supply later filings and cash-flow supplemental data |
| SOFR level, Berkshire percentage and agreements, ratings, lease cost, extraction check (CP-5-GAP-006 to CP-5-GAP-010) | Low | Committee | Supply as listed in the gaps ledger |

## Next module

- Report assembly: use the corrected statement. Say that about 1,780.0 of Term Loan A-2 and revolver balances would fall due on March 2, 2030 on scheduled amortisation if the 4.625% senior notes are still outstanding then, not 2,042.5; use cash buybacks of 870.2 as the single basis; label FY2025 payor shares and use the 31.9% all-commercial share for nine months 2026.
- Committee use stays restricted until the credit agreement, compliance certificates and the executed debt documents are supplied; then rerun CP-2 and CP-5.
