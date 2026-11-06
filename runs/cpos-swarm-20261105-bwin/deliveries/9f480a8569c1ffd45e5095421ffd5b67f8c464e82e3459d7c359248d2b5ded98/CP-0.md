## Request

Issuer: Baldwin Insurance Group, Inc. (issuer id bwin; Nasdaq ticker BWIN; Delaware registrant, SEC file number 001-39095; brand name The Baldwin Group). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD; the statements are in thousands of US dollars and the narrative in millions or billions. Current period named by the context: Q2 2026 (quarter ended 2026-06-30). Prior period named by the context: FY2025.

Question for this module: can the supplied source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This module gives no credit conclusion, legal interpretation or investment opinion. It does not normalize, reconcile or calculate figures. Arithmetic in `## Calculations` is limited to tie-outs that test source consistency and to coverage counts.

The context file holds the run settings and is not issuer evidence. Its deal terms, quotes, ratings, peers, precedents and research questions are empty, it names no borrower, parent, guarantor or sponsor, and its attachments field says legal documents are "none". Those blanks are treated as not supplied, never as zero.

## Sources

### Issuer sources relied on

Each file is one JSONL extraction of an SEC filing. The locator `page:N` is the extraction chunk, not the printed page. The sha256 below is the pinned file hash. Each file prints a different hash for the underlying htm document in its first line; that one is not used here.

| Source name | sha256 | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_bwin-20251231.htm.jsonl | 435ed820e1dedd05dae93bd87717be3ea65acd13ff9cfffaff7aef178e8494c0 | Audited annual report, Form 10-K, 201 chunks; filed statements control their facts | FY2025 (year ended 2025-12-31) with FY2024 and FY2023 comparatives; auditor report signed 2026-02-26 (page:131) |
| 10-Q_2025-09-30_bwin-20250930.htm.jsonl | 0c90579fda7c87633de78b7017eb30aa8347d6e49afceae9c9779736c12ef751 | Unaudited quarterly report, Form 10-Q, 79 chunks | Q3 2025 and nine months 2025, with 2024 comparatives |
| 10-Q_2026-03-31_bwin-20260331.htm.jsonl | 5f7ff56cb35eb60658f5417d0bba0ed7cf98e6637612d04f68a150a621f88e2d | Unaudited quarterly report, Form 10-Q, 76 chunks | Q1 2026, with 2025 comparatives |
| 10-Q_2026-06-30_bwin-20260630.htm.jsonl | c7872b5a0e467a855aa0647c334b01115eb4a8b78c766a2ae8d6dccc7348e147 | Unaudited quarterly report, Form 10-Q, 85 chunks; latest filed statements in the pack | Q2 2026 and six months 2026, with 2025 comparatives and a 2025-12-31 balance sheet |
| EX-99.1_2026-02-26_ex991bwinfy2025q4earningsr.htm.jsonl | a080932734c7e6f80d7856122b745700585d5721dda88f2356f627e5082d8b98 | Earnings release exhibit, 17 chunks; management attribution, supporting claims only | Q4 2025 and FY2025 |
| EX-99.1_2026-05-04_ex99-1fy2026q1earningsrele.htm.jsonl | e172c6af59bf6e4ced5ad8c6113ef1f6cea50e4c9e4f92d7126f157d6d775038 | Earnings release exhibit, 13 chunks; supporting claims only | Q1 2026 |
| EX-99.1_2026-07-30_ex99-1fy2026q2earningsrele.htm.jsonl | cbd7cabcbf8fcf9cc1502cda8859930cd02f842bc6bfad19f57059a1a93bf562 | Earnings release exhibit, 14 chunks; supporting claims only | Q2 2026 and six months 2026 |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 8078b6eb19ff2611ca7e63e8361807aa16e370931c16f21c4255d38d5faaa273 | Run settings only; not issuer evidence |

### Supplied handoffs

None. This is the first module in the run, so the handoff set is empty.

### Ignored file

