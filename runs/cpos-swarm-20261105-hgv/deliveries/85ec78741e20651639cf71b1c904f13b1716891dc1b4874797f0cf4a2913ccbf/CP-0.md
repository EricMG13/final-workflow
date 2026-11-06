## Request

Module: source readiness for Hilton Grand Vacations Inc. (ticker HGV, Commission file number 001-37794), as of 2026-11-05, evidence cutoff 2026-11-05. Pathway: credit snapshot. Reporting currency: USD, in millions unless a source states otherwise (context file). Current period: Q3 2026 (quarter and nine months ended September 30, 2026); prior period: FY2025 (year ended December 31, 2025).

Question answered: can the supplied source set support the selected downstream work (CP-1 financial and debt extraction, CP-1A business and transaction context, CP-2 credit synthesis, CP-5 evidence trace review), and what remains blocked? This module gives no credit conclusion, no legal interpretation and no investment opinion, and it calculates nothing; it distinguishes source sufficiency from completion of downstream analysis. The assertion is SOURCE_SUFFICIENCY_ONLY; CP_MODEL_INPUT_CONTRACT_NOT_EVALUATED.

The run context is a settings file, not issuer evidence. It leaves blank: borrower name, parent name, guarantors, ratings, quotes, deal terms, peers, market capitalisation and all assumptions. Blank is not zero and none of it is used as a fact here.

## Sources

### Issuer sources relied on

Each file below is a text extraction (one record per page chunk) of an SEC filing. The sha256 is the pinned hash of the supplied file. Each file also prints its own embedded hash of the original HTML on its first line; those embedded hashes are a different object and are not used as the pin.

| Source (exact name) | sha256 | Family and authority | Period and basis |
| --- | --- | --- | --- |
| 10-K_2025-12-31_hgv-20251231.htm.jsonl | 17ffd5299d1ce58eaab3023314cb336b0628a563fbd9844c59917a6e453a02cf | Annual report on Form 10-K, filed financial statements with audit report; controlling source for FY2025 facts | FY2025 year ended December 31, 2025, with December 31, 2024 comparatives, consolidated, US GAAP, USD millions |
| 10-Q_2026-03-31_hgv-20260331.htm.jsonl | 8a81895fada4586d8ccd4cb859be2d1886b42ac41a8aafdb19a05d432443584d | Quarterly report on Form 10-Q, unaudited; controlling source for Q1 2026 | Quarter ended March 31, 2026, consolidated |
| 10-Q_2026-06-30_hgv-20260630.htm.jsonl | a81efeb9cd748af0032df304e54e9f41941d57f53ef97a5d684972a6e7db8177 | Quarterly report on Form 10-Q, unaudited; controlling source for Q2 2026 | Quarter and six months ended June 30, 2026, consolidated |
| 10-Q_2026-09-30_hgv-20260930.htm.jsonl | c993d04f6645ba40daf4556f4dc20114eff181da866b29f116f9cba49f88abad | Quarterly report on Form 10-Q, unaudited; controlling source for Q3 2026 and the latest balance sheet | Quarter and nine months ended September 30, 2026, consolidated |
| EX-99.1_2026-04-30_hgvq12026earningsreleaseex.htm.jsonl | 92e4f803974e8b1d1fb782b7fa4c071295d1bcd965fc060f8d1edf8b3dca9f05 | Earnings release (Exhibit 99.1), management-attributed, non-GAAP measures; supporting claims only | Q1 2026 |
| EX-99.1_2026-07-30_hgvq22026earningsreleaseex.htm.jsonl | 5535f4d3e680b0dd2b2a79102a2a9c458f84caa70b4ad3b4d26b8a0600e150b0 | Earnings release (Exhibit 99.1), management-attributed; supporting claims only | Q2 2026 |
| EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl | 53988e1805605a66d65d0b02e89b98e726349e8a8a53c9499714f31b0854d4d4 | Earnings release (Exhibit 99.1), management-attributed; supporting claims only | Q3 2026 |

### Run context

| Source (exact name) | sha256 | Role |
| --- | --- | --- |
| context (1674168-hilton-grand-vacations-inc-hgv.json) | 6edd9e91feb582497e031062a9d2821be0472a4f8a6020100729ec6b65f6bb35 | Dated user settings; not issuer evidence |

