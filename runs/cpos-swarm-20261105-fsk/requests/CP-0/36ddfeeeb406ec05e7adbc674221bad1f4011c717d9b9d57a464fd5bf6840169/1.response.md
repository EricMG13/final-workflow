## Request

Module CP-0 (source readiness) for FS KKR Capital Corp (issuer id fsk, NYSE: FSK), credit_snapshot pathway, as of 2026-11-05 (cutoff 2026-11-05). Reporting currency USD; current period Q3 2026 (quarter ended 2026-09-30); prior period FY2025. The question is whether the supplied source set can support the selected downstream work (CP-1, CP-1A, CP-2, CP-5) and what remains blocked. This module gives no credit opinion, recalculates nothing and does not evaluate any model input contract. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED (no Model deliverable is requested in this run).

Scope facts from the run settings (not issuer evidence): case kind public; deal terms, quotes, ratings, peers and precedents are empty; no legal documents are attached (`legal_documents` is "none"); sector, sponsor, parent and borrower name are blank. Blank values are not treated as zero.

## Sources

### Issuer sources relied on

All seven issuer sources are text extractions ("Visible text of ...") split into numbered pages; `page:N` below is the extraction chunk, not the printed page. The sha256 shown is the pinned hash of the extracted file CP-OS supplies.

| Source (exact name) | sha256 (pinned file) | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_fsk-20251231.htm.jsonl | be99ced2da7392c013fd879201dbe6646929f936ebb77ecc5d0444caab275d72 | Annual report on Form 10-K, filed 2026-02-25 (298 pages); filed audited statements, so controlling for FY2025 facts | FY2025, year ended 2025-12-31; consolidated, USD millions |
| 10-Q_2026-03-31_fsk-20260331.htm.jsonl | c1848df2f7f8ae50873fb96d813147e929f68a7d9fd036caac9a50ef11030183 | Quarterly report on Form 10-Q, filed 2026-05-11 (157 pages); filed unaudited statements | Q1 2026, three months ended 2026-03-31 |
| 10-Q_2026-06-30_fsk-20260630.htm.jsonl | 5179e6b96937e772046c13be81daafa87748d7253056dcfc343a0e0d70e10e37 | Quarterly report on Form 10-Q, filed 2026-08-06 (169 pages); filed unaudited statements | Q2 2026 and six months ended 2026-06-30 |
| 10-Q_2026-09-30_fsk-20260930.htm.jsonl | 9fd3638380d8a2268f17361ef6fc29d66f22c0391f57eb0cb6b68acb61776e4e | Quarterly report on Form 10-Q, filed 2026-11-05 (169 pages); filed unaudited statements; the current-period authority | Q3 2026 and nine months ended 2026-09-30 |
| EX-99.1_2026-05-10_tm2614112d1_ex99-1.htm.jsonl | 7e0c1f798df446f884320f02fed73d08f87b229f9d7b33f04d81f5473d6602e3 | Earnings release exhibit (12 pages); management narrative with non-GAAP measures; stands in for a presentation | Q1 2026; text is dated May 11, 2026 although the file name carries 2026-05-10 |
| EX-99.1_2026-08-06_tm2622260d1_ex99-1.htm.jsonl | 24d1ea2d36b2f64d8b77676a71ecd16bea780f8870e6b7238b28ee023281ffd9 | Earnings release exhibit (12 pages); management narrative with non-GAAP measures | Q2 2026, release dated August 6, 2026 |
| EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | 9570b8d0d4b7076e0359f3122075bc5e24c85c74b9723e31fa99d14ae3f3839b | Earnings release exhibit (11 pages); management narrative with non-GAAP measures | Q3 2026, release dated November 5, 2026 |

### Run settings (not issuer evidence)

| Input | sha256 | Use |
| --- | --- | --- |
| context (1422183-fs-kkr-capital-corp-fsk.json) | 378a6255aee6dac53a389f9bf4cbce2419e6f8121d5d4932c50d57d1600eb13a | Dates, currency and scope only; never used as evidence of an issuer fact |

`_retrieval.json` in the pack folder is ignored by CP-OS as a source; it was read only to confirm that 3 of 3 quarters carry an earnings release instead of a presentation.

### Supplied handoffs

