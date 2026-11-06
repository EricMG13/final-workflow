## Request

Module CP-0 (source readiness) for Alkermes plc. (issuer id alks, Nasdaq: ALKS, Irish public limited company), as of 2026-11-05, pathway credit_snapshot, run alks-2026-11-05-credit_snapshot-host. Cutoff 2026-11-05; current period Q3 2026 (quarter ended September 30, 2026); prior period FY2025; reporting currency USD. The context file sets no ratings, quotes, deal terms, peers, borrower or parent names and no attachments; blank context values are not treated as zero.

Question answered: can the seven pinned issuer sources support the downstream modules CP-1, CP-1A, CP-2 and CP-5 (the minimum set that feeds the key-findings, operating-model, chart-strip, financials and credit-metrics, strengths-and-weaknesses, company-profile and transaction-summary report sections), and what remains blocked? No credit conclusion is given here. This answer assesses source sufficiency only (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED), and no figure is normalized or reconciled in this module.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Family and date |
| --- | --- | --- |
| 10-K_2025-12-31_alks-20251231.htm.jsonl | e4cb39ef2746983905a66c4851e17231fe0e2b3eb3dd9d346653644971686601 | Annual report, Form 10-K, fiscal year ended December 31, 2025 |
| 10-Q_2026-03-31_alks-20260331.htm.jsonl | 2f002a6c3ee21ba1a12ed08afd7616a7de0cb6e62154bfb1ecb118ba4eafd45f | Quarterly report, Form 10-Q, quarter ended March 31, 2026 |
| 10-Q_2026-06-30_alks-20260630.htm.jsonl | bc67cf08c7dfc8de310d0ecdd1030e2a1391c6b7ce68e53f0b348219bcf79e99 | Quarterly report, Form 10-Q, quarter ended June 30, 2026 |
| 10-Q_2026-09-30_alks-20260930.htm.jsonl | df6328c67d9ab03d30760e47eacac03760e7e83fb341e7073082128f2c7068d4 | Quarterly report, Form 10-Q, quarter ended September 30, 2026 |
| EX-99.1_2026-05-05_alks-ex99_1.htm.jsonl | 3f53152d2ff381e382b1d7a092db23f6a1d1dce5883995e4eda0a38a2d5d57a8 | Earnings release (Exhibit 99.1), first quarter 2026, dated May 5, 2026 |
| EX-99.1_2026-07-28_alks-ex99_1.htm.jsonl | 4e5567773d88766be4958174400b81baacad01bd80fe607c8eb27ade6994b31f | Earnings release (Exhibit 99.1), second quarter 2026, dated July 28, 2026 |
| EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl | 041cf8e725b3d45a5b701a4d1acae145f94c2d37b75244f3f5fe173ac5392fc6 | Earnings release (Exhibit 99.1), third quarter 2026, dated November 3, 2026 |

Run context (not issuer evidence): context sha256 885addee0d736fc42d87bc797174ed4ac35a16798074c06e23b1959b2f8975fb. The file _retrieval.json in the pack folder was ignored by CP-OS and is not relied on.

Each source text begins with a line naming the original HTML file and its own sha256 (for example the 10-K line reads "Visible text of 10-K_2025-12-31_alks-20251231.htm, sha256 fa48049fc0dbfc7a7165a35030ee5062ba7c8be0f979cb29b9799665e81dde46."). That embedded hash identifies the original HTML and differs from the pinned hash of the extracted text file listed above; the pinned hashes above are the ones relied on.

### Supplied handoffs

