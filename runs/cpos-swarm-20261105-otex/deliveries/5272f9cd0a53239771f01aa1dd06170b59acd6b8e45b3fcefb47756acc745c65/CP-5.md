## Request

OPEN TEXT CORP (registrant Open Text Corporation, consolidated, USD), as of 2026-11-05, credit_snapshot pathway: an independent evidence trace and integrity review of the readiness, financial base, business context and credit synthesis handoffs for this run, testing whether each material claim rests on the evidence it names and whether the modules tell one consistent story. Scope is the Top 5 material credit drivers plus a full cross-module consistency and handoff check.

## Sources

### Issuer sources behind the reviewed handoffs

| Source file (exact name) | sha256 |
| --- | --- |
| 10-K_2026-06-30_otex-20260630.htm.jsonl | f68e5c975d736a5d60a932e22b4b1113b0dd717debe22c96d4297e49e4b48ad7 |
| 10-Q_2025-12-31_otex-20251231.htm.jsonl | c656e908af03f16a38fffb87df79cdeabf81b11c447b6307e4c89c53daecd451 |
| 10-Q_2026-03-31_otex-20260331.htm.jsonl | 337092207ee075518fbe18b12c9d6afe8e47e489c027bb48960c31b2c5742175 |
| 10-Q_2026-09-30_otex-20260930.htm.jsonl | 1fd82748eef70947f4a4d274b026606169ae599efc16f0e2194cf001bfe65e31 |
| EX-99.1_2026-05-07_q3-26pressreleaseexhibit991.htm.jsonl | e697cff46a3e21a58ac9cf8d31a36bcb6270ad11a5dc8fdcfb37d685f98b9ffa |
| EX-99.1_2026-08-06_q4-26pressreleaseexhibit991.htm.jsonl | 83f62f97a6b7c7e9bfc3742a4b7bc9c0199bd0f87ffa7a765f100c4602287036 |
| EX-99.1_2026-11-05_q1-27pressreleaseexhibit991.htm.jsonl | f55be454dd27b1c15a5ec57d7bf7bf620ded41528eca4ef61bb9f128226efbcd |

Run context (not issuer evidence): sha256 cdf3e7e5d139751591ad9d995cdcdd0bad8e54e428f889bfd4cbcc1eae58ab70. In citations below, the aliases 10-K, 10-Q-Dec25, 10-Q-Mar26, 10-Q-Sep26, PR-May26, PR-Aug26 and PR-Nov26 refer to the files above in that order; quotes were opened at the cited extraction chunk ("page:N" is the extracted chunk, not the printed page).

### Supplied handoffs

| Module | Alias | sha256 |
| --- | --- | --- |
| CP-0 | H-CP0 | ae7b653c84c72f696d77e449940280b63c6a90d2bec9f8b7dc52fb0396bbbec0 |
| CP-1 | H-CP1 | fc72d6e76ea4ae4cd11643bc6d6394ce5f711c2810c1cccef5e45ddb67a3d113 |
| CP-1A | H-CP1A | cca33eea8c36426026798a192e210e8371db56b8cf3e67589f7ae7738a743b74 |
| CP-2 | H-CP2 | 6fb494866244976329de012d130d5f0494c0baf83752a1aac44c61b1eabde7cc |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Evidence traceability is ready with remediation: the leverage, cover, liquidity and revenue claims trace to the filings, but two material statements need correction and the covenant and refinancing details remain thinly sourced. | Medium | Executed financing documents, ratings, letters of credit and the September 2026 covenant calculation are not in the pack, so some legal and liquidity claims cannot be traced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every quote in the earlier reports was found at its cited location, and the main leverage and cover figures recompute from filed inputs. | The numbers behind the credit view can be relied on as reported, within the stated definitions. | High |
| The first report wrongly said no filing prints the covenant ratio; the filings print 3.35, 3.02 and 2.75 against a 4.50 maximum. | Covenant headroom is better evidenced than first stated, but only to June 2026. | High |
| Describing the October 2026 notes as higher-coupon overstates the change: the new notes average 6.925 percent against 6.90 percent on the retired notes. | The refinancing changes maturity and ranking far more than cost, so the cost point should not carry weight. | High |
| The reasoning for the guided margin step-down is not stated in the filings. | The outlook is a management figure and the cause of the drop is an analyst inference, so scenario leverage stays conditional. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 3 are directly sourced, 2 are calculated, 0 are assumption-based, 0 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. The most important provenance gap is the missing covenant earnings and the unprinted September 30, 2026 covenant ratio (management states 2.55x without a definition), which matters because covenant headroom is the main test of default distance and implies that committee use should rest on the printed ratios to June 2026 and treat the later figure as attributed.

