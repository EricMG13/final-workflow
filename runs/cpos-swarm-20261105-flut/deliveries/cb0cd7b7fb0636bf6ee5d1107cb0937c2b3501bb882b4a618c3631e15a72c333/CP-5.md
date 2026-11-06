# CP-5 — Evidence trace and research integrity QA: Flutter Entertainment plc (flut)

## Request

- Issuer: Flutter Entertainment plc (issuer id `flut`), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD; current period Q3 2026; prior period FY2025.
- Run: `flut-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, module CP-5 (evidence trace) with its absorbed research integrity grade. Execution: host session; the host re-read the pinned source pages, re-checked every quotation against its cited page and recomputed every derived figure in the four upstream handoffs. No provider was called.
- Scope: Top 5 credit drivers for traceability (default scope), and a full audit of all four upstream handoffs for the integrity grade. This module changes no upstream conclusion and repairs nothing silently; defects are logged with the fix they need.
- Locators are `page:N` of the pinned `.jsonl` text of each source, not printed page numbers.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_flut-20251231.htm.jsonl | b88acc6499b34409bd63bcc7ad6ada664ea0aaf382ca0ec0d2118e7c35eb580e | Source ID S1: annual report, audited FY2025 |
| 10-Q_2026-03-31_flut-20260331.htm.jsonl | 350d396101c8e01e25e223f0670d3e0363c6d230399db566cd885841329d1dbe | Source ID S2: Q1 2026 interim report |
| 10-Q_2026-06-30_flut-20260630.htm.jsonl | a6a0f970aa3d51a04b3c201b89aaae4625c229c4c7864888e69ca9462e615826 | Source ID S3: Q2 2026 interim report |
| 10-Q_2026-09-30_flut-20260930.htm.jsonl | cf209bd21d7ac9131f97943f724a2ebaf7232a79180602605a6b0908ae9a79a1 | Source ID S4: Q3 2026 interim report |
| EX-99.1_2026-05-06_d46069dex991.htm.jsonl | 5416128bf3b9f4328a754a5eff0673c01006c996c64b406795c193ccb390bdfa | Source ID S5: Q1 2026 earnings release |
| EX-99.1_2026-08-05_d127369dex991.htm.jsonl | 548ad754549966d85d0bb747ddc76468d7bd9635705b387877e25f59264aa63f | Source ID S6: Q2 2026 earnings release |
| EX-99.1_2026-11-04_d141532dex991.htm.jsonl | ec2552a07ebcbae61da4247ec9d467815436158552ee8c98ff284c26331c74c1 | Source ID S7: Q3 2026 earnings release |
| context | c092a23c8bebb5c5ed118bc16d3658aa4f2c0513c724b7304133213e545208aa | Source ID C0: user run settings; not issuer evidence |

| Handoff | Module | sha256 |
| --- | --- | --- |
| Source readiness | CP-0 | 6f50887cad81d339bbf86e29e4ef6f91bcf17a0cb9e2b4e94873f1133c5fcfda |
| Financial base | CP-1 | 66391e220a2b7cec03d544f3a1d1fc0013df4fc46ecfb1bf241b39dae37b49a9 |
| Business and transaction context | CP-1A | 91311c8b6645e8dc8bd29a154f2af8fa983f77b3bf20bcf44139fcb121915d25 |
| Fundamental credit synthesis | CP-2 | 690e79dd9d4371144c01b11085ae3dc404130560e29389759e7f51e2f9509384 |

All four handoffs were opened in full. Each carries the run identifier `flut-2026-11-05-credit_snapshot-host`, the as-of date 2026-11-05, the issuer name and the same period labels (Q3 2026, FY2025), so identity and lineage match.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The four earlier analyses are largely traceable: derived figures recompute within rounding and quotations match their sources, with one wrong locator. One material issue limits committee use: a debt ranking and guarantor statement goes beyond the filings. | Medium | Executed credit agreement, indenture and covenant definitions are not supplied, and sources are text extractions never compared with filed documents. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Leverage, interest cover, liquidity and maturity figures recompute from their cited inputs, differing only by rounding. | The headline credit metrics can be relied on as calculated measures. | High |
| One statement about shared collateral, a common guarantor group and equal ranking of funded debt goes beyond the filing wording. | Ranking and guarantor coverage stay unverified until the credit documents are seen. | Medium |
| One locator for the Brazil acquisition price cites the wrong page, and the date of the Boyd stake purchase is inferred, not stated. | These are minor citation fixes and change no conclusion. | High |
| The undrawn revolver figure may already exclude a guarantee reservation, so liquidity is 2,477 or 2,490. | The gap is small against the cushion and is disclosed. | Medium |
| All sources are text extractions never compared with filed HTML or XBRL. | Source fidelity is assumed, not tested. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 3 are calculated, 0 are assumption-based, 1 is an analyst inference, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items. Every quotation in the four handoffs exists in the pinned sources, one locator points to the wrong page, and every derived figure recomputed to within rounding. The most important provenance gap is the absence of the executed credit agreement, indenture and covenant definitions, which matters because debt ranking, guarantor coverage and covenant headroom rest on filing summaries, and it implies that committee use should be restricted on those points until the documents are reviewed.

### Source gate and module register

Module status: Ready with Limitations. All four target handoffs are present with the six required headings. The limits are that the credit documents are absent and the sources are extractions.

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | runs/cpos-swarm-20261105-flut/requests/CP-0/.../1.response.md; run flut-2026-11-05-credit_snapshot-host | Source readiness for four consumers | Filed annual and interim reports plus management releases | Six H2 headings in order; readiness view directly after reader summary | Accepted by structural check; substantive audit below | Reports all consumers ready with limitations. |
| CP-1 | runs/cpos-swarm-20261105-flut/requests/CP-1/.../1.response.md; same run | Financial base, five chart selectors | Same sources; LTM figures calculated | Six H2 headings; financial base view after reader summary; four chart tables and one metrics table | Accepted by structural check; substantive audit below | One note differs from CP-2 on the revolver reservation. |
| CP-1A | runs/cpos-swarm-20261105-flut/requests/CP-1A/.../1.response.md; same run | Business, ownership, transaction, governance | Same sources; no ownership schedule | Six H2 headings; business and transaction view after reader summary; transaction section is prose only | Accepted by structural check; substantive audit below | One wrong locator; one inferred date tagged as fact. |
| CP-2 | runs/cpos-swarm-20261105-flut/requests/CP-2/.../1.response.md; same run | Fundamental credit synthesis | Same sources plus upstream handoffs | Six H2 headings; credit view directly after reader summary; key findings and strengths and weaknesses are prose only | Accepted by structural check; substantive audit below | One ranking and guarantor statement overreaches. |

### Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_flut-20251231.htm.jsonl | Original authority: filed, audited | FY2025 with FY2024 and FY2023 | Flutter Entertainment plc and subsidiaries, consolidated | Statements, notes, debt terms, covenant text, market risk data, Fox option | Credit documents incorporated by reference, not supplied; text extraction | CP-1 statements; CP-2 debt terms |
| S2 | 10-Q_2026-03-31_flut-20260331.htm.jsonl | Original authority: filed, unaudited | Q1 2026 | Same | Statements, debt note, revolver availability | Year-to-date only | CP-1 quarterly points |
| S3 | 10-Q_2026-06-30_flut-20260630.htm.jsonl | Original authority: filed, unaudited | Q2 2026 and six months | Same | Statements, debt note, LSE delisting | Year-to-date only | CP-1 quarterly points; CP-1A timeline |
| S4 | 10-Q_2026-09-30_flut-20260930.htm.jsonl | Original authority: filed, unaudited | Q3 2026 and nine months | Same | Statements, debt note, segments, contingencies, subsequent events | Amendment described, not supplied | All modules |
| S5 | EX-99.1_2026-05-06_d46069dex991.htm.jsonl | Management release | Q1 2026 | Same | Net debt and leverage statements | Non-GAAP definitions differ from filings and debt documents | CP-1 comparison only |
| S6 | EX-99.1_2026-08-05_d127369dex991.htm.jsonl | Management release | Q2 2026 | Same | Net debt, leverage ratio, CEO transition | Same | CP-1 comparison; CP-1A profile |
| S7 | EX-99.1_2026-11-04_d141532dex991.htm.jsonl | Management release | Q3 2026 | Same | Net debt reconciliation, guidance, refinancing statement | Same; guidance is a management claim | CP-1, CP-1A, CP-2 |
| C0 | context | User settings; not issuer evidence | As of 2026-11-05 | Run settings | Currency, periods, blank ratings and quotes | Country field disagrees with filings | Run identity only |

### Top five credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage up to 5.28x total and 4.55x net debt to Adjusted EBITDA at Q3 2026 | CP-1 | Debt 12,313 and LTM Adjusted EBITDA 2,331 | Flat debt with falling earnings raises default risk and refinancing cost | Sets the credit view and covenant context | S4 `page:26`, `page:72`; S1 `page:107` | Company-defined EBITDA; covenant EBITDA not supplied |
| 2 | Interest cover down to 3.67x on cash interest | CP-1 | Cash interest paid 636 over twelve months | Debt service capacity falls while 61.9% of debt is term and revolver debt | Drives monitoring posture | S4 `page:10`; S1 `page:149`; S2 `page:7`; S3 `page:8` | Interest paid not netted for interest income |
| 3 | Liquidity of 2,477 or 2,490 and maturities extended to May 2032 | CP-1, CP-2 | Cash 1,708 and undrawn revolver 782; amendment of October 30, 2026 | Short-term liquidity and the 2028 wall decide refinancing risk | Central support for the credit view | S4 `page:5`, `page:27`, `page:42` | Post-amendment drawn revolver not printed; pro forma maturities indicative |
| 4 | UK gaming duty and the Brazil ban pressure earnings | CP-1A, CP-1 | Duty from 21% to 40%; Brazil operations ceased September 26, 2026 | Raises cost of sales and removes a revenue stream | Main cause of weaker earnings | S4 `page:48`, `page:49` | Further effects of the April 2027 betting duty not in results |
| 5 | Ranking, collateral and guarantor structure of funded debt | CP-2 | Notes first-ranking over collateral that also secures the facilities, as applicable; notes guarantors are also facility obligors | Determines creditor rights and loss sharing | Affects whether creditors share one claim | S1 `page:127`, `page:128`, `page:189` | Credit documents not supplied; CP-2 wording goes further than the filings |

### Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt to Adjusted EBITDA of 5.28x and net debt to Adjusted EBITDA of 4.55x | CP-1 | Debt, cash and Adjusted EBITDA from S4, S1 and S2/S3 comparatives | Yes | Filed statements plus management non-GAAP | Calculated | Supported (recomputed) | High | Committee-Ready |
| Cash interest cover of 3.67x | CP-1 | Cash interest paid from S1 and S4; Adjusted EBITDA as above | Yes | Filed cash flow statements | Calculated | Supported (recomputed) | High | Committee-Ready |
| Liquidity of 2,477 and maturities extended to 2032 | CP-1, CP-2 | Cash, undrawn revolver, amendment note | Yes | Filed note; amendment document not supplied | Calculated | Supported with the revolver reservation ambiguity | Medium | Remediation Needed |
| UK duty and Brazil ban as the main earnings pressure | CP-1A | S4 business environment and segment notes | Yes | Filed MD&A | Directly Sourced | Supported | High | Committee-Ready |
| Funded debt ranks first lien on the same collateral and guarantor group, sharing one pool | CP-2 | S1 describes first-ranking security over collateral that also secures the facilities "as applicable" and guarantors who are also facility obligors | Partial | Filed summary of executed documents | Analyst Inference | Partially Supported | Medium | Remediation Needed |

### Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 12,313 and current portion 170 at September 30, 2026 | runs/cpos-swarm-20261105-flut/source-text/ | 10-Q_2026-09-30_flut-20260930.htm.jsonl | S4 | `page:26`, Note 12 | CP-1 metrics table | Sourced | Filed, unaudited | Carrying value net of issuance costs. |
| Unrestricted cash 1,708 | same | same | S4 | `page:5` | CP-1 metrics table | Sourced | Filed, unaudited | Excludes restricted and player deposit cash. |
| Adjusted EBITDA 1,499 (nine months 2026) and 2,013 (2025) | same | same | S4 | `page:72` | CP-1 metrics table | Sourced | Filed, unaudited; non-GAAP | Company definition. |
| FY2025 Adjusted EBITDA 2,845 and FY2024 2,357 | same | 10-K_2025-12-31_flut-20251231.htm.jsonl | S1 | `page:107` | CP-1 metrics table | Sourced | Filed, audited statements; non-GAAP measure | Revised definition from 2024. |
| LTM Adjusted EBITDA 2,331 | same | S1 and S4 files | S1, S4 | `page:107`, `page:72` | CP-1 metrics and chart tables | Calculated | Derived | 2,845 − 2,013 + 1,499. |
| Cash interest paid 426, 321, 531, 462 | same | S4 and S1 files | S4, S1 | `page:10`, `page:149` | CP-1 metrics table | Sourced | Filed | Supplemental cash flow line. |
| Undrawn revolver 782 (£590 million) and 13 reservation | same | S4 file | S4 | `page:27` | CP-1 and CP-2 liquidity | Sourced | Filed | Reservation wording ambiguous. |
| Liquidity 2,477 and 2,490 | same | S4 file | S4 | `page:5`, `page:27` | CP-2 liquidity table | Calculated | Derived | Sum of cash and undrawn revolver, less 13 or not. |
| Amendment of October 30, 2026: maturity May 3, 2032, revolver 1.86 billion, covenant 5.70:1.00, margin 1.40% to 2.00% | same | S4 file | S4 | `page:42`, Note 17 | CP-1A, CP-2 | Sourced | Filed note on an executed document | Document not supplied. |
| Maturity table: 13, 52, 2,681, 1,143, 3,692, 4,696 | same | S4 file | S4 | `page:26` | CP-1 chart, CP-2 | Sourced | Filed | Pre-amendment. |
| Indicative 2028 residual of about 51 | same | S4 file | S4 | `page:26` | CP-2 maturity table | Calculated | Derived | Analyst reading. |
| Credit agreement margins: TLA 1.75%, TLB 2030 1.75%, TLB 2032 2.00% | same | S1 file | S1 | `page:126`, `page:127` | CP-2 debt table | Sourced | Filed | As of December 31, 2025; later changes not shown. |
| Notes: 5.875%, 4.000%, 6.125% due 2031; 6.375%, 5.000% due 2029; issuer Flutter Treasury DAC | same | S1 file | S1 | `page:128` | CP-2 debt table | Sourced | Filed | Maturity months not printed. |
| Net total leverage covenant not greater than 5.20:1 | same | S1 file | S1 | `page:128` | CP-1, CP-2 | Sourced | Filed summary | Ratio values not printed. |
| UK remote gaming duty 21% to 40% from April 2026 | same | S4 file | S4 | `page:48` | CP-1A, CP-2 | Sourced | Filed MD&A | Betting duty rise in April 2027. |
| Brazil operations ceased September 26, 2026 | same | S4 file | S4 | `page:49` | CP-1A, CP-2 | Sourced | Filed MD&A | Impairment 873 at `page:16`. |
| US 43% and International 57% of FY2025 revenue | same | S1 file | S1 | `page:11` | CP-1A | Sourced | Filed | Percentages as printed. |
| Fox option price 4.8 billion at December 31, 2025; exercise until December 2030 | same | S1 file | S1 | `page:29`, `page:132` | CP-1A, CP-2 | Sourced | Filed summary | Option agreement not supplied. |
| Fox option liability 100 at September 30, 2026 | same | S4 file | S4 | `page:33` | CP-1A, CP-2 | Sourced | Filed | Management valuation. |
| Fast Code provision 109; GST demand 527 and provision 54; IRS 181 | same | S4 file | S4 | `page:40`, `page:41` | CP-2 claims table | Sourced | Filed | Gross claims, not loss estimates. |
| Release net debt 10,656 and leverage ratio 4.6x | same | S7 file | S7 | `page:11`, `page:26` | CP-1, CP-2 | Sourced | Management release | Different definition from CP-1 net debt. |
| Notes fair values 2,074, 1,479, 891 | same | S4 file | S4 | `page:32` | CP-2 | Sourced | Filed | Quoted market prices per the note. |
| Unhedged floating debt 6,629; 100 basis points adds 61 | same | S1 file | S1 | `page:140` | CP-2 | Sourced | Filed | December 31, 2025 basis. |
| Sterling revolver arithmetic: 1,100 − drawn − 10 = undrawn | same | S1, S2, S3, S4 files | S1, S2, S3, S4 | `page:126`, `page:19`, `page:22`, `page:26`, `page:27` | CP-2 | Calculated | Derived | Commitment £1.10 billion assumed unchanged. |
| Funded debt shares one collateral pool and guarantor group | same | S1 file | S1 | `page:128`, `page:189` | CP-2 key findings and reader summary | Inference | Filed summary read beyond its wording | See ISS-001. |
| Boyd 5% stake acquired in the third quarter of 2025 | same | S1, S4 files | S1, S4 | `page:9`; `page:9` | CP-1A timeline | Inference | Filed | Date inferred from the 2025 third-quarter financing line; see ISS-004. |
| New CEO from October 1, 2026 | same | S6 file | S6 | `page:1` | CP-1A profile | Sourced | Management release | Tagged Management Language. |
| Ownership: no sponsor or controlling holder identified | same | S1 file | S1 | `page:2` | CP-1A profile | Insufficient Information | Filed table of contents | Item 12 incorporated by reference to a proxy not supplied. |

### Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA (Q3, Q2, Q1 2026) | CP-1 charts and metrics | FY2025 2,845; comparatives and 2026 periods as printed | FY2025 − comparative + 2026: 2,331; 2,449; 2,860 | Calculated | Supported (recomputed, exact) | High | PD, leverage | S1 `page:107`; S2 `page:53`; S3 `page:66`; S4 `page:72` |
| Total and net debt to Adjusted EBITDA | CP-1 charts | Carrying debt and unrestricted cash at five dates | 12,313 / 2,331 = 5.28x; 10,605 / 2,331 = 4.55x; FY2025 4.31x and 3.67x; FY2024 2.86x and 2.21x | Calculated | Supported (recomputed, exact) | High | PD, refinancing | S1 `page:145`, `page:187`; S2 `page:19`; S3 `page:22`; S4 `page:26` |
| Cash interest cover | CP-1 charts | LTM cash interest 636, 639, 537; FY2025 531; FY2024 462 | 2,331 / 636 = 3.67x; 5.36x; 5.10x | Calculated | Supported (recomputed, exact) | High | Debt service | S1 `page:149`; S4 `page:10` |
| Free cash flow and player-fund-excluded measure | CP-1 metrics | Operating cash flow, three capital expenditure lines, two player deposit lines | 1,332 − 817 = 515; 1,136 − 817 = 319 | Calculated | Supported (recomputed, exact) | High | Cash conversion | S1 `page:148`; S4 `page:9` |
| Liquidity | CP-2 | Cash 1,708; undrawn revolver 782; reservation 13 | 1,708 + 782 = 2,490; less 13 = 2,477 | Calculated | Supported; reservation treatment ambiguous | Medium | Liquidity | S4 `page:5`, `page:27` |
| Sterling revolver arithmetic | CP-2 | £1.10 billion commitment, drawn amounts, £10 million reservation | 1,100 − 400 − 10 = 690; 1,100 − 195 − 10 = 895; 1,100 − 275 − 10 = 815; 1,100 − 500 − 10 = 590 | Calculated | Supported (four dates agree with printed figures) | High | Liquidity | S1 `page:126`; S2 `page:19`; S3 `page:22`; S4 `page:26`, `page:27` |
| Facility change from the amendment | CP-2 | Revolver 1,458 to 1,860; term A 1,967 to about 1,807 | +402 − 160 = +242 against release approximately 240 | Calculated | Assumption-Based (euro rate at September 30 implied by the debt table) | Medium | Liquidity, refinancing | S4 `page:26`, `page:27`, `page:42`; S7 `page:12` |
| Indicative 2028 residual | CP-2 | Maturity table and carrying values | 2,681 − 1,967 − 663 = 51 | Calculated | Assumption-Based (carrying values stand for principal) | Medium | Refinancing | S4 `page:26` |
| Covenant gap, company basis | CP-2 | Net debt 10,605; levels 5.20 and 5.70 | 10,605 / 5.20 = 2,039.4; 10,605 / 5.70 = 1,860.5 | Calculated | Supported; rounded to 2,040 and 1,861 in CP-2 | Medium | Covenant | S1 `page:128`; S4 `page:42` |
| Notes fair value against carrying | CP-2 | Fair values and carrying amounts | 94.1%, 94.8%, 93.4% (2026); 100.4%, 100.2%, 99.7% (2025) | Calculated | Supported; carrying includes accrued interest | Medium | Market view | S4 `page:26`, `page:32` |
| Floating unhedged share | CP-2 | 6,629 and 12,359 | 53.6% | Calculated | Supported; December 31, 2025 basis | Medium | Interest risk | S1 `page:140`, `page:187` |
| Unprovided claims, gross | CP-2 | GST 527 less 54; IRS 181; Austrian 52; Belgian 27 | 473 + 181 + 52 + 27 = 733 | Calculated | Supported; not a loss estimate | Medium | Claims | S4 `page:39`, `page:40`, `page:41` |
| Covenant net debt / EBITDA not computed on covenant definitions | CP-1, CP-2 | Definitions not supplied | Not Calculable | Not Calculable | Insufficient Information | Medium | Covenant | S1 `page:128` |

### Unsupported-claim audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-2 | Key findings and reader summary: funded debt is "guaranteed by the same group of guarantors" and creditors "share one pool" | Partially Supported | The filing says the notes are guaranteed by the Group and certain subsidiaries who are also obligors under the facilities, and that notes security covers collateral that also secures the facilities "as applicable". It does not say the facility guarantor list equals the notes guarantor list or that ranking is equal across instruments. | Restate as "notes guarantors are also facility obligors; notes are first-ranking over collateral that also secures the facilities as applicable"; confirm in the indenture and security documents | Restricts Committee Use |
| Minor | CP-1A | Timeline row: Boyd 5% stake acquired in the third quarter of 2025, tagged Documentary Fact | Partially Supported | The date is inferred from a 2025 third-quarter financing line and the bridge draw on July 30, 2025; no sentence states the completion date. | Re-tag as Analyst Interpretation or cite a completion date | Monitoring Follow-Up |
| Minor | CP-1 | Reader summary: cash interest rose because the acquisition debt carried a full year of interest | Partially Supported | The cited sentence compares quarters; the twelve-month mechanism is a reasonable reading but is not stated. | Re-tag as Analyst Interpretation | Monitoring Follow-Up |
| Minor | CP-2 | Credit view and first reader summary row: no sizeable maturity before 2029 | Partially Supported | Relies on an indicative 2028 residual calculated from carrying values, not a reported schedule. | State as indicative in the opening paragraph | Monitoring Follow-Up |

### Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Undrawn revolver 782 described in CP-1 as including the 13 reservation; CP-2 shows the sterling arithmetic implies it is already deducted | Liquidity of 2,490 or 2,477 depending on reading | Filing wording "of which" against arithmetic of 1,100 − 500 − 10 = 590 | Confirm with the credit agreement; keep the conservative figure | Monitoring Follow-Up |
| Minor | CP-2 | Covenant gap thresholds rounded to 2,040 and 1,861 | Unrounded thresholds are 2,039.4 and 1,860.5, so the gaps are 291.6 and 470.5 against 291 and 470 stated | Rounding only | Present unrounded thresholds | Formatting / Hygiene Only |
| Minor | CP-2 | Floating share 53.6% uses December 31, 2025 principal while the credit view refers to September 30, 2026 debt | Period mismatch between numerator date and balance used in the summary | Reader summary states "about 54%" without a date | Add the date | Monitoring Follow-Up |
| Minor | CP-1 | LTM method takes 2025 comparatives as printed in 2026 filings | Segment comparatives may not be recast, so LTM segment lines mix bases | Disclosed in CP-1 and CP-0 | Keep the segment caveat attached to LTM segment lines | Monitoring Follow-Up |

### Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-2 | Equal ranking, one collateral pool and a common guarantor group for all funded debt | Indenture of April 29, 2024 with officer's certificates, the credit agreement of November 24, 2023 with amendments, and the security and guarantee documents | Only filing summaries; guarantor list and Exhibit 21.1 not supplied | Restate within the filing wording; obtain the documents | Yes: counsel review of ranking and guarantors |
| Minor | CP-2, CP-1A | Amendment terms of October 30, 2026 (maturity, covenant level, margin) | Executed First Amendment and Restatement Agreement | Described in a subsequent-event note and a release only | Obtain the agreement and compliance certificate | Yes: confirm terms |
| Minor | CP-1A | Fox option rights on exercise described as unresolved | Fox Option Term Sheet and FanDuel LLC Agreement | Only the annual report summary is supplied | Obtain the documents | Yes: confirm rights |

### Market and relative-value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Notes at about 94% of carrying value, read as market repricing | Quoted prices in percent of par with dates, and spreads | The note gives fair values in dollars and carrying values include accrued interest | Obtain quotes if a price view is needed; keep the claim qualified | Monitoring only; no relative value claim is made |
| Minor | CP-1A, CP-2 | Post-amendment margin depends on corporate ratings | Moody's, S&P and Fitch ratings | No rating is stated in any source and the context ratings field is blank | Obtain agency reports | Monitoring only |

No peer ranking, instrument recommendation or recovery conclusion appears in the four handoffs; the prohibition in the method was respected.

### Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Undrawn revolver note differs on the 13 reservation | CP-2 states the correction; CP-1 cannot be edited | Cite CP-2 for the liquidity figure | Liquidity figure of 2,477 carried forward |
| Minor | CP-0, CP-1A, CP-2 | Facility-size statements (release approximately 240 against revolver 1.86 billion) | CP-2 offers a calculation of +242 that matches; stays logged as unconfirmed | Confirm in the amended agreement | None on conclusions |
| Minor | CP-1A | Boyd stake consideration 1,553 against financing line 1,620 | Logged, not reconciled; CP-2 does not use either as a debt-funding amount | Obtain the acquisition agreement | None on conclusions |
| Minor | CP-1, CP-1A, CP-2 | Net debt: 10,605 on carrying values against 10,656 in the release | Definitions differ and are disclosed in CP-1 and used consistently thereafter | Keep both labelled | None on conclusions |

Consistent across modules: issuer name and perimeter, the period labels, the total debt of 12,313, cash of 1,708, LTM Adjusted EBITDA of 2,331, leverage of 5.28x and 4.55x, cover of 3.67x, the amendment terms and the conflicts log. Nothing in CP-1A or CP-2 contradicts CP-0.

### Duplication, materiality and committee readiness

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Duplicative content | The covenant-headroom caveat is restated in the reader summary, key findings, covenant table, risks and gaps, against the instruction to state each limitation once. | Keep one statement where it changes a conclusion | Formatting only |
| Minor | CP-1A | Duplicative content | The facility-size conflict is stated in the transaction summary, the conflicts table and the gaps. | Keep the conflicts table entry | Formatting only |
| Material | CP-2 | Committee readiness | The ranking and guarantor overreach sits in the headline reader summary, where a committee would read it first. | Fix as in the legal audit before committee use | Restricts Committee Use |

### Handoff envelope and export integrity

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Source citation for the NSX purchase price | The figure `$674 million (BRL 3,799 million)` is cited to the annual report `page:9`, where the figures appear in the reverse order; the quoted form is on Q3 10-Q `page:25` | Correct the locator | None on conclusions |
| Minor | CP-1A | Category tag on a timeline row | Documentary Fact used for an inferred date | Re-tag | None on conclusions |
| Minor | CP-1 | Category of the cash interest mechanism | Stated as fact in the reader summary | Re-tag | None on conclusions |

All four handoffs carry the six required headings once each and in order, list every source with its sha256, list every upstream handoff with its sha256, place the named view heading directly after the reader summary with prose before any table, and keep the selector sections to their required form (tables where tables are required, prose where prose only is required). No heading, hash or table defect was found.

### Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| ISS-001 | Material | CP-2 | Legal Support Gap / Ranking Overreach | Same guarantor group, one collateral pool and equal ranking stated beyond filing wording | Restate within filing wording; obtain documents | Restricts Committee Use | Open |
| ISS-002 | Minor | CP-1, CP-2 | Cross-Module Inconsistency | Revolver reservation treatment differs; CP-2 corrects and uses the conservative figure | Confirm with credit agreement | Monitoring Follow-Up | Disclosed |
| ISS-003 | Minor | CP-1A | Citation Gap | NSX price figure cited to the wrong page | Correct locator to Q3 10-Q `page:25` | Formatting / Hygiene Only | Open |
| ISS-004 | Minor | CP-1A | Partially Supported Claim | Boyd stake date inferred, tagged Documentary Fact | Re-tag or cite | Monitoring Follow-Up | Open |
| ISS-005 | Minor | CP-0, CP-1A, CP-2 | Conflicting Evidence | Facility-size statements unreconciled; reconciliation reading offered | Confirm in amended agreement | Requires Source Reconciliation | Open |
| ISS-006 | Minor | CP-1 | Partially Supported Claim | Cash interest mechanism stated as fact | Re-tag as interpretation | Monitoring Follow-Up | Open |
| ISS-007 | Minor | CP-2 | Partially Supported Claim | No sizeable maturity before 2029 rests on an indicative residual | State as indicative | Monitoring Follow-Up | Open |
| ISS-008 | Minor | CP-2 | Period Mismatch | Floating share on a December 31, 2025 basis shown without date in summary | Add date | Monitoring Follow-Up | Open |
| ISS-009 | Minor | CP-2 | Calculation (rounding) | Covenant gap thresholds rounded; gaps differ by one | Present unrounded | Formatting / Hygiene Only | Open |
| ISS-010 | Minor | All | Source Quality Limitation | Sources are text extractions, not compared with filed HTML or XBRL; disclosed in CP-0 | Spot-check key lines | Monitoring Follow-Up | Disclosed |

### Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | Funded debt shares one collateral pool and guarantor group | Read beyond the filing wording | Analyst Inference | Evidence is a filing summary; the mechanic is who shares which collateral and guarantees; the implication is that loss sharing among creditors could be misstated | Restate; obtain documents | CP-2 key findings, reader summary, strengths and weaknesses |
| Minor | Boyd stake bought in the third quarter of 2025 | Date inferred | Analyst Inference | Dates order the financing narrative; an error would misplace the Boyd bridge timing | Re-tag or cite | CP-1A timeline |
| Minor | Cash interest rose because of a full year of acquisition interest | Mechanism not stated in the cited sentence | Analyst Inference | Affects how persistent the higher cash interest is judged to be | Re-tag | CP-1 reader summary |
| Minor | No sizeable maturity before 2029 | Rests on indicative calculation | Assumption-Based | Maturity wall is a refinancing driver | State as indicative | CP-2 credit view |
| Minor | Floating share about 54% | Date basis not shown in summary | Calculated | Rate sensitivity is basis-dependent | Add date | CP-2 reader summary |

### Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filings and releases cover every period; credit documents, ownership schedule and ratings are absent | Absent executed documents leave ranking, covenants and rights unverified | Committee should treat those points as unverified | Obtain credit agreement, indenture and amendment |
| Citation completeness | Ready with Remediation | Every quotation exists in the sources; one locator is wrong; two inferred statements carry the wrong category | A wrong locator slows verification but does not change a figure | No effect on conclusions | Fix ISS-003, ISS-004, ISS-006 |
| Calculation traceability | Committee-Ready | All derived figures recomputed to within rounding; formulas and inputs are shown | A mis-stated input would move leverage; none found | Leverage and cover figures can be used | None beyond rounding presentation |
| Assumption transparency | Ready with Remediation | Indicative calculations (2028 residual, facility reconciliation) are labelled as readings; the summary omits the label once | An unlabelled assumption could be read as reported | Maturity profile should be read as indicative | State indicative in the opening lines |
| Markdown/export artifact integrity | Committee-Ready | Headings, hashes, selectors and tables meet the contract | A broken heading would stop downstream use; none found | None | None |

Overall auditability is Ready with Remediation (the lowest of the five dimensions).

### Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Executed credit agreement, indenture, amendment, security and guarantee documents | No document text in the pack | Ranking, guarantors, baskets and covenant definitions cannot be verified; creditor rights could be misstated | CP-2 ranking statement; CP-2 covenants | High impact | Credit agreement, indenture, amendment, Exhibit 21.1 |
| CP-5-GAP-002 | Covenant ratio values and covenant EBITDA bridge | Not printed | Headroom is the main downside protection signal and cannot be measured | CP-1 and CP-2 covenant sections | High impact | Compliance certificate |
| CP-5-GAP-003 | Text extraction not compared with filed HTML or XBRL | No fidelity review | A transcription error in a source would flow through every module | All figures | Medium impact | Filed HTML or XBRL |
| CP-5-GAP-004 | Post-amendment drawn revolver and pro forma maturity schedule | Not printed | Liquidity and 2028 maturities after October 30, 2026 are indicative | CP-1 liquidity chart; CP-2 liquidity and maturities | Medium impact | Position at November 3, 2026 |
| CP-5-GAP-005 | Ratings and quotes | None supplied | The post-amendment margin depends on ratings; market view is limited to note fair values | CP-2 market statements | Medium impact | Agency reports; price quotes |
| CP-5-GAP-006 | Shareholder register or proxy statement | Item 12 incorporated by reference | Ownership concentration and sponsor-like influence cannot be assessed | CP-1A profile | Low impact | Proxy statement |
| CP-5-GAP-007 | Recast segment comparatives | Not supplied | LTM and trend by segment mix bases | CP-1 segment lines | Medium impact | Recast tables from the company |
| CP-5-GAP-008 | Boyd acquisition terms and date | Agreement not supplied; consideration and cash flow line differ | Funding of the Boyd stake and timing cannot be confirmed | CP-1A timeline and conflicts | Low impact | Acquisition agreement |

### Remediation priority map

1. Must-fix before committee: ISS-001 (restate the ranking, collateral and guarantor wording within the filings, and obtain the credit documents).
2. Must-fix before the handoff is consumed downstream: ISS-003 (correct the NSX locator), ISS-004 and ISS-006 (re-tag inferred statements), ISS-007 (label the maturity statement as indicative).
3. Monitoring follow-up: ISS-002, ISS-005, ISS-008 and ISS-010; obtain the amended agreement, the position after November 3, 2026, the compliance certificate and a fidelity spot-check.
4. Formatting and hygiene: ISS-009 (present unrounded covenant thresholds) and the duplicated caveats.

Remediation instructions only; no upstream analysis is rewritten here.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 1. Minor Issues: 9. Committee Use: Restricted.

No critical defect was found: no figure changes by more than rounding, no source is fabricated and no recommendation, peer ranking or recovery conclusion appears. The one material issue, ISS-001, restricts committee use of the ranking and guarantor statement, which must be disclosed as unverified until the credit documents are reviewed. QA status: Restricted. Confidence: Medium (qualitative; the numeric confidence score script is not available in host mode, so no score is stated).

## Calculations

Each derived figure in the four handoffs was recomputed from raw inputs read from the cited pages. All matched.

| ID | Quantity | Recomputation from cited inputs | Result and comparison |
| --- | --- | --- | --- |
| R1 | LTM Adjusted EBITDA, three dates | 2,845 − 2,013 + 1,499; 2,845 − 1,535 + 1,139; 2,845 − 616 + 631 | 2,331; 2,449; 2,860; match CP-1 |
| R2 | Leverage, five dates | 6,736 / 2,357; 12,266 / 2,845; 11,965 / 2,860; 11,978 / 2,449; 12,313 / 2,331; net debt over the same EBITDA with cash 1,531; 1,828; 1,512; 1,563; 1,708 | Total 2.86x; 4.31x; 4.18x; 4.89x; 5.28x. Net 2.21x; 3.67x; 3.65x; 4.25x; 4.55x. Match CP-1 |
| R3 | Cash interest cover | 2,357 / 462; 2,845 / 531; 2,860 / 537; 2,449 / 639; 2,331 / 636 | 5.10x; 5.36x; 5.33x; 3.83x; 3.67x. Match CP-1 |
| R4 | Segment and group tie | 3,124 − 279; 1,739 − 240; 2,226 − 213; quarter sums 631 + 508 + 360 and 616 + 919 + 478 | 2,845; 1,499; 2,013; 1,499; 2,013. Match CP-1 |
| R5 | Free cash flow and player-fund-excluded measure | 1,332 − 817; 1,136 − 817; 904 − 527; 756 − 487 | 515; 319; 377; 269. Match CP-1 |
| R6 | Release net debt tie | 12,313 + 77 − 26 − 1,708 | 10,656. Matches S7 `page:26` and CP-1 |
| R7 | Debt table and maturity sums | 1,370 + 431 + 166 + 663 + 3,808 + 1,234 + 579 + 540 + 981 + 1,664 + 954; 13 + 52 + 2,681 + 1,143 + 3,692 + 4,696 | 12,390; 12,277. Match |
| R8 | Liquidity | 1,708 + 782; less 13 | 2,490; 2,477. Match CP-2 |
| R9 | Sterling revolver arithmetic | 1,100 − 400 − 10; 1,100 − 195 − 10; 1,100 − 275 − 10; 1,100 − 500 − 10 | 690; 895; 815; 590. Each equals the printed undrawn amount |
| R10 | Facility change | 782 + 663 + 13 = 1,458; 1,860 − 1,458; 1,374 + 382 × 431 / 380 = 1,807; 1,967 − 1,807 | +402; −160; net +242. Match CP-2 |
| R11 | Covenant gap, company basis | 10,605 / 5.20; 10,605 / 5.70; 2,331 minus each | 2,039.4 (gap 291.6, 12.5%); 1,860.5 (gap 470.5, 20.2%). CP-2 shows 2,040 and 1,861, gaps 291 and 470: rounding only |
| R12 | Forward cover | 2,331 / 696 | 3.35x. Match |
| R13 | Notes fair value against carrying | 2,074 / 2,204; 1,479 / 1,560; 891 / 954; 2,190 / 2,181; 1,603 / 1,600; 952 / 955 | 94.1%; 94.8%; 93.4%; 100.4%; 100.2%; 99.7%. Match |
| R14 | Floating share, claims, debt mix | 6,629 / 12,359; 473 + 181 + 52 + 27; 4,718 / 12,390 | 53.6%; 733; 38.1%. Match |
| R15 | Release leverage ratios on CP-1 LTM EBITDA | 10,575 / 2,860; 10,480 / 2,449; 10,656 / 2,331 | 3.70x; 4.28x; 4.57x; round to the 3.7x, 4.3x and 4.6x printed in the releases |
| R16 | Revenue and net income LTM | 16,383 − 11,646 + 12,504; −407 − (−417) + (−1,235) | 17,241; −1,225. Match CP-1 |

Quotation check: every backticked quotation in the four handoffs was searched in the pinned source pages. All were found; the cited page was checked for each, and one locator (the NSX price figure in CP-1A) cites a page where the figures appear in a different order.

## Gaps

| Gap | Severity | Affects | Action |
| --- | --- | --- | --- |
| Executed credit documents not supplied; ISS-001 cannot be closed from the pack. | Material | Ranking, guarantors, covenants | Obtain documents; legal review of ranking. |
| Covenant ratio values not printed; headroom Not Calculable. | Material | Covenant statements | Obtain compliance certificate and EBITDA bridge. |
| Text extraction fidelity not tested against filed HTML or XBRL. | Minor | All figures | Spot-check key lines. |
| Post-amendment position (drawn revolver, maturities) not supplied. | Minor | Liquidity, maturities | Obtain the position at November 3, 2026. |
| Numeric confidence score not computed because the scoring script is not available in host mode. | Minor | QA grade | Confidence stated qualitatively as Medium. |

## Next module

CP-5 is the last selected module. CP-OS should deliver the report with the QA status of Restricted and the single material issue, ISS-001, disclosed. Before committee use, the ranking and guarantor wording in the fundamental credit synthesis should be read within the filing wording, and the next evidence action is to obtain the credit agreement, the indenture, the October 30, 2026 amendment and the covenant definitions.
