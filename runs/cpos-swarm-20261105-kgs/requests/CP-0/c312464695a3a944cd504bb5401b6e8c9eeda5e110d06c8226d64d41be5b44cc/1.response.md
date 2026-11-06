## Request

Module: source readiness for Kodiak Gas Services, Inc. (issuer id kgs, NYSE: KGS), pathway credit_snapshot, as-of date 2026-11-05, evidence cutoff 2026-11-05. The run context names USD as reporting currency, q2-2026 (the three and six months ended June 30, 2026) as the current period and fy-2025 (the year ended December 31, 2025) as the prior period. Requested downstream modules: CP-1, CP-1A, CP-2, CP-5. The context leaves borrower, parent, guarantors, sponsor, quotes, ratings, deal terms, market capitalisation, net debt, peers and research questions blank; blank means not supplied, never zero.

Question answered: can the effective source set support the requested work, and what remains blocked. This handoff gives no credit conclusion, legal interpretation or investment opinion, and it separates source sufficiency from the completion of downstream analysis.

## Sources

### Issuer sources relied on

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_kgs-20251231.htm.jsonl | e6f626e8ec2572cfebf2e718e3182d92317f6b3aa59e3698f1eee834557c8791 |
| 10-Q_2025-09-30_kgs-20250930.htm.jsonl | 6db116b2f7c71c732775eba343378dd9074804cd017a46d662467d5ecc03a35b |
| 10-Q_2026-03-31_kgs-20260331.htm.jsonl | b0c6d87ecc739135889320e66c86ebf276495d3e9a2db77ae4ac15158d5c70bd |
| 10-Q_2026-06-30_kgs-20260630.htm.jsonl | 5759bf9f234dd11e438ac1ffdc287279a37a411d788492589a0ab13b93ffe323 |
| EX-99.1_2026-02-25_kgsq42025earningsrelease.htm.jsonl | ad11af9e19e3a760d7586680bcd6c48b50c7738da5c5d9535e8a17c6b9eb6e1f |
| EX-99.1_2026-05-11_kgsq12026earningsrelease.htm.jsonl | 28d16a69c5b1c7a653a4d372cd4408de628fa59c0bf8c9e28886ae87b3878e62 |
| EX-99.1_2026-08-06_kgsq22026earningsrelease.htm.jsonl | 1fc26851224dc87b9b00439921419ff667a90cf4a5077539afcc9f2e07b9ff72 |

### Run context (settings, not issuer evidence)

| Item | sha256 |
| --- | --- |
| context file 1767042-kodiak-gas-services-inc-kgs.json | 45f2a3562d2dfb1c25d8d6636b278dfe41f8d48fe6d85e1a214b7248a9909e44 |

The pack also holds `_retrieval.json`, which CP-OS ignored; it is not evidence and was not used.

### Upstream handoffs

None supplied. CP-0 is the first module of this run, so no module handoff and no handoff sha256 exists to list.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven supplied filings and earnings releases are sufficient for a bounded credit snapshot of Kodiak as of the 2026-11-05 cutoff, subject to stated limitations. No source is blocked and no downstream workflow is conditional. | Medium | Credit agreement, indentures, guarantor lists, ratings and market data are not supplied. Covenant levels rest on the annual report, and the latest evidence is the June 2026 quarter. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Audited annual statements and three quarterly filings carry the debt, liquidity, cash flow and covenant disclosures needed for extraction. | Facility-level debt, maturities and liquidity can be read from filed notes rather than management claims. | High |
| The April 2026 power acquisition and the segment recast put earlier periods on a different perimeter and segment basis; the purchase price allocation is preliminary. | Trends across the acquisition need care, and acquired-asset values may still change. | Medium |
| Covenant levels are printed only in the annual report and the September 2025 quarterly; the 2026 quarterlies state compliance and an amendment without levels. | Current covenant headroom cannot be tested against current terms from this pack. | Medium |
| Sources differ on the power acquisition price and on what counts as total debt in the September 2025 table. | Analysts must choose and label the basis, because the filings do not reconcile the differences. | Medium |
| No ratings, executed financing documents, guarantor lists, presentations or later-quarter filings are supplied. | Guarantee structure, recovery and market-implied views cannot be assessed from this pack. | Medium |

### Readiness view

