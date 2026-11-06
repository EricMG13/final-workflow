## Request

Issuer: Wayfair Inc. (issuer id w; NYSE ticker W; Delaware registrant, SEC file number 001-36666). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, stated in millions in all seven sources. Current period: Q3 2026 (quarter ended 2026-09-30). Prior period named by the context: FY2025.

Question for this module: can the supplied source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion. It does not normalize, reconcile or calculate figures. Arithmetic below is limited to tie-outs that test source consistency, and it is not a liquidity, leverage or covenant conclusion.

The context file holds the run settings and is not issuer evidence. Its borrower, parent, guarantor, deal-term, quote, rating, valuation, peer and research-question fields are blank or empty, and its legal-documents attachment is set to none. Those blanks are treated as not supplied, never as zero.

## Sources

### Issuer sources relied on

Each file is a JSONL text extraction of an SEC filing or exhibit. The locator `page:N` is the extraction chunk, not the printed page. The sha256 below is the pinned file hash. The first line of each file also prints a different hash for the underlying htm document; that one is not used here.

| Source name | sha256 | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_w-20251231.htm.jsonl | 8ef4121e11689a0c5565962f85cfafc125f39e54e08df2c3b6c79eaf68e84e4d | Annual report on Form 10-K, 152 chunks; audited statements control their facts | Fiscal year ended 2025-12-31 (page:1); signed 2026-02-19 (page:152); FY2025 opinion by PricewaterhouseCoopers LLP (page:96, page:98) |
| 10-Q_2026-03-31_w-20260331.htm.jsonl | 79f74f0ba7972d92f75742a90568a879936b4ecf939af4026c967768203f5019 | Quarterly report on Form 10-Q, 45 chunks; unaudited condensed statements | Quarter ended 2026-03-31 (page:1); dated 2026-04-30 |
| 10-Q_2026-06-30_w-20260630.htm.jsonl | e52476a4ad53b4396b19ba631702cd30b522eb54aecabc978fa654467e46935a | Quarterly report on Form 10-Q, 57 chunks; unaudited condensed statements | Quarter and six months ended 2026-06-30 (page:1); dated 2026-08-04 |
| 10-Q_2026-09-30_w-20260930.htm.jsonl | 9224a05a14ec554aa7f19d7d2ae6869a07a996f1d60af972e32e1595aefdd8c3 | Quarterly report on Form 10-Q, 57 chunks; unaudited condensed statements; latest filed report | Quarter and nine months ended 2026-09-30 (page:1); signed 2026-11-04 (page:56) |
| EX-99.1_2026-04-30_a2026-04x30ex991.htm.jsonl | a3debc23ce5c3027daa8862793a0e092539f933475881f34dd98f47a74a5cd40 | Earnings release furnished as Exhibit 99.1, 13 chunks; management attribution, supporting claims only | Q1 2026, dated 2026-04-30 (page:1) |
| EX-99.1_2026-08-04_a2026-08x04ex991.htm.jsonl | bd4c1a88b49b8e4441931ccafc159f4e1f6d02b8d8bf7918ce20a28d44352f87 | Earnings release furnished as Exhibit 99.1, 13 chunks; supporting claims only | Q2 2026, dated 2026-08-04 (page:1) |
| EX-99.1_2026-11-04_a2026-11x04ex991.htm.jsonl | 2907d0c055207f89b1a08967b4ff5b2fe5bb05c815f0f3ad4e1479f1b9a353cb | Earnings release furnished as Exhibit 99.1, 12 chunks; supporting claims only | Q3 2026, dated 2026-11-04 (page:1) |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | e3b6fe003758c2152693bc3785d916a8d51266f353efa91b71daa0110cb48520 | Run settings only; not issuer evidence |

### Supplied handoffs

None. CP-0 is the first module in this run, so the handoff set is empty.

### Ignored file

