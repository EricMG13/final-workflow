# CP-5 — Evidence trace and research integrity: SERVICE CORP INTERNATIONAL (sci)

## Request

- Issuer: SERVICE CORP INTERNATIONAL (issuer id `sci`), as of 2026-11-05, information cutoff 2026-11-05; run `sci-2026-11-05-credit_snapshot-host`, pathway credit_snapshot, current period Q3 2026, prior period FY2025, reporting currency USD.
- Scope: trace the material conclusions of the readiness (CP-0), financial base (CP-1), business context (CP-1A) and synthesis (CP-2) handoffs to the seven pinned filings and releases, recompute every derived figure, log conflicts, and grade the result. Traceability scope: Top 5 drivers plus all material claims listed in the registers.
- This module changes no upstream conclusion and repairs nothing silently; accepted handoffs cannot be edited, so each correction is stated here. Host session; no provider was called.

## Sources

Locators are `page:N` chunks of the pinned `.jsonl` text. Every locator named in this handoff was opened and the figure or wording checked on that page.

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_sci-20251231.htm.jsonl | 36f224c032003fbd2390907d9603b5b257c583b876df570b13d8b342fe4f5f00 | FY2025 annual report; audited statements and notes |
| 10-Q_2026-03-31_sci-20260331.htm.jsonl | e6b5e437aefdd3d93a7df7ee4a72da856eb2c3e8d8864dff282c77ac49311d26 | Q1 2026 quarterly report |
| 10-Q_2026-06-30_sci-20260630.htm.jsonl | 3f4554fa1a62f231e9dd455be55fe862d78b2b61391019d236799268dd70b592 | Q2 2026 quarterly report |
| 10-Q_2026-09-30_sci-20260930.htm.jsonl | 236742c90fb88a0fc6e3b830a1a819da8579c8436891d794242d5625f7bae113 | Q3 2026 quarterly report |
| EX-99.1_2026-04-29_exhibit991q126earningsrele.htm.jsonl | dc7d39675688d257986d7838f6da2271b0d5a328325d0081a47485a7f2412e53 | Q1 2026 earnings release |
| EX-99.1_2026-07-29_exhibit991q226earningsrele.htm.jsonl | 8ffbca4fd985e89d67fcf44643913b74684aa9a27e65aeca772948faf99925ff | Q2 2026 earnings release |
| EX-99.1_2026-10-28_exhibit991q326earningsrele.htm.jsonl | d5fe76c2497f82e8e53c22501a405cf8fb7df74cae0b9bd5b7f0b933f384c2b3 | Q3 2026 earnings release |
| context | 65d65475c254be68b493ea4436b1695cdda5a813079114b87a550c9ce00dd797 | Run settings; not issuer evidence |

Supplied handoffs (module, sha256):

| Module | sha256 | Run and period consumed |
| --- | --- | --- |
| CP-0 | a4424fa5ae507987bbabfc0ea081c1e6d0634859958366cc6d6a3e21db770495 | Run `sci-2026-11-05-credit_snapshot-host`; as of 2026-11-05 |
| CP-1 | b2929721b6dd1fe38c8e3fe6a91d3ab13c7f3197b5f3265b7ede5c6f6e3cdc9f | Same run; Q3 2026, nine months 2026, FY2025, FY2024, LTM to Q3 2026 |
| CP-1A | b01abf4ad8bf7d83bda476fbd5b626e74996926a7ff4ea4e5b5602e926d1af16 | Same run; business facts to September 30, 2026 and subsequent events to October 29, 2026 |
| CP-2 | dcd55d4835bd4138b4b4827282bd5b0bef71995e771217c1cfe1956c6511089c | Same run; synthesis as of 2026-11-05 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The upstream figures trace to the filings and recompute correctly. One unsupported claim about note security and several loose summary phrases were found, so committee use is restricted until they are corrected downstream. | Medium | Accepted handoffs cannot be edited, and the credit agreement and indentures are not supplied, so security and ranking claims cannot be traced. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Every printed figure checked against the cited pages matched, and every derived figure recomputed. | Leverage, liquidity and debt figures can be relied on as stated, with their labelled definitions. | High |
| The financial base view calls the senior notes mostly unsecured, but the filings describe only the 2032 notes that way. | Ranking and loss given default work must not assume unsecured notes. | High |
| Estimated leverage rests on an analyst EBITDA definition and is not the covenant measure. | Headroom should be taken only from the reported covenant ratio. | Medium |
| Two source conflicts stay open: the maturity table basis and the floating-rate average. | The maturity wall and interest sensitivity carry a basis caveat. | Medium |
| Some reader summaries use loose wording on liquidity, concentration and maturities. | Readers should rely on the detailed sections, not the summary wording. | Medium |