None. CP-0 is the first module of this run and CP-OS supplied no upstream handoff.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filed statements and earnings releases through the third quarter of 2026 support a credit snapshot of Alkermes after the Avadel acquisition, with limitations. Debt, cash and operating results are well covered; covenant levels are not. | Medium | The credit agreement and its amendment are not in the pack, so covenant levels, guarantors and pricing grid cannot be read. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited FY2025 statements and three 2026 quarterly reports are present, with matching earnings releases. | Annual and quarterly figures can be traced to filed statements. | High |
| The Avadel acquisition closed on February 12, 2026, so 2026 periods are not comparable with FY2025. | Pre-acquisition history understates the current debt and cost base. | High |
| Debt is two term loans with carrying and principal amounts in the notes; covenant levels are only named. | Leverage and coverage headroom cannot be tested from the pack. | Medium |
| No revolving facility, interest paid for 2026 or rating is found in the sources. | Liquidity rests on cash and investments only. | Medium |
| The purchase price allocation is preliminary and some management add-backs differ from statement figures. | Goodwill, intangibles and adjusted EBITDA may be restated or need care. | Medium |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for the four downstream modules that CP-OS will run. The pack contains the audited FY2025 annual report, the three 2026 quarterly reports including the quarter ended September 30, 2026 filed before the cutoff, and the three matching earnings releases, so statements, debt and liquidity notes, the Avadel business combination note, litigation, subsequent events and management non-GAAP reconciliations are all located in filed or furnished text. The limiting gaps are source gaps, not extraction failures: the executed credit agreement and its first amendment are referenced but not supplied, so covenant levels, step-downs, the margin grid, guarantor identities and baskets cannot be read; no revolving credit facility is described anywhere in the pack; cash paid for interest is not presented for any 2026 period; the Avadel purchase price allocation is preliminary; no presentation decks are supplied; and the discrete fourth quarter of 2025 has no standalone report. None of these prevents a consumer from performing its own method, because each consumer can state the gap and carry it forward. No consumer is CONDITIONAL or BLOCKED. The next evidence action is to obtain the executed credit agreement and amendment (both listed as exhibits) before any covenant headroom is stated.

### Source-by-source assessment

| Source | Original authority and perimeter | Period and basis | Version relationship and limitation |
| --- | --- | --- | --- |
| 10-K FY2025 | Audited annual report of Alkermes plc and subsidiaries; auditor opinion present on page:162 and statements on pages:165-168 | Years ended December 31, 2025, 2024 and 2023, USD thousands, US GAAP | Pre-acquisition: Avadel acquisition and the term loans are described as post-year-end events. Authority for FY2025; superseded for 2026 by later 10-Qs |
| 10-Q Q1 2026 | Unaudited condensed consolidated statements of Alkermes plc and subsidiaries | Three months ended March 31, 2026 versus 2025 and December 31, 2025 balance sheet | First report including Avadel (closed February 12, 2026) and the original term loans; amounts later affected by the August 2026 amendment |
| 10-Q Q2 2026 | Unaudited condensed consolidated | Three and six months ended June 30, 2026 | Separate active source; cumulative six-month cash flow, not discrete Q2 |
| 10-Q Q3 2026 | Unaudited condensed consolidated; most recent filing, signed November 3, 2026 | Three and nine months ended September 30, 2026 | Controls Q3 2026 and the September 30, 2026 balance sheet; describes the amended credit agreement |
| EX-99.1 May 5, 2026 | Issuer earnings release; management narrative and non-GAAP | Q1 2026 | Supporting attributed claims; filings control where they differ |
| EX-99.1 July 28, 2026 | Issuer earnings release containing 2026 financial expectations | Q2 2026 | Contains the guidance table that the November release says it reiterates |
| EX-99.1 November 3, 2026 | Issuer earnings release, unaudited, with GAAP to Adjusted EBITDA reconciliation | Q3 2026 and nine months 2026 | The release states the 10-Q was still to be filed; the 10-Q in the pack is dated November 3, 2026 |

Entity roles. Alkermes plc is the registrant and the TopCo Borrower; Alkermes, Inc. is the U.S. Borrower and Alkermes Finance LLC the U.S. Co-Borrower (10-Q_2026-09-30_alks-20260930.htm.jsonl page:28, "Alkermes plc, as the TopCo Borrower, Alkermes, Inc., as the U.S. Borrower, Alkermes Finance LLC, as the U.S. Co-Borrower"). Guarantors are only described generically: "The Credit Agreement is guaranteed by subsidiary guarantors and secured by a lien on substantially all of the assets of the borrowers and the subsidiary guarantors" (10-Q_2026-09-30_alks-20260930.htm.jsonl page:28). No parent, sponsor, restricted or unrestricted subsidiary designation appears in the pack or the context; the registrant is the top entity and listed equity issuer. Presentation is consolidated and single-segment: "is managed as one segment on a consolidated basis" (10-Q_2026-09-30_alks-20260930.htm.jsonl page:14).

### Coverage by evidence area

