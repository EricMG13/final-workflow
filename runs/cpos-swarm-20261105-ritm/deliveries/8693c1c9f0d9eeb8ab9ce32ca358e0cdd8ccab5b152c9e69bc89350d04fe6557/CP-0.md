## Request

Issuer: Rithm Capital Corp. (issuer id ritm; NYSE: RITM). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot, public case. Reporting currency per the run context: USD, with filing tables stated in thousands of dollars. Current period per the context: Q3 2026 (quarter ended September 30, 2026); prior period: FY2025.

Question for this module: can the effective source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? This module gives a source-readiness view only. It gives no credit conclusion, legal interpretation or investment opinion, and it does not normalize, reconcile or calculate figures. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

Context file settings relied on (the context is user input, not issuer evidence): ratings list empty, deal terms empty, quotes empty, valuation inputs blank, legal documents attached: none, no portfolio workbook, no prior case, no management bridge. Blank values are not treated as zero.

## Sources

### Issuer sources (pack files, sha256 of the pinned text file)

| Source name | sha256 | Pages retained | Document family and period |
| --- | --- | --- | --- |
| 10-K_2025-12-31_nrz-20251231.htm.jsonl | 1c6dc6fc4ac22ec0f983aa2d74b8236f15d06cb3d694e11e9adbcc9895b8a598 | 394 of 394 | Annual report, fiscal year ended December 31, 2025 |
| 10-Q_2026-03-31_nrz-20260331.htm.jsonl | 767e2e953064f6127dd3b7225c6f0b5f7530f4df6d8ed091932733330f9a34a9 | 173 of 173 | Quarterly report, quarter ended March 31, 2026 |
| 10-Q_2026-06-30_nrz-20260630.htm.jsonl | 6daf210aa16182f6824c848a97ad4428da4dc1534373b7320d814299eab6f84f | 184 of 184 | Quarterly report, quarter ended June 30, 2026 |
| 10-Q_2026-09-30_nrz-20260930.htm.jsonl | fe67ca59ff02f150e9ee570dc94fbca4e7146def420f7701280eb0487eeda6c4 | 186 of 186 | Quarterly report, quarter ended September 30, 2026 |
| EX-99.1_2026-04-28_ritm-2026331x8xkxexhibit991.htm.jsonl | 7f51477fb7c8b90bc73114496ecaaec4ef4c755e9b5be36834e7ff89e1e4f463 | 10 of 10 | Earnings release exhibit, Q1 2026 |
| EX-99.1_2026-07-28_ritm-2026630x8xkxexhibit991.htm.jsonl | 67986b436cacab7f9ff46416cb7f57062e1228ff3e0789e90880132c1b737079 | 10 of 10 | Earnings release exhibit, Q2 2026 |
| EX-99.1_2026-10-23_ritm-2026930x8xkxexhibit991.htm.jsonl | 7701308b9bdf89d27236cd23ca8f47f1dead7d427d8e354df0b2502bcac258f6 | 10 of 10 | Earnings release exhibit, Q3 2026 |

Non-issuer input: context file 73b514b2c18312238fd1fbb7bdc629559e11381beb8e9b95dfc9d7b54bcabe9d (user settings, not evidence). The pack also holds a retrieval index file that CP-OS ignores; it was not used.

### Supplied handoffs

None. CP-0 is the first module in this run, so no upstream handoff exists to list.

### Coverage basis

