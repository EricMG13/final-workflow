## Request

- Issuer: NABORS INDUSTRIES LTD (issuer id nbr, NYSE: NBR), the Bermuda registrant that files the consolidated statements.
- As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. The newest pinned filing is the third-quarter 2026 Form 10-Q signed November 4, 2026.
- Pathway: credit_snapshot, public case, research run. Reporting currency per context: USD. Current period: Q3 2026 (quarter ended September 30, 2026). Prior period: FY2025 (year ended December 31, 2025).
- Question for this module: can the supplied source set support the requested downstream work, and what remains blocked? Source sufficiency only; no credit conclusion, legal interpretation or investment opinion is given here.
- Requested consumers assessed: CP-1, CP-1A, CP-2, CP-5. The Python dependency planner, not this module, sequences them.
- Settings file `context` is a user input, not issuer evidence. It leaves blank the borrower, parent, guarantors, sponsor, ratings, quotes, deal terms and valuation inputs; these are treated as not supplied, not as zero or none.
- Upstream handoffs: none. CP-0 is the first module in this run.
- Method limits honoured: no figure is normalized, reconciled or calculated in this module; figures below are quoted with locators only. A page locator is the source chunk shown as `page:N`, not a printed page.

## Sources

### Issuer sources relied on

| Source name | sha256 | Document family and period | Pages retained |
| --- | --- | --- | --- |
| 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | 427cc2fc64bcd723a27a6c2478a12093e219dc045e02d41b40eab49061568751 | Annual report on Form 10-K, fiscal year ended December 31, 2025 | 143 |
| 10-Q_2026-03-31_nbr-20260331x10q.htm.jsonl | 11eb9a5886137a3201a1d5b34cd6e8ef50e247d641cd61ec9c9814adc458e187 | Quarterly report on Form 10-Q, quarter ended March 31, 2026 | 40 |
| 10-Q_2026-06-30_nbr-20260630x10q.htm.jsonl | 6c2a6d1bdbcbd71ad95906094386639f0ffd409dc513dcadc487db645242cb3b | Quarterly report on Form 10-Q, quarter ended June 30, 2026 | 44 |
| 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | 7e240e48875d03a0d84a20d6f741fc0c9988f286076c7c4d265721b0e0793ce2 | Quarterly report on Form 10-Q, quarter ended September 30, 2026 | 46 |
| EX-99.1_2026-04-28_tm2612942d1_ex99-1.htm.jsonl | 811d6f2d82a109aad668cd621d65877dd4784a4f2a4d17ed4d8fd9b20e6f9b37 | Earnings release (Exhibit 99.1), first quarter 2026, dated April 28, 2026 | 11 |
| EX-99.1_2026-07-28_tm2621313d2_ex99-1.htm.jsonl | 4fe99e5d4274f6274ec08f0c05beac58f1ab8c742acabe22ed57e9e2bd36a4e7 | Earnings release (Exhibit 99.1), second quarter 2026, dated July 28, 2026 | 12 |
| EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | f9d4d37c25f2acc92f4bf176ff35ad6539e2f40b8c58a320a92c16c59d447e59 | Earnings release (Exhibit 99.1), third quarter 2026, dated October 27, 2026 | 12 |

The pack folder also holds `_retrieval.json`, which the run ignored as a non-issuer file. Each source file begins with a line giving the sha256 of the original HTML; the sha256 values in the table are those of the pinned `.jsonl` extractions that CP-OS hashes and that downstream modules cite.

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 2447d4a661e92334753a8e1c6e3f04df86843d3399afe1ed1f2ac26814412213 | User settings for the run (dates, currency, pathway); not issuer evidence |

### Upstream handoffs