| Evidence area | Located evidence | Status |
| --- | --- | --- |
| Audited annual statements | Audit opinion: "present fairly, in all material respects, the financial position of the Company as of December 31, 2025 and 2024" (10-K_2025-12-31_alks-20251231.htm.jsonl page:162); balance sheet page:165, operations page:166, cash flows page:168 | Retained |
| Quarterly statements and notes | Balance sheet, operations and cash flows at 10-Q_2026-09-30_alks-20260930.htm.jsonl pages:5-8; equivalent statements in the Q1 and Q2 10-Qs at pages:5-7 | Retained |
| Debt and facility terms | Note 12 table lists Term Loan A Facility, due February 12, 2031 and Term Loan B Facility, due August 12, 2031 (10-Q_2026-09-30_alks-20260930.htm.jsonl page:27); terms, amendment, maturities and compliance statement at pages:28-30 | Retained, covenant levels absent |
| Original facility size | "the Company borrowed the full $1.525 billion available under the Facilities" (10-K_2025-12-31_alks-20251231.htm.jsonl page:193) | Retained |
| Liquidity | Cash, investments and the management sufficiency statement: "We expect that our existing cash, cash equivalents and investments will be sufficient to finance our anticipated working capital and other cash requirements" (10-Q_2026-09-30_alks-20260930.htm.jsonl page:50); total cash and investments "$787.6 million" (EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl page:2) | Retained, no revolver found |
| Business combination | "the Company completed the acquisition of Avadel Pharmaceuticals plc" with consideration, preliminary allocation and unaudited pro forma figures (10-Q_2026-09-30_alks-20260930.htm.jsonl pages:15-19) | Retained, preliminary |
| Contingent consideration | "a potential additional aggregate cash payment of $165.7 million, or $1.50 per Avadel Share, upon achievement of the CVR Milestone" (10-Q_2026-09-30_alks-20260930.htm.jsonl page:53) | Retained |
| Litigation and contingencies | Note 18 at 10-Q_2026-09-30_alks-20260930.htm.jsonl pages:34-36, including LUMRYZ, LYBALVI and VIVITROL matters and the Acorda appeal | Retained |
| Management non-GAAP | EBITDA and Adjusted EBITDA reconciliations for Q3 2026 and nine months 2026 (EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl page:6); definition: "Adjusted EBITDA excludes share-based compensation expense and non-recurring gains or losses" (page:3) | Retained, management measure |
| Guidance | 2026 expectations table in EX-99.1_2026-07-28_alks-ex99_1.htm.jsonl page:2; the November release "reiterates its financial expectations for 2026" by reference (EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl page:2) | Retained, forward-looking |
| Subsequent events to cutoff | October 2026 interest rate collars: "In October 2026, the Company entered into two zero-cost interest rate collar agreements, each with a notional amount of $375.0 million" (10-Q_2026-09-30_alks-20260930.htm.jsonl page:30) | Retained |

### Strongest contrary evidence and limitations

1. Covenants. The covenant package is named but not quantified: "requires the maintenance of a maximum Secured Net Leverage Ratio and a minimum Consolidated Interest Coverage Ratio (as defined in the Credit Agreement), in each case, with the levels set forth in the Credit Agreement" (10-Q_2026-09-30_alks-20260930.htm.jsonl page:28), and compliance is a management statement only: "The Company was in compliance with its debt covenants at September 30, 2026." (page:30). The text carves out the Term Loan B from the maintenance tests. Mechanism: without levels, defined terms and add-back rules, headroom cannot be computed from the statements, so any leverage or coverage view is a computed ratio, not the covenant measure.
2. Period comparability. The business combination closed on February 12, 2026, so nine months 2026 contains Avadel results only from that date, while FY2025 and nine months 2025 contain none. The company states that "the presentation of net (loss) income is impracticable due to the integration of Avadel’s operations" (10-Q_2026-09-30_alks-20260930.htm.jsonl page:19). Unaudited pro forma revenue and net income are given in the same note, as a separate comparative basis. Consequence: trend statements across FY2025 and 2026 need the pro forma note and explicit labelling.
3. Preliminary accounting. "The Company’s purchase price allocation is preliminary" (10-Q_2026-09-30_alks-20260930.htm.jsonl page:16, in the note text "purchase price allocation is preliminary and based on the information available as of the reporting date"); goodwill and intangibles can still move for up to one year from closing.
4. Liquidity structure. No revolving facility, undrawn commitment or letter of credit facility is described in any pinned source (searches for "revolv" returned no match in all seven sources). The only letters of credit mentioned are collateralised by held-to-maturity investments tied to leases (10-Q_2026-09-30_alks-20260930.htm.jsonl page:50). Liquidity therefore equals cash and investments in the sources, and the absence of a revolver is a finding of the searched text, not proof the issuer has none.
5. Management add-backs. The nine-month reconciliation adds back share-based compensation of 112,624 thousand (EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl page:6) while the cash flow statement shows 94,216 thousand (10-Q_2026-09-30_alks-20260930.htm.jsonl page:7). The difference is unexplained in the pack and is carried as a conflict below.