### Evidence trace view

The upstream analysis is largely traceable to the filings, with one material wording defect. Of 16 material claims traced, 6 are directly sourced, 4 calculated, 1 assumption-based, 2 analyst inference, 1 weak lineage and 2 conflicting. Every printed figure checked on its cited page matched, and every derived figure recomputed. The weak claim is the financial base view's description of the senior notes as mostly unsecured, which the filings state only for the 2032 notes, so ranking and recovery work must not rely on it. The two conflicting claims, the maturity table basis and the floating-rate average, are preserved as logged. Committee use is Restricted, with confidence 52 and band Low. The most important remediation is supplying the credit agreement and indentures.

### Traceability summary

| Measure | Result | Register |
| --- | --- | --- |
| Material claims traced | 16 | T5B.3 |
| Directly sourced or calculated | 10 | T5B.3 |
| Assumption-based or analyst inference | 3 | T5B.3 |
| Weak lineage or conflicting | 3 | T5B.3 |
| Findings open | 1 material, 5 minor, plus 1 logged source conflict | T5.9 |
| Committee status | Restricted | T5.9 |

### Analytical appendix — complete canonical registers

#### T5B.1 Source register

Module Status: Ready with Limitations (all seven pinned sources and four handoffs available; credit documents and ratings not supplied). Traceability Scope: Top 5 drivers plus the material claims in T5B.3. Entity key: issuer_id `sci`.

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_sci-20251231.htm.jsonl | Primary, filed, audited | FY2025, FY2024, FY2023 | SERVICE CORPORATION INTERNATIONAL, consolidated | Statements, debt note, leases, pension, covenant table, maturities, business | Text extraction; exhibits by reference only | CP-1, CP-1A, CP-2 |
| S2 | 10-Q_2026-03-31_sci-20260331.htm.jsonl | Primary, filed, unaudited | Q1 2026 | Same consolidated perimeter | Statements, debt, covenant, liquidity | Text extraction | CP-1 |
| S3 | 10-Q_2026-06-30_sci-20260630.htm.jsonl | Primary, filed, unaudited | Q2 and six months 2026 | Same | Statements, debt, covenant, liquidity | Text extraction | CP-1 |
| S4 | 10-Q_2026-09-30_sci-20260930.htm.jsonl | Primary, filed, unaudited | Q3 and nine months 2026 | Same | Statements, debt, covenant, segments, backlog, subsequent events | Text extraction; no printed signature date | CP-1, CP-1A, CP-2 |
| S5 | EX-99.1_2026-04-29_exhibit991q126earningsrele.htm.jsonl | Issuer release, unaudited, management-prepared | Q1 2026 | Same, issuer presentation | Results, outlook | Management claims; 10-Q controls | CP-1A |
| S6 | EX-99.1_2026-07-29_exhibit991q226earningsrele.htm.jsonl | Issuer release, unaudited, management-prepared | Q2 2026 | Same | Results, prior outlook | Management claims | CP-1A, CP-2 |
| S7 | EX-99.1_2026-10-28_exhibit991q326earningsrele.htm.jsonl | Issuer release, unaudited, management-prepared | Q3 2026 | Same | Results, discrete Q3 operating cash flow and capex, revised outlook | Management claims; non-GAAP measures | CP-1, CP-1A, CP-2 |
| S8 | context | Run settings, not issuer evidence | As of 2026-11-05 | Issuer identity and period labels | Identity, currency, periods | Ratings, quotes, deal terms, peers blank | All modules |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Liquidity and near-term maturities | CP-1 | Cash 172,653 thousand and revolver capacity 1,513.7 million US dollars at September 30, 2026; current maturities 195,060 thousand | Covers the April 2027 and December 2027 notes without market access | Refinancing and debt service risk is low in the next twelve months | S4 page:7, page:18 | Part of cash encumbered; amount not given |
| 2 | Leverage against the covenant | CP-1 | Reported covenant ratio 3.69 against 5.00 maximum; analyst gross 4.15x and net 4.01x | A leverage covenant is the only financial maintenance test described | Headroom is wide as reported; analyst ratio cannot be tied to it | S4 page:25; S1 page:72; S4 page:8 | Covenant definition and EBITDA not supplied |
| 3 | Operating margin and funeral volume | CP-1 and CP-1A | Gross margin 25.2% against 25.9% for nine months; funeral gross profit down 5.5%; outlook lowered | Fixed-cost base amplifies volume loss | Coverage could ease; cash generation still positive | S4 page:6, page:21, page:43; S7 page:4 | Cost drivers described by management only |
| 4 | Shareholder distributions against free cash flow | CP-1A and CP-2 | Dividends and buybacks 644,586 thousand against operating cash flow less capex 554,245 thousand in FY2025 | Discretionary use of cash drives leverage drift | Policy risk without a sponsor commitment | S1 page:72 to page:73; S4 page:8 | Payment restrictions in the credit agreement not supplied |
| 5 | Preneed backlog and funding structure | CP-1A | Total backlog 17.72 billion US dollars; insurance and other funded 9.15 billion | Revenue visibility, with off-balance-sheet insurance funding | Supports durability of revenue, not margin | S4 page:31 | Backlog is revenue not yet recognised; cash received can lag |

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| M1 Cash and undrawn revolver capacity at September 30, 2026 | CP-1 | "$ 172,653" cash, "$1,513.7 million in borrowing capacity" | Yes | Primary, filed | Directly Sourced | Supported | High | Committee-Ready |
| M2 Liquidity of 1,686.4 million US dollars | CP-1, CP-2 | Sum of M1 components | Yes | Primary inputs | Calculated | Recomputed | High | Committee-Ready |
| M3 Total debt 5,172,948 thousand and instrument register | CP-1 | Debt table with "Total debt 5,172,948" | Yes | Primary, filed | Directly Sourced | Supported | High | Committee-Ready |
| M4 Reported covenant leverage 3.69 against 5.00 maximum | CP-1, CP-2 | "Leverage ratio 5.00 (Max) 3.69" | Yes | Primary, filed | Directly Sourced | Supported; definition not supplied | Medium | Committee-Ready |
| M5 Analyst leverage 4.15x gross, 4.01x net | CP-1, CP-2 | Operating income plus two printed amortization lines | Yes | Derived from primary inputs | Assumption-Based | Recomputed; definition is analyst-chosen | Medium | Remediation Needed |
| M6 Annual maturity ladder | CP-1 | Table captioned as excluding issuance costs totals the net carrying amount | Yes | Primary, filed | Conflicting | Preserved as logged | Low | Remediation Needed |
| M7 Floating-rate cost | CP-1, CP-1A, CP-2 | 4.1% average against 5.68% debt-note rate | Yes | Primary, filed | Conflicting | Preserved as logged | Low | Remediation Needed |
| M8 Nine-month margin and segment trend | CP-1, CP-2 | Segment table and gross profit | Yes | Primary, filed | Calculated | Recomputed | High | Committee-Ready |
| M9 Outlook lowered on October 28, 2026 | CP-1, CP-1A, CP-2 | "now expected to be $3.94 to $4.04" against "$4.10 to $4.30" | Yes | Issuer release | Directly Sourced | Management Language, accurately quoted | Medium | Committee-Ready |
| M10 Preneed backlog 17.72 billion US dollars | CP-1A, CP-2 | Backlog table "Total backlog of deferred revenue $ 17.72" | Yes | Primary, filed | Directly Sourced | Supported | High | Committee-Ready |
| M11 FY2025 distributions exceeded operating cash flow less capex | CP-1A, CP-2 | Cash flow statement lines | Yes | Derived from primary inputs | Calculated | Recomputed | High | Committee-Ready |
| M12 Behaviour category Neutral or Mixed | CP-1A | Documented distributions and debt movement | Yes | Analyst reading of primary inputs | Analyst Inference | Labelled as interpretation | Medium | Committee-Ready |
| M13 32.2% of locations in California, Texas and Florida | CP-1A, CP-2 | Location table counts | Yes | Primary inputs | Calculated | Recomputed; revenue share not supplied | Medium | Committee-Ready |
| M14 Senior notes described as mostly unsecured | CP-1 | Only the 2032 notes are called "unsecured" | Partial | Primary, filed | Weak Lineage | Unsupported for the other series | Low | Remediation Needed |
| M15 Fundamental credit view and thesis | CP-2 | Synthesis of M1 to M13 | Yes | Analyst synthesis | Analyst Inference | Labelled as interpretation | Medium | Committee-Ready |
| M16 Surety bonds and the 258.7 million US dollar trust-funding exposure | CP-1A, CP-2 | "fund approximately $258.7 million into state-mandated trust accounts" | Yes | Primary, filed | Directly Sourced | Supported | High | Committee-Ready |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents 172,653 thousand at September 30, 2026 | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:7 | CP-1 financials table | Sourced | Primary, filed | Matches the balance sheet |
| Borrowing capacity 1,513.7 million US dollars and letters of credit 1.3 million | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:18 | CP-1 liquidity table | Sourced | Primary, filed | Equals 1,750.0 less 235.0 less 1.3 |
| Total debt 5,172,948 thousand | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:18 | CP-1 debt register | Sourced | Primary, filed | Net of issuance costs 32,405 |
| Covenant 3.69 against 5.00 maximum | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:25 | CP-1 liquidity table | Sourced | Primary, filed | Definition not supplied |
| Current maturities 195,060 thousand | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:7, page:18 | CP-1 chart data | Sourced | Primary, filed | Includes 7.500% notes due April 2027 |
| Operating income 978,087, depreciation and amortization 219,654, amortization of intangibles 16,370 for FY2025 | source-text | 10-K_2025-12-31_sci-20251231.htm.jsonl | S1 | page:71, page:72 | CP-1 EBITDA estimate | Sourced | Primary, audited | Inputs to analyst EBITDA |
| Nine-month 2026 depreciation and amortization 172,429 and intangibles 10,465 | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:8 | CP-1 EBITDA estimate | Sourced | Primary, filed | Inputs to LTM |
| Cash interest 162.9 million and 159.5 million for nine months | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:18 | CP-1 interest cover | Sourced | Primary, filed | Rounded to 0.1 million |
| Maturity table total 5,139,817 thousand | source-text | 10-K_2025-12-31_sci-20251231.htm.jsonl | S1 | page:100, page:101 | CP-1 maturity chart | Conflicting | Primary, audited | Caption and amount disagree |
| Floating-rate average 4.1% | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:46 | CP-1 reconciliation | Conflicting | Primary, filed | Against 5.68% at page:18 |
| Floating debt rate 5.68% | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:18 | CP-1 debt register | Sourced | Primary, filed | Debt note |
| 5.750% notes due October 2032 described as unsecured | source-text | 10-K_2025-12-31_sci-20251231.htm.jsonl | S1 | page:102 | CP-1A transaction summary | Sourced | Primary, audited | Only series with a security statement |
| Surety and 258.7 million US dollar trust funding | source-text | 10-K_2025-12-31_sci-20251231.htm.jsonl | S1 | page:26 | CP-1A operating model | Sourced | Primary, audited | December 31, 2025 date |
| 1,491 funeral locations and 506 cemeteries | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:24 | CP-1A operating model | Sourced | Primary, filed | 317 combination locations |
| California 209, Florida 201 and Texas 229 locations of 1,985 | source-text | 10-K_2025-12-31_sci-20251231.htm.jsonl | S1 | page:11 | CP-1A concentration row | Sourced | Primary, audited | December 31, 2025 |
| Dividends 145,421 and buybacks 318,942 thousand, nine months 2026 | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:8 | CP-1 financials table | Sourced | Primary, filed | Cash flow statement |
| FY2025 dividends 183,571 and buybacks 461,015 thousand | source-text | 10-K_2025-12-31_sci-20251231.htm.jsonl | S1 | page:73 | CP-1A distributions row | Sourced | Primary, audited | Cash flow statement |
| Net debt repayments 70.7 million US dollars, nine months 2026 | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:28 | CP-1A distributions row | Sourced | Primary, filed | Management discussion |
| Funeral gross profit 349,185 against 369,554; cemetery 483,040 against 458,844 | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:21 | CP-1A mix; CP-2 findings | Sourced | Primary, filed | Segment note |
| Fair value of debt instruments 4,833,217 thousand | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:19 | CP-2 summary | Sourced | Primary, filed | Level 2 and Level 3 estimates |
| Outlook 3.94 to 4.04 against 4.10 to 4.30 | source-text | EX-99.1_2026-10-28_exhibit991q326earningsrele.htm.jsonl | S7 | page:4 | CP-1A timeline | Sourced | Issuer release | Prior range in S6 page:4 |
| Backlog 17.72 billion US dollars | source-text | 10-Q_2026-09-30_sci-20260930.htm.jsonl | S4 | page:31 | CP-1A operating model | Sourced | Primary, filed | Table in billions |

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| EBITDA estimate, LTM to Q3 2026 = 1,246,945 thousand | CP-1 C1 and C2; CP-2 | Operating income, depreciation and amortization, amortization of intangibles | FY2025 plus nine months 2026 less nine months 2025; 1,214,111 + 911,186 - 878,352 | Recomputed, matches | Assumption-Based: the definition is analyst-chosen and amortization of cemetery property is excluded | Medium | Basis for all leverage and cover ratios | S1 page:71, page:72; S4 page:6, page:8 |
| Total and net debt / EBITDA 4.15x and 4.01x | CP-1 C7; CP-2 | Total debt 5,172,948; cash 172,653; EBITDA 1,246,945 | 5,172,948 / 1,246,945; 5,000,295 / 1,246,945 | Recomputed, matches | Calculated | Medium | Leverage level; differs from the covenant 3.69 on an unsupplied definition | S4 page:7, page:18 |
| EBITDA / cash interest 4.87x | CP-1 C8; CP-2 | Cash interest LTM 256.301 million | 1,246,945 / 256,301 | Recomputed, matches | Calculated | Medium | Debt service capacity | S1 page:103; S4 page:18; S3 page:17 |
| Operating cash flow less capex 681,444 thousand, 13.2% of debt | CP-1 C3 and C10; CP-2 | Operating cash flow 1,082,226; capex 400,782 | 1,082,226 - 400,782; 681,444 / 5,172,948 | Recomputed, matches | Calculated | High | Cash conversion | S1 page:72; S4 page:8 |
| Discrete Q3 operating cash flow 296,849 and capex 99,454 | CP-1 C2 | Nine-month less six-month | 869,288 - 572,439; 275,047 - 175,593 | Recomputed; release prints 296.8 and 99.5 million | Calculated | High | Quarter run rate | S4 page:8; S3 page:8; S7 page:3, page:17 |
| Liquidity 1,686.4 million US dollars | CP-1 C11; CP-2 | Cash 172.653 and capacity 1,513.7 million | Sum | Recomputed, matches | Calculated | High | Near-term resilience | S4 page:7, page:18 |
| Capacity equals commitment less drawn less letters of credit at four dates | CP-1 C11 | 1,750.0 less 255.0 less 47.0, and the other three dates | Subtraction | Recomputed, matches printed capacity | Calculated | High | Confirms commitment of 1,750.0 million | S1 page:44, page:102; S2 page:17; S3 page:17; S4 page:18 |
| Floating-rate instruments 1,081,790 thousand, 20.8% of gross principal | CP-1 C11; CP-2 C4 | Term loan, revolver and headquarters facility | 735,938 + 235,000 + 110,852; divided by 5,205,353 | Recomputed, matches; the floating status of each instrument is inferred | Analyst Inference | Medium | Interest sensitivity | S4 page:18 |
| Mix and concentration percentages | CP-1A C1 and C2 | Segment revenue and gross profit; location counts | 1,838,004 / 3,307,004 and so on; 639 / 1,985 | Recomputed, matches | Calculated | High | Earnings quality; regional risk | S4 page:21; S1 page:11 |
| Distributions against free cash flow | CP-1A C3 | Dividends, buybacks, operating cash flow less capex, total debt change | 644,586 - 554,245 = 90,341; 5,139,817 - 4,835,298 = 304,519 | Recomputed, matches | Calculated | High | Funding of shareholder returns | S1 page:72, page:73, page:100 |
| Liquidity coverage of maturities 8.6x and 2.5x; notes at 94.6% of face; analyst EBITDA decline of 17.0% to reach 5.00x; 100 basis point sensitivity of 10.8 million US dollars | CP-2 C1 to C4 | Liquidity, current maturities, fair values, face values | 1,686.4 / 195.06; 3,676,913 / 3,886,924; 5,172,948 / 5.00; 1,081,790 x 1% | Recomputed, matches | Analyst Inference where definitions are analyst-chosen | Medium | Context for refinancing and rate risk, not covenant headroom | S4 page:19 |

#### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1 financial base view: "The stack is mostly unsecured senior notes" | Only the 5.750% notes due October 2032 are described as unsecured; security of the other series is not stated, and CP-1 itself lists note security as a gap | Weak Lineage | Security and ranking drive loss given default for about 3,886.9 million US dollars of notes | Treat note security as unsupported until the indentures are supplied; do not use the phrase downstream | CP-1 Financial base view |
| MINOR | CP-1 reader summary: "Liquidity is cash plus undrawn revolver capacity of 1,513.7 million US dollars" | 1,513.7 million is the undrawn capacity alone; liquidity including cash is 1,686.4 million US dollars | Weak Lineage | Reader could read liquidity as understated | Read liquidity as 1,686.4 million from the CP-1 liquidity table | CP-1 Reader summary |
| MINOR | CP-1A reader summary: "Revenue and locations are concentrated in California, Texas and Florida" | Locations are 32.2% in the three states; revenue by state is not supplied, and the 10-K says only that they are three of the largest states by revenue | Weak Lineage | Overstates the revenue concentration evidence | Read the claim as a location share plus a management risk statement | CP-1A Reader summary |
| MINOR | CP-2 reader summary: "ample liquidity and distant maturities" | The nearest maturities are 136.9 million US dollars of notes due April 2027 and 550.0 million due December 2027, within about five and thirteen months of the as-of date | Weak Lineage | Understates near-term maturity timing, though liquidity covers it | Read the detailed section: well covered, not distant | CP-2 Reader summary |
| MINOR | CP-1 debt register and CP-2 risk table state the term loan, revolver and headquarters facility as floating | The sources do not list the floating instruments; the status is inferred from rates and the Level 3 classification, as CP-1 C11 says | Analyst Inference | Interest sensitivity rests on the inference | Label as inferred wherever used | CP-1 Debt register; CP-2 risk table |
| MINOR | CP-1A operating model: other cemetery revenue "including trust fund income" cited to the 10-K segment note and Q3 10-Q segment table | The cited tables list "Other revenue" without describing it; the description is at Q3 10-Q page:40 | Weak Lineage | Locator does not carry the claim | Cite S4 page:40 for the description | CP-1A Company and operating model |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Citation coverage | Strong | Every figure in the registers carries a file and `page:N`; all locators opened and matched except the six items in T5B.6 | Missing locators would block independent recomputation | Figures can be reproduced from the filings | Correct the six flagged items downstream |
| Calculation reproducibility | Strong | All derived figures in CP-1, CP-1A and CP-2 recomputed and matched, including every LTM, discrete-quarter and ratio family | A wrong LTM would move every ratio | Leverage and cover are reliable as labelled estimates | None for arithmetic |
| Definition control | Limited | EBITDA is not printed anywhere; CP-1 builds an estimate and CP-2 reuses it with the covenant ratio shown separately | Mixing the estimate with the covenant measure would misstate headroom | Headroom must be quoted from the reported ratio only | Supply the covenant definition |
| Conflict handling | Adequate | The maturity table basis and the floating-rate average are logged in CP-1, CP-1A and CP-2 without reconciliation | An unlogged conflict would be smoothed into one number | Maturity wall and interest sensitivity carry a basis caveat | Confirm in filed HTML or with the issuer |
| Management language | Adequate | Market share, cash-flow-neutral and outlook claims are tagged Management Language in CP-1A and CP-2 | Promotional claims adopted as fact would inflate the view | Credit view does not depend on them | None |
| Legal and structural lineage | Weak | Credit agreement, indentures, guarantor and security detail are not supplied; one note-security phrase is unsupported | Ranking and creditor control cannot be traced | Loss given default analysis is not possible from these sources | Supply executed documents |

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| G1 | Covenant definition and EBITDA | Credit agreement and compliance certificate | Headroom cannot be rebuilt | Leverage estimate not comparable with 3.69 | Caps lineage of M4 and M5 | Credit agreement |
| G2 | Note security, guarantors and ranking | Indentures and guarantor schedule | Loss given default and structural position | M14 unsupported | Material finding | Senior indenture and supplements |
| G3 | Maturity table basis | Filed HTML or XBRL for the debt maturity table | Maturity wall labelled as printed | M6 conflicting | Lowers lineage | Issuer filing in HTML |
| G4 | Floating-rate average conflict | Explanation of the 4.1% average | Interest sensitivity unsettled | M7 conflicting | Lowers lineage | Issuer or filed HTML |
| G5 | Ratings and market prices | Rating reports, quotes | No external opinion to compare | CP-2 has no external anchor | Keeps view at Medium | Rating agencies, dealer quotes |
| G6 | Ownership and governance detail | 2026 proxy statement | Control rights and related parties untraced | CP-1A governance rows limited | Keeps governance at interpretation | Proxy statement |
| G7 | Revenue by state and encumbered cash | Company disclosure | Concentration and usable cash unquantified | M13 is a location share only | Medium confidence on concentration | Issuer disclosure |
| G8 | Events from October 30, 2026 to the cutoff | Later 8-Ks | New financing or rating actions | Statements limited to October 29, 2026 | Date-bound view | EDGAR filings |

