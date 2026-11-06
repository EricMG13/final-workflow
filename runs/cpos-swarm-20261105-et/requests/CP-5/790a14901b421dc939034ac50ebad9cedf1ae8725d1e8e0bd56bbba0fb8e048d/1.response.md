# CP-5 evidence trace and research integrity grade: Energy Transfer LP (et)

## Request

Evidence trace validation and research integrity grade (the absorbed QA phase) for Energy Transfer LP as of 2026-11-05, pathway credit_snapshot, current period Q3 2026, prior period FY2025, USD. Scope: the four accepted handoffs (source readiness, financial base, business and transaction context, fundamental credit synthesis) traced to the seven pinned issuer sources, with Top 5 traceability. Source text was re-read for this audit: the key locators were opened, the debt, liquidity and maturity claims were tested against the instrument tables, and every derived figure below was recomputed.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 |
| --- | --- |
| 10-K_2025-12-31_et-20251231.htm.jsonl | cf6ec450a74c280b3feab654167ed9d76760431021a13bf17a88d72b8532eaa7 |
| 10-Q_2026-03-31_et-20260331.htm.jsonl | 204d33e965723c9110a8bd3c410929503a162c990398e4a307e9e4585208124c |
| 10-Q_2026-06-30_et-20260630.htm.jsonl | f6fbfa69a08a1bbb53482543b3abf672768e886f0ec8d32dd533da3f97f4bf88 |
| 10-Q_2026-09-30_et-20260930.htm.jsonl | b99e2e6cdfbc85d8be8a5393c48692fdcdcd98f8ad63f20f2e4b37b17c6562f1 |
| EX-99.1_2026-05-05_ex991eterq12026.htm.jsonl | 28e020c73aad041b3d8d17b54f534d805074c7d2b4b4b027cc87b57e5e12fd7c |
| EX-99.1_2026-08-04_ex991eterq22026.htm.jsonl | ee1907b3dce0abf5f0cf3c0b28a73722fa7c995776f463ee976582a26da21fa9 |
| EX-99.1_2026-11-03_ex991eterq32026.htm.jsonl | 5531a7cf0a40c534ed0feab25ecafdebb29b6fb0df1d6b068954124b5c1f91f7 |

Run context (settings, not issuer evidence): context sha256 dfad783f6af55323b89ba2b387376722ec78e773820c07687193a91e09314cf8.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 1b2196fae78086f62479df5a2fd3f99eb6278b9f99a6e4364bc9961bc241c594 | Source readiness, gap and identity log |
| CP-1 | e1f728d8ef2389dd86a9731e74ebfa406b4f14ddfa5f40add9ef875434607923 | Financial base, charts, calculations |
| CP-1A | d60945a38b019c3f662c040f9814e52772a5d5839683a7c4acb2eb49f93eaa5c | Business, transaction, governance rows |
| CP-2 | 4a55234569dea26ef83b657d06c824d781ad9698228cf02ac03924e686341407 | Credit synthesis |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Almost every figure traces to the filings and recomputes, but one maturity comparison in the financial base was wrong and has been corrected downstream, and covenant terms and the 2026 change of state cannot be traced. Committee use is restricted. | Medium | Executed debt documents, the filing explaining the change of state and a post-2025 maturity table are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All recomputed figures reproduce, including LTM Adjusted EBITDA of 19,216 US$m, 3.58 times total debt, liquidity of 8,692 US$m and free cash flow of 6,082 US$m. | Quantitative claims in the credit view can be relied on, subject to the non-GAAP basis. | High |
| The 4,350 US$m due by September 30, 2027 was compared with the parent's 4,406 US$m of availability, but includes Sunoco LP notes; the parent portion is about 3,300 US$m. | The parent's near-term refinancing need is smaller than first stated. | Medium |
| Covenant definitions, indentures and the filing explaining the move from Delaware to Texas are not supplied, so headroom and the obligor cannot be verified. | Default triggers and structure remain unverified. | High |
| The balance sheet notes no material restricted cash, which closes a gap the financial base left open. | Cash is available to the group, but its split by borrower is still not supplied. | Medium |

### Evidence trace view

Overall, evidence traceability is Ready with Remediation. Of the Top 5 material credit drivers, 1 is directly sourced, 3 are calculated from sourced inputs, 0 are assumption-based, 0 are analyst inferences, and 1 is an insufficient-information item. The most important provenance gap is the set of executed debt documents together with the filing that explains the state and exchange change, which matters because covenant levels, guarantee structure and the identity of the obligor decide default triggers and where creditor claims sit, so committee use must stay restricted until they are obtained. The quality grade is Restricted: there are no Critical findings and four Material ones. A numeric confidence score is not asserted because the scoring routine is script-owned and was not run in this host session; the band for the handoffs together is Medium.

