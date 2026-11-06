## Request

Module CP-5 (evidence trace validator with research integrity QA) for FS KKR Capital Corp (NYSE: FSK), credit_snapshot pathway, as of 2026-11-05 (cutoff 2026-11-05), run fsk-2026-11-05-credit_snapshot-host. It audits whether the CP-0, CP-1, CP-1A and CP-2 handoffs trace to the pinned filings, recomputes every calculation, compares the modules with one another and grades the set for committee use. Scope is the Top 5 material credit drivers; it changes no credit conclusion and rewrites no earlier analysis.

## Sources

### Issuer sources

Each source was opened at the pages cited in the lineage register. Source IDs SRC-01 to SRC-07 are used in the registers below.

| ID | Source (exact name) | sha256 (pinned file) |
| --- | --- | --- |
| SRC-01 | 10-K_2025-12-31_fsk-20251231.htm.jsonl | be99ced2da7392c013fd879201dbe6646929f936ebb77ecc5d0444caab275d72 |
| SRC-02 | 10-Q_2026-03-31_fsk-20260331.htm.jsonl | c1848df2f7f8ae50873fb96d813147e929f68a7d9fd036caac9a50ef11030183 |
| SRC-03 | 10-Q_2026-06-30_fsk-20260630.htm.jsonl | 5179e6b96937e772046c13be81daafa87748d7253056dcfc343a0e0d70e10e37 |
| SRC-04 | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | 9fd3638380d8a2268f17361ef6fc29d66f22c0391f57eb0cb6b68acb61776e4e |
| SRC-05 | EX-99.1_2026-05-10_tm2614112d1_ex99-1.htm.jsonl | 7e0c1f798df446f884320f02fed73d08f87b229f9d7b33f04d81f5473d6602e3 |
| SRC-06 | EX-99.1_2026-08-06_tm2622260d1_ex99-1.htm.jsonl | 24d1ea2d36b2f64d8b77676a71ecd16bea780f8870e6b7238b28ee023281ffd9 |
| SRC-07 | EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | 9570b8d0d4b7076e0359f3122075bc5e24c85c74b9723e31fa99d14ae3f3839b |

Run settings (dates, currency and scope only): context sha256 378a6255aee6dac53a389f9bf4cbce2419e6f8121d5d4932c50d57d1600eb13a.

### Supplied handoffs

| Module | sha256 | Role here |
| --- | --- | --- |
| CP-0 | 6fa09daba39205fb415654f095188714149fb623a5ac6f52a41f3d1dba8bb321 | Audited: source readiness |
| CP-1 | 3041d0a971deb9687f6b6c966a852ccaab08ba47aa98c5992b8b989d073887d8 | Audited: financial base |
| CP-1A | 43fb1cbbafd205e1e427477f2873b5963996f5272fadd75cdf79065e627cc3eb | Audited: business and transaction context |
| CP-2 | 5dd1f5ad0b0027717a33a1ae16e30d65c8f197f061dfc6fcb1f2c447bbcfa74e | Audited: credit synthesis |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The upstream analysis traces to the filings with remediation: every recomputed figure matched, but one earlier handoff misstated covenant levels and covenant headroom still rests on an equity definition that is not supplied. | Medium | Executed credit agreements, the borrowing base and covenant certificates are not supplied, so covenant and availability conclusions trace only to filing summaries. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 25 calculation groups in the financial and synthesis handoffs recomputed to the printed results from their stated inputs. | Reported leverage, liquidity, maturity and coverage figures can be relied on as arithmetic. | High |
| An earlier handoff said covenant levels beyond asset coverage were not printed; the filings print the revolver equity floor of 3,750.0 and a later handoff corrected it. | Covenant headroom now rests on a filing figure, but the equity definition is unsupplied, so headroom stays a proxy. | High |
| Three wording errors in earlier handoffs were corrected downstream: joint venture income attribution, the CCT Tokyo termination and a release attribution. | No figure changed; readers should use the corrected statements. | High |
| Source conflicts remain unresolved: letters of credit of 21 against 50, a Callowhill maturity of June 2 against June 3, 2030, and earnings per share of 0.27 against 0.26. | None changes a conclusion; the statement figures are used. | Medium |
| Legal and covenant claims rest on filing summaries, not executed agreements. | Committee use is restricted until the credit agreement, indentures and compliance certificate are reviewed. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 0 are directly sourced, 3 are calculated, 0 are assumption-based, 2 are analyst inferences, and 0 are weak-lineage, untraced, conflicting, or insufficient-information items; the inputs to all five are directly sourced from the filings. The most important provenance gap is that the revolver's equity definition, the borrowing base and the executed agreements are not supplied, which matters because the covenant headroom and the liquidity total depend on them and implies that committee use is restricted to the proxy basis stated in the credit view.

### Clearance decision

CLEARANCE DECISION: Pass with Remediation. Critical Issues: 0. Material Issues: 4. Minor Issues: 8. Committee Use: Restricted.

No unresolved Critical issue exists. The four Material issues are the superseded covenant statement in CP-0 (corrected in CP-1), the covenant-ordering inference in CP-2 (CP5-002), the unhedged use of borrowing-base-limited availability in the liquidity total (CP5-003) and the dependence of legal and ranking claims on filing summaries (CP5-004). Committee use needs those three open items disclosed with the proxy basis stated; the research QA status is Restricted. The numeric confidence score and the band are script-owned and are not computed in this transport.

