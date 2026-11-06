# CP-0 — Source readiness: NCL CORP Ltd. (ncl-corp-ltd)

## Request

- Issuer: NCL CORP Ltd. (issuer id `ncl-corp-ltd`; the filings name the registrant NCL Corporation Ltd., "NCLC"), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026 (quarter and nine months ended September 30, 2026); prior period FY2025 (context).
- Run: `ncl-corp-ltd-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned page text of the sources and wrote this answer. No provider was called.
- Question: can the supplied filings and earnings releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles or calculates no figure.
- Locators are `page:N` of the pinned `.jsonl` text of each source, not printed page numbers. Quoted text is copied from the cited page.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_nclc-20251231x10k.htm.jsonl | 1590d4030e80abfbd09d00a74521526f72070052531a8716f865a880a8fa9501 | Annual report on Form 10-K for the fiscal year ended December 31, 2025 (169 pages) |
| 10-Q_2026-03-31_nclc-20260331x10q.htm.jsonl | 1693fea3f52de137a2e148c9e6f9853be5398eb34944625b7e837b2bd396c943 | Quarterly report on Form 10-Q for the quarter ended March 31, 2026 (43 pages) |
| 10-Q_2026-06-30_nclc-20260630x10q.htm.jsonl | 2f18ccd1a947471efb9474a7bd377c5db5871d9445b97fe0a1fc7e783f6d645f | Quarterly report on Form 10-Q for the quarter ended June 30, 2026 (47 pages) |
| 10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl | 7769d1c310cec4c8e024523931f2cd599a487768128283054dca38ddd11d7d93 | Quarterly report on Form 10-Q for the quarter ended September 30, 2026 (51 pages) |
| EX-99.1_2026-05-04_exh_991.htm.jsonl | 19e48d4c7cb2b40fb1bcbfbbe436e7e39f669c8965c4e705c327d948db3f04d8 | Exhibit 99.1 press release for the first quarter of 2026, issued by the parent NCLH (17 pages) |
| EX-99.1_2026-07-30_exh_991.htm.jsonl | ffe75efbccd58bfc3c88fabf4a188883f7003d5a095dba1da47bbe08c4d94307 | Exhibit 99.1 press release for the second quarter of 2026, issued by the parent NCLH (19 pages) |
| EX-99.1_2026-10-29_exh_991.htm.jsonl | 6f93f8906074ef388d05f277a1b3874ed298e830f3945372d3d73a8925dc791c | Exhibit 99.1 press release for the third quarter of 2026, issued by the parent NCLH (18 pages) |
| context | 1eac4b587c5c6cd9d96c3f400eed0e70dc9aa1137a14c30469dde7d21791294f | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module, so no upstream handoff exists.

The pack also holds `_retrieval.json`, which the launcher ignores. It is not a source here.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The three quarterly reports and the annual report are filed by the issuer itself and can support all four selected modules. The three earnings releases describe the parent group, not the issuer, and must be labelled that way. | Medium | No credit agreement, indenture or covenant ratio values are supplied, and the releases use a different entity perimeter. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The issuer files its own statements, debt tables, maturity schedule and liquidity text in the annual report and each quarterly report. | Debt, liquidity and earnings work can be traced to the issuer's own filed statements. | Medium |
| The earnings releases report the parent group, whose cash, net income and debt differ from the issuer's. | Leverage and liquidity quoted from releases cannot be used as the issuer's figures. | High |
| October 2026 notes, a larger revolver and a covenant-definition amendment came after quarter-end and are described only in summary. | Post-quarter liquidity and covenant headroom cannot be verified without the amendment text. | Low |
| Covenant types are named, but covenant ratio values and governing definitions are not supplied. | Headroom against the maintenance tests cannot be verified. | Low |

### Readiness view

Every selected consumer can proceed on the supplied sources with bounded limitations; none is conditional or blocked. The annual report and the three quarterly reports are original authority and are filed by the issuing entity itself, which is a voluntary filer. The three press releases are management-prepared support and cover the listed parent, Norwegian Cruise Line Holdings Ltd., so they cannot stand in for the issuer's statements. The recurring limits are that the governing debt documents and the covenant definitions are not supplied, that the October 2026 financing is described only in the third-quarter report, and that nothing dated after October 29, 2026 is supplied.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025 statements (10-K page:121 to page:123) and unaudited statements for the three 2026 periods are located, with comparatives, an EBITDA reconciliation and a single-segment note. Limit: releases are parent-level, and the adjusted EBITDA the releases quote is not the issuer's reported line. |
| CP-1A | READY_WITH_LIMITATIONS | Business, brands, fleet and newbuild orders, ownership by the parent, and the 2026 ship sales and charters are located. Limit: no governing agreements, no parent-level governance papers, and the guarantor roster is not listed. |
| CP-2 | READY_WITH_LIMITATIONS | Instrument-level debt table, maturities, exchangeable note terms, revolver terms, ratings and liquidity text are located. Limit: no executed credit agreement or indenture; covenant ratio values and definitions are not printed; the October 2026 amendment is summarized only. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has stable page locators, so claims can be traced. Limit: the text extraction was not compared with the filed HTML or XBRL, and no image or chart was inspected. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### Form 10-K for FY2025 (`10-K_2025-12-31_nclc-20251231x10k.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited consolidated statements. Cover at page:1: “For the fiscal year ended December 31, 2025” (10-K, page:1). The registrant is a voluntary filer: “(Note: The registrant is a voluntary filer of reports required to be filed under Section 13 or 15 (d) of the Securities Exchange Act of 1934).” (Q3 10-Q, page:1).
- Audit: the index lists “Report of Independent Registered Public Accounting Firm (PCAOB ID 238)” (10-K, page:118); the report is signed “/s/ PricewaterhouseCoopers LLP” and dated March 2, 2026 (10-K, page:121).
- Statements: operations at page:121, balance sheet at page:122, cash flows at page:123. Notes follow. Long-term debt note (Note 9) at page:139 to page:142; debt covenants at page:150 to page:151; fair value of debt at page:155; commitments and contingencies (Note 13) at page:164 to page:165; leases (Note 6) at page:136.
- MD&A: Item 7 starts at page:71; the EBITDA and Adjusted EBITDA reconciliation is at page:83; liquidity at page:84; funding sources and collateral at page:90; market risk at page:91.
- Risk factors on covenants and the rating-sensitive financing are at page:41 and page:42.
- Exhibits: the credit agreements, indentures and newbuild loan agreements are listed at page:96 to page:114 as exhibits; their texts are not in the pack.
- Units: dollars in thousands in the statements (10-K, page:121). USD.
- Perimeter: NCL Corporation Ltd. and subsidiaries; the parent NCLH is a separate registrant.

