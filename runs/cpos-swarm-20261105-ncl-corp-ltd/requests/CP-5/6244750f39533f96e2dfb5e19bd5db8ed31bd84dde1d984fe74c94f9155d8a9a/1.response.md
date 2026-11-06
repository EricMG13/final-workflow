# CP-5 — Evidence trace and research integrity QA: NCL CORP Ltd. (ncl-corp-ltd)

## Request

NCL CORP Ltd. (issuer id `ncl-corp-ltd`; the filings name the registrant NCL Corporation Ltd., "NCLC"), as of 2026-11-05, pathway `credit_snapshot`. Scope: trace the top five credit drivers of the earlier handoffs (CP-0, CP-1, CP-1A, CP-2) to the seven pinned filings and releases, recompute every derived number, search the sources again for every gap marked Not supplied, and grade the research for committee use. Run `ncl-corp-ltd-2026-11-05-credit_snapshot-host`; a host session, no provider call.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | 1590d4030e80abfbd09d00a74521526f72070052531a8716f865a880a8fa9501 | Audited FY2025 statements, debt table, revolver terms, pension note, segment note |
| 10-Q_2026-03-31_nclc-20260331x10q.htm.jsonl | 1693fea3f52de137a2e148c9e6f9853be5398eb34944625b7e837b2bd396c943 | Q1 2026 statements, liquidity, repayment schedule |
| 10-Q_2026-06-30_nclc-20260630x10q.htm.jsonl | 2f18ccd1a947471efb9474a7bd377c5db5871d9445b97fe0a1fc7e783f6d645f | Q2 2026 statements, liquidity, repayment schedule |
| 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | 7769d1c310cec4c8e024523931f2cd599a487768128283054dca38ddd11d7d93 | Q3 2026 statements, debt, liquidity, commitments, market risk, subsequent events |
| EX-99.1_2026-05-04_exh_991.htm.jsonl | 19e48d4c7cb2b40fb1bcbfbbe436e7e39f669c8965c4e705c327d948db3f04d8 | Q1 2026 parent press release (supporting) |
| EX-99.1_2026-07-30_exh_991.htm.jsonl | ffe75efbccd58bfc3c88fabf4a188883f7003d5a095dba1da47bbe08c4d94307 | Q2 2026 parent press release (supporting) |
| EX-99.1_2026-10-29_exh_991.htm.jsonl | 6f93f8906074ef388d05f277a1b3874ed298e830f3945372d3d73a8925dc791c | Q3 2026 parent press release (supporting) |
| context | 1eac4b587c5c6cd9d96c3f400eed0e70dc9aa1137a14c30469dde7d21791294f | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 240a9004c9f054e89ac320762ee0dbd447c416d5523fbbb0826a7a829f32f3c2 | Audited: source readiness |
| CP-1 | 0d306e620183fe5605e53df2bfa6840225b9fdf3340d4d66074ce76c6547a7b6 | Audited: financial base |
| CP-1A | 3ea102b4043a2f05facc314042b53d7d4ce7ff98e5ddc43910a907daf003a111 | Audited: business and transaction context |
| CP-2 | 8de8b4e726e42817ca2b4b105e5656373aac29ed39c6eb4fb5f8d83eca1c6e1d | Audited: credit synthesis |

Locators are `page:N` of the pinned `.jsonl` text of each source. Consistency with upstream: this answer re-anchors on all four handoffs, which share run `ncl-corp-ltd-2026-11-05-credit_snapshot-host`, issuer, as-of date and period labels. It finds one Material and seven Minor defects, listed in the issue log (CP5-001 to CP5-008). The earlier handoffs cannot be edited, so the corrections live in this answer. All other figures recomputed here match.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The earlier research is traceable to the filings and its numbers recompute, but one material omission and seven minor defects restrict committee use. The main omission is a second springing-maturity trigger on the revolver. | Low | Credit agreements, covenant values and the October 2026 amendment are not supplied, so legal terms rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every recomputed ratio matched, including 5.51x total and 5.42x net leverage on last-twelve-months Adjusted EBITDA of 2,700.1. | Leverage figures can be relied on as arithmetic from the company Adjusted EBITDA measure. | High |
| The revolver can mature before January 22, 2030 under a clause tied to senior notes above 400 million; earlier handoffs showed only the November 17, 2026 clause. | The effective revolver tenor and the 2029 and 2030 refinancing picture may be shorter than stated. | Medium |
| A pension obligation of 34.7 was reported as not supplied, and the nine-vessel collateral for the revolver was omitted. | Both sharpen the claims outside debt and the ranking picture, though neither changes leverage. | High |
| Covenant values and the October 2026 amendment text have no source evidence. | Headroom and post-amendment terms cannot be traced or assessed. | Low |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 2 are directly sourced, 1 are calculated, 0 are assumption-based, 0 are analyst inferences, and 2 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the revolver's springing-maturity mechanics: the earlier handoffs reported the November 17, 2026 test but not the second trigger tied to senior notes above USD 400 million, and the liquidity test and the October 2026 amendment are not in the sources. This matters because the revolver is the main liquidity backstop, so its effective maturity decides when refinancing pressure arrives, and it implies committee use stays restricted until the credit agreement and amendment are supplied.

### Traceability summary