### Remediation priority map

Must-fix before committee: None that is Critical. Disclose CP5-002 (the equity floor ordering is an inference on mixed bases), CP5-003 (availability of USD 3,197 million is subject to a borrowing base not printed) and CP5-004 (covenant, ranking and capacity statements rest on summaries); obtain the revolver credit agreement, the compliance certificate and the 2031 notes indenture to clear them.

Must-fix before the canonical handoff is consumed downstream: Consumers of CP-0 must use the CP-1 correction for CP5-001 (revolver equity floor of 3,750.0), and consumers of CP-1 must use the CP-1A corrections for CP5-005 to CP5-007.

Monitoring follow-up: CP5-011 source conflicts (letters of credit, Callowhill date, earnings per share) until the filer clarifies; the fee waiver end date after the quarter ending March 31, 2027; litigation developments; the next compliance statement for the equity floor.

Formatting and hygiene: CP5-010 (net asset walk omits repurchases in the CP-1 base view) and CP5-012 (host transport lacks the YAML envelope and the Evidence Trace and Source Registry headings).

### Analytical appendix — complete canonical registers

#### T5.1 Input module register

| Module | Handoff canonical .md / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | sha256 6fa09daba39205fb415654f095188714149fb623a5ac6f52a41f3d1dba8bb321; run fsk-2026-11-05-credit_snapshot-host | Source readiness for 7 filed sources | Primary filed documents | Six transport H2 headings present; no YAML envelope (host transport) | Restricted (one Material issue, corrected in CP-1) | Accepted by CP-OS structural check; covenant statement superseded |
| CP-1 | sha256 3041d0a971deb9687f6b6c966a852ccaab08ba47aa98c5992b8b989d073887d8; same run | Financial base, debt schedule, covenants, liquidity | Primary filed documents plus calculations | Six transport H2 headings and four chart tables present; no YAML envelope | Restricted (minor wording items corrected in CP-1A) | Accepted by CP-OS structural check |
| CP-1A | sha256 43fb1cbbafd205e1e427477f2873b5963996f5272fadd75cdf79065e627cc3eb; same run | Business, ownership, governance, transactions, litigation | Primary filed documents and management releases | Six transport H2 headings present; no YAML envelope | Passed after corrections stated in the handoff | Accepted by CP-OS structural check |
| CP-2 | sha256 5dd1f5ad0b0027717a33a1ae16e30d65c8f197f061dfc6fcb1f2c447bbcfa74e; same run | Credit synthesis from CP-1 and CP-1A | Upstream handoffs only | Six transport H2 headings present; no YAML envelope | Restricted (CP5-002, CP5-003) | Accepted by CP-OS structural check |

Module Status: Ready with Limitations (the executed legal documents and the borrowing base are not in the pack; the CP-OS receipts are the only automated check run).

#### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| SRC-01 | 10-K_2025-12-31_fsk-20251231.htm.jsonl | Audited annual report, primary | FY2025 | FS KKR Capital Corp, consolidated | Statements, Note 9, covenants, business, adviser | Text extraction; tables flattened | CP-1, CP-1A, CP-2 |
| SRC-02 | 10-Q_2026-03-31_fsk-20260331.htm.jsonl | Unaudited quarterly report, primary | Q1 2026 | Same | Statements, Note 9, Amendment No. 1 | Same | CP-1, CP-1A |
| SRC-03 | 10-Q_2026-06-30_fsk-20260630.htm.jsonl | Unaudited quarterly report, primary | Q2 2026, six months | Same | Statements, Note 9, 7.500% Notes, terminations | Same | CP-1, CP-1A |
| SRC-04 | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | Unaudited quarterly report, primary | Q3 2026, nine months | Same | Statements, Note 9, liquidity, related party, litigation | Same; one dropped date at page 167 | CP-1, CP-1A, CP-2 |
| SRC-05 | EX-99.1_2026-05-10_tm2614112d1_ex99-1.htm.jsonl | Management release, supporting | Q1 2026 (text dated May 11, 2026) | Same | Strategic actions, net debt | Management claims, non-GAAP measures | CP-1A |
| SRC-06 | EX-99.1_2026-08-06_tm2622260d1_ex99-1.htm.jsonl | Management release, supporting | Q2 2026 | Same | Leverage, liquidity, progress on actions | Same | CP-1, CP-1A |
| SRC-07 | EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | Management release, supporting | Q3 2026 | Same | Leverage, liquidity, portfolio, subsequent events | Same | CP-1, CP-1A, CP-2 |

#### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Equity cushion erosion: net asset value per share from USD 20.89 to USD 18.28, equity down USD 850 million, debt principal USD 6,337 million | CP-2 key finding 1; CP-1 | Balance sheets and Note 9 totals | The cushion beneath the debt and every equity-based test shrinks with asset marks | Drives default risk and covenant headroom | SRC-01 p165; SRC-04 p2-3, p110; SRC-07 p9 | Marks are management fair values |
| 2 | Revolver equity floor reset to USD 3,750.0 million from about USD 5,048.6 million as the nearest covenant constraint | CP-2 key finding 3; CP-1 | Amendment No. 1 text; equity from balance sheet | Equity near the old floor forced relief; headroom sets covenant risk | Governs default risk and monitoring | SRC-02 p107; SRC-03 p108; SRC-04 p3 | Equity definition and compliance figure not supplied |
| 3 | Liquidity of USD 3,308 million against USD 900 million of 2027 maturities and a USD 3,944 million 2029 to 2031 wall | CP-2 key finding 2; CP-1 | Liquidity discussion, Note 9 maturities | Determines refinancing capacity | Governs liquidity and refinancing view | SRC-04 p109-110, p141 | Borrowing base not printed |
| 4 | Net investment income coverage of common distributions: 98.1% over nine months, 95.0% in Q3 without the waiver | CP-2 key finding 4; CP-1 | Statements of operations and changes in net assets; waiver letter | Distribution and buyback cash competes with debt reduction | Governs leverage tolerance and sponsor behaviour | SRC-04 p3, p4, p77 | Waiver end date is a management-set term |
| 5 | Debt structure: USD 4,650 million of unsecured notes beside USD 1,687 million of secured debt and USD 3,134 million of revolver availability | CP-2 key finding 5; CP-1 | Note 9 table, security descriptions, 7.500% notes text | Sets ranking and priming mechanics for unsecured creditors | Governs loss given default mechanics | SRC-04 p110; SRC-01 p273; SRC-03 p108-109 | Debt incurrence limits in executed documents not supplied |

Scope: Top 5. Sponsor support and litigation (CP-2 key finding 6) are outside the ranked scope and are covered in T5.2 and T5B.6.

#### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Equity cushion erosion | CP-2 / CP-1 | Net asset value per share 20.89 and 18.28; equity 5,849 and 4,999; principal 7,620 and 6,337 | Yes | Primary filed | Calculated | Verified by recomputation | High | Committee-Ready |
| Equity floor as nearest constraint | CP-2 / CP-1 | Floor 3,750.0 from about 5,048.6 (SRC-02 p107); equity 4,999; ordering uses investments of 11,306 and rounded coverage ratios | Yes | Primary filed for the floor; proxy for the comparison | Analyst Inference | Open: definition unsupplied | Medium | Remediation Needed |
| Liquidity and maturity wall | CP-2 / CP-1 | Cash 111; availability 3,197; Note 9 maturities | Yes | Primary filed | Calculated | Verified by recomputation | Medium | Committee-Ready |
| Distribution coverage | CP-2 / CP-1 | Net investment income 127 and 366; distributions 121 and 373; waiver 12 | Yes | Primary filed | Calculated | Verified by recomputation | High | Committee-Ready |
| Secured capacity ahead of unsecured notes | CP-2 / CP-1 | Security descriptions; secured 1,687; unsecured 4,650; availability 3,134 | Yes | Primary filed summaries | Analyst Inference | Open: executed documents unsupplied | Medium | Remediation Needed |

#### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Common equity 4,999; net asset value per share 18.28; total assets 11,695 at 2026-09-30 | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:2, page:3, balance sheet | CP-1 Financials and credit metrics | Sourced | Primary | Opened; matches |
| Equity 5,849 and net asset value per share 20.89 at 2025-12-31 | source-text/10-K_2025-12-31_fsk-20251231.htm.jsonl | 10-K_2025-12-31_fsk-20251231.htm.jsonl | SRC-01 | page:165, balance sheet | CP-1 Financials | Sourced | Primary | Opened; matches |
| Debt principal 6,337 at 2026-09-30 | source-text/EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | SRC-07 | page:9, reconciliation; Note 9 total 6,487 less 150 preferred, SRC-04 page:110 | CP-1 Financials | Sourced and Calculated | Primary and supporting | Both agree |
| Debt principal 7,620 at 2025-12-31 | source-text/10-K_2025-12-31_fsk-20251231.htm.jsonl | 10-K_2025-12-31_fsk-20251231.htm.jsonl | SRC-01 | page:259, Note 9 | CP-1 Financials | Sourced | Primary | Opened; matches |
| Revolver equity floor reset to 3,750.0 from about 5,048.6; commitments to about 4,051.7 from 4,700.0 | source-text/10-Q_2026-03-31_fsk-20260331.htm.jsonl | 10-Q_2026-03-31_fsk-20260331.htm.jsonl | SRC-02 | page:107, Note 13; SRC-03 page:108 | CP-1 Covenants; CP-1A; CP-2 | Sourced | Primary | Opened in both; matches |
| Revolver financial covenants: minimum shareholders' equity and 150% asset coverage | source-text/10-K_2025-12-31_fsk-20251231.htm.jsonl | 10-K_2025-12-31_fsk-20251231.htm.jsonl | SRC-01 | page:273, Note 9 | CP-1 Covenants | Sourced | Primary summary | Summary, not clause text |
| Asset coverage 179% on debt, 177% including preferred; senior securities 6,487 | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:109, page:142-143 | CP-1 Financials | Sourced | Primary | Opened; matches |
| Cash 111 and borrowings available 3,197 at 2026-09-30; 50 of letters of credit | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:141, page:110 footnote 5 | CP-1 Liquidity | Sourced | Primary | Opened; matches |
| Restricted cash 61 excluded from the 111 | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:2, page:5 footnote 1; SRC-07 page:9 | CP-1 Definition review | Sourced | Primary | Opened; matches |
| Maturities by year (900, 750, 1,000, 1,644, 1,300, 380, 363) | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:109, Note 9 table | CP-1 Chart data: debt maturities | Calculated | Primary | Each instrument matched to its listed maturity date |
| Total investment income 294 and 888; net investment income 127 and 366; interest expense 99 and 305 | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:3 | CP-1 Financials | Sourced | Primary | Opened; matches |
| Incentive fee waiver 12 in Q3 and 23 over nine months; 50% through the quarter ending March 31, 2027, no recoupment | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:3, page:77 | CP-1A; CP-2 | Sourced | Primary | Opened; matches |
| 7.500% Notes due 2031 of 900 issued June 8, 2026; rank effectively junior to secured debt; change of control offer at 100% | source-text/10-Q_2026-06-30_fsk-20260630.htm.jsonl | 10-Q_2026-06-30_fsk-20260630.htm.jsonl | SRC-03 | page:108, page:109 | CP-1A Transaction summary | Sourced | Primary | Opened; matches |
| Convertible preferred of 150 sold to KKR Alternative Assets L.P.; two directors; change of control and six-year redemption rights | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:74, page:81-83 | CP-1A Ownership; Governance | Sourced | Primary | Opened; matches |
| Five stockholder suits; loss not estimable | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:114, page:115 | CP-1 Claims; CP-1A; CP-2 | Sourced | Primary | Opened; five matters counted |
| Joint venture: total assets 4,538.9, debt 2,330.9, 79% held; 434.0 unfunded | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:94, page:141 | CP-1A; CP-2 | Sourced | Primary | Selected data only |
| Non-accrual 3.4% of fair value and 6.4% of cost; 63.2% senior secured; first lien 58.9% | source-text/EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | SRC-07 | page:2, page:3 | CP-1; CP-1A | Sourced | Supporting (management release) | Also in SRC-04 page:130 |
| 27% secured and 73% unsecured of debt | source-text/EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | SRC-07 | page:3 | CP-1 Debt schedule | Sourced | Supporting | Agrees with the recomputed 26.6% and 73.4% |
| Interest rate swaps of 2,600 notional; 100 basis point rise adds 27 to net interest income | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:29, page:155 | CP-1; CP-2 | Sourced | Primary | Opened; matches |
| Distributions declared October 7, 2026 (0.44 and special 0.20) and repurchases to October 30, 2026 | source-text/10-Q_2026-09-30_fsk-20260930.htm.jsonl | 10-Q_2026-09-30_fsk-20260930.htm.jsonl | SRC-04 | page:75, page:123 | CP-1; CP-1A | Sourced (subsequent events) | Primary | Dated after quarter end, before cutoff |
| Management expects the portfolio to move toward more first lien exposure; net leverage within target range | source-text/EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | EX-99.1_2026-11-05_tm2628917d1_ex99-1.htm.jsonl | SRC-07 | page:1; SRC-06 page:1 | CP-1A | Management Language | Supporting | Labelled as management language; target range unquantified |
| Adviser jointly operated by KKR Credit and a Future Standard affiliate; chair and chief executive roles | source-text/10-K_2025-12-31_fsk-20251231.htm.jsonl | 10-K_2025-12-31_fsk-20251231.htm.jsonl | SRC-01 | page:6, page:7 | CP-1A Profile | Sourced | Primary | Opened; matches |

#### T5B.6 Missing-citation and weak-lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-0: covenant levels beyond asset coverage are not printed | Contradicted by SRC-02 page:107 and SRC-03 page:108, which print the floor of 3,750.0 from about 5,048.6 | Conflicting | Understating covenant disclosure would understate headroom analysis and hide the relief granted | Use the CP-1 correction; CP-0 cannot be edited | CP-0 Gaps; corrected in CP-1 |
| MATERIAL | CP-2: the equity floor is the nearest covenant constraint | Compares a floor on an undefined equity measure with a coverage ratio built from rounded inputs; the credit view states it, the Reader summary does not hedge it | Analyst Inference | A wrong ordering would misdirect monitoring from asset coverage to equity or the reverse | State it as a proxy ordering wherever used; obtain the credit agreement definition | CP-2 Key findings and Reader summary |
| MATERIAL | CP-1 and CP-2: liquidity of USD 3,308 million includes availability of USD 3,197 million | The borrowing base is not printed, so availability may be lower in practice; CP-1 discloses this, CP-2 Reader summary does not | Weak Lineage for the availability limit | Overstated liquidity would understate refinancing risk | Disclose base limit wherever the total is quoted | CP-1 Liquidity; CP-2 Reader summary |
| MATERIAL | CP-1, CP-1A and CP-2: ranking, priming capacity and the absence of creditor-adverse action | Based on filing summaries; indentures, the credit agreement and the purchase agreement are not in the pack | Insufficient Information | Recovery ranking and capacity statements need clause-level support | Obtain executed documents or keep the statements as mechanics | CP-1A Governance; CP-2 Key findings |
| MINOR | CP-1: affiliated dividend income came partly from the joint venture | The filing shows only totals by affiliation | Untraced | Misattributes income to one vehicle | Corrected in CP-1A; treat as not supplied | CP-1 Earnings and income quality |
| MINOR | CP-1: CCT Tokyo facility lapsed at its listed maturity | SRC-03 page:109 states it was terminated on June 29, 2026 | Conflicting | Wrong event date for a secured facility | Corrected in CP-1A | CP-1 Debt schedule |
| MINOR | CP-1: Q1 leverage row attributes the 138% gross ratio to the release | The 138% is printed in the Q2 release; the Q1 release prints only the net ratio | Weak Lineage | Attribution of a ratio to the wrong document | Corrected in CP-1A | CP-1 Chart data: leverage |

#### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-0 | Numeric covenant thresholds other than the 150% test are not printed | Conflicting | SRC-02 page:107 prints the floor of 3,750.0 from about 5,048.6 | Rely on the CP-1 correction | Requires Source Reconciliation |
| MATERIAL | CP-2 | The revolver equity floor is the nearest covenant constraint | Partially Supported | Inference on mixed bases; floor definition unsupplied | Label as a proxy ordering | Restricts Committee Use |
| MATERIAL | CP-2 | Liquidity of USD 3,308 million adequately covers 2027 maturities | Partially Supported | Availability is subject to a borrowing base not printed | Quote availability with its limit | Restricts Committee Use |
| MINOR | CP-1 | Affiliated dividend income of 84 included the joint venture | Unsupported | Filing gives only the affiliation totals | Corrected in CP-1A | Monitoring Follow-Up |
| MINOR | CP-1 | CCT Tokyo facility gone at its listed maturity | Partially Supported | Termination dated June 29, 2026 | Corrected in CP-1A | Monitoring Follow-Up |
| MINOR | CP-0 | Cash basis changed between Q2 and Q3 releases | Partially Supported | Restricted cash was nil at 2026-06-30, so the figures were comparable | Refined in CP-1 | Monitoring Follow-Up |
| MINOR | CP-0 | No guarantor is named for the revolver | Partially Supported | The 10-K states certain subsidiaries guarantee it, names not given (SRC-01 page:273) | Refined in CP-1 | Monitoring Follow-Up |
| MINOR | CP-1 | Net asset walk in the base view | Partially Supported | Omits repurchases of 73 from the explanation of the 850 decline | Use the CP-1 Calculations table | Formatting / Hygiene Only |
| MINOR | CP-1A and CP-2 | Management statements on strategy, intrinsic value and target leverage | Supported | Labelled Management Language and not adopted; targets unquantified | None | Monitoring Follow-Up |

#### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-1 | Debt principal to common equity (126.8% at 2026-09-30): numerator is Note 9 total less preferred, denominator common equity | Recomputed 6,337 / 4,999; release prints 127% | None | None | Monitoring Follow-Up |
| MINOR | CP-1 | Net investment income plus interest expense over interest expense (2.28x in Q3 2026) | A proxy, not EBITDA cover; labelled as such and recomputed | None | None | Monitoring Follow-Up |
| MATERIAL | CP-2 | Equity floor headroom (11.0% of investment fair value) against asset coverage fall (about 15% to 16%) | Different bases: equity measure per the credit agreement against rounded coverage ratios and investments at fair value | Floor definition not supplied | Present as a proxy ordering only | Restricts Committee Use |
| MINOR | CP-1 | Cash for liquidity excludes restricted cash in all periods (129 at Q1 against management 133) | A consistent basis disclosed in the table | Management bases differ by quarter | None | Monitoring Follow-Up |
| MINOR | CP-1 | Debt on three bases: carrying 6,231, principal 6,337, with preferred 6,487 | Definition drift risk; each is labelled | None | None | Monitoring Follow-Up |

#### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-1 | Revolver covenants: minimum shareholders' equity of 3,750.0 and 150% asset coverage | Third Amended and Restated Senior Secured Revolving Credit Agreement and Amendment No. 1 | Only filing summaries; definitions unsupplied | Review the agreement and compliance certificate | Legal review required |
| MATERIAL | CP-1A and CP-2 | The 7.500% notes rank effectively junior to secured debt and offer a change of control purchase at 100% | Sixteenth Supplemental Indenture and base indenture | Summary in the 10-Q only | Review the indenture | Legal review required |
| MATERIAL | CP-2 | Secured capacity can rank ahead of the unsecured notes, limited by the borrowing base and the asset coverage test | Debt incurrence and lien covenants of the indentures and credit agreement | Capacity to incur secured debt not supported at clause level | Keep as a mechanic until clauses are reviewed | Legal review required |
| MINOR | CP-1A | Preferred stock terms: two directors, change of control redemption, six-year redemption right | Articles Supplementary and Purchase Agreement | Summary in the 10-Q | Review the Articles Supplementary | Legal review required |
| MINOR | CP-1A and CP-2 | No priming, uptiering, collateral release or non-pro-rata exchange is documented | Executed financing documents | Absence of evidence in a limited source set, not evidence of absence | Phrase as not documented in the sources read | Legal review required |

#### T5.5 Relative value and market claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| MINOR | CP-2 | The 7.500% coupon on the 2031 notes compared with 3.400% on the notes that matured implies higher refinancing cost | Trading prices, yields and spreads of the notes and a quote date | Coupons are contractual rates at issue, not market levels | Keep as a cost-of-issue comparison, not a market view | Monitoring Follow-Up |
| MINOR | CP-1A and CP-2 | No peer ranking, relative value or instrument recommendation is made | Ratings, quotes and a comparable set | None needed because no such claim is made | None | None beyond disclosure |