None. CP-0 is the first module in this run and CP-OS supplied no upstream handoff.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filed sources support the downstream snapshot with limitations: statements, debt schedule, liquidity, leverage and 2026 capital actions are located, but covenant levels, ratings and underlying financing documents are absent. | Medium | No credit agreements, indentures, ratings or investor presentations were supplied; covenant thresholds beyond asset coverage cannot be read, and the cash definition changed between releases. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Filed statements and the full debt schedule are readable for the third quarter of 2026 and for FY2025. | Leverage, liquidity and maturity work can start from filed figures rather than management claims. | High |
| The issuer is a business development company, so corporate measures such as EBITDA and segment margins do not map. | Credit metrics must rest on investment income, net asset value, asset coverage and debt rather than industrial-style cash flow. | Medium |
| Cash is defined differently across releases: restricted cash was included in earlier net debt and excluded in the latest. | Quarter-on-quarter net leverage comparisons can mislead unless cash is put on one basis. | High |
| Covenant thresholds, ratings and the underlying financing agreements are not in the pack. | Headroom against lender tests cannot be measured beyond the disclosed asset coverage and a compliance statement. | High |
| The joint venture with an outside investor is described only through selected balance sheet and income data. | Its own debt and look-through exposure can be noted but not analysed in depth. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for all four selected consumers. The filed 10-K and three filed 10-Qs carry the statements, the note on financing arrangements, liquidity discussion, commitments, financial highlights and subsequent events for the issuer's own consolidated perimeter, and three earnings releases add attributed management narrative and the 2026 capital actions. Nothing blocks a consumer on identity, period or perimeter. The limitations are bounded: no executed financing documents, no ratings or market quotes, no investor presentations, and a business development company structure that changes which credit metrics exist. Readiness here is source sufficiency only; it does not say that any downstream analysis is complete or that any figure has been normalised or reconciled.

### Source-by-source assessment

- **Entity and perimeter.** The registrant is a single legal entity filing consolidated statements. Note 1 describes it as an "externally managed, non-diversified, closed-end management investment company" with "various wholly-owned subsidiaries, including special-purpose financing subsidiaries" (10-Q Q3 2026 page:67). The adviser is FS/KKR Advisor, LLC (10-K FY2025 page:4: "We are managed by FS/KKR Advisor, LLC"). Borrowings of the financing subsidiaries count as the Company's: "Borrowings of each of the Company’s wholly-owned, special-purpose financing subsidiaries are considered borrowings of the Company" (10-Q Q3 2026 page:113). No separate issuer, guarantor or restricted/unrestricted group is named in the sources read; the notes and credit-facility names (Callowhill, Senior Secured Revolving Credit Facility, CLO-2, CLO-3) are borrowing vehicles inside the consolidated perimeter.
- **Original authority.** The 10-K and 10-Qs are filed statements and control their facts. The three earnings releases are management presentations of the same quarters and carry non-GAAP measures (adjusted net investment income, net debt); they are attributed supporting claims and cannot override the filings. Where the release and the 10-Q show the same item they agree on the points sampled (net asset value per share $18.28 and total assets $11,695 in both the Q3 release pages 8 and 9 and the Q3 10-Q pages 2 and 3).
- **Periods and basis.** Current period Q3 2026 is covered by the Q3 10-Q (three and nine months ended September 30, 2026) and the Q3 release. The prior period FY2025 is covered by the 10-K and by the December 31, 2025 comparative column in each 2026 10-Q (for example 10-Q Q3 2026 page:2, "Total assets $ 11,695 $ 13,729"). The Q1 and Q2 10-Qs and releases provide the intermediate quarters for a discrete Q1, Q2, Q3 view; the Q2 10-Q gives six-month and the Q3 10-Q nine-month cumulative columns, so quarter versus year-to-date must stay labelled. All amounts are USD millions unless marked; the senior revolver also holds euro, sterling and Australian dollar borrowings translated to USD (10-Q Q3 2026 page:110, footnote 4).
- **Version relationships.** Each filing is the original for its period. No amendments (10-K/A, 10-Q/A) are in the pack. The pack does not hold any executed indenture, credit agreement, purchase agreement or supplement, so no base-versus-amendment question arises.
- **Debt and liquidity evidence located.** Note 9 lists every financing arrangement with rate, amount outstanding, amount available and maturity, and gives the total: "Total $ 6,487 $ 3,197" including the $150 convertible preferred (10-Q Q3 2026 page:110). The senior revolver availability is stated net of standby letters of credit: "As of September 30, 2026, $50 of such letters of credit have been issued" (page:110). A December 31, 2025 table is on page:111. The 10-K carries the full note (10-K FY2025 page:259 onward, with the indenture descriptions on pages 274 to 276). Liquidity text, unfunded commitments and the asset coverage discussion are on 10-Q Q3 2026 pages 141 to 143; the 10-K equivalent is on page:144.
- **Covenant evidence located.** The only compliance statement is generic: "The Company was in compliance with all covenants required by its financing arrangements as of September 30, 2026 and December 31, 2025" (10-Q Q3 2026 page:113). The 10-K says the covenants "require us and our subsidiaries to, among other things, maintain certain financial ratios, including asset coverage and minimum stockholders’ equity" (10-K FY2025 page:93) without printing a threshold. The statutory asset coverage test is quantified in the 10-Q: coverage on senior securities representing indebtedness of 179% and on senior securities that are stock of 177%, against a 150% requirement (page:109 and pages 142 to 143).
- **Subsequent events and the cutoff.** All seven sources were filed on or before 2026-11-05, so nothing postdates the cutoff. The Q3 10-Q and Q3 release were filed on the as-of date itself. Subsequent events are in the 10-Q Q3 2026 Note 13 (page:123) and release page:2: repurchases from October 1 through October 30, 2026, a declared fourth quarter distribution, a declared special distribution and a declared preferred dividend. Future payment dates in those items are declared terms, not events after the cutoff.
- **Transaction and ownership evidence.** The 2026 capital actions are documented: the May release announces a $150 million convertible preferred from a KKR subsidiary, a $150 million tender offer, a $300 million repurchase program and a 50% incentive fee waiver (EX-99.1 Q1 2026 pages 2 and 3); the Q3 10-Q share transactions note records the preferred issue on June 29, 2026 to KKR Alternative Assets L.P. (page:74) and the $900 principal 7.500% Notes due 2031 issued June 8, 2026 appear in the Q2 10-Q (page:95) and the Q3 note table. Governing documents (purchase agreement, advisory agreement) are referenced but not supplied.
- **Joint venture.** Credit Opportunities Partners JV, LLC is a 50/50 voting joint venture with South Carolina Retirement Systems Group Trust; the 10-Q gives selected balance sheet and income data (10-Q Q3 2026 page:94), including the joint venture's own debt, which is not the issuer's borrowing. The venture's full statements are not supplied.