| Rank | Credit driver | Classification | Traceability status | Most important gap |
| --- | --- | --- | --- | --- |
| 1 | Leverage and earnings trend | Calculated | Committee-Ready | Adjusted EBITDA is a company non-GAAP measure |
| 2 | Liquidity and the October 2026 financing | Directly Sourced | Committee-Ready | Revolver drawn amount and pro forma issuer cash are not supplied |
| 3 | Revolver springing maturity and the maturity profile | Weak Lineage | Remediation Needed | Second trigger omitted; liquidity test and amendment not supplied |
| 4 | Newbuild commitments and funding | Directly Sourced | Committee-Ready | Three effective contracts are not yet financed |
| 5 | Covenant headroom | Insufficient Information | Not Traceable | No covenant ratio values or definitions |

### Audit summary and clearance

Confidence Score: 19 / 100 (Band: Insufficient Information). qa_status: Restricted. committee_status: Restricted. The score is the canon formula clamp((0.6 x E + 0.4 x C) x S - P, 0, 100): E = 64 from the lineage of the five material drivers (one Calculated at 9, two Directly Sourced at 10, one Weak Lineage at 3 and one Insufficient Information at 0, averaged and scaled to 100), C = 100 because all 17 required registers are present, S = 0.7 because the source gate is partial (executed agreements are missing), and P = 36 from one Material finding (15) and seven Minor findings (21). Score = (0.6 x 64 + 0.4 x 100) x 0.7 - 36 = 18.88, rounded to 19. The low band reflects missing legal evidence on the central open item and the penalty for eight defects; it does not mean the recomputed arithmetic is unreliable.

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 1. Minor Issues: 7. Committee Use: Restricted.

No finding changes a ratio or the direction of the credit view, but one committee-facing account of the revolver's maturity is incomplete (CP5-001), so committee use is restricted until that account is read with the correction in this answer and the credit agreement and October 2026 amendment are supplied.

### Remediation priority map

- Must-fix before committee: CP5-001. Read CP-1's maturity bucket and CP-2's third key finding together with this answer: the revolver's January 22, 2030 date is a stated maximum, and the clause tied to senior notes above USD 400 million can bring it forward to 91 days before the final maturity of any such note series not repaid or refinanced beyond April 23, 2030. The 7.75% senior unsecured notes due 2029 (USD 600.0 million in the 10-K table title) meet the size test; their exact maturity date is not in the pages read.
- Must-fix before the handoff is consumed downstream: None. The correction travels with this answer.
- Monitoring follow-up: CP5-003 (pension obligation 34.7 is supplied), CP5-005 (revolver collateral of nine vessels), CP5-006 (trend of advance ticket sales), CP5-007 (evidence-quality grades on governance rows).
- Formatting and hygiene: CP5-002, CP5-004 and CP5-008.

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

