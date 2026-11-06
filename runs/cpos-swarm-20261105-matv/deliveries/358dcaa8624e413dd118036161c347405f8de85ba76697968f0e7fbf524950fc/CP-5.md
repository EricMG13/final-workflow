## Request

This evidence trace and research integrity review covers Mativ Holdings, Inc. (ticker MATV, issuer id matv) as of 2026-11-05 on the credit_snapshot pathway, reporting currency USD in millions, periods Q3 2026 and FY2025. It tests the source readiness, financial, business and synthesis handoffs for claim-to-source lineage, locators, calculations, cross-module consistency and committee readiness, using the seven pinned issuer sources, and changes none of their conclusions.

## Sources

### Issuer sources re-opened for the trace

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_matv-20251231.htm.jsonl | 0987bdd177918d1704e3f88d583ff72f6a39e66a94dd95882dba466d3888311c |
| 10-Q_2026-03-31_matv-20260331.htm.jsonl | be2515741fe2f13e179c4c2e30c15996c434ad9db582dc94e1ef7a9b4954e68d |
| 10-Q_2026-06-30_matv-20260630.htm.jsonl | 7184a20d311477dd5cb1dfc9b30dba5f1ea74b357d6c5b8b24327bc29eea17ff |
| 10-Q_2026-09-30_matv-20260930.htm.jsonl | cd05c1595b274a699b4cdcd913ff17f3c1b042cf31d245b0741f58eac17a20fb |
| EX-99.1_2026-05-06_ex991earningsrelease2026q1.htm.jsonl | 9f2d35ab42751d0b53917904e34ca17dd018903790ffb5f1f2e30283805e8933 |
| EX-99.1_2026-08-05_ex991earningsrelease2026q2.htm.jsonl | 6cdc4bf84d342bfc79bbfbfa3bbc0faf89dc1156b59bfb476359102520bc07e0 |
| EX-99.1_2026-11-04_ex991earningsrelease2026q3.htm.jsonl | 1d8a4657f455e3276abc49c4e3ccf64e82f7d0ab6a0f632c1c495bd5b53fcf53 |

### Run context (settings, not issuer evidence)

| Source name | sha256 |
| --- | --- |
| context (1000623-mativ-holdings-inc-matv.json) | 43cba5e2e4b206f93654450fc247b91671c4b4e4ab36f2ccb3891319991c5f21 |

### Handoffs under review

| Handoff module | sha256 |
| --- | --- |
| CP-0 | 92a14b77ed2bb9def0944723f4f65aeedad508eab324c95320e6d76a3b3d4ee9 |
| CP-1 | 4592a648cae094f6158e4316f1530fee27bfdea9527de2676d0f914ffc2ab970 |
| CP-1A | 72b704ec84c33eb840a037aebb90e6259df29db7cdc6498566f14704772c741e |
| CP-2 | a74131f4b7185b995359ee537ffb2750707da6137d687a7bf9a8742ab8cdd76a |

Method of the trace: every cited page was opened in the extracted source text; 58 key input figures (statement lines, debt table, covenant and liquidity statements, segment and cash flow items) were checked by exact string against the page each handoff cites, and every derived figure was recomputed from those inputs. The review ran on the supplied text only; no external material was used.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The analysis traces to the filings: every checked input was found on its cited page and every calculation recomputes. Use is restricted because covenant terms, legal capacity and one maturity wording cannot be settled from the evidence. | Medium | The financing documents are absent, so covenant definitions and creditor-control conclusions cannot be verified at source. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| All 58 checked inputs match their cited pages, and the leverage, cover, liquidity and maturity figures recompute exactly. | The numbers a committee would rely on are sound. | High |
| The explanation of why reported-basis leverage exceeds management's 3.8x names specific add-backs that the sources do not support. | Treat the gap between the two leverage measures as unreconciled. | Medium |
| The revolver and Term Loan A maturity wording conflicts with the maturity table and is carried consistently as unresolved. | Refinancing timing conclusions stay restricted. | Medium |
| A few locators are incomplete and one trailing dividend figure is not in an upstream handoff; each was verified against the sources. | Presentation defects only; no number changes. | High |

### Evidence trace view

