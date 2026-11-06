## Request

Issuer: Uniti Group Inc. (issuer id unit; Nasdaq ticker UNIT; Delaware registrant, SEC file number 001-42779, page:1 of the Q2 2026 10-Q). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, with the filings stating amounts in millions. Current period named by the context: Q2 2026 (quarter ended 2026-06-30). Prior period named by the context: FY2025.

Question for this module: can the supplied source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion. It does not normalize, reconcile or calculate figures. Arithmetic below is limited to tie-outs that test source consistency. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

The context file holds run settings and is not issuer evidence. Its deal terms, quotes, ratings, peers, precedents and research questions are empty, and it lists no borrower, parent or guarantor. Those blanks are treated as not supplied, never as zero or as absence.

## Sources

Each issuer file is one JSONL text extraction of an SEC filing. The locator `page:N` is the extraction chunk, not the printed page. The sha256 below is the pinned file hash; each file's first line prints a different hash for the underlying htm document, which is not used here.

### Issuer sources relied on

| Source name | sha256 | Document family, authority and chunks | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_unit-20251231.htm.jsonl | 6d67619ba1ab3647c20a79710ac6373101e1f3efd1454ad58308edf1101a7a6b | Audited annual report, Form 10-K, 222 chunks; filed audited statements control their facts | Fiscal year ended 2025-12-31; Old Uniti is the accounting acquirer, so FY2025 holds Windstream only from 2025-08-01 (10-Q Q2 2026 page:11, page:19; 10-K page:95-96) |
| 10-Q_2025-09-30_unit-20250930.htm.jsonl | 5887e391d2d0fd28ff7625b79ed82dcf62027435a26c54f6cbb097f48f8f2e90 | Unaudited quarterly report, Form 10-Q, 148 chunks | Quarter and nine months ended 2025-09-30; first quarter after the 2025-08-01 merger |
| 10-Q_2026-03-31_unit-20260331.htm.jsonl | 6eef1c3a3881ef793ddfc9610c4d46208d57c3bb26c5a88a18ed1115bb75d5ba | Unaudited quarterly report, Form 10-Q, 84 chunks | Q1 2026, a combined-company quarter; the comparative quarter is Old Uniti only |
| 10-Q_2026-06-30_unit-20260630.htm.jsonl | 44ae41cd731221c3fab785c468962d8927f45d4ed20722ebe4d9e689ea9bcd05 | Unaudited quarterly report, Form 10-Q, 95 chunks; latest filed statements in the pack | Q2 2026 and six months ended 2026-06-30 |
| EX-99.1_2026-03-02_unit-ex991202510xk.htm.jsonl | c7190cfa9cb627d04b3e648821ebf4356c56f99434b32385548463e0d9accab6 | Earnings release exhibit, 9 chunks; management attribution, supporting claims only | Fourth quarter and full year 2025; release date 2026-03-02 |
| EX-99.1_2026-05-11_unit-ex9911q26.htm.jsonl | cfd5a9da978c996627652ac9d3c7077c0533d727405c7b27dfe93c7e85d28fc5 | Earnings release exhibit, 7 chunks; supporting claims only | Q1 2026; release date 2026-05-11 |
| EX-99.1_2026-07-30_unit-ex9912q26.htm.jsonl | 1d9925874068c008696dd366506144e0d697bf35f0c978f5473bf3052738ff6f | Earnings release exhibit, 8 chunks; supporting claims only | Q2 2026; release date 2026-07-30 |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | e531a4ec67bdeec3bf2b02e8047c90f4c69262abee202a8c1e2071ff24adf370 | Run settings only; not issuer evidence |

### Supplied handoffs

None. CP-0 is the first module in the run, so the handoff set is empty.

### Ignored file