No handoff was supplied to this module; none was relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filed annual report, three quarterly reports and three earnings releases are sufficient for a credit snapshot of Nabors, with stated limitations. No source is blocked. Indentures, the credit agreement and rating reports are not in the pack. | Medium | Debt terms, guarantors and covenant definitions rest on filing summaries only; no executed legal documents or ratings are supplied, and the quarterly reports omit cash paid for interest and taxes. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The latest quarter is covered by the filed quarterly report and the earnings release, with prior-year and prior-quarter comparatives. | Supports current-period leverage, liquidity and cash flow work on the quarter ended September 30, 2026 against FY2025. | High |
| Debt is listed instrument by instrument, but the maturity table by year is printed only as of December 31, 2025, before the 2026 redemptions. | The maturity wall must be rebuilt from the instrument list, so refinancing timing depends on careful downstream work. | Medium |
| The Saudi joint venture and a special purpose acquisition company are consolidated, and the joint venture balance sheet is disclosed. | Consolidated cash and debt include a half-owned venture, so what creditors can reach has to be tested downstream. | Medium |
| The receivables sales facility, letters of credit and purchase commitments are described in the filings but sit outside reported debt. | These claims and liquidity uses need separate treatment from the debt total in later liquidity work. | Medium |
| The release states five Saudi rig suspensions and forward guidance that the filed quarterly report does not repeat. | These are management statements; the filed report governs wherever the two differ. | Medium |

### Readiness view

The effective source set can support the requested credit snapshot for Nabors Industries Ltd as of 2026-11-05, with bounded limitations; the source-level view is READY_WITH_LIMITATIONS for all four requested consumers (CP-1, CP-1A, CP-2, CP-5), and none is CONDITIONAL or BLOCKED. Identity and perimeter are largely resolved: the registrant, the borrower subsidiary, the consolidated joint venture and, through the exhibit index, the issuer entity of each outstanding note series are named in the filings, with one wording ambiguity on the 7.625% notes (see the entity map). The strongest contrary evidence is the absence of executed legal documents (indentures, credit agreement), of any rating-agency report, and of a Q4 2025 earnings release, together with the 10-Q omission of cash paid for interest and taxes. These limit how far debt terms, guarantor coverage, covenant definitions and cash interest can be verified from primary documents, but they do not stop the method from running. This is a statement of source sufficiency only; completion of any downstream analysis, normalization of quarters or acceptance of model inputs is not asserted (SOURCE_SUFFICIENCY_ONLY).

| Consumer | Source-readiness view | Command sheet | Governing limitation |
| --- | --- | --- | --- |
| CP-1 | READY_WITH_LIMITATIONS | RUN | Debt terms from filed notes only; year-end 2025 maturity table is stale; FY2025 consolidated adjusted EBITDA is not printed by that name in the annual report |
| CP-1A | READY_WITH_LIMITATIONS | RUN | Business and transaction facts come from the annual report and releases; no executed Parker or Quail Tools agreements; ownership and governance detail is limited to filing text |
| CP-2 | READY_WITH_LIMITATIONS | RUN | Inherits the CP-1 and CP-1A limitations; no ratings, quotes or peer data supplied in context |
| CP-5 | READY_WITH_LIMITATIONS | RUN | Trace checks are possible against seven pinned filings; extraction fidelity is not reviewed and tables are flattened to one cell per line |

### Source-by-source assessment

#### Annual report, fiscal year ended December 31, 2025 (10-K)

- Authority and perimeter: original filed audited annual report of Nabors Industries Ltd. and subsidiaries, consolidated. Items 1 to 16 and Notes 1 to 20 are present (Item 1 at page:4, Item 7 at page:57, Item 8 at page:75, Note 9 Debt at page:103, Note 12 Joint Ventures at page:111, Note 17 Segment Information at page:121, Note 19 Leases at page:126). This is the only audited source and the only source with a lease note, full-year supplemental cash flow information and a statement of exhibits.
- Coverage: debt by instrument and a principal maturity table as of December 31, 2025 (page:103); the covenant statement as of year-end (page:63); first-lien security description (page:30); lease position (page:127); cash paid for interest and income taxes for 2025, 2024 and 2023 (page:121).
- Limits: the text does not print a consolidated line named Adjusted EBITDA; the segment note prints total adjusted operating income and depreciation and amortization (page:122). No rating-agency ratings are printed. The exhibit index lists but does not contain the indentures and credit agreement (pages:135-136).

#### Quarterly reports on Form 10-Q (March 31, June 30 and September 30, 2026)

