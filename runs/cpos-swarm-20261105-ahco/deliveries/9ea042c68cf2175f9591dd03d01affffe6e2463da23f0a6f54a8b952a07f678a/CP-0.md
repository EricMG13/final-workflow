## Request

Issuer: AdaptHealth Corp. (issuer id ahco; Nasdaq ticker AHCO; Delaware registrant, SEC file number 001-38399). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD; the filings state amounts in thousands of US dollars and the narrative in millions. Current period: Q3 2026 (quarter ended 2026-09-30). Prior period named by the context: FY2025.

Question for this module: can the supplied source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion. It also does not normalize, reconcile or calculate figures. Arithmetic below is limited to tie-outs that test source consistency.

The context file holds the run settings and is not issuer evidence. Its deal terms, quotes, ratings, peers, precedents and research questions are all empty, and it lists no borrower, parent or guarantor. Those blanks are treated as not supplied, never as zero.

## Sources

### Issuer sources relied on

Each file is one JSONL extraction of an SEC filing, and the locator `page:N` is the extraction chunk, not the printed page. The sha256 below is the pinned file hash. Each file also prints its own hash for the underlying htm document in its first line; that is a different hash and is not used here.

| Source name | sha256 | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_ahco-20251231.htm.jsonl | ab2ec08f93eea99a2c9d582aaa2f8bd4d1c4f2aa62641d3b784e702a3bdcc76c | Audited annual report, Form 10-K, 207 chunks; filed statements control their facts | Fiscal year ended 2025-12-31; four reportable segments including Diabetes Health (page:5, page:98); pre-recast |
| 10-Q_2026-03-31_ahco-20260331.htm.jsonl | cc01aa88546035b041251eaca53354757481e77019d2aa4177a669ddd6279ff0 | Unaudited quarterly report, Form 10-Q, 69 chunks | Q1 2026; four reportable segments (page:7, page:19); pre-recast |
| 10-Q_2026-06-30_ahco-20260630.htm.jsonl | 6f9505a3792b53d02437ac824331bcd7d04f44b090fdd001f46d6c8128891c95 | Unaudited quarterly report, Form 10-Q, 92 chunks | Q2 2026 and six months; three reportable segments with Diabetes Health shown as held for sale (page:3, page:8, page:25); recast |
| 10-Q_2026-09-30_ahco-20260930.htm.jsonl | 9972ed3f9dddf422ff2b662dabdd681108366e28bd8c4ae70359b4ed7246cede | Unaudited quarterly report, Form 10-Q, 97 chunks; signed 2026-11-03 (page:97) | Q3 2026 and nine months; three reportable segments, Diabetes Health in discontinued operations for all periods (page:9, page:27); recast |
| EX-99.1_2026-05-05_ahco-20260505x8k_ex991.htm.jsonl | f3ab001bcc2c9ba7977e50b28183c49771c9b8a0719329baefd53ef80e8618f7 | Earnings release exhibit; management attribution, supporting claims only | Q1 2026; four segments, pre-recast (page:2) |
| EX-99.1_2026-08-04_ahco-20260804x8k_ex991.htm.jsonl | 0b36996a99a75e0d1a0ef0e6f97fbb42fdcb41f16a689bade487fa2dab0dc23a | Earnings release exhibit; supporting claims only | Q2 2026; continuing-operations basis excluding Diabetes Health (page:1, page:3) |
| EX-99.1_2026-11-03_ahco-20261103x8k_ex991.htm.jsonl | 8001e1aa0b352faa53a1b3726a1c918e40448a376cbe7f6418edd3708c625e0c | Earnings release exhibit; supporting claims only | Q3 2026; continuing-operations basis; guidance (page:1, page:2) |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 5c0b7cfd7056b03b072c2e872e8a22a98d7b1d4547009d9470e718056f435868 | Run settings only; not issuer evidence |

### Supplied handoffs

None. This is the first module in the run, so the handoff set is empty.

### Ignored file