`_retrieval.json` sits in the pack folder and is not a pinned source. It is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filings and releases through the second quarter of 2026 are enough to build the financial base, debt picture and business context, with bounded limits. Executed debt documents and covenant levels are not supplied. | Medium | Reported history mixes a pre-merger company with the combined company, and no executed credit agreement or indenture is in the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Windstream is included only from 2025-08-01, so annual 2025 and early 2025 figures reflect a smaller company than the 2026 quarters. | Year-on-year comparisons overstate or misstate change unless the filed pro forma tables are used with labels. | High |
| The debt note lists each credit facility, note and asset-backed series with principal, rate and maturity, and a July 2026 asset-backed issue is disclosed as a subsequent event. | The capital structure can be set out from the filings, including the post-quarter refinancing. | High |
| Covenant thresholds, executed indentures and credit agreements, and the third-quarter 2026 report are not in the pack. | Covenant headroom and legal ranking cannot be tested from primary documents, and the latest quarter is the second. | High |

### Readiness view

The effective source set supports the requested work with limitations. All four requested consumers are assessed as READY_WITH_LIMITATIONS, none CONDITIONAL and none BLOCKED. The pack holds one audited annual report, three unaudited quarterly reports and three earnings releases, all in USD, all dated on or before 2026-07-30 and so inside the cutoff. The binding limitations are four. First, the merger of 2025-08-01 changes the perimeter, so Old Uniti history before that date and combined history after it must not be set side by side as like for like. Second, no executed credit agreement, indenture, ABS indenture or supplement is supplied, so covenant levels, guarantor lists and security terms rest on filing summaries. Third, nothing after the filing of the second-quarter report on 2026-07-30 is supplied, including any third-quarter 2026 report. Fourth, the text extraction has not been reviewed for fidelity and no chart or image content exists to inspect. None of these blocks a consumer from starting, and each is carried forward as a stated limit.

### Source-by-source assessment

All seven sources identify Uniti Group Inc. as the registrant or the announcing company (page:1 of each). No source is blocked, draft, unsigned or a duplicate of another. The filed 10-K and 10-Qs control their own facts. The three releases are management claims and must not override the filings. The pack has no investor presentations; the retrieval record in the pack folder lists releases in their place, so no slide coverage is claimed or needed.

| Source | What it supports | Limit |
| --- | --- | --- |
| 10-K FY2025 | Auditor opinions (page:95-100), debt table (page:139), pro forma for the year (page:135), unrestricted subsidiary information (Note 21, page:193-195), subsequent events (Note 22, page:195), exhibit list (page:209-217) | Windstream only from 2025-08-01; Windstream excluded from the internal control assessment (page:96) |
| 10-Q Q3 2025 | First post-merger quarter, debt (page:32), pro forma (page:29), unrestricted subsidiaries (page:66-67), Adjusted EBITDA (page:120) | Quarter holds two months of Windstream; superseded for balance sheet facts by later reports |
| 10-Q Q1 2026 | Statements (page:4-5), debt (page:19), unrestricted subsidiaries (page:49), Adjusted EBITDA (page:79) | Comparative quarter is Old Uniti only |
| 10-Q Q2 2026 | Statements (page:4-6), merger and basis (page:9-12), pro forma (page:19-20), debt (page:20-30), swaps (page:32-34), segments (page:45-49), unrestricted subsidiaries (page:50-51), subsequent events (page:52-54), liquidity (page:83-85), Adjusted EBITDA (page:90-91), exhibits (page:94-95) | Covenant levels not printed; cash taxes and interest printed for six months only (page:13) |
| EX-99.1 2026-03-02 | Fourth quarter and full year 2025 highlights, outlook, non-GAAP definitions (page:1, page:8) | Management claims; unaudited |
| EX-99.1 2026-05-11 | Q1 2026 highlights and reiterated outlook (page:1) | Management claims; superseded outlook |
| EX-99.1 2026-07-30 | Q2 2026 highlights, updated 2026 outlook (page:1-2) and Adjusted EBITDA reconciliation (page:7) | Management claims; outlook is forward-looking |

### Entity and perimeter

