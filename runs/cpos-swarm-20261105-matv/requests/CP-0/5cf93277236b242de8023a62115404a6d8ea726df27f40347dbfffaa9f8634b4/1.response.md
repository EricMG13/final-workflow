## Request

Module: source readiness for Mativ Holdings, Inc. (ticker MATV, issuer id matv), pathway credit_snapshot, as-of date 2026-11-05 (cutoff 2026-11-05). Reporting currency USD, in millions unless a line says otherwise; current period Q3 2026 (quarter and nine months ended September 30, 2026), prior period FY2025 (run context, not issuer evidence). Case kind: public. Requested downstream modules: CP-1, CP-1A, CP-2, CP-5, with the minimum report sections key findings, company operating model, model chart strip, financials and credit metrics, strengths and weaknesses, company profile and transaction summary. Capital structure, relative value, portfolio fit, committee challenge and what-changed sections are not part of this run.

Question answered here: can the supplied source set support that work, and what remains blocked. This handoff gives no credit conclusion and no investment opinion. It does not normalize quarters, reconcile non-GAAP measures or accept any downstream input (SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED).

Run context supplies no ratings, quotes, deal terms, peers, valuation inputs, sponsor, borrower, parent or guarantor names; those fields are blank and are treated as not supplied, not as zero or none.

## Sources

### Issuer sources relied on

All seven are SEC filings by the registrant itself (text extraction, one JSONL row per source chunk; `page:N` is the chunk number, not the printed page). The sha256 below is the pinned hash of the supplied JSONL. Each file's first row also prints the hash of the original HTML, shown in the last column for traceability.

| Source name | sha256 (pinned JSONL) | Pages retained | HTML sha256 printed on page:1 |
| --- | --- | --- | --- |
| 10-K_2025-12-31_matv-20251231.htm.jsonl | 0987bdd177918d1704e3f88d583ff72f6a39e66a94dd95882dba466d3888311c | 135 | 6cf155f27518a32f76ae30ed1951e5867e99d3ce4232f4684b7b5dc5739f819c |
| 10-Q_2026-03-31_matv-20260331.htm.jsonl | be2515741fe2f13e179c4c2e30c15996c434ad9db582dc94e1ef7a9b4954e68d | 33 | ad1de47fdff5ba2cecb96531388ad1efa2294159417e846562e7d4c146644fb2 |
| 10-Q_2026-06-30_matv-20260630.htm.jsonl | 7184a20d311477dd5cb1dfc9b30dba5f1ea74b357d6c5b8b24327bc29eea17ff | 34 | 411ceb9d9e9a0f5d9fc9286f17cfc17ab7684f645a16870f4521bb3a03085447 |
| 10-Q_2026-09-30_matv-20260930.htm.jsonl | cd05c1595b274a699b4cdcd913ff17f3c1b042cf31d245b0741f58eac17a20fb | 34 | 78f80204e5a0c435c1779d1b30a1baaad0a34d97f3025048483aac5d96a91284 |
| EX-99.1_2026-05-06_ex991earningsrelease2026q1.htm.jsonl | 9f2d35ab42751d0b53917904e34ca17dd018903790ffb5f1f2e30283805e8933 | 10 | 3806def35ba83980ecbaddb4da9e422d0e71874fa39e5241c937ef772fe857a5 |
| EX-99.1_2026-08-05_ex991earningsrelease2026q2.htm.jsonl | 6cdc4bf84d342bfc79bbfbfa3bbc0faf89dc1156b59bfb476359102520bc07e0 | 11 | e0ca23387d9b2f01c419fae4a5c8f8d1f8b5185dae454bbafc73cfb850a3e698 |
| EX-99.1_2026-11-04_ex991earningsrelease2026q3.htm.jsonl | 1d8a4657f455e3276abc49c4e3ccf64e82f7d0ab6a0f632c1c495bd5b53fcf53 | 11 | 6a61807df94a304a57603966f303d53a5ed23e9525ab76791248c3223c213746 |

### Run context (settings, not issuer evidence)

| Source name | sha256 |
| --- | --- |
| context (1000623-mativ-holdings-inc-matv.json) | 43cba5e2e4b206f93654450fc247b91671c4b4e4ab36f2ccb3891319991c5f21 |

### Handoffs relied on

| Handoff module | sha256 |
| --- | --- |
| None supplied: this module is the first in the run order (CP-0, then CP-1, CP-1A, CP-2, CP-5) | Not applicable |