### Handoffs supplied

None. CP-0 is the first module; no upstream handoff exists.

### Not supplied (not part of the pack)

The retrieval record lists no investor presentations; the three earnings releases stand in for them. Credit agreements, indentures and amendments are listed only in the 10-K exhibit index and are not in the pack.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The seven filings cover the latest annual report, three quarters and three earnings releases, and are enough for debt, liquidity and business extraction at the consolidated level. Covenant terms are not in the pack. | Medium | Credit agreement and indenture terms, and the net leverage definition, are not supplied, so covenant headroom cannot be tested. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Corporate debt and non-recourse securitisation debt are reported separately in one consolidated filing, with a maturity table and weighted-average rates. | Allows corporate and non-recourse claims to be separated downstream; only consolidated figures exist. | High |
| Covenant compliance is stated only as a general sentence; test levels, definitions and headroom are absent. | Covenant headroom cannot be assessed from this pack. | High |
| Third quarter results include a large construction recognition and a change in the receivables allowance method. | Reported earnings are not comparable with earlier quarters without adjustment; the releases disclose both effects. | Medium |
| The Elara acquisition accounting is preliminary and its price differs between the first and third quarter filings. | Later figures supersede the first quarter figure; acquired balances may still change. | Medium |

### Readiness view

The effective source set is sufficient for source-level work on a consolidated, USD, US GAAP basis for the Q3 2026 and FY2025 periods named in the context. Every module in scope can proceed: the filings contain the statements, the debt note, a maturity table, a liquidity discussion, segment tables, commitments and a business description. The binding limitations are (a) no executed financing documents, so covenant levels, definitions, guarantor identities and lien packages cannot be read from primary legal text; (b) the leverage ratio quoted in the releases is a management figure with no definition in the pack; (c) the third quarter contains a one-time construction recognition and an estimate change that the downstream modules must carry; and (d) the Elara purchase accounting is preliminary. No source is blocked, and none is used as a fallback for another. This view concerns source sufficiency only and says nothing about the quality of downstream analysis.

### Source-by-source assessment

| Source | Located evidence of identity and period | Locator | Quote |
| --- | --- | --- | --- |
| 10-K | Registrant, fiscal year | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:1` | "For the fiscal year ended December 31, 2025" |
| 10-K | Consolidated balance sheet, FY2025 and FY2024 | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:112` | "CONSOLIDATED BALANCE SHEETS (in millions, except share and per share data)" |
| Q1 10-Q | Quarter period | `10-Q_2026-03-31_hgv-20260331.htm.jsonl page:1` | "For the quarterly period ended March 31, 2026" |
| Q2 10-Q | Quarter period | `10-Q_2026-06-30_hgv-20260630.htm.jsonl page:1` | "For the quarterly period ended June 30, 2026" |
| Q3 10-Q | Registrant, quarter period | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:1` | "For the quarterly period ended September 30, 2026" |
| Q3 10-Q | Registrant name | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:1` | "Hilton Grand Vacations Inc. (Exact Name of Registrant as Specified in Its Charter)" |
| Q3 10-Q | Unaudited condensed consolidated statements | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "CONDENSED CONSOLIDATED BALANCE SHEETS (in millions, except share and per share data)" |
| Q3 release | Release date and quarter | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:2` | "Hilton Grand Vacations Reports Third Quarter 2026 Results" |
| Q2 release | Release quarter | `EX-99.1_2026-07-30_hgvq22026earningsreleaseex.htm.jsonl page:1` | "Hilton Grand Vacations Reports Second Quarter 2026 Results" |
| Q1 release | Release quarter | `EX-99.1_2026-04-30_hgvq12026earningsreleaseex.htm.jsonl page:1` | "Hilton Grand Vacations Reports First Quarter 2026 Results" |

Document families and authority. The 10-K and the three 10-Qs are filed statements and control their respective facts. The three releases are management communications that present non-GAAP measures and cannot override a filing. The releases and 10-Qs agree on the third quarter facts checked here (cash, revolver capacity, revenue), so no filing-versus-release conflict was found in the items read.

Version relationships. The four periodic reports are sequential periods of one registrant, not versions of one another; each stays an active source. The first 10-Q of 2026 and the third differ on the Elara price, addressed in the conflicts section.

### Entity and perimeter

The registrant is Hilton Grand Vacations Inc., and all periodic statements are consolidated. The consolidation includes variable interest entities and a 51 percent joint venture, so the figures include non-recourse and noncontrolling-interest perimeters.

| Perimeter point | Locator | Quote |
| --- | --- | --- |
| Joint venture consolidated at 51 percent | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:6` | "Bluegreen/Big Cedar Vacations LLC (“Big Cedar”), a joint venture in which we are deemed to hold a controlling financial interest based on our 51% equity interest" |
| Variable interest entities inside total assets and liabilities | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "TOTAL ASSETS (variable interest entities - $2,835 and $2,601)" |
| Noncontrolling interest in equity | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "Noncontrolling interest 162 151" |
| Corporate versus non-recourse debt shown on separate balance sheet lines | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:2` | "Non-recourse debt, net 2,891 2,716" |
| Guarantors of the 2032 secured notes are unnamed in the notes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:24` | "The Senior Notes due 2032 are guaranteed on a senior secured basis by certain of our subsidiaries." |
| Borrower and issuer entities appear only in the exhibit index | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:167` | "Indenture, dated as of January 17, 2024, among Hilton Grand Vacations Borrower LLC, Hilton Grand Vacations Borrower Inc., Hilton Grand Vacations Inc., Hilton Grand Vacations Parent LLC" |
| Apollo affiliates as a related party; holding above 20 percent at the 2021 acquisition (current holding not read) | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:31` | "Apollo obtained more than 20% of our common stock at the time of the acquisition" |