Module Status: Ready with Limitations. Traceability Scope: Top 5. Files used: seven pack sources and four handoffs. Missing required inputs: executed credit agreement and amendments, indentures, newbuild loan agreements, covenant compliance certificate, subsidiary guarantor exhibit. External sources: none used by the upstream handoffs or by this answer. Entity key: issuer_id ncl-corp-ltd available.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | Audited filing, primary | FY2025 | NCL Corporation Ltd. consolidated | Statements, debt table, revolver terms, pension note, segment note | Text extraction only; reduced disclosure format | CP-1 base, CP-2 debt table |
| S2 | 10-Q_2026-03-31_nclc-20260331x10q.htm.jsonl | Unaudited filing, primary | Q1 2026 | NCL Corporation Ltd. consolidated | Statements, liquidity, repayment schedule | Unaudited | LTM and quarterly figures |
| S3 | 10-Q_2026-06-30_nclc-20260630x10q.htm.jsonl | Unaudited filing, primary | Q2 2026 and six months | NCL Corporation Ltd. consolidated | Statements, liquidity, repayment schedule | Unaudited | LTM and quarterly figures |
| S4 | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | Unaudited filing, primary | Q3 2026 and nine months | NCL Corporation Ltd. consolidated | Statements, debt, liquidity, commitments, market risk, subsequent events | Unaudited; no instrument table | Current-period base |
| S5 | EX-99.1_2026-05-04_exh_991.htm.jsonl | Management release, supporting | Q1 2026 | Norwegian Cruise Line Holdings Ltd. (parent) | Parent liquidity, net leverage | Management prepared; parent perimeter | Perimeter label only |
| S6 | EX-99.1_2026-07-30_exh_991.htm.jsonl | Management release, supporting | Q2 2026 | Parent | Parent liquidity, net leverage | Management prepared; parent perimeter | Perimeter label only |
| S7 | EX-99.1_2026-10-29_exh_991.htm.jsonl | Management release, supporting | Q3 2026 | Parent | Parent liquidity, pro forma liquidity, net leverage, delivery timing | Management prepared; parent perimeter | Perimeter label; pro forma label |
| S8 | context | Run settings, not evidence | 2026-11-05 | Run | As-of date, currency, periods | Not issuer evidence | Scope |
| H0 | CP-0 handoff | Analyst handoff | As of 2026-11-05 | Issuer | Source readiness | Host authored | Audited here |
| H1 | CP-1 handoff | Analyst handoff | FY2025 to Q3 2026 | Issuer | Financial base | Host authored | Audited here |
| H1A | CP-1A handoff | Analyst handoff | As of 2026-11-05 | Issuer | Business and transaction | Host authored | Audited here |
| H2 | CP-2 handoff | Analyst handoff | As of 2026-11-05 | Issuer | Credit synthesis | Host authored | Audited here |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage of 5.51x total and 5.42x net on last-twelve-months Adjusted EBITDA of 2,700.1, with Q3 2026 Adjusted EBITDA down 8.1% | CP-1, CP-2 | Balance sheet debt lines, Adjusted EBITDA reconciliation | Higher debt and lower earnings leave little cushion before covenant or rating pressure | Direction of the credit trend | S4 page:3, page:36; S1 page:83, page:122 | Company non-GAAP EBITDA; covenant EBITDA differs |
| 2 | Liquidity of about 1,350.7 at September 30, 2026 and the October 2026 financing | CP-1, CP-2 | Liquidity text, subsequent events note | Liquidity covers 2026 and 2027 scheduled principal on the printed figures | Near-term default risk is moderated by liquidity | S4 page:6, page:11 to page:12, page:38 | Availability is rounded to 0.1 billion; pro forma cash not supplied |
| 3 | Revolver springing maturity (November 17, 2026) and the maturity profile | CP-1, CP-2 | Revolver terms in the debt note | The facility is the main backstop and its effective maturity sets refinancing timing | Time-critical open item | S1 page:142; S4 page:38 | Liquidity test undefined; second trigger omitted upstream; amendment text missing |
| 4 | Newbuild commitments of 19,421.2 with about 10.8 billion of export-credit facilities and three effective contracts not yet financed | CP-1, CP-1A, CP-2 | Commitments note, newbuild chart, market risk | Delivery payments are contractual and add debt | Capital intensity and funding need | S4 page:20, page:40 to page:42, page:44 | Financing of three contracts not secured |
| 5 | Covenant headroom against maintenance tests | CP-1, CP-2 | Covenant text only | Breach would trigger cross-default | Headroom cannot be measured | S1 page:41; S4 page:13 | No ratio values, definitions or agreements |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Balance-sheet debt 14,884.5 at September 30, 2026 | CP-1 | Four balance sheet lines (S4 page:3) | Yes | Filing | Calculated | Recomputed | High | Committee-Ready |
| Total debt / Adjusted EBITDA 5.51x; net 5.42x | CP-1, CP-2 | 14,884.5 and 14,633.8 over 2,700.1 | Yes | Filing, company non-GAAP EBITDA | Calculated | Recomputed, matches | Medium | Committee-Ready |
| Q3 2026 Adjusted EBITDA 936.7 against 1,019.4, down 8.1% | CP-1, CP-2 | S4 page:36 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Liquidity about 1.4 billion: cash 250.7 and about 1.1 billion available | CP-1, CP-2 | S4 page:6 and page:38 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| October 2026 notes issue, revolver upsizing to about 2.8 billion, 2028 notes redeemed | CP-1, CP-1A, CP-2 | S4 page:11 to page:12 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Revolver springing maturity November 17, 2026 tied to the 2027 exchangeable notes | CP-1, CP-2 | S1 page:142 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Revolver maturity January 22, 2030 shown as the maturity bucket | CP-1, CP-2 | S1 page:142 clause (a) | Partial | Filing, incomplete reading | Weak Lineage | Corrected here (CP5-001) | Medium | Remediation Needed |
| Scheduled principal by year, total 15,498.0 | CP-1, CP-2 | S4 page:12 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Ship contracts 19,421.2; export-credit facilities about 10.8 billion; three contracts not yet financed | CP-1, CP-1A, CP-2 | S4 page:20, page:41, page:42 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Unfunded 2027 spending plus principal is 1.02x LTM operating cash flow | CP-2 | 3.1 and 2.0 billion; 1,105.7; 2,169.0 | Yes | Filing figures, rounded plan | Calculated | Recomputed, illustrative | Low | Committee-Ready |
| Covenant headroom | CP-1, CP-2 | Types named, values absent | Yes | Filing | Insufficient Information | Correctly marked Not calculable | Low | Not Traceable |
| Compliance with covenants at September 30, 2026 | CP-1, CP-2 | S4 page:13 | Yes | Filing statement | Directly Sourced | Verified | Medium | Committee-Ready |
| Parent linkage: NCLH owns all shares and guarantees the exchangeable notes | CP-1A, CP-2 | S1 page:2, page:71, page:144 | Yes | Filing | Directly Sourced | Verified | High | Committee-Ready |
| Issuer versus parent perimeter differences in cash, net income and debt | CP-0, CP-1 | S4 page:2, page:36; S7 page:1, page:14, page:18 | Yes | Filing against release | Directly Sourced | Verified | High | Committee-Ready |
| Single reportable segment, so no segment diversification inside the issuer | CP-1A | S1 page:128 | Partial | Filing, narrower than the statement | Weak Lineage | Corrected here (CP5-002) | Medium | Remediation Needed |
| Shipboard Retirement Plan obligation Not supplied | CP-1, CP-2 | S1 page:159 states 34,729 thousand | No | Gap fillable from the 10-K | Untraced | Corrected here (CP5-003) | High | Remediation Needed |
| Governance behaviour Supportive or Neutral | CP-1A | Equity contributions, no distributions, refinancing | Yes | Filings | Analyst Inference | Labelled interpretation | Medium | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents 250.7 at September 30, 2026 | pack/10-Q_2026-09-30_nclc-20260930x10q.htm | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | S4 | page:2 balance sheet; page:6 | CP-1 liquidity | Sourced | Filing | Opened and confirmed |
| Liquidity about 1.4 billion; 1.1 billion available | pack/10-Q_2026-09-30_nclc-20260930x10q.htm | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | S4 | page:6 and page:38 | CP-1, CP-2 liquidity | Sourced | Filing | Opened and confirmed |
| Debt lines 918,784; 212,464; 12,214,862; 1,538,363 (thousands) | pack/10-Q_2026-09-30_nclc-20260930x10q.htm | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | S4 | page:3 balance sheet | CP-1 leverage | Sourced | Filing | Sum 14,884,473 confirmed |
| Scheduled principal total 15,497,999 and yearly buckets | pack/10-Q_2026-09-30_nclc-20260930x10q.htm | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | S4 | page:12 Debt Repayments | CP-1 maturities, CP-2 | Sourced | Filing | Buckets sum to the total |
| Adjusted EBITDA 936,702; 2,136,035; 2,167,348; FY2025 2,731,377 | pack/10-Q_2026-09-30_nclc-20260930x10q.htm | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | S4; S1 | S4 page:36; S1 page:83 | CP-1 metrics | Sourced | Filing | Quarter sum confirmed |
| Operating cash flow 1,709,302 and additions 2,292,043 for 9M 2026 | pack/10-Q_2026-09-30_nclc-20260930x10q.htm | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | S4 | page:3 cash flows | CP-1 cash flow | Sourced | Filing | Opened and confirmed |
| Cash paid for interest 952.0 including early redemption premiums | pack/10-K_2025-12-31_nclc-20251231x10k.htm | 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | S1 | page:169 supplemental cash flow | CP-1 interest cover | Sourced | Audited | Only year with printed cash interest |
| Early redemption premium 162,374 | pack/10-K_2025-12-31_nclc-20251231x10k.htm | 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | S1 | page:123 cash flows | CP-1 interest cover | Sourced | Audited | Opened and confirmed |
| Revolver maturity January 22, 2030 with springing clauses (a), (b) and (c) | pack/10-K_2025-12-31_nclc-20251231x10k.htm | 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | S1 | page:142 Note 9 | CP-1, CP-2 debt | Sourced | Audited | Clause (a) not carried upstream |
| Revolver and guarantees secured by first-priority interests in nine vessels | pack/10-K_2025-12-31_nclc-20251231x10k.htm | 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | S1 | page:147 to page:148 | CP-2 inventory | Sourced | Audited | Not carried upstream (CP5-005) |
| Covenant types and levels | pack/10-K_2025-12-31_nclc-20251231x10k.htm | 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | S1 | page:41 risk factor | CP-1, CP-2 covenants | Sourced | Audited | No ratio values printed |
| October 2026 notes, revolver amendment, redemption of 2028 notes | pack/10-Q_2026-09-30_nclc-20260930x10q.htm | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | S4 | page:11 to page:12 | CP-1, CP-1A, CP-2 | Sourced | Filing | Amendment text not supplied |
| Ship construction contracts 19,421,174; export-credit facilities about 10.8 billion | pack/10-Q_2026-09-30_nclc-20260930x10q.htm | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | S4 | page:20, page:42 | CP-1, CP-2 | Sourced | Filing | Opened and confirmed |
| Anticipated spending 1.1, 3.1 and 1.8 billion against export-credit funding 0.6, 2.0 and 1.3 billion | pack/10-Q_2026-09-30_nclc-20260930x10q.htm | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | S4 | page:40 | CP-2 funding | Sourced | Filing | Rounded to 0.1 billion |
| Interest rate and currency sensitivities | pack/10-Q_2026-09-30_nclc-20260930x10q.htm | 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | S4 | page:43 to page:44 | CP-2 | Sourced | Filing | Opened and confirmed |
| Parent liquidity, pro forma liquidity, net leverage 5.5x | pack/EX-99.1_2026-10-29_exh_991.htm | EX-99.1_2026-10-29_exh_991.htm.jsonl | S7 | page:3, page:18 | CP-0, CP-1 perimeter | Sourced | Release | Parent perimeter; not used as issuer figure |
| Shipboard Retirement Plan projected benefit obligation 34,729 thousand | pack/10-K_2025-12-31_nclc-20251231x10k.htm | 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | S1 | page:159 pension note | Not used upstream | Sourced | Audited | New in this audit (CP5-003) |
| Each brand is an operating segment aggregated into one reportable segment | pack/10-K_2025-12-31_nclc-20251231x10k.htm | 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | S1 | page:128 segment reporting | CP-1A operating model | Sourced | Audited | CP-1A wording narrower (CP5-002) |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA Q3 2026 | CP-1 leverage | 2,731,377; 2,136,035; 2,167,348 (thousands) | 2,731,377 + 2,136,035 - 2,167,348 = 2,700,064 | Calculated | Recomputed, matches | High | Leverage | S1 page:83; S4 page:36 |
| LTM Adjusted EBITDA Q1 and Q2 2026 | CP-1 | 533,254; 453,211; 1,199,333; 1,147,997 | 2,811,420 and 2,782,713 | Calculated | Recomputed, matches | High | Leverage trend | S2, S3 EBITDA tables |
| Balance-sheet debt at four dates | CP-1 | Four balance sheet lines per date | 14,583,441; 15,025,080; 14,982,382; 14,884,473 | Calculated | Recomputed, matches | High | Leverage | S1 page:122; S2, S3, S4 balance sheets |
| Total debt / LTM Adjusted EBITDA | CP-1, CP-2 | Debt and LTM EBITDA | 5.34; 5.34; 5.38; 5.51 | Calculated | Recomputed, matches | High | Leverage | as above |
| Net debt / LTM Adjusted EBITDA | CP-1, CP-2 | Debt less cash 203,996; 179,200; 212,261; 250,722 | 5.26; 5.28; 5.31; 5.42 | Calculated | Recomputed, matches | High | Leverage | as above |
| Principal-basis leverage | CP-1 | Repayment schedule totals 14,994,609; 15,609,507; 15,467,745; 15,497,999 | 5.49; 5.55; 5.56; 5.74 | Calculated | Recomputed, matches | High | Basis comparison | S1 page:150; S2 page:10; S3 page:11; S4 page:12 |
| LTM interest expense, net and proxy cover | CP-1 | 971,036; 184,447; 244,222; 374,362; 504,235; 564,473; 782,390 | 911,261; 841,163; 753,119; cover 3.09; 3.31; 3.59; FY2025 2.81 | Calculated | Recomputed, matches | High | Coverage proxy | S1 page:121; S2-S4 statements |
| FY2025 cash interest cover | CP-1 | 2,731,377; 952,000; 162,374 | 2.87 and 3.46 excluding premium | Calculated | Recomputed, matches | High | Coverage | S1 page:169, page:123 |
| LTM operating cash flow and additions | CP-1 | FY2025 2,077,283 and 3,259,606; 9M 1,709,302 and 2,292,043; 9M 2025 1,617,591 and 2,821,959 | 2,168,994 and 2,729,690; difference -560,696 | Calculated | Recomputed, matches | High | Cash conversion | S1 page:123; S4 page:3 |
| Quarterly derivations | CP-1 | Year-to-date reports | Q2 604,999; Q3 292,790 operating cash flow; Q2 457,694; Q3 397,682 additions | Calculated | Recomputed, matches | High | Cash flow trend | S2, S3, S4 page:3 |
| Adjusted EBITDA margins | CP-1 | EBITDA over revenue | 22.9; 25.2; 31.8; 27.0; 28.6; 27.8; 26.6 percent | Calculated | Recomputed, matches | High | Seasonality | S4 page:36 and statements |
| Liquidity sum | CP-1, CP-2 | 250.7 and about 1,100 | 1,350.7 against about 1.4 billion stated | Calculated | Recomputed, matches | Medium | Liquidity | S4 page:6 |
| Pro forma revolver availability | CP-2 | About 1,100; commitment increase about 300; repayment 380.0 | About 1,780, in line with the parent's 1.8 billion | Calculated | Recomputed, matches | Low | Liquidity | S4 page:12; S7 page:3 |
| 2027 funding ratio | CP-2 | 3.1 minus 2.0 billion; 1,105.7; 2,169.0 | 2,205.7 / 2,169.0 = 1.02x | Assumption-Based | Recomputed; rounded plan and trailing cash flow | Low | Deleveraging room | S4 page:40, page:12 |
| Maturity shares | CP-2 | 4,134.3; 1,346.1; 1,370.0; 15,498.0 | 26.7 percent and 44.2 percent | Calculated | Recomputed, matches | High | Refinancing | S4 page:12 |
| Debt composition at December 31, 2025 | CP-2 | 5,237.6; 1,925.1; 1,100.0; 6,312.1; 8.7 | Shares 35.9; 13.2; 7.5; 43.3; 0.1 percent | Calculated | Recomputed, matches | High | Structure | S1 page:140 |
| Implied variable-rate debt | CP-2 | 18.2 per one percentage point | 18.2 / 1 percent = about 1,820, about 12 percent of debt | Calculated | Recomputed, matches | Medium | Rate risk | S4 page:43 |
| Pro forma maturity buckets | CP-2 | 1,346.1; 525.0; 4,134.3; 380.0; 1,875.1; 950.0 | 821.1; 3,754.3; 2,825.1 | Assumption-Based | Recomputed; assumes full 525.0 outstanding and revolver in 2030 | Low | Refinancing | S4 page:11, page:12; S1 page:140 |
| Interest change net of extinguishment | CP-1, CP-2 | 782,390; 202,525; 564,473 | 579,865; -2.7 percent | Calculated | Recomputed, matches | High | Interest burden | S4 page:35, page:2 |
| Covenant headroom | CP-1, CP-2 | Levels only | Needs covenant EBITDA and debt service definitions | Not Calculable (definitions not supplied) | Correctly not computed | Low | Covenant risk | S1 page:41 |

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | The Revolving Loan Facility matures January 22, 2030, with only the November 17, 2026 springing test | Clause (a) of the same sentence brings the maturity forward to 91 days before the final maturity of any senior note series above USD 400 million not repaid or refinanced beyond April 23, 2030 (CP5-001) | Weak Lineage | The effective tenor of the main backstop, and the 2029 refinancing picture, are shorter than shown | Read as corrected; obtain the credit agreement | CP-1 maturity bucket and covenants section; CP-2 third key finding |
| Minor | Single reportable segment, so no segment diversification | Brands are operating segments aggregated into one reportable segment; brand results are not supplied (CP5-002) | Weak Lineage | Overstates a structural conclusion | Reword | CP-1A operating model table |
| Minor | Pension obligation Not supplied | The 10-K prints 34,729 thousand (CP5-003) | Untraced | A fillable gap was left open | Use 34.7 | CP-1 claims table, CP-2 inventory |
| Minor | Locator and gap precision in CP-1A | Dividend evidence cited to page:3 sits on page:4; waterpark opening date rests on the release; sale proceeds of 105.0 are supplied (CP5-004) | Directly Sourced | Locator drift reduces trace quality | Correct | CP-1A governance and gaps |
| Minor | Revolver security not stated | First-priority interests in nine vessels are stated (CP5-005) | Directly Sourced | Ranking and collateral context | Add | CP-2 debt and claims inventory |
| Minor | Float trend | Advance ticket sales not trended (CP5-006) | Calculated | Canon requires the trend of non-debt funding float | Add trend | CP-2 |
| Minor | Governance rows | No evidence-quality grade (CP5-007) | Directly Sourced | Reader cannot grade each source | Add High grades | CP-1A governance table |
| Minor | Caveat repetition | Perimeter caveat repeated across sections (CP5-008) | Calculated | Presentation rule asks for each limitation once | State once | CP-0, CP-1, CP-2 |