### Conflicts and anomalies (logged, not reconciled)

| Item | Span A | Span B | Downstream effect |
| --- | --- | --- | --- |
| Facility principal | "provides for (i) a senior secured term loan A facility in an outstanding principal amount of $745.3 million" (10-Q_2026-09-30_alks-20260930.htm.jsonl page:28) with TLB at $773.1 million | Scheduled maturities total 1,511,750 thousand (10-Q_2026-09-30_alks-20260930.htm.jsonl page:29) | Which principal applies at September 30, 2026 needs a choice; the schedule is a dated September 30 table, the narrative amounts are undated. Source-check arithmetic is in Calculations |
| Share-based compensation, nine months 2026 | 112,624 thousand in the release reconciliation (EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl page:6) | 94,216 thousand in the cash flow statement (10-Q_2026-09-30_alks-20260930.htm.jsonl page:7) | Adjusted EBITDA is a management measure whose add-backs do not tie to the statements; consumers must state which basis they use |
| Share-based compensation, Q3 2026 | 26,747 thousand in the release (EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl page:6) | 27,308 thousand in the equity statement (10-Q_2026-09-30_alks-20260930.htm.jsonl page:8) | Same as above, quarter basis |
| Balance sheet captions | Release shows Other assets of 152,604 thousand (EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl page:7) | 10-Q shows Other assets of 72,876 thousand and right-of-use assets of 79,728 thousand (10-Q_2026-09-30_alks-20260930.htm.jsonl pages:5-6) | Classification difference between release and 10-Q; filed 10-Q controls |

### Consumer readiness

| Consumer | Assessment | Evidence demand and carried limitation |
| --- | --- | --- |
| CP-1 (financial extraction and credit metrics) | READY_WITH_LIMITATIONS | Needs statements, debt table, maturities, cash flow and non-GAAP. All present. Carry: no covenant levels, no revolver, no 2026 cash interest paid, preliminary allocation, Avadel comparability, SBC add-back differences. Discrete Q4 2025 has no standalone report; annual FY2025 plus nine-month comparatives are present |
| CP-1A (business and transaction context) | READY_WITH_LIMITATIONS | Needs business description, Avadel transaction terms, milestone payment, litigation and history. Present in the 10-K Item 1 and 10-Q notes. Carry: the Avadel transaction agreement and CVR terms are exhibits not supplied; management language in releases is attributed, not adopted |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Draws only on CP-1 and CP-1A handoffs, which the dependency planner sequences; no source condition. Carry all CP-1 and CP-1A gaps, plus no ratings or market data in the context |
| CP-5 (evidence trace validator) | READY_WITH_LIMITATIONS | Needs the pinned pack to test citations; all seven sources are text-extracted and quotable. Carry the conflicts logged above |

Extraction fidelity. All seven sources extracted to page text. Extraction is not a fidelity review: tables are flattened so each number sits on its own line, which preserves values but not layout. No images, charts or speaker notes were inspected, and no deck is supplied, so no presentation coverage is claimed. The November release mentions "webcast presentation with accompanying slides" (EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl page:2), and those slides are not in the pack.

## Calculations

No normalization, reconciliation or new analytical figure is produced in this module. The following source-consistency checks use only printed figures and are recorded so downstream modules know which ties hold.

