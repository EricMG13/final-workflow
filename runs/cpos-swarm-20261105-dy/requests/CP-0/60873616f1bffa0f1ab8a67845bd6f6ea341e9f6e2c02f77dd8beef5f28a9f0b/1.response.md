## Request

Issuer: DYCOM INDUSTRIES INC (ticker DY, Dycom Industries, Inc., a Florida corporation, SEC file number 001-10613; the single registrant in every filing in the pack). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency per the run context: USD. Current period per the context: q2-2027, meaning the fiscal quarter ended August 1, 2026 (fiscal 2027 ends January 30, 2027). Prior period per the context: fy-2026, meaning the 53-week fiscal year ended January 31, 2026.

Question this handoff answers: can the supplied source set support the requested work (the selected minimum module set: CP-1, CP-1A, CP-2 and CP-5 after this readiness step), and what remains blocked? This is a source-sufficiency review only. It gives no credit conclusion, legal interpretation or investment opinion, and it does not normalize, reconcile or calculate figures. Source sufficiency is not completion of downstream analysis, and no downstream analytical handoff is made a readiness condition.

Context inputs (not issuer evidence): the context names no borrower, parent, guarantors, sponsor, ratings, quotes, deal terms, peers or market data. Those fields are blank and are treated as not supplied, never as zero. Legal documents attached: none (context field `legal_documents` is "none").

Units and conventions found in the sources: the primary statements are in USD thousands; notes, MD&A tables and the results decks are mostly in USD millions. Dycom labels fiscal periods by the calendar year in which the fiscal year ends, so "Q2 2027" in a deck is the quarter ended August 1, 2026, and "fiscal 2026" is the year ended January 31, 2026 (10-Q Q2 FY27 page:5, page:36; 10-K page:8). Fiscal 2026 had 53 weeks, the extra week falling in the fourth quarter, and fiscal 2027 has 52 weeks (10-K page:8, page:51, page:67; 10-Q Q2 FY27 page:5).

## Sources

### Issuer sources relied on

All seven are text extractions (one JSON line per page chunk, not printed pages). The sha256 given is the pack file hash printed by CP-OS. Each file also begins with an embedded line naming the original HTML document and its own hash, which differs from the pack file hash; the pack file hash is the identity used here.

| Source file (exact name) | sha256 | Extracted page chunks | Document family and identity located in the text |
| --- | --- | --- | --- |
| 10-K_2026-01-31_dy-20260131.htm.jsonl | d3cce30e8b33b40ee726fca361a4ac5af2d47cfff9b57a3f36d911b5b73b8e31 | 141 | Form 10-K, fiscal year ended January 31, 2026, registrant Dycom Industries, Inc. (page:1). Filed March 9, 2026 per 10-Q Q2 FY27 page:6. Audited statements with auditor report (page:83-85, page:127-131). |
| 10-Q_2025-10-25_dy-20251025.htm.jsonl | 629b328324cc0ef5393e62b61d8db6e3a1e48e205e2a0f26575592aea3390dd7 | 55 | Form 10-Q, quarter ended October 25, 2025 (Q3 FY26), unaudited, single reportable segment (statements page:2-4; the single-segment statement appears in 10-Q Q2 FY27 page:45). |
| 10-Q_2026-05-02_dy-20260502.htm.jsonl | 237d7d80121afc72a5bb1b73d79141b69d6396b9608af9b8f3dec2db64be0f4f | 53 | Form 10-Q, quarter ended May 2, 2026 (Q1 FY27), unaudited (page:1-3). |
| 10-Q_2026-08-01_dy-20260801.htm.jsonl | 666dcd463f60ce7cc9d18464ad1e3020b3cf1f9ca79b66ed79bb20b35e9cbf79 | 59 | Form 10-Q, quarter ended August 1, 2026 (Q2 FY27), unaudited, signed August 27, 2026 (page:1-5, page:59). Latest period in the pack. |
| EX-99.2_2026-03-04_q42026presentationmateri.htm.jsonl | 6988c6bbc189fb06cb090ad132fb7c67f67f6d428cb3b75cae839c0b2d040376 | 11 | Management results presentation, 4th quarter 2026 results, dated March 4, 2026 (page:1). Unaudited, non-GAAP content. |
| EX-99.2_2026-05-27_q12027presentationmateri.htm.jsonl | fb3e1da73422f05d34562fe3208f0c4af7eb6fffd05db64f60aea98effba2a9e | 11 | Management results presentation, 1st quarter 2027 results, dated May 27, 2026 (page:1). Unaudited, non-GAAP content. |
| EX-99.2_2026-08-26_q22027presentationmateri.htm.jsonl | db5426dcb5222e08c260f53364ad7255c795bb75eba46ab3566a5906d530e4b2 | 10 | Management results presentation, 2nd quarter 2027 results, dated August 26, 2026 (page:1). Unaudited, non-GAAP content. |

