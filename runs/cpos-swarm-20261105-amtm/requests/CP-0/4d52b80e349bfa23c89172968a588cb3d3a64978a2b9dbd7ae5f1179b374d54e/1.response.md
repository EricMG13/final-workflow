## Request

Entity: Amentum Holdings, Inc. (NYSE: AMTM; Delaware registrant, Commission File Number 001-42176; cover of the quarterly report for the period ended July 3, 2026, page:1). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD, stated in millions in the statements.

Question for this step: can the supplied source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5, the minimum module set), and what remains blocked? This step gives no credit conclusion, legal interpretation or investment opinion, and it does not normalise, reconcile or recalculate any figure.

Period labelling used throughout. Amentum's fiscal year ends on the Friday nearest September 30. FY2025 is the 53-week year ended October 3, 2025, with the 53rd week in the fourth quarter (10-K page:118). FY2024 ended September 27, 2024 (52 weeks). Fiscal Q1 2026 ended January 2, 2026, Q2 ended April 3, 2026, Q3 ended July 3, 2026.

Context mismatch to carry forward. The run context names the current period as `q2-2026` and the prior period as `fy-2025`. The latest filed quarter in the pack is fiscal Q3 2026 (quarter ended July 3, 2026; 10-Q signed August 11, 2026, page:32; earnings release dated August 10, 2026), which falls before the cutoff. The Q2 2026 filings are also in the pack. This step treats Q3 2026 (three months and nine months) as the latest balance-sheet and liquidity date, keeps Q2 2026 available as the labelled context period, and leaves the choice of headline period to the downstream modules, which must state it. No currency mismatch: sources report USD.

## Sources

### Issuer sources relied on

| Source name | sha256 (as pinned by CP-OS) | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-10-03_amtm-20251003.htm.jsonl | 8273d25a00529c2b44154e4079fb17aed384ffabfb0b6e916ff874e87d184e2c | Annual report on Form 10-K, audited consolidated statements; 168 pages; signed November 25, 2025 (page:167) | FY2025, 53 weeks ended October 3, 2025, with FY2024 and FY2023 comparatives |
| 10-Q_2026-01-02_amtm-20260102.htm.jsonl | 53306aefcf67aafc6e963ada6d826aebfcc9ef2ae12c58e6020ff2739d2c4784 | Quarterly report on Form 10-Q, unaudited; 24 pages | Fiscal Q1 2026, quarter ended January 2, 2026 |
| 10-Q_2026-04-03_amtm-20260403.htm.jsonl | 39d2941eedc33b6b8a6975be5d0ab047229748e579ab149e336916a6515e4e3c | Quarterly report on Form 10-Q, unaudited; 29 pages | Fiscal Q2 2026, quarter and six months ended April 3, 2026; includes Note 14 subsequent events (page:17) |
| 10-Q_2026-07-03_amtm-20260703.htm.jsonl | e0cfefb75002bb2378240c82d12b55245568de0ae66e976bd3399e669ec7e5df | Quarterly report on Form 10-Q, unaudited; 32 pages | Fiscal Q3 2026, three and nine months ended July 3, 2026 |
| EX-99.1_2026-02-09_exhibit991-february92026.htm.jsonl | f4a0837903a2e7b5b24df97e0fe38362855d47b722b3db774277ece94a59d816 | Earnings release (Exhibit 99.1), management narrative plus non-GAAP reconciliation; 12 pages | Q1 2026, release dated February 9, 2026 |
| EX-99.1_2026-05-11_exhibit991-may112026.htm.jsonl | 70874f67722755b78375d913af6706b9925581a1e0d597e3dc867f0ae2da1e41 | Earnings release (Exhibit 99.1); 13 pages | Q2 2026, release dated May 11, 2026 |
| EX-99.1_2026-08-10_exhibit991-august102026.htm.jsonl | cf451c4e10bf61fb7f1fdcb128f9d46a9635fb48c3681eadc79c1a3f2194b093 | Earnings release (Exhibit 99.1); 12 pages | Q3 2026, release dated August 10, 2026 |

