# CP-0 source readiness: CHS INC (chscp)

## Request

CHS INC (issuer id chscp; Nasdaq-listed cumulative redeemable preferred stock CHSCP, CHSCO, CHSCN, CHSCM and CHSCL) is assessed as of 2026-11-05 on the credit_snapshot pathway. The question is whether the seven pinned filings and releases can support the requested downstream modules CP-1, CP-1A, CP-2 and CP-5, and what remains blocked. This is a source-readiness handoff: it gives no credit conclusion, no legal interpretation and no new figures. Reporting currency is USD; the 10-K and 10-Qs state amounts in USD thousands, the releases state USD millions or billions in prose and USD thousands in tables. The current period is fiscal 2026 (year ended 2026-08-31) and the prior period is fiscal 2025, as named in the run context.

## Sources

### Issuer sources relied on

| Source name | sha256 | Document family and authority | Period or date shown in the text | Pages in extraction |
| --- | --- | --- | --- | --- |
| 10-K_2026-08-31_chscp-20260831.htm.jsonl | 7af90f68bff1cc427159bcc12ffc87c427ce829f2621b0c4238922f45880492c | Annual report on Form 10-K, audited consolidated statements; controls its facts | Fiscal year ended 2026-08-31 with comparatives for 2025 and 2024; auditor report dated November 4, 2026 | 193 |
| 10-Q_2025-11-30_chscp-20251130.htm.jsonl | 3b343d46b4f667e29be99b08f7d799dc25471f06dbcbf91d62c596b40053bc50 | Quarterly report on Form 10-Q, unaudited | Quarter ended 2025-11-30 (fiscal Q1 2026) | 44 |
| 10-Q_2026-02-28_chscp-20260228.htm.jsonl | 335ab8ab1983479e957ab5bcc688bac42f2a8847cb6800ad1d72a83671457084 | Quarterly report on Form 10-Q, unaudited | Quarter ended 2026-02-28 (fiscal Q2 2026) and six months | 49 |
| 10-Q_2026-05-31_chscp-20260531.htm.jsonl | d9720f91bf0c93fa122637a031df8f3b728863173bc1b8717d0a6e377caf2082 | Quarterly report on Form 10-Q, unaudited | Quarter ended 2026-05-31 (fiscal Q3 2026) and nine months | 50 |
| EX-99.1_2026-04-08_a2qfy26earningrelease.htm.jsonl | 33496a1570da087ac1976522b03589f92cee4a9a2670952160166094e3791034 | Earnings release (Exhibit 99.1), management claims | Second quarter fiscal 2026, release dated April 8, 2026 | 4 |
| EX-99.1_2026-07-08_a3qfy26earningrelease.htm.jsonl | 9732954cd83cfd2faab08d34c8a937435e86ab588c7e99ee653b9179d1961e0c | Earnings release (Exhibit 99.1), management claims | Third quarter fiscal 2026, release dated July 8, 2026 | 4 |
| EX-99.1_2026-11-04_a4qfy26earningrelease.htm.jsonl | cae53d4e6b095242a55a168a21c6d1a5d0c45880ba1e0b3a388701114a691f44 | Earnings release (Exhibit 99.1), management claims | Fiscal year 2026, release dated November 4, 2026 | 5 |

Context file: context sha256 7441cd131643680d7cdd1713c448cca9698ae339b2ccfb6c0e8da281781f9451 holds the user's settings (as-of and cutoff 2026-11-05, current period fy-2026, prior period fy-2025, USD, legal_documents none, no ratings, quotes, peers or deal terms). It is not issuer evidence and is not used as such. The file _retrieval.json in the pack folder is ignored by CP-OS and none of its content is relied on.

### Supplied handoffs

None. CP-0 is the first module in this run and the request carries no upstream handoffs (the handoffs object is empty).

### Extraction note

Each extracted file starts with a line "Visible text of ..., sha256 ..." giving the hash of the original HTML. That hash differs from the pinned hash of the extracted text file listed above, for example the fiscal 2026 release names fcebbd07671b195d579c1a4780a29ef729a2537c5fe7c7c13ad768bedab3fe50 in its first line but is pinned at cae53d4e6b095242a55a168a21c6d1a5d0c45880ba1e0b3a388701114a691f44. This is two different objects (original HTML and its text conversion), not a conflict. Later modules cite the pinned hashes and the page number of the extracted chunk (page:N), which is not the printed page number of the filing.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filed statements and releases are enough to proceed with the financial base, business, credit and evidence-trace modules for this cooperative issuer, but not to test covenants or read legal terms. | Medium | No credit agreements, note purchase agreements, ratings or EBITDA measure are supplied, so covenant levels and headroom cannot be assessed from the sources. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited fiscal 2026 statements with two prior years, three quarterly reports and three releases are present and agree where checked. | Statement-based debt, liquidity and earnings work can rest on filed documents. | High |
| Debt is described only in the notes: private placement notes, a term loan and short-term facilities, with covenant levels unstated. | Covenant headroom and legal ranking cannot be established until the agreements are supplied. | Medium |
| The latest release and the annual report differ on equity redemptions planned for fiscal 2027. | Fiscal 2027 cash returns to owners need the filing figure, not the headline. | Medium |
| No discrete fourth-quarter statements or adjusted EBITDA are reported. | Quarterly trend and leverage measures must be derived downstream with stated limits. | Medium |