#### T5.1 Module and handoff register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | Accepted CP-0 handoff; run `sci-2026-11-05-credit_snapshot-host` | Source readiness for four consumers | Primary filings, text extraction | Six canonical H2 headings present; no YAML envelope in Markdown transport | Accepted by CP-OS; one superseded gap noted | The gap on discrete quarterly cash flows is corrected by CP-1 |
| CP-1 | Accepted CP-1 handoff; same run | Financial base and charts | Primary filings | Six H2 headings, reader summary, view, chart selectors present | Accepted by CP-OS; one material and two minor findings here | Analyst EBITDA throughout |
| CP-1A | Accepted CP-1A handoff; same run | Business, ownership, behaviour, conflicts | Primary filings and releases | Six H2 headings and required selectors present | Accepted by CP-OS; two minor findings here | Management Language tagged |
| CP-2 | Accepted CP-2 handoff; same run | Credit synthesis | Upstream handoffs | Six H2 headings and required selectors present | Accepted by CP-OS; two minor findings here | Reuses CP-1 and CP-1A figures |

#### T5.2 Citation and evidence support issues

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1 | Financial base view: mostly unsecured senior notes | Weak Lineage | Security stated only for the 2032 notes | Do not rely on the phrase; obtain the indentures | Restricts committee use |
| MINOR | CP-1 | Reader summary: liquidity wording | Weak Lineage | 1,513.7 million is capacity, not liquidity including cash | Use 1,686.4 million for liquidity | Clear with note |
| MINOR | CP-1A | Reader summary: concentration of revenue | Weak Lineage | Revenue by state not supplied | Use the location share and risk statement | Clear with note |
| MINOR | CP-2 | Reader summary: distant maturities | Weak Lineage | Notes due April 2027 and December 2027 are near | Use the detailed section | Clear with note |
| MINOR | CP-1A | Revenue streams locator | Weak Lineage | Description of other revenue sits at Q3 10-Q page:40 | Cite the correct page | Clear with note |