The effective source set supports the requested work with bounded limitations. All four requested downstream workflows are assessed READY_WITH_LIMITATIONS; none is CONDITIONAL or BLOCKED, and no source has blocked preparation. The deciding facts are that the audited annual report and three quarterly reports, each identified from its own cover or text rather than its filename, carry the statements, debt note, liquidity discussion and segment disclosures, and that three earnings releases add attributed non-GAAP figures. The limits are real and carry forward: no executed financing documents, no guarantor identities, no ratings, no decks, no filing for the quarter ending September 30, 2026, a preliminary acquisition accounting, and a segment recast that leaves 2025 annual figures on the earlier basis. Readiness here means source sufficiency only; it is not a finding that any downstream analysis is complete or correct, and no extraction fidelity review was performed.

| Consumer | Status | Command sheet |
| --- | --- | --- |
| CP-1 financial data | READY_WITH_LIMITATIONS | RUN |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | RUN |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | RUN |
| CP-5 evidence trace validation | READY_WITH_LIMITATIONS | RUN |

### Source-by-source assessment

Identity, document class and period below come from located text on the cited pages, not from filenames. All sources are filings or furnished releases by the registrant itself (the periodic filings show Commission file number 001-41732), in text extraction only. Source quality (original authority) and extraction status are separate: every source extracted to text, and none has had a fidelity review against the original document.

| Source | Document family and authority | Entity and perimeter | Period and basis | Located evidence (page:N) |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31 | Annual report filed by the registrant; audited statements control their facts | Kodiak Gas Services, Inc. consolidated, which operates through Kodiak Gas Services, LLC (Kodiak Services), a variable interest entity | Year ended December 31, 2025 with 2024 and 2023 comparatives; USD thousands; signed February 26, 2026 | page:1 cover ("For the fiscal year ended December 31, 2025"); page:97 audit opinion ("the consolidated financial statements present fairly, in all material respects, the financial position of the Company at December 31, 2025 and 2024"); page:99 balance sheet and operations; page:101-102 equity and cash flows; page:119-125 debt note; page:71-72 liquidity and covenants; page:137 segments; page:139 subsequent events |
| 10-Q_2025-09-30 | Quarterly report; unaudited | Same consolidated perimeter | Quarter and nine months ended September 30, 2025; USD thousands | page:1 cover ("For the quarterly period ended September 30, 2025"); page:6 balance sheet; page:9 cash flows; page:16-17 debt note; page:33 segments; page:53 indebtedness; page:58 adjusted EBITDA reconciliation |
| 10-Q_2026-03-31 | Quarterly report; unaudited | Same consolidated perimeter; first quarter before the power acquisition closed | Quarter ended March 31, 2026; USD thousands | page:5-8 statements; page:11 debt note; page:22-23 segments; page:24 subsequent events (power acquisition); page:36 indebtedness; page:43 adjusted EBITDA reconciliation |
| 10-Q_2026-06-30 | Quarterly report; unaudited; latest periodic filing in the pack | Same consolidated perimeter, now including the acquired power business from April 1, 2026 | Quarter and six months ended June 30, 2026; USD thousands; cover share count as of August 3, 2026 | page:1 cover; page:6-10 statements; page:12-15 acquisition and pro forma; page:19-24 debt note; page:29-31 commitments and contingencies; page:33-35 segments; page:36-59 MD&A; page:56 adjusted EBITDA reconciliation |
| EX-99.1_2026-02-25 (fourth quarter 2025 release) | Press release furnished by the issuer; management attributed, non-GAAP measures | Same consolidated perimeter | Fourth quarter and year 2025, plus 2026 guidance that excludes the pending acquisition; USD thousands in tables | page:3 summary table; page:4-5 guidance; page:13 adjusted EBITDA reconciliation; page:14 cash flow reconciliation |
| EX-99.1_2026-05-11 (first quarter 2026 release) | Press release; management attributed | Same consolidated perimeter | Quarter ended March 31, 2026; two-segment naming still in use | page:4 summary; page:11 balance sheet; page:12 reconciliation |
| EX-99.1_2026-08-06 (second quarter 2026 release) | Press release; management attributed | Same consolidated perimeter including the power business | Quarter ended June 30, 2026 with March 2026 and June 2025 comparatives; revised 2026 guidance | page:5-6 summary and liquidity; page:7 operating data; page:2 and page:7-8 guidance; page:13-15 balance sheet, cash flows and segment reconciliations |