The credit analysis for Mativ Holdings, Inc. is traceable enough for restricted committee use. Every one of the 58 key inputs checked is printed on the page the handoffs cite, the derived leverage, interest cover, liquidity, maturity and free cash flow figures recompute exactly, and the same figure carries the same value in every handoff that uses it. Of 20 material claims, 10 are directly sourced, 5 calculated, 1 assumption-based and 4 analyst inference. The weakest point is the explanation of the gap between reported-basis and management leverage, which names add-backs the sources do not support. What decides committee use is the missing financing documents: covenant definitions, creditor-control terms and the revolver maturity wording cannot be settled, so no covenant-capacity or legal conclusion is verified.

### Source register

| Source document id | Source document name | Source quality | Period | Entity covered | Data supplied | Limitation | Downstream use |
| --- | --- | --- | --- | --- | --- | --- | --- |
| S1 | 10-K FY2025 | High: audited filed statements | Year ended December 31, 2025 and 2024, 2023 | Mativ Holdings, Inc. and subsidiaries | Statements, notes, debt, covenants, leases, pensions, business description | Pre-refinancing debt terms | Annual base for CP-1 and CP-1A |
| S2 | 10-Q Q1 2026 | High: unaudited filed | Three months to March 31, 2026 | Same | Statements, debt, Ninth Amendment as subsequent event | Pre-amendment balance sheet | Quarterly series |
| S3 | 10-Q Q2 2026 | High: unaudited filed | Six months to June 30, 2026 | Same | First balance sheet under amended facilities | None beyond filing limits | Quarterly series |
| S4 | 10-Q Q3 2026 | High: unaudited filed | Nine months to September 30, 2026 | Same | Latest statements, debt, covenants, tornado, subsequent events | Credit agreement not attached | Controlling source for current balances |
| S5 | Earnings release Q1 2026 | Medium: management, attributed | Three months to March 31, 2026 | Same | Adjusted EBITDA, net debt, liquidity | Non-GAAP, definitions partial | Management measures |
| S6 | Earnings release Q2 2026 | Medium: management, attributed | Three months to June 30, 2026 | Same | Same | Same | Management measures |
| S7 | Earnings release Q3 2026 | Medium: management, attributed | Three months to September 30, 2026 | Same | Same, with segment reconciliations | Same | Management measures |

### Top credit drivers and traceability

| Rank | Credit driver | Originating module | Source-supported basis | Why material | Committee relevance | Source trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Refinancing and maturity profile | CP-1, CP-1A, CP-2 | Amended facilities and 8.000% notes due 2029; maturity table | Sets repayment and refinancing risk | Determines medium-term risk | S4 pages 12 to 14 and 28 | Wording versus table unresolved |
| 2 | Leverage and covenant headroom | CP-1, CP-2 | Management 3.8x against 5.00x maximum; covenant ranges | Compliance and flexibility | Headroom narrows with step-downs | S4 pages 14 and 28; S7 page 11 | Covenant definitions absent |
| 3 | Earnings coverage and quality | CP-1, CP-2 | Operating profit, D&A, cash interest | Debt service capacity | Thin cover on reported basis | S1 pages 75, 77, 78; S4 pages 2, 4, 5 | Reported basis, not covenant basis |
| 4 | Liquidity | CP-1, CP-2 | Cash, undrawn revolver | Near-term resilience | Adequate, less deep than before | S4 pages 27, 28; S7 page 3 | 8.8 unexplained |
| 5 | Segment volume, price and the tornado | CP-1, CP-1A, CP-2 | Segment tables; tornado note | Revenue durability and margin | Price-led recovery; supply concentration | S4 pages 17, 18, 22, 24; S7 pages 1, 2 | Insurance outcome open |

### Traceability map (claim lineage)