Every page of every source above is retained as extracted text, one page per chunk (`page:N` is the chunk number, not the printed page). The page counts are extraction counts. A successful extraction is not a fidelity review: tables arrive as flattened text lines and some tables break across chunks (for example the Note 17 debt table runs from 10-Q Q3 page:53 to page:56). This review opened the locators quoted in Findings and read the section headings of the others; it does not claim a line-by-line reading of all 967 retained pages.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The supplied annual report, three quarterly reports and three earnings releases are enough to start the requested snapshot work for Rithm Capital Corp., with bounded limits. No downstream step is blocked on sources. | Medium | No indentures, credit agreements, ratings or presentation decks were supplied, so debt terms rest on filing summaries only. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The latest quarterly report and its release both cover the quarter ended September 30, 2026 and sit inside the cutoff. | Latest financial position and results can be sourced from filed statements. | High |
| The debt note, maturity table, borrowing capacity table and covenant disclosures are present in the filings. | Debt and liquidity work can use filed disclosure, but only the filings' own summary of covenant terms. | Medium |
| Much of the debt is held in consolidated entities with no recourse to the parent, and no parent-only statements were supplied. | Parent-level creditor claims cannot be separated from consolidated figures without the filings' own recourse split. | Medium |
| No credit ratings, indentures, credit agreements or investor decks are in the pack. | Ratings, covenant definitions and presentation claims stay unverified. | High |
| A few figures in the filings use different scopes or look inconsistent on their face. | Downstream modules must cite the scope used and carry these conflicts forward. | Medium |

### Readiness view

The effective source set is adequate for the requested snapshot work, with limitations. The four periodic reports and three earnings releases are filed or furnished issuer documents with located financial statements, debt, liquidity, covenant, segment and subsequent-event disclosure, and the latest period (Q3 2026) is covered by both a quarterly report and a release. The view for each consumer is READY_WITH_LIMITATIONS. The strongest limiting evidence is that the covenant and guarantee terms of the senior unsecured notes are known only through the 10-Q summaries, because the indentures themselves are not in the pack, and that no external rating, quote or market data exists in the pack or the context. Nothing found makes a consumer CONDITIONAL or BLOCKED. This is a statement about source sufficiency only; it does not say any downstream analysis is complete or that any model input contract is met.

### Source assessment

| Source | Original authority | Entity and perimeter | Period and basis | Evidence located (exact text, locator) |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Filed audited annual report; auditor opinion present | Rithm Capital Corp. and subsidiaries, consolidated | Fiscal year ended December 31, 2025 | "For the fiscal year ended December 31, 2025" (10-K page:1); "/s/ Ernst & Young LLP" (10-K page:225) |
| 10-Q Q1 2026 | Filed unaudited interim report | Same consolidated perimeter | Quarter ended March 31, 2026 | "For the quarterly period ended March 31, 2026" (10-Q Q1 page:1) |
| 10-Q Q2 2026 | Filed unaudited interim report | Same consolidated perimeter | Quarter ended June 30, 2026 | "For the quarterly period ended June 30, 2026" (10-Q Q2 page:1) |
| 10-Q Q3 2026 | Filed unaudited interim report, signed October 30, 2026 | Same consolidated perimeter | Quarter and nine months ended September 30, 2026; balance sheet compared with December 31, 2025 | "For the quarterly period ended September 30, 2026" (10-Q Q3 page:1); "October 30, 2026" (10-Q Q3 page:186) |
| EX-99.1 Q1 2026 | Issuer earnings release, furnished; management narrative and non-GAAP measures | Same, with segment tables | Q1 2026 | "Rithm Capital Corp. Announces First Quarter 2026 Results" (release Q1 page:1) |
| EX-99.1 Q2 2026 | Same | Same | Q2 2026 | "Rithm Capital Corp. Announces Second Quarter 2026 Results" (release Q2 page:1) |
| EX-99.1 Q3 2026 | Same | Same | Q3 2026 against Q2 2026 | "Rithm Capital Corp. Announces Third Quarter 2026 Results" (release Q3 page:1) |

Name change: the 10-K refers to the acquired company as Paramount Group while the Q3 10-Q says "Elecor (f/k/a Paramount Group)" (10-Q Q3 page:20); downstream modules should treat them as one entity.

Identity: the file names carry the legacy label "nrz", but the cover pages name the registrant as Rithm Capital Corp. ("Rithm Capital Corp." with Commission File Number 001-35777, 10-Q Q3 page:1). Identity is taken from the cover text, not the file name. The preferred stock series and the ticker RITM also appear on that cover. No version conflicts among the filings were found; each is a distinct period, none supersedes another, and the earnings releases do not replace the filed statements. Filed statements control over release narrative; where a release restates a figure it is supporting evidence only.

