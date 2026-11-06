## Request

Module: source readiness for BAYTEX ENERGY CORP. (issuer id bte, TSX and NYSE: BTE, Alberta, Canada; sector per run context "Drilling Oil & Gas Wells"). As-of date 2026-11-05; evidence cutoff 2026-11-05. Pathway: credit snapshot. Reporting currency per run context: CAD (all pinned financial statements are in thousands of Canadian dollars, with US$ amounts labelled). Current period per context: Q2 2026 (quarter ended June 30, 2026); prior period: FY2025.

Question: can the pinned source set support the four requested downstream consumers (CP-1 financial data, CP-1A business and transaction context, CP-2 fundamental credit synthesis, CP-5 evidence trace validation), and what remains blocked? This module gives no credit conclusion, no legal interpretation and no investment opinion, and it does not normalize, reconcile or calculate figures. No upstream handoff exists for this module (it is first in the run).

The run context names no borrower, no parent, no guarantors, no ratings, no market data, no deal terms and no legal documents ("legal_documents": "none"). Blank context values are treated as not supplied, not as zero.

## Sources

### Issuer sources relied on

| Alias | Exact source name | sha256 |
| --- | --- | --- |
| S1 | 40-F_2025-12-31_bte-20251231.htm.jsonl | 7928c3aee2847a067565e87aab941fb0fa693ec3a05da16abf228b0aca516096 |
| S2 | 6-K-EX-99.1_2025-09-30_a991-q32025fs.htm.jsonl | 88b3b8e7d8e11703b95eab9a12edb425d85ec75970d2d968e209a9c3a366a490 |
| S3 | 6-K-EX-99.1_2025-12-31_a991-2025yepressrelease.htm.jsonl | 3673c1a3e44baf8845d8213620919370a57219f3e6310c71f221c475210c6b47 |
| S4 | 6-K-EX-99.1_2026-03-31_a991-q12026fs.htm.jsonl | 792eab73e1363b4073690efb2135aa655fd77f770258c41719cb471c48ece251 |
| S5 | 6-K-EX-99.1_2026-03-31_tm2613640d2_ex99-1.htm.jsonl | 9b4c8c62190d6a1b8a9c4e232069f5ad6fc7f4c944563935fd4bf5121d096095 |
| S6 | 6-K-EX-99.1_2026-06-30_a991-q22026fs.htm.jsonl | 16eeba2e704f92279ab76d18bdc0c26c8ff5c06bb58d42d66e8037ca77adddf4 |
| S7 | 6-K-EX-99.1_2026-08-05_tm2619297d2_ex99-1.htm.jsonl | 2da1f8d94e5a6b644192e34205faf74054d51d4cb86b7a7a5ff6f34cc5c6aa6a |

Run context (user settings, not issuer evidence): /workspace/secdata/data/2026-11-05/contexts/1279495-baytex-energy-corp-bte.json, sha256 a4beb54d12cde8b01d2e19e329c06ce5b476e74c9a66d64a29ea9c069505e245.

The pack also holds `_retrieval.json`, which CP-OS ignores; it is not evidence. Where this handoff mentions filing dates it labels them "pack metadata".

### Supplied handoffs

None. CP-0 is the first module of this run; no upstream handoff with a module code and sha256 was supplied.

### Citation form

A locator is `alias page:N`, where the page is the source chunk number in the pinned `.jsonl` file, not a printed page. Quotes are exact substrings of that chunk (whitespace-normalised).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filed interim statements and results releases support financial, business-context and synthesis work, with bounded limits. The audited annual statements, annual information form and all debt documents are missing, so debt terms and annual figures rest on summaries. | Medium | Annual report exhibits and debt agreements are referenced but not in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual report is only a cover document; the audited statements, annual information form and management discussion are not included. | Full-year 2025 figures rest on a results release and later comparatives, not audited statements. | High |
| No credit agreement or note indenture is included; covenant and debt facts come from company summaries in the statements. | Guarantors, security, baskets and call terms cannot be verified from legal text. | High |
| The Eagle Ford sale changed the reporting perimeter, so figures before 2026 mix restated and unrestated bases. | Trend and leverage comparisons across the sale date need care and explicit labelling. | High |
| The latest document in the pack is the second quarter of 2026; nothing later is included. | Anything after August 2026 up to the as-of date cannot be assessed from this pack. | Medium |