| Credit driver or conclusion | Originating module | Source evidence | Citation present | Source quality | Classification | Claim status | Confidence | Traceability status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt 976.4 and net debt 879.1 | CP-1 | S4 page 12; S7 page 11 | Yes | High and Medium | Directly Sourced | Supported | High | Traced |
| Liquidity 373.5 (cash 97.3 plus undrawn 276.2) | CP-1, CP-2 | S4 page 28; S7 page 3 | Yes | High and Medium | Directly Sourced | Supported | High | Traced |
| Management net leverage 3.8x against 5.00x | CP-1, CP-2 | S4 page 28 | Yes | High | Directly Sourced | Supported | High | Traced |
| Covenant ranges 5.00x to 4.00x and 2.50x to 3.00x | CP-1 | S4 page 14 | Yes | High | Directly Sourced | Supported | High | Traced; step dates absent |
| Maturity table 2026 to Thereafter, total 1,011.1 | CP-1, CP-2 | S4 page 14 | Yes | High | Directly Sourced | Supported | High | Traced |
| Adjusted EBITDA 62.3 and 184.8 | CP-1 | S7 page 11 | Yes | Medium | Directly Sourced | Supported (management) | Medium | Traced |
| Free cash flow 90.5 | CP-1, CP-2 | S7 page 11; S4 page 4 | Yes | Medium | Directly Sourced | Supported (management) | Medium | Traced |
| Segment sales and gross margins | CP-1, CP-1A, CP-2 | S4 pages 22, 24 | Yes | High | Directly Sourced | Supported | High | Traced |
| Tornado expense 43.8, recoveries 5.0 and 38.0 | CP-1, CP-1A | S4 pages 17, 18 | Yes | High | Directly Sourced | Supported | High | Traced; some locators partial |
| Receivables sold 837.3 | CP-1, CP-1A | S4 page 6 | Yes | High | Directly Sourced | Supported | High | Traced |
| Reported-basis EBITDA 210.0 | CP-1 | S1 pages 75, 77; S4 pages 2, 4 | Yes | High | Calculated | Recomputed | High | Traced |
| Net debt to EBITDA 4.19x, total 4.65x | CP-1, CP-2 | Same inputs | Yes | High | Calculated | Recomputed | High | Traced |
| EBITDA to cash interest 2.62x | CP-1, CP-2 | S1 page 78; S4 page 5 | Yes | High | Calculated | Recomputed | High | Traced |
| Deleveraging attribution (1.09x EBITDA, 0.26x net debt) | CP-2 | CP-1 figures | Yes (upstream) | High | Calculated | Recomputed | Medium | Traced; rests on trough FY2025 base |
| EBITDA cushion 24.0 percent and 5.0 percent | CP-1, CP-2 | S4 page 28 (3.8x) | Yes | Medium | Calculated | Recomputed | Medium | Traced; uses rounded 3.8x |
| Free cash flow retires 57 percent of the notes by 2029 | CP-2 | CP-1 figures | Yes (upstream) | Medium | Assumption-Based | Illustrative | Low | Assumption stated |
| Gap between reported and management leverage is due to add-backs | CP-1 | S7 pages 10, 11 | Partial | Medium | Analyst Inference | Not supported as written | Low | Weak lineage |
| Term Loan B margin about 75 basis points higher | CP-1A | S1 page 65; S4 page 14 | Yes | High | Analyst Inference | Plausible, pairing assumed | Low | Disclosed as interpretation |
| Revolver and Term Loan A could mature ahead of the notes | CP-1, CP-1A, CP-2 | S4 pages 13, 14, 28 | Yes | High | Analyst Inference | Unresolved conflict | Low | Carried as conflict |
| No related-party, priming or non-pro rata transactions | CP-1A | Text search of all seven sources | Partial | High | Analyst Inference | Absence of evidence | Low | Search described, not locatable |

### Statement-level locator tests

