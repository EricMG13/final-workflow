# CP-0 Source readiness: CENTENE CORP (cnc)

## Request

- Issuer: CENTENE CORP (issuer id `cnc`), registrant name "CENTENE CORPORATION", ticker CNC. As-of date and information cutoff: 2026-11-05. Reporting currency: USD. Current period q3-2026, prior period fy-2025 (context).
- Run `cnc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. Requested downstream modules: CP-1, CP-1A, CP-2 and CP-5 (the launcher's `minimum` set). CP-0 runs first as their dependency.
- Execution: host session. The host read the pinned files and wrote this answer. No provider was called.
- Question: can the supplied public filings and releases support CP-1, CP-1A, CP-2 and CP-5, and what remains blocked?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This answer gives no credit conclusion, legal interpretation or investment opinion, and it normalizes, reconciles and calculates nothing.
- Locators are `page:N` chunk numbers of the pinned `.jsonl` extracts, not printed page numbers. Quotes are copied from the cited chunk.

## Sources

### Issuer sources relied on

| Short name | Exact source name | sha256 (pinned file) | Role |
| --- | --- | --- | --- |
| 10-K FY2025 | 10-K_2025-12-31_cnc-20251231.htm.jsonl | 097062d4e055a3b7fe83b7f7a6e69a627cdfc677e170580a5543c61781d7f32c | Annual report, 182 chunks |
| Q1 10-Q | 10-Q_2026-03-31_cnc-20260331.htm.jsonl | 6fdb16147461b8c90a892872b86f94619262dc29b1649522f12be59d50d43010 | Quarterly report, 42 chunks |
| Q2 10-Q | 10-Q_2026-06-30_cnc-20260630.htm.jsonl | 2be254120598acb867bfc89cb539dc675621975d5b2820213b11fde2ab54d522 | Quarterly report, 50 chunks |
| Q3 10-Q | 10-Q_2026-09-30_cnc-20260930.htm.jsonl | cfb19f79c82250660e2e3f3fc4242fe18840a50e06dfa54c4c173df9081f0994 | Quarterly report, 53 chunks |
| Q1 release | EX-99.1_2026-04-28_a20260428ex991pressrelease.htm.jsonl | 85e525be3f7df9445c1acc49590c58f56053e97a34531af048cb7fd64ca5f94b | Earnings release, 14 chunks |
| Q2 release | EX-99.1_2026-07-28_a20260728ex991pressrelease.htm.jsonl | ef848078ad02a5ade77bb7226070a38945f9e917a1e3e86d5abb0edd73e6d395 | Earnings release, 15 chunks |
| Q3 release | EX-99.1_2026-10-27_a20261027ex991pressrelease.htm.jsonl | 916ad849ec4d38de97614bebc7921009e1fad702ea222f32804d2cf10f3a8c80 | Earnings release, 15 chunks |

### Run settings

| Item | sha256 | Role |
| --- | --- | --- |
| context | 513a568e8f913d85d10b3279b6da71f4942d77c29169f956b5f35a2740b22b67 | User run settings; not issuer evidence. Blank fields (borrower, parent, guarantors, quotes, ratings, market data) are not zero. |

### Supplied handoffs

None. CP-0 is the first module, so no upstream handoff exists.

### Provenance note

The first chunk of each extract begins "Visible text of ..." and names the sha256 of the original HTML document. Those original-document hashes (10-K FY2025 84f363689f1eece5286ce0dc59aa3056b86661579db8f8deb3c84c222eb50ec3; Q1 10-Q ca7706752a9c72356443db182cb1fb91c3cae7866d206d7a26e6c3eb7ad81d66; Q2 10-Q 7fc98f7d77f2e49ceaa9d2468247189c3993bb785908f54fb145bfc7c86f2918; Q3 10-Q 79ddcf084bbb94a972eaff9b37bfae2e01e530497d998523788ec4a726b43a76) differ from the pinned extract hashes above, as expected. The pinned extract hashes are the ones this run is bound to. The original HTML and XBRL are not supplied.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied filings and releases are sufficient for all four downstream modules to run, each with stated limitations. No consumer is blocked or conditional. | Medium | Executed credit agreement, indentures, receivable purchase agreement and divestiture agreement are not supplied; sources are text extracts without original tables or XBRL. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual statements and unaudited statements for every 2026 quarter are present, with comparatives. | Supports reported-fact extraction and trend work; cash flows are cumulative only, so quarterly flows must be derived downstream. | High |
| Debt, covenant, letter of credit and liquidity disclosures are located in each filing, including the October senior note redemption. | Debt and headroom analysis can proceed from filed notes, but covenant terms rest on summaries, not executed agreements. | Medium |
| The receivable sale arrangement and the pending Magellan divestiture are described only in filing notes. | Off-balance-sheet liquidity support and perimeter changes cannot be checked against contracts; treat them as disclosed claims. | Medium |
| The releases are management documents that repeat the filings. No rating reports, investor decks or market data are supplied. | Releases add no independent corroboration; rating and relative-value judgments have no source support in this set. | Medium |

### Readiness view

The effective source set supports the requested work with bounded limitations. All four consumers, CP-1, CP-1A, CP-2 and CP-5, are READY_WITH_LIMITATIONS, and none is conditional or blocked. The set holds one audited annual report for FY2025 with FY2024 and FY2023 comparatives, three unaudited quarterly reports for Q1, Q2 and Q3 2026 with 2025 comparatives, and three earnings releases dated 2026-04-28, 2026-07-28 and 2026-10-27. All of it is dated before the cutoff of 2026-11-05. The main restrictions are that the filed financial statements are the controlling evidence, the releases are secondary and largely duplicative, and no executed financing, receivable-sale or divestiture agreements are supplied. Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Consumer assessments

| Consumer | Status | Basis | Limitation carried forward |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | Audited FY2025, FY2024 and FY2023 statements (10-K FY2025 page:129, page:131) and unaudited Q1, Q2 and Q3 2026 statements with 2025 comparatives (Q1 10-Q page:7, Q2 10-Q page:7, Q3 10-Q page:8) are located, with debt notes in all four filings. | Cash flow statements are cumulative (three, six and nine months), so discrete quarterly cash flow is not printed. Text extracts flatten tables. Segment, KPI and non-GAAP tables sit in the 10-Qs and releases. |
| CP-1A | READY_WITH_LIMITATIONS | Business, segments, regulatory and contract changes, the pending Magellan sale, the receivable sale arrangement and management narrative are located in 10-K FY2025 page:12 onward, Q3 10-Q page:28 to page:39 and the releases. | Magellan sale agreement, receivable purchase agreement and contract-award documents are not supplied. No proxy statement, no investor presentation. |
| CP-2 | READY_WITH_LIMITATIONS | CP-2 synthesises from CP-1 and CP-1A. Covenant, liquidity, letter of credit and unregulated cash text is located (Q3 10-Q page:46, page:47). | Covenant definitions are known only from filing summaries. No ratings, market prices or peer data are supplied (context). |
| CP-5 | READY_WITH_LIMITATIONS | Every source has stable chunk numbers, so claims can be traced to a locator and quote. | Visual and table-layout checks against the filed HTML are not possible. Releases cannot corroborate filings. |

### Source register

#### 10-K FY2025

- Family and authority: filed annual report on Form 10-K (10-K FY2025 page:1: "For the fiscal year ended December 31, 2025"). Original authority for audited consolidated statements, notes and Item 7 text. Auditor report signed KPMG LLP in St. Louis (10-K FY2025 page:129: "We have served as the Company's auditor since 2005.").
- Entity and perimeter: Centene Corporation and subsidiaries, consolidated. Parent-company-only condensed information is also supplied (10-K FY2025 page:170: "20. Condensed Financial Information of Registrant").
- Period and basis: FY2025 with FY2024 comparatives on the balance sheet and FY2025, FY2024 and FY2023 on operations and cash flows. US GAAP, USD millions (10-K FY2025 page:129: "CONSOLIDATED BALANCE SHEETS (In millions, except shares in thousands and per share data in dollars)").
- Located content: balance sheet and operations statement (page:129), cash flows with cash paid for interest and taxes (page:131, page:132), debt note (page:158 to page:160), leases (page:160), segment note (page:169, page:170), parent-only schedule (page:170 to page:172), Item 9B on the receivable purchase agreement (page:177) and exhibit index (page:179 to page:182).
- Version relation: the base annual report for the period. The Q3 10-Q balance sheet carries the 2025 year-end comparative and states that "Certain 2025 amounts in the consolidated financial statements and notes to the consolidated financial statements have been reclassified to conform to the 2026 presentation." (Q3 10-Q page:12). Where the 10-K and a later 10-Q differ on a 2025 figure, both are kept and CP-1 must label which presentation it uses.

#### Q1 10-Q, Q2 10-Q and Q3 10-Q

- Family and authority: filed quarterly reports with unaudited statements (Q1 10-Q page:1: "For the quarterly period ended March 31, 2026"; Q2 10-Q page:1: "For the quarterly period ended June 30, 2026"; Q3 10-Q page:1: "For the quarterly period ended September 30, 2026"). Signed as of April 28, 2026 (Q1 10-Q page:42), July 28, 2026 (Q2 10-Q page:49) and October 27, 2026 (Q3 10-Q page:52: "duly authorized as of October 27, 2026").
- Entity and perimeter: Centene Corporation and subsidiaries, consolidated (Q3 10-Q page:1: "CENTENE CORPORATION (Exact name of registrant as specified in its charter)").
- Period and basis: three-month columns for each quarter and cumulative columns (three, six, nine months) with 2025 comparatives; balance sheets compare to December 31, 2025. USD millions (Q3 10-Q page:8: "CONSOLIDATED BALANCE SHEETS (In millions, except shares in thousands and per share data in dollars)").
- Located content in the Q3 10-Q: balance sheet (page:8), operations (page:9), cash flows with interest paid and taxes paid (page:11), debt note (page:20, page:21), the receivable sale note (page:14, page:15), segment note (page:22 to page:24), legal matters (page:25 to page:27), MD&A (page:28 to page:50) and unregulated cash (page:46).
- Version relation: each 10-Q supersedes nothing; the three remain separate active sources. Q2 and Q3 interim data build on each other: the Q3 10-Q states "the quarter-to-date operating cash flow use of $3,669 million" (Q3 10-Q page:12), which matches the Q3 release (Q3 release page:1: "Total cash flow (used in) operations (in millions) $ (3,669)").

#### Q1 release, Q2 release and Q3 release

- Family and authority: issuer news releases furnished as Exhibit 99.1, dated April 28, 2026, July 28, 2026 and October 27, 2026 (Q3 release page:1: "ST. LOUIS, October 27, 2026 -- Centene Corporation (NYSE: CNC)"). Management-prepared, unaudited; they carry attributed management narrative and non-GAAP measures.
- Located content: reported and adjusted results, reconciliations, guidance (Q3 release page:4), statements of operations, balance sheet and cash flows (Q3 release page:12, page:13), membership, medical claims liability roll-forward (Q3 release page:15) and a liquidity statement (Q3 release page:3: "maintained $175 million of cash available for general corporate use").
- Version relation: their statements repeat the 10-Q statements for the same date, so the 10-Q controls and the release is not independent corroboration. The release also states "Debt reduced by $1.1 billion since June 30, 2026" (Q3 release page:1), a management claim that sits on top of the filed debt note.

### Identity and perimeter

- Reporting entity: Centene Corporation, Delaware, NYSE "CNC" (Q3 10-Q page:1: "Common Stock $0.001 Par Value CNC New York Stock Exchange"). The same entity files the 10-K, three 10-Qs and three releases. Identity is confirmed from content, not file names.
- Debt issuer and borrower: Centene Corporation issues the senior notes ("The indentures governing the senior notes listed in the table above contain restrictive covenants of Centene Corporation." 10-K FY2025 page:158). The Revolving Credit Facility and Term Loan Facility sit under one credit agreement (10-K FY2025 page:159: "The maturity date for the New Credit Agreement is March 5, 2030.").
- Guarantors and restricted group: no subsidiary guarantor of the notes or the credit agreement is named in any supplied source (a text search of the 10-K FY2025 for "guarant" finds no guarantor of the notes or the credit agreement; the hits are generic risk language, government-backed securities and the performance guaranty on the receivable purchase agreement, page:177). The context leaves guarantors blank. Guarantor-level analysis is an unresolved distinction and a gap, not evidence of absence.
- Operating subsidiaries: health plans are regulated entities that are subject to statutory capital rules (10-K FY2025 page:33), and the filings split cash and investments into regulated and unregulated (Q3 release page:14). Parent-only data are supplied only for FY2025 (10-K FY2025 page:170 to page:172).
- Perimeter changes: the remaining Magellan Health businesses are held for sale (Q3 10-Q page:13: "In December 2025, the Company signed a definitive agreement to sell the remaining Magellan Health businesses, which is included in the Other segment."). The 10-K FY2025 also records the earlier Circle Health sale agreement (page:147).
- Currency and units: USD millions except shares in thousands and per share data in dollars. Membership is a count of members. No foreign-currency reporting basis was found.

### Debt, covenant and liquidity coverage

- Debt table at each date: seven senior note series plus a Term Loan Facility and issuance costs (Q3 10-Q page:20: "Total debt 15,542 17,401"; 10-K FY2025 page:158: "Total debt 17,401 18,533"). The Dec 31, 2025 total debt in the 10-K and the Q3 10-Q comparative show the same printed figure.
- Subsequent debt event: "In October 2026, the Company redeemed in full at par the remaining $569 million of its par value Senior Notes due 2027 through the debt repurchase program." (Q3 10-Q page:21). It is dated after the balance sheet date and before the cutoff.
- Covenant: "Our maximum debt-to-capital ratio under the credit agreement may not exceed 0.60 to 1.00." (Q3 10-Q page:47); the 10-K adds a step-up (10-K FY2025 page:159: "to 0.65 to 1.00"). The reported ratio is stated by the issuer (Q3 10-Q page:47: "was 41.1%, compared to 46.5% at December 31, 2025"). The credit agreement definition is not supplied.
- Letters of credit and surety bonds: "We had outstanding letters of credit of $113 million as of September 30, 2026, which were not part of our Revolving Credit Facility." (Q3 10-Q page:47).
- Liquidity: unregulated cash of "$175 million was available for general corporate use at September 30, 2026" (Q3 10-Q page:46). Cash available for general corporate use is also stated for the earlier quarters (Q1 release page:4: "$437 million of cash available for general corporate use"; Q2 release page:3: "$715 million of cash available for general corporate use"). The undrawn revolver amount is not printed as a figure; the 10-Q gives the facility size and "no borrowings outstanding under our Revolving Credit Facility" (Q3 10-Q page:47).
- Receivable sale: "The maximum outstanding purchase amount permitted under the agreement is $4,250 million." (Q3 10-Q page:14). The agreement itself is not supplied; the 10-K FY2025 lists it as Exhibit 2.1 filed with that report (page:179).
- Cash paid: "Interest paid $ 438 $ 458" and "Income taxes paid, net $ 15 $ 540" are the nine-month figures (Q3 10-Q page:11). Annual figures are in 10-K FY2025 page:132.

### Cross-source relationships and conflicts

- No contradiction was found between the 10-K FY2025 year-end balance sheet figures and the December 31, 2025 columns of the Q1 10-Q and Q3 10-Q for total debt, long-term debt and total stockholders' equity. The 2026 10-Qs state that some 2025 amounts were reclassified (Q3 10-Q page:12), so a 2025 comparative can differ from the original 10-K and must be traced to the right document.
- The 10-K FY2025 maturity schedule prints "Total $ 17,493" (page:160). The debt table prints "Total senior notes 15,490" and "Term Loan Facility 2,000" (page:158). The printed schedule total is not identical to the sum of those two lines. This is carried to CP-1 as an unreconciled presentation difference, not resolved here.
- Letters of credit were $120 million at December 31, 2025 (10-K FY2025 page:160) and $113 million at September 30, 2026 (Q3 10-Q page:47). These are different dates, not a conflict.
- Q3 10-Q page:12 states about $1,635 million of state pass-through payments at September 30, 2026 against about $4,500 million at June 30, 2026. These are balance-sheet timing items that affect quarterly operating cash flow; CP-1 must not read the quarterly cash flow without them.

### Information-availability boundary

- Every source is dated on or before October 27, 2026, which is before the cutoff of 2026-11-05. The latest dated facts are the Q3 10-Q signature and the debt repurchase program balance "as of October 27, 2026" (Q3 10-Q page:21).
- The Q3 10-Q extract does not print the EDGAR filing date, only the signature date, so the filing date is Not supplied. No supplied source dated after October 27, 2026 exists. Events between October 27, 2026 and the as-of date are Not supplied, not absent.
- A digital audio playback of the Q3 call is dated "November 3, 2026" (Q3 release page:4); it is a future logistic date inside a release, not a fact used.

### Analytical read-through

- Usable coverage: the FY2025 audit-backed statements and the 2026 interim statements with 2025 comparatives give a reported base for the latest twelve months and for each discrete quarter of 2026 from the three-month columns. This supports the data foundation for CP-1 and the business context for CP-1A.
- Strongest contrary evidence: the debt and covenant mechanics sit in filing summaries and not in the executed credit agreement or indentures, which are listed only as exhibits (10-K FY2025 page:180: "4.4 Indenture, dated as of February 13, 2020, by and between Centene Corporation, as issuer, and The Bank of New York Mellon Trust"). The risk mechanism is that a consumer may read the issuer's debt-to-capital ratio as a covenant test when the credit agreement's own definition is not available, which would mis-state covenant headroom in CP-2.
- Second mechanism: the Part D receivable sale is accounted as a sale, so the receivable leaves the balance sheet and the cash proceeds are operating cash flow (Q3 10-Q page:14: "The cash proceeds and associated loss on sale of receivables are recorded as operating cash flows."). A consumer that reads operating cash flow without this note would overstate organic cash conversion, which CP-1 and CP-2 must separate from the sale.
- Third mechanism: the Magellan businesses are held for sale, so segment and consolidated trends include a perimeter that is leaving (Q3 10-Q page:13). CP-1A must keep that perimeter visible.
- What cannot proceed: legal interpretation of covenants, baskets or guarantees; guarantor-level or restricted-group analysis; rating-agency or market-based valuation work; any fact after October 27, 2026.
- Next evidence action: supply the Credit Agreement dated March 5, 2025 and the indentures (exhibit index, 10-K FY2025 page:180), the Receivable Purchase Agreement and Performance Guaranty (10-K FY2025 page:179), the Magellan sale agreement, any 8-Ks after October 27, 2026, and rating reports if relative-value work is wanted.

## Calculations

No new calculation. CP-0 does not normalize, reconcile or calculate figures. Every figure above is quoted from a located chunk and is labelled with its period. Where this answer says two printed figures are not identical (the maturity schedule total against the debt table), it leaves the reconciliation to CP-1.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreement and indentures not supplied; covenant definitions and guarantor structure unknown | High for legal work; Medium for CP-2 | CP-2, CP-5 | Supply the executed Credit Agreement and indentures |
| Receivable Purchase Agreement and Performance Guaranty not supplied; purchaser appetite and terms only from filing notes | Medium | CP-1, CP-2 | Supply Exhibits 2.1 and 2.2 to the 10-K |
| Magellan sale agreement not supplied; closing terms and proceeds not in the set | Medium | CP-1A, CP-2 | Supply the agreement or the related 8-K |
| Cash flows only cumulative; discrete Q2 and Q3 cash flows are not printed (the Q3 operating figure is quoted) | Medium | CP-1 | Derive downstream from cumulative columns and show the formula |
| Parent-only financial information supplied for FY2025 only | Medium | CP-1, CP-2 | Treat parent liquidity as annual; do not extend to 2026 |
| Undrawn revolver amount not printed as a figure | Low | CP-2 | Derive from the facility size and borrowings, citing each; the filings state that the letters of credit are not part of the revolver |
| Maturity schedule total differs from the debt table lines (10-K FY2025 page:160 against page:158) | Low | CP-1 | Reconcile in CP-1 and state the choice |
| 2025 comparatives reclassified in 2026 filings | Low | CP-1, CP-5 | Label which presentation each 2025 figure uses |
| Events after October 27, 2026 and the Q3 10-Q filing date not supplied | Medium | CP-1A, CP-2 | Supply later 8-Ks or confirm none |
| No rating reports, investor presentations, market prices or peers | Low for the selected modules | CP-2 | Not required for this scope; keep Not supplied |
| Text extracts only; original HTML tables and XBRL not supplied | Low | CP-1, CP-5 | Check flagged tables against the filed HTML |

## Next module

- CP-1: treat the 10-K FY2025 and the 10-Qs as controlling and the releases as secondary. Keep annual, three-month, six-month and nine-month columns separate. Show debt table lines, the October 2026 redemption and the receivable sale as separate items. Label the issuer's debt-to-capital and adjusted measures as issuer-defined.
- CP-1A: carry the Magellan sale, the receivable sale arrangement, the 2026 contract and membership changes and the CMS Star Ratings disclosure as dated facts, and mark anything after October 27, 2026 as Not supplied.
- CP-2 and CP-5: carry the missing executed agreements, the guarantor gap and the cumulative cash flow limitation as restrictions. CP-5 must treat the releases as duplicative of the filings.
