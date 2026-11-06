## Request

Issuer: COHERENT CORP. (issuer id cohr; NYSE ticker COHR; Pennsylvania registrant, SEC file number 001-39375). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD; the statements are in thousands of US dollars, the narrative and liquidity tables in millions, and the earnings releases in millions with one decimal. Current period named by the context: q1-2027, which is the fiscal quarter ended 2026-09-30 (Q1 FY2027). Prior period named by the context: fy-2026, the fiscal year ended 2026-06-30 (FY2026). The sources confirm that the fiscal year ends on 30 June (10-K page:1, 10-Q Q1 FY2027 page:1), so the context periods and the filing periods agree.

Question for this module: can the supplied source set support the requested downstream work (CP-1, CP-1A, CP-2, CP-5), and what remains blocked? This module gives no credit conclusion, legal interpretation or investment opinion. It does not normalize, reconcile or calculate figures. Arithmetic below is limited to tie-outs that test source consistency.

The context file holds the run settings and is not issuer evidence. Its deal terms, quotes, ratings, peers, precedents, assumptions and research questions are all empty, it names no borrower, parent, guarantor or sponsor, and it states legal documents as "none". Those blanks are treated as not supplied, never as zero.

## Sources

### Issuer sources relied on

Each file is one JSONL extraction of an SEC filing. The locator `page:N` is the extraction chunk, not the printed page. The sha256 below is the pinned file hash. Each file also prints its own hash for the underlying htm document in its first line; that is a different hash and is not used here.

| Source name | sha256 | Document family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2026-06-30_iivi-20260630.htm.jsonl | e427b31d3ddbac8e2682229c0851cd57a35f7942a911c46bc2f7e184a8d2417f | Audited annual report, Form 10-K, 141 chunks; filed statements control their facts. Auditor report dated 2026-08-14 (page:83) | FY2026, year ended 2026-06-30, with FY2025 and FY2024 comparatives; two reportable segments |
| 10-Q_2025-12-31_iivi-20251231.htm.jsonl | f7c4c25b26330da07c84899cb176e2f656eac9af26c4128e5f71e23f3921c2c5 | Unaudited quarterly report, Form 10-Q, 51 chunks | Q2 FY2026, quarter ended 2025-12-31, and six months |
| 10-Q_2026-03-31_iivi-20260331.htm.jsonl | f448bb1aae6e87add6b50bc7c2c3335a7137b8a9e4f7f09915b24d3212838bb2 | Unaudited quarterly report, Form 10-Q, 52 chunks | Q3 FY2026, quarter ended 2026-03-31, and nine months |
| 10-Q_2026-09-30_iivi-20260930.htm.jsonl | 2522ad33326b2e35e6501525fb87f419508656f6b0de5277f8f2cf521928150e | Unaudited quarterly report, Form 10-Q, 45 chunks; latest filed statements | Q1 FY2027, quarter ended 2026-09-30, three months only |
| EX-99.1_2026-05-06_d57080dex991.htm.jsonl | dd0ab92d28fa855aab2f4b2d6a0ad55f65e0e80e6b5fe9f8c4fcf3b5db2b5776 | Earnings release exhibit, 11 chunks; management attribution, supporting claims only | Q3 FY2026 results |
| EX-99.1_2026-08-12_d128030dex991.htm.jsonl | 2026b9917624616c285039908d8b9c9ea20eabeae7f1857e479c3c647a5b1bab | Earnings release exhibit, 11 chunks; supporting claims only | Q4 FY2026 and full-year FY2026 results |
| EX-99.1_2026-11-04_d176836dex991.htm.jsonl | c65396b97d274ca2df0db447a0ca9d97bbff5b1393199d2c9b3e69ebf1b4d0a2 | Earnings release exhibit, 10 chunks; supporting claims only | Q1 FY2027 results and Q2 FY2027 outlook |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 51ad9088927a94e7d9ee78792ddf70230393bd5579849af5550b3403180d1e22 | Run settings only; not issuer evidence |

### Supplied handoffs

None. This is the first module in the run, so the handoff set is empty.

### Ignored file