### Readiness view

The effective source set supports the requested work with limitations. CHS Inc. is a Minnesota agricultural cooperative whose only registered securities are five series of listed preferred stock; its borrowing is private placement notes, bank term loans and short-term facilities described in the notes to the audited statements. The annual report for fiscal 2026, three quarterly reports and three earnings releases give audited and unaudited statements, a debt table, a maturity schedule, segment tables and a statement that covenants were met. What is absent is the legal and market layer: the agreements that carry the covenants, any rating, any trading quote and any EBITDA reconciliation. The binding consequence is that financial, business and evidence-trace work can proceed on filed documents, while covenant testing and instrument-level legal analysis cannot proceed from these sources and need a further evidence action.

### Source assessment

| Source | Entity and perimeter | Period and basis | Located evidence (exact quote) | Locator |
| --- | --- | --- | --- | --- |
| 10-K | CHS Inc. and subsidiaries, consolidated; the registrant has no common stock | Fiscal year ended 2026-08-31, audited, USD thousands | "The Registrant has no common stock outstanding." | 10-K page:2 |
| 10-K | Consolidated balance sheet and income statement | Years ended 2026-08-31 and 2025-08-31 | "Total assets $ 20,112,875 $ 18,863,849" | 10-K page:144 |
| 10-K | Consolidated cash flow including cash paid for interest | Years ended 2026-08-31, 2025 and 2024 | "Cash paid for interest $ 167,057 $ 147,583 $ 100,542" | 10-K page:146 |
| 10-K | Debt note, issuer CHS Inc. | Balances at 2026-08-31 and 2025-08-31 | "Total long-term debt 2,052,723 1,835,833" | 10-K page:165 |
| 10-K | Maturity schedule excluding finance leases | Fiscal years from 2027 | "Thereafter 1,105,000" | 10-K page:165 |
| 10-K | Segment note with three reportable segments and Corporate and Services | Fiscal 2026, 2025 and 2024 recast | "Income before income taxes $ 554,590 $ 127,378 $ 354,640 $ 1,036,608 $ 92,111 $ — $ 1,128,719" | 10-K page:181 |
| 10-Q Q1 | CHS Inc. and subsidiaries, condensed consolidated, unaudited | Three months ended 2025-11-30 | "Effective September 1, 2025, we changed our segment reporting to align with our new product-line operating model" | 10-Q Q1 page:6 |
| 10-Q Q2 | Same perimeter | Three and six months ended 2026-02-28 | "(Loss) income before income taxes (164,977) (84,712) 107,211 174,125" | 10-Q Q2 page:5 |
| 10-Q Q3 | Same perimeter | Three and nine months ended 2026-05-31 | "Income before income taxes 282,213 258,855 389,424 432,980" | 10-Q Q3 page:5 |
| Release Q2 | CHS Inc. consolidated and segments, management narrative | Three and six months ended 2026-02-28 | "(Loss) income before income taxes (164,977) (84,712) 107,211 174,125" | Release Q2 page:2 |
| Release Q3 | Same | Three and nine months ended 2026-05-31 | "Income before income taxes 282,213 258,855 389,424 432,980" | Release Q3 page:2 |
| Release FY | Same | Year ended 2026-08-31 | "Income before income taxes 1,128,719 614,772" | Release FY page:2 |

Cross-document checks that agree: fiscal 2026 income before income taxes of 1,128,719 appears in the 10-K statement of operations (page:144), the 10-K segment table (page:181) and the fiscal year release (page:2); nine-month income before income taxes of 389,424 appears in the third quarter 10-Q (page:5) and the third quarter release (page:2); six-month 107,211 appears in the second quarter 10-Q (page:5) and release (page:2).

### Consumer assessment