A pack file named `_retrieval.json` is ignored by the run and is not used as evidence here.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied filings and earnings releases are enough for the requested financial, business and synthesis work, with bounded gaps. They do not cover the legal documents, ratings or an annual adjusted earnings figure. | Medium | The credit agreement, indenture and receivables agreement are absent, and trailing adjusted earnings cannot be built from the pack. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every page of all seven sources was retained, and the three quarterly filings tie to the nine-month totals. | Quarterly and year-to-date figures can be used with a low risk of extraction error. | Medium |
| Covenant terms are described only in summary; the amended agreement itself is not in the pack. | Covenant headroom beyond the stated leverage figure cannot be tested. | Medium |
| Adjusted earnings appear only in management releases, and none for the fourth quarter of 2025 or the full prior year. | The management leverage figure cannot be reproduced from supplied inputs. | High |
| The July tornado and the October receivables amendment are disclosed, but recovery and facility size after the amendment are open. | Liquidity and working-capital effects need cautious treatment. | Medium |

### Readiness view

Overall view: READY_WITH_LIMITATIONS for the requested module set. The registrant is a single reporting entity, Mativ Holdings, Inc., filing consolidated statements for itself and its subsidiaries; there is no parent, sponsor or separate borrower reporting entity in the supplied evidence, so the perimeter question that arises for subsidiary issuers does not arise here. The latest annual report (FY2025, filed with an audit opinion and an effective internal control opinion, 10-K page:121 and page:125) and the three 2026 quarterly reports give a continuous filed-statement series from December 31, 2025 to September 30, 2026. The three earnings releases supply attributed management measures (adjusted EBITDA, adjusted income, free cash flow, net debt, liquidity) that no filing in the pack supplies. These are supporting claims; the filed statements control where both speak to the same fact.

Strongest contrary evidence and limits: (1) the governing financing documents (the Ninth Amendment to the credit agreement of April 3, 2026, the indenture for the 8.000% senior notes due October 1, 2029, the receivables purchase agreement and its October 23, 2026 amendment) are only summarized in notes, so definitions, baskets, covenant step-down dates and guarantor lists cannot be read at source; (2) none of the periodic reports prints adjusted EBITDA and the releases cover only the first three quarters of 2026 with 2025 comparatives, so an annual or trailing figure is not available from supplied inputs and the stated net leverage cannot be reproduced; (3) no credit ratings, presentations, call transcripts or market quotes are supplied. Evidence-to-risk-to-consequence: the missing legal text means the downstream financial module can state covenant levels as management and note disclosures describe them but cannot test definitions; the missing annual adjusted figure means downstream leverage must be shown on reported-debt and reported-GAAP bases with management's figure attributed.

What cannot proceed: any analysis that depends on reading the financing documents themselves is outside what this pack can support and is not part of the requested set; relative value, market pricing and rating-based views are likewise outside the supplied evidence. What can proceed: all four requested modules, per the consumer table below. Next evidence action: add the credit agreement as amended and the indenture (both filed as exhibits per the 10-K and Q1 10-Q exhibit lists), the fourth quarter 2025 earnings release, and any rating agency publications, if the committee needs covenant headroom or a trailing adjusted leverage figure.

### Source profile

| Source | Document family and authority | Entity and perimeter | Period and basis | Version relationship |
| --- | --- | --- | --- | --- |
| 10-K FY2025 | Annual report, filed audited statements; controls for FY2025 and earlier facts (page:1, page:75) | Mativ Holdings, Inc. and subsidiaries, consolidated (page:75) | Years ended December 31, 2025, 2024, 2023; USD millions; continuing operations basis after the 2023 Engineered Papers divestiture (page:4) | Base annual source; December 31, 2025 balances are repeated in later 10-Qs with some line condensation (see conflicts) |
| 10-Q Q1 2026 | Quarterly report, unaudited filed statements (page:2) | Consolidated | Three months ended March 31, 2026 vs 2025 | Separate source; the Ninth Amendment is treated as a subsequent event in Note 14 (page:21) |
| 10-Q Q2 2026 | Quarterly report, unaudited filed statements (page:2) | Consolidated | Three and six months ended June 30, 2026 vs 2025 | Separate source; first quarter-end balance sheet under the amended facilities; the July 27, 2026 tornado is a subsequent event (page:21) |
| 10-Q Q3 2026 | Quarterly report, unaudited filed statements (page:2, page:3) | Consolidated | Three and nine months ended September 30, 2026 vs 2025; balance sheet vs December 31, 2025 | Latest filed financial source; quantifies the tornado (page:17, page:18); lists subsequent events (page:22, page:23) |
| Release Q1 2026 (May 6, 2026) | Earnings release furnished as exhibit; management claims and non-GAAP measures (page:1, page:10) | Consolidated | Three months ended March 31, 2026 | Separate dated release; the only source of that quarter's adjusted EBITDA |
| Release Q2 2026 (August 5, 2026) | Earnings release; same status (page:1, page:11) | Consolidated | Three months ended June 30, 2026 | Retained separately |
| Release Q3 2026 (November 4, 2026) | Earnings release; same status (page:1, page:11) | Consolidated, segments FAM and SAS | Three and nine months ended September 30, 2026 | Latest management source, dated before the cutoff |