### Readiness view

The source set is READY_WITH_LIMITATIONS for all four selected consumers. The pack carries filed second quarter 2026, first quarter 2026 and third quarter 2025 interim statements, a fourth quarter 2025 results release and two combined results-plus-management-discussion exhibits. This is enough text-located evidence for each consumer to perform its own method on the current capital structure (a revolving credit facility, one remaining series of senior notes, lease obligations) and on the post-Eagle Ford Canadian business. No consumer is CONDITIONAL or BLOCKED, because no missing source prevents any of them from running. The limits are bounded but real: the audited annual financial statements, annual information form and annual management discussion (exhibits to the annual report, S1) are referenced and not retained; no debt agreement is retained, so the company's own summaries are the only authority for covenants and note terms; the reporting perimeter changed on the Eagle Ford sale, so pre-2026 comparatives mix bases; and the pack stops at the second quarter 2026 documents. Every figure and claim a consumer uses should carry these limits forward. Source sufficiency here is not completion of any downstream analysis. This is a source-sufficiency view only; no model-input contract is evaluated.

### Coverage and document register

| Alias | Document family | Original authority | Entity and perimeter | Period and basis | Version relationship |
| --- | --- | --- | --- | --- | --- |
| S1 | Annual report cover (Form 40-F, 6 chunks) | Filed annual report; but its substantive exhibits are not retained | BAYTEX ENERGY CORP., the registrant; Baytex Energy USA, Inc. appears only as agent for service | Fiscal year ended December 31, 2025 | Standalone wrapper; exhibits 99.1 to 99.4 and certifications are cited by reference only |
| S2 | Unaudited condensed interim financial statements (19 chunks) | Filed interim statements (IAS 34); controls interim facts | Consolidated, still including U.S. operations (pre-sale; multi-column segment table at page:6) | Q3 2025 and nine months, versus December 31, 2024 | Standalone; not restated for the later discontinued-operations presentation |
| S3 | Fourth quarter and full-year 2025 results release (16 chunks) | Management release; attributed claims, with reconciliation tables | Consolidated, with a Canada versus Discontinued operations split in the production and adjusted funds flow tables | Q4 2025 and FY2025 against Q3 2025 and 2024 | Standalone; says audited statements are on the company website and later on SEDAR+ and EDGAR |
| S4 | Unaudited condensed interim financial statements (18 chunks) | Filed interim statements; controls interim facts | Continuing (Canada) with Eagle Ford as discontinued operations | Q1 2026, versus December 31, 2025 | Standalone; its statements and notes also appear inside S5 (spot-checked: net loss, cash, net cash, covenant table) |
| S5 | Results release, management discussion and interim statements (67 chunks) | Mixed: release and discussion are management claims; statements are filed interim statements | As S4 | Q1 2026 (release dated May 7, 2026) | Superset of S4; both retained as active sources |
| S6 | Unaudited condensed interim financial statements (18 chunks) | Filed interim statements; controls interim facts | As S4; one operating segment | Q2 2026 and six months, versus December 31, 2025; 2025 comparatives revised | Standalone; its statements and notes also appear inside S7 (spot-checked: covenants, notes, net cash, adjusted funds flow) |
| S7 | Results release, management discussion and interim statements (89 chunks) | Mixed, as S5 | As S4 | Q2 2026 (release dated July 30, 2026) | Superset of S6; both retained as active sources |

Containment basis: S4 inside S5 and S6 inside S7 were established by matching specific figures and wording at the cited locators, not by hash identity and not by a full line-by-line comparison. For a statement fact, the standalone statements (S4, S6) are retained as the primary source and the combined exhibit (S5, S7) as the containing document. Management-discussion and release content exists only in S5 and S7. Pack metadata lists filings on 2026-05-08 (S4), 2026-05-12 (S5), 2026-07-31 (S6) and 2026-08-05 (S7); all precede the cutoff.

Coverage counts: 7 of 7 pinned sources have retained text (no image-only source in this pack); the chunk counts above total 233 retained chunks. Text extraction only: no chart, image or speaker-note content is claimed, and no presentation is in the pack. A successful extraction is not a fidelity review of tables.

### Evidence register