| Check | Inputs (USD thousands unless stated) | Result |
| --- | --- | --- |
| Debt carrying amount ties to balance sheet | Term Loan A 735,016 plus Term Loan B 762,715 (10-Q_2026-09-30_alks-20260930.htm.jsonl page:27) equals 1,497,731; current portion 26,500 plus long-term debt 1,471,231 (page:6) equals 1,497,731 | Ties exactly |
| Carrying amount to scheduled principal | Carrying 1,497,731 plus unamortized original issue discount 10.4 million plus unamortized deferred financing costs 3.6 million (page:30) gives about 1,511.731 million; schedule total 1,511,750 (page:29) | Differs by about 0.019 million, within rounding of the two printed millions |
| Narrative principal versus schedule | TLA 745.3 million plus TLB 773.1 million (page:28) equals 1,518.4 million; schedule total 1,511.750 million (page:29) | Narrative exceeds schedule by 6.65 million; unexplained in the sources. The scheduled 2026 remaining payment is 6,625 thousand, which is close but is not asserted as the cause |
| Cash and investments tie | Cash 631,314 plus short-term investments 124,150 plus long-term investments 32,110 (page:5-6) equals 787,574; release states 787.6 million (EX-99.1_2026-11-03_alks-ex99_1.htm.jsonl page:2) | Ties |
| Borrowing flows | Net proceeds on original borrowings 1,511.6 million plus 45.5 million additional proceeds equals 1,557.1 million, matching proceeds from issuance of debt, net of 1,557,097 thousand (10-Q_2026-09-30_alks-20260930.htm.jsonl pages:7 and 52) | Ties |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed Credit Agreement dated February 12, 2026 and Amendment No. 1 dated August 12, 2026 not supplied; both are listed as exhibits ("Amendment No. 1 to Credit Agreement, dated as of August 12, 2026", 10-Q_2026-09-30_alks-20260930.htm.jsonl page:58, and the original at 10-Q_2026-03-31_alks-20260331.htm.jsonl page:50). Covenant levels, step-downs, definitions, baskets, margin grid thresholds and guarantor names are Not supplied | High | CP-1, CP-2, CP-5 | Add both documents to the pack; until then headroom is Not calculable |
| No revolving credit facility, undrawn commitments or letter of credit capacity found in any source; liquidity can only be stated as cash and investments | Medium | CP-1, CP-2 | Confirm in the credit agreement whether any revolver exists |
| Cash paid for interest not presented for 2026 periods; the Q3 10-Q supplemental disclosure shows cash paid for taxes only (10-Q_2026-09-30_alks-20260930.htm.jsonl page:8), while the 10-K shows an interest-paid line of nil for 2025 | Medium | CP-1 | Use interest expense from the statements and label it as expense, not cash paid |
| Avadel purchase price allocation preliminary; measurement period open up to one year from February 12, 2026 | Medium | CP-1, CP-1A, CP-2 | Treat goodwill and intangibles as provisional |
| Avadel Transaction Agreement, CVR terms and Rule 2.7 announcement are exhibits not supplied | Low | CP-1A | Rely on the 10-K and 10-Q descriptions; milestone terms beyond them are Not supplied |
| No quarterly presentation decks in the pack; only the three earnings releases | Low | CP-1A | No presentation coverage is claimed |
| Discrete Q4 2025 and Q4 2024 have no standalone report or release; annual figures only | Low | CP-1 | Derive only with explicit subtraction labelling, or leave Not calculable |
| Management non-GAAP add-backs do not tie to statement share-based compensation | Medium | CP-1, CP-5 | Present Adjusted EBITDA as management's measure with the conflict noted |
| Guarantor names, restricted-group definition and collateral schedules not supplied | Medium | CP-1A, CP-2 | See credit agreement gap |
| Context holds no ratings, market quotes, peers or deal terms; no bonds or notes appear in the debt note | Low | CP-2 | State as Not supplied; no market-based view is possible from this pack |
| Cash-flow interest rate hedge effect: collars entered in October 2026 are described but no fair value or effect on interest cost is stated | Low | CP-1 | Carry as a subsequent event with notional and strike terms only |

## Next module

Proceed to CP-1 with the seven pinned issuer sources and this handoff. Carry forward: the covenant, revolver and interest-paid gaps; the open Avadel purchase price allocation; the February 12, 2026 comparability break between FY2025 and 2026 periods (use the unaudited pro forma note and label it); the conflicts between release add-backs and statement figures; the debt principal narrative versus schedule difference; and the October 2026 collar subsequent event. CP-1A, CP-2 and CP-5 follow in the order set by the dependency planner; none is blocked by source evidence.