_retrieval.json sits in the pack folder and is not a pinned source. It is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filings and releases through the latest quarter are enough to build the financial base, debt picture and business context, with bounded limits. The credit agreement, notes indentures and covenant levels are not supplied. | Medium | Covenant thresholds and the credit agreement are not in the pack, and the diabetes carve-out changes comparability. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The Diabetes Health business is now reported as discontinued operations in the latest two quarterly reports, but not in the annual report or the first-quarter report. | Prior-period and annual figures cannot be compared with current figures without a recast annual base, which is not supplied. | High |
| Debt terms are printed in the latest quarterly report, including the April 2026 refinancing and the redemption of the 6.125% notes. | Facility sizes, balances, amortization and maturities can be set out from the filing. | High |
| Covenant names are given but their levels and the reported ratios are not printed anywhere in the pack. | Covenant headroom cannot be measured, only the borrowing capacity the company states. | High |
| A cybersecurity incident, open government investigations and a consumer class action settlement awaiting court approval are disclosed, with financial impact undetermined for the incident. | These are unquantified contingent claims that downstream work must carry as limits. | Medium |

### Readiness view

The effective source set supports the requested work with limitations. The four requested consumers are all assessed as READY_WITH_LIMITATIONS, none CONDITIONAL and none BLOCKED. The audited annual report, three quarterly reports and three earnings releases cover the periods the context names, in the reporting currency, up to the evidence cutoff. The binding limitations are four. First, the annual report and the first-quarter report precede the Diabetes Health discontinued-operations recast, so the annual base and the current base differ in perimeter. Second, no executed legal document is in the pack, so covenant levels, guarantor lists and security terms rest on filing summaries. Third, no fidelity review of the text extraction has been done, and chart or image content was not inspected. Fourth, the cybersecurity incident and the investigations carry unquantified exposure. None of these blocks a consumer from starting, and each carries forward as a stated limit.

### Source-by-source assessment

All seven sources identify AdaptHealth Corp. as the registrant or the announcing company (page:1 of each). No source is blocked, draft, unsigned or a duplicate of another. The quarterly statements are unaudited. The filed 10-K and 10-Qs control their own facts. The three releases are management claims that must not override the filings.

| Source | What it supports | Limit |
| --- | --- | --- |
| 10-K FY2025 | Audited statements (auditor report at page:121-122), four-segment results (page:98), Adjusted EBITDA reconciliation (page:96), debt note (page:167-170), exhibit list naming AdaptHealth LLC as indenture and credit agreement party (page:202-203) | Includes Diabetes Health in continuing operations; no recast version supplied |
| 10-Q Q1 2026 | Quarter ended 2026-03-31 statements, four segments (page:7, page:19), debt and the April 2026 refinancing described (page:26-28, page:59-60) | Same pre-recast perimeter as the 10-K |
| 10-Q Q2 2026 | Cash 43,289 and held-for-sale assets 168,098 at 2026-06-30 (page:3), goodwill impairment 144,236 (page:4), three segments (page:8, page:25) | Does not carry Q3 events |
| 10-Q Q3 2026 | Latest statements (page:3-8), discontinued-operations note (page:27), segments (page:29-32), goodwill (page:33-34), debt (page:38-43), contingencies (page:52-56), subsequent events (page:57), Adjusted EBITDA reconciliation (page:74-76), liquidity (page:85-93) | Covenant levels not printed |
| EX-99.1 2026-05-05 | Q1 highlights and original FY2026 guidance on the four-segment basis (page:1-2) | Guidance superseded |
| EX-99.1 2026-08-04 | Q2 highlights, revised guidance on the continuing basis (page:1-3) | Guidance superseded |
| EX-99.1 2026-11-03 | Q3 highlights and revised guidance (page:1-2) | Management claims; guidance has no GAAP reconciliation (page:7) |

### Entity and perimeter

The registrant and reporting entity is AdaptHealth Corp. and its subsidiaries, consolidated (Q3 10-Q page:10). The Q3 10-Q describes the debt as the Company's, and one passage names AdaptHealth LLC as holding the 1,100.0 million of unsecured senior notes (page:87). The 10-K exhibit list names AdaptHealth LLC as party to the note indentures and the earlier credit agreement (page:202-203). The Q3 10-Q says guarantors party to supplemental indentures dated 2026-05-28 guaranteed the 5.125% and 4.625% notes (page:42-43). The pack does not name those guarantors, does not name the borrower under the 2026 Credit Agreement, and has no subsidiaries exhibit text. The issuer-versus-borrower-versus-guarantor map is therefore an unresolved gap, not a conclusion. The context names no borrower, parent or guarantor.