Roles that remain unresolved: the identity of each guarantor subsidiary, which subsidiaries are restricted or unrestricted under the credit agreement, and the lien package. The pack contains no restricted-group financials. The context leaves borrower, parent and guarantors blank, so the filing exhibit index is the only place the Borrower LLC, Borrower Inc. and Parent LLC names appear.

### Coverage by evidence need

| Evidence need | Located | Locator | Quote |
| --- | --- | --- | --- |
| Corporate debt by instrument with rates, balances at the latest date and at year end | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:22` | "Total debt, gross 4,946 4,603" |
| Non-recourse debt by facility | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:24` | "Total non-recourse debt, gross 2,923 2,751" |
| Contractual maturity table by year for debt and non-recourse debt | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:26` | "Total $ 4,946 $ 2,923 $ 7,869" |
| Revolver letters of credit and remaining capacity | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | "we have $457 million remaining borrowing capacity under the revolver facility" |
| Letters of credit drawn on the revolver | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | "we had $53 million of letters of credit outstanding under the revolving credit facility" |
| Unrestricted and restricted cash | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:57` | "we had total cash and cash equivalents of $227 million and restricted cash of $275 million" |
| Non-recourse warehouse capacity | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:25` | "As of September 30, 2026, our Timeshare Facility has a remaining borrowing capacity of $450 million." |
| Cash flow statement, nine months | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:4` | "Net cash provided by operating activities 349 133" |
| Cash paid for interest, corporate debt | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:24` | "Cash paid for interest on our corporate debt, net was $207 million" |
| Segment revenues and Adjusted EBITDA definition | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:32` | "We define Adjusted EBITDA as EBITDA, further adjusted to exclude certain items" |
| Adjusted EBITDA reconciliation, three and nine months | Yes (release) | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:18` | "Adjusted EBITDA attributable to stockholders $ 609 $ 245 $ 1,123 $ 658" |
| 2025 quarterly Adjusted EBITDA and full year, for a trailing build | Yes (release) | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:7` | "Adjusted EBITDA 185 238 249 297 969" |
| Inventory purchase commitments, marketing and license commitments | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:35` | "we were committed to purchase approximately $304 million of inventory over a period of 12 years" |
| Total contractual obligations | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:59` | "we were committed to $10.1 billion in contractual obligations over 14 years" |
| Surety bonds | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:36` | "We have commitments from surety providers in the amount of $346 million" |
| Litigation accrual | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:36` | "we accrued liabilities of approximately $19 million and $8 million, respectively, for all legal matters" |
| Acquisition note (Elara) | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:8` | "completed the acquisition of the remaining 75% ownership interest in BRE Ace LLC" |
| Business and segment description | Yes | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:1` | Cover page only; the business description is at `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:6`: "a global timeshare company engaged in developing, marketing, selling, managing and operating timeshare resorts" |
| Annual 10-K business and risk sections | Yes | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:116` | "NOTE 1: ORGANIZATION AND BASIS OF PRESENTATION" |
| Year-end debt and revolver capacity for the FY2025 comparison | Yes | `10-K_2025-12-31_hgv-20251231.htm.jsonl page:144` | "we have $809 million remaining borrowing capacity under the revolver facility" |
| Management leverage figure | Yes (release only) | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:6` | "total net leverage on a trailing 12-month basis was approximately 3.9x" |
| Full-year guidance change | Yes (release only) | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:2` | "The Company is reducing its guidance for the full year 2026 Adjusted EBITDA, excluding deferrals and recognitions" |

### Events and items the downstream modules must carry

| Item | Locator | Quote |
| --- | --- | --- |
| Term Loan B refinancing on July 17, 2026 (a Q3 event disclosed first in the Q2 report) | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | "On July 17, 2026, we refinanced our Term Loan B due 2028 with an amended $850 million Term Loan B due 2033." |
| New receivables warehouse facility at Big Cedar | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:25` | "On September 14, 2026, Big Cedar entered into the Big Cedar Timeshare Facility, a $200 million revolving receivables warehouse facility" |
| Timeshare Facility renewal and upsizing in May 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:25` | "increasing the facility size from $850 million to $1.0 billion" |
| Change in the financing-receivable allowance method, prospective | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:16` | "we recorded a $55 million decrease in the allowance for originated timeshare financing receivable" |
| Large Q3 construction recognition affecting reported revenue and Adjusted EBITDA | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:2` | "Total revenues were affected by a net construction recognition of $536 million." |
| Share repurchase program authorised August 12, 2026 | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:59` | "On August 12, 2026, our Board of Directors approved a share repurchase program authorizing us to repurchase up to an aggregate of $600 million" |
| Preliminary purchase accounting for Elara | `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:9` | "Any potential adjustments made could be material in relation to the values presented in the table below." |
| Q1 report's subsequent event securitisation | `10-Q_2026-03-31_hgv-20260331.htm.jsonl page:29` | "On April 16, 2026, we completed a $500 million securitization of timeshare loans" |