| ID | Source | Locator | Exact quote |
| --- | --- | --- | --- |
| E1 | S1 | page:2 | For the Registrant's Annual Information Form for the year ended December 31, 2025, see Exhibit 99.1 of this Annual Report on Form 40-F. |
| E2 | S1 | page:2 | see Exhibit 99.2 of this Annual Report on Form 40-F |
| E3 | S1 | page:2 | see Exhibit 99.3 of this Annual Report on Form 40-F |
| E4 | S1 | page:1 | agent for service in the United States |
| E5 | S3 | page:6 | Our audited consolidated financial statements for the year ended December 31, 2025 and the related Management's Discussion and Analysis of the operating and financial results can be accessed on our website |
| E6 | S3 | page:5 | On December 19, 2025, Baytex completed the divestiture of its U.S. Eagle Ford assets for net proceeds of US$2.2 billion |
| E7 | S3 | page:5 | have been classified as discontinued operations for the current and comparative periods |
| E8 | S6 | page:4 | A segment note is no longer presented as there is only one operating segment at period end. |
| E9 | S6 | page:8 | Baytex had $750 million of revolving credit facilities |
| E10 | S6 | page:8 | that mature on June 27, 2030. The Credit Facilities are secured |
| E11 | S6 | page:10 | The long-term notes do not contain any significant financial maintenance covenants |
| E12 | S6 | page:9 | Total Debt totaled $95.5 million of principal amounts outstanding |
| E13 | S6 | page:9 | Bank EBITDA for the twelve months ended June 30, 2026 was $758.9 million |
| E14 | S6 | page:9 | Interest Coverage (3) (Minimum Ratio) 9.3:1.0 3.5:1.0 |
| E15 | S6 | page:9 | Senior Secured Debt (1) to Bank EBITDA (2) (Maximum Ratio) 0:0:1.0 3.5:1.0 |
| E16 | S6 | page:8 | Baytex continues to be in compliance with all financial and commercial covenants under its debt agreements. |
| E17 | S6 | page:9 | Baytex had $4.4 million of outstanding letters of credit |
| E18 | S7 | page:49 | The 7.375% Senior Notes were issued on April 1, 2024 and US$64.1 million remains outstanding as at June 30, 2026. |
| E19 | S7 | page:48 | The agreements and associated amending agreements relating to the Credit Facilities are accessible on the SEDAR+ website |
| E20 | S7 | page:38 | redeemed the 8.5% Senior Notes and partially redeemed the 7.375% Senior Notes |
| E21 | S2 | page:9 | 8.50% notes due April 30, 2030 |
| E22 | S7 | page:46 | adjusted funds flow from continuing operations of $254.4 million for Q2/2026 and $406.6 million for YTD 2026 |
| E23 | S7 | page:18 | Adjusted funds flow $ 254,433 $ 151,125 $ 366,919 $ 405,558 |
| E24 | S5 | page:3 | Adjusted funds flow - Discontinued operations (4) (1,086 ) |
| E25 | S6 | page:14 | The most recent statement of account issued by the CRA assert taxes owing by the trusts of $244.8 million |
| E26 | S7 | page:50 | Baytex retains liability for matters related to our prior ownership of assets located in the U.S. |
| E27 | S6 | page:1 | Subsequent event (note 11) |
| E28 | S7 | page:49 | As at July 30, 2026, there were 699.2 million common shares issued and outstanding |
| E29 | S7 | page:6 | we have no WTI hedges in place after Q2/2026 |
| E30 | S6 | page:3 | Interest paid $ 842 $ 53,957 $ 5,295 $ 90,632 |
| E31 | S6 | page:6 | In February 2026, ownership transferred to Gibson |
| E32 | S2 | page:9 | Total Debt (4) to Bank EBITDA (2) (Maximum Ratio) 1.1:1.0 4:0:1.0 |
| E33 | S6 | page:2 | Comparative period has been revised to reflect current period presentation of continuing and discontinued operations. |
| E34 | S3 | page:13 | the Company had $744.2 million of available credit facility capacity |
| E35 | S7 | page:49 | are redeemable at our option, in whole or in part, at specified redemption prices on or after March 15, 2027 |
| E36 | S6 | page:7 | negative technical revisions in proved plus probable reserves |
| E37 | S7 | page:50 | Processing agreements 4,496 |

### Readiness by consumer