Orphan claim check (VE-015): the claim that covenant headroom cannot be measured is Insufficient Information but carries a limitation flag in all four handoffs, so it is not an orphan claim. The pension claim in CP5-003 was an unsupported Not supplied statement and is corrected here.

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases with page text; no agreements, amendment text or compliance certificate | Terms of debt cannot be verified from summaries | Covenant and maturity conclusions stay restricted | Supply agreements and amendment |
| Citation completeness | Ready with Remediation | Almost every figure carries a page locator; two locators drift and two gap statements (pension obligation and sale proceeds) were not searched exhaustively | A weak locator hides narrower or wider wording | Small | Correct locators (CP5-003, CP5-004) |
| Calculation traceability | Committee-Ready | All derived items recomputed with formulas and inputs; the rounded-plan ratio is labelled illustrative | Visible arithmetic | Ratios can be relied on | None |
| Assumption transparency | Committee-Ready | Pro forma buckets and the 2027 funding ratio state their assumptions | Assumptions are visible | Indicative use only | None |
| Markdown and export artifact integrity | Committee-Ready | Six CP-OS headings, reader summaries and tables present in all four handoffs | Structure supports downstream use | None | None |

Overall auditability is Ready with Remediation, the lowest of the five dimension assessments.

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Revolver credit agreement, liquidity test, third amendment and exact maturity date of the 7.75% notes due 2029 | Executed agreement and amendment dated October 15, 2026; 2029 indenture | The effective revolver maturity and the November 17, 2026 test cannot be resolved | CP-1 maturities, CP-2 third key finding | High impact | Credit agreement exhibits listed in the Q3 10-Q; indenture |
| CP-5-GAP-002 | Covenant ratio values, covenant EBITDA and free liquidity definition | Compliance certificate and agreement definitions | Headroom cannot be measured | CP-1 covenants, CP-2 seventh key finding | High impact | Credit agreement and certificates |
| CP-5-GAP-003 | Instrument-level debt table at September 30, 2026; security and guarantors by instrument | Later filing or indentures | Ranking and structure rest on December 31, 2025 data | CP-2 inventory | Medium impact | Indentures; subsidiary guarantor exhibit |
| CP-5-GAP-004 | Revolver drawn amount, letters of credit and issuer pro forma cash after October 2026 | Facility reports | Liquidity is stated rounded and partly parent-level | CP-1 and CP-2 liquidity | Medium impact | Later filing or lender report |
| CP-5-GAP-005 | Parent and issuer debt totals do not reconcile in the text | Parent consolidating schedule | Perimeter mixing risk | CP-0, CP-1 | Medium impact | Parent filings |
| CP-5-GAP-006 | Governance, beneficial ownership and executive compensation | Items 10 to 13 omitted by reduced disclosure | Control and alignment context | CP-1A | Medium impact | Parent filings |
| CP-5-GAP-007 | Same-date prior-year advance ticket sales (Q3 2025) | Q3 2025 balance sheet | Seasonal float cannot be trended like for like | CP-2 | Low impact | Q3 2025 quarterly report |
| CP-5-GAP-008 | Events from October 29, 2026 to 2026-11-05 | Later Form 8-K filings | For example repayment of the 2027 exchangeable notes | Event calendar | Medium impact | Form 8-K filings to the cutoff |
| CP-5-GAP-009 | Text extraction not compared with filed HTML or XBRL | Original documents | Table-layout errors undetected | All figures | Low impact | Filed HTML or XBRL |