_retrieval.json sits in the pack folder and is not a pinned source. It is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The annual report, three quarterly reports and three earnings releases through the second quarter of 2026 are enough to build the financial base, debt picture and business context, with bounded limits. | Medium | The credit agreement, indenture and covenant compliance figures are not supplied, and the large January 2026 acquisitions change comparability. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The financial maintenance covenant is described only in the annual report, and no later report states a ratio or compliance. | Covenant headroom cannot be measured from the pack; only the company's stated borrowing capacity is available. | High |
| Debt terms, balances and the January 2026 term loan add-on are printed in the latest quarterly report. | Facility sizes, balances, rates and maturities can be set out from the filing. | High |
| Three acquisitions closed in January 2026, alongside higher revenue, debt, earnout and deferred payment balances, against prior-year comparatives that exclude them. | Year-over-year figures mix acquired and organic results, so downstream work must use the stated organic and pro forma measures. | High |
| Segment profit is disclosed as net income only; segment adjusted EBITDA, ratings and guarantor names are not supplied. | Segment cash earnings, rating context and the guarantor perimeter are open gaps. | Medium |

### Readiness view

The effective source set supports the requested work with limitations. All four requested consumers are assessed as READY_WITH_LIMITATIONS; none is CONDITIONAL and none is BLOCKED. The audited annual report, three quarterly reports and three earnings releases cover the periods the context names, in the reporting currency, with the latest dated 2026-07-30, before the 2026-11-05 cutoff. The binding limitations are five. First, no executed legal document is supplied, so covenant levels, guarantor lists and security terms rest on filing summaries, and the quarterly reports print no covenant compliance statement at all. Second, the January 2026 acquisitions of CAC Group, Obie and Capstone make the 2025 comparatives and the FY2025 base differ in perimeter from the 2026 reports. Third, segment adjusted EBITDA is not disclosed in the segment note. Fourth, no fidelity review of the text extraction was done, and the pack contains no slides or charts. Fifth, no report for the quarter ended 2026-09-30 is supplied, so the latest balance sheet is 2026-06-30. None of these blocks a consumer from starting, and each carries forward as a stated limit.

### Source-by-source assessment

All seven sources identify The Baldwin Insurance Group, Inc. as registrant or announcing company (page:1 of each). No source is blocked, draft, unsigned or a duplicate of another; the three releases and the quarterly reports overlap in content but are different documents. The filed 10-K and 10-Qs control their own facts. The releases are management claims and must not override a filing.

| Source | What it supports | Limit |
| --- | --- | --- |
| 10-K FY2025 | Audited statements (auditor report page:128; balance sheet page:131-132; income statement page:132; cash flows page:134-135), debt note 12 (page:161-165), covenant text (page:164), debt maturities (page:165), segment note (page:183-186), subsequent events including the January 2026 acquisitions and Amendment No. 4 (page:188-189), Adjusted EBITDA reconciliation (page:99), exhibit list (page:196-200) | The exhibit list names the indenture and credit agreement amendments but does not reproduce them; maturities are as of 2025-12-31, before the January 2026 add-on |
| 10-Q Q3 2025 | Nine-month 2025 statements (page:5-6, page:9), debt note (page:28), segments (page:38), Adjusted EBITDA reconciliation (page:55), liquidity (page:68) | Supplies the third-quarter 2025 discrete period and 2024 comparatives |
| 10-Q Q1 2026 | Q1 2026 statements (page:5-8), debt note including Amendment No. 4 (page:23), segments (page:39), Adjusted EBITDA reconciliation (page:54), liquidity (page:65) | Unaudited |
| 10-Q Q2 2026 | Statements (balance sheet page:5-6, income page:6-7, cash flows page:9-10), business combinations (page:16-19), debt (page:24-25), fair value of debt (page:38), segments (page:40-44), subsequent events (page:46-47), non-GAAP reconciliations (page:58-61), liquidity and contractual obligations (page:72-75), controls (page:82-83) | Unaudited; no covenant text; no principal maturity table |
| EX-99.1 2026-02-26 | Q4 and FY2025 headline results, share repurchase authorization, adjusted free cash flow definition change (page:1, page:12) | Management claims |
| EX-99.1 2026-05-04 | Q1 2026 headlines and adjusted EBITDA reconciliation (page:1, page:11) | Management claims |
| EX-99.1 2026-07-30 | Q2 2026 headlines, liquidity sentence, adjusted EBITDA and adjusted free cash flow reconciliations (page:1-2, page:11, page:13) | Management claims; guidance has no GAAP reconciliation (page:11) |