- Authority and perimeter: original filed unaudited interim reports on a consolidated basis, each prepared under interim reporting rules (the September report says it is to be read together with the 2025 annual report). They are separate, successive documents; none supersedes another. The September 30, 2026 report is the latest and carries the balance sheet, income statement, cash flow statement (nine months only), notes and management discussion.
- Coverage: the debt note by instrument (September 30 report page:15, March 31 report page:13, June 30 report page:13), the credit agreement terms and Joinder (page:15 to page:16 of the September report), covenant ratios at each quarter end (March 31 page:33, June 30 page:37, September 30 page:40), letter-of-credit facility availability (page:40 to page:41), the receivables purchase and sales agreements (page:14, page:41), purchase commitments (page:42), joint venture balance sheet (page:13) and segment information (page:24).
- Limits: cash flow statements are year-to-date, so discrete quarters other than the first need the releases or subtraction downstream; no lease note, no debt maturity table by year, and no cash paid for interest or income taxes were found in the three reports after a search for those terms and their variants (the only matches were an accounting-standard paragraph and investing-activity lines); no separate subsequent events note was found.

#### Earnings releases, Exhibit 99.1 (April 28, July 28 and October 27, 2026)

- Authority: issuer press releases furnished with Form 8-K; management attributed claims and non-GAAP measures with reconciliations. They do not override the filed reports.
- Coverage: adjusted EBITDA, adjusted operating income and adjusted free cash flow with reconciliations to net income and to operating cash flow (October release page:9 to page:12); net debt reconciliation (page:11 of each release); segment results and rig activity (October release page:6 to page:7); outlook and guidance (October release page:3 to page:4); condensed income statement and balance sheet (page:5 to page:6).
- Limits: the releases are unaudited, the guidance cannot be reconciled by the issuer ("We do not provide a forward-looking reconciliation"), and the October release presents a Quail Tools carve-out for the prior-year quarter only. The pack holds no presentation deck; its retrieval record lists these releases in place of decks.

### Entity and perimeter map

| Role | Entity as named in the sources | Where stated |
| --- | --- | --- |
| Registrant, consolidated reporting entity | Nabors Industries Ltd. (Bermuda) | September 2026 report page:1 |
| Credit agreement borrower | Nabors Industries, Inc. ("Nabors Delaware"), wholly owned subsidiary; Nabors Industries Ltd. is Holdings | September 2026 report page:6 and page:15; 10-K page:136 |
| Issuer of the exchangeable, 9.125%, 8.875% and 7.625% notes per the exhibit index | Nabors Industries, Inc. | 10-K page:135 and page:136 |
| Issuer of the 7.625% notes per the debt note | Described as issued by "Nabors", guaranteed by Nabors and certain indirect wholly owned subsidiaries; the exhibit index names Nabors Industries, Inc., so the issuing entity wording is unresolved | 10-K page:104 |
| Guarantors | Named only for the 2020 indenture in the exhibit index; otherwise "the guarantors party thereto" | 10-K page:135 |
| Consolidated joint venture (VIE) | SANAD, equally owned by Saudi Aramco and Nabors | September 2026 report page:12 |
| Consolidated special purpose acquisition company (VIE) | Nabors Energy Transition Corp. II | September 2026 report page:29 |
| Acquired / sold businesses | Parker Drilling Company (acquired March 11, 2025); Quail Tools (sold August 20, 2025) | September 2026 report page:8 |
| Parent, sponsor, restricted/unrestricted group | None supplied; the issuer is a listed company with no sponsor; no restricted or unrestricted designation appears in the sources | context; unresolved |

### Coverage by objective

| Evidence needed | Located in | Status |
| --- | --- | --- |
| Discrete quarters 2026 and prior-year comparatives | Three releases (quarterly columns) and three 10-Qs | Retained; Q4 2025 only as a comparative column in the first-quarter release |
| Fiscal years | 10-K (FY2025, FY2024, FY2023 segment and cash flow data) | Retained |
| Quarter versus year-to-date distinctions | 10-Qs present three-month and year-to-date columns; cash flow is year-to-date | Retained; discrete-quarter cash flow only from release reconciliations |
| Segments and KPIs (rigs working, daily margin) | Releases and 10-K / 10-Q segment notes | Retained |
| Add-backs and non-GAAP reconciliation | Releases | Retained; issuer definitions only |
| Facility-level debt and carrying values | 10-K page:103, 10-Q Note 6 and fair value note (September report page:19) | Retained; instrument-level terms beyond the note are a gap |
| Cash paid for interest and tax | 10-K page:121 for FY2025 only | Gap for interim 2026 |
| Business and transaction narrative | 10-K Item 1 and 7, 10-Q Note 3, releases | Retained; executed transaction documents not supplied |