| Consumer | Status | Evidence located | Bounded gaps carried |
| --- | --- | --- | --- |
| CP-1 financial base | READY_WITH_LIMITATIONS | Statements, cash flow, segment tables and three fiscal quarters of 10-Q data (10-K page:144, page:146, page:181; 10-Q Q3 page:5) | No discrete fourth-quarter statements, no adjusted EBITDA, segment recast, nine-month versus full-year labelling |
| CP-1A business and transaction | READY_WITH_LIMITATIONS | Business description, segments, joint ventures, announced projects (10-K page:4, page:76; Release FY page:2) | Announced facilities are proposed and subject to approvals; no transaction terms or financing documents |
| CP-2 credit view | READY_WITH_LIMITATIONS | Debt table, maturities, liquidity table, covenant compliance statement (10-K page:74, page:76, page:163, page:165) | Covenant levels, ratings, quotes and letters of credit not supplied |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | Located page chunks for every statement and note used | Text extraction only, no image or chart inspection, printed page differs from chunk page |

The assertion for any later model objective is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This handoff does not assert normalized quarters, reconciliation or downstream input acceptance.

### Coverage by profile

| Profile | What is retained | Quote supporting it | Locator |
| --- | --- | --- | --- |
| Financial statements and notes | Balance sheet, operations, comprehensive income, equities, cash flows, notes 1 to 19 | "Note 9 Notes Payable and Long-Term Debt" | 10-K page:163 |
| Debt and liquidity | Notes payable table, committed revolver, securitization and repurchase facilities, term loan, long-term debt table and maturity schedule | "The credit facility provides a committed amount of $2.8 billion that expires on April 21, 2028." | 10-K page:163 |
| Facility extension before year end | Securitization and repurchase facilities extension | "On August 26, 2026, we amended both the Securitization and Repurchase Facilities to extend the terms of the facilities to August 25, 2027." | 10-K page:164 |
| Revolving term loan | Revolving period and reversion date | "On October 29, 2026, the total funded loan balance outstanding reverts to a nonrevolving term loan that is payable on October 29, 2029." | 10-K page:165 |
| Covenants | Statement only, no levels | "We were in compliance with our debt covenants as of August 31, 2026." | 10-K page:163 |
| Guarantees and commitments | Guarantees of nonconsolidated companies, credit commitments, purchase obligations | "Our bank covenants allow maximum guarantees of $1.1 billion, of which $110.4 million were outstanding as of August 31, 2026." | 10-K page:190 |
| Contractual obligations | Debt, interest, leases and purchase obligations by period | "Purchase obligations (3) 6,500,640 1,103,551 7,604,191" | 10-K page:77 |
| Preferred stock | Five listed series with redemption values and rates | "Class B Reset Rate Cumulative Redeemable, Series 2 CHSCN" | 10-K page:170 |
| Equity returns to owners | Patronage and redemption estimates for fiscal 2027 | "Total patronage distributions for fiscal 2026, to be paid in fiscal 2027, are estimated to be $486.3 million" | 10-K page:169 |
| Segment and seasonality | Segment definitions, Corporate and Services, seasonality | "Our revenues and IBIT generally trend lower during the second fiscal quarter and increase in the third fiscal quarter." | 10-K page:179 |
| Earnings release content | Reported figures and attributed narrative | "Consolidated revenues of $39.2 billion for fiscal year 2026 compared to $35.5 billion for fiscal year 2025" | Release FY page:1 |
| Exhibit index for governing agreements | Credit agreements and note purchase agreements listed, incorporated by reference | "Credit Agreement (5-Year Revolving Loan), dated as of April 21, 2023, by and between CHS Inc., CoBank, ACB" | 10-K page:133 |

### Conflicts and discrepancies between sources

| Item | Statement A | Statement B | Downstream effect |
| --- | --- | --- | --- |
| Fiscal 2027 equity redemptions | Release FY: "$150 million in cash patronage and up to $150 million in equity redemptions" (Release FY page:1) | 10-K: "the Board of Directors authorized an additional $15.0 million of redemptions" (10-K page:170) and the equity statement line "Estimated 2026 equity redemptions (1) (165,000)" (10-K page:145) | The filing, which controls, carries more redemptions than the release headline; cash return sizing in CP-2 must use the filing and state the difference |
| Quarter label in second quarter release | Release Q2: "Energy reported a pretax loss of $133.6 million for the first quarter of fiscal year 2026" (Release Q2 page:1) | Release Q2 table "Three Months Ended February 28" (Release Q2 page:2) and 10-Q Q2 segment table "Loss before income taxes $ (133,642) $ (17,936) $ (11,492) $ (163,070) $ (1,907) $ — $ (164,977)" (10-Q Q2 page:21) | The release sentence mislabels the quarter; the 10-Q controls and the figure is second quarter fiscal 2026 |
| Capital expenditure totals | 10-K MD&A: "capital expenditures of $463.3 million in fiscal 2026" (10-K page:76) | 10-K segment note total "$ 531,517" with footnote "Includes amounts related to acquisition of property, plant and equipment and expenditures for major maintenance." (10-K page:181) | The two totals use different definitions; CP-1 must state which it uses |
| Revolver drawn balance | 10-Q Q3: "There were $190.0 million and $180.0 million in borrowings outstanding on this facility as of May 31, 2026, and August 31, 2025." (10-Q Q3 page:12) | 10-K: "There were no borrowings outstanding on this facility as of August 31, 2026" (10-K page:163) | Different dates, not a conflict; it shows intra-year swing in short-term borrowing that quarter-end figures hide |