#### T5.1 Input module register

Module Status: Ready with Limitations (all four handoffs present with the six CP-OS headings; no YAML front matter, which this transport does not use; executed documents absent).

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | requests/CP-0/86f379bea14f.../1.response.md; ncl-corp-ltd-2026-11-05-credit_snapshot-host | Source readiness for four consumers | Seven filings and releases | Six headings present; reader summary and readiness view present | Not previously graded; passed the launcher's structure check | No defect found beyond CP5-008 |
| CP-1 | requests/CP-1/c8d6aeec963f.../2.response.md; same run | Financial base FY2025 to Q3 2026 | Filings with company non-GAAP measures | Six headings, reader summary, chart tables and one metrics table present | Not previously graded; accepted on attempt 2 after a reader-summary number check | Material CP5-001 and Minor CP5-003, CP5-008 |
| CP-1A | requests/CP-1A/a98426681d16.../1.response.md; same run | Business, transaction, governance | Filings and releases | Six headings, three selector sections present | Not previously graded | Minor CP5-002, CP5-004, CP5-007 |
| CP-2 | requests/CP-2/6e600b7af9ea.../1.response.md; same run | Credit synthesis | CP-1 and CP-1A plus 10-K and Q3 10-Q pages | Six headings, key findings and strengths sections present | Not previously graded | Material CP5-001 and Minor CP5-003, CP5-005, CP5-006 |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Revolver maturity bucket (CP-1 debt maturities, FY2030) and CP-2 third key finding | Partially Supported | The 10-K sentence (page:142) has three clauses. CP-1 and CP-2 carry the January 22, 2030 date and clauses (b) and (c) for November 17, 2026 but not clause (a) | Read the revolver as maturing no later than January 22, 2030 and possibly 91 days before the final maturity of a senior note series above USD 400 million that is not repaid or refinanced beyond April 23, 2030 | Restricts Committee Use |
| Minor | CP-1, CP-2 | Shipboard Retirement Plan obligation marked Not supplied | Not Supported | The 10-K pension note (page:159) prints a projected benefit obligation of 34,729 thousand, 1.9 million current and 32.8 million non-current | Use 34.7 as an outside-debt claim | Monitoring Follow-Up |
| Minor | CP-1A | Operating model row Segment | Partially Supported | The statement says the business has a single reportable segment and no diversification inside the issuer; page:128 says each brand is an operating segment, aggregated | State that brand-level results are not supplied | Formatting / Hygiene Only |
| Minor | CP-1A | Governance row on dividends cited to Q3 10-Q page:3; operating model row on the waterpark cited to Q3 10-Q page:32 | Supported | The financing section is on page:4; the September 2026 opening date is on Q3 release page:1 | Correct locators | Formatting / Hygiene Only |
| Minor | CP-1A | Gaps: sale prices of Oceania Sirena Not supplied | Partially Supported | Cash proceeds from sale of ships of 105.0 and a loss on disposal of 16.8 are printed (S4 page:3, page:7); only the gross price and buyer are absent | Say proceeds are supplied | Formatting / Hygiene Only |
| Minor | CP-2 | Debt and claims inventory: revolver security and the statement that security by loan is not stated | Partially Supported | The 10-K says the Revolving Loan Facility and related guarantees are secured by first-priority interests in nine vessels (page:147 to page:148) and that the 2025 refinancing repaid the senior secured notes | Add collateral description | Monitoring Follow-Up |
| Minor | CP-1A | Governance table | Supported | No evidence-quality grade per row | Add grades | Monitoring Follow-Up |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None - lane clear | CP-1, CP-2 | All ratios, LTM flows, quarterly derivations, shares and tie-outs recomputed | Formulas, inputs and periods match; the rounded 2027 funding ratio and pro forma buckets state their assumptions | None between sources; parent versus issuer totals are a perimeter difference, not an error | None | None |
| Minor | CP-2 | Advance ticket sales not trended | Canon requires non-debt funding float to be trended. Balance 3,200.6 at December 31, 2025 against 3,106.0 a year earlier is up 3.0 percent; 3,142.0 at September 30, 2026 is down 1.8 percent from December 31, 2025. Q3 2025 balance not supplied, so a like-for-like seasonal comparison is not possible | S1 page:122 against S4 page:3 | Add the trend and the gap | Monitoring Follow-Up |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Revolver maturity and springing mechanics (CP5-001) | Seventh Amended and Restated Credit Agreement and the third amendment | Clause (a), the liquidity test and the amendment effect are not in the sources | Read with the correction; obtain the agreement | Legal review needed before any maturity, covenant capacity or ranking use |
| Minor | CP-2 | Security and guarantor statements for the revolver and notes | Credit agreement, indentures, guarantor exhibit | Collateral of nine vessels omitted; guarantor names not supplied | Add collateral; keep guarantor gap | Legal review needed before any recovery use |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| None - lane clear | CP-2 | No price, spread, yield, peer or relative-value claim is made; ratings are quoted from the filing | Market quotes and comparables are not in the pack and not needed for this scope | Marked Not supplied in the gaps | None for this scope | Market Data Not Provided; no relative-value use is permitted from these handoffs |