### Source-quality and version relationships

- Three 10-Qs, three releases and one 10-K are distinct documents for distinct periods. No source is a duplicate of another; none is draft; all are filed or furnished and unaudited except the 10-K.
- Overlap: each release repeats statements that the matching 10-Q also files. The 10-Q controls the fact; the release is an attributed management presentation. This module does not reconcile the two.
- Basis difference to carry forward: the release net debt reconciliation takes total debt after deferred financing costs, while the debt note also lists principal amounts before those costs. Downstream modules must state which basis they use.
- Basis difference to carry forward: the release adjusted free cash flow uses capital expenditures net of proceeds from asset sales, while the cash flow statement lists capital expenditures and asset sale proceeds on separate lines.
- Conflict between 10-K sections: the debt note describes the exchangeable notes as due June 2029 (10-K page:103), while the exhibit index describes the indenture as for 1.750% Senior Exchangeable Notes "due 2027" (10-K page:135). The debt note, being the audited disclosure, controls; the exhibit-index title is an unresolved wording inconsistency that affects only CP-1 maturity work and CP-5 trace checks.
- Version relationship: the 10-K states that the 2024 credit agreement matures on a trigger tied to the 7.50% notes or the exchangeable notes (10-K page:62 and page:106); the September 2026 report states only the exchangeable-note trigger, consistent with the 7.50% notes having been redeemed. Both are retained as dated statements.
- Extraction: the text is a flattened render; in the 10-Qs most table cells are on separate lines, so column alignment is inferred. Extraction success is not a fidelity review, and no image, chart or speaker-note content exists in the pack.

### Evidence register

| Ref | Source | Locator | Quote |
| --- | --- | --- | --- |
| E1 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:6 | References in this report to “Nabors Delaware” mean Nabors Industries, Inc., a wholly owned subsidiary of Nabors. |
| E2 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:15 | On June 17, 2024, Nabors Delaware amended and restated its existing credit agreement |
| E3 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:40 | which were 5.20:1.00 and 99.8%, respectively, as of September 30, 2026 |
| E4 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:40 | We had seven letter-of-credit facilities with various banks as of September 30, 2026. |
| E5 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:42 | Purchase commitments outstanding at September 30, 2026 totaled approximately $296.4 million |
| E6 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:12 | SANAD is equally owned by Saudi Aramco and Nabors. |
| E7 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:16 | As of September 30, 2026, we had no borrowings and $68.2 million of letters of credit outstanding under our 2024 Credit Agreement. |
| E8 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:41 | The maximum purchase commitment of the Purchasers under the A/R Agreements is $250.0 million |
| E9 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:15 | We also redeemed $100.0 million of the 9.125% senior priority guaranteed notes due January 2030 |
| E10 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:41 | Our largest customer in Mexico has a history of making late payments |
| E11 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:33 | More recently, certain operators have taken measures to reduce near-term activity |
| E12 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:40 | The major U.S. credit rating agencies have previously downgraded our senior unsecured debt rating to non-investment grade. |
| E13 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:30 | The 2024 Credit Agreement (as defined below) is secured with a first lien security interest on all land drilling rigs and related equipment, spare parts and inventory in the contiguous United States. |
| E14 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:135 | Nabors Industries, Inc.’s 1.750% Senior Exchangeable Notes due 2027 |
| E15 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:103 | As of December 31, 2025, the principal amount and maturities of our primary debt for each of the five years following 2025 and thereafter are as follows: |
| E16 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:104 | which are fully and unconditionally guaranteed by Nabors and certain of Nabors’ indirect wholly-owned subsidiaries |
| E17 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:63 | which were 4.16:1.00 and 99.8%, respectively, as of December 31, 2025 |
| E18 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:121 | Cash paid for interest, net of capitalized interest |
| E19 | 10-Q_2026-03-31_nbr-20260331x10q.htm.jsonl | page:33 | which were 4.40:1.00 and 99.8%, respectively, as of March 31, 2026 |
| E20 | 10-Q_2026-06-30_nbr-20260630x10q.htm.jsonl | page:37 | which were 4.69:1.00 and 99.8%, respectively, as of June 30, 2026 |
| E21 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:2 | despite a lower SANAD rig count following the suspension of five rigs |
| E22 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:11 | RECONCILIATION OF NET DEBT TO TOTAL DEBT |
| E23 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:4 | Adjusted EBITDA is computed similarly, but also excludes depreciation and amortization expenses. |
| E24 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:1 | The quarter ended September 30, 2025 includes revenue of $34 million, EBITDA of $20 million, and operating income of $14 million from Quail Tools, which was sold in August 2025. |
| E25 | EX-99.1_2026-04-28_tm2612942d1_ex99-1.htm.jsonl | page:1 | The Company’s next debt maturity is $250 million due in 2029. |
| E26 | EX-99.1_2026-07-28_tm2621313d2_ex99-1.htm.jsonl | page:2 | extended the duration of our contract backlog |
| E28 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:135 | Nabors Global Holdings Limited, as Guarantor |
| E29 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:136 | Nabors Industries, Inc., as Issuer, the guarantors party thereto |
| E27 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:5 | We do not provide a forward-looking reconciliation of our outlook for Segment Adjusted EBITDA |