#### T5.3 Metric, logic and definition issues

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Analyst gross and net leverage 4.15x and 4.01x | EBITDA is operating income plus depreciation and amortization plus amortization of intangibles, with no adjustment for divestiture gains, impairments or restructuring; not the covenant measure | Reported covenant ratio 3.69 is lower; cause not determinable | Keep both labelled; quote headroom from the reported ratio only | Clear with note |
| MINOR | CP-1 | Maturity ladder as printed | Caption excludes issuance costs but total equals the net carrying amount | 10-K page:100 against page:101 | Label basis; confirm in HTML | Clear with note |
| MINOR | CP-1, CP-1A, CP-2 | Floating-rate cost | Average rate and period-end rate describe different populations or one is misprinted | 4.1% at Q3 10-Q page:46 against 5.68% at page:18 | Use debt-note rates; request explanation | Clear with note |
| MINOR | CP-2 | Leverage illustration 17.0% EBITDA fall to 5.00x | Uses analyst definitions, not the covenant, as CP-2 states | None | Keep the disclaimer | Clear with note |

#### T5.4 Legal and structural claim issues

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1 | Senior notes mostly unsecured | Senior indenture and supplements | Executed indentures not supplied; one series described as unsecured | Remove or qualify the claim | Legal review of security and ranking |
| MINOR | CP-1, CP-2 | Bank credit agreement guaranteed by a majority of domestic subsidiaries with a maximum leverage covenant and dividend and repurchase restrictions | Credit agreement | Terms, guarantor list and baskets not supplied | Carry as stated in the 10-Q only | Legal review of restrictions |
| MINOR | CP-1A | Cross-default from the credit agreement to the senior indenture | Credit agreement and senior indenture | Stated in a risk factor; terms not supplied | Cite as issuer risk language | Legal review of default provisions |

