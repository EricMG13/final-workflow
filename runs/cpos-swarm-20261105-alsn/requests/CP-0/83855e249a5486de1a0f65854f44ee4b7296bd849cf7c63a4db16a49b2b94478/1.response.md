## Request

Issuer: Allison Transmission Holdings Inc (issuer id alsn, NYSE: ALSN), as of 2026-11-05. Evidence cutoff 2026-11-05. Pathway credit_snapshot, case kind public, current period q3-2026, prior period fy-2025, reporting currency USD (the filings report in US dollars millions, so no currency mismatch with the run context). The context names no borrower, parent, guarantors, ratings, quotes, deal terms or legal documents; those context fields are blank and are not read as zero or as absence in the filings.

Question this module answers: can the supplied source set support the downstream work (CP-1 financial base, CP-1A business and transaction context, CP-2 credit synthesis, CP-5 evidence trace and QA), and what remains blocked? This is a source-sufficiency assessment only. It gives no credit conclusion, performs no normalization or reconciliation of financials, and does not evaluate any downstream input contract (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

Locator convention: S1 to S7 are the sources listed below; `page:N` is the source chunk number in the extracted text, not the printed page. Quotes are exact substrings of the retained page text with line breaks collapsed to single spaces.

## Sources

### Issuer sources relied on

| Id | Exact name | sha256 (pinned file) | Document family and authority | Period or date covered |
| --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_alsn-20251231.htm.jsonl | 4759ff666c33cf9b4aa9fc9af406b5ff948ca8c7e8b83ef1d1b8c3371ee474c1 | Annual report on Form 10-K; filed statements, audited; controlling for FY2025 and earlier facts | Fiscal year ended 2025-12-31 |
| S2 | 10-Q_2026-03-31_alsn-20260331.htm.jsonl | be0a328aec24e49cdf0300569cba1bccab7cce3c7f95d5658c5db76418cb7b3d | Quarterly report on Form 10-Q; filed, unaudited interim statements | Quarter ended 2026-03-31 |
| S3 | 10-Q_2026-06-30_alsn-20260630.htm.jsonl | 0d35855e179d244457d2146b580b35b12b14abea216ea0bdfab3dfa942713609 | Quarterly report on Form 10-Q; filed, unaudited interim statements | Quarter and six months ended 2026-06-30 |
| S4 | 10-Q_2026-09-30_alsn-20260930.htm.jsonl | 45fe422f6a742d85a38f1278f190cb497541b353ed938208d565068e9ab989b0 | Quarterly report on Form 10-Q; filed, unaudited interim statements; latest filed statements | Quarter and nine months ended 2026-09-30 |
| S5 | EX-99.1_2026-05-04_d138525dex991.htm.jsonl | fe207b266e861065ca33402f15b822e8bf63e3f1f6c76c7ba33719a7889867e5 | Earnings release (Exhibit 99.1); management narrative and non-GAAP figures, supporting only | First quarter 2026, dated 2026-05-04 |
| S6 | EX-99.1_2026-08-03_d95413dex991.htm.jsonl | 351a085e364488314b64d2b881181e5b5b95879fe010b71d75af6ac7e45fdd04 | Earnings release (Exhibit 99.1); management narrative and non-GAAP figures, supporting only | Second quarter 2026, dated 2026-08-03 |
| S7 | EX-99.1_2026-11-02_d187329dex991.htm.jsonl | b8087f0341293bcafb0ca28c8fc71ee181a5c666b45fe74a0ca9cfe109b0ba65 | Earnings release (Exhibit 99.1); management narrative and non-GAAP figures, supporting only | Third quarter 2026, dated 2026-11-02 |

### Run settings (not issuer evidence)

| Item | sha256 | Use |
| --- | --- | --- |
| context file 1411207-allison-transmission-holdings-inc-alsn.json | f65312705cd8bb204fde9755509326ba975099b166b8d246c949fcd0ea955b5a | Dated run settings only; read for as-of date, periods, currency and identity fields |

The pack also holds `_retrieval.json`, which CP-OS ignores as a source. It is external pack metadata (retrieval manifest), not issuer evidence. Where this handoff uses it for a filing date or for the absence of presentations, the text says so.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| None | CP-0 is the first module in the run; CP-OS supplied no upstream handoff, so there is no handoff hash to list |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed documents are enough for a bounded credit snapshot of Allison Transmission Holdings through the quarter ended 2026-09-30. Debt, liquidity, covenant and acquisition facts are all present in filed text. | High | No credit agreement, indentures or acquired-business history are supplied, so legal terms and a combined trailing view rest on filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The third quarter 10-Q is the latest filed statement and carries the full debt table, revolver availability and the first lien net leverage ratio. | Current debt, liquidity and covenant headroom can be taken from one filed source. | High |
| The Dana off-highway acquisition closed on 2026-01-01, so 2026 results include it and the 2025 annual figures do not. | Trailing metrics that mix 2025 and 2026 periods blend two business perimeters and must be labelled. | High |
| The annual report gives a preliminary acquisition price of $2,732 million, while the later quarterly reports give $2,628 million. | The later filed figure should be used for the transaction, with the earlier one shown as superseded. | High |
| Debt is reported as $4,037 million in the debt note and $4,012 million in the release. | The two measures differ by deferred financing costs; analysts must name which one they use. | High |
| Legal documents are absent, and the guarantor wording in the notes is hard to reconcile. | Covenant definitions, baskets and the guarantee package cannot be verified from source documents. | Medium |

### Readiness view

The effective source set supports the requested credit snapshot with limitations. All seven filed sources are retained: the annual report, the three quarterly reports and the three earnings releases, with every page of text extracted and no blocked preparation. The filings are the controlling authority; the releases are management attributions and are used only as supporting claims. The entity boundary resolves in the filings: Allison Transmission Holdings, Inc. is the registrant and consolidated reporter, and Allison Transmission, Inc. (ATI), its wholly-owned subsidiary, is the issuer of the senior notes and the borrower under the credit facility. Readiness for each consumer is READY_WITH_LIMITATIONS. No consumer is CONDITIONAL or BLOCKED, because no required source for the consumer's own method is missing. The binding limitations are: no executed legal documents (credit agreement, amendments, indentures); no pro forma or pre-acquisition financials for the acquired business; the annual figures predate the acquisition and use one segment; no maturity schedule by year after the January 2026 amendment; and an unresolved guarantor roster. These bound what downstream modules may conclude; they do not stop them from running.

### Consumer readiness

| Consumer | Status | Usable evidence | Limitation carried forward | Next evidence action |
| --- | --- | --- | --- | --- |
| CP-1 financial base (leverage, interest cover, liquidity, debt maturities, financials table) | READY_WITH_LIMITATIONS | Balance sheet, income statement and cash flow in S4 page:2 and page:3; debt table S4 page:19; revolver S4 page:21; annual EBITDA bridge S1 page:117; nine-month EBITDA reconciliation S4 page:41; cash interest paid in S1 page:81 and S4 page:3 | Trailing periods mix the pre-acquisition and post-acquisition perimeter; debt maturity by year exists only for 2025 year-end (S1 page:101), so later years must be built from instrument maturities in S4 page:19 and page:21 | CP-1 labels perimeter on every trailing figure and states which debt measure it uses |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Acquisition terms and purchase price allocation S4 page:5 to page:9; financing of the acquisition S4 page:6; segments S4 page:29 and page:30; business description S1 page:5 to page:12 | No executed purchase agreement or financing documents; ownership beyond the listed-equity facts is not in the context; purchase price figure differs between S1 and S4 | CP-1A uses the later quarterly figure and records the earlier one as superseded |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Draws only on CP-1 and CP-1A handoffs, which have sufficient source evidence | Inherits the limitations above; no ratings in the context, so agency ratings come only from S4 page:46 | None at source level; the dependency planner sequences CP-2 after CP-1 and CP-1A |
| CP-5 evidence trace and QA | READY_WITH_LIMITATIONS | Every source is retained with page locators and hashes | Quality depends on the upstream handoffs; extraction is text only | None at source level; CP-5 checks the handoffs against the sources |

### Source-by-source assessment

| Id | Identity and perimeter | Period and basis | Exact quote supporting the assessment | Locator | Limitation |
| --- | --- | --- | --- | --- | --- |
| S1 | Allison Transmission Holdings, Inc., consolidated, Commission File Number 001-35456 | FY2025 audited; one reportable segment; the acquisition is a subsequent event | "The Company’s one reportable segment as of December 31, 2025 was the same as its consolidated financial results" | S1 page:117 | Does not include the acquired business; FY2025 not recast for two segments |
| S2 | Same registrant, consolidated | Three months ended 2026-03-31, unaudited | "For the quarterly period ended March 31, 2026" | S2 page:1 | Superseded for balances by S3 and S4; retained for the quarter's own facts |
| S3 | Same registrant, consolidated | Three and six months ended 2026-06-30, unaudited | "For the quarterly period ended June 30, 2026" | S3 page:1 | Superseded for balances by S4; retained for the quarter's own facts |
| S4 | Same registrant, consolidated; debt issuer is ATI | Three and nine months ended 2026-09-30, unaudited; balance sheet also at 2025-12-31 | "For the quarterly period ended September 30, 2026" | S4 page:1 | Purchase accounting is preliminary and the 10-Q shows measurement period adjustments |
| S5 | Registrant, consolidated, plus segment commentary | First quarter 2026, management and non-GAAP | "Adjusted EBITDA of $362 million" | S5 page:1 | Management claim; the 10-Q reconciliation controls |
| S6 | Registrant, consolidated, plus segment commentary | Second quarter 2026, management and non-GAAP | "Adjusted EBITDA of $404 million" | S6 page:1 | Management claim; the 10-Q reconciliation controls |
| S7 | Registrant, consolidated, plus segment commentary | Third quarter 2026, management and non-GAAP, with full-year guidance | "Adjusted EBITDA of $400 million, up 56% year over year, 26.1% of Net Sales" | S7 page:1 | Guidance is a management forward-looking statement, not a filed fact |

### Entity and instrument roles

| Role | Entity or instrument | Quote | Locator |
| --- | --- | --- | --- |
| Registrant and consolidated reporter | Allison Transmission Holdings, Inc. | "ALLISON TRANSMISSION HOLDINGS, INC." | S4 page:1 |
| Issuer of notes and borrower | Allison Transmission, Inc. (ATI), wholly-owned subsidiary | "the Company’s wholly-owned subsidiary" | S1 page:102 |
| Secured facilities | Term Loan due 2031, Incremental Term Loan due 2033 and Revolving Credit Facility due 2031, under the Second Amended and Restated Credit Agreement | "collateralized by a lien on substantially all assets of the Company, ATI and certain existing and future U.S. subsidiary guarantors, as provided in the Credit Agreement" | S4 page:20 |
| Unsecured notes | 4.75% due 2027, 5.875% due 2029, 3.75% due 2031 and 5.875% due 2033 senior notes | "Each series of the Senior Notes is unsecured" | S4 page:22 |
| Guarantors | Unresolved: the notes text says none of ATI's domestic subsidiaries currently guarantee the facility | "None of ATI’s domestic subsidiaries currently guarantee its obligations under the Senior Secured Credit Facility" | S4 page:22 |
| Parent-only view | Holdings has no cash and holds only its investment in subsidiaries | "Investments in and advances to subsidiaries" | S1 page:119 |

### Conflicts and version relationships

| Topic | Source A | Source B | Treatment and downstream effect |
| --- | --- | --- | --- |
| Acquisition purchase price (Dana Incorporated off-highway business, closed 2026-01-01, S4 page:5) | S1 page:118: "for a purchase price of approximately $2,732 million" | S4 page:7: "a final purchase price of $2,628 million" (S4 page:5 repeats the figure as approximately that amount) | Different dates and a measurement-period change; the quarterly filing postdates the annual report and is used for the transaction. CP-1A must show $2,732 million as the earlier preliminary estimate. The pack does not reconcile the two beyond the S4 page:7 adjustment text |
| Total debt measure | S4 page:19: "Total long-term debt $ 4,037 $ 2,909" | S7 page:3: "total debt of $4,012 million and net debt of $3,515 million" | Not a conflict in fact: the note total includes $38 million of finance lease liabilities and is before $25 million of deferred financing costs; the release figure equals the balance sheet current plus long-term debt. CP-1 must name the measure, and net debt must use the same measure as gross debt |
| First lien net leverage ratio | S1 page:103: "achieving a (0.87x) ratio" at 2025-12-31 | S4 page:22: "achieving a 0.84x ratio" at 2026-09-30 | The ratio is the credit agreement definition, which the pack does not contain; it cannot be reproduced from statements. CP-1 must not treat it as equal to a net debt over EBITDA metric it computes |
| Segment basis | S1 page:117: one reportable segment at FY2025 | S4 page:29: "changed its segment structure from one operating and reportable segment to two operating and reportable segments" | 2025 quarterly segment data are recast in S4 page:30, but FY2025 annual segment data are not. Segment trends across FY2025 and 2026 need a basis label |
| Revolver size and maturity | S1 page:47: commitments of $750 million due March 2029 at 2025-12-31 | S4 page:19 and page:21: commitments of $1,000 million due January 2031 | Version relationship, not a conflict: Amendment No. 5 (January 2026) changed the facility (S1 page:119, S4 page:20). Amendment No. 6 (June 2026) lowered the Term Loan margin (S4 page:20). The agreement and amendments are not in the pack |

### Coverage ledger

| Id | Pages of extracted text retained | Statements, notes and tables located | Extraction caveat |
| --- | --- | --- | --- |
| S1 | 129 of 129 pages | Balance sheet, income statement, cash flows and equity statement S1 page:79 to page:81; Notes 1 to 25 from page:82; Schedule I at page:119 and page:120; exhibit index page:125 to page:129 | Tables are flattened text; no fidelity review against the original HTML |
| S2 | 46 of 46 pages | Balance sheet, income statement and cash flows S2 page:2 and page:3; equity statement to page:4; Notes A to S from page:4; MD&A from page:25 | Same |
| S3 | 52 of 52 pages | Balance sheet, income statement and cash flows S3 page:2 and page:3; equity statement to page:4; Notes A to T from page:4; MD&A from page:28 | Same |
| S4 | 54 of 54 pages | Balance sheet, income statement and cash flows S4 page:2 and page:3; equity statement to page:4; Notes A to T from page:4; MD&A from page:30 | Same |
| S5 | 11 of 11 pages | Release text with financial tables | Same; any chart or image in the original release is not covered by text extraction |
| S6 | 12 of 12 pages | Same | Same |
| S7 | 12 of 12 pages | Same | Same |

### Evidence located for downstream demands

| Demand | Located evidence | Quote | Locator |
| --- | --- | --- | --- |
| Cash | Cash and equivalents at 2026-09-30 | "Cash and cash equivalents $ 497 $ 1,495" | S4 page:2 |
| Undrawn facility | Revolver availability net of letters of credit | "As of September 30, 2026, the Company had $996 million available under the Revolving Credit Facility, net of $4 million in letters of credit." | S4 page:21 |
| Covenant | Maintenance test, level and reported figure | "specified maximum first lien net leverage ratio of 5.50x" | S4 page:22 |
| Debt by instrument | Seven lines in the debt note | "Total long-term debt $ 4,037 $ 2,909" | S4 page:19 |
| Redemption in the quarter | Partial redemption of the 2027 notes | "In September 2026, the Company made a $100 million redemption payment on the 4.75% Senior Notes." | S4 page:22 |
| Cash interest | Nine-month interest paid | "Interest paid $ (152 ) $ (87 )" | S4 page:3 |
| FY2025 cash interest | Full-year interest paid | "Interest paid $ (120 ) $ (124 ) $ (131 )" | S1 page:81 |
| Nine-month EBITDA | Adjusted EBITDA reconciliation | "Adjusted EBITDA (Non-GAAP) $ 400 $ 256 $ 1,166 $ 865" | S4 page:41 |
| FY2025 EBITDA | Annual Adjusted EBITDA | "Adjusted EBITDA $ 1,130 $ 1,165 $ 1,108" | S1 page:117 |
| Maturity table (2025 year-end) | Five-year principal schedule, before the January 2026 incremental term loan | "Principal payments required on long-term debt during the next five years are as follows" | S1 page:101 |
| Ratings | Moody's and Fitch corporate ratings at 2026-09-30 | "Corporate Credit Ba1 BB+" | S4 page:46 |
| Pension and retiree medical | Unfunded status at 2025-12-31 | "the unfunded status of our defined benefit pension plans was $4 million and the unfunded status of our OPEB plan was $66 million" | S1 page:50 |
| Leases | Lease payment table at 2026-09-30 | "Total lease payments 107 49" | S4 page:25 |
| Foreign cash | Cash held by foreign subsidiaries | "the total of cash held by foreign subsidiaries was $361 million" | S4 page:44 |
| Subsequent events and cutoff | Latest dated source content is 2026-11-04 (10-Q signature date, S4 page:54); latest release is 2026-11-02; share count as of 2026-10-22 | "As of October 22, 2026, there were 82,133,940 shares of common stock outstanding." | S4 page:1 |

## Calculations

CP-0 forbids normalizing, reconciling or calculating financial figures, so no leverage, coverage, liquidity or trailing metric is computed here. The only arithmetic below ties printed figures to each other to explain conflicts; every input is a printed figure in US$ millions.

| Check | Inputs and locators | Result |
| --- | --- | --- |
| Debt note total | 300 + 500 + 1,000 + 505 + 500 + 1,194 + 38, from the debt table S4 page:19 | 4,037, equal to the printed total |
| Release debt measure | 4,037 less deferred financing costs 25 (S4 page:19) | 4,012, equal to the release figure in S7 page:3 |
| Balance sheet debt | Current portion of long-term debt 20 plus long-term debt 3,992 (S4 page:2) | 4,012, equal to the release figure |
| Release net debt | 4,012 less cash 497 (S4 page:2) | 3,515, equal to the release figure in S7 page:3 |
| Revolver availability | Commitments 1,000 less letters of credit 4, no loans outstanding (S4 page:21) | 996, equal to the printed availability |
| Segment sales | Allison Transmission 881 plus Allison Off-Highway 653 (S4 page:30) | 1,534, equal to consolidated net sales for the third quarter of 2026 |
| Nine-month adjusted EBITDA | 362 (S5 page:1) plus 404 (S6 page:1) plus 400 (S7 page:1) | 1,166, equal to the nine-month figure in S4 page:41 |
| Coverage counts | Retained pages over total pages per source, as in the coverage ledger | 129 of 129; 46 of 46; 52 of 52; 54 of 54; 11 of 11; 12 of 12; 12 of 12 |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed legal documents are not supplied: the Second Amended and Restated Credit Agreement and Amendments No. 5 and No. 6, and the four note indentures. The context records legal documents as none. Terms come only from filing descriptions. The exhibit index lists earlier amendments, for example "Amendment No. 4 to Credit Agreement, dated March 13, 2024" (S1 page:126) | Medium | CP-1, CP-1A, CP-2 | Obtain the agreement, amendments and indentures; until then covenant definitions, baskets, restricted payment capacity and excess cash flow terms are Not supplied |
| Guarantor roster unresolved: S4 page:20 refers to "existing and future U.S. subsidiary guarantors" while S4 page:22 says none of ATI's domestic subsidiaries currently guarantee the facility or the notes | Medium | CP-1A, CP-2 | Resolve against the credit agreement and indentures; until then do not state a guarantor list |
| No pro forma, carve-out or pre-acquisition financials for the acquired business. A search of all seven sources for pro forma disclosure found none. FY2025 annual results exclude the acquired business | High for trailing metrics | CP-1, CP-2 | CP-1 labels perimeter on every trailing figure; a combined trailing EBITDA is Not calculable from the pack |
| No year-by-year debt maturity schedule after the January 2026 incremental term loan; the only schedule is at 2025-12-31 (S1 page:101) | Low | CP-1 | Build maturities from instrument maturity dates and minimum amortization in S4 page:19 to page:21 and label it as constructed |
| Quarterly presentations are not supplied; the retrieval manifest records releases in their place for all three quarters (external pack metadata) | Low | CP-1A | Earnings releases are used as attributed management claims |
| Purchase accounting is preliminary: "The preliminary fair values of the assets acquired and liabilities assumed in the Acquisition are subject to further change" (S4 page:8); the internal control report for FY2026 will exclude the acquired business (S4 page:53) | Medium | CP-1A, CP-2 | Treat goodwill, intangibles and acquired balances as provisional |
| Text extraction only: charts, images and original HTML layout are not inspected, and extraction is not a fidelity review | Low | All | CP-5 compares handoff figures with the page text |
| Context supplies no ratings, quotes, valuation inputs or sponsor; agency ratings appear only in S4 page:46 | Low | CP-2 | Treat market and valuation inputs as Not supplied |
| Filing dates come from the retrieval manifest, which is external pack metadata; the filing text shows the 10-Q signature date of 2026-11-04 (S4 page:54) | Low | All | None needed; no source is dated after the 2026-11-05 cutoff |

## Next module

CP-1, the financial base. Carry forward: use S4 as the latest filed statements; name the debt measure ($4,037 million note total or $4,012 million balance sheet and release measure) beside every leverage figure; label the perimeter of every trailing period (the acquired business is in 2026 and not in FY2025); treat the reported first lien net leverage ratio of 0.84x as the credit agreement definition, not a computed metric; and build the maturity chart from instrument dates, labelled as constructed.