The review opened every quoted span in the first four reports at its cited location (157 spans across the readiness, financial base and business context reports; the synthesis quotes no source text and cites the upstream reports), recomputed every derived figure the reports show, and compared shared figures across the four reports. No Critical defect was found. Two Material defects and four Minor ones are logged below; neither Material defect changes a financial figure, and both are corrections of wording or of an earlier statement that a later report already supersedes. Committee use is restricted until those two corrections are carried with the reports.

### Source and handoff register

| Item | Scope | Source quality | Period | Entity | Limitation |
| --- | --- | --- | --- | --- | --- |
| Annual report (10-K) | FY2026 statements and notes | Filed, original authority | Year ended June 30, 2026 | Open Text Corporation, consolidated | Extraction fidelity not independently reviewed |
| Quarterly reports (three 10-Qs) | Q2 FY2026, Q3 FY2026, Q1 FY2027 | Filed, original authority | Quarters ended December 31, 2025, March 31, 2026, September 30, 2026 | Same | Latest report filed on the cutoff date |
| Earnings releases (three exhibits) | Q3 FY2026, Q4 FY2026, Q1 FY2027 | Issuer statements, supporting only | Same quarters | Same | Management characterisation, non-GAAP |
| H-CP0 readiness | Source sufficiency | Analyst work, dated 2026-11-05 | Run | Same | Contains one superseded statement (issue M1) |
| H-CP1 financial base | Statements, debt, liquidity, covenants | Analyst work | FY2024 to Q1 FY2027 and last twelve months | Same | Issuer-defined adjusted EBITDA |
| H-CP1A business context | Business, ownership, transaction, governance | Analyst work | Through the cutoff | Same | Management language for outlook and strategy |
| H-CP2 credit synthesis | Credit view | Analyst work, upstream-only | Run | Same | Cites handoffs, not source text |

Module status: Ready with Limitations (all four handoffs are present and each carries its required headings; the Markdown transport has no separate YAML envelope, see M5). Traceability scope: Top 5 for driver tracing, full population for the consistency, calculation and quote checks.

### Top 5 material credit drivers

| Rank | Credit driver | Originating module | Source-supported basis | Why material | Committee relevance | Source trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Deleveraging: total debt to adjusted EBITDA 3.63x at FY2025, 3.07x at FY2026, 3.10x last twelve months | H-CP1 | Principal from the debt notes and adjusted EBITDA from the reconciliations | Sets leverage tolerance and default distance | Core of the credit view | [10-K page:268 — "Total principal payments due 5,836,525 6,485,375"], [10-Q-Sep26 page:16 — "Total principal payments due 5,827,563 5,836,525"] | Issuer-defined EBITDA, not covenant EBITDA |
| 2 | Debt service: adjusted EBITDA to cash interest 3.69x in FY2024 to 6.26x last twelve months | H-CP1 | Cash paid for interest in the cash flow supplements | Sets distance of earnings from debt service | Supports cover resilience | [10-K page:306 — "Cash paid during the period for interest $ 321,694 $ 352,383 $ 533,866"] | Gross of interest received; October 2026 refinancing not in figures |
| 3 | Revenue durability: revenue down 4.0 percent, support down 9.0 percent, recurring share 84.1 percent | H-CP1, H-CP1A | Release summary table and income statement | Drives earnings and free cash flow | Main weakness | [PR-Nov26 page:2 — "Client support 534 587 (53) (9.0) %"], [10-Q-Sep26 page:3 — "Total revenues 1,236,634 1,288,135"] | Outlook is management language |
| 4 | Refinancing and structure: nearest note maturity February 2028, secured share 45.7 percent | H-CP1, H-CP1A, H-CP2 | Subsequent-events note and debt note | Sets refinancing risk and ranking | Main structural point | [10-Q-Sep26 page:44 — "On October 2, 2026, the Company purchased and cancelled $300.0 million of the aggregate outstanding principal amount of the Senior Notes 2028"] | Premium, tender price and cash after the transactions not supplied; wording defect M2 |
| 5 | Covenant headroom and liquidity: ratio 2.75 against a 4.50 maximum at June 2026; cash plus undrawn revolver | H-CP1 | Printed covenant ratio, balance sheet, revolver note | Sets near-term default risk | Supports liquidity view | [10-K page:124 — "as calculated in accordance with the applicable agreement, was 2.75:1.00"], [10-Q-Sep26 page:19 — "we had no outstanding balance under the Revolver (June 30, 2026—nil)"] | Letters of credit and covenant earnings not supplied; September 2026 ratio not printed |

