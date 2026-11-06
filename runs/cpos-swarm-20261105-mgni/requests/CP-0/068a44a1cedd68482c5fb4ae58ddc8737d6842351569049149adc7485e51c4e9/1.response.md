# Source readiness: MAGNITE, INC. (mgni)

## Request

- Issuer: MAGNITE, INC. (issuer id mgni, Nasdaq MGNI), as-of date 2026-11-05, information cutoff 2026-11-05 (context). Pathway credit_snapshot; reporting currency USD; current period Q3 2026, prior period FY2025 (context).
- Run `mgni-2026-11-05-credit_snapshot-host`. Requested downstream modules: CP-1, CP-1A, CP-2 and CP-5 (the minimum set). CP-0 runs first as their dependency. Execution is a host session: the analyst read the pinned text files and wrote this answer; no provider was called.
- Question: can the seven supplied public filings and earnings releases support those four modules, and what remains blocked or limited?
- Assertion: SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED. This answer gives no credit conclusion, legal interpretation or investment opinion, and normalizes or reconciles no figures.
- Locator convention: `key pN` means the source chunk `page:N` of the pinned text file (not the printed page). Keys: 10K, Q1Q, Q2Q, Q3Q (Forms 10-K and 10-Q), ER1, ER2, ER3 (earnings releases of May 6, August 5 and November 4, 2026). Quotes are exact substrings of the located chunk.

## Sources

| Key | Source (exact name) | sha256 (pinned file) | Role |
| --- | --- | --- | --- |
| 10K | 10-K_2025-12-31_mgni-20251231.htm.jsonl | f96c3c8e001359e3762f2fdcdb5fec62dc8b34a692251ca50bc2b0320cbc2a0a | Annual report, year ended December 31, 2025 (183 chunks) |
| Q1Q | 10-Q_2026-03-31_mgni-20260331.htm.jsonl | a236956e4f58c23dd0c7e9814923ff8c58122f0f2ffc4593ab7dcd2ac0165adf | Quarterly report, quarter ended March 31, 2026 (57 chunks) |
| Q2Q | 10-Q_2026-06-30_mgni-20260630.htm.jsonl | 796b488acb30e088707602178e4e306b131923e994381f8d88dd91dd9706c3bb | Quarterly report, quarter ended June 30, 2026 (62 chunks) |
| Q3Q | 10-Q_2026-09-30_mgni-20260930.htm.jsonl | c6922a9ebeac839059c55928b8190f39ac8376ff2e5306b6695aa910a9515bb4 | Quarterly report, quarter ended September 30, 2026 (64 chunks) |
| ER1 | EX-99.1_2026-05-06_a991-earningsq12026.htm.jsonl | 1a65026a829ea6d3398cf84619845f6c5e542133314c7959aef5563816dda9a4 | Exhibit 99.1 earnings release, Q1 2026 (12 chunks) |
| ER2 | EX-99.1_2026-08-05_a991-earningsq22026.htm.jsonl | 7a22ad7a167049f41876318b3adec058b3521559a35265d5009853f0eba7f49d | Exhibit 99.1 earnings release, Q2 2026 (14 chunks) |
| ER3 | EX-99.1_2026-11-04_a991-earningsq32026.htm.jsonl | 9404d81beccd30783613c5d17e44e7f768a511dbf6b00a1825d39fa611f52e22 | Exhibit 99.1 earnings release, Q3 2026 (14 chunks) |
| context | context (run settings; not issuer evidence) | add9e4e5fe29cabeba543552138279256276897be557a9b8ceef018e156869fc | Dated user settings; valuation, ratings, deal terms, quotes and research questions are blank or empty |

Supplied handoffs: none (CP-0 is the first module in this run). The retrieval index `_retrieval.json` in the pack was ignored by the launcher and is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The supplied filings and releases are sufficient to run the four planned analyses on Magnite, with limitations. Statements, the current credit agreement description, liquidity, covenant text and the latest quarter are all located. | Medium | No credit agreement, indenture, ratings or market data are supplied, and the text conversion flattens tables. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual and three unaudited quarterly filings are supplied, with a third-quarter report filed on November 4, 2026, one day before the cutoff. | Statements and recent results can be traced to filed documents. | High |
| Only one debt instrument remains: a term loan, with the revolver undrawn. The convertible notes matured March 15, 2026 and were repaid in cash. | Capital structure is simple, but the only legal source is the filings' own description. | High |
| The springing leverage covenant and the October 2026 repricing are described in the filings, but no covenant calculation or credit agreement text is supplied. | Headroom cannot be taken from a supplied figure; the analysis must state that gap. | Medium |
| The releases define operating cash flow differently from the cash flow statement and are management presentations. | Non-GAAP cash figures need filing-based cross-checks before use. | Medium |