_retrieval.json sits in the pack folder and is not a pinned source. It is not relied on.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Filings and releases through the quarter ended 2026-09-30 are enough to build the financial base, debt picture and business context, with bounded limits. Covenant levels appear only in the annual report; no financing documents are supplied. | Medium | No executed financing documents, no reported covenant ratios and no EBITDA figure are in the pack, so covenant headroom cannot be measured from the sources. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt rose to 4,000,598 thousand at 2026-09-30 from 3,222,224 thousand at 2026-06-30, mainly through other credit facilities, now 802,793 thousand, unsecured and held at foreign subsidiaries. | Those lines sit outside the guarantor group, so debt balances and ranking must be set out separately for downstream work. | High |
| Maintenance covenant levels (net leverage 4.25 to 1.00, interest coverage 2.50 to 1.00) are printed only in the annual report, and no ratio is reported. | Headroom is not measurable from the pack; only the stated compliance and the revolver availability can be carried forward. | High |
| Two documents disagree: the latest quarterly report and the annual report give different gains on the Munich sale, and different sizes for the August 2026 facility. | Downstream work must follow the annual report where it conflicts and record the discrepancy as a limitation. | High |
| Restricted cash of 583 million is mostly held by the Silicon Carbide subsidiary for its own use; purchase commitments at 2026-06-30 were 3.4 billion in fiscal 2027. | Restricted cash is not available to the wider group, and purchase commitments are a claim that is not part of reported debt. | Medium |

### Readiness view

The effective source set supports the requested work with limitations. The four requested consumers are all assessed as READY_WITH_LIMITATIONS, none CONDITIONAL and none BLOCKED. The audited annual report, three quarterly reports and three earnings releases cover the periods the context names, in the reporting currency, up to the evidence cutoff, and every source identifies COHERENT CORP. as the registrant or announcing company. The binding limitations are five. First, no credit agreement, amendment or indenture text is in the pack, so covenant definitions, baskets, guarantor lists and security terms rest on filing summaries. Second, covenant levels are printed only in the annual report risk factors, and no source reports a covenant ratio or any EBITDA measure. Third, two cross-document conflicts are unresolved and are logged below. Fourth, the pro forma growth rates in the releases have no definition or reconciliation in the pack. Fifth, no fidelity review of the text extraction has been done, and tables, charts and images were not inspected beyond their text. None of these blocks a consumer from starting, and each carries forward as a stated limit.

### Source-by-source assessment

No source is blocked, draft, unsigned or a duplicate of another. The quarterly statements are unaudited. The filed 10-K and 10-Qs control their own facts. The three releases are management claims that must not override the filings. Chunk coverage was located by section for every source; the sections not listed as supporting an item below (risk factors, human capital, properties, controls, certifications) are retained but were not read for this module.

| Source | What it supports | Limit |
| --- | --- | --- |
| 10-K FY2026 | Business description (page:8 to page:14), covenant levels in risk factors (page:51), liquidity discussion (page:75 to page:78), audited statements (balance sheet page:85, earnings page:86, cash flows page:88 to page:89), debt note (page:104 to page:108), leases (page:108 to page:109), employee benefits (page:109 to page:110), commitments (page:113), segments (page:127), subsequent events (page:134), exhibit list (page:137 to page:140) | Exhibit list names the credit agreement and amendments but the documents are not in the pack; one critical audit matter on goodwill (page:83) |
| 10-Q Q2 FY2026 | Statements (page:3 to page:5), debt (page:10 to page:13), liquidity (page:44 to page:46) | Three months and six months only; superseded by later quarters for balances |
| 10-Q Q3 FY2026 | Statements (page:3 to page:5), debt (page:12 to page:15), Munich sale (page:11), liquidity (page:46 to page:48) | Three and nine months only |
| 10-Q Q1 FY2027 | Statements (page:2 to page:5), assets held for sale (page:9), debt (page:10 to page:14), contingencies (page:18), equity and NVIDIA investment (page:18), noncontrolling interests (page:20), restricted cash (page:29), segment discussion (page:38), liquidity (page:39 to page:41) | Three months only; no subsequent events note; covenant levels not printed |
| EX-99.1 2026-05-06 | Q3 FY2026 highlights and non-GAAP reconciliation | Management claims; pro forma basis undefined |
| EX-99.1 2026-08-12 | Q4 and full-year FY2026 highlights and reconciliation | Management claims; pro forma basis undefined |
| EX-99.1 2026-11-04 | Q1 FY2027 highlights (page:1), outlook (page:2), earnings and balance sheet (page:6), cash flows and segment revenues (page:7), non-GAAP reconciliation (page:8 to page:10) | Management claims; outlook carries no GAAP reconciliation (page:3) |

### Entity and perimeter