### Traceability map

| Conclusion | Module | Source evidence | Citation present | Source quality | Classification | Claim status | Confidence | Traceability status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 3.07x at FY2026 and 3.10x last twelve months | H-CP1 | Principal, cash and adjusted EBITDA quoted and recomputed (calculation C1) | Yes | Filed | Calculated | Supported | High | Committee-Ready |
| Cover 6.26x last twelve months | H-CP1 | Cash interest and EBITDA inputs quoted (C2) | Yes | Filed | Calculated | Supported | High | Committee-Ready |
| Covenant ratios 3.35, 3.02, 2.75 against 4.50 | H-CP1 | Filing statements quoted | Yes | Filed | Directly Sourced | Supported | High | Committee-Ready |
| Management net leverage 2.55x at September 2026 | H-CP1, H-CP2 | Release statement only, no definition | Yes | Issuer statement | Directly Sourced as an attributed claim | Partly supported (not usable as covenant) | Low | Remediation Needed (kept attributed) |
| Revenue and support declines, recurring share 84.1 percent | H-CP1A, H-CP2 | Release and 10-Q tables; share recomputed (C3) | Yes | Filed and issuer | Directly Sourced and Calculated | Supported | High | Committee-Ready |
| FY2027 outlook implies adjusted EBITDA about USD 1,643.2 to 1,711.1 million | H-CP1A, H-CP2 | Outlook table quoted; product of ranges (C4) | Yes | Issuer outlook | Assumption-Based (management) | Supported as arithmetic, not as forecast | Medium | Committee-Ready if labelled |
| Cause of the guided margin step-down | H-CP1A, H-CP2 | No statement of cause in the filings | Partial | Analyst | Analyst Inference | Partly supported | Low | Remediation Needed (M3) |
| October 2026 refinancing facts | H-CP1, H-CP1A, H-CP2 | 10-Q subsequent events note | Yes | Filed | Directly Sourced | Supported | High | Committee-Ready |
| Replacement notes at "higher coupons" | H-CP1, H-CP1A, H-CP2 | 6.70 and 7.15 against 6.90 | Yes | Filed | Directly Sourced facts, overstated characterisation | Partly supported | Medium | Remediation Needed (M2) |
| Covenant ratio "not printed in any supplied filing" | H-CP0 | Contradicted by three filings | Yes | Filed | Conflicting | Unsupported | High | Superseded by H-CP1 (M1) |
| Trustees not named in the pack | H-CP1A | Exhibit list names trustees | Yes | Filed | Conflicting | Unsupported | High | Remediation Needed (m1) |

### Source lineage register