#### Form 10-Q for Q1 2026 (`10-Q_2026-03-31_nclc-20260331x10q.htm.jsonl`)

- Family and authority: filed quarterly report, unaudited, for the three months ended March 31, 2026 (Q1 10-Q, page:2 for the statement of operations). Balance sheet at page:2, cash flows at page:3, debt note at page:9 to page:10, fair value of debt at page:14.
- MD&A: EBITDA and Adjusted EBITDA reconciliation at page:30; liquidity and capital resources at page:31; funding sources and covenants at page:35; ratings at page:32.
- The report carries no subsequent event note (searched for “Subsequent Event”; no occurrence).

#### Form 10-Q for Q2 2026 (`10-Q_2026-06-30_nclc-20260630x10q.htm.jsonl`)

- Family and authority: filed quarterly report, unaudited, for the quarter and six months ended June 30, 2026. Statements from page:2, cash flows at page:3, debt note at page:10 to page:11, subsequent event note at page:21 to page:22 (sale of Oceania Sirena).
- MD&A: EBITDA reconciliation at page:33; liquidity at page:35; covenant and funding text at page:39 to page:40.

#### Form 10-Q for Q3 2026 (`10-Q_2026-09-30_nclc-20260930x10q.htm.jsonl`)

- Family and authority: filed quarterly report, unaudited; the latest filing and the controlling source for the current period. Cover at page:1: “For the quarterly period ended September 30, 2026” (Q3 10-Q, page:1). The same cover states “There were 31,164,004 ordinary shares outstanding as of October 22, 2026.”
- Statements: operations and comprehensive income at page:2 to page:3, balance sheet at page:2 to page:3, cash flows at page:3 to page:4. Note 1 at page:5; liquidity policy text at page:6; segment note at page:6 to page:7; revenue note at page:9; leases at page:10; long-term debt (Note 7) at page:11 to page:13, including the exchangeable note table and the scheduled repayments at page:12; subsequent event (Note 13) at page:24.
- MD&A: Adjusted EBITDA reconciliation at page:36; liquidity at page:38; funding sources, covenants and ratings at page:39 to page:42; Part II legal proceedings at page:46; exhibits at page:50.
- Units: dollars in thousands in the statements (“(in thousands)” on page:2). USD. Unaudited interim.