| Statement | Source file | Source document id | Page | Module section | Type | Source quality | Result |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Net sales 499.5, 1,510.9 | 10-Q Q3 | S4 | 2 | CP-1 metrics | Statement line | High | Confirmed |
| Total debt 976.4; issuance costs 34.7; revolver 20.0 | 10-Q Q3 | S4 | 12 | CP-1 debt register | Debt note | High | Confirmed |
| Covenant ranges; average rates 7.66%, 6.40%, 8.40% | 10-Q Q3 | S4 | 14 | CP-1 covenants | Debt note | High | Confirmed |
| Net leverage 3.8x; undrawn 276.2; debt to capital on page 29 (67.6%) | 10-Q Q3 | S4 | 28, 29 | CP-1 covenants | MD&A | High | Confirmed |
| Operating profit and D&A for FY2025 | 10-K | S1 | 75, 77 | CP-1 EBITDA | Statement line | High | Confirmed |
| Cash interest 82.8, 55.2, 52.5, 40.2, 10.9 and prior comparatives | 10-K, 10-Q Q1 to Q3 | S1 to S4 | 78, 4, 5, 5 | CP-1 interest cover | Supplemental cash flow | High | Confirmed |
| Adjusted EBITDA by quarter 47.5, 75.0, 62.3 | Releases Q1 to Q3 | S5 to S7 | 9, 10, 10 and 11 | CP-1 segments | Non-GAAP | Medium | Confirmed |
| Pension funded status, leases, purchase obligations | 10-K | S1 | 112, 92, 67 | CP-1 claims outside debt | Notes | High | Confirmed |
| Product mix, geography Q3 2026 | 10-Q Q3 | S4 | 22 | CP-1A operating model | Segment note | High | Confirmed |
| Engineered Papers sale 620.0 and repayment 641.2 | 10-K | S1 | 95 | CP-1A transaction | Note | High | Confirmed (conflict logged) |

### Calculation and assumption register

| Item | Where used | Source inputs or assumption | Formula or logic | Status | Claim status | Confidence | Credit relevance | Source trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Reported-basis EBITDA, LTM Q3 2026 | CP-1, CP-2 | Operating profit and D&A: 72.6 and 137.4 | (-384.4 + 394.5 + 62.5) + (141.0 - 106.3 + 102.7) = 72.6 + 137.4 = 210.0 | Recomputed, equal | Verified | High | Denominator of leverage | S1 75, 77; S4 2, 4 |
| EBITDA, FY2025 | CP-1 | -384.4, 141.0, 411.9 | Sum = 168.5 | Recomputed, equal | Verified | High | FY2025 leverage | S1 75, 77 |
| Total and net debt to EBITDA | CP-1 | 976.4, 879.1, 210.0 | 4.65x and 4.19x | Recomputed, equal | Verified | High | Leverage | S4 12; S7 11 |
| LTM cash interest and cover | CP-1 | 82.8, 55.2, 52.5 | 80.1 and 210.0 / 80.1 = 2.62x | Recomputed, equal | Verified | High | Cover | S1 78; S4 5 |
| LTM interest expense cover | CP-1 | 71.1, 54.1, 54.9 | 71.9 and 2.92x | Recomputed, equal | Verified | High | Cover | S1 75; S4 2 |
| Implied covenant EBITDA from 3.8x | CP-1 | 879.1, 3.8 | 231.3 (range 228.3 to 234.4) | Recomputed, equal; inference flagged | Verified as arithmetic | Low | Definition gap | S4 28 |
| Maturity concentration 2029 | CP-2 | 406.2, 1,011.1, 109.7 | 40.2 percent; 51.0 percent with the springing reading | Recomputed, equal | Verified | Medium | Refinancing | S4 14 |
| Deleveraging attribution | CP-2 | 934.0, 168.5, 210.0, 879.1 | 5.54, 4.45, 4.19; 1.09x and 0.26x | Recomputed, equal | Verified | Medium | Source of improvement | S1; S4; S7 |
| Free cash flow after dividends and 3-year capacity | CP-2 | 98.5, 22.5, 3.0 years, 400.0 | 76.0; 228.0; 57 percent | Recomputed, equal; 22.5 not in upstream | Assumption-Based | Low | 2029 notes | S1 77, 78; S4 4, 24 |
| Liquidity | CP-1 | 97.3, 276.2 | 373.5 | Recomputed, equal | Verified | High | Liquidity | S4 28; S7 3 |
| Commitment less drawings versus printed capacity | CP-1 | 305.0, 20.0, 276.2 | 285.0 - 276.2 = 8.8; same at three other dates | Recomputed, equal | Verified | Medium | Unexplained usage | S4 12, 13, 28 |
| Debt principal and maturity total | CP-1 | 20.0, 89.7, 498.7, 400.0, 2.7 | 1,011.1; less 34.7 = 976.4 | Recomputed, equal | Verified | High | Debt tie-out | S4 12, 14 |
| Quarterly sums to nine months | CP-1 | Quarter statements | 1,510.9; 184.8; -9.3 | Recomputed, equal | Verified | High | Series integrity | S2 to S4; S5 to S7 |
| Debt to capital | CP-1 | 976.4, 467.1 | 67.6 percent | Recomputed, equal to printed | Verified | High | Capital | S4 3, 29 |