| Consumer | Status | Evidence demand and what the pack carries | Limitations carried |
| --- | --- | --- | --- |
| CP-1 financial data | READY_WITH_LIMITATIONS | Statements, notes and tables for Q2 2026 (S6, S7), Q1 2026 (S4, S5), Q3 2025 (S2) and Q4 2025 and FY2025 (S3). Debt at facility level: revolving credit facilities of $750 million maturing June 27, 2030, secured, undrawn at June 30, 2026 with $4.4 million of letters of credit (E9, E10, E17); one note series, 7.375% due March 15, 2032 (E18); the 8.50% notes due April 30, 2030 are in the Q3 2025 note table (E21), and S7 states that the 8.5% Senior Notes were redeemed in Q4 2025 (E20). Covenant table and compliance (E14, E15, E16). Cash interest paid (E30), lease maturity table (S6 page:8), contractual obligations (E37, S7 page:50), liquidity input at December 31, 2025 (E34). | Audited FY2025 statements and notes not retained (G1). Debt terms from summaries only (G2). Perimeter change (G5). Adjusted funds flow appears on two perimeters (G6). Bank EBITDA and net cash are company-defined (G7). Discrete Q4 2025 statements are not retained; only the release (S3). |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business and operating narrative, guidance, shareholder returns and the Eagle Ford sale in S3, S5, S7 (E6, E7); the Gibson infrastructure conveyance and lease (E31); the Canada Revenue Agency matter (E25); retained U.S. liability (E26); the debt repayment and note redemptions of Q4 2025 (E20); hedge roll-off (E29); subsequent events after June 30, 2026 (E27, E28). | No annual information form or governance, ownership or reserves document (G1). No sale agreement or transaction document, so the Eagle Ford terms rest on the release and statement notes (G4). Narrative is management language, to be attributed. |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Consumes upstream registers only; the pack supports the inputs it will need (leverage, liquidity, covenants, cash flow, business drivers). | Inherits every limitation above. No ratings, no market data and no valuation inputs are in the run context (G9); that does not stop this consumer. |
| CP-5 evidence trace validator | READY_WITH_LIMITATIONS | Validates module claims against quotes in the pinned pack; the pack has locatable text for every source. | Inherits the limits above; duplicate coverage between S4 and S5, and S6 and S7, is useful for cross-checks but each cited fact must name its retained source. Upstream modules are sequenced by the planner and are not a source condition. |

### Conflicts and perimeter notes

| ID | Item | Locators | Downstream effect |
| --- | --- | --- | --- |
| K1 | Year-to-date 2026 adjusted funds flow is printed on two perimeters: $405,558 thousand on the consolidated reconciliation (E23) and "$406.6 million" for continuing operations in the discussion (E22). S5 prints a discontinued-operations component for Q1 2026 (E24). Logged as printed; not reconciled here. | E22, E23, E24 | CP-1 must label the perimeter on every adjusted funds flow figure and must not mix the two. |
| K2 | Prior-year comparatives change basis: S2 consolidates U.S. operations; S6 states 2025 comparatives are revised (E33); S3 shows Canada versus Discontinued operations for 2025 in some tables only. | E7, E33, S2 page:6 | CP-1 trend and leverage comparisons across the sale date must name the basis; the Q2 2025 and Q3 2025 columns are not like-for-like. |
| K3 | Covenant ratio text is printed in odd forms: the Total Debt maximum is printed "4:0:1.0" in S2 (E32) but "4.0:1.0" in S4, S5, S6 and S7; the Senior Secured Debt position is printed "0:0:1.0" in S6 (E15). Treated as print or extraction oddities, not as different covenant levels or values; no interpretation is made here. | E15, E32 | CP-1 should quote the printed covenant text and flag the oddity rather than normalise it. |

## Calculations

None. CP-0 performs no financial calculation. The only derived values are source counts: 7 of 7 pinned sources readable as text; 233 retained chunks in total (6 + 19 + 16 + 18 + 67 + 18 + 89, from the chunk counts in the register). No unknown is treated as zero.

## Gaps