### Entity and perimeter

The registrant is The Baldwin Insurance Group, Inc., a holding company whose "sole material asset is its ownership interest in Baldwin Holdings" (10-Q Q2 2026 page:11). The operating company and borrower is The Baldwin Insurance Group Holdings, LLC ("Baldwin Holdings"), defined at 10-Q Q2 2026 page:4 and named "as borrower" under the JPM Credit Agreement (10-Q Q2 2026 page:4). The statements are consolidated with Baldwin Holdings and carry a noncontrolling interest for LLC Units held by others (page:11). No stand-alone financial statements of Baldwin Holdings or of the issuer group are supplied, so debt-level analysis rests on consolidated figures. This is a perimeter gap, not a conclusion.

The 7.125% Senior Secured Notes were issued by Baldwin Holdings and a wholly-owned corporate subsidiary of Baldwin Holdings, called the co-issuer (10-K page:161); the exhibit list names the co-issuer as The Baldwin Insurance Group Holdings Finance, Inc. (10-K page:196). The notes and the JPM Credit Facility are guaranteed by certain direct and indirect subsidiaries of Baldwin Holdings (10-K page:163); no guarantor is named in the pack. Exhibit 21.1, the list of subsidiaries, is marked as filed with the 10-K (page:200) but its text is not in the pack. Security is "substantially all the assets of Baldwin Holdings and the guarantors" (10-K page:163). The Tax Receivable Agreement is an obligation of the parent, not of Baldwin Holdings (10-Q Q2 2026 page:15). Consolidated variable interest entities have assets usable only to settle their own obligations and creditors of those entities have no recourse to the Company (10-Q Q2 2026 page:6, page:20).

### Period basis and version relationships

Statements are unaudited for the interim periods and audited for FY2025. The balance sheet at 2025-12-31 in the interim reports is derived from the audited statements (10-Q Q2 2026 page:12). The interim income statements use three-month and six-month columns (Q2 2026 page:6-7); the Q3 2025 report uses three-month and nine-month columns. A discrete Q4 2025 therefore comes from the Q4 release (page:1, page:5) or from the FY2025 less nine-month 2025 figures, which is downstream work and is not done here. Discrete Q1 2026 is in the Q1 10-Q, and discrete Q2 2026 in the Q2 10-Q.

The perimeter changes inside the pack. Three business combinations with aggregate purchase price of $1.6 billion closed in the first half of 2026: CAC Group effective 2026-01-01, Obie and Capstone effective 2026-01-02 (10-Q Q2 2026 page:16-17; 10-K page:188-189). The 10-K and Q3 2025 report precede them; the 10-K describes them as subsequent events and says the company had not yet completed its evaluation of the identifiable assets and liabilities acquired (10-K page:188). The Q2 10-Q still describes purchase price allocations as provisional (page:18). The Q2 10-Q provides pro forma results as if the acquisitions had occurred on 2025-01-01 (page:19-20) and organic revenue growth (page:60). Reported 2025 comparatives and the FY2025 base do not include the acquired businesses; pro forma and organic figures are the only like-for-like bridges supplied.

The 10-K debt note mixes periods. Its narrative still describes the 2024 Term Loans at a margin of 325 bps and revolver margins of 200 bps to 300 bps (10-K page:162) before later paragraphs reprice them to 250 bps and 175 bps to 250 bps (10-K page:164-165). The later paragraphs supersede the earlier text. The Q2 10-Q gives the revolver margin as "SOFR plus 185 bps to SOFR plus 260 bps" in the liquidity section (page:73) and as a 10 bps credit spread adjustment plus 175 bps to 250 bps in Note 10 (page:24). These are the same range once the adjustment is added; see Calculations.