### Document conflicts and version distinctions

| Item | Locators | Effect |
| --- | --- | --- |
| Elara purchase price: the Q1 report states one price, the Q3 report states a higher total cash consideration | Q1: `10-Q_2026-03-31_hgv-20260331.htm.jsonl page:30` "The purchase price was $129 million and is subject to certain post-closing adjustments"; Q3: `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:8` "for a total cash consideration of $131 million" | Not a contradiction: the Q1 text is a subsequent-event statement made before closing adjustments. The Q3 note controls. Downstream modules should use the Q3 note and label the Q1 figure as superseded. |
| Management leverage statement is in the releases only; the filings do not print a leverage ratio | `EX-99.1_2026-10-29_hgvq32026earningsreleaseex.htm.jsonl page:6` and the absence of any ratio in the 10-Q covenant sentence at `10-Q_2026-09-30_hgv-20260930.htm.jsonl page:23` | A management claim, not an audited or filed figure. It cannot be used as a covenant measure; any leverage computed downstream must be labelled as the analyst's own and not the credit agreement definition. |

No other filing-to-release or period-to-period conflict was found in the items read. This is not a full line-by-line reconciliation, which CP-0 does not perform.

### Consumer assessments

| Consumer | Status | Reason |
| --- | --- | --- |
| CP-1 financial and debt extraction | READY_WITH_LIMITATIONS | Statements, debt note, maturities, liquidity, cash flow, segment and non-GAAP reconciliation are located. Limitations: covenant levels and definitions not supplied; consolidated perimeter only; Q3 estimate change and construction recognition; revolver total commitment not printed (only drawn amount, letters of credit and remaining capacity). |
| CP-1A business and transaction context | READY_WITH_LIMITATIONS | Business note, segment note, Elara acquisition, Big Cedar, related-party and Apollo disclosures, commitments and risk-factor references are located. Limitation: no investor presentation, no executed transaction documents, and the Elara allocation is preliminary. |
| CP-2 credit synthesis | READY_WITH_LIMITATIONS | Source evidence supports synthesis from the CP-1 and CP-1A handoffs. It must carry every limitation above, and it cannot draw on text from the sources directly. |
| CP-5 evidence trace review | READY_WITH_LIMITATIONS | Every cited source is retained and addressable by page chunk. It inherits the same limitations and must flag any claim that leans on the management leverage figure. |