Instrument and entity roles found: issuer and registrant Mativ Holdings, Inc.; the 8.000% senior unsecured notes due October 1, 2029 are guaranteed by wholly-owned subsidiaries that are borrowers or guarantors under the senior secured facilities (10-Q Q3 page:12); under the pre-amendment agreement the secured facilities were guaranteed by wholly-owned direct material domestic subsidiaries and Mativ Luxembourg (10-K page:100); after the Ninth Amendment certain subsidiaries became additional U.S. borrowers and another a guarantor, unnamed (10-Q Q3 page:13); a bankruptcy-remote special purpose entity receives the sold receivables (10-K page:93, Mativ Receivables LLC named in the exhibit list, page:132). The supplied text does not print a guarantor list or Exhibit 21.1 content.

### Consumer readiness

| Consumer | Evidence demand | Readiness | Limitations carried forward |
| --- | --- | --- | --- |
| CP-1 financial extraction | Statements, notes, segment and KPI tables, debt, liquidity, covenants, cash flows, quarter vs year-to-date | READY_WITH_LIMITATIONS | No annual or trailing adjusted EBITDA; facility-level debt only at carrying value net of issuance costs plus a principal maturity table; letters of credit not printed; covenant ratios stated for leverage only; December 31, 2025 line condensation |
| CP-1A business and transaction context | Business description, ownership, transactions, history | READY_WITH_LIMITATIONS | Cover page shows NYSE-listed common stock (10-Q Q3 page:1) and no sponsor or parent was found in the sources or the context; transaction facts (refinancing, tornado, receivables amendment, held-for-sale facility sale) are in filed notes; no legal documents for the refinancing |
| CP-2 credit synthesis | Upstream registers only | READY_WITH_LIMITATIONS | Inherits all limits above; no ratings or market data |
| CP-5 evidence trace | Upstream modules and their citations | READY | Nothing source-side beyond the limits above; its result depends on upstream citations |

Report sections: key findings, operating model, model chart strip, financials and credit metrics, strengths and weaknesses, company profile and transaction summary can be populated from these sources. The model chart strip needs discrete quarters: Q1, Q2 and Q3 2026 statements are all supplied, and the three quarters tie to the nine-month totals (see Calculations); a discrete fourth quarter of 2025 would have to be derived from the 10-K and is not supplied as a quarter.

### Conflicts, restatements and unreconciled items

| Item | Locator A | Locator B | Downstream effect |
| --- | --- | --- | --- |
| December 31, 2025 balance sheet is shown with condensed lines in the Q3 10-Q: property, plant and equipment, net of 624.9 there equals 609.1 plus finance lease right-of-use assets of 15.8 in the 10-K; accrued expenses and other current liabilities of 111.2 there equals 109.4 plus current finance lease liabilities of 1.8 in the 10-K. Totals agree (total assets 2,051.6; total current liabilities 285.3). The Q3 10-Q states a reclassification only for the cash flow statement | 10-K page:76 | 10-Q Q3 page:2, page:3, page:6 | Use the 10-K lines for lease detail; do not treat the change as a restatement of totals |
| Debt table label changed from "German loan agreement" (3.7) to "Other loan agreements" (3.7) at December 31, 2025 | 10-K page:99 | 10-Q Q3 page:12 | Same amount, different label |
| Prior-year restructuring add-back differs between the two release reconciliations: Q3 2025 shows 9.7 in the adjusted income table and 10.6 in the adjusted EBITDA table (nine months 2025: 19.4 and 20.7). The release does not explain the basis difference | EX-99.1 Q3 page:10 | EX-99.1 Q3 page:11 | Carry as a presentation difference between non-GAAP tables; adjusted EBITDA is a management measure |
| Maturity of the revolver and Term Loan A: Note 8 says they mature on the earlier of five years from April 3, 2026 or 182 days before the maturity of the 8.000% notes due 2029, and Term Loan B on the earlier of seven years or 91 days before that maturity. The maturity table puts only the notes and small amortization in 2029 (406.2) and the rest in "Thereafter" (583.8), and the MD&A calls the notes the nearest maturity | 10-Q Q3 page:13 | 10-Q Q3 page:14, page:28 | Read literally the text places the revolver and Term Loan A earlier than the notes; the table and MD&A do not. Carry as an unresolved presentation conflict; the amended agreement is needed to settle it |
| Cash dividends: 17.0 in the cash flow statement vs 16.9 in the equity statement for nine months 2026 (16.8 vs 17.0 for 2025) | 10-Q Q3 page:4 | 10-Q Q3 page:4 | Small; no explanation found in the Q3 10-Q text |
| Receivables program: the 10-K states a maximum funding commitment of 150.0 through November 5, 2026; the Q3 10-Q states the term was extended to October 23, 2029 but not the commitment after the amendment | 10-K page:93 | 10-Q Q3 page:6, page:22 | Size of the program after the amendment is not supplied |

