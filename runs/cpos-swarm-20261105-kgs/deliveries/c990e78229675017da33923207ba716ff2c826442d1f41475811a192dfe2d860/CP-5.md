## Request

Evidence trace and research-integrity review of the Kodiak Gas Services, Inc. (KGS) credit snapshot run, as of 2026-11-05, pathway credit_snapshot, reporting currency USD. It checks whether each material claim in the source-readiness, financial-base, business-context and credit-synthesis handoffs rests on the evidence it names, and whether the four tell one consistent story. It changes no upstream conclusion and repairs no lineage silently.

## Sources

### Issuer sources relied on

All seven pinned sources were reopened to test the cited pages and quotations.

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

### Upstream handoffs

| Module | sha256 |
| --- | --- |
| CP-0 source readiness | 1490db53fcb453be1025254f11915cd1c064e8caa925cbc2f680c4e837a39f8b |
| CP-1 financial base | 928e75ea3fae150cc85c2160f71e6fedb1e4eb8f73c7fa7de4272160b731156b |
| CP-1A business and transaction context | d0241813cd4782b418a4a9fd140c7da5b42a2f1e8f8fafd5f5fb9446a87dfaa7 |
| CP-2 credit synthesis | bd5f3e5cb0b756c4f3ac8db38a5c6a77f29f908f3e27b90c219031aa7ae5587a |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The credit view is traceable: every key figure and quotation tested matched the filings at the cited pages, and each derived metric reproduces. Eleven defects were found, one material and already corrected, none changing a conclusion. | Medium | Executed financing documents, power contracts and covenant definitions are not supplied, so covenant headroom and power visibility cannot be traced to primary terms. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 53 figures and quotations tested in the key claims matched the cited pages; derived metrics such as 766,091 LTM adjusted EBITDA and 3.63x leverage reproduce. | Leverage, liquidity and cash-flow conclusions rest on traceable inputs. | High |
| Ten minor locator, wording and lineage defects were found, eight still open; none changes a figure. | Citations need the corrected pages listed here, but the credit conclusions stand. | High |
| The source-readiness handoff misstated sponsor holdings and the financial-base handoff overstated a dividend condition; the business-context handoff corrected both. | Readers should use the corrected statements: the sponsor affiliate exited by December 2, 2025. | High |
| The year-end leverage range of 3.27x to 3.52x is an analyst inference whose capital spending inputs sit outside the earlier handoffs. | Treat it as indicative; it does not change the accepted credit view. | Medium |
| Covenant headroom, guarantor structure and power contract terms cannot be traced to primary documents. | Committee use is restricted for covenant- and structure-dependent decisions. | High |

### Evidence trace view

The analysis is traceable enough for a credit snapshot decision on leverage, liquidity and cash flow, and restricted for covenant, guarantee-structure and power-visibility conclusions. Of 20 material claims traced, 9 are directly sourced and string-matched to a page, 7 are calculations that reproduce from verified inputs, 2 are management statements correctly attributed, and 2 are analyst inferences, each labelled. The five top drivers (leverage, liquidity and commitments, contracted revenue, earnings and cash quality, covenant headroom) trace to the filings except the last, which stops at a summary because the credit agreement is not supplied. The critical provenance gap is the absence of executed financing documents; adding the credit agreement, its amendments and the indentures would clear it, owned by the data team that assembles the pack.

| Traceability summary | Count |
| --- | --- |
| Directly sourced claims | 9 |
| Calculated claims, reproduced | 7 |
| Management language, attributed | 2 |
| Analyst inference or interpretation | 2 |
| Defects open | 8 |
| Defects closed | 3 |

Committee status: Restricted. QA status: Restricted for covenant, guarantee-structure and power-visibility conclusions. The deterministic confidence score is not computed in this run; claim-level confidence is shown row by row in the registers.

### Analytical appendix — complete canonical registers

#### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_kgs-20251231.htm.jsonl | Audited annual report; primary | Year ended December 31, 2025 with 2024 and 2023 comparatives | Kodiak Gas Services, Inc. consolidated | Statements, debt note, covenant terms, business, sponsor exit | Segment tables on the earlier two-segment basis; no exhibits text | Financial base, business context |
| S2 | 10-Q_2025-09-30_kgs-20250930.htm.jsonl | Quarterly report; unaudited; primary | Quarter and nine months ended September 30, 2025 | Same consolidated perimeter | September 2025 balances, ABL drawings and letters of credit | Debt table includes bond premium inside its total | Liquidity point, history |
| S3 | 10-Q_2026-03-31_kgs-20260331.htm.jsonl | Quarterly report; unaudited; primary | Quarter ended March 31, 2026 | Same consolidated perimeter | March 2026 balances, flows, early disclosure of the power acquisition | Acquisition accounting incomplete at filing | Financial base, LTM March 2026 |
| S4 | 10-Q_2026-06-30_kgs-20260630.htm.jsonl | Quarterly report; unaudited; primary | Quarter and six months ended June 30, 2026 | Same perimeter, including the power business from April 1, 2026 | Statements, debt, commitments, segments, performance obligations | Preliminary purchase accounting | All modules |
| S5 | EX-99.1_2026-02-25_kgsq42025earningsrelease.htm.jsonl | Earnings release; management attributed | Fourth quarter and year 2025 | Same consolidated perimeter | Discrete third and fourth quarter figures, reconciliations, initial guidance | Non-GAAP; furnished, not filed statements | Financial base |
| S6 | EX-99.1_2026-05-11_kgsq12026earningsrelease.htm.jsonl | Earnings release; management attributed | Quarter ended March 31, 2026 | Same consolidated perimeter | Management leverage ratio, capacity commentary | Management characterisations | Business context |
| S7 | EX-99.1_2026-08-06_kgsq22026earningsrelease.htm.jsonl | Earnings release; management attributed | Quarter ended June 30, 2026 | Same perimeter | Liquidity statement, management ratios, revised guidance | Non-GAAP; guidance is a management claim | Financial base, synthesis |

#### Top five material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage of 3.63x total and 3.45x net on LTM adjusted EBITDA | CP-1 | Total debt outstanding 2,780,917; LTM adjusted EBITDA 766,091; cash 137,553 | Sets debt capacity and covenant context | Core leverage statistic | S4 page:20, page:56; S5 page:13; S4 page:6 | Excludes acquired EBITDA before April 1, 2026 |
| 2 | Liquidity of 1,742.0 US$m against twelve-month commitments of USD 587.9 million | CP-1, CP-1A | Cash plus undrawn ABL; commitments disclosure | Funds the power build | Determines funding risk | S4 page:6, page:20-21, page:29; S7 page:5 | Borrowing base not supplied |
| 3 | Contracted compression revenue of 2,643,245 (USD thousands) in performance obligations | CP-1A | Performance obligations table | Revenue visibility supports debt service | Supports the credit view | S4 page:17; S1 page:116-117; S3 page:10 | Rise is unexplained; excludes power leases |
| 4 | Earnings and cash quality: add-backs of 21.2% and cash conversion of 62.5% | CP-1 | Reconciliations of adjusted EBITDA; cash flow statements | Metrics on adjusted EBITDA overstate cash earnings | Informs monitoring | S5 page:13; S4 page:9, page:56 | Company definition of adjusted EBITDA |
| 5 | Covenant headroom: management ratio 3.2x against a 5.25 to 1.00 maximum | CP-1 | Printed covenant levels and management ratio | Determines default headroom | Gating for committee use | S1 page:72; S7 page:5 | Definitions and current terms not supplied |

#### Traceability map

