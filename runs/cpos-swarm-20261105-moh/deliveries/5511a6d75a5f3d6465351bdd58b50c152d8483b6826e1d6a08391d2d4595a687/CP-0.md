## Request

Issuer: MOLINA HEALTHCARE, INC. (ticker MOH, Delaware registrant, Commission file number 1-31719; consolidated reporting entity, parent-level notes). As-of date and cutoff: 2026-11-05. Pathway: credit snapshot, public case, reporting currency USD (all issuer statements are in USD millions unless stated). Current period Q3 2026 (quarter and nine months ended September 30, 2026); prior period FY2025 (year ended December 31, 2025).

Question answered here: can the supplied source set support the downstream work (financial extraction, business and transaction context, fundamental credit synthesis, evidence-trace review), and what remains blocked? This handoff gives no credit conclusion, legal interpretation or investment opinion, and it normalizes or reconciles no figures; the tie-outs under `## Calculations` only test whether sources agree with each other.

Context file (user settings, not issuer evidence): borrower, parent, guarantor, sponsor, deal terms, quotes, ratings, peers and research questions are all blank or empty in the context. They are therefore not supplied; none is treated as zero.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Family and authority | Period or date |
| --- | --- | --- | --- |
| 10-K_2025-12-31_moh-20251231.htm.jsonl | c9fc11483fb4b7c19a024a1eea5a26db7d569aa891c87974935ef7d58e311c73 | Audited annual report; controlling for FY2025 facts | FY2025, year ended December 31, 2025; auditor report dated February 10, 2026 (page:105) |
| 10-Q_2026-03-31_moh-20260331.htm.jsonl | 13a11f49b2609a371d7feaaf1fc732c450976bf0759ca520903d8cae2d01480e | Unaudited quarterly report; controlling for Q1 2026 | Q1 2026, signed April 23, 2026 (page:40) |
| 10-Q_2026-06-30_moh-20260630.htm.jsonl | 2e116fbc160064a31ee8ffdf3cb7b87c5a30be87614aee212f07d7cf0a47d671 | Unaudited quarterly report; controlling for Q2 2026 | Q2 2026, six months ended June 30, 2026 |
| 10-Q_2026-09-30_moh-20260930.htm.jsonl | 0eb181a17a96ec54e5242c30d2326e1cb431ceae3183b3fa8dd8bb665798cbdd | Unaudited quarterly report; controlling for Q3 2026 | Q3 2026, nine months ended September 30, 2026; signed October 22, 2026 (page:44) |
| EX-99.1_2026-04-22_moh1q26_er.htm.jsonl | 209474d035cda2f89bcc2ac9abfc62e08120c0698a0cff7b05687b4b711891da | Earnings release; management-attributed supporting claims | Q1 2026, dated April 22, 2026 |
| EX-99.1_2026-07-22_moh2q26_er.htm.jsonl | fd72c687dc87193147ac248ab3371c514003ac36c928d56dc905298dfee99d6d | Earnings release; management-attributed supporting claims | Q2 2026, dated July 22, 2026 |
| EX-99.1_2026-10-21_moh3q26_er.htm.jsonl | f0ee0db37cb0340d37b34fde6c6107463ac060309062b86bfa3e7caa6f07a604 | Earnings release; management-attributed supporting claims | Q3 2026, dated October 21, 2026 |

The context file (sha256 038deefd3d0187dee809d7ec7eb3f32548cc8a768b8a64a8e4dfbffc4bec802f) holds run settings only. The runner ignored `_retrieval.json`; it is not evidence here.

### Supplied handoffs

None. CP-0 is the first module in the run, so no upstream handoff exists. Each of the seven sources is a distinct filing; no source is a duplicate of another, and no source is a draft.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases cover annual and quarterly financials, debt and liquidity through September 30, 2026, and they agree with each other. Downstream work can proceed, with covenant, rating and legal-document limits. | Medium | No credit agreement, indentures, rating reports or reported covenant ratio values are supplied, and there are no presentation slides. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Quarterly premium revenue of $10,172 million, $10,244 million and $10,457 million sums to the nine-month figure of $30,873 million. Net income sums to $112 million. | Releases and filings can be used together without a reconciliation break. | High |
| Debt is five senior unsecured notes of the parent, $3,800 million principal and $3,771 million carrying value at September 30, 2026; nothing is drawn on the $1.25 billion revolver. | Maturity and facility analysis is supportable from the filings. | High |
| An amendment dated February 4, 2026 cut the interest coverage floor to 1.75 to 1.00 through December 31, 2026. Filings state compliance but print no ratio. | Covenant headroom cannot be measured from the supplied sources. | Medium |
| The only rating evidence is the annual report statement that each senior note is rated BB by S&P and Ba2 by Moody's. | Rating evidence is dated to the annual report; later rating actions are not supplied. | Medium |