The extraction headers inside each file print a sha256 of the original HTML document that differs from the pack-file sha256 listed above (for example the Q3 10-Q header prints c8b8c0ade8484f2f52a8bf354845358b10bf971ea028898b6750877410787345). The pack-file hash is the one CP-OS pins; the original-document hash is recorded here as a provenance note only.

### Located coverage by evidence need

| Evidence need | Located in the latest quarterly report | Located elsewhere | Exact text and locator |
| --- | --- | --- | --- |
| Balance sheet | 10-Q Q3 page:7 | 10-K page:227 to page:228; release Q3 page:4 to page:5 | "Total Assets $ 56,661,330 $ 53,063,126" (10-Q Q3 page:7) |
| Income statement, quarter and nine months | 10-Q Q3 page:8 | release Q3 page:4 | "Net Income Attributable to Common Stockholders $ 217,126 $ 193,662 $ 305,150 $ 514,084" (10-Q Q3 page:8) |
| Cash flows | 10-Q Q3 page:12 to page:13 | 10-K page:232 to page:233 | "Net cash provided by financing activities 3,597,283 283,075" (10-Q Q3 page:13) |
| Debt table by facility and collateral | 10-Q Q3 page:53 to page:55 (Note 17) | 10-K page:311; 10-Q Q2 page:52 to page:53 | "Total / Weighted Average $ 36,102,221 $ 35,646,765 5.5 % 5.6 $ 33,865,374" (10-Q Q3 page:54) |
| Maturities, recourse and non-recourse | 10-Q Q3 page:57; page:169 | 10-K page:314 | "$ 18,196,962 $ 19,680,259 $ 37,877,221" (10-Q Q3 page:57) |
| Borrowing capacity | 10-Q Q3 page:57 | 10-K page:314 | "Although available financing is uncommitted" (10-Q Q3 page:57) |
| Senior unsecured notes terms | 10-Q Q3 page:58 to page:63 | 10-K page:315 to page:318 | "for proceeds of approximately $493.7 million, net of commissions and initial offering expenses" (10-Q Q3 page:58) |
| Covenants | 10-Q Q3 page:57; page:61; page:63; page:169 | 10-K page:315 | "Rithm Capital was in compliance with all of its debt covenants as of September 30, 2026." (10-Q Q3 page:57) |
| Liquidity discussion | 10-Q Q3 page:165 to page:172 | 10-K page:201 to page:205 | "Our total cash and cash equivalents at September 30, 2026 was $1.7 billion." (10-Q Q3 page:169) |
| Cash reconciliation | 10-Q Q3 page:44 | 10-K page:302 (restricted cash by segment) | "Total Cash, Cash Equivalents and Restricted Cash $ 2,551,037 $ 2,789,413" (10-Q Q3 page:44) |
| Business, segments and acquisitions | 10-Q Q3 page:14 to page:16; page:20; page:23 to page:27 | 10-K page:8 onward | "The Company completed the acquisition of Elecor (f/k/a Paramount Group) on December 19, 2025" (10-Q Q3 page:20) |
| Subsequent events | 10-Q Q3 page:125 (Note 27) | 10-K page:385 | "determined that there were no subsequent events requiring recognition or additional disclosure in the consolidated financial statements, other than as described in these notes." (10-Q Q3 page:125) |
| Non-GAAP measure and reconciliation | The term does not appear in the Q3 10-Q text | release Q3 page:3, page:7 to page:8 | "Earnings Available for Distribution is a non-GAAP financial measure" (release Q3 page:3) |
| Recourse perimeter | 10-Q Q3 page:56 | 10-Q Q3 page:8 | "creditors of the VIE do not have recourse to Rithm Capital Corp." (10-Q Q3 page:56) |
| Note guarantees | 10-Q Q3 page:59, page:60, page:62 | none | "At the time of issuance, the 2031 Senior Notes were not guaranteed by any of the Company’s subsidiaries" (10-Q Q3 page:59) |
| Unencumbered asset test | 10-Q Q3 page:168 | page:59, page:61, page:63 | "each contain a requirement that the Company maintain Total Unencumbered Assets" (10-Q Q3 page:168) |

### Document conflicts and scope differences

These are recorded with both locators. None is reconciled here.