### T5B.1 Source register

| Source Document ID | Source Document Name | Source Quality | Period | Entity Covered | Data Supplied | Limitation | Downstream Use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K_2025-12-31_et-20251231.htm.jsonl | High (audited, filed) | FY2025 with FY2024 and FY2023 | Energy Transfer LP and subsidiaries, consolidated | Statements, debt note and instrument table, business, governance risk factors, acquisitions note | Pre-dates the 2026 change of state and exchange | Financial base, business rows, maturity table |
| S2 | 10-Q_2026-03-31_et-20260331.htm.jsonl | High (filed, unaudited) | Q1 2026 | Same | Balance sheet, debt table, facilities, covenant ratio | Delaware cover | Quarterly balances, liquidity trend |
| S3 | 10-Q_2026-06-30_et-20260630.htm.jsonl | High (filed, unaudited) | Q2 and six months 2026 | Same | Balance sheet, debt table, facilities, covenant ratio | Texas cover with NYSE listing | Quarterly balances, liquidity trend |
| S4 | 10-Q_2026-09-30_et-20260930.htm.jsonl | High (filed, unaudited) | Q3 and nine months 2026 | Same | Statements, debt note and table, segments, recent developments, litigation | Cross-references an 8-K12B not supplied; no maturity table | Debt, liquidity, transactions |
| S5 | EX-99.1_2026-05-05_ex991eterq12026.htm.jsonl | Medium (furnished release, management measures) | Q1 2026 | Same | Adjusted EBITDA reconciliation | Management non-GAAP | Quarterly Adjusted EBITDA |
| S6 | EX-99.1_2026-08-04_ex991eterq22026.htm.jsonl | Medium (furnished release) | Q2 and six months 2026 | Same | Adjusted EBITDA reconciliation | Management non-GAAP | Quarterly Adjusted EBITDA |
| S7 | EX-99.1_2026-11-03_ex991eterq32026.htm.jsonl | Medium (furnished release) | Q3 and nine months 2026 | Same | Reconciliation, Distributable Cash Flow, segments, liquidity table, guidance | Management non-GAAP and forward-looking | Adjusted EBITDA, liquidity, outlook |
| H0 | CP-0 handoff | Medium (analyst work product) | As of 2026-11-05 | Same | Readiness, gaps, identity | Source readiness only | Gap carry-forward |
| H1 | CP-1 handoff | Medium (analyst work product with derived figures) | FY2025 to Q3 2026 and LTM | Same | Financial figures, charts | Approximate LTM cash interest; stale maturity basis | Credit synthesis |
| H2 | CP-1A handoff | Medium (analyst work product) | As of 2026-11-05 | Same | Business, transaction, governance | Partnership agreement not supplied | Credit synthesis |
| H3 | CP-2 handoff | Medium (analyst work product) | As of 2026-11-05 | Same | Credit view, risks, corrections | Derived maturity split | Committee use |

Module Status: Ready with Limitations (all four handoffs and all seven sources available; executed debt documents, partnership agreement and the 8-K12B absent). Traceability Scope: Top 5. Entity key: issuer_id et available. Re-anchor: each handoff names Energy Transfer LP, the as-of date 2026-11-05, current period Q3 2026 and prior period FY2025; CP-1, CP-1A and CP-2 list the upstream hashes above and they match the run record.

### T5B.2 Top 5 material credit drivers

| Rank | Credit Driver | Originating Module | Source-Supported Basis | Why Material | Committee Relevance | Source Trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage of 3.58x total debt and 3.53x net debt on LTM Adjusted EBITDA of 19,216 US$m, down from 4.28x and 4.20x for FY2025 | CP-1, restated in CP-2 | Printed total debt and cash; issuer Adjusted EBITDA reconciliations | Earnings growth, not debt repayment, drove the fall | Leverage tolerance and default risk | S4 page:3, page:4 and page:87; S7 page:7; S1 page:187 and page:324 | Adjusted EBITDA is issuer non-GAAP; covenant ratio uses an unsupplied definition |
| 2 | Liquidity of 8,692 US$m of cash and undrawn facilities, 4,406 US$m at the parent | CP-1, CP-2 | Balance sheet and facility text | Main buffer; most of it sits at subsidiaries | Liquidity and access | S4 page:3 and page:18; S7 page:17 | Cash split by borrower not supplied |
| 3 | About 4,350 US$m of principal due by September 30, 2027, classed as long-term | CP-1, CP-2 | Footnote to the debt table and instrument table | Sets the near-term refinancing point | Refinancing risk | S4 page:88; S1 page:322 | Split between parent and Sunoco LP is derived |
| 4 | Free cash flow of 6,082 US$m LTM against distributions of 6,955 US$m | CP-1, CP-2 | Cash flow statements | Shows reliance on external funding for growth capital | Cash conversion and funding | S1 page:289 and page:290; S4 page:6 and page:7 | LTM built from three periods |
| 5 | Covenant headroom and obligor identity after the 2026 change of state | CP-0, CP-1, CP-2 | Covenant statements and cover pages | Decides default triggers and where claims sit | Monitoring posture | S1 page:330; S4 page:1, page:18 and page:57 | Executed documents and the 8-K12B absent |