### Readiness view

The effective source set supports the requested work with bounded limitations. Every consumer is READY_WITH_LIMITATIONS and none is CONDITIONAL or BLOCKED: the filed statements, the debt note, the liquidity discussion, the covenant description, the subsequent event and the latest quarter are all located in filed documents, and the identity of the reporting entity is not in doubt. The limits are that executed legal documents (the 2024 Credit Agreement and the amendments) are not supplied, that no ratings, price or market data are supplied, that no presentation decks are supplied (the releases stand in), that the sources are text conversions of HTML with flattened tables, and that the Q4 2025 quarter is not separately reported in any supplied document. This is source sufficiency only; the downstream analysis is not done here.

| Consumer | Status | Basis |
| --- | --- | --- |
| CP-1 (financial statements, KPIs, quarter and year-to-date) | READY_WITH_LIMITATIONS | Audited FY2025 and FY2024 statements, plus Q1, Q2 and Q3 2026 interim statements with prior-year comparatives, are located. Discrete Q4 2025 is not reported in a supplied source; flattened tables need a check against the cited chunk. |
| CP-1A (business, history, structure, transactions) | READY_WITH_LIMITATIONS | Business description, one operating segment, 2024 refinancing and amendments, convertible maturity, Google litigation and the October 2026 amendment are located. Subsidiary and guarantor lists and the executed documents are not supplied. |
| CP-2 (capital structure, liquidity, covenants) | READY_WITH_LIMITATIONS | Term loan balance, maturity table, revolver availability net of letters of credit, cash, covenant description and subsequent amendment are located. Credit agreement text, covenant definitions and a reported covenant ratio are not supplied. |
| CP-5 (evidence review of the handoffs) | READY_WITH_LIMITATIONS | All claims can be traced to numbered chunks. Visual and layout checks against the filed HTML are not possible, and releases cannot independently corroborate the 10-Q statements they repeat. |

Command sheet: CP-1 RUN; CP-1A RUN; CP-2 RUN; CP-5 RUN.

### Source register

#### 10K: Form 10-K for the year ended December 31, 2025

- Family and authority: filed annual report; original authority for audited consolidated statements and the annual debt note. Cover: "For the fiscal year ended December 31, 2025" (10K p1); "Commission File Number: 001-36384" (10K p1).
- Audit: the auditor's report covers the balance sheets as of December 31, 2025 and 2024 and the three years ended December 31, 2025: "In our opinion, the financial statements present fairly, in all material respects" (10K p115). Signed "/s/ Deloitte & Touche LLP Los Angeles, California February 25, 2026" (10K p119). Critical audit matters are revenue and income taxes: "Revenue — Refer to Notes 2 and 4 to the financial statements" (10K p117).
- Statements located: balance sheet (10K p119), statements of operations (10K p120), cash flows (10K p121 and p122, with cash paid for interest and taxes on p122). Debt note: "Maturities of the principal amount of the Company's debt were as follows as of December 31, 2025" (10K p148). Liquidity discussion on 10K p102. Signed February 25, 2026 (10K p183).
- Units: thousands of USD for statements; MD&A uses millions.
- Perimeter: consolidated Magnite, Inc. and subsidiaries; subsidiaries guarantee the credit agreement: "secured by substantially all of the assets of the Company and those of its subsidiaries that are guarantors" (10K p64).

#### Q1Q, Q2Q, Q3Q: Forms 10-Q for 2026

- Family and authority: filed, unaudited condensed consolidated statements; original authority for interim figures. Periods: "For the quarterly period ended March 31, 2026" (Q1Q p1), "For the quarterly period ended June 30, 2026" (Q2Q p1), "For the quarterly period ended September 30, 2026" (Q3Q p1). Signed May 6, August 5 and November 4, 2026 (Q1Q p57, Q2Q p62, Q3Q p64).
- Q3Q statements: balance sheet at September 30, 2026 and December 31, 2025 (Q3Q p2); statements of operations for three and nine months (Q3Q p3); cash flows for nine months (Q3Q p5 and p6); debt note (Q3Q p17 to p21); commitments and contingencies (Q3Q p22); subsequent events (Q3Q p29); liquidity and capital resources (Q3Q p50 and p51).
- Basis note: "The condensed consolidated balance sheet at December 31, 2025 has been derived from the audited financial statements at that date" (Q3Q p8). The Q1 and Q2 filings each carry their own comparatives and remain separate sources; Q3Q does not replace them, because it reports only the third quarter and the nine months, not the first and second quarters on their own.

#### ER1, ER2, ER3: Exhibit 99.1 earnings releases