Classification: DS Directly Sourced; CALC Calculated; ML Management Language; AI Analyst Inference.

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt outstanding USD 2,780,917 thousand at June 30, 2026 | CP-1 | "Total debt outstanding 2,780,917 2,614,647" | Yes | Primary filing | DS | Supported | High | Verified at page |
| LTM adjusted EBITDA 766,091 | CP-1 | Reported FY2025, H1 2026 and H1 2025 figures; equals sum of four reported quarters | Yes | Primary filing plus release | CALC | Supported | High | Reproduced |
| Total debt / EBITDA 3.63x and net 3.45x | CP-1 | Debt, cash and EBITDA above | Yes | Primary filing plus release | CALC | Supported | High | Reproduced |
| Liquidity 1,742.0 US$m | CP-1 | Commitments of $2.0 billion, drawn 380,917, letters of credit $14.6 million, cash 137,553; company states $1.7 billion total liquidity | Yes | Primary filing | CALC | Supported with limitation | Medium | Reproduced; upper bound |
| Purchase commitments $2.5 billion, $587.9 million within twelve months | CP-1, CP-1A | "these commitments amounted to $2.5 billion, of which $587.9 million is expected to be settled within the next twelve months" | Yes | Primary filing | DS | Supported | High | Verified at page |
| Compression performance obligations 2,643,245 and schedule | CP-1A | Table at 10-Q 2026-06-30 page:17 | Yes | Primary filing | DS | Supported | High | Verified at page |
| Add-backs 162,706 (21.2%) | CP-1 | Company reconciliations; unadjusted EBITDA plus add-backs equals reported adjusted EBITDA for FY2025 and LTM | Yes | Primary filing plus release | CALC | Supported | High | Reproduced |
| Operating cash flow 62.5% of LTM adjusted EBITDA | CP-1 | Cash flow statements and reported EBITDA | Yes | Primary filing | CALC | Supported | High | Reproduced |
| Covenant levels 5.25 to 1.00, 3.25 to 1.00, 2.5x | CP-1 | "The maximum Leverage Ratio is 5.25 to 1.00" | Yes | Primary filing | DS | Supported for FY2025 terms only | Medium | Verified; later terms not supplied |
| Management leverage 3.5x, 3.6x, 3.2x, 3.1x | CP-1, CP-2 | Release statements at page:2, page:3, page:5 | Yes (pages added here) | Management release | ML | Attributed | Medium | Verified at page |
| Sponsor ownership 43.1% to zero by December 2, 2025 | CP-1A | "approximately 43.1% at the beginning of the year to zero by December 2, 2025" | Yes | Primary filing | DS | Supported | High | Verified at page |
| Power acquisition consideration 726,354 and signing value about USD 675.0 million | CP-1, CP-1A | Both statements | Yes | Primary filing | DS | Supported; conflict logged | High | Verified at both pages |
| Revised 2026 guidance (adjusted EBITDA 830,000 to 860,000 and other lines) | CP-1, CP-2 | Release guidance table | Yes | Management release | ML | Attributed | Medium | Verified at page |
| Guided discretionary cash flow less growth and other capital spending of (235,000) to (125,000) | CP-1, CP-2 | Guidance table | Yes | Management release | CALC | Supported | Medium | Reproduced |
| One disclosed power lease, initial term to April 1, 2028 | CP-1A | "The initial lease term ends on April 1, 2028" | Yes | Primary filing | DS | Supported | High | Verified at page |
| Customer concentration 32% and 14%; 82.8% Permian and Eagle Ford | CP-1A | 10-K page:13, page:14, page:110 | Yes | Primary filing | DS | Supported | High | Verified at page |
| Distributions 263,525 against company free cash flow 229,581 | CP-1A | 10-K page:102; release page:14 | Yes | Primary filing plus release | CALC | Supported | High | Reproduced |
| Sanctions-related payments matter, penalty not estimated | CP-1, CP-1A | "The aggregate amount of these payments was not material" | Yes | Primary filing | DS | Supported | High | Verified at page |
| Year-end 2026 net leverage 3.27x to 3.52x | CP-2 | Guidance, first-half actuals, dividends | Yes (in the synthesis calculations) | Derived | AI | Inference | Low | Reproduced; inputs partly outside upstream |
| Behaviour category Neutral or Mixed | CP-1A | Documented equity issuance, buybacks, dividends | Yes | Primary filing | AI | Interpretation | Medium | Supported by listed actions |

#### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt outstanding 2,780,917 and ABL 380,917 | runs/cpos-swarm-20261105-kgs/source-text/ | 10-Q_2026-06-30_kgs-20260630.htm.jsonl | S4 | page:19-20 | CP-1 Debt and capital structure | Table | Primary | ABL and notes principal printed on page:19 |
| Adjusted EBITDA reconciliation, H1 and Q2 | runs/cpos-swarm-20261105-kgs/source-text/ | 10-Q_2026-06-30_kgs-20260630.htm.jsonl | S4 | page:56 | CP-1 Income statement and EBITDA | Table | Primary | Company non-GAAP |
| FY2025 adjusted EBITDA 715,033 and add-backs | runs/cpos-swarm-20261105-kgs/source-text/ | EX-99.1_2026-02-25_kgsq42025earningsrelease.htm.jsonl | S5 | page:13 | CP-1 Cash flow quality and add-backs | Table | Management release | Reproduces to the dollar |
| Cash paid for interest and operating cash flow | runs/cpos-swarm-20261105-kgs/source-text/ | 10-K_2025-12-31_kgs-20251231.htm.jsonl; 10-Q_2026-06-30_kgs-20260630.htm.jsonl; 10-Q_2026-03-31_kgs-20260331.htm.jsonl | S1, S4, S3 | S1 page:102; S4 page:9; S3 page:8 | CP-1 Reported balance sheet and cash flow | Table | Primary | Quarterly interest derived by subtraction |
| ABL terms and compliance statement | runs/cpos-swarm-20261105-kgs/source-text/ | 10-Q_2026-06-30_kgs-20260630.htm.jsonl | S4 | page:21 | CP-1 Debt and capital structure | Text | Primary | Fifth Amendment effect through June 30, 2026 |
| Covenant levels | runs/cpos-swarm-20261105-kgs/source-text/ | 10-K_2025-12-31_kgs-20251231.htm.jsonl | S1 | page:72 | CP-1 Covenants | Text | Primary | FY2025 terms |
| Management leverage ratios | runs/cpos-swarm-20261105-kgs/source-text/ | EX-99.1 releases | S5, S6, S7 | S5 page:2; S6 page:3; S7 page:5 | CP-1 Chart data: leverage | Text | Management release | Definition not supplied |
| Purchase commitments | runs/cpos-swarm-20261105-kgs/source-text/ | 10-Q_2026-06-30_kgs-20260630.htm.jsonl; 10-Q_2026-03-31_kgs-20260331.htm.jsonl | S4, S3 | S4 page:29; S3 page:34 | CP-1 Debt and capital structure | Text | Primary | Rise from $276.4 million |
| Performance obligations | runs/cpos-swarm-20261105-kgs/source-text/ | 10-K, 10-Q March, 10-Q June | S1, S3, S4 | S1 page:116; S3 page:10; S4 page:17 | CP-1A Revenue visibility | Table | Primary | Contract Services label before June 2026 |
| Sponsor exit | runs/cpos-swarm-20261105-kgs/source-text/ | 10-K_2025-12-31_kgs-20251231.htm.jsonl | S1 | page:25, page:63 | CP-1A Ownership and governance | Text | Primary | Corrects the source-readiness handoff |
| Power acquisition terms | runs/cpos-swarm-20261105-kgs/source-text/ | 10-K, 10-Q March, 10-Q June | S1, S3, S4 | S1 page:25; S3 page:24; S4 page:12-13 | CP-1A Transaction summary | Text and table | Primary | Signing and closing bases differ |
| Guidance | runs/cpos-swarm-20261105-kgs/source-text/ | EX-99.1_2026-02-25; EX-99.1_2026-08-06 | S5, S7 | S5 page:4-5; S7 page:7 | CP-1 Guidance; CP-2 sensitivity | Table | Management release | Management claim |
| Power lease term | runs/cpos-swarm-20261105-kgs/source-text/ | 10-Q_2026-06-30_kgs-20260630.htm.jsonl | S4 | page:18 | CP-1A Operating model | Text | Primary | One agreement |
| Customer and basin concentration | runs/cpos-swarm-20261105-kgs/source-text/ | 10-K_2025-12-31_kgs-20251231.htm.jsonl | S1 | page:13, page:14, page:110 | CP-1A Operating model | Text | Primary | FY2025 |
| Distributions and free cash flow | runs/cpos-swarm-20261105-kgs/source-text/ | 10-K_2025-12-31_kgs-20251231.htm.jsonl; EX-99.1_2026-02-25 | S1, S5 | S1 page:102; S5 page:14 | CP-1A Calculation A4 | Table | Primary and release | Free cash flow is company non-GAAP |
| Segment capital expenditure and growth capital expenditure | runs/cpos-swarm-20261105-kgs/source-text/ | 10-Q_2026-06-30_kgs-20260630.htm.jsonl | S4 | page:34, page:58 | CP-1 Calculation C11; CP-2 Calculation D2 | Table | Primary | CP-2 inputs from page:58 are not in upstream text |

#### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM adjusted EBITDA | CP-1, CP-2 | 715,033; 406,938; 355,880 | FY2025 + H1 2026 - H1 2025 = 766,091; also sum of four quarters | Reproduced | Supported | High | Denominator of leverage | S5 page:13; S4 page:56 |
| Total and net debt / EBITDA | CP-1, CP-2 | 2,780,917; 137,553; 766,091 | 2,780,917 / 766,091 = 3.63x; 2,643,364 / 766,091 = 3.45x | Reproduced | Supported | High | Leverage | S4 page:6, page:20 |
| Debt on carrying value basis | CP-5 (this register) | Long-term debt net 2,720,989 plus other borrowings 4,283 = 2,725,272 | 2,725,272 / 766,091 = 3.56x; net of cash (2,725,272 - 137,553) / 766,091 = 3.38x; gross delta to principal 59,928 | New check | Supported | High | Alternative basis for leverage | S4 page:6, page:20 |
| Cash interest cover | CP-1 | 766,091; 185,176 | 766,091 / 185,176 = 4.14x | Reproduced | Supported | Medium | Coverage; cash timing | S1 page:102; S4 page:9; S3 page:8 |
| Liquidity | CP-1 | 2,000,000; 380,917; 14,600; 137,553 | 2,000,000 - 380,917 - 14,600 + 137,553 = 1,742,036 | Reproduced | Supported with limitation | Medium | Funding capacity | S4 page:6, page:20-21 |
| Add-backs and unadjusted leverage | CP-1 | Reconciliation lines | 603,385 + 162,706 = 766,091; 2,780,917 / 603,385 = 4.61x | Reproduced | Supported | High | Earnings quality | S5 page:13; S4 page:56 |
| Operating cash flow conversion | CP-1 | 478,887; 766,091 | 478,887 / 766,091 = 62.5% | Reproduced | Supported | High | Cash quality | S4 page:9 |
| Covenant cushion on management ratio | CP-1 | 3.2x; 5.25 to 1.00 | 1 - 3.2 / 5.25 = 39.0% | Reproduced | Indicative | Low | Headroom, not recomputed | S1 page:72; S7 page:5 |
| Share of performance obligations in 2028 or later | CP-1A | Three tables | 1,318,499 / 2,643,245 = 49.9% | Reproduced | Supported | High | Visibility tenor | S4 page:17 |
| Guided free cash flow range | CP-1, CP-2 | 570,000 to 600,000; 725,000 to 805,000 | 570,000 - 805,000 = (235,000); 600,000 - 725,000 = (125,000) | Reproduced | Supported | Medium | Funding need | S7 page:7 |
| Year-end 2026 net leverage | CP-2 | Guidance, H1 actuals, dividends of 99,082 | Net debt 2,809,322 / 860,000 = 3.27x; 2,919,322 / 830,000 = 3.52x | Reproduced | Inference | Low | Indicative trajectory; assumes debt funding and excludes equity | S4 page:57-58; S7 page:7 |
| Distributions against free cash flow | CP-1A | 159,557; 103,968; 229,581 | 263,525 - 229,581 = 33,944 | Reproduced | Supported | High | Capital allocation | S1 page:102; S5 page:14 |

#### Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | Gas compression equipment buyout | CP-1 cites the release at page:2; the 43,000 horsepower statement is at S7 page:5 | Locator error | Wrong page in the event table | Cite S7 page:5 | CP-1 financing events table |
| Minor | Debt instrument principal amounts | CP-1 cites page:20-23 for principal amounts printed in the debt table on S4 page:19 | Locator error | Reader cannot find the figure at the cited page | Cite S4 page:19-20 | CP-1 debt table |
| Minor | Management leverage ratios | CP-1 covenant table cites "releases" without pages; first-quarter 3.6x is at S6 page:3 | Weak locator | Claim not individually traceable in that row | Cite S5 page:2, S6 page:3, S7 page:5 | CP-1 covenant table |
| Minor | Loss on extinguishment 36,512; loss on disposal 33,349; impairment 6,344 | Cited pages print rounded millions; exact thousands at S4 page:7, S5 page:13, S1 page:99-100 | Precision mismatch | Exact figure not on the cited page | Add the exact-figure pages | CP-1 financing events and add-backs |
| Minor | Leverage and cover chart rows | Inputs appear without row-level page locators | Weak lineage | Row cannot be traced in isolation | Cite the debt, cash and EBITDA pages in each row | CP-1 chart data |
| Minor | Preferred shares paired with OpCo Units | CP-1A cites S4 page:26 for 224 thousand; the figure is at S4 page:9 and page:35 | Locator error | Wrong page | Cite S4 page:9, page:35 | CP-1A company profile |
| Minor | Release headline quotation | CP-0 quotes "Record Compression Infrastructure segment revenues" and omits the footnote marker printed in the source | Quotation fidelity | Quote is not character-exact | Quote with the marker or paraphrase | CP-0 credit-relevant observations |
| Minor | Capital spending inputs to the leverage sensitivity | CP-2 uses first-half growth and other capital spending of 134,357, 152,356 and 61,167 from S4 page:58, which no upstream handoff carries; CP-2 also states that no source page was read again | Lineage break | Inputs are not traceable through upstream text | Cite S4 page:58 in CP-2; carry inputs upstream | CP-2 calculation D2 |

#### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source access and identity | Strong | All seven sources identified from cover or text and reopened | Misidentified periods would corrupt LTM sums | LTM metrics can be relied on | None |
| Locator specificity | Good with slips | 53 of 53 figures and quotations tested matched at their pages; eight locator or wording slips | A reader may not find a figure | Citations need the corrections in the flags register | Apply listed corrections |
| Calculation reproducibility | Strong | Every derived figure reproduces from verified inputs; four-quarter sums equal LTM sums | Silent arithmetic error | Metrics are dependable | None |
| Definition consistency | Adequate | Principal debt used, carrying-value basis delta logged as 59,928; adjusted EBITDA kept separate from covenant EBITDA | Mixed definitions inflate or deflate leverage | Leverage is a principal-basis, adjusted-EBITDA measure | Keep basis labelled |
| Management versus filing separation | Strong | Releases labelled as Management Language; filings control figures | Management claims treated as fact | Covenant and growth claims remain attributed | None |
| Subsequent events | Strong | July 2026 lease buyout and August 2026 dividend labelled as subsequent events | Events blended into period figures | June 30, 2026 balances remain clean | None |
| Cross-module consistency | Adequate after corrections | Two upstream statements corrected downstream; acquisition value difference logged | Contradictory facts across modules | Readers must use corrected statements | Apply corrections |
| Gap disclosure | Strong | Executed documents, contracts and later filings stated as gaps | Hidden dependence on missing documents | Confidence bounded | Obtain documents |

#### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| TG1 | Covenant definitions and current terms | Credit agreement, Fifth Amendment, amendments | Headroom cannot be tested | Covenant statements remain attributed | Caps covenant confidence | Executed ABL documents |
| TG2 | Guarantors and security | Indentures, guarantor schedules | Structural claims cannot be traced | Structure statements remain at summary level | Caps structure confidence | Indentures and schedules |
| TG3 | Power contract portfolio | Customer contracts or disclosure beyond one lease | Visibility of the new segment not testable | Power conclusions marked as inference | Caps power confidence | Contract summaries or later filings |
| TG4 | Pro forma EBITDA for the acquired business | Acquired-business earnings before April 1, 2026 | Leverage overstated on a full-year perimeter | Leverage carries a stated caveat | Medium confidence on trajectory | Acquisition current report or later filings |
| TG5 | Later periodic filing | Quarter ended September 30, 2026 | Latest balance sheet is June 30, 2026 | Metrics are as of that date | Bounded by date | Any filing on or before 2026-11-05 |
| TG6 | Reasons for the rise in performance obligations and for allowance write-offs | Management explanation | Quality of new contracts and credit events not traceable | Interpretation labelled | Medium confidence | Later filings or management |
| TG7 | Use of equity offering proceeds | Offering documents | Funding of the acquisition not traceable | Link to ABL repayment is inference | Medium confidence | Prospectus supplement |

#### Module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | runs/cpos-swarm-20261105-kgs/requests/CP-0/c312464695a3a944cd504bb5401b6e8c9eeda5e110d06c8226d64d41be5b44cc/1.response.md; kgs-2026-11-05-credit_snapshot-host | Source readiness for four downstream modules | Primary filings and releases | Six H2 headings present; accepted by CP-OS | Accepted with one material correction | Sponsor holdings statement corrected by CP-1A; one quotation lacks a footnote marker |
| CP-1 | runs/cpos-swarm-20261105-kgs/requests/CP-1/fabb29da3e28583a80828d5fb778e74e08b97a0bacf3fe4a06cc0843f49fdcf2/1.response.md; kgs-2026-11-05-credit_snapshot-host | Financial base, chart data and credit metrics | Primary filings and releases | Six H2 headings and selectors present; accepted | Accepted with minor locator defects | Dividend-condition wording narrowed by CP-1A |
| CP-1A | runs/cpos-swarm-20261105-kgs/requests/CP-1A/84ca961de212017fb66092804759f77085ca1be3ae506e4bad5afc76adc54e40/1.response.md; kgs-2026-11-05-credit_snapshot-host | Business, ownership and transaction context | Primary filings and releases | Six H2 headings and selectors present; accepted | Accepted with one minor locator defect | Carries the corrections to CP-0 and CP-1 |
| CP-2 | runs/cpos-swarm-20261105-kgs/requests/CP-2/3b07a6bc7a9c2ce73f17cca9cf101d5e8971f2e1f019c8b94520238460c319c2/1.response.md; kgs-2026-11-05-credit_snapshot-host | Fundamental credit synthesis | Upstream handoffs | Six H2 headings and selectors present; accepted | Accepted with one minor lineage defect | Sensitivity inputs partly outside upstream text |

#### Citation and evidence-support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Financing events: buyout of leased equipment | Supported at a different page | Release page cited as page:2; statement at page:5 | Correct the page | None on conclusions |
| Minor | CP-1 | Debt table principal amounts | Supported at a different page | Principal printed on page:19 | Correct the page range | None on conclusions |
| Minor | CP-1 | Covenant table management ratios | Supported | Pages not given in the row | Add pages | None on conclusions |
| Minor | CP-1 | Exact thousands for three add-back and refinancing figures | Supported at other pages | Cited pages print millions | Add exact-figure pages | None on conclusions |
| Minor | CP-1A | Preferred shares and OpCo Units | Supported at a different page | Figure at page:9 and page:35 | Correct the page | None on conclusions |
| Minor | CP-0 | Release headline quotation | Supported | Footnote marker omitted | Restore the marker | None on conclusions |
| Minor | CP-2 | Leverage sensitivity inputs | Supported at S4 page:58 | Not carried by an upstream handoff | Cite the page and carry inputs upstream | Sensitivity remains labelled inference |

#### Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Leverage is on principal debt, whereas the canon basis is carrying value net of issuance costs | Gross delta between principal 2,780,917 and carrying value 2,720,989 is 59,928 (63,817 of issuance costs less 3,889 of premium); on carrying value including other borrowings leverage is 3.56x total and 3.38x net | None | Keep the principal basis labelled and cite the carrying-value alternative here | None on conclusions |
| Minor | CP-1 | LTM adjusted EBITDA excludes the acquired business before April 1, 2026 | Pro forma EBITDA Not calculable | Pack gives pro forma revenue and earnings only | Obtain acquired-business earnings | Leverage carries a stated caveat |
| Minor | CP-1 | Adjusted EBITDA versus covenant EBITDA | Different defined terms | Covenant definition not supplied | Keep the two separate | Headroom stays attributed |
| Minor | CP-2 | Guidance-based sensitivity mixes company non-GAAP definitions with guidance | Assumes debt funding of the shortfall; excludes equity, working capital and asset sale proceeds | None | Keep the sensitivity labelled indicative | Does not change the credit view |

#### Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-1A, CP-2 | ABL secured on essentially all assets; notes senior unsecured; issuer is Kodiak Gas Services, LLC; guarantors unnamed | Credit agreement, indentures, guarantor schedules | Documents not supplied; statements rest on filing summaries | Add executed documents | Yes: counsel review of guarantees, security and restrictions |
| Material | CP-1, CP-2 | Covenant package: maximum Leverage Ratio 5.25 to 1.00, secured maximum 3.25 to 1.00, minimum coverage 2.5x, amended calculation through June 30, 2026 | ABL credit agreement and Fifth Amendment | Definitions and current levels not supplied | Add documents | Yes |
| Minor | CP-1A | Registration rights and stockholder agreements with the former sponsor remain on exhibit lists | The agreements and any termination notice | Status after the exit not stated | Add documents | Yes |

#### Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | No relative value, pricing, ratings or peer claim is made in any handoff | Quotes, ratings, peers, market capitalisation (context fields blank) | Not supplied, and not required for this snapshot | Supply if relative value is wanted | None on the snapshot; no market-implied view available |

#### Cross-module consistency and version-control audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-0, CP-1A | Sponsor holdings: CP-0 said current holdings were not stated; the 10-K states ownership fell to zero by December 2, 2025 (S1 page:25, page:63) | CP-0 cannot be edited; correction sits in CP-1A | Use the CP-1A statement | Corrected before the synthesis; CP-2 uses the corrected statement |
| Minor | CP-1, CP-1A | Dividend condition: CP-1 said dividends require pro forma ABL availability of at least $100,000,000; the filing states it for dividends funded with ABL borrowings (S4 page:48) | CP-1 cannot be edited; correction in CP-1A | Use the CP-1A statement | CP-2 uses the narrower statement |
| Minor | CP-1, CP-1A | Power acquisition value: about USD 675.0 million at signing against 726,354 (USD thousands) at closing | Different dates and share prices | Cite by basis, as both handoffs do | None |
| Minor | CP-0, CP-1 | Total debt basis: September 2025 total includes premium; later tables exclude it; CP-1 does not use September 2025 total as a leverage input | Version of the debt table | Keep September 2025 out of leverage series | None |
| Minor | CP-0, CP-1, CP-1A | Segment basis: older annual segments against June 2026 recast | Recast comparatives only for 2025 quarter and half-year | Label basis | None |
| Minor | CP-1, CP-1A | Sales tax liability on two bases (65.8 million Texas portion; 69,635 accrued line) | Different scope | Cite both | None |

#### Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Duplication | Leverage and liquidity figures are restated in the synthesis; they match the financial base | None | None |
| Minor | CP-1A | Materiality | The unexplained rise in performance obligations is a material support for the credit view but is stated as unexplained | Seek management explanation | Committee should read the rise as unverified |
| Material | CP-1, CP-2 | Committee readiness | Covenant and structure conclusions lack primary documents | Add documents | Restricted for covenant- and structure-dependent decisions |

#### Handoff structure audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Sources statement that no source page was read again | Inaccurate for sensitivity inputs from S4 page:58 | State the exception | None |
| Minor | CP-0 | Readiness view table | No defect: the command sheet uses RUN for all four consumers, consistent with the READY_WITH_LIMITATIONS statuses | None | None |
| Minor | CP-1, CP-1A, CP-2 | Reader summary word limits and placement | Within limits and first under Findings in all three | None | None |

#### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | Minor | CP-1 | Locator | Buyout statement cited at release page:2; it is at page:5 | Correct page | None | Open |
| I-02 | Minor | CP-1 | Locator | Debt principal amounts printed on S4 page:19, cited page:20-23 | Correct page range | None | Open |
| I-03 | Minor | CP-1 | Weak locator | Management leverage ratios cited to "releases" without pages | Add pages | None | Open |
| I-04 | Minor | CP-1 | Precision | Exact thousands for 36,512, 33,349 and 6,344 not on the cited pages | Add pages | None | Open |
| I-05 | Minor | CP-1 | Weak lineage | Chart rows lack row-level page locators | Add locators | None | Open |
| I-06 | Minor | CP-1A | Locator | 224 thousand preferred shares cited at page:26; printed at page:9 and page:35 | Correct page | None | Open |
| I-07 | Minor | CP-0 | Quotation | Footnote marker omitted in a release headline quotation | Restore marker | None | Open |
| I-08 | Material | CP-0 | Factual | Sponsor holdings stated as not disclosed; the 10-K states zero by December 2, 2025 | Use the CP-1A correction | Cleared by correction | Closed |
| I-09 | Minor | CP-1 | Overstatement | Dividend condition stated for all dividends; applies to ABL-funded dividends | Use the CP-1A correction | Cleared by correction | Closed |
| I-10 | Minor | CP-2 | Lineage | Sensitivity inputs from S4 page:58 not in upstream text; sources note inaccurate | Cite page; carry inputs upstream | Sensitivity stays labelled inference | Open |
| I-11 | Minor | CP-1 | Definition | Debt basis delta between principal and carrying value not logged | Delta logged in this handoff: 59,928 | None | Closed |