### T5B.3 Traceability map

| Credit Driver / Conclusion | Originating Module | Source Evidence | Citation Present? | Source Quality | Classification | Claim Status | Confidence Level | Traceability Status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Leverage 3.58x and 3.53x on LTM Adjusted EBITDA | CP-1 | Total debt 68,850 (S4 page:87); cash 926 (S4 page:3); Adjusted EBITDA 15,984 (S1 page:187), 15,034 and 11,802 (S7 page:7) | Yes | High for debt, Medium for EBITDA | Calculated | Supported with qualification | Medium | Committee-Ready with label |
| Liquidity 8,692 US$m | CP-1 | Cash 926 (S4 page:3); parent 4,406 (S7 page:17); Sunoco LP 2,300 and USAC 1,060 (S4 page:18) | Yes | High | Calculated | Supported | High | Committee-Ready |
| About 4,350 US$m due by September 30, 2027 | CP-1, CP-2 | "approximately $4.35 billion aggregate principal amount due on or before September 30, 2027" (S4 page:88); instrument amounts (S1 page:322) | Yes | High | Directly Sourced | Supported; parent split is an interpretation | Medium | Remediation Needed |
| Free cash flow 6,082 US$m and shortfall of 873 US$m | CP-1 | Operating cash flow and capital expenditures (S1 page:289; S4 page:7) | Yes | High | Calculated | Supported | High | Committee-Ready |
| Covenant headroom of 2.17 turns and obligor continuity | CP-1, CP-2 | Reported ratio 2.83x (S4 page:18); limit "5.00 to 1.00" (S1 page:330); no credit agreement or 8-K12B | Yes | High for the statements | Insufficient Information | Not testable | Low | Not Traceable |
| Control by one individual through the general partner | CP-1A | "Mr. Warren owns an 81.2% membership interest in our general partner" (S1 page:132) | Yes | High | Directly Sourced | Supported | High | Committee-Ready |

### T5B.4 Source lineage register