### Missing citation and weak lineage flags

| Severity | Conclusion | Issue | Classification | Why it matters | Required remediation | Affected output |
| --- | --- | --- | --- | --- | --- | --- |
| MATERIAL | Reported-basis leverage is higher than management's 3.8x because the covenant and management measures add back items such as stock compensation, restructuring, financing fees and purchase-accounting items | The covenant definition is not supplied; purchase accounting adjustments appear in the adjusted income reconciliation (S7 page 10) and not in the adjusted EBITDA reconciliation (S7 page 11); the add-back list is therefore inference | Analyst Inference | A reader could take the explanation as a verified reconciliation | State the gap as unreconciled until the compliance certificate or Q4 2025 release is supplied | CP-1 financial base view (accepted; cannot be edited) |
| MINOR | Trailing dividends 22.5 | The figure is not in any upstream handoff; recomputed as 22.3 (S1 page 78) - 16.8 + 17.0 (S4 page 4) = 22.5 | Calculated, lineage gap | CP-2 is meant to use upstream evidence only | Carry the input in the upstream handoff | CP-2 free cash flow capacity |
| MINOR | Revolver availability 276.2 | Row cites pages 12 to 14 but the figure is on S4 page 28 | Locator incomplete | Reader cannot find the figure at the cited page | Add page 28 | CP-1 debt register |
| MINOR | Issuance costs paid 32.7 | Row cites S4 page 13 and S2 page 21; the figure is on S4 page 4 | Locator incomplete | Same | Add page 4 | CP-1 events table |
| MINOR | Tornado total expense 43.8 and net loss 0.8 | Cited S4 page 17; the table continues on page 18 | Locator incomplete | Same | Add page 18 | CP-1A operating model |
| MINOR | Nine-month restructuring 4.7 and free cash flow 90.5 | Cited to S1 page 7 and S1 page 77; the figures are on S4 page 2 and S7 page 11 | Locator incorrect | Misdirects a checker | Correct the locators | CP-1A operating model |
| MINOR | Sector "Paper Mills" tagged Documentary Fact | The value is from the run context, not the filings | Classification | Context is not issuer evidence | Tag as context | CP-1A company profile |
| MINOR | Reported-basis cover is "close to the covenant floor" | The covenant level applicable today is not supplied (range 2.50x to 3.00x over time; 2.75x applied after December 2025 before the amendment) | Qualification | Overstates precision of the comparison | Qualify the comparison | CP-2 key findings |

### Auditability assessment

| Auditability dimension | Assessment | Evidence | Risk mechanic | Credit implication | Remediation needed |
| --- | --- | --- | --- | --- | --- |
| Citation coverage | Strong | Locators on every table row in the financial and business handoffs | A reader can reopen each figure | Low reperformance cost | Fix the minor locator defects |
| Calculation reproducibility | Strong | All derived figures recomputed exactly from cited inputs | No hidden arithmetic | Leverage and cover can be relied on | None |
| Definition control | Weak | Covenant EBITDA, interest and net debt definitions absent | Reported and covenant measures cannot be bridged | Covenant headroom cannot be verified | Obtain agreement or compliance certificate |
| Cross-module consistency | Strong | Identical values wherever a figure repeats; no contradictory variants | Prevents mixed numbers in a report | Consistent story | None |
| Management versus filing authority | Adequate | Management measures labelled and not adopted | Prevents silent override of filings | Appropriate caution | Keep labels in the report |
| Conflict handling | Adequate | Maturity wording and Engineered Papers repayment logged, not reconciled | Open conflicts stay visible | Restricts refinancing timing view | Resolve from the agreement |

### Handoff register