`_retrieval.json` sits in the pack folder and is not a pinned source. It is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The pack supports the requested work on Wayfair Inc. through the third quarter of 2026, with bounded limits. Executed debt documents, covenant ratios and guarantor lists are not supplied, so legal terms rest on filing summaries. | Medium | The credit agreement, indentures and reported covenant ratio are not in the pack; the covenant level is known only from filing text. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The annual report, three quarterly reports and three releases cover FY2025 through Q3 2026 in US dollars, with statements, debt note and liquidity table located. | A financial base, debt picture and liquidity view can be built from filed statements without outside data. | High |
| Convertible notes are issued by the parent, while the secured notes and the revolver sit at a subsidiary; guarantors are not named in full. | Ranking of each claim and structural subordination of the convertible notes need the executed documents, which are not supplied. | Medium |
| One maintenance test is named, a senior secured leverage cap, and the reported ratio and headroom are not printed. | Covenant headroom cannot be measured from the pack; only the stated compliance can be carried forward. | High |
| The 2027 convertible notes became convertible for the fourth quarter of 2026, and an equity instrument settled for cash after quarter end. | Cash settlement of conversions and share-repurchase outflows can draw on liquidity; they must be carried as open items. | Medium |
| Ratings, market prices and executed legal documents are not supplied, and the Canadian customs matter appears only in the annual report. | Relative-value and rating-based work cannot proceed, and the customs exposure is not updated after year end. | High |

### Readiness view

The effective source set supports the requested work with limitations. All four consumers are assessed as READY_WITH_LIMITATIONS, none CONDITIONAL and none BLOCKED. The audited annual report, three quarterly reports and three earnings releases cover the periods the context names, in the reporting currency, up to the evidence cutoff, and the latest filed report is signed on 2026-11-04. The binding limitations are four. First, no executed legal document is in the pack, so the covenant, guarantor, security and indenture terms rest on filing summaries, and the reported value of the one named financial covenant is not printed. Second, the debt sits at more than one legal entity (parent convertible notes; subsidiary secured notes and revolver) and the guarantor group is not listed, so the claim-by-claim map is incomplete. Third, no fidelity review of the text extraction has been done, and the pack has no slides or images. Fourth, no credit rating, market price or peer data is supplied. None of these prevents the owners from running their methods, but each must be carried forward as stated in the consumer assessment and gaps below.

### Source-by-source assessment

All seven sources identify Wayfair Inc. as the registrant or the announcing company (page:1 of each). No source is blocked, draft, unsigned or an exact duplicate of another. The 10-K is audited; the three 10-Qs are unaudited and condensed. The filed 10-K and 10-Qs control their own facts. The three releases are management claims that must not override the filings, and each repeats the statements already in the matching 10-Q. Base, amendment, waiver and supplement documents do not arise: no legal document of any kind is in the pack.

| Source | What it supports (locators) | Limit |
| --- | --- | --- |
| 10-K FY2025 | Business (page:9); balance sheet (page:99-100); statement of operations (page:100); cash flows (page:101); Adjusted EBITDA reconciliation (page:88); free cash flow reconciliation (page:89); debt note (page:118-131); contractual obligations (page:83-84); commitments and legal (page:132-133); segments (page:142) | Year-end 2025 only; auditor changed (PricewaterhouseCoopers LLP signed FY2025 at page:98; Ernst & Young LLP covered FY2024 and earlier at page:99) |
| 10-Q Q1 2026 | Quarter ended 2026-03-31 statements (page:2-5); debt note with total debt (page:9); liquidity table (page:31); covenant text (page:34) | Superseded by later reports for balance sheet facts |
| 10-Q Q2 2026 | Quarter and six months statements (page:2-4); debt note and 2034 Secured Notes (page:10-16); covenant text (page:42); exhibit list naming the May 2026 indenture (page:56) | Superseded by the Q3 report for balance sheet facts |
| 10-Q Q3 2026 | Balance sheet (page:2); statement of operations (page:3); cash flows (page:4-5); debt note (page:10-17); legal matters (page:17); stockholders' deficit and repurchases (page:18); segments (page:22); liquidity and covenants (page:39-42); contractual obligations (page:44-45); Adjusted EBITDA and free cash flow reconciliations (page:49-50); legal proceedings and exhibits (page:54-56) | Condensed; defers to the 10-K for accounting policies and contractual obligation detail (page:6, page:45) |
| EX-99.1 2026-04-30 | Q1 2026 highlights and statements (page:1-12) | Management claims; Q1 only |
| EX-99.1 2026-08-04 | Q2 2026 highlights and statements (page:1-12) | Management claims; Q2 only |
| EX-99.1 2026-11-04 | Q3 2026 highlights, statements, segment Adjusted EBITDA and reconciliations (page:1-12) | Management claims; superlative wording is not independently verifiable from the pack |