The registrant is Uniti Group Inc., the ultimate parent after the merger. On 2025-08-01 Windstream merged into the registrant and a merger subsidiary merged into Old Uniti, which survived as an indirect wholly owned subsidiary and ceased to be a REIT (Q2 10-Q page:9). The merger was accounted for as a reverse merger with Windstream as legal acquirer and Old Uniti as accounting acquirer, so periods before the merger show Old Uniti only (page:10-11). The Q2 10-Q states that Windstream is included from 2025-08-01 (page:19). The auditor of record changed: the FY2025 opinion is signed by PricewaterhouseCoopers LLP, "auditor since 2025" (10-K page:99), and a second report covers FY2024 and the year before it (10-K page:100).

Debt sits at several levels. Uniti Services LLC, CSL Capital, LLC and Uniti Group Finance 2019 Inc. are the borrowers under the Uniti Credit Agreement (page:23). Uniti Services, formerly Windstream Services, LLC, is the borrower under the Windstream Credit Agreement (page:24). The senior secured credit facilities are guaranteed by Uniti Group Inc. and Uniti Group LLC on a senior unsecured basis and by certain wholly owned subsidiaries of Uniti Services on a senior secured basis (page:25). Asset-backed notes are issued by bankruptcy-remote subsidiaries: Uniti Fiber ABS Issuer LLC and Uniti Fiber TRS Issuer LLC for the Fiber Infrastructure ABS Notes, and Kinetic ABS Issuer LLC for the Kinetic ABS Notes (page:22, page:50). Kinetic ABS Parent LLC and the Kinetic ABS obligors are unrestricted subsidiaries under the credit agreements and indentures (page:50). The Q2 10-Q gives a restricted versus unrestricted consolidating view of the balance sheet and statement of operations (page:50-51); the 10-K and earlier 10-Qs give the same view for their dates (10-K page:193-195; Q1 10-Q page:49; Q3 2025 10-Q page:66-67).

The notes and their individual issuers and guarantors beyond these passages are an unresolved distinction, not a conclusion. The pack gives the 2026 unsecured notes ranking language (10-K page:201) but no executed indenture, no guarantor schedule and no subsidiary exhibit text. The context names no borrower, parent or guarantor.

### Period basis and version relationships

The perimeter changes within the pack. Fiscal 2025 in the 10-K holds Old Uniti for seven months and the combined company for five (page:19, 10-K page:135). Q1 2026 and Q2 2026 are combined-company quarters whose comparative quarters are Old Uniti only (Q2 10-Q page:11). The Q2 10-Q states that the Windstream operations generated revenues and sales of 795.9 million and operating income of 69.7 million for the three months and 1,605.2 million and 173.0 million for the six months (page:19). It also gives unaudited pro forma comparatives, as if the merger had occurred on 2024-01-01, for the three and six months ended 2025-06-30 (page:19-20). The 10-K gives a pro forma table for the years 2025 and 2024 (page:135). Each pro forma table adjusts for the settlement of preexisting relationships, intangible amortization and other items and is stated to be for information only (page:20). A last-twelve-months figure on the combined perimeter is therefore not available directly from reported figures; it would need pro forma inputs with their labels, which is downstream work.

Statements of operations were reclassified in 2026: the prior-period Old Uniti statements were recast to show sales revenues apart from service revenues, to split cost of services from cost of sales, to add an operating income subtotal and to show loss on extinguishment of debt apart from interest expense, with no effect on net income (page:11). The prior-period cash flow statement was also reclassified (page:12). Comparative columns in the 2026 10-Qs are on this recast basis; the FY2025 10-K and the Q3 2025 10-Q are not.

Quarter versus year to date: the Q2 10-Q and release give three-month and six-month columns (page:5, release page:1). Q1 2026 stands alone in its own 10-Q and release, so each discrete 2026 quarter is available without subtraction. The fourth quarter of 2025 is in the release (page:1) and is derivable from the year and the 10-Q nine-month figures, which is downstream work, not done here.

### Debt, liquidity and subsequent-event evidence present