#### T5.5 Market and relative-value claim issues

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | Senior notes at fair value of 94.6% of face at September 30, 2026 | Dealer quotes, spreads and yields | Fair values are issuer estimates, Level 2 for the notes | Keep the label; no spread or relative-value conclusion drawn | Context only; no instrument view |
| MINOR | CP-2 | No ratings in the sources | Rating reports | Context rating field blank | Keep ratings as not supplied | Committee must source external ratings |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1 | CP-0 listed discrete Q2 and Q3 2026 cash flows as not printed; the Q3 release prints discrete Q3 operating cash flow and capex, and CP-1 corrected this plainly | CP-0 is accepted and cannot be edited | Use CP-1; this handoff records the correction | None on figures |
| MINOR | CP-1, CP-1A, CP-2 | Floating-rate average and maturity-table conflicts logged consistently in all three | None | Keep both unreconciled | Caveat carried to CP-2 |
| MINOR | CP-1, CP-2 | The reader summaries differ in wording on liquidity and maturities; the detailed sections agree on 1,686.4 million and 195.1 million | None | Use detailed sections | None on figures |

All carried figures (leverage 4.15x and 4.01x, cover 4.87x, liquidity 1,686.4 million US dollars, distributions 644,586 against 554,245 thousand) agree across CP-1, CP-1A and CP-2. No version conflict exists: each module consumed the exact hash of its predecessors.