### Entity and perimeter

The registrant and reporting entity is Wayfair Inc., with its financial statements stated to be those of "Wayfair Inc. and its wholly-owned subsidiaries" (Q3 10-Q page:6). The context names no borrower, parent or guarantor, and a search of the sources for "parent" found no corporate parent of Wayfair Inc. Two reportable segments are given, the U.S. and International (Q3 10-Q page:22).

Debt roles as the filings print them:

- Revolver: the 10-K says "Wayfair LLC, a subsidiary of Wayfair, as borrower", with Wayfair and "certain of its subsidiaries" as the Guarantors, and first-priority liens on substantially all assets of the Borrower and the Guarantors (10-K page:119). Administrative agent and collateral agent is Citibank, N.A. (page:119).
- Senior Secured Notes: Wayfair LLC is the Issuer of the 2029, 2030, 2032 and 2034 secured notes, under indentures that name guarantors "including Wayfair" (10-K page:121-122; Q2 10-Q page:12 for the 2034 series; the Q3 10-Q page:41 repeats that Wayfair LLC issued the 2034 series). The notes rank pari passu with the revolver on the same first-priority liens (10-K page:130).
- Convertible Notes: the 10-K says "The Convertible Notes are general senior unsecured obligations of Wayfair" and "structurally subordinated to all existing and future indebtedness and liabilities of" Wayfair's subsidiaries (10-K page:130); the indentures "also include Wayfair LLC, as guarantor" (page:125). Only the 2027 Notes remain outstanding at 2026-09-30 (Q3 10-Q page:10-11).

Unresolved distinctions, kept as gaps and not as conclusions: the "certain of its subsidiaries" that guarantee are not listed; the Q3 10-Q does not repeat the guarantor description for the revolver or the notes; the restricted versus unrestricted subsidiary split used in the secured-note indentures is not supplied; and no guarantor or non-guarantor financial information is in the pack (search below).

### Period basis and version relationships

All seven sources are on one perimeter (consolidated Wayfair Inc.), one currency (USD, millions) and one accounting basis (GAAP, with management non-GAAP measures labelled as such). A search of all seven sources for "discontinued operation" and "held for sale" returned no hit, and no restated or recast statement was found (the 10-K hits for "restated" are the amended and restated credit agreement and exhibit titles), so no perimeter change is evident. For net revenue, the prior-year quarterly columns in the Q1 and Q2 reports sum to the nine-month 2025 amount in the Q3 report (tie-out below); other prior-year lines were not re-tested.

Discrete periods available: Q1 2026 (Q1 10-Q page:2, release page:2), Q2 2026 (Q2 10-Q page:2, release page:2), Q3 2026 (Q3 10-Q page:3) and the nine months to 2026-09-30, each with a prior-year comparative column; FY2025, FY2024 and FY2023 annual columns (10-K page:100). Q4 2025 as a stand-alone quarter is not printed anywhere in the pack: no fourth-quarter release or report is supplied, so it is derivable only as FY2025 less nine months 2025, which is downstream work and is not done here. A last-twelve-months view to 2026-09-30 can be built from FY2025, nine months 2026 and nine months 2025 for net revenue, Adjusted EBITDA, free cash flow and cash interest; each of those components is printed.