Also supplied and ignored by CP-OS: `_retrieval.json` (not issuer evidence, not relied on).

### Run context (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context (67215-dycom-industries-inc-dy.json) | c91849e9583c2227ff5d8a95aa89da364bfff0f885232cdd128e95fb51281f42 |

### Handoffs relied on

None. CP-0 is the first module in this run, and CP-OS supplied no upstream handoff. The run requests CP-1, CP-1A, CP-2 and CP-5 as downstream consumers.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The pack supports a credit snapshot of Dycom through the quarter ended August 1, 2026: audited fiscal 2026 statements, three interim filings and three results decks. Downstream work can proceed within the limits listed. | Medium | The executed credit agreement and note indenture are absent, so covenant definitions and actual covenant ratios cannot be tested against primary documents. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Filings and the latest deck agree on debt components, cash, letters of credit and liquidity at August 1, 2026; one acquisition cash figure differs by a rounding-level amount. | Debt and liquidity inputs can be taken from the filings with limited reconciliation risk. | High |
| Fiscal 2026 had 53 weeks, and the Building Systems segment exists only from December 23, 2025, so year-on-year and segment comparisons are limited. | Trend and margin comparisons need adjustment and clear period labels before they inform leverage or coverage views. | Medium |
| Adjusted EBITDA and organic revenue are management measures, and the fourth-quarter deck shows two different extra-week revenue amounts. Covenant EBITDA is not disclosed. | Leverage and coverage on adjusted figures carry definitional risk until the covenant definition is available. | Medium |

### Readiness view

The overall view is READY_WITH_LIMITATIONS for the requested credit snapshot. The effective source set is internally coherent: one registrant, one fiscal calendar, one reporting currency (USD), audited annual statements for fiscal 2026 with an unqualified opinion on the statements and on internal control (10-K page:127), and unaudited interim statements through the quarter ended August 1, 2026 (10-Q Q2 FY27 page:2-5). The strongest contrary evidence is that every debt-covenant fact is secondhand: the Third Amended and Restated Credit Agreement dated December 23, 2025, its First Amendment dated January 27, 2026 and the April 1, 2021 indenture for the 4.50% senior notes due 2029 are described in the filings and listed as exhibits incorporated by reference (10-K page:139, page:135), but their text is not in the pack. The filings state that Dycom was in compliance with the financial covenants and give the covenant levels (10-Q Q2 FY27 page:21), but they do not print the actual consolidated net leverage ratio, the actual interest coverage ratio, or the Credit Agreement's definition of EBITDA. Evidence to source risk to consequence: without the covenant definition, any leverage or coverage computed from reported or adjusted EBITDA may differ from the tested ratio, so downstream modules must label such figures as analyst constructs and must not present covenant headroom as a fact. The next evidence action is to obtain the executed credit agreement, the First Amendment and the indenture, and the latest compliance certificate if public. Nothing in this step is a credit conclusion.

Consumers are assessed in the table below. None is CONDITIONAL or BLOCKED, because each owner can perform its method on the supplied filings with bounded gaps. The commands for all four are therefore not marked DO NOT RUN.

| Consumer | Evidence demand | Readiness | Limitations carried forward |
| --- | --- | --- | --- |
| CP-1 financial data and registers | Statements, discrete quarters and years, segments, debt and liquidity, cash flows, cash-paid interest and tax | READY_WITH_LIMITATIONS | 53-week fiscal 2026; segment data only from the fourth quarter of fiscal 2026; Adjusted EBITDA is non-GAAP; covenant EBITDA not disclosed; derived discrete quarters need computation downstream; extraction fidelity not reviewed. |
| CP-1A business and transaction context | Business description, customers, acquisitions, governance, history | READY_WITH_LIMITATIONS | Acquisition purchase agreements are not in the pack; the purchase price allocation for the 2027 acquisition is preliminary (10-Q Q2 FY27 page:10); no sponsor or parent exists in the context; management claims in decks are attributed only. |
| CP-2 fundamental credit synthesis | Settled CP-1 and CP-1A registers | READY_WITH_LIMITATIONS | Inherits every limit above. This step does not judge the handoffs that do not exist yet. |
| CP-5 evidence trace validation | Located quotes and figures across modules | READY_WITH_LIMITATIONS | Deck-versus-filing differences listed under conflicts below must be traced to the filing as controlling source. |