| Module | Handoff canonical file and run | Scope | Source quality | Envelope and headings status | QA status | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| CP-0 | Run matv-2026-11-05-credit_snapshot-host, CP-0 | Seven sources, four downstream consumers | High filings, Medium releases | Six H2 headings present; readiness view after summary | Accepted | READY_WITH_LIMITATIONS; conflicts logged |
| CP-1 | Same run, CP-1 | Financial base, charts, registers | As above | Required chart selectors present once | Accepted | Weak lineage on one explanation |
| CP-1A | Same run, CP-1A | Business, transaction, governance | As above | Required selectors present once | Accepted | Minor locator defects |
| CP-2 | Same run, CP-2 | Credit synthesis | Upstream only | Selectors present once | Accepted | One input not carried upstream |

### Consolidated issue log

| Issue id | Severity | Module | Issue type | Description | Required fix | Clearance impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | MATERIAL | CP-1 | Unsupported explanation | Add-back attribution of the leverage gap | Treat as unreconciled; restate in any report | Do not repeat the attribution; restrict leverage-reconciliation claims | Open; mitigated by CP-2 wording |
| I-02 | MATERIAL | CP-0, CP-1, CP-1A, CP-2 | Source conflict | Revolver and Term Loan A maturity wording versus maturity table | Obtain the amended agreement | Restrict refinancing timeline conclusions | Open, carried consistently |
| I-03 | MATERIAL | All | Source gap | Credit agreement, indenture, receivables agreement absent | Obtain documents | No covenant-capacity, security or legal conclusions | Open |
| I-04 | MINOR | CP-1 | Locator | 276.2 and 32.7 locators incomplete | Add pages | None | Open, cosmetic |
| I-05 | MINOR | CP-1A | Locator | 43.8, 0.8, 4.7 and 90.5 locators incomplete or incorrect | Correct | None | Open, cosmetic |
| I-06 | MINOR | CP-2 | Lineage | Trailing dividends 22.5 not carried upstream | Carry the inputs | None; recomputed | Open |
| I-07 | MINOR | CP-1A | Classification | Sector value is context, tagged as fact | Retag | None | Open |
| I-08 | MINOR | CP-2 | Qualification | Cover compared with the lowest covenant level | Qualify | None | Open |
| I-09 | MINOR | CP-1A | Source conflict | Engineered Papers repayment above stated price | Not resolvable | None | Open, logged |
| I-10 | MINOR | CP-1 | Source gap | 8.8 gap in revolver availability unexplained | Compliance certificate | Liquidity precision | Open, carried |

### Clearance decision

The committee may use this credit snapshot in a restricted form: the financial figures, liquidity, maturity profile, business description, segment dynamics and the credit view are traceable and may be relied on as stated, with management measures labelled as management's. The committee should not rely on any statement about covenant capacity or headroom beyond the cited ranges and management's 3.8x, any legal or creditor-control conclusion, the timing of the revolver and Term Loan A maturities, or the explanation of the gap between reported-basis and management leverage. Committee status: Restricted. Research QA status: Restricted. Confidence: Medium. A numeric confidence score was not computed because the scoring script is not available in this run; no score is stated. No finding rises to Critical: no input was missing from its cited page and no calculation failed.

## Calculations

All amounts USD millions. Each derived figure in the upstream handoffs was recomputed from inputs re-read on the cited pages.

