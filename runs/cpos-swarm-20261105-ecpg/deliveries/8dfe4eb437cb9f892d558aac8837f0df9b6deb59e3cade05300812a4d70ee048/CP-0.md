## Request

Issuer: ENCORE CAPITAL GROUP INC (ticker ECPG, issuer id ecpg). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. Current period: q3-2026; prior period: fy-2025 (both from the run context, which is user settings and not issuer evidence).

Question for this module: can the effective source set support the requested downstream work (the financial data extraction, the business and transaction fact pack, the fundamental credit synthesis and the evidence trace review), and what remains blocked? This module gives a source-sufficiency view only. It gives no credit conclusion, legal interpretation or investment opinion, and it normalises, reconciles and calculates no figures. The assertion is SOURCE_SUFFICIENCY_ONLY. The run is not an HTML Model objective, so no model input contract is assessed.

The context names no borrower, parent or guarantor, and holds no deal terms, quotes, ratings or peers. It states that no portfolio workbook, prior case, management bridge or legal documents are attached. A blank context field is read as not supplied, never as zero.

## Sources

### Issuer sources relied on

Hashes are the sha256 values CP-OS pinned for the retained text of each source. Each source is a SEC filing text extraction (retained page spans), so page locators are the retained `page:N` spans, not printed page numbers.

| Source name | sha256 | Document family and authority | Period and basis | Retained spans |
| --- | --- | --- | --- | --- |
| 10-K_2025-12-31_ecpg-20251231.htm.jsonl | 34ff88efcf361fa9aeafcc136a26a65107894a6eccc6d81525528ab9ff5d0d5d | Annual report, Form 10-K, audited filed statements; controlling for FY2025 and year-end 2025 facts | FY2025, fiscal year ended December 31, 2025; consolidated | 128 pages (page:1 to page:128) |
| 10-Q_2026-03-31_ecpg-20260331.htm.jsonl | 78afd13c000763f54a4aba736b73215614c4d9f919d4b8b0b086fe99e4f165ec | Quarterly report, Form 10-Q, unaudited filed statements | Q1 2026, quarter ended March 31, 2026; consolidated | 50 pages |
| 10-Q_2026-06-30_ecpg-20260630.htm.jsonl | b9101ef4153230b6bac0c232b19beeb72b0be52512669a3b5f826ec55ac35d2f | Quarterly report, Form 10-Q, unaudited filed statements | Q2 2026, quarter and six months ended June 30, 2026; consolidated | 58 pages |
| 10-Q_2026-09-30_ecpg-20260930.htm.jsonl | 732e46e0fdf56804d0e4376f251fca05b1fb9b8a2542ea7489a917605ffcd2f2 | Quarterly report, Form 10-Q, unaudited filed statements; latest filed period | Q3 2026, three and nine months ended September 30, 2026; consolidated | 62 pages |
| EX-99.1_2026-05-06_exhibit991ecpgq12026earnin.htm.jsonl | 52e6f2f8497b4c376deb09345bbca84227e91bc87999210c914e4332ca310a30 | Earnings release furnished as Exhibit 99.1; management attributed claims plus reproduced statements and a non-GAAP reconciliation | Q1 2026 | 5 pages |
| EX-99.1_2026-08-05_exhibit991ecpgq22026earnin.htm.jsonl | c912421ecebbdeab115865e4c75e4397e60fc06977b32c09b5fe72e8026c1bc7 | Earnings release furnished as Exhibit 99.1 | Q2 2026 | 7 pages |
| EX-99.1_2026-11-04_exhibit991ecpgq32026earnin.htm.jsonl | 55d38b7d96066eb32a5cc33bf9d08102e9a0e050298f0028532e13cfed8c82ea | Earnings release furnished as Exhibit 99.1 | Q3 2026 | 6 pages |

### Other inputs

| Input | sha256 | Role |
| --- | --- | --- |
| context (1084961-encore-capital-group-inc-ecpg.json) | fb9232dcd1631add7bbcdb6eec1a7bd4a0eec6466deb6a3148ebd7ee287099b7 | User settings for the run; not issuer evidence |