| Statement | Source Path | Source File | Source Document ID | Page / Section | Module Section | Type | Source Quality | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 68,850 and 68,333 | Debt table | 10-Q_2026-09-30_et-20260930.htm.jsonl | S4 | page:87 | CP-1 Debt and capital structure | Sourced | High | Components add to the printed total (recomputed) |
| Balance sheet: cash 926; current maturities 12; long-term debt 68,838 | Balance sheet | 10-Q_2026-09-30_et-20260930.htm.jsonl | S4 | page:3 and page:4 | CP-1 Debt and liquidity | Sourced | High | 12 + 68,838 = 68,850 |
| FY2025 revenue 85,536; operating income 9,027; interest expense 3,474; net income 5,708 | Statement of operations | 10-K_2025-12-31_et-20251231.htm.jsonl | S1 | page:287 | CP-1 Reported results | Sourced | High | |
| FY2025 Adjusted EBITDA 15,984 and reconciliation | MD&A table | 10-K_2025-12-31_et-20251231.htm.jsonl | S1 | page:187 | CP-1 Reconciliation | Sourced | Medium | Issuer non-GAAP; also page:398 |
| Nine-month Adjusted EBITDA 15,034 and 11,802; Q3 5,031 and 3,838 | Reconciliation | EX-99.1_2026-11-03_ex991eterq32026.htm.jsonl | S7 | page:7 | CP-1 Reconciliation | Sourced | Medium | Reproduces from the Q1 and Q2 releases (page:7 of S5 and S6) |
| Segment Adjusted EBITDA by segment | Segment note and MD&A | 10-Q_2026-09-30_et-20260930.htm.jsonl | S4 | page:55 and page:67 | CP-1 Segments | Sourced | High | Segments sum to the totals (recomputed) |
| Cash flows: operating 11,671 and 8,251; capital expenditures 5,364 and 4,180 | Cash flow statement | 10-Q_2026-09-30_et-20260930.htm.jsonl | S4 | page:6 and page:7 | CP-1 Cash flow quality | Sourced | High | |
| FY2025 operating cash flow 10,149 and capital expenditures 6,303 | Cash flow statement | 10-K_2025-12-31_et-20251231.htm.jsonl | S1 | page:289 | CP-1 Cash flow quality | Sourced | High | |
| Cash paid for interest 3,136 (FY2025) | Supplemental cash flow information | 10-K_2025-12-31_et-20251231.htm.jsonl | S1 | page:294 | CP-1 Interest cover | Sourced | High | |
| Cash paid for interest 2.45 billion and 2.05 billion US$ (nine months) | MD&A | 10-Q_2026-09-30_et-20260930.htm.jsonl | S4 | page:85 | CP-1 Interest cover | Sourced | High | Printed in billions; LTM cash interest approximate |
| Facility availability: parent 4.41 billion, Sunoco LP 2.30 billion, USAC 1.06 billion | Note 7 | 10-Q_2026-09-30_et-20260930.htm.jsonl | S4 | page:18 | CP-1 Liquidity | Sourced | High | Release shows parent 4,406 (S7 page:17) |
| Covenant ratios 3.16x, 3.01x, 2.83x and 3.21x | Debt notes | S2 page:14; S3 page:17; S4 page:18; S1 page:330 | S1 to S4 | as listed | CP-1 Leverage | Sourced | High | Management statement of a ratio calculated under the credit agreement |
| Maturities 3,512 / 5,314 / 4,505 / 11,619 / 6,154 / 37,581 | Note 6 | 10-K_2025-12-31_et-20251231.htm.jsonl | S1 | page:324 | CP-1 Maturity chart | Sourced | High | December 31, 2025 basis; no later table |
| About 4,350 due by September 30, 2027 classed as long-term | Debt table footnote | 10-Q_2026-09-30_et-20260930.htm.jsonl | S4 | page:88 | CP-1, CP-2 Maturities | Sourced | High | Covers the parent notes and Sunoco LP notes lines |
| Parent notes maturing by September 30, 2027: 1,000 + 700 + 600 + 44 + 956 | Note 6 instrument table | 10-K_2025-12-31_et-20251231.htm.jsonl | S1 | page:322 | CP-2 Key findings | Derived | High for amounts, Medium for the split | Plus Sunoco LP 550, 499 and 1 gives 4,350 |
| Junior subordinated notes: 3,800 at December 31, 2025 plus 1,750 issued in July 2026 | Note 6 and Note 7 | 10-K S1 page:323; 10-Q S4 page:17 | S1, S4 | as listed | CP-1, CP-1A | Derived | High | Notes and debentures roll forward: 48,870 + 3,000 + 1,750 - 2,150 = 51,470 |
| Senior notes are not guaranteed by subsidiaries | Note 6 | 10-K_2025-12-31_et-20251231.htm.jsonl | S1 | page:325 | CP-1, CP-1A structure | Sourced | High | Other instruments' guarantees not stated |
| Control: 81.2 percent of the general partner; Class A units | Risk factors | 10-K_2025-12-31_et-20251231.htm.jsonl | S1 | page:132 | CP-1A Ownership | Sourced | High | 851,420,597 Class A units |
| Vaquero: 2.63 billion US$, 1.95 billion US$ cash, 33.3 million units | Note 2 and MD&A | 10-Q_2026-09-30_et-20260930.htm.jsonl | S4 | page:9 and page:57 | CP-1A Transactions | Sourced | High | Signed October 6, 2026, unclosed |
| Cover pages: Delaware and NYSE, then Texas and Texas Stock Exchange | Covers | S1 to S4 | S1 to S4 | page:1 | CP-0, CP-1A | Sourced | High | 8-K12B cited at S4 page:57, not supplied |
| No material restricted cash | Note 3 | 10-Q_2026-09-30_et-20260930.htm.jsonl | S4 | page:13 | This audit | Sourced | High | Closes a gap stated in CP-1 |

### T5B.5 Calculation and assumption register