Document-family notes: no base agreement, amendment, waiver or supplement is supplied as its own document. The ABL credit agreement, its Fifth Amendment of April 2, 2026, and the indentures appear only as described inside the filings and as exhibit list entries (10-K page:91). They are therefore descriptions, not executed sources, and none was collapsed into another.

### Coverage map

| Coverage unit | Status | Evidence |
| --- | --- | --- |
| Consolidated balance sheets, statements of operations and cash flows, annual | Retained | 10-K page:99, page:101-102 |
| Same statements, interim (September 2025, March 2026, June 2026 quarters) | Retained | 10-Q 2025-09-30 page:6-9; 10-Q 2026-03-31 page:5-8; 10-Q 2026-06-30 page:6-10 |
| Debt and credit facilities, instrument level, with maturities | Retained | 10-K page:119-125; 10-Q 2026-06-30 page:19-24 ("Total debt outstanding 2,780,917 2,614,647" at page:20) |
| Liquidity and ABL availability | Retained | 10-Q 2026-06-30 page:21, page:48; release 2026-08-06 page:5 |
| Cash paid for interest and taxes | Retained | 10-K page:102 ("Cash paid for interest $ 168,716 $ 147,144 $ 216,648"); 10-Q 2026-06-30 page:9 ("Cash paid for interest $ 103,535 $ 87,075") |
| Adjusted EBITDA, discretionary cash flow, free cash flow and their reconciliations | Retained as attributed non-GAAP | 10-Q 2026-06-30 page:56-58; releases as listed above |
| Segment and KPI tables (horsepower, megawatts, utilisation, adjusted gross margin) | Retained, with basis change | 10-Q 2026-06-30 page:34, page:38; 10-K page:137 |
| Leases, commitments, contingencies, subsequent events | Retained | 10-Q 2026-06-30 page:29-32, page:35; 10-K page:139 |
| Business description, risk factors, governance | Retained as extracted text; located but not read for credit facts beyond the locators above | 10-K page:10-55 |
| Executed financing documents (credit agreement, amendments, indentures, guarantee schedules) | Explicit gap | See Gaps G1 to G3 |
| Presentations, charts, images, speaker notes | Explicit gap: no deck supplied and no image content inspected from text extraction | See Gaps G8 |
| Quarter ended September 30, 2026 filing or release | Explicit gap | See Gaps G5 |

All pages of all seven sources are retained as extracted text (139, 67, 51, 66, 14, 13 and 16 pages respectively, in the order of the source table). No page is claimed as inspected beyond those cited; unread pages are retained, not excluded. Filing tables were spot-checked for continuity across page breaks on the pages cited.

### Entity and instrument roles

| Role | What the sources state | Locator |
| --- | --- | --- |
| Registrant and public equity issuer | Kodiak Gas Services, Inc., Delaware; common stock listed as KGS | 10-Q 2026-06-30 page:1 |
| Operating subsidiary and note issuer | Kodiak Gas Services, LLC ("Kodiak Services"); the registrant is its primary beneficiary and Kodiak Services is a variable interest entity; the senior notes were issued by Kodiak Services | 10-Q 2026-06-30 page:11, page:22-23 |
| ABL parties | Kodiak and Kodiak Services entered into the Fifth Amendment; JPMorgan Chase Bank, N.A. is administrative agent | 10-Q 2026-06-30 page:21 |
| Guarantors | Described only as "the guarantors party thereto" in the exhibit list; no named list located | 10-K page:91 |
| Noncontrolling and preferred holders | Preferred shares paired with OpCo Units, accounted for as noncontrolling interests in Kodiak Services | 10-Q 2026-06-30 page:26 |
| Acquired business | Distributed Power Solutions, LLC, acquired by Kodiak Services on April 1, 2026 and rebranded Kodiak Power Solutions | 10-Q 2026-06-30 page:12 |
| Former sponsor-affiliated holder | An affiliate of EQT AB described as "a then stockholder of the Company" in the 2025 repurchase; current ownership not stated | 10-K page:139 |