Assertion for any HTML model objective: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. No normalized quarters, reconciliation or downstream input acceptance is asserted.

### Source-by-source assessment

| Source | Original authority | Entity and perimeter | Period and basis | Version relationships and limits |
| --- | --- | --- | --- | --- |
| 10-K fiscal 2026 | Filed audited statements; controls over the deck and any management claim | Consolidated Dycom Industries, Inc. and subsidiaries, all wholly owned (10-Q Q2 FY27 page:6 describes the same perimeter); guarantors are "substantially all of our domestic subsidiaries" (page:77, page:114), not named | Fiscal year ended January 31, 2026 with comparatives for January 25, 2025 and January 27, 2024 (page:83); 53 weeks | Annual base for the three 10-Qs; not superseded. Contains debt note (page:112-115), segment note (Note 21, page:123-124), commitments (page:126), exhibit list (page:135-139). |
| 10-Q Q3 FY26 | Filed, unaudited | Same consolidated perimeter before the Power Solutions acquisition | Quarter and nine months ended October 25, 2025; single reportable segment; debt then 945.0 per the Q4 deck (deck page:4) | Separate active interim source. Note 22 records the Power Solutions agreement and debt commitment (page:24). |
| 10-Q Q1 FY27 | Filed, unaudited | Consolidated, includes Power Solutions and the Building Systems segment | Quarter ended May 2, 2026 | Separate active interim source; subsequent events record the National Technology Integrators agreement of May 22, 2026 (page:26). |
| 10-Q Q2 FY27 | Filed, unaudited, latest period | Consolidated, includes Power Solutions and National Technology Integrators from July 2, 2026 (page:27) | Quarter and six months ended August 1, 2026, comparatives July 26, 2025 and January 31, 2026 | Separate active interim source. Carries Note 22 supplier finance (page:29) and Note 23 subsequent events (page:29-30). |
| Q4 FY26 deck | Management presentation; attributed supporting claims | Consolidated and two segments | Quarter and fiscal year ended January 31, 2026; non-GAAP | Does not override the 10-K. Page:7 reconciles organic revenue and page:8 reconciles Adjusted EBITDA. |
| Q1 FY27 deck | Management presentation | Consolidated and two segments | Quarter ended May 2, 2026; non-GAAP | Does not override the 10-Q. Page:5 describes the pending National Technology Integrators acquisition. |
| Q2 FY27 deck | Management presentation | Consolidated and two segments | Quarter and six months ended August 1, 2026; non-GAAP | Does not override the 10-Q. Page:5 holds the updated fiscal 2027 outlook (a forward-looking management statement). |

### Document conflicts and unresolved distinctions

| Item | Locator A | Locator B | Downstream effect |
| --- | --- | --- | --- |
| Cash paid for the 2027 acquisition, net of cash acquired: the 10-Q note gives $225.4 million; the Q2 deck cash-flow slide shows $225.5 million. The six-month cash flow shows $238.3 million for current and previous acquisitions. | 10-Q Q2 FY27 page:10 (Note 5), page:4 (cash flow) | Q2 deck page:4 | Rounding-level difference of $0.1 million, cause not stated. The 10-Q controls. Downstream modules should cite the filing. |
| Extra-week revenue in the fourth quarter of fiscal 2026: the Q4 deck deducts $97.3 million for the quarter and $90.8 million for the fiscal year, although the extra week falls in the fourth quarter (10-K page:8), so the two amounts would be expected to match. | Q4 deck page:7 | Not explained in the deck or the 10-K | Organic growth percentages for the quarter and year (16.6% and 6.5% in the deck) cannot be fully tied. Cite them only as management claims. Unresolved gap. |
| Revolver availability: the 10-K states availability of $746.4 million "as determined by the most restrictive covenant"; the 10-Q Q2 FY27 states the same $746.4 million at both August 1, 2026 and January 31, 2026 without that qualifier. Cash differed between the two dates. | 10-K page:78 | 10-Q Q2 FY27 page:21 | The availability test and its inputs are not disclosed, so the liquidity figure in the deck (page:4) depends on a non-printed computation. Treat liquidity as a management-reported figure with its method in the deck footnote (page:9-10). |
| Prior adjustment of non-GAAP net income: the decks exclude intangible amortization from Adjusted Net Income beginning with the fourth quarter of fiscal 2026 and restate prior periods. | Q2 deck page:9 (note 2) | Q4 deck page:7 | Earlier Adjusted EPS from older releases is not comparable. Only the restated figures in the pack are on the current basis. |