### Conflicts, definitional differences and extraction cautions

- **Cash basis changed.** The Q2 release nets "Cash, cash equivalents, restricted cash and foreign currency $ (109 )" in net debt (EX-99.1 Q2 2026 page:10), with restricted cash defined as "cash collateral required to be posted pursuant to the Company’s derivative contracts" (page:12). The Q3 release nets "Cash, cash equivalents, and foreign currency ($111)" (EX-99.1 Q3 2026 page:9), while the Q3 balance sheet shows "Restricted cash 61" separately (10-Q Q3 2026 page:2). The Q3 cash flow statement ends at "$ 172" including "restricted cash of $61" (page:5). The reported net debt-to-equity ratios (122% for Q2, 125% for Q3) are therefore not on an identical cash basis. Downstream modules must label which cash they use; CP-0 does not restate.
- **Three debt figures.** The Q3 balance sheet shows "Debt (net of deferred financing costs and discount of $46 and $45, respectively) 6,231" (10-Q page:2), the Q3 release shows "Debt outstanding (principal) $6,337" (release page:9), and Note 9 totals "$ 6,487" including the convertible preferred (page:110). Footnote 7 on page:110 identifies hedge-accounting carrying adjustments on four notes. The differences are of basis (carrying versus principal versus including preferred); CP-0 does not reconcile them, and CP-1 must carry the basis with each figure.
- **Interest rate bases differ.** The Q3 release quotes a "weighted average stated interest rate on borrowings was 5.57%" (release page:3) and the Q2 release a "weighted average effective interest rate (including the effect of non-usage fees) was 5.49%" (EX-99.1 Q2 2026 page:3); the Q3 10-Q gives 5.72% for the nine months including non-usage fees (page:113). These are different bases and periods, not a conflict in the filing.
- **Date labels.** The Q1 release file name carries 2026-05-10 but its text is dated "May 11, 2026" and the pack index lists filing date 2026-05-11. The file-name date is not used as an authority. The purchase agreement for the preferred is dated May 10, 2026 (10-Q Q3 2026 page:74).
- **Extraction fidelity.** Extraction is visible text only; no charts, images or speaker notes exist in these sources, and no presentation is supplied. Tables are flattened into lines, so column alignment must be checked against the page before a figure is read. At least one value is dropped in extraction: "is outstanding as of ) and (iv)" in the fee table footnote leaves a blank date (10-Q Q3 2026 page:167). A successful extraction is not a fidelity review; the figures sampled above matched across filing and release, but the schedule of investments pages (tens of pages in each 10-Q, for example roughly pages 5 to 66 of the Q3 10-Q extraction) were not read line by line in CP-0.
- **No filing conflicts found in the sampled facts.** The Q3 10-Q liquidity text ("$111 in cash, cash equivalents, including money market funds, and foreign currency" and "$3,197 in borrowings available", page:141) agrees with the Q3 release and with Note 9.

### Consumer assessment

