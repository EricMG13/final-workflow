## Request

Module: source readiness for Brightstar Lottery PLC (issuer id brsl, NYSE: BRSL), pathway credit snapshot, as-of date 2026-11-05, evidence cutoff 2026-11-05. The context names USD as reporting currency, current period q2-2026 and prior period fy-2025. The selected downstream consumers are the financial data module, the business and transaction module, the fundamental credit synthesis and the evidence trace validator. This module answers only whether the pinned source set can support that work and what stays blocked. It gives no credit view, no legal interpretation and no figure normalisation.

Currency and period check: the filings state "Our Condensed Consolidated Financial Statements are stated in millions of United States (“U.S.”) dollars" (second-quarter 2026 interim report, page:8), so the reporting currency matches the context. The latest period supplied is the quarter and six months ended June 30, 2026, and the prior period is FY2025 (year ended December 31, 2025). Both match the context. Part of the debt is euro-denominated (euro notes and euro term loans), so euro amounts are translated into dollars in the filings and the translation rate is a downstream limitation.

## Sources

### Issuer sources relied on

| Source file (exact name) | sha256 | Document family and authority | Period and date located |
| --- | --- | --- | --- |
| 20-F_2025-12-31_igt-20251231.htm.jsonl | 1c18bf53e9995ce6c2aca12af6c18a64523551fba3492e8f989685fea08386fa | Annual report on Form 20-F with audited consolidated financial statements (Item 18) and PwC audit opinion; original authority for FY2025 facts | Year ended December 31, 2025; signed "Dated: February 24, 2026" (page:133); 191 pages |
| 6-K_2025-09-30_brightstar-9302025xform6k.htm.jsonl | d46e904b239bdfcdf629b7154b5f837586e94b09f3d9adb6cf2a3a22cad2c307 | Form 6-K containing unaudited condensed consolidated financial statements and interim management discussion; original authority for nine-month 2025 facts | Quarter and nine months ended September 30, 2025; signed "Dated: November 4, 2025"; 36 pages |
| 6-K_2026-03-31_brightstar-3312026xform6k.htm.jsonl | bd68ab805934e86ab47882d408ef93ab3b6ce1b76f45e4a9303ec66c324fbd07 | Form 6-K containing unaudited condensed consolidated financial statements and interim management discussion; original authority for first-quarter 2026 facts | Quarter ended March 31, 2026; signed "Dated: May 12, 2026"; 26 pages |
| 6-K_2026-06-30_brightstar-6302026xform6k.htm.jsonl | 59ad2951e3fb4482f8541a5bd23eebbb988b008e57b642801a0675f3dc319de2 | Form 6-K containing unaudited condensed consolidated financial statements and interim management discussion; original authority for second-quarter and six-month 2026 facts | Quarter and six months ended June 30, 2026; signed "Dated: August 4, 2026"; 31 pages |
| 6-K-EX-99.2_2025-12-31_q425earningsslidedeck-fi.htm.jsonl | 52d9fd83276756c04d4933b539c2d599c1b0335f475eb7ae194b8d0285bb64ab | Management earnings presentation (exhibit 99.2); attributed supporting claims, not filed statements | Q4 and full year 2025; filing date not printed in the extracted text; 11 pages of extracted text |
| 6-K-EX-99.2_2026-03-31_q126earningsslidedeckfin.htm.jsonl | 904bf049bdca8cf2ecdea2a5b2e5271032b7a15662b32cecb7e8b6ac25de48c2 | Management earnings presentation (exhibit 99.2); attributed supporting claims | Q1 2026; filing date not printed (a slide cites a share price "on May 11,2026"); 9 pages of extracted text |
| 6-K-EX-99.2_2026-06-30_q226earningsslidedeck-fi.htm.jsonl | 2e4571f9e2637bd424291bf68428c53b010290fd8734caabd6c6df90116096fc | Management earnings presentation (exhibit 99.2); attributed supporting claims | Q2 2026; filing date not printed (a footnote cites "August 3, 2026"); 11 pages of extracted text |

All seven pinned sources are retained and located: 315 of 315 extracted pages were available to the reader (191, 36, 26, 31, 11, 9 and 11 pages). The pack also holds a retrieval index file that CP-OS ignores; it is not evidence. The first line of each extracted file prints a sha256 of the underlying HTML document, which differs from the pinned sha256 of the extracted file; the pinned values above identify the evidence used.

### Run settings (not issuer evidence)

| Item | sha256 |
| --- | --- |
| context (dated user settings and inputs for this run) | 5dec6fdc4bf237796c486a0095b8a59b71b216970050467cf9aed314b06e0f82 |

### Handoffs