### Handoffs

No upstream handoff was supplied to this module. It is the first module of the run. No handoff is relied on.

### Ignored file

The pack folder also holds a retrieval index file, `_retrieval.json`, which CP-OS ignored. It lists the filing dates and accession numbers of the pack. It is not a retained source here and is not cited as evidence.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The filed annual report, three quarterly reports and three earnings releases give a sound, dated base for the requested analysis, with bounded gaps on covenant headroom, ratings and legal terms. | Medium | No credit agreement, indenture, rating report or market data is supplied, so covenant headroom and market-based views cannot be built from the sources. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The latest quarterly report and its earnings release carry matching statements and a full borrowings note covering the facilities and notes. | Debt, liquidity and interest work can proceed from filed statements. | High |
| Covenant limits are summarised, but the issuer's actual covenant ratios are not reported in the sources. | Headroom against the covenants cannot be measured; only a compliance statement exists. | Medium |
| The capital structure changed materially during 2026 through new notes, redemptions and a convertible settlement funded from the revolver. | Debt figures must be read at the latest balance sheet date, not from the annual report. | High |
| No ratings, market prices, indentures or credit agreement are supplied. | Relative value, legal ranking beyond the notes' summary and market-implied views are not supportable. | High |

### Readiness view

The effective source set is READY_WITH_LIMITATIONS for the requested work. All seven issuer sources are filed SEC text with identifiable issuer, period and basis, the periods tie to the run context (current period Q3 2026, prior period FY2025), and nothing is dated after the 2026-11-05 cutoff. Every requested consumer can run its own method on these sources with bounded gaps. None is CONDITIONAL or BLOCKED, because no missing source prevents any consumer's workflow and no preparation is blocked. Readiness is for source sufficiency only; it does not say that downstream analysis is complete, correct or accepted, and a successful text extraction is not a fidelity review.

### Source-by-source assessment

For every source, the identity, period and perimeter below come from located content, not from the file name. Quotes are exact substrings of the retained spans.

| Source | Identity and period evidence (located) | Perimeter and roles | Limitation |
| --- | --- | --- | --- |
| 10-K FY2025 | page:1 "For the fiscal year ended December 31, 2025"; page:1 "ENCORE CAPITAL GROUP, INC. (Exact name of registrant as specified in its charter)" | Single registrant filing consolidated statements. page:106 "Encore is the parent of the restricted group for the Global Senior Facility and the Senior Secured Notes" | Retained spans end at the goodwill note on page:128; exhibits are referenced but not retained. The 10-K numbers borrowings as Note 6 and goodwill as Note 15, while the 10-Qs use different note numbers. |
| 10-Q Q1 2026 | page:1 "For the quarterly period ended March 31, 2026" | Same registrant, consolidated, unaudited | Q1 is a discrete quarter; it is the only source for first-quarter balance sheet items. |
| 10-Q Q2 2026 | page:1 "For the quarterly period ended June 30, 2026" | Same registrant, consolidated, unaudited | Income statement carries three and six month columns; the six-month column is year to date, not a discrete quarter. |
| 10-Q Q3 2026 | page:1 "For the quarterly period ended September 30, 2026"; page:62 "Date: November 4, 2026" | Same registrant, consolidated, unaudited; page:25 names the Cabot securitisation vehicle as a VIE and page:25 names the U.S. financing subsidiary | Income statement carries three and nine month columns; there is no discrete fourth quarter and no stated last-twelve-months figure. |
| Release Q1 2026 | page:1 "Encore Capital Group Announces First Quarter 2026 Financial Results" | Management release, not a filing; attributed claims only | Superlatives such as record collections are management language and remain attributed. |
| Release Q2 2026 | page:1 "Encore Capital Group Announces Second Quarter 2026 Financial Results" | Management release | The headline attributes a per share refinancing cost effect to management; the filing controls the amount. |
| Release Q3 2026 | page:1 "Encore Capital Group Announces Third Quarter 2026 Financial Results"; page:1 "SAN DIEGO, November 4, 2026" | Management release; carries guidance | Guidance is a management forward-looking claim, not evidence of outcome. |