The Q2 10-Q debt note (page:20-22) lists, at 2026-06-30 and 2025-12-31, the Uniti and Windstream revolvers, the 2025 term loan, six senior note series, the 7.50% convertible senior notes due 2027 and six Fiber Infrastructure ABS series plus three Kinetic ABS 2026-1 series, each with principal, coupon, maturity and unamortized premium or discount. The Windstream term loan was repaid on 2026-02-04 (page:24). Liquidity is stated in the 10-Q (page:83): cash on hand, letters of credit and available revolver capacity. The two revolvers are described with their commitments, maturity date of 2027-12-30, letters of credit and amounts available (page:23-24). Covenants appear in general terms: the debt agreements require certain financial ratios and "the Company was in compliance with all of its debt covenants" (page:22). Pricing grids and mandatory prepayment step-downs refer to leverage ratios without printing the levels in force (page:23-25). The 10-Q prints interest paid and income taxes paid for six months only (page:13). Interest rate swaps and a terminated cap are described (page:32-34).

Subsequent events at the filing date, all inside the cutoff: the Kinetic ABS Series 2026-2 Notes issued on 2026-07-15 with classes A-2, B and C, the associated increase of the liquidity funding note facility, and a term loan prepayment offer and asset sale offers announced on 2026-07-23 with a partial repayment on 2026-07-30 (page:52-54, page:63). The release dated 2026-07-30 also updates 2026 outlook (page:2). The outlook is a management forward-looking statement, not a fact.

### Consumer assessment

| Consumer | Evidence demand | Status | Carried limitations |
| --- | --- | --- | --- |
| CP-1 financial base | Discrete periods, fiscal year, segments, add-backs, facility-level debt, cash flows, cash interest and taxes | READY_WITH_LIMITATIONS | Perimeter change at 2025-08-01; reclassified comparatives; pro forma tables are adjusted and unaudited; cash interest and taxes printed for six months only (Q2 10-Q page:13); non-GAAP Adjusted EBITDA is a management measure (page:90-91) |
| CP-1A business and transaction context | Business, segments, merger, ownership and history | READY_WITH_LIMITATIONS | Merger Agreement and financing documents not supplied (only exhibit lists at Q2 10-Q page:94-95); no sponsor, ownership map or deal terms in the context |
| CP-2 fundamental synthesis | Settled upstream registers plus filings | READY_WITH_LIMITATIONS | Covenant levels, executed debt documents, guarantor schedule and ratings not supplied; context ratings empty; Q3 2026 results not supplied |
| CP-5 evidence trace | Citations that resolve in pinned sources | READY_WITH_LIMITATIONS | Locators are page chunks; extraction fidelity and table layouts not reviewed; releases are management attributions |

Missing downstream analytical handoffs are not treated as source conditions. The dependency planner sequences them. Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Extraction status and fidelity

Every source was retrieved as text chunks and read by search and targeted page reads. Tables arrived as flattened text; column headers were checked against the period labels printed in each table that was cited. No image, chart, slide or workbook content exists in the pack. A successful extraction is not a fidelity review of every table, and none is claimed.

## Calculations

Source tie-outs only, in USD millions. No figure is normalized or reconciled beyond the checks shown.