None of these is CONDITIONAL or BLOCKED. A missing downstream handoff is not treated as a source condition.

## Calculations

None. CP-0 does not normalise, reconcile or calculate figures. Every number above is quoted from a located source span. A trailing twelve-month Adjusted EBITDA would need assembly from the FY2025 quarterly table and the 2026 nine-month table in the Q3 release; that is a downstream task and is not done here.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Executed credit agreement, amendments, indentures and the intercreditor terms are not in the pack. The 10-K exhibit index lists them but their text is not supplied. Covenant test levels, step-downs, definitions, baskets, guarantor identities and collateral cannot be read. | High | CP-1, CP-2, CP-5 | Add the credit agreement and its amendments and the three indentures to the pack. |
| Covenant compliance appears only as a general statement: "We were in compliance with all applicable maintenance and financial covenants and ratios as of September 30, 2026". No reported covenant ratio or headroom. | High | CP-1, CP-2 | Obtain the compliance certificate or the credit agreement; otherwise mark headroom Not supplied. |
| Management net leverage figure has no definition or calculation in the pack. | Medium | CP-1, CP-2, CP-5 | Carry it as a management claim; compute any leverage with stated inputs. |
| Revolver total commitment is not printed in the pages read; the notes give drawn balance, letters of credit and remaining capacity only. A search of the Q3 10-Q and the 10-K for commitment wording found none. | Medium | CP-1 | Use the printed remaining capacity; do not infer a commitment size without labelling the derivation. |
| No investor presentation; the releases substitute for it. They carry management narrative and non-GAAP measures only. | Low | CP-1A | None needed for source readiness. |
| No ratings, market prices, peer set or valuation inputs in the context. | Low | CP-2 | Not required for the selected modules. |
| Elara purchase accounting is preliminary, within a one-year measurement period. | Medium | CP-1, CP-1A | Carry as preliminary; re-check at the next filing. |
| Third quarter earnings include a one-time construction recognition and an allowance method change, so Q3 is not comparable with earlier quarters without adjustment. | Medium | CP-1, CP-2 | Use the construction deferral tables in the releases to present results with and without the effect. |
| The Q3 10-Q has no subsequent-events note; a search of the Q3 10-Q and Q3 release text for subsequent events found none. Events after September 30, 2026 up to the cutoff are therefore only those in the October 29, 2026 release and the filing text. | Low | CP-1A, CP-2 | Treat the release and the cover-page share count date as the latest dated evidence. |
| Extraction fidelity has not been reviewed. The files are text extractions; tables are flattened, so column alignment in multi-period tables was read from row context. No images, charts or speaker notes exist in the pack, and none are claimed as inspected. | Low | All | Spot-check key tables against the filings downstream. |
| Currency and unit: all financial statements are in USD millions; share counts and per-share data are in units as printed. No other currency is reported. | Info | All | None. |

## Next module

Proceed to CP-1 (financial and debt extraction) on the consolidated, USD, US GAAP perimeter, with the following carried forward: corporate debt and non-recourse debt kept separate; revolver capacity net of letters of credit read from the notes; the covenant levels listed as Not supplied; the leverage figure treated as a management claim; the Q3 construction recognition and allowance estimate change presented separately; the Elara price taken from the Q3 note. CP-1A, CP-2 and CP-5 follow in the dependency order and inherit the same limitations. The next evidence action, outside this run, is to add the credit agreement and indentures to the pack.