### Version relationships and conflicts

- The three 10-Qs and the 10-K are separate periodic filings, not amendments of each other. No amendment, restatement, supplement or draft is present among the sources, and none is collapsed. Each retains its own period.
- The year-end 2025 comparative in the Q3 filing agrees with the 10-K for total borrowings: page:19 of the Q3 10-Q "Total $ 4,237,800 $ 4,001,293" and page:105 of the 10-K "Total $ 4,001,293 $ 3,672,762". No conflict was found.
- Release and filing agree on the Q3 headline statement lines read: page:51 of the Q3 10-Q "Adjusted EBITDA $ 245,171 $ 184,756 $ 644,320 $ 489,449" and page:6 of the Q3 release "Adjusted EBITDA $ 245,171 $ 184,756 $ 644,320 $ 489,449". No conflict was found. Where figures differ in future, the filing controls and the release is a supporting claim.
- The 10-K debt table at page:107 lists notes that were later redeemed (page:107 "Encore 2029 Notes 500,000 500,000 USD Apr 1, 2029 Apr 1, Oct 1 9.250 %"). The later filings supersede it for current debt: page:21 of the Q3 10-Q shows that note at nil. Both remain active, period-specific sources.
- No duplicates were found.

### Coverage by profile

Financial reports (10-K and three 10-Qs):

| Needed content | Located in retained spans | Status |
| --- | --- | --- |
| Statements of financial condition, income, cash flows | Q3 10-Q page:2 "Borrowings 4,237,800 4,001,293"; page:3 "Net income $ 124,013 $ 74,660 $ 274,255 $ 180,177"; page:6 "Cash paid for interest $ 183,459 $ 172,756" | Retained |
| Debt by facility and notes, rates, maturities | Q3 10-Q page:21 "Encore 2032 Notes 750,000 — USD Jun 1, 2032 Jun 1, Dec 1 6.625 %"; page:19 "Global senior secured revolving credit facility $ 974,763 $ 631,998" | Retained |
| Facility terms, security, ranking | Q3 10-Q page:20 "The Global Senior Facility is secured by substantially all of the assets of the Company and the guarantors." | Retained; guarantor entity names not located |
| Covenant terms | Q3 10-Q page:20 "A restrictive covenant that requires the Company to maintain a Fixed Charge Coverage Ratio (as defined in the Global Senior Facility) of at least 2.0" | Terms retained; reported ratios not located |
| Liquidity: cash and undrawn capacity | Q3 10-Q page:20 "Available capacity under the Global Senior Facility, after taking into account applicable debt covenants, was approximately $510.2 million as of September" and page:58 "Our cash and cash equivalents as of September 30, 2026, consisted of $54.8 million held by U.S.-based entities and $103.6 million held by foreign entities." | Retained |
| Commitments | Q3 10-Q page:30 "estimated minimum aggregate purchase price of $684.5 million" | Retained |
| Quarter versus year to date | Q3 10-Q page:3 shows three and nine month columns; Q1 and Q2 10-Qs give the earlier quarters | Retained; discrete fourth quarter 2025 and last twelve months are not printed |
| Segment and geography | Q3 10-Q page:30 "The Company has one reportable segment, the debt purchasing and recovery segment." | Retained |
| Business and operating description | 10-K page:4 onward (Item 1 business) and Q3 10-Q page:34 onward (management discussion) | Retained |
| Collections and estimated remaining collections by vintage | Q3 10-Q page:52 "Supplemental Performance Data" | Retained |
| Hedging and derivatives | Q3 10-Q page:14 "In October 2026, the Company entered into new interest rate swap contracts" | Retained; a post-period item inside a note |

Earnings releases:

| Needed content | Located | Status |
| --- | --- | --- |
| Reported and adjusted figures with reconciliation | Q3 release page:5 and page:6 Adjusted EBITDA reconciliation; page:2 "Estimated Remaining Collections (ERC) $ 10,451,677 $ 9,489,772 10%" | Retained |
| Quarter versus year to date | Q3 release page:6 shows three and nine month columns | Retained |
| Guidance | Q3 release page:1 "we are raising our full-year 2026 guidance" | Retained as management claim |
| Attributed narrative | Q3 release page:1 "Global collections up 14% to record $754 million" | Retained, attributed to management |

Legal and financing sources: none supplied as executed documents. The context states legal documents are none. Covenant, collateral and intercreditor facts exist only as the issuer's own summary in the notes. They are filed statements, but they are not the executed agreements. Page:20 of the Q3 10-Q: "Pursuant to the terms of an intercreditor agreement". No clause, definition, basket, schedule or guarantor list is available.

Workbooks, scans, images and decks: none supplied. No presentation was supplied; the pack substitutes earnings releases. The Q3 release page:2 says a slide presentation was used on the call ("conference call and slide presentation today, November 4, 2026"), and its content is not in the sources. This is a parse and coverage gap, not an exclusion.

### Consumer assessments

| Consumer | Status | Basis | Carried limitations |
| --- | --- | --- | --- |
| Financial data extraction (CP-1) | READY_WITH_LIMITATIONS | Statements, debt note, liquidity text, commitments, adjusted EBITDA reconciliation and cash flow lines are all retained for FY2025, Q1, Q2 and Q3 2026 | No covenant ratios reported; no letters of credit figure located; no ratings; no discrete fourth quarter or last twelve months printed; composition of "Other" borrowings not itemised in the notes read; currency conversion rates are period-end rates stated for foreign currency debt |
| Business and transaction fact pack (CP-1A) | READY_WITH_LIMITATIONS | 10-K Item 1 and the quarterly management discussions describe the business, funding, regulation and 2026 refinancing | Ownership and sponsor are not stated in the context; no transaction document; guarantor entities not named; management language must stay attributed |
| Fundamental credit synthesis (CP-2) | READY_WITH_LIMITATIONS | Source evidence is sufficient to support a synthesis once its upstream handoffs exist | Dependent on the two modules above; the dependency planner sequences it, and a missing handoff is not a source condition |
| Evidence trace review (CP-5) | READY_WITH_LIMITATIONS | Filed statements and releases are retained with located page spans for every claim to be traced | Depends on upstream answers; extraction fidelity was not independently reviewed |

### Evidence, risk mechanism and consequence

- Evidence: Q3 10-Q page:24 "On September 24, 2026, the Company settled in full its $230.0 million aggregate principal amount of 2029 Convertible Notes in cash for $367.9 million." Source risk: the capital structure changed materially in the nine months, so the 10-K year-end debt table is stale for current debt. Consequence: debt and liquidity analysis must be read from the Q3 filing, with the 10-K used only for year-end 2025 comparatives.
- Evidence: Q3 10-Q page:58 "Available capacity under our Global Senior Facility, was $510.2 million as of September 30, 2026." against 10-K page:107 "was approximately $814.3 million as of December 31, 2025". Source risk: the capacity figure moves with revolver draws and is covenant-adjusted by the issuer, so it cannot be rebuilt from commitments alone. Consequence: liquidity must use the issuer's stated figure with its stated basis, and the agreement is not available to test it.
- Evidence: Q3 10-Q page:58 "We are in compliance in all material respects with all covenants under our financing arrangements." Source risk: a compliance statement is not a measured ratio. Consequence: covenant headroom is a recorded gap, and no headroom figure is available from the sources.
- Evidence: Q3 release page:1 "Global collections up 14% to record $754 million". Source risk: a superlative from management in a release. Consequence: it stays attributed and must not override filed statements.

## Calculations

None. This module normalises, reconciles and calculates no figures. The only counts are coverage counts: seven issuer sources retained, one context input, no handoffs, and retained page spans of 128, 50, 58, 62, 5, 7 and 6 for the sources in the order of the table above. Those sum to 316 retained page spans: 128 + 50 = 178; 178 + 58 = 236; 236 + 62 = 298; 298 + 5 = 303; 303 + 7 = 310; 310 + 6 = 316. A page-count total does not establish readiness; it is a bounded inventory only.