### Consumer assessments

#### CP-1 (canonical financial data)

Evidence: the debt note lists each series with its balance (September 2026 report page:15), the credit agreement has dated terms, a covenant ratio is reported each quarter end (E3, E19, E20, E17), and letter-of-credit facility availability is tabulated (E4). Risk mechanism: the maturity table by year exists only as of year-end 2025 (E15), before the January 2026 redemption of the 7.50% notes (10-K page:103) and the redemption of part of the 9.125% notes (E9; the October release places it in the third quarter), so a maturity wall copied from it would misstate refinancing timing. FY2025 consolidated adjusted EBITDA is not printed under that name in the annual report, which limits a like-for-like LTM build to the release period columns and the segment note, and the adjusted EBITDA definition is the issuer's own (E23). Consequence: CP-1 can run, must rebuild the maturity profile from the instrument list, must state the debt basis it uses (principal versus carrying value), and must label cash interest as FY2025 only. Verdict: READY_WITH_LIMITATIONS.

#### CP-1A (business and transaction context)

Evidence: Item 1 of the annual report, Notes 3 and 4 of the 10-Qs, and three releases describe the Parker acquisition, the Quail Tools sale (E24), SANAD (E6) and segment structure. Risk mechanism: only filing descriptions exist for these transactions, with no executed merger or sale agreements, so deal terms and any creditor-relevant covenants of those documents cannot be checked; the release statement on rig suspensions (E21) is management language and the 10-Q only speaks of suspension notices in general (E11). Governance and ownership detail is limited to what the filings state; no sponsor exists in context. Consequence: CP-1A can run and must tag management statements as such. Verdict: READY_WITH_LIMITATIONS.

#### CP-2 (fundamental credit synthesis)

Evidence: CP-2 consumes only upstream CP-1 and CP-1A registers, so its source need is the sum of theirs. Risk mechanism: the absence of ratings in context and sources beyond a statement of past downgrade to non-investment grade (E12), of peer data and of executed legal terms narrows what it can say on recovery and relative position. Consequence: CP-2 can run if CP-1 and CP-1A are settled; the dependency planner orders it, and its gaps ledger should carry the items below. Verdict: READY_WITH_LIMITATIONS.

#### CP-5 (evidence trace validator)

Evidence: all quotes and figures can be matched to seven pinned filings, and the same fact appears in both a release and a 10-Q for each quarter. Risk mechanism: the overlap is where cross-module identity can fail (principal versus carrying debt; gross versus net capital expenditures; the 2027 versus 2029 exchangeable-note wording at E14). Consequence: CP-5 can run; it should treat the 10-Q as controlling over the release and flag basis differences instead of treating them as errors. Verdict: READY_WITH_LIMITATIONS.

### Reasoning chain for the main limitation