The registrant and reporting entity is Coherent Corp. and subsidiaries, consolidated (10-Q Q1 FY2027 page:2). The Senior Credit Facilities borrower is Coherent Corp. (page:11). The 5.000% Senior Notes are guaranteed by each domestic subsidiary that guarantees the Senior Credit Facilities (page:13), and the Senior Credit Facilities are secured on substantially all assets of the borrower and the other guarantors (page:11). The pack does not name those guarantors and has no subsidiaries exhibit text, so the guarantor map is an unresolved gap, not a conclusion. The foreign unsecured credit lines are outside that group: neither the Company nor any other subsidiary is a party to or a guarantor of them (page:14). Silicon Carbide LLC is a subsidiary with outside investors that holds restricted cash for its own use (page:20, page:29); whether it is a guarantor or restricted subsidiary is not stated. The context names no borrower, parent or guarantor.

### Located evidence by topic

| Topic | Source | Locator | Exact quote |
| --- | --- | --- | --- |
| Latest period | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:1 | “For the quarterly period ended September 30, 2026” |
| Annual period | 10-K_2026-06-30_iivi-20260630.htm.jsonl | page:1 | “for the fiscal year ended June 30, 2026” |
| Annual audit opinion | 10-K_2026-06-30_iivi-20260630.htm.jsonl | page:82 | “present fairly, in all material respects, the financial position of the Company at June 30, 2026 and 2025” |
| Annual revenue | 10-K_2026-06-30_iivi-20260630.htm.jsonl | page:86 | “Revenues $ 7,118,181 $ 5,810,115 $ 4,707,688” |
| Quarter revenue | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:3 | “Revenues $ 2,370,324 $ 1,581,378” |
| Total debt | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:10 | “Total debt 4,000,598 3,222,224” |
| Term A facility | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:10 | “Term A Facility, interest at adjusted SOFR, as defined, plus 1.25% $ 1,140,625 $ 1,140,625” |
| Other credit facilities | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:10 | “Other Credit Facilities 802,793 28,004” |
| Senior notes | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:10 | “5.00% Senior Notes 990,000 990,000” |
| Springing maturity | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:12 | “liquidity is less than (x) $250 million plus (y) the aggregate outstanding principal amount of such notes or term B loans, as applicable” |
| Compliance and availability | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:13 | “the Company was in compliance with all covenants under the Senior Credit Facilities. The Company had aggregate availability of $669 million under its Revolving Credit Facility as of September 30, 2026.” |
| Note guarantee | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:13 | “The Senior Notes are guaranteed by each of the Company’s domestic subsidiaries that guarantee its obligations under the Senior Credit Facilities.” |
| Foreign facility not guaranteed | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:14 | “Neither the Company, nor any other of its subsidiaries, is a party to, or a guarantor of, the August 2026 Facility.” |
| Covenant levels | 10-K_2026-06-30_iivi-20260630.htm.jsonl | page:51 | “a maximum total net leverage ratio, as defined in the Credit Agreement, of 4.25 to 1.00 through maturity” |
| Covenant levels | 10-K_2026-06-30_iivi-20260630.htm.jsonl | page:51 | “an interest coverage ratio, as defined in the Credit Agreement, of at least 2.50 to 1.00” |
| Liquidity table | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:41 | “Available borrowing capacity under Revolving Credit Facility 669 664” |
| Restricted cash | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:29 | “total restricted cash was $583 million, which includes $581 million held by Silicon Carbide LLC and restricted for use only by that subsidiary” |
| Noncontrolling holders | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:20 | “Denso and MELCO each own approximately 12.5% of the Class A Common Units of Silicon Carbide.” |
| Purchase commitments | 10-K_2026-06-30_iivi-20260630.htm.jsonl | page:113 | “total future purchase commitments were $3.4 billion in fiscal 2027 and $8.4 billion thereafter” |
| Pension | 10-K_2026-06-30_iivi-20260630.htm.jsonl | page:110 | “The underfunded pension liability was $22 million and $25 million as of June 30, 2026 and 2025, respectively.” |
| Regulatory inquiry | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:18 | “the Company is unable to determine an estimate or range of loss” |
| Equity raise | 10-Q_2026-09-30_iivi-20260930.htm.jsonl | page:18 | “aggregate gross proceeds of $2 billion” |
| Segment revenue | EX-99.1_2026-11-04_d176836dex991.htm.jsonl | page:7 | “Datacenter & Communications $ 1,951.7 $ 1,615.0 $ 1,090.0” |
| Pro forma headline | EX-99.1_2026-11-04_d176836dex991.htm.jsonl | page:1 | “Q1 REVENUE OF $2.37B, INCREASED 50% Y/Y AND 56% Y/Y ON A PRO FORMA BASIS” |
| Outlook | EX-99.1_2026-11-04_d176836dex991.htm.jsonl | page:2 | “Revenue for the second quarter of fiscal 2027 is expected to be between $2.55 billion and $2.75 billion.” |