AdaptHealth Corp. is party to a Tax Receivable Agreement with members of AdaptHealth Holdings LLC (page:50), and cash payments under it were 26,846 thousand in the nine months of 2026 (page:7). The 10-K flags legal and contractual restrictions in subsidiary debt agreements that may limit upstream cash (page:67).

### Period basis and version relationships

The perimeter changes across the pack. The 10-K, the Q1 10-Q and the Q1 release report four segments with Diabetes Health inside continuing operations. The Q2 10-Q, Q3 10-Q, Q2 release and Q3 release treat Diabetes Health as held for sale or discontinued. The definitive sale agreement is dated 2026-07-19 for 235.0 million in cash, expected to close in the first quarter of 2027 (Q3 10-Q page:27). The Q3 10-Q presents 2025 comparatives recast (page:9, page:27, page:29), but there is no recast FY2025 income statement, segment table or Adjusted EBITDA reconciliation. Only the 2025-12-31 balance sheet is recast, through held-for-sale lines (Q3 10-Q page:3-4). A last-twelve-months figure on the current perimeter cannot be built from the pack without such a base.

Total FY2025 net revenue in the 10-K is 3,244,857 thousand including Diabetes Health segment revenue of 592,413 thousand (page:98). The 10-K Adjusted EBITDA is 616,681 thousand (page:96). Those are pre-recast and must not be set beside the Q3 2026 nine-month continuing figures of 2,165,828 thousand revenue and 378,462 thousand Adjusted EBITDA (Q3 10-Q page:74-76) as like for like. The shared-cost reallocation across segments on recast (page:29) makes a simple subtraction of the Diabetes segment unreliable.

Two discrete-quarter facts follow. Q2 2026 and Q3 2026 are on the recast basis in their own reports. Q1 2026 on the recast basis is not supplied as a stand-alone figure; it would need derivation from the six-month and Q2 figures, which is downstream work, not done here.

The Q3 release's headline "net loss attributable to AdaptHealth Corp." of 168.2 million (page:1) is a continuing-operations measure net of noncontrolling interest. The 10-Q statement of operations shows total net loss attributable of 153,987 thousand, which includes 14,259 thousand of discontinued-operations income (page:5). The tie-out is in Calculations. The two are not a conflict, but a reader who picks one without the label will mislabel the period result.

### Debt and liquidity evidence present

The Q3 10-Q debt note (page:38-43) gives the following at 2026-09-30, in thousands unless stated: secured term loans 647,969, revolving credit facility 147,000, senior unsecured notes 1,100,000, unamortized deferred financing fees (11,112), total 1,883,857, current portion 16,250, long-term portion 1,867,607. The 2026 Credit Agreement of 2026-04-10 has a 325.0 million term loan, a 325.0 million delayed draw term loan and 450.0 million of revolving commitments with a 75.0 million letter of credit sublimit; maturity is April 2031 with a springing maturity 91 days before the 4.625% and 5.125% notes if more than 150.0 million of them remain outstanding (page:40). Letters of credit outstanding are 34.3 million and the maximum revolver borrowing the company states is 268.7 million (page:42). Cash is 80,687 thousand (page:3). In October 2026 the company repaid 10.0 million, leaving 137.0 million outstanding on the revolver as of the filing date (page:86). The 6.125% notes were redeemed in full on 2026-08-03 using the delayed draw term loan and cash (page:43, page:89). New interest rate swaps with a notional of 100 million and an October 2028 maturity were entered into in October 2026 (page:38, page:57).

The pack does not give: covenant levels or step-downs; the reported leverage and coverage ratios; a maturity table for the term loans beyond the stated amortization schedule; the interest rate on the revolver; the fair value of the debt at 2026-09-30 (the 10-K gives fair values at 2025-12-31 only, page:137); or the issuer of each instrument beyond the passages cited above.

### Quarter, subsequent events and contingencies