Quarter versus year-to-date: the Q3 report prints both three-month and nine-month columns side by side (page:3), and the Q3 cash flow statement is nine months only (page:4). Quarterly cash flow therefore needs the Q2 report's six-month column to be subtracted downstream. Cash paid for interest is printed for each cumulative period (Q1 10-Q page:4; Q2 10-Q page:4; Q3 10-Q page:5; 10-K page:101). Cash taxes paid are not printed in the interim reports; the 10-K gives FY2025 only, as state and foreign payments (page:137).

Management claims to carry with attribution only: the Q3 release calls the 6.9% Adjusted EBITDA Margin "our best Q3 result since 2020" and Q3 "our strongest quarter of growth in the post-pandemic period" (page:1), and the Q2 release headline reports "Strongest Free Cash Flow Since 2020" (page:1). The pack holds only the current and prior-year quarters, so these multi-year comparisons cannot be checked and are not relied on.

### Debt and liquidity evidence present

The Q3 10-Q debt note (page:10-17) gives, at 2026-09-30 and 2025-12-31, in millions: principal, unamortized discount and net carrying amount for the revolver (nil drawn), 2026 Notes, 2027 Notes, 2028 Notes, 2029, 2030, 2032 and 2034 Secured Notes. Total debt carrying amount is 2,799 (2025-12-31: 3,272), of which short-term 227 and long-term 2,572 (page:11). Coupons, maturity dates, effective rates and interest dates for the four secured series and the 2027 Notes are tabulated (page:11), as are conversion terms for the 2027 Notes (initial conversion price $63.45, free convertibility from June 15, 2027; page:12) and the capped calls (page:16). Fair values at 2026-09-30 are printed for each outstanding series (page:15). The 10-K and the Q2 10-Q give the issuance terms of the secured notes (10-K page:121-122; Q2 10-Q page:12).

Revolver: US$500 million, matures March 13, 2030, no loans outstanding, and US$82 million of letters of credit (mostly lease security) reduce availability (Q3 10-Q page:11, page:39). The 10-K also says the maturity is "subject to a springing earlier maturity in certain circumstances" without stating the trigger (page:119). Margin at 2025-12-31 is 1.25% for Term SOFR loans (10-K page:120); no later margin is printed.

Liquidity: the 10-Q table shows cash and cash equivalents of 1,038 and short-term investments of 60, total 1,098, which excludes the revolver (page:39). The release states "total liquidity was $1.5 billion, including availability under our revolving credit facility" (release page:1). All inputs for a liquidity build by component are printed: cash, short-term investments, revolver size, letters of credit, and the cash, cash equivalents and restricted cash line of the cash flow statement (page:4).

The 2027 Notes: conditional conversion was triggered in the quarter ended 2026-09-30, so they are convertible during the quarter ending 2026-12-31 (page:13, page:41); the if-converted value exceeded principal by 141 (page:15); settlement may be in cash, shares or a combination at the company's election (page:13). This is evidence for downstream cash-need analysis, not a conclusion here.

Other claims outside the debt note that are located: operating lease liabilities of 864 non-current (page:2) and lease obligations of 110 for leases not yet commenced (page:8, page:45); a logistics lease termination that reduced lease obligations by 138 (page:8); purchase obligations of 649 at 2025-12-31 for software licence and freight commitments (10-K page:84, page:132); the 10-K contractual obligations table at 2025-12-31 (page:83-84), which the Q3 report says has had no material change other than the financing transactions (page:45). No finance lease arrangements were material at 2025-12-31 (10-K page:106). Retirement benefits are a defined-contribution 401(k) plan (10-K page:133). No pension, factoring, supply-chain finance or rating-agency item appears (search results in Gaps).

### Quarter, subsequent events and contingencies