| Item | Where Used | Source Inputs / Assumption | Formula or Logic | Status | Claim Status | Confidence Level | Credit Relevance | Source Trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| LTM Adjusted EBITDA 19,216 | CP-1, CP-2 | 15,984; 15,034; 11,802 | FY2025 + nine months 2026 - nine months 2025 | Recomputed, matches | Supported | Medium | Denominator of leverage | S1 page:187; S7 page:7 |
| Total debt / EBITDA 3.58x; net 3.53x | CP-1, CP-2 | 68,850; 926; 19,216 | 68,850 / 19,216 = 3.583; 67,924 / 19,216 = 3.535 | Recomputed, matches | Supported | Medium | Leverage | S4 page:3 and page:87 |
| FY2025 leverage 4.28x; net 4.20x | CP-1 | 68,333; 1,272; 15,984 | 68,333 / 15,984 = 4.275; 67,061 / 15,984 = 4.196 | Recomputed, matches | Supported | Medium | Trend | S1 page:286 and page:324 |
| Coverage 5.14x (expense) and 5.43x (cash, approximate) | CP-1, CP-2 | 3,735; 3,536; 19,216 | 19,216 / 3,735 = 5.145; 19,216 / 3,536 = 5.434 | Recomputed, matches | Supported with approximation | Medium | Debt service | S4 page:85 |
| LTM free cash flow 6,082; shortfall 873 | CP-1, CP-2 | 13,569; 7,487; 6,955 | 13,569 - 7,487 = 6,082; 6,082 - 6,955 = -873 | Recomputed, matches | Supported | High | Funding gap | S1 page:289 and page:290; S4 page:6 and page:7 |
| Liquidity 8,692; undrawn 7,766 | CP-1, CP-2 | 926; 4,406; 2,300; 1,060 | Sum | Recomputed, matches | Supported | High | Liquidity | S4 page:3 and page:18; S7 page:17 |
| Principal 69,251; parent 52,035; subsidiaries 16,276 | CP-1, CP-2 | Debt table lines | Sum of lines | Recomputed, matches | Supported | High | Structure | S4 page:87 |
| Parent maturities by September 30, 2027: 3,300 | CP-2 | 1,000; 700; 600; 44; 956 | Sum; plus Sunoco LP 1,050 = 4,350 | Recomputed, matches the issuer total | Supported as interpretation | Medium | Refinancing | S1 page:322; S4 page:88 |
| Covenant headroom 2.17 turns; 43.4 percent EBITDA cushion | CP-2 | 5.00; 2.83 | 5.00 - 2.83; 1 - 2.83 / 5.00 | Recomputed, matches | Indicative only | Low | Headroom | S1 page:330; S4 page:18 |
| Parent proxy 3.48x | CP-2 | 52,035; 14,946 | LTM EBITDA excluding Sunoco LP and USAC segments | Recomputed, matches | Analyst Interpretation | Low | Structural subordination | S1 page:187; S4 page:55 |
| Distributable Cash Flow coverage 2.22x | CP-2 | 7,813; 3,515 | 7,813 / 3,515 | Recomputed, matches | Supported | Medium | Distribution cover | S7 page:8 |

### T5B.6 Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why It Matters | Required Remediation | Affected Output / Export Record |
| --- | --- | --- | --- | --- | --- | --- |
| Material | The near-term wall is about 4,350 US$m, "close to" the parent revolver availability | The footnote covers the parent notes and Sunoco LP notes lines; CP-1 compared the whole amount with the parent's availability | Weak Lineage | Overstates the parent's need | Use CP-2 wording: about 3,300 US$m at the parent | CP-1 Liquidity, corrected in CP-2 |
| Material | Maturity profile shown as of December 31, 2025 | No later table; 2026 redemptions and new issues change the buckets | Weak Lineage | Refinancing timing is approximate after 2025 | Build an instrument-level schedule | CP-1 maturity chart |
| Material | Obligor continuity across the 2026 change of state | Evidence is cover pages and one cross-reference | Insufficient Information | Indenture and credit agreement parties may differ | Obtain the 8-K12B | CP-1A, CP-2 |
| Minor | Restricted cash "not supplied" | The 10-Q states none was material | Weak Lineage | Gap was fillable | Use the Q3 10-Q page:13 statement | CP-1 Liquidity |
| Minor | Covenant ratios | Management statements; definitions not supplied | Analyst Inference where headroom is derived | Headroom is indicative | Obtain the credit agreement | CP-2 |

### T5B.7 Auditability assessment

| Auditability Dimension | Assessment | Evidence | Risk Mechanic | Credit Implication | Remediation Needed |
| --- | --- | --- | --- | --- | --- |
| Source traceability | Strong | Every figure in the Top 5 maps to a page of a pinned file | A reader can reopen each locator | Low risk of unsupported numbers | None |
| Calculation reproducibility | Strong | All derived figures recomputed from printed inputs | Rounded billions in the cash interest and facility text limit precision | Cover ratios are approximate | Use precise cash interest if later supplied |
| Definition consistency | Moderate | Adjusted EBITDA is issuer non-GAAP; covenant ratio is on another basis | Different measures give 3.58x, 3.90x and 2.83x | Leverage depends on the measure chosen | Keep all three labelled |
| Cross-module consistency | Good after correction | CP-2 corrects the CP-1 maturity comparison | Uncorrected CP-1 text could be read alone | Parent refinancing need misread | Read CP-2 as controlling for that point |
| Legal and structural support | Weak | No executed indentures, credit agreements, partnership agreement or 8-K12B | Structure rests on filing summaries | Priority and covenant analysis restricted | Obtain executed documents |
| Subsequent-event handling | Good | Post-quarter events are dated and kept out of period figures | Vaquero and Offen are not in the balance sheet | Forward leverage is not calculable | None |

### T5B.8 Gaps ledger