Evidence present for the latest quarter and the period after it: the diabetes sale agreement, expiry of the Hart-Scott-Rodino waiting period before 2026-09-30 (page:27); deconsolidation of the eCommerce subsidiary into a joint venture on 2026-07-29 with a 12,002 thousand gain and a 42.5 million equity-method carrying value (page:16-17); goodwill impairment of 184,751 thousand in Q3 and 328,987 thousand for nine months (page:4), allocated to Respiratory Health and Wellness at Home (page:33-34); a restructuring plan of June 2026 costing 6.1 million (page:57); a cybersecurity incident disclosed on 8-K of 2026-07-02, with full financial impact not yet determined (page:60-62); a settled shareholder class action funded by 34.0 million of insurance cash and 1.0 million of company cash (page:52-53); a North Carolina consumer class action with a proposed 14.5 million settlement, a remaining liability of 14.1 million and a court hearing set for 2027-01-20 (page:55-56); and two civil investigative demands under the False Claims Act (page:56). Revised FY2026 guidance on a continuing basis is net revenue of 2.88 billion to 2.90 billion, Adjusted EBITDA of 510 million to 525 million and free cash flow of 50 million to 75 million (Q3 release page:2). That guidance is a management claim without a GAAP reconciliation (page:7). No event dated after 2026-11-05 is relied on. The 2027-01-20 hearing and the expected first-quarter 2027 close are future dates stated as scheduled or expected, not as facts.

### Consumer assessment

| Consumer | Evidence demand | Status | Carried limitations |
| --- | --- | --- | --- |
| CP-1 financial base | Discrete periods, annual base, segments, add-backs, debt, cash flow, cash interest and taxes | READY_WITH_LIMITATIONS | Annual base is pre-recast; Q1 2026 recast not stand-alone; cash paid for interest 96,639 thousand and cash taxes refunded 12,788 thousand are printed for nine months only, on a cash flow statement that includes discontinued operations (Q3 10-Q page:8, page:89); lease obligations are on the balance sheet (page:4) with a maturity table (page:49) |
| CP-1A business and transaction context | Business, ownership, transaction and history facts | READY_WITH_LIMITATIONS | Diabetes sale agreement, the joint venture contract and the refinancing documents are not supplied; only filing and release descriptions; context has no sponsor, deal terms or ownership map |
| CP-2 fundamental synthesis | Settled upstream registers plus filings | READY_WITH_LIMITATIONS | Covenant levels, guarantor map and ratings not supplied; ratings and quotes in the context are empty |
| CP-5 evidence trace | Citations that resolve in pinned sources | READY_WITH_LIMITATIONS | Depends on the page-chunk locators; extraction fidelity not reviewed |

Missing downstream analytical handoffs are not treated as source conditions. The dependency planner sequences them.

### Extraction status and fidelity

Every source was retrieved as text chunks and read by search and targeted page reads. Tables arrived as flattened text; column headers were checked against the period labels printed in each table. No image, chart or slide content exists in the pack, and the releases are text only. A successful extraction is not a fidelity review of every table, and none is claimed.

## Calculations

These are source tie-outs only, in thousands of USD unless stated. No figure is normalized.