| Check | Inputs and locator | Result |
| --- | --- | --- |
| Senior notes and convertible principal | 570.0 + 2,200.0 + 1,400.0 + 1,110.0 + 700.0 + 1,600.0 + 306.5 (Q2 10-Q page:20-21) | 7,886.5, equal to the printed subtotal |
| ABS principal | 426.0 + 65.0 + 98.0 + 180.0 + 28.2 + 41.8 + 677.7 + 113.0 + 169.4 (page:21) | 1,799.1, equal to the printed subtotal |
| Total principal | 7,886.5 + 995.0 + 1,799.1 (page:20-21) | 10,680.6, equal to the printed total on page:20 |
| Debt carrying value | 10,680.6 - 34.0 - 10.0 (page:20) | 10,636.6, equal to the printed notes and other debt, net and the balance sheet line (page:5) |
| Year-end 2025 principal | 315.0 + 500.0 + 1,000.0 + 570.0 + 2,200.0 + 1,400.0 + 1,110.0 + 700.0 + 600.0 + 306.5 + 839.0 (page:20-21) | 9,540.5, equal to the printed total and to the 10-K (page:139) |
| Revolver availability | 499.7 + 338.4 (page:23-24) | 838.1, equal to the figure in liquidity (page:83) |
| Letters of credit | 0.3 + 136.6 (page:23-24) | 136.9, equal to the figure in liquidity (page:83) |
| Revolver arithmetic | 500.0 - 0.3 and 475.0 - 136.6 (page:23-24) | 499.7 and 338.4, as printed; no drawings were outstanding at 2026-06-30 |
| Balance sheet | 12,819.4 + 161.5 (page:5) | 12,980.9, equal to total assets |
| Cash by entity group | 15.7 + 593.2 (page:50) | 608.9, equal to consolidated cash |
| Net loss, six months | (70.3) + (155.9) (Q1 10-Q page:4; Q2 10-Q page:5) | (226.2), equal to the six-month figure |
| Revenue, six months | 987.5 + 909.7 (releases page:1) | 1,897.2, equal to the 10-Q six-month figure (page:63) |
| Adjusted EBITDA, six months | 441.6 + 357.1 (Q1 10-Q page:79; Q2 10-Q page:91) | 798.7, equal to the printed six-month figure (page:91) |
| Windstream share of revenue | 795.9 / 909.7 and 1,605.2 / 1,897.2 (page:19, page:63) | 87.5 percent and 84.6 percent; the filing states 87% and 85% (page:63) |
| Kinetic ABS outstanding after 2026-07-15 | 960.1 + (805.2 + 134.2 + 201.3) (page:52) | 2,100.8, consistent with the filing's "$2.1 billion" (page:52, page:63) |
| Release against filing | Q2 2026 net loss 155.9 and Adjusted EBITDA 357.1 (release page:1; 10-Q page:5, page:91) | Equal; no conflict between release and filing |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed Uniti and Windstream credit agreements, indentures, ABS base indentures and supplements are not supplied; only filing descriptions and exhibit lists | High for covenant and legal work; Medium otherwise | CP-2, CP-1A | Supply the executed documents or the 8-K exhibits |
| Covenant levels, step-downs and reported ratios are not printed; only compliance is stated (Q2 10-Q page:22) | High | CP-2 | Supply the credit agreement definitions and any compliance certificate |
| No source after 2026-07-30; no third-quarter 2026 report, no later 8-K | Medium | CP-1, CP-1A, CP-2 | Supply later filings up to the cutoff or confirm none |
| Windstream standalone statements before 2025-08-01 are not supplied; only pro forma tables | Medium | CP-1 | Treat pro forma as adjusted and unaudited; supply Windstream pre-merger statements if a standalone history is needed |
| Perimeter and reclassification changes between FY2025 and 2026 reporting | Medium | CP-1, CP-2 | Label every figure by period and basis; do not mix |
| Merger Agreement and financing commitments are listed in exhibits only | Low to Medium | CP-1A | Supply if transaction detail is needed |
| No credit ratings, market prices, peers or valuation inputs | Low for the selected modules | CP-2 | Not required for this scope; keep Not supplied |
| Text extraction only; no fidelity review, no original HTML or XBRL | Low | CP-1, CP-5 | Check flagged tables against the filed document when available |
| Cash paid for interest and taxes printed for six months only in the Q2 10-Q (page:13) | Low | CP-1 | Use the 10-K for the year and label the periods |

## Next module

- CP-1: use the 10-K and 10-Qs as controlling. Keep Old Uniti history, combined-company periods and pro forma tables separate and labelled. Take Q2 2026 as the current period and FY2025 as the prior period named by the context. Carry the reclassified comparatives, the facility-level debt table (Q2 10-Q page:20-21) and the six-month cash interest and tax figures as stated, and label Adjusted EBITDA as a management non-GAAP measure.
- CP-1A: carry the 2025-08-01 reverse merger and its accounting as the central transaction, the three reportable segments (Q2 10-Q page:8, page:45-49), and the entity map above, including the unrestricted ABS subsidiaries. Label anything after 2026-07-30 as Not supplied.
- CP-2 and CP-5: carry the missing executed documents, covenant levels, ratings and third-quarter results as restrictions; treat release statements as attributed claims; cite page chunks as given.