| Item | Locator A | Locator B | Downstream effect |
| --- | --- | --- | --- |
| Total debt: MD&A states one total, Note 17 face amount and the maturity table give others | "our total outstanding debt obligations amounted to $38.1 billion" (10-Q Q3 page:167) | "Total / Weighted Average $ 36,102,221 $ 35,646,765 5.5 % 5.6 $ 33,865,374" (10-Q Q3 page:54) and "$ 18,196,962 $ 19,680,259 $ 37,877,221" (10-Q Q3 page:57) | The retained text does not reconcile the three totals; they are described as face amount, carrying value and contractual maturities respectively. CP-1 must name the basis it uses and must not mix them. |
| Cash: two scopes | "Our total cash and cash equivalents at September 30, 2026 was $1.7 billion." (10-Q Q3 page:169) | "Cash, cash equivalents and restricted cash(A) 2,449,322 2,656,938" (10-Q Q3 page:7) and "Total Cash, Cash Equivalents and Restricted Cash $ 2,551,037 $ 2,789,413" (10-Q Q3 page:44) | Unrestricted cash, balance-sheet cash with restricted cash, and cash-flow-statement cash (which includes restricted cash of consolidated entities held in other lines) are three scopes. Liquidity work must pick the unrestricted figure and say so. |
| Senior notes issuance proceeds in the cash flow statement | "Proceeds from issuance of unsecured senior notes 495,000 495,000" (10-Q Q3 page:13) | "for proceeds of approximately $493.7 million, net of commissions and initial offering expenses" (10-Q Q3 page:58) | The nine-month 2026 cash-flow line equals the prior-year column and differs from the stated net proceeds of the 2031 Senior Notes issued May 14, 2026. The cause is not explained in the retained text. CP-1 should treat the Note 17 amounts as controlling for the notes and flag the cash-flow line. |
| Release comparative column | "Total Assets $ 56,661,330 $ 54,108,868" (release Q3 page:5) | "Total Assets $ 56,661,330 $ 53,063,126" (10-Q Q3 page:7) | The release compares with June 30, 2026 and the 10-Q compares with December 31, 2025. Different comparative dates, not a conflict in the September 30, 2026 figure. Line captions also differ (the release prints "Mortgage servicing rights and mortgage servicing rights financing receivables, at fair value"). |

### Per-consumer readiness

| Consumer | Readiness | Basis | Carried limitations |
| --- | --- | --- | --- |
| CP-1 (financial extraction) | READY_WITH_LIMITATIONS | Statements, debt note, maturities, capacity and covenant disclosures are located for Q3 2026, the prior two quarters and FY2025. | Debt-total basis conflict; cash scope conflict; no facility agreements; corporate facility covenant levels are not printed (see Gaps); tables flattened. |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, segment notes, acquisitions (Crestline, Elecor) and the quarterly release narrative are located. | No sponsor or ownership structure beyond the public registrant; release narrative is management claim only; no deck supplied. |
| CP-2 (credit synthesis) | READY_WITH_LIMITATIONS | Sources suffice to start; the module consumes the CP-1 and CP-1A handoffs, whose completion is sequenced by CP-OS and is not a source condition. | No ratings, market quotes or valuation inputs; recourse perimeter limits parent-level claims. |
| CP-5 (evidence trace validation) | READY_WITH_LIMITATIONS | Pinned sources are citable by page; quotes can be matched to retained spans. | Extraction is text only; a table-layout error cannot be detected from the text. |

## Calculations

No calculation is performed in this module. The method forbids normalizing, reconciling or calculating figures here. The only counts are page counts of retained sources, taken from the retained page numbers: 394 plus 173 plus 184 plus 186 plus 10 plus 10 plus 10 gives 967 retained pages across the seven issuer sources. Every dollar amount quoted above is copied unchanged from its locator, in thousands of dollars as printed in the tables unless the text states billions.

## Gaps

