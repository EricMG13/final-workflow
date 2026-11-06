# CP-0 — Source readiness: Bally's Corp (baly)

## Request

- Issuer: Bally's Corp (issuer id `baly`; the filings name the registrant "Bally’s Corporation", NYSE: BALY), as of 2026-11-05, information cutoff 2026-11-05, reporting currency USD, current period Q2 2026, prior period FY2025 (context).
- Run: `baly-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Requested downstream modules: CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The analyst searched all seven pinned page files by term and read the chunks cited below in full; chunks not cited were not read in full. No provider was called.
- Question: can the supplied filings and releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This answer gives no credit conclusion, legal interpretation or investment opinion, and normalizes, reconciles and calculates nothing.
- Locators: `page:N` is the source chunk number in the pinned `.jsonl` file, not the printed page. Quotes are exact substrings of that chunk.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_baly-20251231.htm.jsonl | 2416bb6463c147a405baaa3764d6b99dd0f04403aa6bd66a1af2136569a6e954 | Form 10-K for the fiscal year ended December 31, 2025 (204 chunks) |
| 10-Q_2025-09-30_baly-20250930.htm.jsonl | 56bb4ccb0d42545489eded0e33ef5cc1b6e43986515a8c8a0964234c0c5a1ad2 | Form 10-Q for the quarter ended September 30, 2025 (87 chunks) |
| 10-Q_2026-03-31_baly-20260331.htm.jsonl | 4cf63f6c58a65fd25da3815352379f245d409f7447d9868c7381e2ae8ff65e16 | Form 10-Q for the quarter ended March 31, 2026 (87 chunks) |
| 10-Q_2026-06-30_baly-20260630.htm.jsonl | 972ae065bf1c6675d8214b94858dd8284ab57f02cd1acc546c671e0cb75a811b | Form 10-Q for the quarter ended June 30, 2026 (75 chunks) |
| EX-99.1_2026-03-16_ex991q42025earningsrelease.htm.jsonl | 409058f48783e9f5b7a8a00d5cc7ac8351ce41c9bc84bcf81e7c679d11a21bfd | Exhibit 99.1, preliminary Q4 and full-year 2025 results, dated March 16, 2026 (10 chunks) |
| EX-99.1_2026-05-18_ex991q12026earningsrelease.htm.jsonl | 7a189d9a918a76f21f04890e1c9f027b4cb34b6b08652098f8604b464b20f405 | Exhibit 99.1, Q1 2026 results, dated May 18, 2026 (8 chunks) |
| EX-99.1_2026-08-14_ex991q22026earningsrelease.htm.jsonl | d7b82a85199a3932febed54513d2e10fb96188bb07713475fd80698b0568c17c | Exhibit 99.1, Q2 2026 results, dated August 14, 2026 (9 chunks) |
| context | 49e5852827798fdbde43be3fcd478e45f6e9875c774c07cb1f9810d5a929f053 | User run settings; not issuer evidence |

Supplied handoffs: none. CP-0 is the first module, so no upstream handoff exists. The pack also holds `_retrieval.json`, a retrieval log that CP-OS ignored; it is not evidence.

Short labels used below: 10-K = FY2025 annual report; Q3-25 10-Q, Q1-26 10-Q, Q2-26 10-Q = the quarterly reports; Q4-25 release, Q1-26 release, Q2-26 release = the three Exhibit 99.1 files.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases support all four requested analyses with stated limits. The latest quarterly report carries a going concern warning and a covenant waiver, so downstream work must treat liquidity as the central issue. | Medium | No credit agreement, waiver, amendment or filing after the August 14, 2026 quarterly report is supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The June 30, 2026 quarterly report states substantial doubt about continuing as a going concern and describes a conditional lender waiver. | Debt and liquidity analysis must start from the waiver conditions and the unfinished financing plans. | High |
| Reported 2025 figures are split between a Predecessor and a Successor period around the February 7, 2025 merger. | Annual and trailing comparisons need explicit period labels and cannot be read as one clean year. | High |
| Debt sits at both the parent group and the majority-owned Bally’s Intralot, which does not guarantee parent debt. | Debt must be kept by borrower group before any consolidated leverage view is used. | Medium |
| Waiver terms, credit agreement amendments and filings after mid-August 2026 are not supplied. | Covenant headroom and later events cannot be verified from this pack. | High |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for all four requested consumers. Audited annual statements, three sets of interim statements and three earnings releases are located, with debt, liquidity, covenant, segment and cash-flow notes. The limits are three. First, the filings are the controlling authority and the releases are attributed management claims. Second, the 2025 comparatives are split into Successor and Predecessor periods. Third, executed credit documents and any event after the August 14, 2026 report are not supplied. Source sufficiency is not completion of downstream analysis; CP-OS sequences that.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Annual, interim and segment statements, debt and maturity tables, cash paid for interest and Adjusted EBITDA are located. 2025 columns are split by the merger date, and the Q4-25 release is preliminary. |
| CP-1A | READY_WITH_LIMITATIONS | Business description, segments, the February 2025 merger, the Intralot transaction, the sale-leaseback and the pending evoke offer are described in the filings and releases. Transaction agreements are not supplied. |
| CP-2 | READY_WITH_LIMITATIONS | Debt note, covenant text, waiver description, going concern note and liquidity discussion are located. Executed credit documents, the minimum liquidity level and post-June 30, 2026 financing outcomes are not supplied. |
| CP-5 | READY_WITH_LIMITATIONS | Every source has stable chunk numbers, so claims can be traced. Extraction is text only, so table layout and images are not inspected. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN. No consumer is CONDITIONAL or BLOCKED: no critical identity boundary is unresolved and no source has blocked preparation.

### Source register

#### Form 10-K for FY2025 (`10-K_2025-12-31_baly-20251231.htm.jsonl`)

- Family and authority: filed annual report, original authority for audited statements and the debt note. page:1 "FORM 10-K"; page:1 "For the fiscal year ended December 31, 2025". Signed page:203 "on March 23, 2026".
- Audit: page:102 states an unqualified opinion on the financial statements and refers to an adverse opinion on internal control: "expressed an adverse opinion on the Company's internal control over financial reporting because of a material weakness". Management's description is at page:51: "identified a material weakness as of December 31, 2025".
- Periods: the statements are split by the merger. page:102 "from February 8, 2025 to December 31, 2025 (successor), from January 1, 2025 to February 7, 2025 (predecessor), and for the year ended December 31, 2024 (predecessor)". There is no single full-year 2025 column.
- Statements located: balance sheet page:106 and page:107; cash flows page:109 and page:110, including page:110 "Cash paid for interest, net of amounts capitalized $340,739 $39,069 $314,245"; debt note page:162; maturities page:170; covenant text page:165; segment Adjusted EBITDAR and consolidated Adjusted EBITDA page:80 ("Adjusted EBITDA 478,009 24,390 495,611"); liquidity discussion from page:82; segment note page:187.
- Units: statements in thousands, MD&A summary in millions (page:75 "Total revenue $2,436.2 $220.5 $2,450.5"). USD.

#### Form 10-Q for Q3 2025 (`10-Q_2025-09-30_baly-20250930.htm.jsonl`)

- Family and authority: filed, unaudited quarterly report; supplies the discrete Q3 2025 quarter. page:3 "Three Months Ended September 30, 2025 Period from February 8, 2025 to September 30, 2025 Period from January 1, 2025 to February 7, 2025".
- Located: balance sheet page:2; cash flow supplement page:6 ("Cash paid for interest, net of amounts capitalized $ 243,341 $ 39,069 $ 256,161"); debt note page:38; covenant text page:41; segment note from page:50; Adjusted EBITDA page:70; liquidity from page:73.
- Version relationship: superseded for the balance sheet by later reports, but the only source for discrete Q3 2025 operations and the September 30, 2025 balance sheet. Keep it as a separate active source.

#### Form 10-Q for Q1 2026 (`10-Q_2026-03-31_baly-20260331.htm.jsonl`)

- Family and authority: filed, unaudited. page:3 "Three Months Ended March 31, 2026 Period from February 8, 2025 to March 31, 2025 Period from January 1, 2025 to February 7, 2025".
- Located: balance sheet page:2 (page:2 "Long-term debt, net 4,389,903 4,463,313"); cash flow page:5 including cash paid for interest; debt note page:39; maturities page:48; covenant text page:42; waiver page:43; Adjusted EBITDA page:71; liquidity from page:71.
- The waiver is already described here. This report contains no going concern language (search for "substantial doubt" across all seven sources finds it only in the Q2-26 10-Q).

#### Form 10-Q for Q2 2026 (`10-Q_2026-06-30_baly-20260630.htm.jsonl`)

- Family and authority: filed, unaudited; the latest periodic report, signed August 14, 2026 (page:75 "on August 14, 2026"). Controls the June 30, 2026 balance sheet and the going concern disclosure.
- Basis: page:10 "a Predecessor period, which includes the period from January 1, 2025 through February 7, 2025". The Successor period runs from February 8, 2025.
- Located: balance sheet page:2; operations page:3; equity page:4 and page:5; cash flows page:5 and page:6; going concern and plans page:11; debt note page:31 to page:38; segment note page:47 and page:48; MD&A from page:51 (consolidated Adjusted EBITDA at page:60, page:60 "Adjusted EBITDA 124,034 129,246 247,318 212,517 24,390"); liquidity page:62 to page:65; risk factor addition page:74; exhibit index page:74 and page:75.
- Units: thousands, USD. Foreign-currency debt is shown with principal currency at page:32.

#### Earnings releases (Exhibit 99.1)

- Family and authority: issuer press releases furnished as exhibits; management-prepared, unaudited, attributed claims. They do not override the filings.
- Q4-25 release: page:1 "reported preliminary financial results for the fourth quarter and full year ended December 31, 2025" and page:2 "The Company will file an extension for the filing of its Annual Report on Form 10-K". Its preliminary status means the 10-K controls. The Form 12b-25 it mentions is not supplied.
- Q1-26 release: dated May 18, 2026; page:1 "Consolidated revenue of $755.7 million increased 28.3% year over year".
- Q2-26 release: dated August 14, 2026. It adds a pro forma combined view of Bally’s and The Queen Casino & Entertainment, Inc. for six months 2025 (page:7 "Successor Pro Forma Combined(1)"), swap and hedge footnotes (page:9) and triple net lease cash payments (page:8 "Cash payments associated with triple net operating leases(2) 133,561 69,983 14,877"). Its text says reconciliations are in the tables below, but only segment Adjusted EBITDAR and revenue tables appear in the extracted text; the reconciliation to net loss is in the Q2-26 10-Q at page:48.
- Version relationship: the Q2-26 release repeats statement facts from the 10-Q (for example page:8 "Long-term debt, including current portion 4,506,700 4,500,657", also at Q2-26 10-Q page:31). It is not independent corroboration. The 10-Q controls.

### Information-availability boundary

- All sources are dated on or before August 14, 2026, before the as-of date and cutoff of 2026-11-05.
- Nothing dated between August 14, 2026 and 2026-11-05 is supplied. The Q2-26 10-Q refers to a Form 8-K filed on August 5, 2026 (page:74 "Fifth Amendment to Credit Agreement, dated as of July 29, 2026"). Neither that 8-K nor its exhibit is supplied. Any Q3 2026 results, financing outcome, equity sale or evoke closing are therefore Not supplied, not absent.
- Subsequent events inside the Q2-26 10-Q are dated before August 14, 2026 and are usable as disclosed: page:37 "On July 27, 2026, Bally’s Intralot" signed a sterling term facility; page:11 "In July 2026, the Company executed a term sheet" for a Bally’s Bronx loan, described as non-binding.

### Identity and perimeter

- Reporting entity: Bally’s Corporation, Delaware, consolidated with non-controlling interests. Bally’s Intralot S.A. is majority owned and consolidated: page:8 of the Q2-26 10-Q "the Company’s ownership of Bally’s Intralot increased to a controlling 57.9% interest".
- Predecessor and Successor: the February 7, 2025 merger with SG Parent LLC and The Queen Casino & Entertainment, Inc. created a push-down basis. Q2-26 10-Q page:10: "the results of operations, financial position and cash flows of the Predecessor and the Successor are not directly comparable".
- Debt borrower groups (Q2-26 10-Q page:31 to page:37): the parent group (2026 Term Loans, Revolving Credit Facility, 5.625% Senior Notes due 2029, 5.875% Senior Notes due 2031) and the Bally’s Intralot group (Intralot British Term Loan, Greek Term Loan, Greek Retail Bond, Revolving Credit Facility, Fixed and Floating Rate Notes, Supplemental Indenture, borrower Intralot Capital Luxembourg S.A.). page:11: "Bally’s Intralot does not guarantee any of Bally’s Corporation’s debt." The reverse relationship, whether parent group debt is guaranteed by Intralot entities, is stated only for the Senior Notes guarantors at page:32 ("guaranteed, jointly and severally, by certain of the Company’s restricted subsidiaries"). The full guarantor list and restricted or unrestricted designations are not supplied.
- Lease counterparty: GLPI leases many properties (Q2-26 10-Q page:7 footnote "Properties leased from Gaming and Leisure Properties, Inc."). Lease liabilities are on the balance sheet outside Long-term debt (page:2 "Long-term portion of lease liabilities 2,265,504 1,829,190").
- The context leaves borrower, parent and guarantor fields blank. That is not evidence of their absence.

### Strongest contrary evidence and conflicts

- Going concern. Q2-26 10-Q page:11: "raise substantial doubt about the Company’s ability to continue as a going concern", and "management’s plans do not alleviate substantial doubt". The Q1-26 10-Q and the 10-K do not carry this language. The evidence is a change between filings, not a conflict; downstream modules must date it to the June 30, 2026 report.
- Covenant description. The waiver is called a waiver of the "consolidated net leverage ratio covenant" at Q2-26 10-Q page:11 and page:38, while the covenant description at page:37 is a "maximum first lien net leverage ratio" tested when utilization exceeds 25% of commitments. The same page:38 later refers to the "consolidated first lien net leverage ratio covenant". The 10-K threshold was 30% (page:165 "exceed 30% of"). The wording difference is unresolved without the Credit Agreement and waiver, and CP-2 must carry it as a gap, not choose a definition.
- Revolver capacity. Q2-26 10-Q page:33: "there was $195.8 million available under the Company’s Revolving Credit Facility" and availability "will be further reduced to approximately $319 million" from October 2026. The same page states a total reduced commitment of about $519.3 million in February 2026. The balance sheet debt table shows Revolving Credit Facility 303,750 outstanding at page:31. Any liquidity consumer must keep these separate and must not infer letters of credit.
- Carrying amount versus principal. Page:31 "Long-term debt, including current portion 4,506,700 4,500,657" is after discount and a fair value adjustment, while page:37 maturities total "$ 4,910,068". The two are different bases, not a conflict; the note footnote (3) at page:32 explains the fair value adjustment.
- 10-K internal wording. The risk factor summary at page:20 refers to "material weaknesses" while the body at page:51 describes "a material weakness". The count is unresolved from text; the adverse internal control opinion at page:102 is unambiguous.
- Preliminary release versus 10-K. The Q4-25 release is labelled preliminary and announces an extension for the 10-K, which was signed March 23, 2026. Revenue of $2,436,189 thousand for the Successor period in the release (page:2 "Total $ 746,245 $ 580,365 $ 2,436,189 $ 220,498 $ 2,450,478") matches the 10-K MD&A summary of $2,436.2 million (page:75). No conflict found on revenue; other release figures must be checked against the 10-K before use.

### Consumer evidence demand

| Consumer | Evidence it needs | Located | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | Statements, segments, debt by instrument, maturities, cash paid for interest, Adjusted EBITDA | 10-K page:106 to page:110, page:162, page:170; Q3-25 10-Q page:2, page:38; Q1-26 10-Q page:2, page:5, page:39, page:48; Q2-26 10-Q page:2 to page:6, page:31 to page:37, page:47 to page:48, page:60 | Successor and Predecessor split; Q2 2025 three-month comparatives come only from the Q2-26 10-Q and its release; Q4-25 release preliminary; Adjusted EBITDA is issuer non-GAAP |
| CP-1A | Business, segments, history, ownership, transactions | 10-K page:9; Q2-26 10-Q page:6 to page:8; Q2-26 release page:1 to page:4; Q4-25 release page:1 | Merger Agreement, Intralot Transaction Agreement, evoke offer documents and sale-leaseback agreement not supplied |
| CP-2 | Liquidity, covenants, waiver, lease burden, going concern, financing plans | Q2-26 10-Q page:11, page:33, page:37 to page:38, page:62 to page:65, page:74; Q1-26 10-Q page:42 to page:43; 10-K page:165 | Credit Agreement, Amendments No. 3 to No. 5, Conditional Waiver, 2026 Term Loan agreement, indentures not supplied; minimum liquidity level not located in the text |
| CP-5 | Traceable claims in every source | All sources carry chunk numbers | Text extraction only; no table-layout or image check; no external or market data supplied |

### Analytical read-through

- Usable coverage: audited FY2025 statements, interim statements to June 30, 2026 and the Q3 2025 comparatives are located in the filings. Debt, maturities, cash paid for interest, segments and consolidated Adjusted EBITDA are all in the Q2-26 10-Q, so a trailing view to June 30, 2026 can be built from filed figures once period labels are kept separate.
- Strongest contrary evidence: the Q2-26 10-Q page:11 states that the company "does not project that it would satisfy the liquidity maintenance requirement". The mechanism: a reduction in revolver availability from October 2026 and the end of the covenant waiver require financing that is not yet committed, so a downstream consumer that reads only reported covenant compliance at June 30, 2026 (page:38 "the Company was in compliance with all covenants under its debt agreements") would overstate near-term headroom.
- Source risk mechanism: the Successor and Predecessor split and the Intralot consolidation break like-for-like comparison. A consumer that sums or subtracts across the merger date, or reads consolidated debt as one borrower group, mixes bases.
- What cannot proceed from this pack alone: covenant headroom against the executed definitions, waiver condition testing, guarantor-level or restricted-group analysis, and any view of events after August 14, 2026.
- Next evidence action: supply the Credit Agreement with Amendments No. 3, No. 4 and No. 5, the Conditional Waiver dated May 14, 2026, the 2026 Term Loan Credit Facility agreement, the Senior Notes Indenture, the Form 8-K of August 5, 2026 and every later 8-K and the Q3 2026 report if filed before the cutoff.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Figures quoted above are printed in the sources with their locators.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit Agreement, Amendments No. 3 to No. 5, Conditional Waiver, 2026 Term Loan agreement and indentures not supplied; minimum liquidity level and waiver conditions not located in the text | High | CP-2, CP-5 | Supply the executed documents (Q2-26 10-Q page:74 lists them as exhibits or incorporated exhibits) |
| Nothing dated after August 14, 2026 supplied; the August 5, 2026 Form 8-K and any Q3 2026 report or financing outcome are Not supplied | High | CP-1A, CP-2 | Supply later 8-Ks and the Q3 2026 report if filed on or before 2026-11-05 |
| Successor and Predecessor periods are not comparable; no single full-year 2025 column | Medium | CP-1, CP-2 | Keep period labels explicit; use the Q2-26 release pro forma combined view only as labelled non-GAAP |
| Bally’s Intralot debt and parent group debt sit in separate borrower groups; full guarantor and restricted or unrestricted detail not supplied | Medium | CP-1, CP-2 | Supply guarantor schedules and Intralot group financial statements |
| Covenant naming differs across the Q2-26 10-Q (net leverage versus first lien net leverage; 25% versus 30% trigger in the 10-K) | Medium | CP-2 | Confirm against the Credit Agreement and waiver |
| Q4-25 release is preliminary and the Form 12b-25 is not supplied | Low | CP-1 | Use the 10-K as controlling |
| Merger, Intralot, sale-leaseback, evoke and GLPI lease agreements not supplied | Medium | CP-1A, CP-2 | Supply the agreements or rely on filed descriptions with that limit |
| Text extraction only; no original HTML, XBRL or image inspection | Low | CP-1, CP-5 | Check flagged tables against the filed HTML |
| No ratings, market prices or peer data | Low for the selected modules | CP-2 | Keep Not supplied |

## Next module

- CP-1: use the 10-K and 10-Q statements as controlling and the releases as attributed support. Keep Successor and Predecessor columns separate, keep parent group and Bally’s Intralot debt separate, keep lease liabilities outside debt, and label Adjusted EBITDA and Adjusted EBITDAR as issuer non-GAAP.
- CP-1A: carry the February 7, 2025 merger, the October 8, 2025 Intralot Transaction, the 2026 Bally’s Twin River (Lincoln) sale-leaseback, the New York license and the evoke offer as the central transactions, citing the filings. Label anything after August 14, 2026 as Not supplied.
- CP-2: start from the going concern note, the waiver conditions and the October 2026 revolver reduction. Carry the covenant naming difference and the missing minimum liquidity level as gaps.
- CP-5: check each claim against the cited chunk, and carry the limitation that no agreement and no post-August 14, 2026 filing is supplied.