### Readiness view

The source set is adequate for the requested snapshot, with bounded limitations. Every section the later analysis needs is present in text form in the filed statements: income statement, balance sheet and cash flow for FY2025 and for each 2026 quarter, the debt note, the liquidity discussion with the revolver and covenant summary, segment tables, and the legal and subsequent-event disclosures. Filed statements and the audited annual report control; the three earnings releases are attributed management claims and agree with the filings on every tied figure. The strongest contrary evidence is not a conflict but an absence: the executed credit agreement, its February 2026 amendment and the indentures are listed in the annual report exhibit index but are not in the pinned set, no actual covenant ratio is printed, no letter-of-credit usage figure is printed, and rating information is limited to one annual-report sentence. The mechanism is that covenant definitions and headroom, revolver availability net of letters of credit, and note guarantor structure then rest on filer summaries rather than executed terms, so any later covenant or liquidity-headroom statement must be labelled as a summary-based limitation. Nothing in the set is blocked. No document dated after the cutoff is used. The next evidence action, if the committee needs covenant headroom, is to add the executed credit agreement, first amendment and the five note indentures, and the compliance figures or rating agency reports.

### Source-by-source assessment

| Source | Entity and perimeter | Basis and coverage | Located evidence | Limitation |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31 | Molina Healthcare, Inc. consolidated; parent-only condensed information in Schedule I (pages 142-144) | US GAAP, USD millions, FY2025 with FY2024 and FY2023 comparatives; all 154 of 154 pages carry text | "Premium revenue $ 43,052" (page:105); "Long-term debt 3,766" (page:106); debt table and maturities (page:130); credit agreement and amendment (pages 131-132); debt ratings (page:94) | Tables are flattened to text; page:85 begins mid-table. Extraction fidelity was not reviewed against the rendered filing. |
| 10-Q_2026-03-31 | Consolidated | Unaudited, Q1 2026 (three months) with Q1 2025 comparative; 40 of 40 pages carry text | "Net income $ 14 $ 298" (page:2); impairment of $93 million (page:25); debt (page:14) | Same text-extraction limitation. |
| 10-Q_2026-06-30 | Consolidated | Unaudited, Q2 2026 and six months; 43 of 43 pages carry text | Debt (pages 14-15); covenant summary (page:39); liquidity (pages 34-40) | Same. |
| 10-Q_2026-09-30 | Consolidated | Unaudited, Q3 2026 and nine months, with December 31, 2025 balance sheet; 44 of 44 pages carry text | Statements (pages 2-4); debt (pages 14-15); legal (pages 18-19); liquidity (pages 35-41) | Same. |
| EX-99.1 Q1, Q2, Q3 2026 | Consolidated | Quarterly releases with GAAP and non-GAAP reconciliations; 8 of 8, 9 of 9 and 9 of 9 pages carry text | Q3 release: "Premium Revenue $10,457 $10,841 $30,873 $32,337" (page:1) | Adjusted net income appears only in the releases (none in the Q3 quarterly report), so it is a management measure, not a filed GAAP figure. |

### Consumer assessment

| Consumer | Assessment | Evidence it needs and what is present | Carried limitations |
| --- | --- | --- | --- |
| CP-1 (financial extraction) | READY_WITH_LIMITATIONS | Annual and quarterly statements, segment tables, debt note, cash flow and liquidity text present for FY2025 and Q1 to Q3 2026 | No covenant ratio values, no letter-of-credit usage, no guarantor schedule; adjusted measures are release-only |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, segments, contract awards and losses, MAPD exit, Florida contract, legal proceedings and subsequent events are in the annual and quarterly reports | No presentation slides; no ownership or sponsor information needed (listed public company, sponsor blank in context) |
| CP-2 (credit synthesis) | READY_WITH_LIMITATIONS | Depends on upstream registers; source evidence for business risk, financial risk and liquidity is present | Covenant headroom, executed-document terms and rating actions after the annual report are not supplied |
| CP-5 (evidence trace review) | READY_WITH_LIMITATIONS | Cross-filing tie-outs pass (see `## Calculations`); locators exist for all material facts | Extraction fidelity not reviewed; releases are management claims |