Restricted versus unrestricted subsidiary status, and which entities guarantee which instrument, are unresolved and carried as gaps. The note indentures are stated to limit "forming unrestricted subsidiaries" (10-Q 2026-06-30 page:24) but no designation is shown.

### Currency, units, periods and version relationships

- Currency and unit: all filed statements are in USD thousands, matching the context's reporting currency of USD. Earnings releases use USD thousands in tables and USD millions or billions in prose. No other currency was located.
- Periods: the context's current period (three and six months ended June 30, 2026) and prior period (year ended December 31, 2025) are both covered by filed statements. Discrete quarters for third quarter 2025, fourth quarter 2025 and first quarter 2026 are available as reported columns in filings or releases; the fourth quarter 2025 three-month figures exist only in the release (unaudited, furnished), because the annual report presents the full year.
- Version relationships: the annual report, three quarterly reports and three releases are distinct dated documents, none an amendment of another. No draft or unsigned material was found. Restated or recast comparatives are described in Differences between sources below.

### Differences between sources

Each difference is logged with both locators. None is reconciled, averaged or resolved here, and filed statements outrank release narrative where they differ.

| Id | Topic | Source A | Source B | Downstream effect |
| --- | --- | --- | --- | --- |
| D1 | Power acquisition consideration | 10-K page:139: "equity and cash transaction valued at approximately $675.0 million"; the fourth quarter release page:3 says the same | 10-Q 2026-06-30 page:12: "The total consideration consisted of $587.3 million of cash"; the allocation table shows "Fair value of consideration transferred $ 726,354" with shares valued at $139.0 million | The announced value and the closing fair value rest on different share prices and cash adjustments that the pack states but does not bridge; CP-1 and CP-1A must cite the closing figure for the transaction and label the announced figure as signing-date |
| D2 | What "total debt outstanding" contains | 10-Q 2025-09-30 page:16: premium lines ("2033 Senior Notes - debt premium 3,400") sit inside the table above "Total debt outstanding 2,675,765" | 10-K page:119 and 10-Q 2026-06-30 page:20 show "Add: unamortized debt premiums" below "Total debt outstanding" | The September 2025 total is not on the same basis as December 2025 and 2026 totals; CP-1 must restate to a common principal basis from the printed lines and say so |
| D3 | Debt maturity totals | 10-Q 2026-06-30 page:20: "Total debt outstanding 2,780,917" with other borrowings shown on a separate line | 10-Q 2026-06-30 page:24 maturity table total "$ 2,785,200" | The filing does not state the bridge between the two totals; CP-1 must pick one, name it and not mix them |
| D4 | ABL maturity wording | 10-K page:72: maturity extended "from March 2028 to September 2030" | 10-K page:121 adds "or November 16, 2028 if aggregate principal amount of the 2029 Senior Notes outstanding on such date exceeds $200.0 million" | The 2029 notes were redeemed in April 2026 (10-Q 2026-06-30 page:21-22), and the latest quarterly states only the 2030 date; the springing test may no longer apply on those facts, but the pack does not say so |
| D5 | Power segment capital spending | 10-Q 2026-06-30 page:34: Power Infrastructure "Capital expenditures" of 118,012 for the quarter | 10-Q 2026-06-30 page:58: Power Infrastructure growth capital expenditures of (134,371) for the quarter | Different measures (segment capital expenditures versus growth capital expenditures including accrual changes); the filing does not bridge them, so neither can be substituted for the other |
| D6 | Segment presentation | 10-Q 2026-03-31 page:22 and release 2026-05-11 page:4 use Contract Services and Other Services | 10-Q 2026-06-30 page:33-34 recasts to three segments and states an $18.0 million power investment "was included within Compression Infrastructure in our first quarter 2026 presentation" | First quarter 2026 and earlier segment figures are on the older basis unless the June 2026 recast comparatives are used; the 10-K annual segment tables are not recast |

### Credit-relevant observations on source limits

Evidence, then source-risk mechanism, then downstream consequence, for the items that bind most.