No other conflict between a filing and a deck was found in the figures opened: net income, Adjusted EBITDA, cash, debt components and letters of credit agree between 10-Q Q2 FY27 (page:2, page:20, page:44) and the Q2 deck (page:4, page:7, page:9). Not every number in every source was compared; this is a located-content check, not a reconciliation.

### Coverage by profile

| Profile | Located evidence | Status |
| --- | --- | --- |
| Statements and period labels | Balance sheet, operations, equity and cash flow statements in all four filings (10-K page:83-85; 10-Q Q2 FY27 page:2-5; 10-Q Q1 FY27 page:2-3; 10-Q Q3 FY26 page:2-4) | Retained. Annual and interim bases are distinct. |
| Segments and KPIs | Segment note and MD&A tables in 10-Q Q2 FY27 (page:26-28, page:44-46) and backlog table (page:54-55); 10-K backlog (page:10, page:80) | Retained. Two segments exist only from the fourth quarter of fiscal 2026; the Q3 FY26 10-Q reports one segment. |
| Debt, liquidity and covenants | 10-Q Q2 FY27 Note 14 (page:18-22) and MD&A compliance text (page:51-53); 10-K (page:77-78, page:112-115) | Retained from filings. Executed documents absent. |
| Cash flows, cash-paid interest and tax | 10-Q Q2 FY27 page:4-5 gives six-month cash paid for interest and taxes; 10-K cash flow page:84-85 | Retained. Discrete second-quarter amounts are not printed in the 10-Q; the deck gives quarterly operating cash flow and free cash flow (deck page:4, page:8). |
| Earnings and deck content | Three decks with non-GAAP reconciliations | Retained as attributed management claims. |
| Subsequent events and cutoff | Q2 FY27 10-Q Note 23: new $150.0 million repurchase program announced August 26, 2026 (page:30); deck outlook for the quarter ending October 31, 2026 (deck page:5) | Retained. The results for the quarter ending October 31, 2026 are not in the pack and were not published as of the pack. |
| Controls and audit | Auditor opinions and critical audit matters (10-K page:127-131); disclosure controls effective as of August 1, 2026 (10-Q Q2 FY27 page:56) with the internal-control assessment of National Technology Integrators excluded (page:56) | Retained. |

## Calculations

No new calculation was performed in this handoff, as the method requires for source readiness. No figure above is derived: every amount is copied from the located source with its stated unit and period. The following are comparisons of copied figures, not derivations:

| Comparison | Figure in filing | Figure in deck | Result |
| --- | --- | --- | --- |
| Cash and equivalents, August 1, 2026 | $340,080 thousand (10-Q Q2 FY27 page:2) | $340.1 million (Q2 deck page:4) | Same figure at different precision |
| Standby letters of credit under the Credit Agreement, August 1, 2026 | $53.6 million (10-Q Q2 FY27 page:20) | $53.6 million (Q2 deck page:9) | Same |
| Non-GAAP Adjusted EBITDA, quarter ended August 1, 2026 | $315.5 million (10-Q Q2 FY27 page:44) | $315.5 million (Q2 deck page:7) | Same |
| Total backlog, August 1, 2026 | $12,242 million (10-Q Q2 FY27 page:55) | $12.242 billion (Q2 deck page:3) | Same, in different units |
| Acquisition cash, net of cash acquired, 2027 acquisition | $225.4 million (10-Q Q2 FY27 page:10) | $225.5 million (Q2 deck page:4) | Differs by $0.1 million; listed as a conflict |

Not calculable at this step: any ratio, net debt, liquidity, discrete fourth-quarter or last-twelve-month figure. Reason: calculation is outside this module, and the covenant EBITDA definition is not supplied.

## Gaps