| Gap ID | Gap | Missing Evidence / Citation | Why It Matters | Impact on Output | Consequence for Confidence | Required Follow-Up Source |
| --- | --- | --- | --- | --- | --- | --- |
| CP5-GAP-001 | Executed indentures and credit agreements | Not supplied | Covenants, guarantees and baskets | Headroom indicative only | Caps confidence at Medium | Indentures, Five-Year Credit Facility agreement |
| CP5-GAP-002 | Filing explaining the change of state and exchange | Form 8-K12B of July 6, 2026 | Obligor and indenture parties | Structural conclusions restricted | Caps confidence at Medium | The 8-K12B and supplemental indentures |
| CP5-GAP-003 | Maturity table after December 31, 2025 | Not in the quarterly reports | Refinancing timing | Maturity chart stale | Lowers confidence on the wall | Next maturity disclosure or instrument-level build |
| CP5-GAP-004 | Vaquero funding plan and pro forma leverage | Not supplied | Forward leverage | Not calculable | Lowers confidence on forward view | Closing or financing disclosure |
| CP5-GAP-005 | Parent-only statements and cash by borrower | Not supplied | Structural subordination and liquidity access | Parent coverage untested | Lowers confidence on parent credit | Subsidiary filings |
| CP5-GAP-006 | Contracted share of margin | Not supplied | Revenue visibility | Business risk less precise | Minor | Contract detail |
| CP5-GAP-007 | Partnership agreement and proxy statement | Not supplied | Control and removal rights | Governance view rests on risk factors | Minor | Partnership agreement |

### T5.1 Input module register

| Module | Handoff canonical `.md` / run_id | Scope | Source Quality | Envelope / Headings Status | QA Status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | et-2026-11-05-credit_snapshot-host, accepted | Source readiness for all seven sources | Medium | Six H2 headings present; Readiness view after Reader summary | Pass with limitations | Identity and perimeter points confirmed against the filings |
| CP-1 | et-2026-11-05-credit_snapshot-host, accepted | Financial base, charts and metrics | Medium | Six H2 headings; four chart tables and one metrics table present once each | Pass with Material finding CP5-001 | Maturity comparison corrected in CP-2 |
| CP-1A | et-2026-11-05-credit_snapshot-host, accepted (second attempt) | Business, transaction, governance | Medium | Six H2 headings; operating model and profile tables single; transaction summary prose | Pass | No locator defects found in the pages opened |
| CP-2 | et-2026-11-05-credit_snapshot-host, accepted | Credit synthesis | Medium | Six H2 headings; key findings and strengths prose | Pass with limitations | Derived maturity split labelled as interpretation |

### T5.2 Citation and evidence support audit

| Severity | Module | Claim / Section | Evidence Status | Issue | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1 | About 4,350 US$m due by September 30, 2027 compared with the parent availability | Partially supported | The footnote's amount covers more than the parent's notes | Use CP-2 wording | Restricts Committee Use |
| Minor | CP-1 | Restricted cash Not supplied | Supported by search but incomplete | Q3 10-Q page:13 states no material restricted cash | Cite the statement | Formatting / Hygiene Only |
| Minor | CP-1 | Net increase in debt of 231 versus total debt increase of 517 | Supported | Difference unexplained; CP-1 labelled it as non-cash movement without a source | Mark as unexplained | Formatting / Hygiene Only |
| Minor | CP-1A | Locators for acquisitions, governance and timeline | Supported | All opened locators confirm the figures and wording | None | None |
| Minor | CP-2 | Parent split of the 4,350 US$m | Supported as interpretation | The 2027 months for the Sunoco LP notes are not printed | Keep Analyst Interpretation label | None |

### T5.3 Math, logic and definition audit

| Severity | Module | Metric / Logic Issue | Formula / Definition Issue | Source Conflict | Required Fix | Clearance Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | LTM combines FY2025 from the 10-K with 2025 comparatives from the 2026 filings | The Q3 10-Q notes that certain prior period amounts were reclassified; LTM could mix bases | None found in the Adjusted EBITDA totals | Note the basis | Formatting / Hygiene Only |
| Minor | CP-1 | LTM cash interest 3,536 is approximate | Nine-month figures printed in billions | None | Keep approximate label | Formatting / Hygiene Only |
| Minor | CP-2 | Covenant sensitivity 43.4 percent | Uses the reported ratio and limit; definition not supplied | Reported ratio is lower than the simple ratio | Keep indicative label | Restricts Committee Use |
| Minor | CP-1A | Class A voting share 19.84 percent | Class A divided by Class A plus common units | Filing says approximately 20 percent | None | None |
| Minor | CP-1 | Junior subordinated notes of 5,550 | Assumes none of the earlier issues was redeemed | Notes and debentures roll forward 48,870 + 3,000 + 1,750 - 2,150 = 51,470 matches the printed line | None; assumption supported | None |

### T5.4 Legal and structural claim audit