Located for the latest quarter and after, to the cutoff: the 2026 Notes matured on August 15, 2026 and 39 was paid in cash (Q3 10-Q page:13); the 2027 Notes conversion trigger above; share repurchases of 60 under the 2020 program (page:18); an equity instrument for 60 that "was settled on October 28, 2026, resulting in a cash settlement of $64 million" (page:18, page:42), a post-quarter-end event dated before the cutoff; and Class A shares outstanding of 115,862,125 at October 28, 2026 (page:1). Earlier in 2026: repurchases and redemptions of the 2028 and 2027 Notes with loss on debt extinguishment, and the $400 million 2034 Secured Notes issued May 18, 2026 (page:14-15, page:41). Litigation: ordinary-course matters, accruals recorded and "fully insured for a majority of these matters" (page:17); no amounts are quantified there, and the Q3 report says no material change in risk factors (page:55). The Canada Border Services Agency review and customs examinations are described in the 10-K only (page:132-133) and are not mentioned in any 2026 report. Nothing dated after 2026-11-05 is relied on; the Q3 release and report are dated 2026-11-04, one day before the as-of date, and nothing dated between is supplied.

### Consumer assessment

| Consumer | Evidence demand | Status | Carried limitations |
| --- | --- | --- | --- |
| CP-1 financial base | Discrete quarters, annual base, segments, add-backs, KPIs, facility-level debt, cash interest and tax, business narrative | READY_WITH_LIMITATIONS | Q4 2025 stand-alone quarter is not printed; interim cash flows are cumulative; cash taxes paid are annual only (10-K page:137); lease claims sit outside the debt table; no recast or restatement to reconcile |
| CP-1A business and transaction context | Business model, segments, ownership, financing history, capital actions | READY_WITH_LIMITATIONS | Indentures, credit agreement and the 2026 8-K exhibits are not supplied; descriptions come from filings and releases; no sponsor, deal term or ownership map in the context |
| CP-2 fundamental synthesis | CP-1 and CP-1A handoffs plus covenant, liquidity and maturity evidence | READY_WITH_LIMITATIONS | Reported covenant ratio, guarantor list, springing maturity trigger and ratings not supplied; convertible and equity-instrument cash needs must be carried as open items |
| CP-5 evidence trace | Claims that resolve to located text in the pinned sources | READY_WITH_LIMITATIONS | Locators are extraction chunks (page:N), not printed pages; no fidelity review of flattened tables; releases are supporting claims only |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN. Missing downstream analytical handoffs are not treated as source conditions; the dependency planner sequences them.

### Extraction status and fidelity

Every source was retrieved as text chunks and read by search and targeted page reads. Tables arrive as flattened text, and column headers were checked against the period labels printed beside each table. The pack contains no slides, images or charts, so no image-content coverage is claimed. A successful extraction is not a fidelity review of every table, and none is claimed.

## Calculations

These are source tie-outs only, in millions of USD unless stated. No figure is normalized.