The `_retrieval.json` file in the pack was ignored by CP-OS and is not relied on.

### Context and handoffs

- Run context (settings, not issuer evidence): sha256 f35913dfc940216c52100a4ebad511585e07d7ab0e645bded7b78046135f5c43. It carries no deal terms, quotes, ratings, peers, attachments or research questions; those blanks are not zero.
- Supplied handoffs: none. CP-0 is the first module, and CP-OS supplied no upstream handoff (the request lists an empty handoff set).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings and releases are enough to support a corporate credit snapshot of the reporting group through the quarter ended July 3, 2026, with each downstream module able to run, subject to the named limits. | Medium | No credit agreement, indenture, ratings report or market data is supplied, so covenant terms after the April 2026 amendment cannot be read from the contract. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Filed statements cover the latest quarter, the prior fiscal year and the debt note, with a dated debt table and revolver capacity. | Debt, liquidity and leverage can be built from filed figures rather than management claims. | High |
| The April 2026 credit agreement amendment is described in the filings, but the amendment itself is not in the pack. | Post-amendment covenant level, pricing grid and guarantor terms rest on summary text only. | Medium |
| Prior-year comparatives mix a 53-week year and a merger-affected FY2024 base. | Year-on-year trends must be labelled by period and perimeter before they are used. | Medium |
| Adjusted EBITDA and net leverage appear only as management measures with a reconciliation. | Any leverage figure needs the filed definitions and a clear label against a filed-statement calculation. | Medium |

### Readiness view