| Statement | Source file | Page | Module section | Type | Notes |
| --- | --- | --- | --- | --- | --- |
| Principal debt 5,827,563 at September 30, 2026 | 10-Q-Sep26 | page:16 | H-CP1 debt register | Sourced | Matches note total |
| Principal debt 5,836,525 and 6,485,375 at June 30, 2026 and 2025 | 10-K | page:268 | H-CP1 table | Sourced | Matches |
| Cash 983,292 at September 30, 2026 | 10-Q-Sep26 | page:2 | H-CP1 table | Sourced | [10-Q-Sep26 page:2 — "Cash and cash equivalents $ 983,292 $ 956,024"] |
| Adjusted EBITDA 1,903,162, 1,784,465 and 1,970,200 | 10-K | page:136, 139, 142 | H-CP1 table | Sourced | Reconciliation pages |
| Adjusted EBITDA 442,432 and 467,411 | 10-Q-Sep26 | page:76, 78 | H-CP1 table | Sourced | Used for last-twelve-months |
| Cash interest 57,917 and 79,500 | 10-Q-Sep26 | page:42 | H-CP1 table | Sourced | [10-Q-Sep26 page:42 — "Cash paid during the period for interest $ 57,917 $ 79,500"] |
| Covenant ratios 3.35 and 3.02 | 10-Q-Dec25, 10-Q-Mar26 | page:23, 24 | H-CP1 covenants | Sourced | [10-Q-Dec25 page:23 — "was 3.35:1:00"], [10-Q-Mar26 page:24 — "was 3.02:1:00"] |
| Management net leverage 2.55x | PR-Nov26 | page:3 | H-CP1, H-CP2 | Sourced, attributed | [PR-Nov26 page:3 — "Our net leverage ratio is 2.55x as of September 30, 2026."] |
| Canada Revenue Agency exposure of approximately USD 88.8 million and up to USD 470 million | 10-Q-Sep26 | page:30, 85 | H-CP1, H-CP2 | Sourced | [10-Q-Sep26 page:30 — "approximately $88.8 million"], [10-Q-Sep26 page:85 — "of up to approximately $470 million"] |
| FY2027 outlook margin 32 to 33 percent | 10-Q-Sep26 | page:53 | H-CP1A, H-CP2 | Sourced, management | [10-Q-Sep26 page:53 — "Adjusted EBITDA Margin (Non-GAAP) 32% to 33%"] |
| Recurring revenue 84.1 percent | 10-Q-Sep26 | page:3 | H-CP1A | Calculated | Inputs 505,469, 534,111 and 1,236,634 |
| Largest holder 11.17 percent | 10-K | page:214 | H-CP1A | Sourced | [10-K page:214 — "1832 Asset Management L.P. (6) 27,039,270 11.17%"] |
| Trustees named for the new secured notes | 10-Q-Sep26 | page:90 | Contradicts H-CP1A | Sourced | [10-Q-Sep26 page:90 — "The Bank of New York Mellon, as U.S. trustee and Notes collateral agent"] |
| Four chart tables, the financial table and the debt register in H-CP1 | H-CP1 | n/a | Recomputed | Calculated | See calculations |

### Calculation and assumption register

| Item | Where used | Inputs | Formula | Status | Confidence | Credit relevance | Trace |
| --- | --- | --- | --- | --- | --- | --- | --- |
| C1 Total debt / adjusted EBITDA, last twelve months at September 30, 2026 | H-CP1, H-CP2 | 5,827,563; 1,878,183 (1,903,162 less 467,411 plus 442,432) | 5,827,563 / 1,878,183 = 3.10x | Calculated, reproduced | High | Leverage | Debt note and reconciliations |
| C2 Adjusted EBITDA / cash interest, last twelve months | H-CP1, H-CP2 | 1,878,183; 300,111 (321,694 less 79,500 plus 57,917) | 1,878,183 / 300,111 = 6.26x | Calculated, reproduced | High | Debt service | Cash flow supplements |
| C3 Recurring share Q1 FY2027 | H-CP1A, H-CP2 | 505,469 plus 534,111 over 1,236,634 | 1,039,580 / 1,236,634 = 84.1 percent | Calculated, reproduced | High | Revenue visibility | 10-Q income statement |
| C4 Outlook-implied adjusted EBITDA | H-CP1A, H-CP2 | Revenue 5,135 to 5,185 million; margin 32 to 33 percent | 5,135 x 0.32 = 1,643.2; 5,185 x 0.33 = 1,711.1 million | Calculated, extremes of two ranges (not a forecast) | Medium | Scenario leverage | Outlook table |
| C5 Scenario leverage if outlook met | H-CP2 | 5,527.563 million over 1,711.1 and 1,643.2 million | 3.23x and 3.36x | Calculated, reproduced; ignores amortization and repayment | Medium | Leverage tolerance | C4 and H-CP1 pro forma principal |
| C6 Secured share after October 2026 | H-CP1, H-CP1A, H-CP2 | 1,527,563 plus 500,000 plus 500,000 over 5,527,563 | 2,527,563 / 5,527,563 = 45.7 percent | Calculated, reproduced | High | Ranking | Debt register |
| C7 Distributions share of free cash flow FY2026 | H-CP1, H-CP2 | 268,357 plus 416,411 plus 52,901 over 807,517 | 737,669 / 807,517 = 91.4 percent | Calculated, reproduced | High | Cash conversion | 10-K cash flow statement |
| C8 Coupon change on exchanged notes | H-CP1, H-CP2 | 500,000 at 6.70 percent, 500,000 at 7.15 percent, less 1,000,000 at 6.90 percent and 300,000 at 3.875 percent | 69,250 less 69,000 less 11,625 = minus 11,375 | Calculated, reproduced | High | Interest cost | Coupons from the 10-Q notes |
| C9 Blended coupon on replaced 1,000,000 | Review | 6.70 and 7.15 percent, equal tranches | (6.70 + 7.15) / 2 = 6.925 percent against 6.90 percent, a difference of 0.025 percentage points or 250 thousand per year | Calculated, new here | High | Corrects wording (M2) | Debt note |
| C10 Net debt / adjusted EBITDA | H-CP1 | 5,827,563 less 983,292 = 4,844,271 over 1,878,183 | 2.58x | Calculated, reproduced | High | Leverage | Balance sheet |
| C11 Covenant headroom | H-CP1 | 4.50 less 3.35, 3.02, 2.75 | 1.15, 1.48, 1.75 turns | Calculated, reproduced | High | Default distance | Filings |
| C12 Revenue growth and margins | H-CP1 | Revenue and adjusted EBITDA by year | Minus 10.4, 1.5 and minus 4.0 percent; margins 34.1, 34.5, 36.3, 36.2 | Calculated, reproduced | High | Trend | Statements |