- Reported-basis EBITDA, LTM Q3 2026: operating profit -384.4 - (-394.5) + 62.5 = 72.6; D&A 141.0 - 106.3 + 102.7 = 137.4; sum 210.0 (equal to CP-1). LTM Q2: 68.7 + 139.0 = 207.7; LTM Q1: 53.5 + 140.5 = 194.0; FY2025: -384.4 + 141.0 + 411.9 = 168.5 (all equal).
- Leverage: 976.4 / 210.0 = 4.65; 879.1 / 210.0 = 4.19; FY2025 1,018.2 / 168.5 = 6.04 and 934.0 / 168.5 = 5.54; Q2 974.5 / 207.7 = 4.69 and 908.2 / 207.7 = 4.37; Q1 1,035.8 / 194.0 = 5.34 and 953.5 / 194.0 = 4.91 (all equal).
- Cover: 82.8 - 55.2 + 52.5 = 80.1; 210.0 / 80.1 = 2.62; Q2 82.8 - 42.4 + 40.2 = 80.6 and 207.7 / 80.6 = 2.58; Q1 82.8 - 13.2 + 10.9 = 80.5 and 194.0 / 80.5 = 2.41; FY2025 168.5 / 82.8 = 2.04 (all equal). Interest expense basis: 71.1 - 54.1 + 54.9 = 71.9; 210.0 / 71.9 = 2.92 (equal).
- Management nine-month cover: 184.8 / 52.5 = 3.52 (equal).
- Maturity table sum 2.2 + 6.6 + 6.1 + 406.2 + 6.2 + 583.8 = 1,011.1 (equal); 406.2 / 1,011.1 = 40.2 percent; (406.2 + 109.7) / 1,011.1 = 51.0 percent (equal).
- Deleveraging: 934.0 / 168.5 = 5.54; 934.0 / 210.0 = 4.45; 879.1 / 210.0 = 4.19; 5.54 - 4.45 = 1.09; 4.45 - 4.19 = 0.26 (equal).
- Free cash flow: 117.4 - 26.9 = 90.5; trailing 133.8 - 114.5 + 117.4 = 136.7 less 40.0 - 28.7 + 26.9 = 38.2 gives 98.5; dividends 22.3 - 16.8 + 17.0 = 22.5; 98.5 - 22.5 = 76.0; 76.0 x 3 = 228.0; 228.0 / 400.0 = 57 percent (equal; assumption of constant trailing amounts and three years to October 1, 2029).
- Covenant cushion: 1 - 3.8 / 5.00 = 24.0 percent; 1 - 3.8 / 4.00 = 5.0 percent (equal). Implied covenant EBITDA: 879.1 / 3.8 = 231.3 (equal).
- Revolver: 305.0 - 20.0 = 285.0 against 276.2, difference 8.8; June 305.0 - 17.0 = 288.0 against 279.2; March 600.0 - 175.0 = 425.0 against 416.2; December 600.0 - 160.0 = 440.0 against 431.2; all differences 8.8 (equal).
- Cross-module identity: the values 976.4, 879.1, 373.5, 3.8x, 5.00x, 4.19x, 2.62x, 406.2, 1,011.1, 90.5, 837.3, 38.0, 0.8, 400.0, 305.0, 276.2 and 97.3 were found with identical values in each handoff that uses them; no contradictory variant of any figure was found.
- Input coverage: 58 key inputs tested by exact string on their cited pages; 0 not found. Locator defects found by a separate scan of every table row that carries a locator: 6 figures (276.2, 32.7, 43.8, 0.8, 4.7 and 90.5), listed in the lineage flags.

## Gaps

| Gap | Severity | What it limits | Action |
| --- | --- | --- | --- |
| Credit agreement as amended, indenture and receivables agreement not supplied | High | Covenant definitions, step-down dates, security, guarantors, distribution capacity; no legal or covenant-capacity conclusion is verified | Obtain exhibits |
| Annual and trailing adjusted EBITDA not supplied (no fourth quarter 2025 figure) | High | Management leverage of 3.8x cannot be reproduced; the leverage gap is unreconciled | Add the Q4 2025 release or compliance certificate |
| Reported interest coverage under the agreement not supplied | Medium | Comparison of reported-basis cover with the covenant is a proxy only | Compliance certificate |
| Revolver and Term Loan A maturity wording versus maturity table unresolved | Medium | Refinancing timing | Amended agreement |
| Outstanding sold receivables and post-amendment commitment not supplied | Medium | Size of off-balance-sheet funding | October 2026 amendment filing |
| Tornado insurance outcome open | Medium | Liquidity timing | Next filing after the cutoff |
| No ratings, market data or shareholder register | Medium | Market-access and ownership views | Add if required |
| Letters of credit behind the 8.8 gap not supplied | Minor | Liquidity precision | Compliance certificate |

Not supplied does not mean zero for any item above. The trace made no change to any underlying credit conclusion and silently repaired no lineage; every defect is stated above.

## Next module

No further module is requested in this run. The report should state the credit view from the synthesis, carry the restrictions in the clearance decision, label management measures as management's, show the two leverage bases side by side without bridging them, and list the unresolved maturity wording and missing financing documents in its limitations. Corrections to apply when composing the report: omit the add-back attribution of the leverage gap, use the corrected locators listed in the lineage flags, tag the sector value as context, and qualify the comparison of cover with the covenant floor.