No upstream handoff is supplied. This module is the first in the run, so the handoff list is empty.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The 2025 annual report and the interim filings through the second quarter of 2026 are supplied and readable, so the four requested workflows can run with stated limitations. | Medium | Nothing after the August 2026 report is supplied, and covenant levels, guarantor lists and debt documents are absent. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The audited 2025 statements and three interim filings give dollar balance sheets, debt tables, maturities and liquidity. | Debt, cash and liquidity can be taken from filings rather than from management slides. | High |
| Adjusted EBITDA, net debt and net debt leverage appear only in management slide decks, not in the filed statements. | Leverage and coverage views must label those figures as management claims. | Medium |
| Covenant thresholds, guarantor lists, indentures and credit agreements are not supplied; filings name the covenant types only. | Covenant headroom cannot be measured from this pack. | High |
| The newest filing is dated August 4, 2026 and no third-quarter 2026 report or rating report is supplied. | Events and ratings between August and the as-of date are unknown. | Medium |
| The slide decks were read as extracted text only; charts and images were not inspected. | Chart-only content, such as the maturity bars, rests on the filings instead. | Medium |

### Readiness view

The effective source set supports the requested work with limitations, so every selected consumer is assessed as ready with limitations and none as conditional or blocked. The assertion is source sufficiency only. Whether the later modules accept their inputs is not evaluated here. The audited annual report and the three interim reports give the statements, debt note, maturity table, liquidity table and commitments needed for a financial data build. The business and transaction work has the annual report's business description and the interim notes on the sale of the gaming business and the Italian Lotto license. The principal restrictions are the absence of any report after the August 2026 interim filing, the absence of covenant levels and debt documents, and the reliance on slide decks for Adjusted EBITDA and leverage.

### Source-by-source assessment

#### Identity and perimeter

- Issuer and reporting entity: Brightstar Lottery PLC (the "Parent") with its consolidated subsidiaries. The annual report states "In July 2025, the Parent changed its corporate name from International Game Technology PLC to Brightstar Lottery PLC (NYSE: BRSL)" (20-F page:4). The pack file names still carry "igt", which is the earlier name, and identity rests on the text, not the filename.
- Basis: US GAAP, single operating segment. The interim report states "The Company operates and manages its continuing operations business as a single segment" (second-quarter 2026 interim report page:10).
- Perimeter change: the gaming and digital business was sold on July 1, 2025 and is shown as discontinued operations ("On July 1, 2025, the Company completed the sale of the Gaming & Digital business", interim report page:7). Continuing-operations figures for 2025 comparatives therefore exclude that business, and discontinued-operations amounts are separate lines. The annual report, the 2025 nine-month report and the 2026 reports must not be mixed without the discontinued-operations label.
- Non-controlling interests: the Italian Lotto license is held through a consortium that Brightstar leads ("a consortium comprised of Allwyn, Arianna 2001, Novomatic Italia, and led by Brightstar", interim report page:12). The income statement and equity statement show non-controlling interests ("Non-controlling interests 1,173 715", interim report page:4), so consolidated cash, debt and EBITDA include partner interests. The ownership percentage of the consortium is not located in the filing text; the Q1 2026 deck gives "BRSL share €879M or $1.03B" of the final installment (Q1 deck page:6), which is a management claim.
- Debt roles: the annual report's debt note lists issuers as Parent, Brightstar Lottery Holdings B.V. and "Parent/Brightstar Global Solutions Corporation" for the 2033 notes (20-F page:169). The paragraph below the table names the co-issuer "Brightstar Lottery Global Solutions Corporation". These two spellings are a naming conflict inside one source and need one resolution downstream. Term loan borrower: Brightstar Lottery S.p.A. (20-F page:171). Guarantors are described only as "certain of the Parent’s subsidiaries"; no list of named guarantors is in the pack. Restricted and unrestricted group distinctions are not described in the supplied text.

#### Financial statements and notes

- Annual report: audited consolidated balance sheet, operations, comprehensive income, cash flows and equity statements, with PwC opinion on statements and internal control ("In our opinion, the consolidated financial statements referred to above present fairly, in all material respects", 20-F page:134). Debt note 15 is at 20-F pages:168-176, liquidity at pages:56-57, and cash requirements at page:59.
- Interim reports: unaudited, "do not include all of the information and note disclosures required by GAAP for complete financial statements" (interim report page:8). Each has balance sheet, operations, cash flows, equity statement, debt note, interest expense note, commitments and management discussion.
- Debt coverage: the June 30, 2026 debt table lists each note and facility with principal, issuance cost and carrying amount, and a maturity table by currency (interim report page:14: "Total principal amounts 1,500 2,883 4,383"). The December 31, 2025 equivalent is in the annual report (20-F page:168). The March 2026 revolving facility refinancing is described in the interim report at page:15 ("entered into a senior secured multicurrency revolving credit facilities agreement expiring March 2031").
- Liquidity coverage: "Total Liquidity 1,742 3,036" for June 30, 2026 and December 31, 2025 (interim report page:27). The figure is built from revolver availability plus cash.
- Cash-paid interest and tax: "Interest paid 68 89" and "Income taxes paid 16 32" for six months (interim report page:6).
- Commitments: the Italian Lotto installments are in the interim report ("On April 24, 2026, LottoItalia paid the final installment", page:12); unconditional purchase obligations at December 31, 2025 are in the annual report (page:59). Factoring is disclosed in the interim report at page:12. Finance lease right-of-use assets are shown in the other assets note (page:12); operating lease liabilities appear only as a balance sheet line (page:3), and no lease maturity schedule or finance lease liability is located in the interim report text read (searched for "lease liabilit" and "finance lease"). The annual report carries the lease notes (20-F pages:162-166).