Definition drift check: all four reports use the issuer-defined adjusted EBITDA for leverage and cover, and all keep the covenant ratio, the management ratio and the computed net leverage apart (2.75 at June 2026, 2.55x at September 2026 as management, 2.56x and 2.58x computed). No drift between modules was found. The reports state period, perimeter and currency for each figure; the only mixed units (US$ thousands in tables, US$ millions in charts and release text) are labelled.

### Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why it matters | Remediation | Affected output |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Covenant ratio not printed in any supplied filing | Wrong for December 2025, March 2026 and June 2026 | Conflicting | Understated covenant evidence; headroom is a default-distance input | Use H-CP1 correction; disclose that H-CP0 is superseded on this point | H-CP0 |
| Material | Refinancing described as higher-coupon | Blended coupon on the replaced paper rises by 0.025 percentage points, and the tender of 3.875 percent notes lowers total coupon | Partly supported | Misstates cost direction in committee-facing summaries | Describe as roughly unchanged cost with longer maturity and more secured share | H-CP1, H-CP1A, H-CP2 reader summaries and risk rows |
| Minor | Trustees not named | Exhibit list names trustees and collateral agent | Conflicting | Minor; structural facts otherwise correct | Note that the indentures are listed as exhibits to the October 1, 2026 current report but not supplied | H-CP1A |
| Minor | Margin step-down mechanic | Sources give no cause for the guided drop; H-CP1A pairs it with unrealized savings, which would work the other way; H-CP2 adds restructuring costs, also unsourced | Analyst Inference | Cause shapes whether the drop is temporary | Label as inference | H-CP1A, H-CP2 |
| Minor | Handoff-level citations in the synthesis | The synthesis cites reports in brackets, not rows | Weak Lineage (granularity) | Slower tracing | Accept for an upstream-only module; keep this trace | H-CP2 |
| Minor | No YAML envelope or Evidence Trace headings | Markdown transport uses six headings only | Transport adaptation | None for content | None | All |

### Auditability assessment

| Dimension | Assessment | Evidence | Risk mechanic | Credit implication | Remediation needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | All seven issuer documents are complete from cover to signatures; the quarterly reports and annual report are original authority | Gaps (executed documents, ratings, letters of credit) limit legal and liquidity tracing | Covenant and ranking points rest on filing summaries | Obtain exhibits and agency reports if needed |
| Citation completeness | Committee-Ready | 157 of 157 quotes found at their cited locators | Low risk of misquotation | Figures can be relied on as reported | None |
| Calculation traceability | Committee-Ready | 12 calculation items reproduced with formula and inputs | Rounding only | Leverage and cover reliable on stated definitions | None |
| Assumption transparency | Ready with Remediation | Outlook and scenario are labelled management or illustrative; margin mechanic unlabelled in places | Mechanic could be read as fact | Scenario leverage conditional | Label as inference (m2) |
| Markdown artifact integrity | Committee-Ready | Required headings, selectors and tables present in each report | None | None | None |