Evidence: the exhibit index lists indentures, with guarantors named only for one 2020 indenture (E28) and as "the guarantors party thereto" for the others (E29). Source risk mechanism: the guarantor set of the priority guaranteed notes, which the debt note calls "certain of Nabors’ indirect wholly-owned subsidiaries" (E16), and the covenant definitions behind the reported ratio (E3) are not readable from primary documents, so structural ranking and covenant headroom depend on management summaries. Downstream consequence: CP-1 can report the reported ratio and its stated minimum, but cannot recompute the covenant definition of EBITDA, and CP-2 must hold structural-priority conclusions as limited.

## Calculations

No financial figure was calculated, normalized or reconciled in this module, as the method requires. The only counts are page counts of the retained extractions, taken from the pack:

| Item | Inputs | Result |
| --- | --- | --- |
| Pages retained across the seven issuer sources | 143 + 40 + 44 + 46 + 11 + 12 + 12 | 308 of 308 pages present in the extraction |
| Quarterly reports present | March 31, 2026; June 30, 2026; September 30, 2026 | 3 of 3 expected for the latest three quarters |
| Earnings releases present | April 28, 2026; July 28, 2026; October 27, 2026 | 3 of 3 expected for the latest three quarters |

Retained means present in the extraction; it does not mean each page was individually read for this module. Pages read for this review were the cover, statements, debt, joint venture, receivables, liquidity, covenant, commitments, segment and exhibit-index pages cited above, the full October release, and the main parts of each other source named in the assessment.

## Gaps

| ID | Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | Executed indentures and the 2024 Credit Agreement are not in the pack (the context sets legal documents to none); guarantor names, covenant definitions and call terms rest on filing summaries | Medium | CP-1, CP-2, CP-5 | Add the indentures and credit agreement from the exhibit index if a legal-structure review is required |
| G2 | No rating-agency report or rating in context; the filings only state a past downgrade to non-investment grade | Medium | CP-2 | Supply current ratings if a rating view is needed |
| G3 | The year-by-year debt maturity table is printed only as of December 31, 2025; no later table found | Medium | CP-1 | Rebuild from the instrument list in the debt note |
| G4 | Cash paid for interest and income taxes is printed for FY2025 only; not found in the three 10-Qs after searching "paid for", "interest paid", "taxes paid" and "supplemental cash" | Medium | CP-1 | Use FY2025 figure labelled as such; interest expense is a different measure |
| G5 | The 10-K does not print consolidated Adjusted EBITDA by name; FY2025 consolidated adjusted EBITDA needs the segment note or release columns; no fourth-quarter 2025 release is in the pack | Medium | CP-1 | Use the release columns and label the basis; request the fourth-quarter 2025 release if needed |
| G6 | The covenant EBITDA definition is not in the pack; the reported ratio cannot be recomputed | Medium | CP-1, CP-2 | Add the credit agreement |
| G7 | Exhibit index wording "due 2027" conflicts with the debt note "due June 2029" for the exchangeable notes | Low | CP-1, CP-5 | Treat the debt note as controlling; confirm in the indenture if added |
| G8 | Release-only statements (five Saudi rig suspensions, guidance, run-rate claims) are not in the filed 10-Q | Low | CP-1A, CP-2, CP-5 | Carry as management language |
| G9 | No executed Parker merger or Quail Tools sale agreement | Low | CP-1A | Not needed for a snapshot; add for transaction review |
| G10 | Extraction fidelity not reviewed; tables flattened; no images or charts | Low | All | Spot-check key tables against the original filings |
| G11 | Parent, sponsor, restricted group and guarantor designations are blank in context | Low | CP-1A, CP-2 | Leave as not supplied |
| G12 | Part of the 10-K (risk factors and governance items) was not read page by page in this module | Low | CP-1A | CP-1A reads the pages it needs |

## Next module

The next module is CP-1, which can run on the retained sources. It should start with the September 30, 2026 quarterly report and the October 27, 2026 release, label every figure Q3 2026, nine months 2026 or FY2025, rebuild the maturity profile from the instrument list rather than the year-end 2025 table, state the debt basis it uses, treat cash interest as FY2025 only, and carry G1 to G7 forward. CP-1A, CP-2 and CP-5 follow in the planner's order, and each should carry these limitations. Command sheet: CP-1 RUN, CP-1A RUN, CP-2 RUN, CP-5 RUN; no consumer is DO NOT RUN.