| Severity | Module | Legal / Structural Claim | Required Legal Source | Evidence Gap | Required Fix | Legal Review Dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1A, CP-2 | Parent senior notes are unguaranteed and structurally behind subsidiary debt | Indentures | Only the note 6 statement is available | Obtain indentures | Legal review required |
| Material | CP-1, CP-2 | Five-Year Credit Facility leverage limit 5.00x (5.50x in a Specified Acquisition Period) | Credit agreement | Definitions and baskets absent | Obtain the agreement | Legal review required |
| Material | CP-0, CP-1A | The registrant moved from Delaware to Texas and from the NYSE to the Texas Stock Exchange | 8-K12B, plan of conversion or successor documents | Cover pages only | Obtain the filing | Legal review required |
| Minor | CP-1A | General partner control and Class A voting rights | Partnership agreement | Risk factor summary only | Obtain the agreement | Legal review required |
| Minor | CP-1 | Junior subordinated notes rank below senior debt | Indenture terms | Ranking not read in the pack | Obtain terms | Legal review required |

### T5.5 Market and relative value claim audit

| Severity | Module | Market / RV Claim | Missing Datapoint | Evidence Gap | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-1A, CP-2 | No market, valuation or relative value claim is made; the non-affiliate market value of 55.98 billion US$ is stale (June 30, 2025) and used only as a profile fact | Current prices, spreads and ratings | Not supplied and not requested for this scope | None | None for this scope |

### T5.6 Cross-module consistency and version audit

| Severity | Affected Modules | Data / Claim Conflict | Version Issue | Required Fix | Downstream Impact |
| --- | --- | --- | --- | --- | --- |
| Material | CP-1 and CP-2 | CP-1 compares 4,350 with 4,406 of parent availability; CP-2 says about 3,300 is the parent portion | CP-1 was not edited | Treat CP-2 as controlling | Parent refinancing need smaller than CP-1 implied |
| Minor | CP-0, CP-1, CP-1A, CP-2 | Totals reused across modules (68,850; 19,216; 8,692; 52,035; 16,276; 5,550) agree everywhere | None | None | None |
| Minor | CP-0 and CP-1 | CP-0 said the debt table is at page:87 and no maturity table is printed after December 31, 2025; CP-1 confirms both | None | None | None |
| Minor | Upstream hashes | Each handoff lists the exact hashes of the upstream handoffs; all match the run record | None | None | None |

### T5.7 Duplication, materiality and committee-readiness audit

| Severity | Module | Issue Type | Description | Required Fix | Committee Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1, CP-2 | Duplicative Content | Leverage and liquidity figures repeat across modules | Condense in the final report | Formatting only |
| Minor | CP-2 | Materiality | Parent proxy leverage 3.48x is low-confidence and secondary | Keep labelled or drop from the headline | Avoid over-reading |
| Minor | CP-1A | Presentation | The change of state and exchange appears in several places | Keep one conflict entry | Formatting only |

### T5.8 Handoff envelope and evidence trace audit

| Severity | Module | Handoff Component | Defect | Required Fix | Downstream Handoff Impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0 to CP-2 | Envelope | Markdown transport has no front matter or generated file name; headings and hashes follow the run rules | None | None |
| Minor | CP-1 | Chart selectors | No defect: four chart tables and one metrics table present once each, with no blank basis cells | None | None |
| Minor | CP-1A | Selectors | Operating model and profile tables are single tables; transaction summary is prose | None | None |
| Minor | CP-2 | Sources | Issuer sources listed as relied on through handoffs plus stated direct checks | None | None |

### T5.9 Consolidated issue log

| Issue ID | Severity | Module | Issue Type | Description | Required Fix | Clearance Impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| CP5-001 | Material | CP-1, CP-2 | Cross-module Consistency | The 4,350 US$m due by September 30, 2027 was compared with the parent's availability; about 3,300 is parent | Use CP-2 wording | Restricts Committee Use | Corrected in CP-2 |
| CP5-002 | Material | CP-1, CP-2 | Evidence Gap | Executed debt documents absent; covenant headroom untestable | Obtain executed documents | Restricts Committee Use | Open |
| CP5-003 | Material | CP-0, CP-1A | Evidence Gap | Change of state and exchange evidenced only by cover pages | Obtain the 8-K12B | Restricts Committee Use | Open |
| CP5-004 | Material | CP-1 | Weak Lineage | Maturity profile stale after December 31, 2025 | Build an instrument-level schedule | Restricts Committee Use | Open |
| CP5-005 | Minor | CP-1 | Evidence Gap | Restricted cash described as Not supplied; the 10-Q states none material | Cite page:13 | Formatting / Hygiene Only | Closed in this audit |
| CP5-006 | Minor | CP-1 | Definition and Assumption | Cash interest approximated; LTM mixes bases | Keep labels | Formatting / Hygiene Only | Open |
| CP5-007 | Minor | CP-2 | Assumption | Parent split of the near-term wall depends on unprinted months for Sunoco LP notes | Keep the interpretation label | Formatting / Hygiene Only | Open |
| CP5-008 | Minor | CP-1, CP-2 | Duplicative Content | Repeated leverage narrative | Condense | Formatting / Hygiene Only | Open |