Interest expense differs between the income statement and the Adjusted EBITDA reconciliations. The Q2 10-Q footnote says "Interest expense, net does not include interest income on surplus notes" (page:61). The Q2 reconciliation uses 46,140 for the quarter against 45,666 on the income statement (release page:11; 10-Q page:7), and the 10-K reconciliation uses 122,778 against 121,428 (page:99; page:132). This is a labelled definition difference, not an error. Downstream work must say which one it uses.

Version relationship among documents: Amendment Nos. 1 to 4 to the JPM Credit Agreement are separate active amendments to the base agreement dated 2024-05-24 (10-Q Q2 2026 page:4). The 10-K exhibit list names the base agreement and each amendment (exhibits 10.27 to 10.31, page:199-200), the indenture (exhibit 4.1, page:196) and the CAC Group Transaction Agreement dated 2025-12-02 with its amendment (exhibits 10.32 and 10.33, page:200). None of these documents is supplied; they remain separate sources to obtain, not collapsed into the filings that summarize them.

### Debt and liquidity evidence present

The Q2 10-Q gives, at 2026-06-30: Term Loans of "$1.6 billion" at 6.13% maturing 2031-05-24; Revolving Facility commitments of $600 million maturing 2029-05-24 with $302.0 million drawn at 6.23%; 7.125% Senior Secured Notes of $600 million due 2031-05-15; undrawn letters of credit under the revolver of $38.6 million; a commitment fee of 0.40% on unused capacity; quarterly Term Loan principal payments of $4.0 million (page:24-25, page:73). The exact principal is in the fair-value table: long-term debt carrying amount 2,193,045 thousand and revolver 302,000 thousand (page:38). The same table's footnote says unamortized discount and issuance costs are $26.2 million, and the balance sheet shows revolving line of credit 302,000, long-term debt less current portion 2,150,725 and a current portion of long-term debt of 16,091 within accrued expenses (page:5, page:23). A $500 million floating-to-fixed swap at 3.244% runs to 2028-09-14 (page:25). The company states cash and cash equivalents of $184.5 million and $259.4 million of available borrowing capacity on the revolver (page:74; release page:2). Fiduciary cash of 426,189 thousand is shown separately from cash and cash equivalents of 184,499 thousand on the balance sheet (page:5) and is not unrestricted cash.

Claims outside the debt figure that are printed: contingent earnout liabilities of 120,901 thousand current and 225,923 thousand non-current; Tax Receivable Agreement liabilities of 144,570 thousand; other liabilities of 129,376 thousand, which include the non-current deferred payment obligations of $129.4 million (page:5, page:19); operating lease liabilities (page:5, page:74-75); and a University of South Florida commitment of $2.5 million through October 2028 (page:38). The contractual obligations table at page:74 gives totals by period for operating leases, debt obligations including estimated interest, undiscounted earnout obligations, deferred payments and the USF grant. The company has a $250 million share repurchase authorization announced 2026-02-26, with approximately $124.5 million remaining at 2026-06-30 (page:83).

The 10-K reports at 2025-12-31: cash and cash equivalents 123,669 thousand, $477.0 million of available revolver capacity (page:110), principal amount of long-term debt 1,603,606 thousand with maturities by year (page:165) and cash paid for interest 115,276 thousand and cash paid for taxes 1,700 thousand for FY2025 (page:135). The Q2 10-Q gives cash paid for interest of 76,315 thousand and for income taxes of 759 thousand for six months 2026 (page:10).

The pack does not give: a principal maturity table at 2026-06-30 after the January 2026 add-on (the 10-K table is as of 2025-12-31; the Q2 contractual obligations table includes interest); an amortization-adjusted exact term loan balance (only "$1.6 billion" and the implied figure derived in Calculations); fair value of the term loans separately from the notes; or any pension or retiree medical obligation beyond a 401(k) plan with employer matching (10-K page:16, page:127 index "Retirement Plan"). Factoring and supply-chain finance did not appear in a search of all seven sources.