#### Earnings presentations

- The three decks contain the Adjusted EBITDA reconciliation, net debt leverage, free cash flow, outlook and same-store sales. Example: "Net debt leverage* 3.24x" appears on the Q2 2026 deck (page:6) and "Adjusted EBITDA 286 274" in its reconciliation (page:10). FY2025 "Adjusted EBITDA 304 290 1,121 1,170" is in the Q4 deck reconciliation (Q4 deck page:8). They are issuer presentations, so they provide attributed supporting claims. The decks themselves say the non-GAAP measures are defined by the company ("other companies may define non-GAAP measures differently", Q2 deck page:3).
- Adjusted EBITDA, net debt and net debt leverage are not in any filed statement in this pack. A search of the annual report and the three interim reports for "Adjusted EBITDA" and "AEBITDA" finds the annual report only in compensation-plan and definition text (20-F pages:5, 73, 74, 75, 184), and finds nothing in the three interim reports. This is a source-quality limit, not a missing document.
- Extraction fidelity: the decks are slide images converted to text. The extraction merges several slides per chunk and loses chart structure; the maturity chart on the Q2 deck (page:6) is a string of numbers without axis labels. No chart or image was inspected, and speaker notes are not claimed. The slide-by-slide coverage cannot be accounted for and is a parse gap. The filed debt tables control instead.

#### Version and conflict observations (preserved, not reconciled)

- Italian Lotto final installment, translated amount: the December 31, 2025 balance sheet shows "Payable to ADM 6 — 1,680" (interim report page:3 shows the 1,680 payable), the Q4 deck says "€1.43B or $1.68B due in Q2’26", the Q1 and Q2 decks say "$1.67B", and the cash flow statement shows "Italian Lotto License payment (1,675)" (interim report page:5). The difference is consistent with euro translation at different dates but the filing does not state it as a reconciliation; downstream modules must use the cash-flow amount for the payment and the balance-sheet amount for the December 2025 liability, each labelled.
- Leverage bases: the Q1 deck states "Q1’26 Net debt leverage* 2.4x; ~3.5x pro forma for final Lotto license payment" while the Q2 deck states 3.24x at Q2 2026. These are different dates and one is pro forma; they are not a restatement.
- Revolving facilities: two facilities due July 2027 were cancelled and replaced in March 2026 (interim report page:15), so the annual report's facility table (20-F page:173) is superseded for revolver terms. Both documents stay active as separate dated sources.
- Liquidity arithmetic: the printed components at June 30, 2026 are 1,185 and 558 against a printed total of 1,742; the page footnote says amounts may not foot due to rounding (interim report page:8).
- Letters of credit: the annual report states "There were no letters of credit outstanding under the Revolving Credit Facilities" at December 31, 2025 (20-F page:176). The June 30, 2026 interim report mentions a letter of credit only for the guarantee of the sold business's lease (page:18); whether any letters of credit sit on the new revolver at June 30, 2026 is not stated in the text read.

#### Consumer assessment

| Consumer | Status | Evidence located | Limitations carried |
| --- | --- | --- | --- |
| Financial data module | READY_WITH_LIMITATIONS | Statements, debt table by instrument, maturity table, liquidity table, interest and tax paid, six-month and quarterly 2026 figures, FY2025 audited figures | Adjusted EBITDA and net debt only in decks; discrete fourth quarter 2025 must be derived from annual less nine months; no third-quarter 2026 report; covenant levels not supplied; period-end euro translation rates not located; deck charts not inspected |
| Business and transaction module | READY_WITH_LIMITATIONS | Annual report business and risk sections, sale of the gaming business, Italian Lotto license award and installments, restructuring programme, shareholder returns | Concession agreement and sale agreements not supplied (the annual report lists the concession as an exhibit incorporated by reference, 20-F page:133); consortium ownership split not located in filing text; contract renewals are described only in decks |
| Fundamental credit synthesis | READY_WITH_LIMITATIONS | Same as the two modules above | Inherits every limitation above; no ratings after December 31, 2025 beyond a statement that margins adjust to "public credit ratings"; no market data in the context |
| Evidence trace validator | READY_WITH_LIMITATIONS | Every source is text-addressable by page chunk | Deck claims must be traced to their slide text, not to charts; the file-name pattern differs from the filing name for the annual report |