## Calculations

These are source tie-outs for readiness only (no normalization, no new analytical figures). USD millions.

### Coverage

- Pages retained: 135 + 33 + 34 + 34 + 10 + 11 + 11 = 268 of 268 pages. Two pages are short: 10-K page:135 (37 characters, signature block remainder) and Q2 10-Q page:34 (142 characters). No page was found empty or unreadable. Tables came through as text; no image, chart or scanned content was inspected, and none is claimed.

### Discrete quarters tie to nine months

- Net sales 2026: 479.6 (Q1 10-Q page:2) + 531.8 (Q2 10-Q page:2) + 499.5 (Q3 10-Q page:2) = 1,510.9, equal to nine months (Q3 10-Q page:2).
- Net sales 2025: 484.8 + 525.4 + 513.7 = 1,523.9, equal to nine months 2025 (Q3 10-Q page:2).
- Net loss 2026: (-11.7) + 3.6 + (-1.2) = (-9.3), equal to nine months (Q3 10-Q page:2).
- Adjusted EBITDA 2026 (management): 47.5 (Q1 release page:1) + 75.0 (Q2 release page:1) + 62.3 (Q3 release page:11) = 184.8, equal to nine months (Q3 release page:11).
- Segment net sales Q3 2026: 218.5 (FAM) + 281.0 (SAS) = 499.5 (Q3 10-Q page:22).

### Debt and liquidity tie-outs (September 30, 2026)

- Principal: 20.0 revolver + 89.7 Term Loan A + 498.7 Term Loan B + 400.0 notes + 2.7 other = 1,011.1, equal to the maturity table total (Q3 10-Q page:12, page:14). Less debt issuance costs 34.7 = 976.4, equal to total debt (page:12). Issuance costs are deducted as a separate line in the debt table, so the facility lines are read as principal-like balances (a reading of the table layout, not a stated fact).
- Net debt per release: 976.4 - 97.3 = 879.1, equal to the printed figure (Q3 release page:11). Total liquidity per release: 97.3 + 276.2 = 373.5, equal to the printed figure (Q3 release page:3).
- Revolver availability difference: commitment 305.0 (Q3 10-Q page:13) - borrowings 20.0 (page:12) = 285.0, versus printed undrawn capacity 276.2 (page:28). Difference 8.8, for which no printed item (such as outstanding letters of credit) was found. The same difference appears at June 30, 2026: 305.0 - 17.0 = 288.0 vs 279.2 (Q2 10-Q page:11, page:27) = 8.8, and at March 31, 2026: 600.0 - 175.0 = 425.0 vs 416.2 (Q1 10-Q page:10, page:26) = 8.8. The cause is Not supplied.
- Tornado: expense 42.5 + 1.3 = 43.8; less recoveries received 5.0 and receivable 38.0 = 0.8 net loss, equal to the printed figure (Q3 10-Q page:17, page:18).

### Reported leverage not reproduced