### Covenants

The only financial maintenance test printed is in the 10-K: "a financial maintenance covenant requiring Baldwin Holdings to maintain a total first lien net leverage ratio at or below 7.00 to 1.00 on a pro forma basis", with compliance stated at 2025-12-31 (10-K page:164). The Senior Secured Notes indenture limits the issuers and restricted subsidiaries on debt, liens, restricted payments, affiliate transactions and mergers, with compliance stated at 2025-12-31 (10-K page:162). The 10-K also gives the incremental facility test of 5.50x total first lien net leverage and a margin step-down at 4.00x first lien net leverage (10-K page:162-163). A search of all seven sources for covenant, 7.00, financial maintenance, springing, fixed charge and interest coverage found covenant wording only in the 10-K. The Q3 2025, Q1 2026 and Q2 2026 reports contain none, and no source prints the reported first lien net leverage ratio, the definition of consolidated EBITDA or whether the test applies at all times or only when the revolver is drawn. Covenant headroom is therefore not calculable from the pack. The 7.00x test is "on a pro forma basis" and its defined terms are not supplied, so they may differ from the company's adjusted EBITDA and from GAAP debt; downstream work must not equate them.

### Quarter, subsequent events and contingencies

Evidence present for 2026 up to the filing of the Q2 10-Q: the three acquisitions and their consideration (CAC Group 1,220,213 thousand, Obie 287,370 thousand, Capstone 52,029 thousand; page:18); Amendment No. 4 with $600 million of incremental term loans on 2026-01-02 and about $12.0 million of debt issuance costs (page:25); a loss on extinguishment and modification of debt of 7,538 thousand for six months (page:7); recognition of Tax Receivable Agreement expense of $128.8 million (page:72) and an income tax benefit of 144,437 thousand for six months from a partial valuation allowance release (page:7, page:29-30); a held-for-sale plan for Media Guarantors, with a definitive sale agreement dated 2026-07-02 for $4.0 million of cash (page:46-47); and share repurchases of 3,839,937 shares in Q2 under the program (page:83). Disclosure controls were concluded effective at 2026-06-30 with no change in internal control (page:82-83); the FY2025 auditor's report states that the statements present fairly and that internal control over financial reporting was maintained effectively in all material respects (10-K page:128). Legal proceedings are stated as ordinary course with no material adverse effect expected (page:38). Item 3 of Part II, defaults upon senior securities, states "None" (page:83). Nothing in the pack is dated after 2026-07-30. No fact dated after 2026-11-05 is relied on.

The pack has no report for the quarter ended 2026-09-30. The context names Q2 2026 as the current period, so this is consistent with the request. Whether a later report exists at the as-of date is not known from the sources, and events between 2026-07-30 and 2026-11-05 are Not supplied, not absent.

### Consumer assessment

| Consumer | Evidence demand | Status | Carried limitations |
| --- | --- | --- | --- |
| CP-1 financial base | Discrete quarters and fiscal years, quarter versus year-to-date, segments, add-backs, facility-level debt and carrying values, cash-paid interest and tax, business and transaction narrative | READY_WITH_LIMITATIONS | Q4 2025 and last-twelve-months need derivation from stated periods; segment disclosures give net income only; 2025 comparatives exclude the January 2026 acquisitions; exact term loan principal appears only in the fair-value table; interest expense definition differs between statements and reconciliations; cash paid for interest and taxes is printed for six months 2026, nine months 2025 and FY2025, not for discrete quarters |
| CP-1A business and transaction context | Business, ownership, transaction and history facts | READY_WITH_LIMITATIONS | Acquisition agreements, the credit agreement amendments, the indenture and the Tax Receivable Agreement are not supplied; context has no sponsor, deal terms or ownership map; purchase accounting is provisional |
| CP-2 fundamental synthesis | Settled upstream registers plus the filings | READY_WITH_LIMITATIONS | Covenant ratio and definitions, guarantor map and ratings not supplied; ratings, quotes and peers in the context are empty |
| CP-5 evidence trace | Citations that resolve in the pinned sources | READY_WITH_LIMITATIONS | Depends on page-chunk locators; extraction fidelity not reviewed |