Overall auditability is Ready with Remediation (the lowest dimension).

### Quote, locator and consistency audit

Citation audit (T5.2): every quoted span in the readiness, financial base and business context reports was searched for at its cited extraction chunk; all were found. The synthesis report quotes no source text. Spot reads confirmed the tables in the financial base against the statements: income statement, balance sheet, cash flow, reconciliations and debt note figures for FY2024 to Q1 FY2027 (revenue 5,246,401; operating cash flow 1,006,817; capital expenditure 199,300; cash 956,024).

Math and logic audit (T5.3): no calculation error changes a metric beyond rounding. One presentation note: the financial base reports a net change in the debt cash flow line of 648,852 against a principal change of 648,850; the reports disclose the difference of 2 as unexplained.

Legal and structural audit (T5.4): the reports describe indenture terms, guarantees and security from the filings' summaries; no executed document is in the pack, so claims about guarantor groups, ranking and restricted-payment capacity are Insufficient Information and are labelled so in all four reports. One structural statement is contradicted: trustees are named in the exhibit list (m1).

Market and relative-value audit (T5.5): none of the reports makes a price, spread, peer or ranking claim; the synthesis contains no instrument recommendation and no recovery conclusion. Nothing to remediate.

Cross-module consistency (T5.6): principal 5,827,563 and 5,527,563, last-twelve-months adjusted EBITDA 1,878,183, cash 983.3 million, undrawn revolver 750.0 million, covenant values 3.35, 3.02 and 2.75, secured share 45.7 percent, distributions 91.4 percent and free cash flow 844,805 match across the financial base, business context and synthesis reports. The only inconsistency is between the readiness report and the later reports on the covenant ratio (M1) and the coupon wording (M2).

Duplication, materiality and committee readiness (T5.7): the reports repeat the refinancing description across modules, which is acceptable; no immaterial padding was found. Committee readiness is restricted only by M1 and M2.

Handoff integrity (T5.8): every report has the six required headings in order, the named view section directly after the reader summary, and its selector sections; the sha256 values listed in Sources are those of the accepted files. The readiness report cannot be edited; its superseded statement is therefore recorded here.

### Gaps ledger

| Gap ID | Gap | Missing evidence | Why it matters | Impact | Confidence consequence | Follow-up source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Covenant earnings and the September 30, 2026 covenant ratio | Compliance certificate or next quarterly report | Default distance at the latest date | H-CP1, H-CP2 headroom | Medium | Next 10-Q |
| CP-5-GAP-002 | Executed indentures, credit agreement and amendments | Filed exhibits (listed in the exhibit index) | Ranking, guarantors, restricted-payment capacity | Legal view | Medium | EDGAR exhibits |
| CP-5-GAP-003 | Ratings and third-party views | Agency reports | Corroboration of the credit view | H-CP1A, H-CP2 | Medium | Agency publications |
| CP-5-GAP-004 | Letters of credit and cash after the October 2026 transactions | Notes or the next quarterly report | Liquidity measurement | H-CP1 liquidity | Medium | Next 10-Q |
| CP-5-GAP-005 | Cause of the guided margin step-down | Management commentary or call transcript | Whether the step-down is temporary | H-CP2 scenario | Low | Investor day, February 2027 |
| CP-5-GAP-006 | Customer concentration and cohort retention | Disclosure from the company | Revenue durability | H-CP1A, H-CP2 | Low | Company disclosure |

### Consolidated issue log