#### Earnings releases (three Exhibit 99.1 files)

- Family and authority: press releases furnished as Exhibit 99.1, management-prepared and unaudited. They give attributed management figures and non-GAAP measures; they do not override the filings.
- Perimeter: each release is issued by the parent and reports the parent's consolidated statements: “NORWEGIAN CRUISE LINE HOLDINGS LTD.” heads the statements (Q3 release, page:13) and the balance sheet (Q3 release, page:14).
- Q3 release (`EX-99.1_2026-10-29_exh_991.htm.jsonl`): highlights and guidance at page:1 to page:4; liquidity and net leverage at page:3; terminology at page:6 to page:7; statements at page:13 to page:14; net debt table at page:18.
- Q2 release (`EX-99.1_2026-07-30_exh_991.htm.jsonl`): highlights at page:1; liquidity at page:3; statements at page:14 to page:15; net debt table at page:19.
- Q1 release (`EX-99.1_2026-05-04_exh_991.htm.jsonl`): highlights at page:1; liquidity at page:3; statements at page:13 to page:14; net debt table at page:17.
- Net Debt and Net Leverage are company non-GAAP measures defined only in the releases: “Net Debt. Long-term debt, including current portion, less cash and cash equivalents.” (Q3 release, page:7). The Q3 10-Q does not use the term Net Leverage (searched; no occurrence).

### Information-availability boundary

- Every source is dated on or before the cutoff. The latest are the Q3 10-Q and the Q3 release, filed October 29, 2026 per the retrieval record.
- Between October 29, 2026 and the as-of date 2026-11-05 nothing is supplied. Events in that window are Not supplied, not absent.
- The October 2026 notes issue, the revolver third amendment and the Oceania Insignia memorandum of agreement are subsequent events to the quarter end but fall before the cutoff and are described in the Q3 10-Q (page:11, page:12, page:24).

### Identity and perimeter

- Registrant and reporting entity: NCL Corporation Ltd., Bermuda, Commission File Number 333-128780 (Q3 10-Q, page:1). The context leaves borrower, parent and guarantor fields blank; blank is not evidence of absence.
- Parent: “NCLH” is defined as Norwegian Cruise Line Holdings Ltd.; the Q3 10-Q defines “NCLC” as NCL Corporation Ltd. and “NCLH” as Norwegian Cruise Line Holdings Ltd., and uses “the Company” for NCLC and its subsidiaries (Q3 10-Q, page:5). The 10-K states “NCLH owns all the” issuer's ordinary shares (10-K, page:71).
- Intercompany: the balance sheet carries a current line “Due to NCLH” (Q3 10-Q, page:3), and the 2025 equity statement shows “Contribution from NCLH” (Q3 10-Q, page:5).
- Debt roles: NCLC is borrower under the Revolving Loan Facility with subsidiary guarantors: “among NCLC, as borrower, the subsidiary guarantors party thereto and JPMorgan Chase Bank, N.A., as administrative agent and collateral agent” (Q3 10-Q, page:29; same wording in 10-K, page:4). The subsidiary guarantors are not named in the supplied text.
- Exchangeable notes: NCLC is issuer and NCLH is guarantor: “pursuant to an indenture among NCLC, as issuer, NCLH, as guarantor, and U.S. Bank National Association, as trustee” (Q3 10-Q, page:27; same wording in 10-K, page:3).
- Newbuild loans: the 10-K exhibit list shows NCLC as guarantor of ship-owning borrower subsidiaries (10-K, page:98). The guarantor structure of each senior note series is not described in the debt table pages read.
- Ratings: “Our Moody’s long-term issuer rating is B1, and our senior unsecured rating is B3.” (Q3 10-Q, page:39).