- Leverage and covenant evidence. The annual report prints the ABL tests ("The maximum Leverage Ratio is 5.25 to 1.00", a secured leverage maximum of 3.25 to 1.00 and "a minimum interest coverage ratio of 2.5x", 10-K page:72). The 2026 quarterlies state "we were in compliance with all covenants under the ABL Facility" (10-Q 2026-06-30 page:21) and that the Fifth Amendment "modifies the calculation of the leverage ratio" through June 30, 2026, but do not restate levels or the amended definition. Mechanism: the covenant EBITDA and Total Indebtedness are "each as defined in the ABL Credit Agreement", which is not supplied, and management's ratios in the releases (for example "credit agreement leverage ratio was 3.2x for the second quarter of 2026", release 2026-08-06 page:5) are attributed claims. Consequence: CP-1 can report the printed tests and management ratios as separately labelled claims but cannot recompute covenant headroom or confirm terms after June 30, 2026.
- Perimeter change. The June 2026 quarter is the first to include the acquired power business, whose purchase accounting "remains preliminary" (10-Q 2026-06-30 page:13); the first quarter filing states valuations were incomplete (10-Q 2026-03-31 page:24). Mechanism: goodwill, intangibles and the opening balance sheet can still change within the measurement period, and pre-April periods contain no power results. Consequence: CP-1 and CP-2 must not present year-over-year growth or leverage across the April 2026 boundary as like-for-like; the pro forma table (10-Q 2026-06-30 page:15) is the only filed bridge and is not a forecast.
- Capital structure change within the period. Notes due 2029 were replaced by notes due 2031 in March and April 2026 with a defeasance and a loss on extinguishment (10-Q 2026-06-30 page:21-22), and an equity offering closed in May 2026 with "aggregate net proceeds of approximately $836.1 million" (page:26). Mechanism: the December 2025 debt table and the June 2026 debt table list different instruments. Consequence: CP-1 must extract facility-level debt at each balance-sheet date separately and carry the refinancing as a flow, not as a restatement.
- Off-debt claims. Purchase commitments are stated as "$2.5 billion, of which $587.9 million is expected to be settled within the next twelve months" (page:29), lease payments and a regulatory matter are disclosed (page:30, page:32). Mechanism: these sit outside the debt table, and the filing gives no estimate of penalties for the regulatory matter. Consequence: CP-1 and CP-2 must show them as separate claims, with the regulatory matter flagged as an unquantified contingency.
- Authority split. Filed statements and notes control financial facts; the releases supply non-GAAP measures, guidance and narrative such as "Record Compression Infrastructure segment revenues". Consequence: management characterisations may be carried only as attributed claims, and a release figure that differs from a filing yields to the filing.

### Consumer assessment

| Consumer | Status | Usable coverage | Limitations carried forward | Missing source (if any) | Command sheet |
| --- | --- | --- | --- | --- | --- |
| CP-1 financial data | READY_WITH_LIMITATIONS | Annual and interim statements, instrument-level debt and maturities, cash paid for interest and taxes, segment and KPI tables, non-GAAP reconciliations, 2026 guidance | D1 to D6; no recast three-segment annual table; fourth quarter 2025 discrete figures only from a release; no covenant definitions; no filing after June 30, 2026 | None that prevents the method | RUN |
| CP-1A business and transaction | READY_WITH_LIMITATIONS | Business description and risk factors (10-K page:10-55), power acquisition terms and preliminary allocation (10-Q 2026-06-30 page:12-15), refinancing, equity offering, guidance, turbine supply commentary in the second quarter release | Current sponsor and holder structure not stated; governance detail incorporated by reference to a proxy statement not supplied; D1 | None that prevents the method | RUN |
| CP-2 fundamental credit synthesis | READY_WITH_LIMITATIONS | Draws only on the settled outputs of the two modules above | Inherits every limitation above; no ratings, peers or market values supplied (context blank) | None; dependency order handled by CP-OS | RUN |
| CP-5 evidence trace validation | READY_WITH_LIMITATIONS | All seven sources are pinned and locatable by page | Inherits every limitation above; cannot test claims about documents that are not supplied | None; dependency order handled by CP-OS | RUN |

## Calculations

None. CP-0 performs no normalisation, reconciliation or arithmetic. Every figure above is copied as printed in the cited source and page, in USD thousands where a table is cited. Unknown values stay unknown and no blank context value was treated as zero.

## Gaps