- Management-stated net leverage 3.8x at September 30, 2026 against a current maximum of 5.00x (Q3 10-Q page:28). Not calculable here: the denominator is trailing adjusted EBITDA under the credit agreement definition. The pack has nine-month 2026 adjusted EBITDA of 184.8 and prior-year Q1 through Q3 comparatives, but no fourth quarter 2025 or full-year 2025 adjusted EBITDA (the 10-K contains no adjusted EBITDA; checked by text search of all seven sources) and no credit agreement definition.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreement as amended by the Ninth Amendment (April 3, 2026) not supplied; the Q1 10-Q lists it as Exhibit 10.1 incorporated from a Form 8-K filed April 6, 2026 (Q1 10-Q page:32). Covenant levels are only summarized: minimum interest coverage 2.50x to 3.00x and maximum net debt to EBITDA 5.00x to 4.00x "over time", applying to the Revolving Facility and Term Loan A (Q3 10-Q page:14). Step-down dates, EBITDA definition and baskets are Not supplied; the reported interest coverage ratio is Not supplied | High for covenant work | CP-1, CP-2 | Obtain the amended agreement |
| Indenture for the 8.000% notes due 2029 not supplied; covenants and guarantor terms known only from Note 8 (Q3 10-Q page:12, page:13); notes callable from October 1, 2026 at indenture prices not supplied | Medium | CP-1, CP-1A | Obtain the indenture |
| Receivables purchase agreement and its October 23, 2026 amendment not supplied; commitment after the amendment Not supplied; reverse receivables programs are described in the 10-K only (page:93) | Medium | CP-1, CP-2 | Obtain amendment or 8-K |
| Annual and trailing adjusted EBITDA Not calculable (no fourth quarter 2025 release in the pack; no adjusted EBITDA in the 10-K) | High for leverage | CP-1, CP-2 | Add the fourth quarter 2025 release |
| Letters of credit under the revolver: nothing found by searching "letter of credit", "standby" and "LC" in all sources beyond fee terms in the 10-K (page:99); amount Not supplied | Medium | CP-1 | Obtain the credit agreement or compliance certificate |
| Maturity detail by instrument: the maturity table is by year in total, not by instrument, and conflicts in reading with the Note 8 maturity wording (see conflicts); term loan commitments (89.9, 500.0) differ from the September 30 balances (89.7, 498.7) and the repayment history is not itemized | Medium | CP-1 | Obtain the amended agreement |
| Guarantor and subsidiary list (Exhibit 21.1 listed in the 10-K, page:133) text not supplied; names of subsidiaries added as borrowers or guarantors in April 2026 Not supplied | Medium | CP-1A | Obtain exhibit |
| No ratings, market quotes, presentations or call transcripts; context ratings and quotes blank | Medium for rating views | CP-2 | Add if needed |
| Tornado: business interruption and recoveries above inventory cost are explicitly not recognized (Q3 10-Q page:17); the net insurance outcome is open | Medium | CP-1, CP-2 | Monitor next filing |
| Management claims are unverified against filings: "strongest sales growth ever" for FAM (Q3 release page:1), "record adjusted EBITDA and margins" (Q2 release page:1) and expectation that inventory losses are "fully recoverable" (Q3 release page:1) are attributed claims only | Low | CP-1A, CP-2 | Carry as management language |
| The release states debt matures "on a staggered basis through 2033" (Q3 release page:3); the Term Loan B is seven years from April 3, 2026 (Q3 10-Q page:13); the maturity table prints only through 2030 and "Thereafter" (page:14) | Low | CP-1 | Use the note for years |
| Subsequent events after September 30, 2026 are limited to the October 23, 2026 receivables amendment, the November 4, 2026 sale of a held-for-sale North American facility, and the November 4, 2026 dividend declaration of 0.10 per share payable December 18, 2026 (Q3 10-Q page:22, page:23, page:28); sale proceeds Not supplied | Low | CP-1, CP-1A | None |
| Image, chart and speaker-note content: none exists in the pack; not claimed | Low | CP-1A | None |

Not supplied does not mean zero for any item above.

## Next module

Proceed to CP-1 with all seven issuer sources as active, separate sources and no handoff dependency. Instruct it to: use the Q3 2026 10-Q as the controlling source for September 30, 2026 balances and the 10-K for December 31, 2025 lease detail; show quarter and nine-month figures with their labels; attribute adjusted EBITDA, free cash flow, net debt, total liquidity and 3.8x net leverage to management releases and the 10-Q MD&A; list the covenant levels as summarized in Note 8 and mark step-down dates, reported coverage and letters of credit as Not supplied; carry the 8.8 revolver availability difference as unexplained; and treat the tornado, the receivables amendment and the sale of the held-for-sale facility as subsequent or open events. CP-1A should draw the business and transaction narrative from 10-K Item 1 (starting at page:3) and the 2026 notes, and CP-2 and CP-5 inherit every limitation in this handoff.