| Check | Inputs and locator | Result |
| --- | --- | --- |
| Debt table adds to total | 647,969 + 147,000 + 1,100,000 - 11,112 (Q3 10-Q page:38-39) | 1,883,857, equal to the printed total |
| Current and long-term debt add to total | 16,250 + 1,867,607 (page:4, page:39) | 1,883,857, equal |
| Term loans match narrative | 323.0 million + 325.0 million (page:42) vs 647,969 thousand | 648.0 million vs 647.969 million; difference is rounding to 0.1 million |
| Notes match narrative | 600.0 + 500.0 million (page:42) vs 1,100,000 thousand | 1,100.0 million, equal |
| Revolver headroom check | 450.0 - 147.0 - 34.3 million (page:40, page:42) | 268.7 million, equal to the stated maximum borrowing. The printed covenant-based maximum therefore equals arithmetic availability (commitments less drawings and letters of credit). This is a consistency check, not a liquidity conclusion and not covenant headroom |
| Revolver after October repayment | 147.0 - 10.0 million (page:86) | 137.0 million, equal to the stated filing-date balance |
| Dec 2025 debt carrying value | 315,000 + 1,435,000 - 13,704 (Q3 10-Q page:38-39 column Dec 2025; 10-K page:167) | 1,736,296, equal to the 10-K fair-value table carrying total (page:137) |
| Held for sale at 2025-12-31 | 36,354 + 139,911 (page:3-4) vs 176,265 (page:27) | Equal |
| Goodwill impairment split | Q2 144,236 (Q2 10-Q page:4) + Q3 184,751 (Q3 10-Q page:4) | 328,987, equal to nine-month figure (page:4) |
| Segment revenue Q3 2026 | 393,860 + 190,808 + 160,980 (page:29) | 745,648, equal to consolidated |
| Segment Adjusted EBITDA Q3 2026 | 70,741 + 56,230 + 14,933 (page:29) | 141,904, equal to page:74 |
| Segment revenue nine months 2026 | 1,138,816 + 563,350 + 463,662 (page:30) | 2,165,828, equal |
| Segment Adjusted EBITDA nine months 2026 | 196,100 + 155,483 + 26,879 (page:30) | 378,462, equal to page:75 |
| Release vs filing net loss, Q3 2026 | -167,025 - 1,221 (page:5) = -168,246; add 14,259 discontinued income | -168,246 matches the release's 168.2 million; -153,987 matches the 10-Q total attributable |
| Release comparison, Q3 2025 | 11,474 - 1,241 (page:5) | 10,233, matches the release's 10.2 million |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Covenant levels, step-downs and reported ratios under the 2026 Credit Agreement are not supplied (only names and compliance statement, Q3 10-Q page:41); searched Consolidated Total Leverage Ratio, Interest Coverage Ratio, "not to exceed" across all seven sources | High | CP-1, CP-2 | Obtain the executed 2026 Credit Agreement or its 8-K exhibit |
| Executed legal documents (credit agreement, indentures, supplemental indentures) not supplied; context legal_documents is none | High | CP-2, CP-5 | Add the executed documents; until then legal terms are filing summaries |
| Borrower, issuer and guarantor identities beyond the passages cited are not named; the 5.125% and 4.625% notes are described both as the Company's and as AdaptHealth LLC's (page:42, page:87) | Medium | CP-2, CP-5 | Obtain the indenture and subsidiaries exhibit |
| No recast FY2025 income statement, segment table or Adjusted EBITDA on the continuing perimeter; last-twelve-months on the current perimeter is not calculable | High | CP-1, CP-2 | Obtain a recast annual set, such as an 8-K recast, if one exists |
| Q1 2026 stand-alone figures on the recast basis are not supplied | Medium | CP-1 | Derive from six-month and Q2 figures downstream, labelled as derived |
| Diabetes Health sale agreement, eCommerce joint venture agreement and the 2026-07-02 cybersecurity 8-K are not in the pack | Medium | CP-1A, CP-2 | Obtain the exhibits or 8-Ks |
| Cybersecurity incident cost and exposure not determined (page:62) | Medium | CP-2 | Carry as unquantified contingent claim; recheck at the next filing |
| Fair value of debt at 2026-09-30 not printed (Note 9 at page:35-37 covers swaps only); 10-K gives 2025-12-31 only (page:137) | Low | CP-1 | Not needed for readiness |
| Revolver interest rate, undrawn commitment fee dollar amount and 2026 term loan maturity table not printed beyond the stated schedule | Low | CP-1 | None |
| Ratings, market quotes, peers and valuation inputs in the context are blank | Medium | CP-2 | Supply if relative value or rating-based work is wanted; not zero |
| Page-chunk locators are extraction chunks, not printed page numbers; no fidelity review of the extracted tables | Low | CP-5 | Spot-check key tables against the original htm if used for external work |
| Release guidance has no GAAP reconciliation (Q3 release page:7) | Low | CP-2 | Treat as an attributed management claim |
| Agency credit ratings are not supplied: a search of all seven sources for Moody, Standard & Poor, S&P, Fitch and credit rating returned no hit, and the context ratings list is empty | Medium | CP-2 | Supply ratings if needed |

## Next module

Proceed to CP-1 first, then CP-1A, CP-2 and CP-5, in the order CP-OS plans. Every consumer is READY_WITH_LIMITATIONS and may run. Carry forward these instructions to the next module: use the Q3 10-Q as the controlling source for the balance sheet, debt and nine-month results; label every annual figure from the 10-K and every Q1 2026 figure as pre-recast, including Diabetes Health; do not place pre-recast and recast figures side by side as like for like; take the borrowing capacity of 268.7 million as the company's stated figure and not as covenant headroom; and keep the covenant levels, guarantor map and cybersecurity exposure as open gaps.