| ID | Severity | Gap | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | High | The annual report is a cover document. It names exhibits 99.1 (annual information form), 99.2 (audited financial statements), 99.3 (management discussion) and 99.4 (supplemental oil and gas disclosures) (E1, E2, E3) but none is retained. The year-end release says the audited statements are on the company website (E5). FY2025 annual figures, annual notes and reserves rest on S3 and later comparatives; S6 page:7 gives a Viking impairment reason (E36) but not the annual reserves report. | CP-1, CP-1A, CP-2, CP-5 | Add the annual report exhibits 99.1 to 99.4 from the same filing. |
| G2 | High | No credit agreement, amending agreement or note indenture is retained. The statements say the credit facility agreements are on SEDAR+ and EDGAR (E19) and give only summary covenant terms (E14 to E16) and note terms (E18, E35). Guarantors, security package, restricted-payment baskets, definitions and change-of-control terms are Not supplied. Search of all sources for guarantor, indenture and rating terms found no such disclosure. | CP-1, CP-2 | Add the credit facility agreement with amendments and the 7.375% note indenture. |
| G3 | Medium | Debt-issuer identity: the sources name only Baytex Energy Corp. as the reporting entity; the issuer, co-issuers and guarantors of the 7.375% notes and the borrowers under the Credit Facilities are not stated. Baytex Energy USA, Inc. appears only as agent for service (E4). The context lists no borrower, parent or guarantors. Unresolved; no perimeter is assumed. | CP-1, CP-1A, CP-2 | Resolve from the indenture and credit agreement (G2). |
| G4 | Medium | No transaction document for the Eagle Ford sale of December 19, 2025 (E6); terms, closing adjustments and retained indemnities rest on the release and notes, and the retained U.S. liability is stated without amount (E26). The statements show later post-closing adjustments only as net after-tax amounts (S6 page:7). | CP-1A, CP-2 | Add the sale agreement or its summary from the annual information form (G1). |
| G5 | Medium | Perimeter change: Eagle Ford is classified as discontinued operations (E7) and one operating segment remains (E8). Pre-2026 comparatives mix consolidated, Canada and discontinued bases (K2). | CP-1, CP-2, CP-5 | Label basis on each figure; use S6 and S7 revised comparatives where available. |
| G6 | Medium | Adjusted funds flow perimeter differs between sentences (K1). | CP-1, CP-5 | Cite statement-level source with its perimeter. |
| G7 | Medium | Net cash, net debt, Bank EBITDA and free cash flow are company-defined measures; Bank EBITDA is given as one trailing-twelve-month amount per covenant date (E13) and its build-up is not supplied. Bank EBITDA at December 31, 2025 sits in the missing audited statements. | CP-1, CP-2 | Treat as management-defined; add the credit agreement definitions (G2). |
| G8 | Medium | Recency: the latest pinned document is the second quarter 2026 results exhibit (S7); the third quarter 2026 period (ended September 30, 2026) is not in the pack. The sources do not show whether later reports were published before the 2026-11-05 cutoff, and no text after August 2026 is supplied. Subsequent events after June 30, 2026 are limited to those printed (E27, E28). | CP-1, CP-1A, CP-2 | Check for any later furnished report up to the cutoff and add it if filed. |
| G9 | Low | Run context holds no ratings, quotes, market data, valuation peers, deal terms or user assumptions. Not supplied; not zero. No investor presentation is in the pack (the quarterly documents are releases, management discussion and statements). Image or chart content was not inspected. | CP-1A, CP-2 | Add rating and market inputs if the committee needs them. |
| G10 | Low | The Canada Revenue Agency tax matter is described with assessed amounts (E25), and the amounts owing depend on which taxpayer is liable and on tax shelter available; no external legal opinion or audited tax note is retained. | CP-1, CP-1A, CP-2 | Add the annual tax note (G1). |

## Next module

Proceed to CP-1 (financial data). Nothing here makes any consumer CONDITIONAL or BLOCKED. Use S6 for Q2 2026 statement facts, S7 for management discussion, releases and covenant narrative, S4 and S5 for Q1 2026, S2 for Q3 2025 (consolidated, pre-sale basis) and S3 for Q4 2025 and FY2025. Carry forward gaps G1 to G10 and the perimeter notes K1 to K3. Do not state guarantors, security, call schedule beyond the printed text, or audited FY2025 amounts as verified facts. Next evidence action: add the annual report exhibits and the debt agreements, and check for any report filed after August 5, 2026 and before the cutoff.