This is a source-sufficiency assessment only (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED). No downstream analysis is asserted as complete.

### Key located facts by area

- Debt: "4.375% Notes due June 15, 2028 $ 800 $ 800", "3.875% Notes due November 15, 2030 650 650", "6.500% Notes due February 15, 2031 850 850", "3.875% Notes due May 15, 2032 750 750", "6.250% Notes due January 15, 2033 750 750", "Deferred debt issuance costs (29) (34)", "Total $ 3,771 $ 3,766" (10-Q Q3, page:14). Maturities at December 31, 2025: "Total $ 3,800 $ — $ — $ 800 $ — $ 650 $ 2,350" for 2026, 2027, 2028, 2029, 2030 and thereafter (10-K, page:130). The notes are described as "senior unsecured obligations of the parent corporation, Molina Healthcare, Inc." (10-Q Q3, page:15).
- Revolver: "revolving credit facility (“Credit Facility”) of $1.25 billion, a $15 million swingline sub-facility, a $100 million letter of credit sub-facility", term "November 20, 2030", "As of September 30, 2026, no amount was outstanding under the Credit Agreement" (10-Q Q3, page:15); "we had available borrowing capacity of $1.25 billion under the Credit Facility" (10-Q Q3, page:40).
- Covenants: "minimum Interest Coverage Ratio threshold of 3.0 to 1.0, and a maximum Consolidated Total Debt to Capital Ratio of 60%, with a step-up to 65%"; amendment "on February 4, 2026 ... 1.75:1.00" for quarters ending March 31, 2026 through December 31, 2026, then 2.00:1.00, 2.50:1.00 and 2.75:1.00 for the March, June and September 2027 quarters; "we were in compliance with all non-financial and financial covenants" (10-Q Q3, page:15).
- Liquidity: parent "Cash, cash equivalents and investments ... approximately $608 million and $223 million as of September 30, 2026, and December 31, 2025" (10-Q Q3, page:36); consolidated cash and cash equivalents $4,479 million and investments $4,100 million at September 30, 2026 (10-Q Q3, page:2); regulated subsidiaries hold most of this and are subject to statutory capital rules (10-K, page:93).
- Ratings: "Each of our senior notes is rated “BB” by Standard & Poor’s, and “Ba2” by Moody’s Investor Service, Inc." (10-K, page:94). Date basis is the annual report, filed with an audit report dated February 10, 2026.
- Subsequent and recent events relevant to the cutoff: Securities Action "formally dismissed by the Court with prejudice" on October 20, 2026 and the Derivative Action dismissal notice filed October 6, 2026 (10-Q Q3, pages 18-19); shares outstanding "approximately 52.2 million" as of October 16, 2026 (10-Q Q3, page:1); "$500 million remained available" for share repurchase as of October 16, 2026 (10-Q Q3, page:40); Florida Kids Medicaid contract commenced October 1, 2026 (10-Q Q3, page:29); guidance for FY2026 reaffirmed on October 21, 2026 (Q3 release, page:2).
- Impairment: a $93 million impairment on intangible assets tied to the exit of the MAPD product for 2027 (10-Q Q1, page:25), consistent with the "approximately $93 million" estimate in the annual report (page:108) and the nine-month impairment line in the Q3 income statement (page:2).

## Calculations

These are source-consistency checks only, not normalization. All amounts are USD millions.