#### T5.6 Cross-module consistency and version control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | The revolver is shown at January 22, 2030 in CP-1 and described only through the November 17, 2026 test in CP-2; neither carries clause (a) | One version of each source; the Q3 10-Q does not restate the clause | Read with the correction in CP5-001 | Maturity and refinancing narrative, committee use |
| None - lane clear | CP-0, CP-1, CP-1A, CP-2 | Compared issuer name, run, period labels, Adjusted EBITDA definition, debt 14,884.5, liquidity, maturities, newbuild commitments and the label ambiguity for the 2031 Notes: all agree | No draft or superseded source | None | None |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-2 | Promotional or Non-Credit Language | The issuer-versus-parent perimeter caveat and the not-a-covenant-ratio caveat are repeated in several sections of each handoff, and judgement words such as heavy and adequate carry no stated threshold | State each caveat once where it changes a conclusion; tie judgement words to figures | Slight dilution; no effect on figures |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Ownership, governance and sponsor behaviour table | Rows carry a category and a locator but no evidence-quality grade (High, Medium, Low, Insufficient) that the method asks for; all rows rest on dated primary filings and would grade High | Add the grade | None for consumers; grades inferred from the sources |
| None - lane clear | CP-0, CP-1, CP-2 | Headings, reader summaries, selector sections, source and handoff tables | Present and matched the launcher's checks | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-1, CP-2 | Partially Supported Claim | Revolver maturity shown without the clause that can bring it forward to 91 days before a qualifying senior note maturity | Read as corrected; obtain agreement | Restricts Committee Use | Open |
| CP5-002 | Minor | CP-1A | Partially Supported Claim | Segment row overstates absence of diversification | Reword | Formatting / Hygiene Only | Open |
| CP5-003 | Minor | CP-1, CP-2 | Gap Fillable From Sources | Pension obligation marked Not supplied though 34.7 is printed | Use 34.7 | Monitoring Follow-Up | Open |
| CP5-004 | Minor | CP-1A | Evidence Trace Defect | Two locators drift and the sale proceeds gap is overstated | Correct | Formatting / Hygiene Only | Open |
| CP5-005 | Minor | CP-2 | Partially Supported Claim | Revolver collateral of nine vessels omitted | Add | Monitoring Follow-Up | Open |
| CP5-006 | Minor | CP-2 | Formula / Definition Drift | Advance ticket sales float not trended | Add trend and gap | Monitoring Follow-Up | Open |
| CP5-007 | Minor | CP-1A | Evidence Trace Defect | No evidence-quality grade on governance rows | Add grades | Monitoring Follow-Up | Open |
| CP5-008 | Minor | CP-0, CP-1, CP-2 | Promotional or Non-Credit Language | Repeated caveats and unbenchmarked adjectives | State once | Formatting / Hygiene Only | Open |