| Issue ID | Severity | Module | Issue type | Description | Required fix | Clearance impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| M1 | Material | H-CP0 | Conflicting Evidence, Cross-Module Inconsistency | Statement that the covenant ratio value is not printed in any filing is wrong for three dates. Evidence: [10-K page:124 — "as calculated in accordance with the applicable agreement, was 2.75:1.00"], [10-Q-Dec25 page:23 — "was 3.35:1:00"], [10-Q-Mar26 page:24 — "was 3.02:1:00"] against the readiness text [H-CP0 — "Covenant ratio value and covenant-defined earnings are not printed in any supplied filing"] | Treat H-CP1 correction as controlling; carry this note | Restricts Committee Use until disclosed | Open (disclosure) |
| M2 | Material | H-CP1, H-CP1A, H-CP2 | Partially Supported Claim | "Higher-coupon" and "higher coupons" wording. Evidence: [10-Q-Sep26 page:43 — "senior secured notes due 2031"], [10-Q-Sep26 page:18 — "Senior Secured Notes 2027 bear interest at a rate of 6.90% per annum"], blended 6.925 percent (C9), net coupon change minus 11,375 (C8) | Replace with "similar blended coupon, longer maturities, larger secured share" | Restricts Committee Use until disclosed | Open (disclosure) |
| m1 | Minor | H-CP1A | Conflicting Evidence | Trustees said not named; [10-Q-Sep26 page:90 — "The Bank of New York Mellon, as U.S. trustee and Notes collateral agent"] | Note | Monitoring Follow-Up | Open |
| m2 | Minor | H-CP1A, H-CP2 | Unsupported mechanic | Cause of margin step-down is inference | Label | Monitoring Follow-Up | Open |
| m3 | Minor | H-CP2 | Citation Gap (granularity) | Handoff-level citations | Accept | Formatting / Hygiene Only | Accepted |
| m4 | Minor | All | Markdown handoff integrity | No YAML envelope | None | Formatting / Hygiene Only | Accepted |

Remediation priority: (1) disclose M1 and M2 wherever the first four reports are read, with the corrected statements above; (2) label the margin mechanic as an analyst inference (m2) and note the named trustees (m1); (3) obtain the covenant, letters of credit and post-October cash items at the next quarterly filing; (4) obtain executed documents and ratings if a legal or market view is required.

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 2. Minor Issues: 4. Committee Use: Restricted.

The two Material issues are wording and supersession problems, not figure errors, and both are fixed by disclosure; once carried with the reports, committee use is Approved on the evidence available. The first four reports remain unedited, as accepted answers cannot be replaced.

## Calculations

The review recomputed each derived figure listed in the calculation register. Inputs are in US$ thousands unless stated. Key reproductions: last-twelve-months adjusted EBITDA = 1,903,162 minus 467,411 plus 442,432 = 1,878,183; total debt / EBITDA = 5,827,563 / 1,878,183 = 3.10x; net debt = 5,827,563 minus 983,292 = 4,844,271, and 4,844,271 / 1,878,183 = 2.58x; last-twelve-months cash interest = 321,694 minus 79,500 plus 57,917 = 300,111, and cover = 1,878,183 / 300,111 = 6.26x; pro forma principal = 5,827,563 minus 300,000 = 5,527,563 and 5,527,563 / 1,878,183 = 2.94x; secured share = 2,527,563 / 5,527,563 = 45.7 percent. New in this review only: blended coupon on the replaced 1,000,000 of secured notes = (6.70 + 7.15) / 2 = 6.925 percent against 6.90 percent, a difference of 0.025 percentage points, equal to 250 thousand per year on 1,000,000. Inputs for the last twelve months: [10-Q-Sep26 page:76 — "Adjusted EBITDA $ 442,432"], [10-Q-Sep26 page:78 — "Adjusted EBITDA $ 467,411"], [10-K page:136 — "Adjusted EBITDA $ 1,903,162"], [10-Q-Sep26 page:16 — "Total principal payments due 5,827,563 5,836,525"].

## Gaps

The gaps ledger above (CP-5-GAP-001 to 006) lists the evidence that would improve traceability. Additional limitations of this review: it relies on text extraction of the filings, not the original documents, and did not inspect charts, images or XBRL; the extraction fidelity of tables was checked only for the figures cited. No external source was used.

## Next module

The trace is complete for this run. Before the report is used by a committee, carry the two corrections (M1 and M2) with the first four reports, label the margin mechanic as an inference, and refresh the covenant, letters of credit and post-October cash items at the next quarterly filing (expected after the cutoff). Recommend no further module in this pathway.