#### T5.7 Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1, CP-2 | Duplication | Debt, liquidity and leverage figures are repeated in CP-1 tables and CP-2 findings; they agree | None | None |
| MINOR | CP-2 | Materiality | Interest sensitivity and a leverage illustration are given; both depend on inferred or analyst definitions | Keep labelled | Low |
| MATERIAL | CP-1 | Committee readiness | The note-security phrase should not reach a committee unqualified | Qualify downstream | Restricted use |

#### T5.8 Structured export and handoff defects

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | YAML envelope | The Markdown transport carries no YAML front matter, filename check or script-run validation block | Rely on CP-OS hashes and checks | None for this run |
| MINOR | CP-1 | Chart data selectors | Maturity chart periods are year buckets with a mixed-basis caveat, not a single reporting period | Keep the basis note | Report renders as printed |
| MINOR | CP-1A, CP-2 | Selector tables | Required selector tables and prose sections are present once each | None | None |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISS-01 | MATERIAL | CP-1 | Weak lineage | Senior notes described as mostly unsecured | Qualify; obtain indentures | Restricted | Open |
| ISS-02 | MINOR | CP-1 | Weak lineage | Liquidity wording in reader summary | Use 1,686.4 million US dollars | Clear with note | Open |
| ISS-03 | MINOR | CP-1A | Weak lineage | Revenue concentration wording | Use location share | Clear with note | Open |
| ISS-04 | MINOR | CP-2 | Weak lineage | Distant maturities wording | Use detailed section | Clear with note | Open |
| ISS-05 | MINOR | CP-1, CP-2 | Inference labelled as fact | Floating status of instruments inferred | Label as inferred | Clear with note | Open |
| ISS-06 | MINOR | CP-1A | Locator | Other revenue description locator | Cite Q3 10-Q page:40 | Clear with note | Open |
| ISS-07 | MINOR | CP-0 | Version | Discrete quarterly cash flow gap superseded by CP-1 | None | None | Closed |
| ISS-08 | MINOR | CP-1, CP-1A, CP-2 | Source conflict | Maturity basis and floating-rate average | Confirm in filed HTML | Clear with note | Open (logged conflict, no penalty) |