### Conflicts and anomalies register

| Id | Conflict | Locators | Authority and downstream effect | Severity |
| --- | --- | --- | --- | --- |
| C1 | The Q1 FY2027 10-Q says the Munich sale impairments were “partially offset by a gain of $115 million recorded within Gain on sale of business” in Q3 FY2026. The FY2026 10-K says “offset by a gain of $9 million recorded within Gain on sale of business” for fiscal 2026, and the Q3 FY2026 10-Q reports a Munich gain of $9 million and a Q3 gain line of (8,922) thousand. | 10-Q Q1 FY2027 page:9; 10-K page:103; 10-Q Q3 FY2026 page:11 and page:3 | The audited annual report and the Q3 statements control. The stated loss of $96 million ties to $105 million of impairments less a $9 million gain, not to a $115 million gain. Downstream work must not use the $115 million figure for the Munich sale. | Medium |
| C2 | The 10-K describes the August 2026 facility as “aggregate commitments of approximately $945 million”, with a local currency tranche equivalent to 470 million US dollars, and undrawn at 2026-08-14. The Q1 FY2027 10-Q gives approximately $950 million, a local tranche equivalent to 475 million US dollars, and 598 million outstanding at 2026-09-30. | 10-K page:134 and page:78; 10-Q Q1 FY2027 page:14 | The 10-K gives its figure as based on exchange rates at signing; the 10-Q does not say why its figure differs. Commitment size is therefore a range, and the drawn amount is the 10-Q figure. | Low |
| C3 | The Q1 FY2027 10-Q liquidity discussion says “The cash provided by financing activities during the first quarter of fiscal 2026 was primarily due to $773 million proceeds from borrowings of other credit facilities” while describing the quarter ended 2026-09-30, which is the first quarter of fiscal 2027. The same page also heads its sources and uses table “Year Ended June 30, 2026 2025” above three-month columns. | 10-Q Q1 FY2027 page:40 and page:39 | Period-label slips in the narrative. The statements (page:4) control: proceeds from borrowings of other credit facilities are 773,355 thousand in the three months ended 2026-09-30. Downstream work must label this Q1 FY2027. | Low |

### Consumer readiness

| Consumer | Status | Evidence in place | Carried limitations |
| --- | --- | --- | --- |
| CP-1 financial extraction | READY_WITH_LIMITATIONS | Annual and quarterly statements, debt note, liquidity tables, segment data, cash paid for interest and taxes (10-Q Q1 FY2027 page:4) and releases for non-GAAP bridges | No EBITDA figure or covenant ratio in any source; discrete Q2 FY2026 and Q3 FY2026 earnings amounts are presented as three-month figures, but cash flow statements are year-to-date only, and the Q1 FY2026 quarterly report is not in the pack (the Q1 FY2027 10-Q carries its comparatives); conflicts C1 to C3 |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business and segment description in the annual report, the NVIDIA private placement (10-Q Q1 FY2027 page:18), the aerospace and defense and Munich disposals (page:9), the August 2026 facility (page:14) and noncontrolling interests (page:20) | No sponsor, no transaction agreements, no investor presentation (the 2026-11-04 release says one will be filed, page:3, but it is not in the pack); pro forma basis undefined |
| CP-2 fundamental synthesis | READY_WITH_LIMITATIONS | Same filed evidence as above; reads only upstream handoffs | Quality depends on the upstream handoffs; no ratings, quotes or peers supplied, so no market or agency cross-check |
| CP-5 evidence trace | READY_WITH_LIMITATIONS | All seven sources retained with pinned hashes | Extraction fidelity not reviewed; tables and charts inspected as text only |

## Calculations

These are tie-outs of the sources against themselves. They are not normalized figures and are not for downstream use as results.