| Check | Inputs and locator | Result |
| --- | --- | --- |
| Debt carrying amounts add to total, 2026-09-30 | 227 + 791 + 693 + 693 + 395 (Q3 10-Q page:10-11) | 2,799, equal to printed Total Debt |
| Short-term plus long-term debt, 2026-09-30 | 227 + 2,572 (page:11) | 2,799, equal |
| Debt carrying amounts add to total, 2025-12-31 | 39 + 477 + 583 + 789 + 692 + 692 (page:10-11) | 3,272, equal to printed Total Debt and to 10-K page:118 |
| Principal, 2026-09-30 | 229 + 800 + 700 + 700 + 400 (page:10-11) | 2,829, consistent with the text "$2.8 billion principal amount" (page:11) |
| Principal bridge 2025-12-31 to 2026-09-30 | 39 + 480 + 589 + 800 + 700 + 700 = 3,308 at year end; less 39, 251 and 589, plus 400 | 2,829, equal to the printed principal. The 2027 Notes fall from 480 to 229 although the narrative gives 250 redeemed (page:14); the Q1 10-Q shows 230 (page:8) and the Q2 10-Q shows 229 (page:10). A reduction of 1 in Q2 is not explained in the text searched. It is small and is a variance to carry, not a conflict |
| 2028 Notes retired | 56 + 89 repurchased (page:14) + 444 redeemed (page:14-15) | 589, equal to the year-end principal; no 2028 Notes remain (page:15) |
| Cash and short-term investments | 1,038 + 60 (page:2, page:39) | 1,098, equal to printed liquidity excluding the revolver |
| Revolver availability, arithmetic only | 500 less 0 drawn less 82 letters of credit (page:11) | 418; with 1,098, a total of 1,516, consistent with the release wording "$1.5 billion". This is a consistency check, not a liquidity conclusion and not covenant headroom |
| Release liquidity wording in earlier quarters | Q1: 1,062 + 500 - 90 (Q1 10-Q page:9, page:31); Q2: 1,143 + 500 - 82 (Q2 10-Q page:2, page:12) | 1,472 and 1,561, consistent with "$1.5 billion" and "$1.6 billion" in the Q1 and Q2 releases (page:1) |
| Net revenue by quarter | 2,931 + 3,519 + 3,420; prior year 2,730 + 3,273 + 3,117 | 9,870 and 9,120, equal to the nine-month columns (Q3 10-Q page:3) |
| Adjusted EBITDA by quarter | 151 + 242 + 236 (Q1 10-Q page:25; Q2 10-Q page:29; Q3 release page:11) | 629, equal to nine months 2026 |
| Adjusted EBITDA reconciliation, nine months 2026 | -44 + 195 + 209 + 120 + 14 + 7 + 2 + 24 + 102 (release page:11) | 629, equal |
| Segment Adjusted EBITDA | 261 + (25) and 683 + (54) (release page:11) | 236 and 629, equal |
| Segment net revenue | 3,040 + 380 and 8,777 + 1,093 (release page:6) | 3,420 and 9,870, equal |
| Free cash flow | 198 - 30 - 32 and 506 - 81 - 94 (release page:12) | 136 and 331, equal; quarterly (106 negative) + 301 + 136 = 331 |
| Net income by quarter | (105) + (1) + 62 (Q1 and Q2 releases page:1; Q3 release page:1) | (44), equal to the nine-month figure |
| Balance sheet, 2026-09-30 | Assets 1,675 + 881 + 533 + 62; liabilities 2,496 + 2,572 + 864 + 23 (page:2) | 3,151 and 5,955, equal to printed totals; deficit (2,804) = 3,151 - 5,955 |
| Interest, nine months 2026 | Contractual interest 143 + amortization 6 (page:15) less interest income 30 (page:9) | 119 against 120 printed as interest expense, net (page:3); the difference of 1 is within rounding of three rounded inputs |
| Post-quarter cash settlement | 64 cash against 60 carried in equity (page:18) | Difference of 4 is stated by the filing as the cash settlement; the cause is not explained |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed credit agreement, indentures (including the 2034 indenture dated 2026-05-18), capped call confirmations and lease agreements are not supplied; the context sets legal documents to none | High | CP-2, CP-5 | Add the executed documents or their 8-K exhibits; until then legal terms are filing summaries |
| Covenant: the one maintenance test named is a Consolidated Senior Secured Debt to Consolidated EBITDA Ratio of "no more than 4.0 to 1.0", with a 0.5 step-up after certain permitted acquisitions, introduced by "For instance" (Q3 10-Q page:42); the 10-K risk factors refer to "financial covenants" in the plural (page:53), so other tests are not excluded. The reported ratio, the definition and any other test are not printed; all seven sources were searched for the covenant name, "financial covenant", leverage, coverage and fixed charge ratios, and "compliance". Only a compliance statement is given | High | CP-1, CP-2 | Obtain the credit agreement for the definition; do not compute headroom from non-GAAP Adjusted EBITDA |
| Guarantor group: "certain of its subsidiaries" are Guarantors and are not named; no guarantor or non-guarantor summary financial information is in the pack (a search of all seven sources for "guarantor" returned only the 10-K and Q2 10-Q passages cited, none in the Q3 10-Q, and a search for "summarized financial" returned nothing) | Medium | CP-2, CP-5 | Obtain the indenture schedules or the exhibit 21 subsidiaries list |
| Restricted versus unrestricted subsidiary designations under the secured-note indentures are not supplied | Medium | CP-2 | Obtain the indentures |
| Springing maturity trigger of the revolver is not described ("subject to a springing earlier maturity in certain circumstances", 10-K page:119); the Q3 10-Q states only the March 13, 2030 maturity | Medium | CP-2 | Obtain the credit agreement |
| Q4 2025 stand-alone quarter is not printed; no fourth-quarter release or 8-K is in the pack | Medium | CP-1 | Derive downstream as FY2025 less nine months 2025, labelled as derived |
| Contractual obligations table is as of 2025-12-31 only (10-K page:83-84); no maturity table at 2026-09-30, although the debt note supports building a maturity wall from principal and dates | Low | CP-1, CP-2 | Build the wall from Note 4 principal and maturity dates, labelled as derived |
| Interim cash flows are cumulative only; discrete Q2 and Q3 cash flows need subtraction; cash taxes paid are not printed in the three 10-Qs (search for "cash paid for" returned interest only) | Low | CP-1 | Subtract downstream and label; use the 10-K for FY2025 taxes paid |
| Credit ratings are not supplied: a search of all seven sources for Moody, Standard & Poor, S&P and Fitch returned no hit, "credit rating" appears only in a generic 10-K risk-factor sentence (page:54), and the context ratings list is empty | Medium | CP-2 | Supply agency ratings if rating-based work is wanted |
| Market data is not supplied: the context quotes, valuation and peer fields are blank; no share-count-times-price market capitalization is in the pack | Medium | CP-2 | Supply dated market data if valuation or relative value is wanted |
| Canada Border Services Agency review and customs examinations are described in the 10-K only (page:132-133); a search of the three 10-Qs for "CBSA" and "Canada Border" returned nothing, so the post-year-end status is unknown | Medium | CP-2 | Check later filings, or carry as an open contingent claim |
| Litigation accruals and the insurance recovery receivable are described but not quantified (Q3 10-Q page:17) | Low | CP-2 | Carry as unquantified |
| The 2027 Notes 1 reduction in principal between Q1 and Q2 2026 is not explained in the text | Low | CP-1 | Check against the indenture or later notes |
| No presentations: the pack holds earnings releases in place of slides, all text only; no chart or image content exists to inspect | Low | CP-5 | None needed for this scope |
| Page-chunk locators are extraction chunks, not printed page numbers; no fidelity review of the flattened tables | Low | CP-5 | Spot-check key tables against the original htm if used externally |
| Management superlatives in the releases cannot be checked against a multi-year quarterly series in the pack | Low | CP-2, CP-5 | Treat as attributed management claims |