### Perimeter conflicts between filings and releases

- Cash at September 30, 2026: the issuer's balance sheet shows cash and cash equivalents of $250,722 thousand (Q3 10-Q, page:2), while the parent's release shows cash and cash equivalents of $256,508 thousand (Q3 release, page:14). Effect: the two cannot be mixed in one liquidity computation.
- Net income for the quarter: the issuer reports quarterly net income of $631,918 thousand (Q3 10-Q, page:2) while the release states “GAAP net income was $491 million” (Q3 release, page:1). Effect: earnings from the release are parent-level.
- Debt: the release reports “total debt of $15.1 billion and Net Debt of $14.8 billion. Net Leverage ended the quarter at 5.5x.” (Q3 release, page:3). The issuer's balance sheet shows its own long-term debt, current portion and exchangeable note lines (Q3 10-Q, page:3). The two sets of totals are different presentations on different perimeters and are not reconciled in the supplied text; the difference is carried to CP-1 and CP-2 as a gap.
- Liquidity: the issuer reports “As of September 30, 2026, we had liquidity of approximately $1.4 billion, including cash and cash equivalents of $250.7 million and $1.1 billion available under our Revolving Loan Facility.” (Q3 10-Q, page:6). The release adds a pro forma figure that includes the October 2026 financing: “liquidity as of September 30, 2026 would have been $2.1 billion” (Q3 release, page:3). The pro forma figure is parent-level, pro forma and management-prepared.
- Earlier quarters follow the same pattern: the issuer reports “cash and cash equivalents of $179.2 million” at March 31, 2026 (Q1 10-Q, page:5) against “approximately $185.0 million of cash and cash equivalents” in the release (Q1 release, page:3); and “cash and cash equivalents of $212.3 million” at June 30, 2026 (Q2 10-Q, page:5) against “approximately $218 million of cash and cash equivalents” in the release (Q2 release, page:3).
- Adjusted EBITDA: the issuer prints its own reconciliation (Q3 10-Q, page:36); the release headline adjusted EBITDA is the parent's. The two are not interchangeable.

### Version relationships and conflicts

- Each 10-Q is a separate period report; the Q3 10-Q does not restate the Q1 or Q2 reports. The 10-Q controls for statement facts; the release is supporting and is parent-level.
- The 10-K debt table (Note 9) and the 10-Q debt notes present different dates. The Q3 10-Q repeats the exchangeable note table at both September 30, 2026 and December 31, 2025 (Q3 10-Q, page:12); the instrument-by-instrument table for the full debt stack is in the 10-K (10-K, page:139 to page:140) and the 10-Qs carry summary lines. Full instrument-level debt at September 30, 2026 is therefore not printed by instrument in the supplied quarterly reports read; scheduled repayments by year are (Q3 10-Q, page:12).
- Naming: the context names the issuer NCL CORP Ltd.; the filings name NCL Corporation Ltd. This is one entity (same Commission File Number on 10-K and Q3 10-Q, page:1).
- No draft, unsigned or superseded source is in the pack.

### Consumer evidence demand

#### CP-1 (financial extraction)

- Located: FY2025 annual statements and FY2024 comparatives (10-K, page:121 to page:123); the three 2026 interim periods with prior-year comparatives; segment reporting (single segment, 10-K page:128; adjusted operating income table, Q3 10-Q page:6); EBITDA reconciliation (Q3 10-Q, page:36); cash flow supplemental information (Q3 10-Q, page:24).
- Limits: the sources print annual and year-to-date figures; a discrete fourth quarter of 2025 is not located and would have to be derived by the consumer and labelled as derived. Units are thousands in statements and millions or billions in prose and releases.