#### Clearance decision and remediation priority

| Priority | Action | Owner | Clears |
| --- | --- | --- | --- |
| 1 | Add the ABL credit agreement, amendments and indentures to the pack | Data team | TG1, TG2, legal audit rows |
| 2 | Add power contract disclosure or later filings | Data team | TG3 |
| 3 | Add the filing for the quarter ended September 30, 2026 if dated on or before 2026-11-05 | Data team | TG5 |
| 4 | Apply the locator corrections I-01 to I-07 and I-10 in any reuse of the handoffs | Analyst | Open minor defects |

Clearance: committee use is permitted for leverage, liquidity, cash-flow and business-model conclusions as labelled, and restricted for covenant, guarantee-structure and power-visibility conclusions until the executed documents are supplied. The underlying credit conclusion of the synthesis is unchanged, and no lineage has been silently repaired.

## Calculations

Independent recomputation from the cited source figures (USD thousands unless stated). Each reproduces the upstream result.

- R1. LTM adjusted EBITDA: 715,033 + 406,938 - 355,880 = 766,091; four quarters 174,702 + 184,451 + 190,092 + 216,846 = 766,091. LTM March 2026: 715,033 + 190,092 - 177,664 = 727,461; four quarters 178,216 + 174,702 + 184,451 + 190,092 = 727,461.
- R2. Leverage on principal debt: 2,780,917 / 766,091 = 3.63x; net 2,643,364 / 766,091 = 3.45x. FY2025: 2,614,647 / 715,033 = 3.66x. Cash interest cover LTM June 2026: 766,091 / (168,716 + 103,535 - 87,075 = 185,176) = 4.14x.
- R3. Carrying-value basis (new check, canon basis): long-term debt net of issuance cost 2,720,989 plus other borrowings 4,283 = 2,725,272 (printed as total long-term debt and other borrowings, S4 page:20). 2,725,272 / 766,091 = 3.56x; (2,725,272 - 137,553) / 766,091 = 3.38x. Gross delta between principal total debt outstanding and the net carrying value: 2,780,917 - 2,720,989 = 59,928, equal to unamortized debt issuance cost 63,817 less unamortized premium 3,889. FY2025 on the same basis: (2,555,250 + 395) / 715,033 = 3.57x.
- R4. Add-backs: FY2025 unadjusted EBITDA 81,588 + 198,370 + 31,884 + 276,185 = 588,027; add-backs 127,006; total 715,033. LTM June 2026: 603,385 + 162,706 = 766,091; 162,706 / 766,091 = 21.2%; 2,780,917 / 603,385 = 4.61x.
- R5. Liquidity: 2,000,000 - 380,917 - 14,600 = 1,604,483; plus cash 137,553 = 1,742,036.
- R6. Performance obligations: 2028 or later at June 30, 2026: 436,242 + 199,853 + 141,356 + 541,048 = 1,318,499; / 2,643,245 = 49.9%.
- R7. Guidance range: 570,000 - 805,000 = (235,000); 600,000 - 725,000 = (125,000). Year-end sensitivity: best (2,643,364 + 165,958) / 860,000 = 3.27x; worst (2,643,364 + 275,958) / 830,000 = 3.52x, with the shortfalls 66,876 and 176,876 plus dividends 99,082 as stated in the synthesis.
- R8. Distributions: 159,557 + 103,968 = 263,525; less company free cash flow 229,581 = 33,944.
- R9. Cross-module numeric match: every figure in the synthesis prose matches a figure or calculation in the financial-base or business-context handoffs, except the synthesis's own calculations and the three capital-spending inputs from S4 page:58 (issue I-10).

## Gaps

The evidence gaps limiting this review are listed in the gaps ledger above (TG1 to TG7). Two limits apply to the review itself. First, the review tested the figures and quotations that the handoffs cite for their material claims (53 strings checked at their cited pages), not every figure in every table, so a non-material slip outside that set could remain. Second, no extraction fidelity review of the source text against the original filings was performed; the sources were treated as the retained text. Neither limit changes the findings above, but both bound the confidence in the review.

## Next module

No further module is selected in this run. The report should be assembled from the four accepted handoffs, with the corrections I-08 and I-09 applied where the earlier statements appear, the locator corrections I-01 to I-07 and I-10 applied to citations, and the restrictions in the clearance decision stated beside the covenant, structure and power-visibility conclusions.