## Calculations

No new calculation is made in this module, by design of the source-readiness method. The only counts used are extraction page counts: 193, 44, 49, 50, 4, 4 and 5 pages for the seven sources in the order of the sources table, which is 349 pages in all. These counts describe the extraction, not review depth: key statements, notes and tables were located and opened by search, and pages of Part III (directors, executive compensation, ownership) and the full risk factor text were not read for this handoff because they carry no figure the requested modules need. Coverage is therefore evidenced for the pages cited above and not claimed for every one of the 349 pages.

Figures quoted above are copied as printed. Where two sources print the same number the match is a locator check, not a reconciliation.

## Gaps

| Gap | Severity | Affected consumers | Remediation | Evidence of absence |
| --- | --- | --- | --- | --- |
| Credit agreements, note purchase agreements and amendments not supplied; the 10-K exhibit index lists them as incorporated by reference | High | CP-2, CP-5 | Obtain the revolving, term loan and note purchase agreements named in the exhibit index | Context states legal_documents none; 10-K page:133 lists the agreements |
| Covenant levels and the reported covenant figures not printed | High | CP-2 | Obtain covenant definitions from the agreements | 10-K page:163 says "minimum consolidated net worth and other financial ratios" without levels |
| Letters of credit drawn on facilities, factoring and supply chain finance: searched for letters of credit, standby, factoring and supply chain financing in all seven sources and found no occurrence | Medium | CP-2 | Obtain facility utilization detail; liquidity net of letters of credit is not calculable from these sources | No match in any source text |
| No adjusted EBITDA or EBITDA reconciliation in any source | Medium | CP-1, CP-2 | Downstream modules construct a labelled measure from statement lines, or obtain management bridge | Searched all seven sources for EBITDA and adjusted earnings: no occurrence |
| No discrete fourth-quarter statements; the fiscal year release and 10-K give full-year figures | Medium | CP-1 | Derive the fourth quarter as full year less nine months and label it derived | Release FY and 10-K page:144 present year totals only |
| Prior-year quarterly segment data was recast for the new product-line operating model; the original fiscal 2025 annual report is not in the pack | Medium | CP-1 | Use recast comparatives and say so; do not compare with pre-recast figures | 10-Q Q1 page:6 recast statement |
| Credit ratings, trading quotes, peer data not supplied | Medium | CP-2 | Context holds none; obtain from market data if a relative view is wanted | Context ratings and quotes empty; searched all seven sources for Moody, Fitch, Standard & Poor and credit rating: no occurrence |
| Facilities with near-term dates: securitization and repurchase facilities now run to August 25, 2027, within twelve months of the as-of date; the revolving term loan period ended October 29, 2026, a date before the as-of date, and no source confirms the reversion occurred | Medium | CP-2 | Treat the reversion as scheduled by the filing and not independently confirmed after year end | 10-K page:164, page:165; no post-year-end document supplied |
| No post year-end document other than the fiscal 2026 10-K and release, both dated November 4, 2026; nothing after the cutoff is used | Low | CP-1A, CP-2 | None needed for cutoff; note that subsequent events are limited to the items in those two documents | Fiscal 2026 10-K and release |
| Announced phosphate joint venture and soybean facility are proposed and subject to approvals; terms, ownership split and funding are not supplied | Medium | CP-1A | Obtain announcement or agreement | Release FY page:2 describes "Pending project-related approvals" |
| Images, charts and any speaker notes not inspected; extraction is text only | Low | CP-5 | Treat flattened tables as located text; check column alignment when a figure is used | Text extraction only |
| Source quality and extraction fidelity not reviewed beyond cross-document number matches | Low | CP-5 | CP-5 samples quotes against pages | No fidelity review performed |
| Currency and unit: statements in USD thousands, release prose in USD millions and billions | Low | CP-1 | Carry units with each figure | 10-K page:144, Release FY page:1 |

## Next module

Proceed to CP-1. Carry forward these limitations: perimeter is CHS Inc. consolidated (the cooperative, with no common stock; the listed securities are preferred stock); segments are recast to the new Energy, Grains, Agronomy and Corporate and Services structure from fiscal 2026; no discrete fourth quarter or EBITDA is supplied; the capital expenditure definition must be named; and cash returns to owners for fiscal 2027 must follow the 10-K figures where they differ from the release. CP-2 must treat covenant levels, letters of credit and ratings as not supplied.