### Remediation priority map

Must-fix before committee: CP5-002 (executed indentures and credit agreement) and CP5-003 (the 8-K12B and any successor documents).

Must-fix before the handoffs are consumed downstream: CP5-001 (read CP-2 as controlling for the parent portion of the 2027 wall) and CP5-004 (build a current instrument-level maturity schedule).

Monitoring follow-up: Vaquero funding and closing, the CPS Energy and Greenpeace judgments, the 2027 notes refinancing, the April 11, 2027 revolver step-down, and cash interest once precisely reported.

Formatting and hygiene: CP5-005 to CP5-008.

### Clearance decision

CLEARANCE DECISION: Conditional. Critical Issues: 0. Material Issues: 4. Minor Issues: 4. Committee Use: Restricted. qa_status: Restricted; committee_status: Restricted. No Critical finding changes the credit conclusion, so the Blocked cap does not apply. Committee use should be limited to a provisional fundamental view until the executed debt documents and the 8-K12B are reviewed and a current maturity schedule is built. The numeric confidence score is not asserted because the scoring routine is script-owned and was not run here; the band is Medium.

## Calculations

Independent recomputation performed for this audit from the cited inputs (US$ millions unless stated). LTM Adjusted EBITDA: 15,984 + 15,034 - 11,802 = 19,216; by quarters 4,937 + 5,066 + 5,031 = 15,034 and 4,098 + 3,866 + 3,838 = 11,802. Total debt: 69,251 + 12 - 413 = 68,850; principal 51,470 + 565 + 75 + 850 + 13,131 + 2,350 + 111 + 684 + 15 = 69,251; parent 51,470 + 565 = 52,035; Sunoco LP and USAC 13,131 + 111 + 2,350 + 684 = 16,276. Ratios: 68,850 / 19,216 = 3.583; (68,850 - 926) / 19,216 = 3.535; 68,333 / 15,984 = 4.275; (68,333 - 1,272) / 15,984 = 4.196; 19,216 / 3,735 = 5.145; 19,216 / 3,536 = 5.434. Cash flow: 13,569 - 7,487 = 6,082; distributions 4,832 + 2,082 + 41 = 6,955; 6,082 - 6,955 = -873. Liquidity: 926 + 4,406 + 2,300 + 1,060 = 8,692. Parent notes by September 30, 2027: 1,000 + 700 + 600 + 44 + 956 = 3,300; Sunoco LP 550 + 499 + 1 = 1,050; total 4,350. Notes and debentures roll forward: 48,870 + 1,000 + 1,000 + 1,000 + 650 + 1,100 - 1,000 - 600 - 550 = 51,470 (net 3,000 + 1,750 - 2,150 = 2,600; 48,870 + 2,600 = 51,470). USAC notes: 1,750 + 600 = 2,350. Maturity table: 3,512 + 5,314 + 4,505 + 11,619 + 6,154 + 37,581 = 68,685. Segment shares: 1,224 / 5,031 = 24.33 percent. Covenant: 5.00 - 2.83 = 2.17; 1 - 2.83 / 5.00 = 0.434. Parent proxy: (15,984 - 2,047 - 614) + (15,034 - 2,889 - 580) - (11,802 - 1,401 - 459) = 13,323 + 11,565 - 9,942 = 14,946; 52,035 / 14,946 = 3.482. Distributable Cash Flow: 7,813 / 3,515 = 2.223. Class A: 851,420,597 / (3,439,986,779 + 851,420,597) = 19.84 percent. All figures reproduce.

## Gaps

The gaps are listed in the gaps ledger above (CP5-GAP-001 to CP5-GAP-007). Principal readiness limits: the executed indentures and credit agreements, the Form 8-K12B and any successor documents, a maturity table after December 31, 2025, the Vaquero funding plan, parent-only statements and the partnership agreement were not supplied. Covenant headroom, obligor continuity, the parent's own coverage and forward leverage therefore cannot be traced. This audit did not review images or charts (none exist in the text extraction) and relied on text extraction fidelity; table layout was not visually checked against the filed HTML.

## Next module

This is the final selected module of the minimum set. The outputs for delivery are the four accepted handoffs plus this audit; deliver with the restricted committee status and the remediation map above. Before committee use, obtain the executed debt documents (CP5-002), the 8-K12B (CP5-003) and a current maturity schedule (CP5-004), and read the CP-2 wording for the parent share of the 2027 wall (CP5-001) if the handoffs are reissued.