#### T5.6 Cross-module consistency and version control

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| MATERIAL | CP-0, CP-1 | CP-0 says covenant thresholds are not printed; CP-1 prints the floor of 3,750.0 | CP-0 superseded by CP-1 | Consumers cite CP-1 | Covenant analysis uses CP-1 |
| MINOR | CP-1, CP-1A | CP-1 attributes affiliated dividend income partly to the joint venture; CP-1A says this is not supplied | CP-1 superseded by CP-1A | Consumers cite CP-1A | CP-2 already uses the corrected view |
| MINOR | CP-1, CP-1A | CCT Tokyo facility end date | CP-1 superseded by CP-1A | Consumers cite CP-1A | None on figures |
| MINOR | CP-1, CP-2 | Liquidity of USD 3,308 million is quoted in CP-2 without the base limit stated in CP-1 | Same figure, different caveat | Quote the caveat | Reader summary of CP-2 |
| MINOR | CP-1, CP-1A (source conflicts) | Letters of credit 21 against 50 (SRC-01 pages 271 and 261); Callowhill maturity June 2 against June 3, 2030 (SRC-01 pages 259 and 266); Q3 earnings per share 0.27 against 0.26 (SRC-04 pages 139 and 4) | Logged, not reconciled | Await filer clarification | None on conclusions |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | Issuer name, issuer id, as-of date, period labels, debt principal 6,337, equity 4,999, five suits, equity floor figures agree across all four | No issue | None | None |

#### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-1A and CP-2 | Duplicative Content | Litigation, preferred terms and the equity floor are restated in three modules | Cite the first occurrence | Longer reading, no effect on conclusions |
| MINOR | CP-1A | Promotional or Non-Credit Language | Management statements (intrinsic value, strategic value enhancement) appear but are labelled Management Language or sponsor language | None | None |
| MINOR | CP-2 | Unsupported adjectives | "Adequately protected" and "weakening" are tied to figures in the same paragraph | None | None |

#### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| MINOR | CP-0, CP-1, CP-1A, CP-2 | YAML front matter and the Evidence Trace and Source Registry headings | Host transport requires six different H2 headings, so the method's envelope is not present; the transport receipts replace it | Accept as a CP-OS transport variance | None; CP-OS recheck passes |
| MINOR | CP-1 | Chart tables | Four chart tables with plain numbers or Not supplied cells meet the launcher check | None | None |
| MINOR | All | Automated scripts | The validate, confidence score and completeness scripts of the method are not run in this transport | State plainly; score and band not computed here | Score absent from this handoff |

#### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | MATERIAL | CP-0 | Conflicting Evidence | Covenant thresholds said not printed; SRC-02 page:107 prints the equity floor | Use CP-1 | Requires Source Reconciliation | Corrected downstream in CP-1 |
| CP5-002 | MATERIAL | CP-2 | Covenant / Basket Overreach | Equity floor as nearest constraint on mixed bases and an unsupplied definition; Reader summary unhedged | State as proxy ordering | Restricts Committee Use | Open |
| CP5-003 | MATERIAL | CP-1, CP-2 | Source Quality Limitation | Liquidity total includes availability subject to a borrowing base not printed | Quote with the limit | Restricts Committee Use | Open |
| CP5-004 | MATERIAL | CP-1, CP-1A, CP-2 | Legal Support Gap | Covenant, ranking and capacity statements rest on filing summaries | Obtain executed documents | Requires Legal Review | Open |
| CP5-005 | MINOR | CP-1 | Unsupported Claim | Joint venture share of affiliated dividend income | Treat as not supplied | Monitoring Follow-Up | Corrected downstream in CP-1A |
| CP5-006 | MINOR | CP-1 | Partially Supported Claim | CCT Tokyo end date | Use termination of June 29, 2026 | Monitoring Follow-Up | Corrected downstream in CP-1A |
| CP5-007 | MINOR | CP-1 | Citation Gap | Q1 leverage row attribution | Use the Q2 release for 138% | Monitoring Follow-Up | Corrected downstream in CP-1A |
| CP5-008 | MINOR | CP-0 | Partially Supported Claim | Cash basis comparison across Q2 and Q3 | Use CP-1 definition review | Monitoring Follow-Up | Refined in CP-1 |
| CP5-009 | MINOR | CP-0 | Partially Supported Claim | Guarantor statement | Use CP-1 | Monitoring Follow-Up | Refined in CP-1 |
| CP5-010 | MINOR | CP-1 | Partially Supported Claim | Base view omits repurchases of 73 from the net asset walk | Use CP-1 Calculations | Formatting / Hygiene Only | Open |
| CP5-011 | MINOR | CP-1, CP-1A | Conflicting Evidence | Source conflicts on letters of credit, Callowhill date and earnings per share | Await filer clarification | Monitoring Follow-Up | Open |
| CP5-012 | MINOR | All | Markdown/export Consistency Defect | No YAML envelope or Evidence Trace and Source Registry headings under host transport | Accept as transport variance | Formatting / Hygiene Only | Open |

#### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source coverage | Ready with Remediation | Seven filed sources cover FY2025 to Q3 2026; no credit agreement, indenture, ratings or proxy statement | Covenant and ownership claims depend on summaries | Headroom and capacity conclusions are proxies | Obtain executed documents and the proxy statement |
| Citation completeness | Ready with Remediation | Every headline figure has a page locator and was opened; CP-2 cites handoffs by design | Missing hedges in two Reader summaries | Readers may over-read liquidity and covenant ordering | Add the caveats listed in CP5-002 and CP5-003 |
| Calculation traceability | Committee-Ready | All 25 calculation groups show inputs and formulas and recomputed to the printed results | None found | Leverage, coverage and liquidity ratios are reliable arithmetic | None |
| Assumption transparency | Ready with Remediation | The equity floor comparison and the unsecured cover use stated proxies | Proxy ordering may differ from the covenant definition | Monitoring emphasis could shift | Obtain the definition; keep the label |
| Markdown and export artifact integrity | Ready with Remediation | Six H2 headings and required tables are present; no YAML envelope | Downstream tools expecting the method's envelope would find none | No credit effect | Accept as a transport variance |