| Gap | Severity | Affected consumers | Remediation | Evidence |
| --- | --- | --- | --- | --- |
| Indentures for the 2029, 2030 and 2031 Senior Notes are not supplied. Covenants, guarantee terms and the Total Unencumbered Assets definition are known only from the 10-Q summaries. | Medium | CP-1, CP-2 | Obtain the indentures dated March 19, 2024, June 20, 2025 and May 14, 2026 named in the filing. | "each contain a requirement that the Company maintain Total Unencumbered Assets" (10-Q Q3 page:168) |
| Warehouse, repurchase, MSR and servicer advance facility agreements are not supplied; corporate facility covenants on tangible net worth, liquidity and indebtedness to tangible net worth are named but no level is printed in the 10-Q Q3 or 10-K text searched. Numeric regulatory minimums for servicers (FHFA and Ginnie Mae) are printed on 10-Q Q3 page:166 and are a separate matter. | Medium | CP-1, CP-2 | Obtain the facility agreements or the exhibits where filed; until then report only the disclosed compliance statement. | "failure to maintain a specified tangible net worth, liquidity or indebtedness to tangible net worth ratio" (10-Q Q3 page:169) |
| No corporate credit ratings for Rithm Capital Corp. or its notes in the pack or the context. The only rating text found concerns servicer ratings as a risk factor and a reference to Crestline's public credit rating in a valuation input. | Medium | CP-2 | Obtain agency ratings and dates from an external source, labelled as external. | "Favorable servicer ratings from third-party rating agencies" (10-K page:61) |
| Earnings presentations (decks) are not supplied. The Q3 release refers to a presentation on the company website. Only release text was available, so no slide coverage is claimed. | Low | CP-1A, CP-2 | Obtain the decks if slide-level claims are needed. | "please refer to the latest presentation posted on the Shareholders - Events & Presentations section of the Company’s website" (release Q3 page:3) |
| No parent-only or guarantor financial statements; the notes are not guaranteed by subsidiaries at issuance, and much debt sits in consolidated non-recourse entities. | Medium | CP-1, CP-2 | Use the filings' recourse and non-recourse maturity split; do not infer parent-only leverage. | "The obligations and liabilities of VIEs may only be satisfied with the assets of the respective consolidated VIEs" (10-Q Q3 page:56) |
| Borrowing capacity is described as uncommitted, while servicer advance facilities are described as committed. No table splits committed from uncommitted capacity by facility in the text searched, so committed liquidity cannot be separated from these sources alone. | Medium | CP-1, CP-2 | Search the facility notes and obtain facility agreements; state the gap if no committed amount is printed. | "Although available financing is uncommitted" (10-Q Q3 page:57); "non-recourse committed facilities" (10-Q Q3 page:137) |
| The conflicts in the table above (debt total basis, cash scope, cash-flow issuance line) are unresolved. | Medium | CP-1, CP-5 | Cite one basis per figure and carry the conflict forward. | See conflict table. |
| Tables are flattened text; column headers can sit on a different chunk from their rows. | Low | CP-1, CP-5 | Open the cited page and the page before it when a table has no header. | 10-Q Q3 page:54 starts mid-table. |
| Market data, quotes, peers and valuation inputs are blank in the context. They are not zero. | Low | CP-2 | Not needed for source readiness; supply if a relative value view is wanted. | Context file settings. |
| Draft versus executed: all sources are filed or furnished documents; no draft or unsigned material is present. The Q3 10-Q is signed October 30, 2026, before the cutoff. | None | All | None. | "October 30, 2026" (10-Q Q3 page:186) |

Currency and period: the sources report in US dollars in thousands, matching the context. The context names Q3 2026 and FY2025; the sources cover both, plus Q1 2026 and Q2 2026.

## Next module

Proceed to CP-1 on the seven issuer sources. Instruct it to: use the Q3 2026 10-Q (page:7, page:8, page:12 to page:13, page:44, page:53 to page:63, page:165 to page:172) as the primary evidence with the FY2025 10-K as the prior-period anchor; state the basis of every debt and cash figure (face, carrying, maturity-table, unrestricted, restricted) and carry the conflicts listed above forward; keep recourse and non-recourse debt separate; record the missing indentures, facility agreements, ratings and decks as gaps rather than zero; and treat the earnings releases as management-attributed support only. CP-1A, CP-2 and CP-5 follow in the order CP-OS sets.