None of the consumers is conditional, because no missing source prevents a workflow that needs only public filings. Legal documents are declared "none" in the context.

## Calculations

No new financial calculation is made here, because this module may not normalise or reconcile figures. Four footing checks on printed tables were performed to test extraction fidelity:

| Check | Inputs | Result |
| --- | --- | --- |
| Maturity table total at June 30, 2026 | 0 + 228 + 798 + 978 + 1,025 + 1,354 (interim report page:14) | 4,383, equal to the printed total |
| Euro column of that table | 228 + 798 + 228 + 1,025 + 604 | 2,883, equal to the printed euro total; dollar column 750 + 750 = 1,500; 1,500 + 2,883 = 4,383 |
| Liquidity at December 31, 2025 | 1,590 + 1,446 (interim report page:27) | 3,036, equal to the printed total |
| Liquidity at June 30, 2026 | 1,185 + 558 (interim report page:27) | 1,743 against printed 1,742, a rounding difference of 1 |

Coverage counts: 7 of 7 pinned issuer sources retained; 315 of 315 extracted pages available; 3 of 3 decks extracted as text only.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Not supplied: any filing after the interim report dated August 4, 2026, including a third-quarter 2026 report. The prior-year third-quarter report was dated November 4, 2025, so a third-quarter 2026 report may exist before the cutoff; the pack neither shows nor excludes it | High | Financial data, synthesis, validator | Add the latest 6-K and deck if filed on or before 2026-11-05; otherwise state June 30, 2026 as the latest balance sheet |
| Not supplied: covenant levels. The notes name "a maximum net leverage ratio covenant and a minimum interest coverage ratio covenant" (interim report page:15) but no threshold or step-down, and the covenant EBITDA definition is not given | High | Financial data, synthesis | Obtain the revolving credit agreement and term loan agreements |
| Not supplied: indentures, credit agreements, security and guarantee documents, intercreditor terms, and the list of named guarantors. The annual report says debt instruments are not filed ("none of which relates to indebtedness that exceeds 10% of the consolidated assets", 20-F page:133) | Medium | Financial data, synthesis | Obtain from the issuer or the registry if a structure view is needed |
| Not supplied: credit ratings after December 31, 2025. The annual report gives the ratings at that date (20-F page:168); the context rating list is empty | Medium | Synthesis | Obtain current agency ratings |
| Parse gap: the three decks are text extracts; charts, images and speaker notes are not inspected and slide-level accounting is not possible | Medium | Financial data, validator | Use filed tables for any figure that also appears in a chart |
| Management claims: Adjusted EBITDA, net debt, leverage, free cash flow and outlook are non-GAAP deck figures; no Adjusted EBITDA reconciliation sits in a filed statement | Medium | Financial data, synthesis, validator | Label as management claims and keep the deck page reference |
| Discrete quarters: no fourth-quarter 2025 interim report and no second-quarter 2025 report is in the pack; the fourth quarter is available only from the Q4 deck and as annual less nine months, and 2025 quarterly comparatives sit in the 2026 reports | Low | Financial data | Derive with labels, or add the missing filings |
| Co-issuer naming conflict inside the annual report debt note (see identity section) | Low | Financial data, validator | Resolve downstream using the executed documents when obtained |
| Whether letters of credit reduce the new revolver availability at June 30, 2026 is not stated: a search of the interim report for "letters of credit" and "letter of credit" finds only the guarantee of the sold business's lease (page:18) | Medium | Financial data | Obtain the revolver agreement or the issuer's confirmation of drawn letters of credit |
| Consortium ownership percentages and partner funding terms for the Italian Lotto license are not located in the filing text | Medium | Business and transaction, financial data | Obtain the concession and consortium documents |
| Period-end euro to dollar rates are not located in the interim report text read; the Q2 deck gives only an average rate ("EUR/USD FX daily average 1.16 in Q2’26", Q2 deck page:8) | Low | Financial data | State the rate used for each translated balance, labelled as derived |

## Next module

Proceed to the financial data module (CP-1) with all seven sources. Carry forward these instructions: use the filed statements and debt notes as primary evidence; treat Adjusted EBITDA, net debt and leverage as management claims from the decks with their page locators; keep continuing and discontinued operations apart; label every figure with its period (Q2 2026, six months 2026, FY2025, LTM) and currency; show the euro-denominated share of debt; do not state covenant headroom because thresholds are not supplied; and record that nothing after the August 4, 2026 filing is supplied. CP-1A, the synthesis and the validator follow in the order the dependency planner sets, each inheriting the gaps above.