Overall auditability is the lowest of the five assessments: Ready with Remediation.

## Calculations

All 25 calculation groups used by CP-1 and CP-2 (and the calculated figures of CP-1A) were recomputed from the cited inputs on this run; each result equals the printed result after the stated rounding.

#### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| C01 Debt principal to common equity | CP-1 table; CP-2 | 7,620 and 5,849; 7,290 and 5,274; 6,491 and 5,118; 6,337 and 4,999 (principal over common equity at each period end) | principal / equity | Calculated | Verified: 130.3%, 138.2%, 126.8%, 126.8% | High | Leverage | SRC-01 p259, p165; SRC-02 p93-94, p3; SRC-03 p102, p3; SRC-04 p110, p3 |
| C02 Net debt to equity, 2026-09-30 | CP-1 | (6,337 + 150 - 111 - 105) / 4,999; with restricted cash 61 netted (6,271 - 61) / 4,999 | net debt / common equity | Calculated | Verified: 125.4% and 124.2% | High | Leverage | SRC-07 p9; SRC-04 p2 |
| C03 Debt plus preferred over equity | CP-1 | 6,487 / 4,999 | senior securities / equity | Calculated | Verified: 129.8% | High | Leverage | SRC-04 p110 |
| C04 Net asset change nine months 2026 | CP-1; CP-2 | 4,999 - 5,849; (402) - 375 - 73; 2.61 / 20.89 | difference and walk | Calculated | Verified: (850), 12.5% | High | Cushion | SRC-04 p4; SRC-01 p165 |
| C05 Debt principal reduction | CP-1; CP-2 | (7,620 - 6,337) / 7,620 | change / opening | Calculated | Verified: 16.8% | High | Deleveraging | SRC-01 p259; SRC-07 p9 |
| C06 Income and interest expense declines | CP-1; CP-2 | (1,171 - 888) / 1,171; (373 - 294) / 373; (354 - 305) / 354 | change / prior year | Calculated | Verified: 24.2%, 21.2%, 13.8% | High | Earnings | SRC-04 p3 |
| C07 Interest cover proxy | CP-1 chart; CP-2 | (NII + interest expense) / interest expense: FY2025 654, 464; Q1 117, 105; Q2 122, 101; Q3 127, 99; nine months 366, 305 | (NII + interest) / interest | Calculated | Verified: 2.41x, 2.11x, 2.21x, 2.28x, 2.20x; not EBITDA cover | High | Debt service proxy | SRC-01 p165; SRC-02 p3; SRC-03 p3; SRC-04 p3 |
| C08 Quarterly cash flow derivations | CP-1 table | Operating cash flow 1,021 - 245 and 1,425 - 1,021; interest paid 213 - 121 and 313 - 213; purchases 1,096 - 505 and 1,431 - 1,096; proceeds 2,047 - 760 and 2,693 - 2,047 | cumulative less prior cumulative | Calculated | Verified: 776, 404; 92, 100; 591, 335; 1,287, 646 | High | Cash conversion | SRC-02 p5; SRC-03 p5; SRC-04 p5 |
| C09 Q3 proceeds reconciliation | CP-1 | 442 + (310 - 106) | release sales and repayments plus fall in receivable | Calculated | Verified: 646 | High | Cash conversion | SRC-07 p1; SRC-03 p2; SRC-04 p2 |
| C10 Liquidity | CP-1; CP-2 | 111 + 3,197 (63 + 3,134) | cash + availability | Calculated | Verified: 3,308 | Medium | Liquidity | SRC-04 p141, p110 |
| C11 Unfunded commitments and cover | CP-1; CP-2 | 1,041.1 + 70.3 + 434.0; 3,308 / 1,545.4 | sum; ratio | Calculated | Verified: 1,545.4; 2.14x | Medium | Liquidity | SRC-04 p141 |
| C12 Maturities by year | CP-1 chart; CP-2 | 0, 900, 750, 1,000, 1,644, 1,300, 380, 363 | grouped by Note 9 maturity year | Calculated | Verified: total 6,337 equals release principal | High | Refinancing | SRC-04 p109-110; SRC-07 p9 |
| C13 Maturity shares and ratios | CP-2 | 900 / 6,337; (1,000 + 1,644 + 1,300) / 6,337; 3,308 / 900 | share; ratio | Calculated | Verified: 14.2%; 3,944 and 62.2%; 3.68x | Medium | Refinancing | as C12, C10 |
| C14 Secured and unsecured split | CP-1; CP-2 | secured 607 + 337 + 380 + 363; unsecured 400 + 500 + 750 + 400 + 600 + 700 + 400 + 900; each over 6,337 | sum / principal | Calculated | Verified: 1,687, 4,650; 26.6%, 73.4%; release 27% and 73% | High | Ranking | SRC-04 p110; SRC-07 p3 |
| C15 Equity floor headroom | CP-1; CP-2 | 4,999 - 3,750.0; 4,999 - 5,048.6; 1,249.0 / 4,999 | equity less floor | Assumption-Based | Verified arithmetic: 1,249.0, (49.6), 25.0%; equity definition is an assumption | Medium | Covenant | SRC-02 p107; SRC-04 p3 |
| C16 Floor headroom against investments | CP-2 | 1,249.0 / 11,306 | headroom / investments at fair value | Assumption-Based | Verified arithmetic: 11.0%; proxy basis | Medium | Covenant | SRC-04 p2 |
| C17 Asset coverage fall to 150% | CP-1; CP-2 | 1 - 1.50 / 1.77; 1 - 1.50 / 1.79 | 1 - minimum / ratio | Assumption-Based | Verified arithmetic: 15.3% and 16.2% from rounded ratios | Medium | Covenant | SRC-04 p109 |
| C18 Distribution coverage | CP-1; CP-2 | 366 / 373; 127 / 121; (127 - 12) / 121 | NII / common distributions | Calculated | Verified: 98.1%, 105.0%, 95.0% | High | Leverage tolerance | SRC-04 p3, p4 |
| C19 Per share distributions and special cost | CP-1; CP-1A | 0.48 + 0.42 + 0.44; 0.20 x 271,986,599 | sum; product | Calculated | Verified: 1.34; about 54.4 | Medium | Distribution | SRC-05 p1; SRC-06 p1; SRC-07 p1; SRC-04 p2 |
| C20 Sponsor support against equity decline | CP-2 | 150 / 850 | preferred / decline | Calculated | Verified: 17.6% | High | Sponsor alignment | SRC-04 p74, p4 |
| C21 Unsecured notes balance sheet cover | CP-2 | (11,306 - 1,687) / 4,650 | investments less secured debt over notes; a mechanic, not a recovery estimate | Assumption-Based | Verified arithmetic: 2.07x | Medium | Ranking | SRC-04 p2, p110 |
| C22 Joint venture ratios | CP-1A; CP-2 | 1,634 / 4,999; 2,330.9 / 2,065.8 | holding / equity; debt / member equity | Calculated | Verified: 32.7%; 1.13x | High | Concentration | SRC-04 p94, p130 |
| C23 Repurchases and preferred economics | CP-1A | 6,533,672 + 1,546,162; 73 + 17; 90 / 300; 25.00 x 5.00% / 4; 150 / 18.83 | sums; ratios | Calculated | Verified: 8,079,834 shares; 90; 30.0%; 0.3125; about 8.0 million shares | High | Sponsor and capital allocation | SRC-04 p75, p123, p82 |
| C24 Revolver changes | CP-1A | 4,700.0 - 4,051.7; 5,048.6 - 3,750.0; 1,298.6 / 5,048.6 | difference; ratio | Calculated | Verified: 648.3; 1,298.6; 25.7% | High | Covenant | SRC-02 p107 |
| C25 Other calculated figures | CP-1; CP-1A | Rated 3 or 4: 859 + 262, 760 + 263, 826 + 416, 888 + 221; non-cash 51 / 294; price 11.03 / 18.28 - 1; cash 124 + 5 | sums and ratios | Calculated | Verified: 1,121, 1,023, 1,242, 1,109; 17.3%; discount 39.7%; 129 | High | Asset quality, market reference | SRC-04 p135, p164, p136, p2 |