The figures quoted in the version comparison are copies of printed values shown to test agreement between sources. No derived amounts are produced.

## Gaps

| Gap | Severity | Affected consumers | Remediation | Evidence of search |
| --- | --- | --- | --- | --- |
| Executed credit agreement, indentures, intercreditor agreement and security documents not supplied; covenant definitions, baskets and guarantor lists unavailable. The context states legal documents are none. | Medium | CP-1, CP-1A, CP-2 | Obtain executed documents and amendments as separate active sources | Covenant text appears only as note summaries, for example Q3 10-Q page:20 |
| Issuer-reported covenant ratios (loan to value and fixed charge coverage actual figures) not located; only limits and a material-compliance statement are retained. | Medium | CP-1, CP-2 | Obtain the compliance certificate or the agreement definitions | Searched all seven sources for "Fixed Charge" and "LTV"; only covenant limit text found in the four periodic filings, none in the releases |
| Letters of credit drawn on facilities, if any: no figure located. | Low | CP-1 | Ask for facility utilisation detail | Searched all sources for the words letter and letter of credit; only unrelated uses of "letters" in the 10-K |
| Credit ratings, market prices, quotes, peers and valuation inputs: none supplied; the context holds none. | Medium | CP-2, relative value work outside the requested set | Supply dated agency ratings and market data | Searched all sources for Moody, Fitch and Standard & Poor; the only match is the S&P SmallCap 600 index name, not a rating |
| Presentation content: the slide deck used on the Q3 call is not supplied; releases substitute. | Low | CP-1A | Supply the deck if narrative slides are needed | Q3 release page:2 refers to the presentation |
| No discrete Q4 2025 and no last-twelve-months figure is printed; both must be assembled from FY2025 and year-to-date columns downstream. | Low | CP-1 | Downstream calculation with inputs shown; state the perimeter and period | Statements checked on Q3 10-Q page:3 and 10-K page:86 |
| No dedicated subsequent events note was located in the Q3 10-Q; one post-period item (new swaps in October 2026) appears inside Note 4, and the share count is dated October 28, 2026. | Low | CP-1, CP-1A, CP-5 | Treat as subsequent events with their dates; no filing after 2026-11-04 is supplied | Searched for "subsequent" in the Q3 10-Q; matches are accounting-policy uses |
| Composition of "Other" borrowings and finance lease liabilities is shown as a table line only. | Low | CP-1 | Read the Note 7 narrative downstream; gap stays if not itemised | Q3 10-Q page:19 table line; narrative on pages 20 to 25 does not itemise it |
| Extraction fidelity of the text spans (tables flattened to text, no images or charts) has not been reviewed against rendered documents. Image and chart content, if any, is not inspected. | Low | all | Spot check key tables against the original filings | Retained spans are text only |
| Foreign currency debt (GBP, EUR) is translated by the issuer at period-end rates stated in the notes; reporting currency of the statements is USD but several instruments are not USD. | Low | CP-1 | Keep original currency beside USD and state the rate | Q3 10-Q page:25 "approximately $338.2 million based on an exchange rate of $1.00 to £0.75" |

No source is blocked, stale, draft or unsigned. The Q3 10-Q is signed and dated November 4, 2026 (page:62), before the cutoff. No figure from any source dated after the cutoff was used.

## Next module

Proceed to the financial data extraction module (CP-1), then the business and transaction fact pack (CP-1A), then the fundamental credit synthesis (CP-2), then the evidence trace review (CP-5), as the dependency planner sequences them. Carry these limitations into each: use the Q3 2026 10-Q as the controlling source for current debt and liquidity and the 10-K only for year-end 2025 comparatives; label every figure by period (Q3 2026, nine months 2026, FY2025); keep management release language attributed; record covenant headroom, letters of credit, ratings, guarantor identity and legal terms as Not supplied where the sources do not hold them; and show any last-twelve-months or discrete-quarter figure as a calculation with its inputs. Next evidence action: obtain the executed financing agreements and the compliance certificate.