- Family and authority: issuer press releases furnished as Exhibit 99.1: "NEW YORK, May 6, 2026" (ER1 p1), "NEW YORK, August 5, 2026" (ER2 p1), "NEW YORK, November 4, 2026" (ER3 p1). Management-prepared and unaudited; they carry attributed management narrative, guidance and non-GAAP measures.
- Content: reported and adjusted results, reconciliations of net income to Adjusted EBITDA and non-GAAP income (ER3 p12 and p13), Contribution ex-TAC reconciliation (ER3 p12), guidance for Q4 2026 and full-year 2026 and 2027 ("Q4 2026 Expectations:" ER3 p1).
- Version relationship: the release statements repeat the 10-Q statements of the same periods; the 10-Q controls for statement facts and the release is not independent corroboration of them. Where the release defines a measure differently (operating cash flow, free cash flow), the definition is the issuer's own: "Operating cash flow is calculated as Adjusted EBITDA less capital expenditures" (ER3 p2).

### Information-availability boundary

- Every supplied document is dated on or before the cutoff: 10-K February 25, 2026; Q1 filings May 6, 2026; Q2 filings August 5, 2026; Q3 filings November 4, 2026. The cutoff is 2026-11-05, so the latest release and 10-Q are inside the boundary by one day.
- Events after the Q3 filings and before the as-of date are Not supplied, not absent. No document dated 2026-11-05 is supplied.
- Subsequent events that are supplied: Amendment No. 3 of October 7, 2026 (Q3Q p29), an event after the balance sheet date but before the report.

### Identity and perimeter

- Reporting entity: MAGNITE, INC., a Delaware registrant, "Large accelerated filer" box checked (10K p1). The context leaves borrower, parent and guarantor fields blank; the filings name the Company itself as party to the credit agreement ("the Company entered into a credit agreement" (Q3Q p19)) and say the guarantors are subsidiaries (10K p64). Borrower and guarantor entity names are Not supplied.
- Segments: one operating and reportable segment: "operates as one operating segment and one reportable segment" (Q3Q p8). Contribution ex-TAC split into CTV and DV+ is a release and MD&A presentation, not a segment note.
- Currency: USD. Foreign-currency cash is disclosed: "$78.1 million was held in foreign currency denominated cash and cash equivalents accounts" (Q3Q p50). No other reporting currency applies.

### Debt and liquidity evidence located (locators only; nothing is computed here)

- Instrument: the 2024 Term Loan B Facility, "$ 357,730" outstanding at September 30, 2026 against "$ 360,454" at December 31, 2025, in thousands (Q3Q p20). Maturity February 2031; revolver "$175.0 million five-year senior secured revolving credit facility" maturing February 2029 (Q3Q p19). Both secured by "substantially all of the assets of the Company" (Q3Q p19).
- Maturity table: "Maturities of the principal amount of the Company's debt were as follows as of September 30, 2026" with a Thereafter amount of "342,294" (Q3Q p17).
- Revolver: "no amounts were outstanding under the 2024 Revolving Credit Facility" (Q3Q p20); availability "$170.9 million, net of letters of credit outstanding in the amount of $4.1 million" (Q3Q p20). A borrowing of $60.0 million was drawn and repaid in Q2 2026 (Q2Q p18; Q3Q p20).
- Cash: "cash and cash equivalents of $392.9 million" (Q3Q p50).
- Convertible Senior Notes: "On March 15, 2026, the Convertible Senior Notes matured" and the Company "repaid the outstanding principal balance of $205.1 million in full with cash on hand" (Q3Q p14).
- Covenant text: "springing financial covenant that is tested on the last day of any fiscal quarter only if utilization of the 2024 Revolving Credit Facility exceeds 35% of the total revolving commitments" with First Lien Net Leverage Ratio "below 3.25 to 1.00" (Q3Q p20). A reported ratio is not located.
- Amendment No. 3 (October 7, 2026): Term Loan B margin to "Term SOFR plus a margin of 2.50%" from 3.00% and revolver margin range lowered (Q3Q p29 and p30).
- Other claims located: non-cancelable contractual obligations "Total $ 115,219" (Q3Q p22); lease liabilities, current and non-current, on the balance sheet (Q3Q p2); Google antitrust suit filed "on September 16, 2025" with no quantified liability (Q3Q p24).

### Consumer evidence demand