| Id | Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- | --- |
| G1 | The ABL credit agreement, the Fifth Amendment (April 2, 2026) and prior amendments are not supplied; only filing descriptions exist. Covenant EBITDA, Total Indebtedness, baskets and borrowing base terms are therefore unavailable (10-K page:72 "each as defined in the ABL Credit Agreement") | High | CP-1, CP-2, CP-5 | Add the credit agreement and amendments from the exhibit index |
| G2 | Covenant levels are printed only in the annual report (10-K page:72) and the September 2025 quarterly (page:17); the 2026 quarterlies give no levels, and the amended leverage calculation applies "Through June 30, 2026" (10-Q 2026-06-30 page:21) | High | CP-1, CP-2, CP-5 | Add the amendment and the next compliance disclosure |
| G3 | Indentures are listed as exhibits (10-K page:91) but not supplied; guarantor identities, whether Kodiak Gas Services, Inc. guarantees the notes, and restricted-subsidiary definitions are not stated in the located text | Medium | CP-1, CP-1A, CP-2 | Add the indentures, supplemental indentures and any guarantor schedule, including any for the notes issued in March 2026 |
| G4 | No credit ratings are supplied. The only rating references are the indenture suspension of covenants on "investment grade ratings from any two of Moody" and the other agencies (10-Q 2026-06-30 page:24) | Medium | CP-2 | Add agency reports if a ratings view is wanted |
| G5 | No filing or release for the quarter ended September 30, 2026. The latest dated items are the August 6, 2026 release and the 10-Q for June 30, 2026; whether later documents existed before the cutoff is not evidenced by the pack | Medium | CP-1, CP-2 | Check for and add any later periodic filing or release dated on or before 2026-11-05 |
| G6 | Power acquisition accounting is preliminary (10-Q 2026-06-30 page:13); the current report on Form 8-K of April 1, 2026 cited at page:38 and any standalone statements of the acquired business are not supplied; pro forma figures are presented only in one table (page:15) | Medium | CP-1, CP-1A | Add the 8-K and any acquired-business statements |
| G7 | Segment recast: annual 2025 and 2024 segment tables use Contract Services and Other Services (10-K page:99, page:137); no recast three-segment annual table is supplied, and third and fourth quarter 2025 segment figures are on the older basis | Medium | CP-1 | Use the June 2026 recast comparatives where available and label the basis; add a recast annual table if it exists |
| G8 | No quarterly presentation, deck, chart or image content is supplied or inspected; speaker notes are not available | Low | CP-1A | Add the decks if narrative slides are needed |
| G9 | Ownership and governance: the proxy statement is not supplied (annual report Part III is incorporated by reference, page:90); the context sponsor field is blank; current holdings of the former sponsor affiliate are not stated | Low | CP-1A | Add the proxy statement and any beneficial ownership table |
| G10 | The sanctions-related payments matter (10-Q 2026-06-30 page:30) states that the aggregate payments "was not material" but gives no estimate of penalties; the outcome with the authorities is open | Medium | CP-1A, CP-2 | Monitor later filings; treat as an unquantified contingency |
| G11 | The fourth quarter 2025 discrete quarter appears only in an earnings release (unaudited, furnished); management ratios such as the credit agreement leverage ratio appear only in releases | Low | CP-1, CP-5 | Label as attributed claims; no remediation possible from the pack |
| G12 | Market data, peers, quotes and deal terms in the context are blank | Low | CP-2 | Supply them if relative value or market-implied views are wanted; they are outside this snapshot's requested modules |
| G13 | No extraction fidelity review of any source was performed; the cited pages were opened and read, but sources were not compared with the original filings | Low | All | Spot-check key figures against the filed originals |

## Next module

Proceed to CP-1 (status READY_WITH_LIMITATIONS, command RUN). CP-1 should open the following and cite them by page: the annual statements and debt note (10-K page:99, page:101-102, page:119-125), the June 2026 quarterly statements, debt note, segments and reconciliations (10-Q 2026-06-30 page:6-10, page:19-24, page:33-35, page:56-58), and the March 2026 and September 2025 quarterlies for discrete quarters. It must carry forward differences D1 to D6 and gaps G1, G2, G6, G7 and G11. It should show the covenant tests and management leverage ratios as separately labelled items, never recompute covenant headroom from an undefined EBITDA, state the perimeter change at April 1, 2026, and keep the debt basis consistent across balance-sheet dates. CP-1A, CP-2 and CP-5 follow in the order CP-OS sets, each carrying the limitations above.