| Check | Inputs and locators | Result |
| --- | --- | --- |
| Nine-month premium revenue | Q1 10,172 (Q1 release, page:5); Q2 10,244 (Q2 release, page:1); Q3 10,457 (Q3 release, page:1) | 10,172 + 10,244 + 10,457 = 30,873, equal to the nine-month 30,873 in the Q3 report (page:2) |
| Six-month premium revenue | Q1 10,172; Q2 10,244 | 20,416, equal to the Q2 release six-month figure 20,416 |
| Nine-month net income | Q1 14; Q2 60; Q3 38 (10-Q Q3 equity statement, page:3) | 14 + 60 + 38 = 112, equal to 112 in the Q3 report (page:2) |
| Nine-month interest expense | Q1 54 (10-Q Q1, page:2); Q2 54 (Q2 release); Q3 53 (Q3 release, page:5) | 54 + 54 + 53 = 161, equal to 161 in the Q3 report (page:2) |
| Principal outstanding | 800 + 650 + 850 + 750 + 750 (10-Q Q3, page:14) | 3,800 |
| Carrying value | 3,800 less deferred debt issuance costs 29 | 3,771, equal to the long-term debt line 3,771 (10-Q Q3, page:2) |
| December 31, 2025 carrying value | 3,800 less 34 (10-K, page:130) | 3,766, equal to the balance sheet (10-K, page:106) |
| Debt maturity total | 800 + 650 + 2,350 (10-K, page:130) | 3,800; no principal falls due in 2026, 2027, 2029 as shown at December 31, 2025 |

Not calculated here by design: leverage, coverage ratios, liquidity headroom and any normalized quarter. The defined covenant ratios cannot be recomputed because the sources give the covenant names but not the definitions.

## Gaps

| Gap | Search performed | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| Executed credit agreement dated November 20, 2025, first amendment dated February 4, 2026 and the five note indentures are not supplied; they are listed in the annual report exhibit index (page:153) | Searched the pinned set for credit agreement, indenture and amendment; found only filer summaries | Medium | CP-1, CP-2, CP-5 | Add the executed documents before any statement on covenant definitions, baskets or guarantees |
| Actual interest coverage and debt to capital values are not printed | Searched all sources for Interest Coverage Ratio and Debt to Capital; only thresholds and compliance statements appear (10-K pages 131-132; 10-Q Q3 page:15) | Medium | CP-1, CP-2 | Add compliance certificate or have analysts compute with a stated definition caveat |
| Letters of credit outstanding under the $100 million sub-facility are not printed | Searched for letter of credit, standby, surety, performance bond; only the sub-facility size appears. The filings state available borrowing capacity of $1.25 billion | Low | CP-1, CP-2 | Obtain a facility utilization statement |
| Ratings are only the annual report sentence (BB, Ba2) | Searched Moody, S&P, rated, rating in all sources; nothing after the annual report | Low | CP-2 | Add current agency reports if needed |
| Subsidiary guarantee status of the notes is not stated; notes are described as obligations of the parent | Searched guarant in the annual report and the Q3 report; only generic text found | Low | CP-1, CP-2 | Read the indentures |
| Parent-only financials are annual only (10-K pages 142-144); quarterly parent data is limited to parent cash and investments | Reviewed Schedule I and the quarterly liquidity text | Low | CP-1, CP-2 | Treat parent liquidity statements as annual or quarter-end only |
| No investor presentation in the pinned set; three earnings releases stand in | Reviewed source list | Low | CP-1A | None required for the minimum set |
| Adjusted net income and per-share adjusted figures are management non-GAAP measures found only in the releases | Searched the Q3 quarterly report for adjusted net income: none | Low | CP-1, CP-5 | Label as management measure |
| Extraction fidelity and table layout were not reviewed against the rendered documents; some tables are flattened or split across pages | Page index reviewed for all pages; key pages read in full | Low | All | Spot-check figures against the filings at use |
| Full-year 2026 guidance (premium revenue of approximately $42 billion, adjusted earnings of at least $5.25 per diluted share) is a management statement in the Q3 release (page:2) | Reviewed the guidance paragraph | Low | CP-1A, CP-2 | Label as guidance |

Conflicts between documents: none found among the tied figures above. The retained-source basis for each period is the filed report; the release is used only as a cross-check.

## Next module

Proceed to the financial extraction module (CP-1) with all seven sources, carrying these limitations: no actual covenant ratio, no letter-of-credit usage, no executed legal documents, ratings as of the annual report only, adjusted measures release-only, and labelled periods (Q3 2026, nine months 2026, FY2025). The business context module, the credit synthesis module and the evidence-trace review follow in the dependency order the runner sets. No consumer is conditional or blocked.