Missing downstream analytical handoffs are not treated as source conditions. The dependency planner sequences them.

### Extraction status and fidelity

Every source was retrieved as text chunks. I ran keyword searches across all seven sources and read targeted pages in full; I did not read every one of the 485 chunks. Tables arrived as flattened text, and column headers were checked against the period labels printed in each table I used. The pack has no image, chart or slide content (no presentations; the releases stand in for them). A successful extraction is not a fidelity review of every table, and none is claimed.

## Calculations

These are source tie-outs and counts only, in thousands of USD unless stated. No figure is normalized or reconciled for use downstream.

| Check | Inputs and locator | Result |
| --- | --- | --- |
| Chunk count across sources | 201 + 79 + 76 + 85 + 17 + 13 + 14 (chunk totals of the seven files) | 485 chunks over 7 files |
| Revolver availability, 2026-06-30 | $600 million commitments less $302.0 million drawn less $38.6 million letters of credit (10-Q Q2 2026 page:5, page:25) | $259.4 million, equal to the printed $259.4 million (page:74) |
| Revolver availability, 2026-03-31 | $600 million less $191.0 million less $16.0 million (10-Q Q1 2026 page:23) | $393.0 million, equal to the printed "$393 million" (page:65) |
| Revolver availability, 2025-12-31 | $600 million less $107.0 million less $16.0 million (10-K page:165) | $477.0 million, equal to the printed $477.0 million (page:110) |
| Debt carrying amount to balance sheet | 2,150,725 + 16,091 (10-Q Q2 2026 page:5, page:23) = 2,166,816; fair-value table 2,193,045 less 2,166,816 (page:38) | 26,229, consistent with the printed $26.2 million of unamortized discount and costs. The table's "carrying amount" is therefore the gross principal although its footnote calls it net |
| Implied Term Loan principal, 2026-06-30 | 2,193,045 less $600,000 notes (page:38, page:24) | 1,593,045 thousand, derived; consistent with the printed "$1.6 billion". Labelled derived, not printed |
| Dec 2025 debt table | 1,603,606 less 24,907 (10-K page:165) | 1,578,699, equal to 1,566,122 + 12,577 (10-K page:131, page:165) |
| Dec 2025 Term Loan principal | 1,603,606 less $600,000 notes | 1,003,606, consistent with the printed "$1.004 billion" (10-K page:165) |
| Revolver margin presentations | 175 + 10 and 250 + 10 bps (10-Q Q2 2026 page:24) | 185 and 260 bps, equal to the range printed at page:73 |
| Interest expense definition gap | Q2: 46,140 less 45,666; six months: 85,347 less 84,566; FY2025: 122,778 less 121,428 (release page:11; 10-Q page:7; 10-K page:99, page:132) | 474; 781; 1,350. Differences are consistent with the surplus-note interest income footnote at page:61 for 2026; the 10-K reconciliation prints no such footnote in the text read |
| Q1 2026 revenue by difference | 1,025,174 less 492,939 (10-Q Q2 2026 page:7) | 532,235, matches the Q1 release's $532.2 million (release page:1) |
| Q1 2026 adjusted EBITDA by difference | 253,988 less 116,740 (10-Q Q2 2026 page:61) | 137,248, matches the Q1 release's $137.2 million (release page:1) |
| Six-month net loss | 1.9 million (Q1 release page:1) + 56.0 million (Q2 release page:1) | 57.9 million, equal to the six-month loss of $57.9 million (Q2 release page:2) |
| Segment revenue, Q2 2026 | 275,343 + 160,247 + 75,327 + (17,978) (10-Q page:41) | 492,939, equal to consolidated total revenues |
| Segment net income, Q2 2026 | (1,279) + 6,693 + 3,764 + (65,159) (10-Q page:42) | (55,981), equal to consolidated net loss |
| Goodwill roll-forward | 1,517,171 + 1,134,895 + 341 (10-Q Q2 2026 page:23) | 2,652,407, equal to the balance sheet |
| Acquisition consideration | 1,220,213 + 287,370 + 52,029 (page:18) | 1,559,612, equal to the printed total and consistent with "$1.6 billion" (page:16) |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Covenant compliance, the reported total first lien net leverage ratio, the definition of Consolidated EBITDA and the conditions under which the 7.00x test applies are not supplied; searched covenant, 7.00, maintenance, springing, fixed charge and interest coverage across all seven sources; only the 10-K (page:164) describes the test | High | CP-1, CP-2 | Obtain the executed JPM Credit Agreement and its amendments, or the company's compliance disclosures |
| Executed legal documents (credit agreement and Amendments 1 to 4, indenture dated 2024-05-24, Tax Receivable Agreement, CAC Group Transaction Agreement and its amendment) not supplied; context legal_documents is none | High | CP-2, CP-5 | Add the documents named in the 10-K exhibit list (page:196-200) |
| Guarantors are described but not named (Exhibit 21.1 not in the pack); no stand-alone or issuer-group financial information; borrower is Baldwin Holdings but its statements are not separate | Medium | CP-2, CP-5 | Obtain the subsidiary list and guarantor information |
| Perimeter change: reported 2025 comparatives and FY2025 exclude CAC Group, Obie and Capstone; purchase accounting provisional (page:18) | High | CP-1, CP-2 | Use organic and pro forma measures (page:19-20, page:60) with labels; no recast annual base supplied |
| No report for the quarter ended 2026-09-30; events after 2026-07-30 not supplied | Medium | CP-1, CP-1A, CP-2 | Supply later filings if they exist before the cutoff, or confirm none |
| Segment adjusted EBITDA not disclosed in the segment note, which gives segment net income only (page:41) | Medium | CP-1, CP-2 | Treat segment cash earnings as not supplied |
| Principal maturity table at 2026-06-30 not printed; 10-K table is pre add-on (10-K page:165) | Medium | CP-1, CP-2 | Derive downstream from terms (quarterly $4.0 million, 2029 and 2031 maturities), labelled as derived |
| Ratings not supplied: the 10-K says agencies assign ratings (page:28) but no rating or agency is named; context ratings list is empty | Medium | CP-2 | Supply ratings if needed; not zero |
| Context blanks: borrower, parent, guarantors, sponsor, deal terms, quotes, peers, valuation inputs | Medium | CP-1A, CP-2 | Supply if wanted; not zero |
| Interest expense defined differently in statements and reconciliations | Low | CP-1, CP-5 | State which definition each ratio uses |
| Page-chunk locators are extraction chunks, not printed page numbers; no fidelity review of extracted tables; no presentations in the pack | Low | CP-5 | Spot-check key tables against the original htm if used externally |
| Management guidance has no GAAP reconciliation (Q2 release page:11) | Low | CP-2 | Treat as an attributed management claim |
| Pension and retiree medical, factoring and supply-chain finance: nothing found beyond a 401(k) plan; absence in the pack is not proof of absence | Low | CP-2 | Confirm in a later filing if material |

## Next module

Proceed to CP-1 first, then CP-1A, CP-2 and CP-5, in the order CP-OS plans. Every consumer is READY_WITH_LIMITATIONS and may run. Carry these instructions forward: use the Q2 2026 10-Q as the controlling source for the 2026-06-30 balance sheet, debt and six-month results, and the 10-K for FY2025; label every FY2025 and 2025 comparative figure as excluding the January 2026 acquisitions; take the $259.4 million of borrowing capacity as the company's stated figure, not as covenant headroom; treat the exact Term Loan principal as derived from the fair-value table; keep the interest expense definition difference visible; and keep the covenant ratio, guarantor map, ratings and later-period events as open gaps.