| Gap | Severity | Affected consumers | Remediation | Citation |
| --- | --- | --- | --- | --- |
| Executed Third Amended and Restated Credit Agreement (December 23, 2025), First Amendment (January 27, 2026) and the 2029 notes indenture (April 1, 2021) are not supplied. Terms are known only from filing summaries. | High for covenants and guarantor analysis | CP-1, CP-2, CP-5 | Obtain the executed documents; until then label covenant and guarantee terms as filing summaries | 10-K page:76, page:135, page:139; 10-Q Q2 FY27 page:19-21 |
| Actual consolidated net leverage ratio, interest coverage ratio and the Credit Agreement's EBITDA definition are not printed. Not supplied: the filings state compliance only. | High | CP-1, CP-2 | Obtain compliance certificate or definitions; do not present headroom as a fact | 10-Q Q2 FY27 page:21 |
| Named guarantors are not listed; the filings say "substantially all of our domestic subsidiaries". The 10-K exhibit 21.1 principal subsidiaries list is only named in the exhibit index, and its text is not in the pack. | Medium | CP-1A, CP-2 | Obtain exhibit 21.1 and the guarantor schedule | 10-K page:77, page:114; 10-Q Q2 FY27 page:20 |
| Fiscal 2026 had 53 weeks. The fourth-quarter deck shows two different extra-week revenue amounts that cannot be tied. | Medium | CP-1, CP-2, CP-5 | Use filing figures; cite organic growth as a management claim | Q4 deck page:7; 10-K page:8, page:51 |
| Building Systems segment exists only from December 23, 2025 and the Q3 FY26 10-Q has one segment. No standalone segment history for prior years. | Medium | CP-1, CP-1A | Compare segments only where both periods exist | 10-Q Q2 FY27 page:27, page:45; 10-K page:123-124 |
| No standalone 10-Q or deck for the quarter ended July 26, 2025 (Q2 FY26) and no deck for Q3 FY26. The Q2 FY26 quarter is available only as comparatives in the Q2 FY27 10-Q. | Low | CP-1 | Use comparatives; note they are as presented in the later filing | 10-Q Q2 FY27 page:2-4 |
| Purchase price allocation for National Technology Integrators is preliminary; the Power Solutions working capital adjustment was recorded in the first quarter of fiscal 2027. | Medium | CP-1, CP-1A | Carry as preliminary; check later filings | 10-Q Q2 FY27 page:10, page:35 |
| Results for the quarter ending October 31, 2026 are not in the pack. Management outlook ranges in the decks are forward-looking statements. | Medium | All | Treat outlook as attributed management claims, not actuals | Q2 deck page:5 |
| Deck charts, images and speaker notes were not inspected. Text extraction shows backlog chart values without their axis mapping. No claim of chart or image coverage is made. | Low | CP-1, CP-5 | Use text tables only; log as parse gap | Q2 deck page:3; Q1 deck page:4 |
| Extraction fidelity of the text files against the original HTML was not reviewed; successful extraction is not a fidelity review. | Low | All | Spot-check key figures against statements | All sources |
| Not every page chunk of the 10-K and the 10-Qs was read in this step. Pages were located by search for the profile items above; risk factor, properties and exhibit text were retained but not individually reviewed. | Low | CP-1A | Downstream modules open the pages they cite | 10-K page:1-141 |
| Context supplies no ratings, quotes, market capitalization, net debt, enterprise value, peers or deal terms. Not supplied; not treated as zero. | Medium for valuation work | Not part of the selected set | None needed for the selected modules | Context |
| Customer concentration: AT&T and Verizon each exceeded 10% of contract revenues for the quarter ended August 1, 2026 (Lumen 5.3%), and AT&T's and Verizon's amounts include acquired businesses (AT&T from February 2, 2026; Frontier retrospectively for Verizon). Source is adequate; this limits comparisons across periods. | Low | CP-1A | Use the footnotes explaining the attribution | 10-Q Q2 FY27 page:13, page:25; Q2 deck page:9 |

## Next module

Proceed to CP-1 (and then CP-1A, CP-2, CP-5 in CP-OS order), each READY_WITH_LIMITATIONS. Instructions for the next module:

- Use the 10-K and 10-Qs as controlling sources and the decks only as attributed management support; where a deck and a filing differ, cite the filing and record the difference.
- Label every period explicitly (quarter ended August 1, 2026; six months ended August 1, 2026; fiscal 2026 of 53 weeks) and keep the USD thousands and USD millions units straight.
- Do not state covenant headroom or covenant leverage as a reported fact; the actual ratios and the EBITDA definition are not supplied.
- Carry the unresolved extra-week revenue discrepancy, the revolver availability method and the preliminary purchase price allocation as limitations.
- Next evidence action for the owner: obtain the executed credit agreement, First Amendment, 2029 notes indenture, exhibit 21.1 and the latest compliance certificate.