#### CP-1A (business and transaction context)

- Located: business description and history (10-K, page:8 onward), fleet and newbuild program (Q3 10-Q, page:5), ship disposals and charters (Q3 10-Q, page:10 and page:24; Q3 release, page:1), parent ownership (10-K, page:71).
- Limits: no governance or sponsor papers; parent-level strategy text appears in the releases only.

#### CP-2 (fundamental credit synthesis)

- Located: instrument-level debt (10-K, page:139 to page:140), October 2026 refinancing (Q3 10-Q, page:11 to page:12), scheduled principal repayments (Q3 10-Q, page:12), liquidity (Q3 10-Q, page:6 and page:38), covenants named (10-K, page:41; Q3 10-Q, page:42), ratings (Q3 10-Q, page:39), operating lease balances (Q3 10-Q, page:10), advance ticket sales (Q3 10-Q, page:3).
- Limits: see Gaps.

#### CP-5 (evidence trace validation)

- Located: all claims can be cited to a `page:N`. Limit: parent-level release figures must be kept apart from issuer filing figures when traced.

## Calculations

No new calculation is made. CP-0 does not normalize, reconcile or calculate figures. Figures above are quoted as printed and are not combined.

Coverage counts (pages in each retained extraction): 10-K 169; Q1 10-Q 43; Q2 10-Q 47; Q3 10-Q 51; Q1 release 17; Q2 release 19; Q3 release 18. The host read the pages named in the register and located searches across every source; it did not read every page line by line, so page coverage is by located content, not by full-page review.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed revolver credit agreement and its amendments (including the October 2026 third amendment), the indentures and the newbuild loan agreements are not supplied; the 10-K exhibit list names them as previously filed. | Medium | CP-2, CP-5 | Obtain the agreements from EDGAR exhibits before any covenant or priority analysis. |
| Covenant ratio values and definitions are not printed. The filings name a minimum liquidity test, a net funded debt to capitalization ratio and a loan to value ratio, and state compliance only. The third amendment “modified certain existing financial covenant definitions” (Q3 10-Q, page:12). | High | CP-2, CP-5 | Obtain the credit agreement and compliance certificate; until then headroom is Not calculable. |
| Press releases are parent-level (NCLH) and differ from issuer figures on cash, net income, debt and liquidity. | High | CP-1, CP-2, CP-5 | Use the issuer's 10-K and 10-Q figures; label any release figure as parent-level. |
| Total debt per the parent release and the issuer balance sheet are not reconciled in the supplied text. | Medium | CP-1, CP-2 | Carry both with perimeter labels; do not mix them. |
| Instrument-by-instrument debt at September 30, 2026 is not printed in the quarterly reports read; the full instrument table is at December 31, 2025 only. | Medium | CP-2 | Rebuild from the 10-K table plus the described 2026 events; flag as derived. |
| Subsidiary guarantor names and the guarantor structure by note series are not supplied. | Medium | CP-2 | Obtain Exhibit 22 or the indentures if filed. |
| Events between October 29, 2026 and 2026-11-05 are not supplied. | Low | All | State as Not supplied. |
| The text extraction was not compared with the filed HTML or XBRL; tables are flattened across lines, so figures must be read against column headers. | Low | CP-1, CP-5 | Re-check key figures against the filed HTML when a number drives a conclusion. |
| Parent-level governance, ownership and strategy documents are not supplied beyond the releases. | Low | CP-1A | Treat parent strategy statements as attributed management claims. |

## Next module

CP-1 should run next on the issuer's own statements (10-K and three 10-Qs), using the releases only as labelled parent-level support. Carry forward these limits: the release-versus-filing perimeter conflict, the missing covenant values and agreements, the absence of an instrument-level debt table at September 30, 2026, and the October 2026 financing treated as a subsequent event rather than a quarter-end balance.