## Calculations

All inputs in USD millions unless thousands are stated, taken from the cited pages or from CP-1 and CP-2. Every upstream derived number was recomputed; the results are in T5B.5. New calculations made in this audit:

- Revolver clause (a) test: the 10-K table title gives USD 600.0 million for the 7.75% senior unsecured notes due 2029 (10-K page:140); 600.0 exceeds the USD 400 million threshold, so the notes qualify if outstanding and not refinanced beyond April 23, 2030. The 6.125% notes due 2028 (USD 525.0 million) also exceeded it and were redeemed from the October 2026 proceeds (S4 page:11). The exact 2029 maturity date is not in the pages read, so the trigger date is Not calculable.
- Pension: current portion 1.9 + non-current 32.8 = 34.7, equal to the projected benefit obligation of 34,729 thousand (10-K page:159).
- Advance ticket sales: 3,200,593 / 3,105,964 - 1 = +3.0 percent (December 2025 against December 2024); 3,141,976 / 3,200,593 - 1 = -1.8 percent (September 30, 2026 against December 31, 2025). Quarterly balances from CP-1: 3,718.9 at March 31, 3,651.2 at June 30 and 3,142.0 at September 30, 2026.
- Sale of ships: proceeds 104,995 thousand in nine months 2026 and loss on disposal 16,825 thousand (S4 page:3, page:7).
- Confidence score: lineage of the five material drivers: 1 Calculated (weight 9), 2 Directly Sourced (10), 1 Weak Lineage (3), 1 Insufficient Information (0), E = (9 + 10 + 10 + 3 + 0) / 5 x 10 = 64. C = 17 of 17 required registers present = 100. S = 0.7 (partial source gate). P = 1 x 15 + 7 x 3 = 36. Score = (0.6 x 64 + 0.4 x 100) x 0.7 - 36 = 78.4 x 0.7 - 36 = 54.88 - 36 = 18.88, rounded to 19; band Insufficient Information; qa_status Restricted because a Material finding is open.
- Recomputed and matching, no change: LTM Adjusted EBITDA 2,700.1; 5.34x, 5.34x, 5.38x and 5.51x total; 5.26x, 5.28x, 5.31x and 5.42x net; 2.81x, 3.09x, 3.31x and 3.59x proxy cover; 2.87x and 3.46x FY2025 cash cover; 26.7 percent and 44.2 percent maturity shares; 1.02x funding ratio; debt composition shares; implied variable debt of about 1,820.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| The revolver credit agreement, its liquidity test, the third amendment and the maturity date of the 7.75% notes due 2029 are not supplied (CP-5-GAP-001). | High | Committee, readers of CP-1 and CP-2 | Obtain the agreement and amendment listed in the Q3 10-Q exhibit index; confirm whether the 2027 exchangeable notes are repaid or refinanced before November 17, 2026. |
| Covenant ratio values and definitions are not supplied (CP-5-GAP-002). | High | Committee | Supply compliance certificates and agreement definitions. |
| The CP5-001 correction lives only in this answer. | Medium | Anyone reading CP-1 or CP-2 alone | Read them with this answer; the earlier handoffs cannot be edited. |
| Instrument table at September 30, 2026, guarantors, revolver drawn amount and issuer pro forma cash (CP-5-GAP-003, CP-5-GAP-004). | Medium | Committee | Supply later filings or indentures. |
| Parent and issuer totals do not reconcile; governance detail omitted by reduced disclosure (CP-5-GAP-005, CP-5-GAP-006). | Medium | Committee | Look to parent filings. |
| Prior-year same-date advance ticket sales, events after October 29, 2026, extraction check (CP-5-GAP-007 to CP-5-GAP-009). | Low to Medium | Committee | Supply as listed in the gaps ledger. |

## Next module

- Report assembly: use the corrected statements. Say that the revolver's stated maturity is January 22, 2030 but that it can spring to November 17, 2026 on the 2027 exchangeable-note test and, under a separate clause, to 91 days before the maturity of a qualifying senior note series above USD 400 million, with the 2029 notes the next qualifying series. State the pension obligation of 34.7 and the nine-vessel collateral.
- Committee use stays restricted until the credit agreement, the October 2026 amendment and the covenant compliance evidence are supplied; then rerun CP-2 and CP-5.