| Consumer | Readiness | Evidence located | Limitations carried forward |
| --- | --- | --- | --- |
| CP-1 canonical data foundation | READY_WITH_LIMITATIONS | Statements of operations, balance sheets, cash flows, net assets, Note 9 debt tables, financial highlights, asset coverage and non-GAAP reconciliations for Q1, Q2 and Q3 2026 and FY2025 | Business development company: no EBITDA, capex or segments (single segment, 10-Q Q3 2026 page:123); covenant levels unprinted; cash basis and debt basis differ across sources; quarter versus year-to-date must stay labelled |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business description in the 10-K (page:4), adviser relationship, KKR-related 2026 capital actions, share repurchase, joint venture, subsequent events | Context carries no deal terms, sector, sponsor or parent; executed purchase and advisory agreements not supplied; ownership beyond filing disclosure not supplied |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Depends on CP-1 and CP-1A registers; source set gives credit-relevant drivers (non-accrual share, net asset value trend, leverage, liquidity, maturities) | No ratings, market quotes, peers or covenant thresholds; synthesis inherits every CP-1 and CP-1A limitation |
| CP-5 evidence trace validator | READY_WITH_LIMITATIONS | Seven pinned sources with page locators allow quote and figure checks against filings | Management-release claims need filing support; presentations absent, so no slide-level trace exists |

## Calculations

No analytical calculation was performed or needed in CP-0. Only coverage counts were tallied from the extraction headers.

| Item | Inputs | Result |
| --- | --- | --- |
| Filing pages in the four filed periodic reports | 298 (10-K) + 157 (Q1 10-Q) + 169 (Q2 10-Q) + 169 (Q3 10-Q) | 793 |
| Release pages in the three earnings releases | 12 (Q1) + 12 (Q2) + 11 (Q3) | 35 |
| Total extraction pages across the seven sources | 793 + 35 | 828 |

Coverage statement: all 828 extraction pages are retained as evidence. Pages read in CP-0 were targeted to the statements, financing notes, liquidity, subsequent events, covenant and rating terms, and the three releases in full; the remaining pages (mainly the schedules of investments, fair value tables, risk factors and tax notes) are retained but not individually reviewed here and carry no CP-0 claim.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreements, indentures, CLO documents and the convertible preferred terms are not supplied; only the notes summarise them (10-Q Q3 2026 pages 109 to 111) | Medium | CP-1, CP-2, CP-5 | Obtain executed facility and indenture documents if covenant-level analysis is required; otherwise report covenant headroom as Not supplied |
| Numeric financial covenant thresholds other than the statutory 150% asset coverage are not printed; "minimum stockholders’ equity" has no level (10-K FY2025 page:93) | Medium | CP-1, CP-2 | State Not supplied; use disclosed asset coverage of 179% and 177% and the compliance statement only |
| No rating of the issuer or its notes was found when the sources were searched for rating terms, and there are no market quotes or peers (context fields are empty; the filings discuss ratings only for portfolio investments, generically, and as a risk factor) | Medium | CP-2 | Treat ratings and relative value as Not supplied; do not infer from filings |
| No investor presentations; 3 of 3 quarters have a release only | Low | CP-1A, CP-5 | Use releases as attributed management claims; no slide-level coverage can be claimed |
| Cash definition differs between the Q2 and Q3 releases, and debt appears on three bases | Medium | CP-1, CP-2, CP-5 | Label basis on every figure; do not mix net debt ratios across quarters without restating cash |
| Business development company structure: no EBITDA, segment, capex or cash-conversion data in the usual form | Medium | CP-1, CP-2 | Use investment income, net investment income, net asset value, non-accrual share and asset coverage as the metric set; say so explicitly |
| Joint venture and affiliated portfolio companies appear only as selected data | Low | CP-1A, CP-2 | Note the venture's own debt as outside the issuer's borrowings; Not supplied for its full statements |
| Context holds no deal terms, sector, sponsor, parent or guarantors; governing agreements for the KKR capital actions not supplied | Low | CP-1A | Rely on filing and release disclosure; leave unfilled fields as Not supplied |
| Text extraction only: tables flattened, one dropped date in the fee table (10-Q Q3 2026 page:167); schedules of investments not reviewed line by line | Low | CP-1, CP-5 | Check column alignment on the page before reading any figure; re-open the source page for every quote |

## Next module

CP-1 (canonical data foundation) can run now on the pinned sources. Instructions for it:

- Use the Q3 10-Q (Q3 2026 and nine months), the Q1 and Q2 10-Qs for discrete quarters and the 10-K for FY2025; keep the Q3 release only for attributed non-GAAP measures.
- Build the debt table from Note 9 (10-Q Q3 2026 pages 109 to 111, 10-K FY2025 page:259 onward), label carrying value, principal and total including preferred, and keep the letters of credit deduction from availability.
- Put cash on one stated basis and show the restricted cash of $61 separately; do not compare the 122% and 125% net debt ratios without saying the bases differ.
- Carry forward: business development company metric set, no covenant thresholds, no ratings, single segment, and quarter versus year-to-date labels.

CP-1A, CP-2 and CP-5 follow in dependency order and inherit every limitation in the Gaps section.