Committee status: Restricted. QA status: Restricted. Confidence score 52, band Low.

## Calculations

- **Confidence score (script `confidence_score.py`).** Lineage of 16 material claims by strongest evidence: Directly Sourced 6, Calculated 4, Assumption-Based 1, Analyst Inference 2, Weak Lineage 1, Conflicting 2. Required fields present 17 of 17 (the 17 required registers). Source gate pass for tracing (all seven sources and four handoffs available). Findings: MATERIAL 1, MINOR 5 (ISS-02 to ISS-06). Script output: E = 70.0, C = 100.0, S = 1.0, P = 30, score = clamp((0.6 x 70 + 0.4 x 100) x 1.0 - 30) = 52, band Low, qa_status Restricted. ISS-07 is closed and ISS-08 is a logged source conflict, so neither carries a penalty.
- **Recomputation of upstream figures (each from the cited inputs).** LTM EBITDA 1,214,111 + 911,186 - 878,352 = 1,246,945 thousand. Total debt / EBITDA 5,172,948 / 1,246,945 = 4.15x; net 5,000,295 / 1,246,945 = 4.01x. Cash interest LTM 252.901 + 162.9 - 159.5 = 256.301 million; cover 1,246,945 / 256,301 = 4.87x. Liquidity 172.653 + 1,513.7 = 1,686.353 million. Distributions FY2025 183,571 + 461,015 = 644,586; less 554,245 = 90,341. Debt rise 5,139,817 - 4,835,298 = 304,519. Location share (209 + 201 + 229) / 1,985 = 32.2%. All matched the upstream figures.
- **Unsecured-note check.** The 10-K states "unsecured 5.75% Senior Notes due October 2032" (page:102); no source states security for the 7.500%, 4.625%, 5.125%, 3.375% or 4.000% series. Senior-note face value of the five unstated series: 136,924 + 550,000 + 750,000 + 850,000 + 800,000 = 3,086,924 thousand of 3,886,924 thousand in total.

## Gaps

Gaps G1 to G8 in the T5B.8 register above are the gaps of this handoff. The two that decide committee use are G2 (indentures and security detail) and G1 (covenant definition). Both belong to documents outside the supplied pack; nothing in this module can fill them.

## Next module

This is the last module in the minimum set. The report delivery should carry the Restricted status, use the detailed sections over the reader-summary wording for liquidity, concentration and maturities, and drop the unsecured description of the senior notes until the indentures are supplied.