## Next module

Proceed to CP-1 first, then CP-1A, CP-2 and CP-5, in the order CP-OS plans. Every consumer is READY_WITH_LIMITATIONS and may run. Carry these instructions forward:

- Treat the Q3 2026 10-Q as the controlling source for the 2026-09-30 balance sheet, debt note and nine-month results, and the 10-K as the audited source for FY2025. Treat the three releases as supporting management claims.
- Keep three legal entities distinct when mapping debt: Wayfair Inc. issues the convertible notes; Wayfair LLC is the Borrower of the revolver and Issuer of the secured notes; the guarantors are only partly named. Do not describe the guarantor group as known.
- Keep quarter, nine-month and annual figures apart. Label any Q4 2025 stand-alone figure and any last-twelve-months figure as derived, and show their inputs.
- Carry the senior secured leverage test as a named covenant with no reported ratio. Do not build headroom from Adjusted EBITDA, which is a management non-GAAP measure.
- Carry the 2027 Notes conversion status for the quarter ending 2026-12-31, the if-converted excess of 141, and the October 28, 2026 cash settlement of 64 as open cash items, and the 1 variance in 2027 Notes principal as a small unexplained difference.
- Keep lease obligations, purchase obligations and the unquantified litigation and customs matters as claims outside the debt figure, and keep ratings, market data and executed legal documents as Not supplied.