## Gaps

#### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP-5-GAP-001 | Revolver equity definition and compliance figure | Credit agreement and compliance certificate | Covenant headroom decides default proximity; the proxy may differ | CP-1 and CP-2 covenant rows | High impact | Third Amended and Restated Senior Secured Revolving Credit Agreement, Amendment No. 1, certificate |
| CP-5-GAP-002 | Borrowing base value | Borrowing base certificate | Availability of USD 3,197 million is base-limited; liquidity may be lower | Liquidity total | High impact | Revolver borrowing base reports |
| CP-5-GAP-003 | Indentures and purchase agreement | Executed documents | Ranking, incurrence limits, change of control terms and the preferred terms rest on summaries | CP-1A governance and CP-2 structure findings | Medium impact | Base and supplemental indentures, Purchase Agreement, Articles Supplementary |
| CP-5-GAP-004 | Common stock ownership and tender result | Proxy statement | Sponsor alignment and control cannot be quantified | CP-1A ownership | Medium impact | 2026 proxy statement |
| CP-5-GAP-005 | Ratings and market debt quotes | Rating reports, quotes | External view of credit and market access | CP-2 assessment | Medium impact | Rating agency reports; market data provider |
| CP-5-GAP-006 | Litigation outcome and exposure | Court filings, accrual note | Unquantified contingent claim | CP-2 risks | Medium impact | Court dockets; later filings |
| CP-5-GAP-007 | Source conflicts: letters of credit, Callowhill date, earnings per share | Filer clarification | Immaterial to conclusions but unresolved | Debt schedule footnotes | Low impact | Amended or later filings |
| CP-5-GAP-008 | Target leverage range and use of proceeds of the 2031 notes | Management disclosure | Management intent cannot be tested | CP-1A, CP-2 | Low impact | Earnings call or offering documents |
| CP-5-GAP-009 | Joint venture full statements and share of dividend income | Joint venture financial statements | Concentration and look-through cannot be measured | CP-1A, CP-2 | Low impact | Joint venture financial statements |

## Next module

No further module is selected after CP-5 in this run. The report can be assembled from the accepted handoffs, with the three open Material items (CP5-002, CP5-003, CP5-004) disclosed and the covenant, joint venture and CCT Tokyo corrections taken from CP-1 and CP-1A.