| Consumer | Evidence needed | Located | Not located |
| --- | --- | --- | --- |
| CP-1 | Discrete quarters, year-to-date, FY2025 and FY2024, cash paid for interest and taxes, Adjusted EBITDA reconciliation | Q3 and nine months 2026 with 2025 comparatives (Q3Q p3, p5, p6); FY2025 statements (10K p119 to p122); cash paid for interest "$ 19,064" nine months 2026 (Q3Q p6) and "$ 28,159" FY2025 (10K p122); Adjusted EBITDA reconciliation (ER3 p12 and p13) | Discrete Q4 2025 (derivable only by subtraction, which is a downstream calculation); XBRL |
| CP-1A | Business model, history, structure, transactions, litigation | 10-K business and risk sections (10K p4 to p6, p12); Google litigation (Q3Q p24); refinancing history (Q3Q p19) | Subsidiary list, guarantor names, executed agreements |
| CP-2 | Debt by instrument, maturities, liquidity, covenants, subsequent events | Q3Q p17 to p21, p29, p50, p51; 10K p148, p153, p154 | Credit agreement text, covenant definitions, reported First Lien Net Leverage Ratio, ratings |
| CP-5 | Traceable claims, version relationships, attributed management claims | All of the above, chunk-numbered | HTML or XBRL for layout checks |

## Calculations

None. CP-0 does not normalize, reconcile or calculate figures. Figures quoted above are copied as printed, in the units and periods of their source (thousands of USD in statements, millions of USD in MD&A and releases).

Cross-checks of printed numbers only (no new figures are carried forward): the revolver availability of $170.9 million printed in Q3Q p20 equals the $175.0 million commitment less the $4.1 million letters of credit, both also printed in Q3Q p50, so the three printed numbers agree; the 10-Q and the 10-K print the same Term Loan B margin history (4.50%, then 3.75%, then 3.00%) in Q3Q p19 and 10K p154.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed 2024 Credit Agreement, Amendments No. 1, 2 and 3 are Not supplied; only the filings' description is available (Q3Q p19, p29). The 10-K exhibit index lists the documents (10K p179 to p182). | Medium | CP-1A, CP-2 | Retrieve the exhibits from EDGAR if covenant definitions, baskets or guarantor terms are needed. Until then they are Not supplied and stay a limitation. |
| Reported First Lien Net Leverage Ratio and covenant headroom are Not supplied. The test springs only above 35% revolver utilization and no amount was outstanding at September 30, 2026 (Q3Q p20). | Low to medium | CP-2 | State the test as untested at the balance sheet date; do not invent headroom. |
| Discrete Q4 2025 results are Not supplied: no Q4 2025 release is in the pack. | Low | CP-1 | Derive only from FY2025 less nine months if the method allows, labelled as derived. |
| Subsidiary and guarantor names, restricted-group detail: Not supplied. | Low | CP-1A, CP-2 | Exhibit 21 and the credit agreement. |
| Ratings, quotes, market capitalization, peers and deal terms: the context fields are blank or empty. Blank is not zero. | Medium for valuation work; none for the four requested modules | Relative value, not requested | Not needed for the minimum set. |
| Presentation decks are Not supplied; the three releases stand in. No image, chart or speaker-note coverage is claimed. | Low | CP-1A | Treat releases as attributed management claims. |
| Source format: text extraction of HTML with flattened tables and no XBRL. Extraction is not a fidelity review. Each chunk begins with a line naming a different sha256 for the original HTML (for example 10K p1: "sha256 a15384d1418958b8c582af521cd6843f8612374ade16c857799c92698c2e1012"); the pinned hashes in Sources are for the text files and are the ones relied on. The original HTML is not supplied, so the inner hashes cannot be checked. | Low | All | Cite chunk numbers; recheck any number against its chunk. |
| Release measures differ from GAAP: "Operating cash flow is calculated as Adjusted EBITDA less capital expenditures" (ER3 p2) while the cash flow statement reports "Net cash provided by operating activities" (Q3Q p5). | Medium | CP-1, CP-2, CP-5 | Use filed cash flow statements for cash conversion; use release measures only as labelled management measures. |
| Headline wording in the releases such as "largest independent sell-side advertising company" (ER3 p1) is a management claim, not verified by a filing. | Low | CP-1A, CP-5 | Attribute to management. |

No conflict between a release and a filing was found in the figures compared for CP-0 (net income of $34,005 thousand for Q3 2026 and Adjusted EBITDA of "$83.4 million" appear in ER3 p1 and the reconciliation in ER3 p13, and net income appears in Q3Q p3). Full tie-out is for CP-1 and CP-5.

## Next module

Run CP-1 next, then CP-1A, CP-2 and CP-5, in the order CP-OS sequences them. Carry these limitations forward: (1) the credit agreement and amendments are not supplied, so every covenant, basket and guarantor statement rests on the filings' own description with locators; (2) the Q4 2025 discrete quarter is not separately reported; (3) the releases are management presentations and their cash flow and free cash flow measures are defined differently from the cash flow statement; (4) the October 7, 2026 amendment is a subsequent event and must be labelled as such, not applied to September 30, 2026 balances; (5) tables are flattened, so every figure should be checked against its chunk. Next evidence action: if covenant headroom or guarantor detail matters, retrieve the credit agreement exhibits and Exhibit 21 from EDGAR before relying on them.