| Check | Inputs (thousands of USD, 2026-09-30 unless stated) | Result | Ties to |
| --- | --- | --- | --- |
| Debt table sum | 1,140,625 − 9,513 + 1,080,000 − 19,609 + 802,793 + 6,745 + 13,235 + 990,000 − 3,678 (10-Q Q1 FY2027 page:10) | 4,000,598 | Reported total debt 4,000,598 |
| Debt on balance sheet | 19,887 current portion + 3,980,711 long-term debt (page:2, page:3) | 4,000,598 | Debt table total |
| Other credit facilities | 205 million (2026 lines) + 598 million (August 2026 facility) (page:14) | 803 million | 802,793 thousand in the table, within rounding |
| Cash and restricted cash | 1,552,929 + 44,576 + 538,838 (page:2, page:5) | 2,136,343 | Cash flow statement end balance 2,136,343 |
| Restricted cash split | 581 million Silicon Carbide + 2 million other (page:29) | 583 million | Total restricted cash 583 million; balance sheet 44,576 + 538,838 = 583,414 |
| Revolver availability | 700 million commitments (page:12) − 669 million availability (page:13) | 31 million | Composition of the 31 million (letters of credit or other usage) is not printed; see Gaps |
| Munich loss | 105 million impairments − 9 million gain (10-K page:103) | 96 million | Stated loss of 96 million; a 115 million gain would not tie |
| Segment revenue | 1,951.7 + 418.6 (EX-99.1 2026-11-04 page:7) | 2,370.3 million | Consolidated revenue 2,370.3 million |
| Revenue growth label | 2,370,324 against 1,581,378 (10-Q Q1 FY2027 page:3) is a reported rise of about 50 percent | About 49.9 percent | Release headline “INCREASED 50% Y/Y”; the 56 percent pro forma figure cannot be recomputed |

## Gaps

| Gap | Why it matters | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Credit agreement, Amendments No. 1 to No. 5 and the notes indenture are listed in the exhibit index (10-K page:138) but their text is not in the pack. Not supplied. | Covenant definitions, baskets, guarantor lists, collateral and the springing maturity mechanics rest on filing summaries. | CP-1, CP-1A, CP-2, CP-5 | Add the executed documents or state that summaries are the limit. |
| No reported covenant ratio and no EBITDA measure in any source (search of all seven sources found none). Not calculable from the pack. | Headroom against 4.25 to 1.00 and 2.50 to 1.00 cannot be measured; the covenant definitions are also absent. | CP-1, CP-2 | Downstream work may build an analyst EBITDA from reported lines and label it as not the covenant definition. |
| Covenant levels appear only in the annual report risk factors (page:51); the quarterly reports state compliance only. | Levels are as of the annual report, not re-confirmed after the 2026-09-30 quarter. | CP-1, CP-2 | Carry compliance statements with dates. |
| Letters of credit and other usage of the revolver are not printed; 700 million of commitments less 669 million availability leaves 31 million unexplained. | Liquidity must be built from stated availability, not from commitments less drawings. | CP-1, CP-2 | Use the stated availability and note the gap. |
| Guarantor and restricted subsidiary lists, and the status of Silicon Carbide LLC, are not named. | Structural ranking of foreign unsecured lines and the usability of restricted cash cannot be fully mapped. | CP-1, CP-1A, CP-2 | Carry as unresolved. |
| Pro forma revenue growth (56 percent in Q1 FY2027) has no definition or reconciliation in the pack. | The headline growth cannot be tied to reported revenue. | CP-1A, CP-2 | Use reported growth; treat pro forma as a management claim. |
| Q1 FY2026 quarterly report and the Q2 FY2026 earnings release are not in the pack, and no investor presentation is supplied. | Discrete quarters come from the later reports’ comparatives and the 10-Qs. | CP-1 | Use the Q1 FY2027 10-Q comparatives. |
| No ratings, market quotes, peers or deal terms in the context. Not supplied. | No external cross-check of credit view. | CP-2 | None available from the pack. |
| No fidelity review of the text extraction; tables, charts and images inspected as text only. | A successful extraction is not a fidelity review. | CP-1, CP-5 | Spot-check key figures against the htm source. |
| Conflicts C1 to C3 in the register above. | See register. | CP-1, CP-1A, CP-5 | Follow the controlling source named in the register. |
| BIS inquiry on past sales to Huawei: no estimate or range of loss is given (10-Q Q1 FY2027 page:18). | Contingent claim with no amount. | CP-1A, CP-2 | Carry as an unquantified contingency. |

## Next module

CP-1, financial extraction and calculation, should run next. It should build debt by instrument from the Q1 FY2027 10-Q debt note (page:10 to page:14) and the FY2026 10-K debt note (page:104 to page:108), keep the foreign unsecured lines separate from the guaranteed group, and not use the 115 million Munich gain (C1). It should build liquidity from stated cash and stated revolver availability, carry the restricted cash limit (page:29), and label every figure with its period: Q1 FY2027, FY2026 or a stated trailing period. It should carry the covenant gap and the missing EBITDA figure forward as stated limits.