The effective source set is sufficient for the requested snapshot work, with bounded limitations; it is not complete for a covenant, legal or market-based read. Filed financial statements and notes (the annual report and three quarterly reports) are the controlling authority for reported figures. The three earnings releases are management documents that supply attributed non-GAAP measures, guidance and a net leverage figure, and they do not override the filings. Readiness is a source-sufficiency view only; it is not a finding that downstream analysis is complete, and CP-MODEL input acceptance is not evaluated (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

| Consumer | Source readiness | Reason and bounded gaps |
| --- | --- | --- |
| CP-1 (canonical financial data) | READY_WITH_LIMITATIONS | Statements, debt note, liquidity, segment tables and non-GAAP reconciliation are located. Limits: comparability (53-week FY2025; FY2024 excludes the merged business before September 27, 2024); the pack has no fourth-quarter FY2025 earnings release; contractual debt terms are from filing notes only. |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Business description, the September 27, 2024 merger and spin-off description, segments, customers, backlog and contract mix are in the annual report and quarterly reports. Limits: ownership or sponsor information is not in the context; transaction documents are not supplied. |
| CP-2 (credit synthesis) | READY_WITH_LIMITATIONS | Depends on upstream handoffs, which the dependency planner sequences; that is not a source condition. Source limits are those of the two rows above plus no ratings or market evidence. |
| CP-5 (evidence trace) | READY_WITH_LIMITATIONS | Text extraction supports quote and locator checks. Limit: extraction fidelity of tables was not reviewed against the original filings, and the source text is a text rendering, so any chart or image content in the releases is not inspected. |

### Source-by-source assessment

1. Annual report, FY2025 (10-K). Document family: Form 10-K, audited. Perimeter: Amentum Holdings, Inc. and subsidiaries (page:118). Entity relationships: Amentum Parent Holdings LLC is the accounting acquirer of CMS (the Jacobs Critical Mission Solutions business and portions of Jacobs Divergent Solutions) and is the predecessor, per Note 1 (page:117 to page:118). The FY2025 statements include the merged business for the full year; the FY2024 and FY2023 statements do not include it because the transaction closed on September 27, 2024 (page:118). Debt: Note 12 table at page:144, credit facility description at page:145 to page:148, available borrowing capacity at page:147, covenant text at page:148. Liquidity discussion at page:104. Leases, Note 14 at page:151; retirement plans, Note 10 at page:139; segment note, Note 18 at page:156. Item 1A risk factors begin at page:21.
2. Quarterly report, Q1 2026 (10-Q, quarter ended January 2, 2026). Unaudited. Covenant wording at page:10; liquidity at page:21. Its debt is the original term loan structure, prior to the April 2026 amendment.
3. Quarterly report, Q2 2026 (10-Q, quarter ended April 3, 2026). Unaudited. Note 14, Subsequent Events, at page:17 records the April 24, 2026 first amendment to the credit facility, which post-dates the balance-sheet date; liquidity and covenant wording at page:26 and page:27.
4. Quarterly report, Q3 2026 (10-Q, quarter ended July 3, 2026). Unaudited. Balance sheet at page:2, statements of operations at page:2 and page:3, revenue disaggregation at page:7 and page:8, receivables sales (MARPA) at page:9, debt table at page:10, credit facility and amendment at page:11 and page:12, covenant compliance statement at page:13, segment results at page:26 and page:27, backlog at page:27 and page:28, liquidity at page:28 and page:29, risk factor statement (no material changes from the annual report) and exhibit list at page:31. The quarterly report contains no subsequent events note.
5. Earnings releases (Q1, Q2, Q3 2026). Management documents. They give reported and non-GAAP figures with a reconciliation to GAAP, fiscal-year 2026 guidance, and, in the Q3 release at page:10, a net leverage computation. The Q3 release updates guidance (page:4) and the Q1 and Q2 releases reaffirm it. Management claims are treated as attributed, supporting claims.
6. Version relationships. The three quarterly reports and three releases cover different periods and are separate active sources; none supersedes another. The Q3 10-Q is the controlling source for the latest balance sheet, and the Q2 10-Q Note 14 and the Q3 10-Q debt note both describe the same amendment. There are no duplicate files and no draft or unsigned documents.

### Coverage of the evidence needed by the objective

- Discrete quarters and fiscal years: Q3 2026 and nine months 2026 against the June 27, 2025 comparatives are in the Q3 10-Q (page:2 to page:3); Q1 and Q2 2026 are in their own reports; FY2025 is in the annual report. The 10-Q covers three and nine months; quarter versus year-to-date must be labelled by the consumer.
- Segments: two reportable segments, Digital Solutions and Global Engineering Solutions, with revenue and Adjusted EBITDA (Q3 10-Q page:26 to page:27; annual report page:156).
- Add-backs and KPIs: Adjusted EBITDA reconciliation, backlog, book-to-bill and free cash flow are in the releases (Q3 release page:10 to page:12) and backlog in the Q3 10-Q (page:27 to page:28).
- Debt and facility-level carrying values: Term Loan A, Term Loan B, senior notes and other debt in the Q3 10-Q debt table (page:10) with unamortised discount and financing costs shown as a total line only.
- Lease and pension terms: located in the annual report (Note 14 at page:151; Note 10 at page:139). Cash-paid interest and cash-paid income taxes: Not supplied. A search of all seven sources for interest paid, cash paid, taxes paid and supplemental cash flow information found only an accounting-standards sentence about future tax-paid disclosure; the cash flow statements printed (for example Q3 release page:8) show no such lines.

### Strongest contrary evidence and limitations

- Perimeter and comparability. The 10-K says the FY2025 statements include the merged business for the full year while FY2024 does not (page:118). Evidence: the statement of FY2024 perimeter. Risk mechanism: year-on-year growth for FY2025 over FY2024 is not like for like. Consequence: CP-1 must label that comparison and prefer the quarterly comparatives, which are both post-merger.
- Revenue base changes. The Q3 10-Q attributes lower revenue to contracts moving from consolidated to unconsolidated joint ventures and to fiscal year 2025 divestitures (page:23, page:25). Evidence: MD&A text. Risk mechanism: reported revenue and equity earnings are not comparable across periods. Consequence: the model should carry equity earnings and distributions separately.
- Management measures. Net leverage and Adjusted EBITDA are defined by management in the release (page:10). A figure computed by an analyst from statement lines will differ in definition. Consequence: both must be shown and labelled.
- Off-balance-sheet and contingent claims. Sales of receivables under the MARPA are disclosed (Q3 10-Q page:9); the debt note excludes them. Consequence: CP-1 and CP-2 should not read the debt table as the full financing claim without that note.

## Calculations

None performed. CP-0 does not normalise, reconcile or calculate figures. Coverage counts only: 168 pages (annual report), 24, 29 and 32 pages (quarterly reports), 12, 13 and 12 pages (releases), 290 pages in total, all retained; no page was excluded.

## Gaps

| Gap | Severity | Affected consumers | Remediation | Locator |
| --- | --- | --- | --- | --- |
| The executed credit agreement and the first amendment of April 24, 2026 are not in the pack; the Q3 10-Q lists the amendment as Exhibit 10.1 incorporated by reference to a Form 8-K filed April 28, 2026 | Medium | CP-1, CP-2 | Add the amendment and the credit agreement to the pack; until then use the 10-Q debt note and treat covenant levels as the annual report's pre-amendment wording | Q3 10-Q page:31 |
| Post-amendment financial maintenance covenant level is not stated in the Q3 10-Q, which says only that a financial covenant applies in certain circumstances to the Term Loan A and Revolver and that the company was in compliance as of July 3, 2026; the maximum first lien net leverage ratio is printed only in the annual report for the pre-amendment revolver | Medium | CP-1, CP-2 | Obtain the amendment; label the annual report level as pre-amendment | Q3 10-Q page:13; 10-K page:148 |
| Senior notes indenture is not supplied; coupon, maturity and guarantee terms come from the filing notes | Low | CP-1, CP-2 | Add the indenture if redemption and covenant detail is required | Q3 10-Q page:12 to page:13 |
| No fourth-quarter FY2025 earnings release and no quarterly presentation slides are in the pack; the releases substitute for decks, and a text rendering cannot evidence images or charts | Low | CP-1, CP-1A | Use the annual report for FY2025; record that slide content is not inspected | Pack file list |
| No credit ratings, market prices, peer or valuation data are supplied (context blank). The Q1 2026 release headline (page:1) states that Moody's upgraded the rating to Ba3 from Ba1; on the Moody's scale Ba3 sits below Ba1, so the headline is internally inconsistent, it is management narrative only, and no rating agency report is supplied to resolve it | Medium | CP-2, relative-value style work (not selected) | Supply agency reports if ratings are needed; the blank context fields are not zero | Context; Q1 release page:1 |
| Context names current period q2-2026 while the latest filed quarter is Q3 2026 | Low | All | Downstream modules label the period they use | Context; Q3 10-Q page:1 |
| Cash-paid interest and cash-paid taxes are not printed in any supplied source | Low | CP-1 | Derive interest burden from the income statement and debt note only, labelled as expense, not cash paid | All sources searched |
| Ownership and sponsor information is blank in the context; listed-equity shareholder detail in the annual report was not reviewed in this step | Low | CP-1A | CP-1A to search the annual report | Context |
| Extraction fidelity of tables was not reviewed against the original HTML filings | Low | All | Spot-check key tables before committee use | All sources |

## Next module

Proceed to CP-1 (financial data) on the full pack. Instructions to carry: (1) label every figure by period (Q3 2026, nine months 2026, FY2025 53-week) and by perimeter; (2) take debt from the Q3 10-Q debt table (page:10) and capacity from page:12, and show the MARPA receivable sales separately (page:9); (3) show the reported Adjusted EBITDA and net leverage as management measures and compute any analyst leverage separately with a stated definition; (4) record the pre-amendment covenant wording from the annual report as such; (5) note the context period mismatch. CP-1A, CP-2 and CP-5 follow in the planner's order. No consumer is marked DO NOT RUN.
