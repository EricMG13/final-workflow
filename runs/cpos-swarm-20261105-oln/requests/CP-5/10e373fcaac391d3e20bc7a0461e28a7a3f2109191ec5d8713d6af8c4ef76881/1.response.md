## Request

Evidence trace validation and research integrity grade for OLIN Corp (Olin Corporation, NYSE: OLN), as of 2026-11-05, pathway credit_snapshot, current period Q3 2026 against FY2025, reporting currency USD millions. The question is whether the four upstream handoffs are traceable enough for the decision, and which provenance gap matters most. This module changes no credit conclusion and silently repairs no lineage; corrections are logged as issues.

## Sources

### Issuer sources re-opened for the trace

| Source name | sha256 |
| --- | --- |
| 10-K_2025-12-31_oln-20251231.htm.jsonl | 4c4aa24234dd70c75f25e45010299b0359519fd53db6b33485bc189c79880655 |
| 10-Q_2026-03-31_oln-20260331.htm.jsonl | b7b2893c43ac8c80dd177251279128741771bfa43d75cbf90bad3645179170d6 |
| 10-Q_2026-06-30_oln-20260630.htm.jsonl | 31cc1696caa1e392e8267ebed3744e51e1777dcbf99f80668497471e88c3bcb0 |
| 10-Q_2026-09-30_oln-20260930.htm.jsonl | fcb130292ef752affbb45743362d92ca38d4b7b812532fc678ec7413956a3cd3 |
| EX-99.1_2026-05-07_exhibit991q12026earningspr.htm.jsonl | 9f1321ffd9728e7b42deb60dc916ea8598957e5a719c0c9054fc2f70430134aa |
| EX-99.1_2026-07-30_exhibit991q22026earningspr.htm.jsonl | 08a70fcc145c266c21d73e09e50eda1490a6994f07dbbc111206ffd51445010c |
| EX-99.1_2026-10-29_exhibit991q32026earningspr.htm.jsonl | 27ebe9b3524b1cfc010f76a20b291e6a4f5bd41b4c9d2abf5a2ffd63c041424f |

The settings source `context` (sha256 09d8a3ab70b39856c937eb920b788157e416ce636cea1515d7a99dd15e9d89b1) is not issuer evidence.

### Supplied handoffs

| Module | sha256 |
| --- | --- |
| CP-0 | 728efd77512ff127e878c235404a8f40fc8f81833ce6d2ce37a46e77c06dd33e |
| CP-1 | 7df7316b863cab8ea464b4d35c09d645a7fd3da78a51db340a44c7a910837154 |
| CP-1A | e75928d2909d837811c9a94d44abfd9bfa0b7de91945f4bfc2f9433576fc2eb4 |
| CP-2 | 565975b3e8279bab48fcadffc15f0dad2393431b7e304b7868132f31d10f3c08 |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| The financial base is well traced: of 16 material claims, 6 are directly sourced and 7 are calculated from sourced inputs. Committee use is restricted on covenant headroom, note ranking and combined-company credit, which the pack cannot support. | Medium | Covenant levels, indentures, the merger agreement and Huntsman data are not supplied, and adjusted EBITDA is a management measure. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Five citations in the business handoff point to the wrong page, but every affected figure appears in the sources. | Figures can be relied on; locators need correction before audit use. | High |
| Net debt to adjusted EBITDA of 5.21x and cash interest cover of 3.15x recompute exactly from sourced inputs. | Core leverage conclusions hold on the management basis. | High |
| Adjusted EBITDA is a company measure; the FY2025 value of 651.8 reproduces from filing lines but no issued add-back schedule is in the pack. | The leverage trend rests on management add-backs. | Medium |
| Covenant levels are not supplied, so no headroom claim is supported, and none was made. | Committee use on covenant compliance is restricted. | High |
| The guidance-implied range of 4.92x to 5.10x is assumption-based. | It shows sensitivity only and is not a forecast. | Medium |

### Evidence trace view

The Olin analysis is traceable enough for a restricted committee read: of 16 material claims traced to filing pages, 6 are directly sourced, 7 are calculated from sourced inputs, 1 is assumption-based, 1 is analyst inference and 1 is a logged conflict. The strongest support is that leverage, cover, liquidity and free cash flow recompute exactly from printed figures. The most important provenance gap is that the numeric covenant levels, indentures, merger agreement and Huntsman data are absent, so covenant compliance, ranking of the senior notes and combined-company credit cannot be traced to anything. The lineage defect that matters next is that trailing adjusted EBITDA is a management non-GAAP measure. Five minor locator errors were found and logged; no figure was wrong. Remediation owner for the critical gap is the document request listed in the gaps ledger.

### Traceability summary

| Item | Result |
| --- | --- |
| Material claims traced | 16 |
| Directly sourced | 6 |
| Calculated from sourced inputs | 7 |
| Assumption-based, inference, conflict | 3 |
| Issues logged | 17 (0 Critical, 5 Material, 12 Minor) |
| Committee status | Restricted |

### Source gate and module register

| Module | Handoff and scope | Source quality | Envelope and headings status | QA status | Notes |
| --- | --- | --- | --- | --- | --- |
| CP-0 | Source readiness, sha256 728efd77, all seven sources, 2026-11-05 | Filed reports and releases, primary | Six headings and reader summary present, accepted | Qualified | One incorrect statement on ratings, corrected downstream |
| CP-1 | Financial base and credit metrics, FY2025 and Q3 2026, USD millions | Primary filings; releases as management claims | Accepted with four chart tables and one metrics table | Qualified | Management non-GAAP basis; covenant levels unsupplied |
| CP-1A | Business, ownership and transaction context, Q3 2026 | Primary filings | Accepted with two key-value tables and prose transaction section | Qualified | Five locator errors; merger documents unsupplied |
| CP-2 | Fundamental credit synthesis, Q3 2026 | Upstream handoffs only | Accepted with prose key findings and strengths and weaknesses | Qualified | One overstated phrase; confidence held at Medium |

Upstream re-anchor: all four handoffs name OLIN Corp, state the as-of date 2026-11-05, use USD millions and carry the same period labels. Figures repeated across handoffs agree: 5.21x, 4.08x, 3.15x, 3.66x, 1,244.4, 536.6, 651.8 and 3,013.1.

### Top five credit drivers

| Rank | Credit driver | Originating module | Source-supported basis | Why material | Committee relevance | Source trace | Limitation |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Leverage rose to 5.21x net and 5.62x total as trailing adjusted EBITDA fell to 536.6 | CP-1 | Debt 3,013.1 and cash 214.8 (10-Q Q3 page:2, page:12); adjusted EBITDA (EX-99.1 Q3 page:11) | Sets default and covenant risk | Core to the credit view | Calculated from sourced inputs | Management non-GAAP EBITDA |
| 2 | Liquidity of 1,244.4 and first maturity of 465.0 in November 2027 | CP-1 | 10-Q Q3 page:2, page:13, page:14 | Determines runway before merger and relief expiry | Supports near-term view | Calculated from sourced inputs | Receivables capacity borrowing-base limited |
| 3 | Covenant relief ends by September 30, 2027; levels unsupplied | CP-1 | 10-Q Q3 page:13; 10-K page:141 | Governs headroom and creditor control | Restricts compliance conclusions | Terms directly sourced; levels absent | Executed agreement not supplied |
| 4 | Huntsman merger and USD 2,500.0 million facility | CP-1A | 10-Q Q3 page:7, page:8, page:9 | Resets structure and collateral | Drives event risk | Directly sourced to filing summary | Merger agreement and Huntsman data absent |
| 5 | Cash generation: nine month free cash flow -36.9 and trailing 221.5 | CP-1 | 10-Q Q3 page:4; 10-K page:82 | Funds dividends and debt service | Tests self-funding | Calculated from sourced inputs | Seasonal working capital timing |

### Traceability map

| Credit driver or conclusion | Originating module | Source evidence | Citation present? | Source quality | Classification | Claim status | Confidence level | Traceability status |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Net and total leverage 5.21x and 5.62x | CP-1 | Balance sheet, debt note, release net debt table | Yes | Primary and management | Calculated | Verified by recomputation | High | Traced |
| Trailing adjusted EBITDA 536.6 | CP-1 | EX-99.1 Q3 page:10, page:11 | Yes | Management claim | Directly Sourced | Verified; 468.9 + 651.8 - 584.1 | Medium | Traced with limitation |
| FY2025 adjusted EBITDA 651.8 | CP-1 | Releases; 10-K page:81 lines | Yes | Management claim | Calculated | Reproduced as 544.4 + 33.4 + 75.0 - 1.0 | Medium | Traced with limitation |
| Cash interest cover 3.15x | CP-1 | 10-Q Q3 page:5; 10-Q Q2 page:5; 10-K page:83 | Yes | Primary | Calculated | Verified by recomputation | High | Traced |
| Liquidity 1,244.4 | CP-1 | 10-Q Q3 page:2, page:13 | Yes | Primary | Calculated | Verified: 214.8 + 1,029.6 | High | Traced |
| Maturity profile | CP-1 | 10-Q Q3 page:12, page:13, page:14; 10-K page:108 | Yes | Primary | Calculated | Verified; total 3,030.7 ties to 3,013.1 plus 17.6 | Medium | Traced with limitation |
| Free cash flow -36.9 nine months, 221.5 trailing | CP-1 | 10-Q Q3 page:4; 10-K page:82 | Yes | Primary | Calculated | Verified | High | Traced |
| Covenant relief terms | CP-1 | 10-Q Q3 page:13; 10-K page:141 | Yes | Primary | Directly Sourced | Verified | High | Traced |
| Merger terms and new facility | CP-1A | 10-Q Q3 page:7, page:8, page:9 | Yes | Primary summary of executed documents | Directly Sourced | Verified against text | Medium | Traced to summary only |
| Segment drivers | CP-1A | 10-Q Q3 page:40, page:41 | Yes | Primary | Directly Sourced | Verified; drivers sum to -190.6 | High | Traced |
| Ratings history | CP-1A | 10-Q Q1 page:43; 10-Q Q3 page:52, page:53 | Yes | Primary | Directly Sourced | Verified | High | Traced |
| Claims outside debt | CP-1 | 10-Q Q3 page:2, page:24, page:25; 10-K page:110 | Yes | Primary | Directly Sourced | Verified | Medium | Traced with limitation |
| Secured mix 38.4 percent and 58.9 percent | CP-2 | Debt note; indentures absent | Partly | Primary | Calculated | Arithmetic verified; note security not stated | Medium | Traced with limitation |
| Guidance-implied range 4.92x to 5.10x | CP-2 | EX-99.1 Q3 page:2 | Yes | Management guidance | Assumption-Based | Verified arithmetic; net debt held constant | Low | Labelled assumption |
| Credit view: weakening, adequate liquidity | CP-2 | Rows above | Yes | Upstream | Analyst Inference | Supported by the rows above | Medium | Traced |
| Winchester share of 2025 sales | CP-1A | 10-K page:4 against page:129 | Yes | Primary | Conflict | Logged, not reconciled | Low | Conflict preserved |

### Source lineage register

| Statement | Source file | Page | Module section | Type | Source quality | Notes |
| --- | --- | --- | --- | --- | --- | --- |
| Total debt 3,013.1; term loans 528.1; revolver 170.0; receivables 465.0 | 10-Q_2026-09-30 | page:12 | CP-1 debt table | Statement | Primary | Opened; foots to total |
| Revolver 1,029.6 undrawn, letters of credit 0.4, relief ends by September 30, 2027 | 10-Q_2026-09-30 | page:13 | CP-1 liquidity, covenants | Note | Primary | Opened |
| Net leverage covenant definition and 425.0 exclusion | 10-Q_2026-09-30 | page:14 | CP-1 covenants | Note | Primary | Opened; differs from 10-K wording |
| Receivables 465.0 drawn, 34.0 capacity, maturity November 19, 2027 | 10-Q_2026-09-30 | page:14, page:15 | CP-1 | Note | Primary | Opened |
| Nine month cash flow 69.7 and capital spending 106.6 | 10-Q_2026-09-30 | page:4 | CP-1 | Statement | Primary | Opened |
| Trailing adjusted EBITDA 536.6, net debt 2,798.3 | EX-99.1_2026-10-29 | page:11 | CP-1 | Reconciliation | Management claim | Opened; ties to 468.9 + 651.8 - 584.1 |
| Merger terms, 0.5476 exchange ratio, 54.5 percent and 45.5 percent | 10-Q_2026-09-30 | page:7, page:8 | CP-1A | Note | Primary | Opened |
| OlinHuntsman facility 2,500.0, term loan 750.0, revolver 1,750.0 | 10-Q_2026-09-30 | page:8, page:9 | CP-1A, CP-2 | Subsequent event | Primary | Opened |
| Segment bridge for Chlor Alkali Products and Vinyls | 10-Q_2026-09-30 | page:41 | CP-1A, CP-2 | MD&A | Primary | Opened; drivers sum to -190.6 |
| Ratings table and actions | 10-Q_2026-03-31; 10-Q_2026-09-30 | page:43; page:52, page:53 | CP-1A | MD&A | Primary | Opened |
| Annual maturities and FY2025 debt table | 10-K_2025-12-31 | page:104, page:108 | CP-1 | Note | Primary | Opened |
| Termination fee 121 and expense reimbursement up to 30 | 10-Q_2026-06-30; 10-Q_2026-09-30 | page:56; page:58 | CP-1A | Risk factor | Primary | Opened; later filing omits reimbursement |

### Calculation and assumption register

| Item | Where used | Source inputs or assumption | Formula or logic | Status | Claim status | Confidence level | Credit relevance | Source trace |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Total debt to adjusted EBITDA, Q3 2026 | CP-1, CP-2 | 3,013.1; 536.6 | 3,013.1 / 536.6 = 5.615, shown as 5.62x | Recomputed, agrees | Calculated | High | Leverage | 10-Q Q3 page:12; EX-99.1 Q3 page:11 |
| Net debt to adjusted EBITDA, Q3 2026 | CP-1, CP-2 | 2,798.3; 536.6 | 2,798.3 / 536.6 = 5.215, shown as 5.21x | Recomputed, agrees | Calculated | High | Leverage | EX-99.1 Q3 page:11 |
| Same ratios at FY2025, Q1 and Q2 2026 | CP-1 | Debt, cash and trailing EBITDA per period | 4.34x and 4.08x; 5.42x and 5.08x; 5.34x and 5.02x | Recomputed, agree | Calculated | High | Trend | EX-99.1 Q1 page:9; Q2 page:11 |
| Trailing cash interest | CP-1 | 129.4 + 177.9 - 137.1 | 170.2; cover 536.6 / 170.2 = 3.15x | Recomputed, agrees | Calculated | High | Debt service | 10-Q Q3 page:5; 10-K page:83 |
| Free cash flow | CP-1, CP-2 | 69.7, 106.6, 474.2, 226.3, 153.0, 163.5 | -36.9 nine months; 247.9 FY2025; 221.5 trailing | Recomputed, agrees | Calculated | High | Self-funding | 10-Q Q3 page:4; 10-K page:82 |
| Maturity by year | CP-1, CP-2 | Instrument amounts and dates | 465.0 + 669.3 + 1,213.4 + 683.0 = 3,030.7 | Recomputed, agrees | Calculated | Medium | Refinancing | 10-Q Q3 page:12 to page:14 |
| Secured and note mix | CP-2 | 1,163.1; 1,784.6; 83.0 | 38.4, 58.9 and 2.7 percent of 3,030.7 | Recomputed, agrees | Calculated | Medium | Priority mechanics | Debt note |
| FY2025 adjusted EBITDA reproduction | CP-1 | -101.1, 183.9, -60.0, 521.6, 33.4, 75.0, -1.0 | 544.4 + 33.4 + 75.0 - 1.0 = 651.8 | Recomputed, agrees | Calculated | Medium | Trend base | 10-K page:81, page:82 |
| Guidance-implied range | CP-2 | 468.9; guidance 80 to 100; net debt 2,798.3 | 2,798.3 / 548.9 = 5.10x; 2,798.3 / 568.9 = 4.92x | Assumption: net debt unchanged | Assumption-Based | Low | Sensitivity | EX-99.1 Q3 page:2 |
| Debt on principal rather than carrying value | CP-1 | 3,030.7 principal; 17.6 deferred costs | 3,030.7 / 536.6 = 5.65x against 5.62x | Gross delta logged | Calculated | Medium | Definition | 10-Q Q3 page:12 |

### Missing citation and weak lineage flags

| Severity | Module | Claim or section | Evidence status | Issue | Required fix | Clearance impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-1A | Dividends of 68.3 and 0.20 per quarter | Figure present in source, page wrong | Cited to 10-K page:83 and EX-99.1 Q1 page:3; figure is on 10-Q Q3 page:4 | Cite 10-Q Q3 page:4 | None to the figure |
| Minor | CP-1A | Acquisition-related costs 13.7 and 24.3 | Figure present in source, page wrong | Cited to 10-Q Q3 page:45; amounts are on page:8, page:9 and page:33 | Correct the locator | None to the figure |
| Minor | CP-1A | Net long-term borrowings 185.3 | Figure present in source, page wrong | Cited to 10-Q Q3 page:4; amount is on page:15 and page:47 | Correct the locator | None to the figure |
| Minor | CP-1A | Trailing adjusted EBITDA 536.6 | Figure present in source, page wrong | Sits in a sentence whose only citation is 10-Q Q3 page:23; the figure belongs to EX-99.1 Q3 page:11 | Correct the locator | None to the figure |
| Minor | CP-1A | Large accelerated filer status | Fact present in source, page wrong | Sits in a row citing 10-K page:80; status is on the 10-K cover page:2 | Correct the locator | None to the fact |
| None | CP-1 | Statement lines and segment gross margin | Verified | Locator checks passed on all other rows opened | None | None |

### Math, logic and definition audit

| Severity | Module | Metric or logic issue | Formula or definition issue | Source conflict | Required fix | Clearance impact |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Leverage uses company adjusted EBITDA, not covenant EBITDA | Covenant nets only unrestricted cash and excludes receivables financing up to 425.0; the 10-K calls the test secured debt while the 10-Q says consolidated total debt | 10-K page:106 against 10-Q Q3 page:14 | Obtain executed agreement; keep ratios labelled management basis | Restricts compliance conclusions |
| Minor | CP-1 | Debt is carrying value net of deferred costs | Principal is 3,030.7; gross delta 17.6 | None | Disclosed in this register | None |
| Minor | CP-1 | Illustrative covenant-style ratio of 4.42x | Uses 425.0 receivables exclusion, all cash as unrestricted, company EBITDA | None | Already labelled not the covenant calculation | None |
| Minor | CP-1 | Cash interest is cash paid, net | Differs from interest expense, net of 176.7; cover on that basis is 3.04x | None | Disclosed | None |

### Legal and structural claims

| Severity | Module | Legal or structural claim | Required legal source | Evidence gap | Required fix | Legal review dependency |
| --- | --- | --- | --- | --- | --- | --- |
| Material | CP-1, CP-2 | Bank debt carries guarantees and liens during relief; notes' security not stated | Credit agreement, indentures | Neither is in the pack | Obtain documents before any ranking statement | Yes |
| Material | CP-1A | Merger terms, conditions and termination payments | Merger Agreement, S-4/A | Only the 10-Q summary is available | Obtain agreement | Yes |
| Minor | CP-1A | OlinHuntsman facility terms | Second amendment of October 27, 2026 | Summary only; levels absent | Obtain exhibit | Yes |
| Minor | CP-1A | Pension plan change-of-control clause | Plan document | Whether the merger triggers it is not stated | Review plan terms | Yes |

### Market and relative value claims

| Severity | Module | Market or relative value claim | Missing datapoint | Evidence gap | Required fix | Committee impact |
| --- | --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | None made: CP-2 states no peer ranking, instrument recommendation or recovery conclusion | Prices, spreads and peers are blank in the settings | No market claim to audit | None | Relative value belongs to a later module |

### Cross-module consistency and version control

| Severity | Affected modules | Data or claim conflict | Version issue | Required fix | Downstream impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-0, CP-1, CP-1A | CP-0 says ratings are printed only as of September 30, 2026 | Corrected in CP-1 and CP-1A, which cite 10-K page:68 and 10-Q Q1 page:43 | None; the correction is stated in later handoffs | None |
| Minor | CP-1, CP-1A | CP-1 gives the termination fee as 121 only; CP-1A adds reimbursement of up to 30 | Corrected in CP-1A, which cites 10-Q Q2 page:56 | None | None |
| Minor | CP-1A | Winchester 26 percent of 2025 sales against 25.4 percent computed | Logged, not reconciled | Use segment amounts | None |
| Minor | CP-1A, CP-2 | Merger closing first half of 2027 in the July release against first quarter of 2027 later | Dated update; later controls | None | None |

All repeated figures agree across the four handoffs. No handoff states a figure that a later handoff contradicts.

### Duplication, materiality and committee readiness

| Severity | Module | Issue type | Description | Required fix | Committee impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-2 | Overstated phrase | The credit view says the three segments do not move together; the sources show differing results in FY2025 and nine months 2026 only | Qualify as two periods of evidence | Slight overstatement of diversification |
| Minor | CP-1, CP-2 | Repetition | Leverage, liquidity and covenant caveats appear in several handoffs | Acceptable for stand-alone reading | None |
| Material | All | Readiness | Covenant headroom, note ranking and combined-company credit cannot be supported | Restrict committee use to the standalone financial base | Restricted |

### Handoff structure

| Severity | Module | Handoff component | Defect | Required fix | Downstream handoff impact |
| --- | --- | --- | --- | --- | --- |
| Minor | CP-1 | Chart tables | Recovery zone bond maturity placed after 2030 by inference from the 10-K schedule | Flagged in the chart row; confirm from bond documents | None |
| Minor | CP-1A | Table format | Key-value tables carry category and locator inside the value cell | Acceptable | None |
| Minor | CP-0 to CP-2 | Hashes | All handoffs list upstream hashes exactly | None | None |

### Consolidated issue log

| Issue ID | Severity | Module | Issue type | Description | Required fix | Clearance impact | Status |
| --- | --- | --- | --- | --- | --- | --- | --- |
| I-01 | Minor | CP-1A | Locator | Dividends cited to wrong pages | Cite 10-Q Q3 page:4 | None | Open, cosmetic |
| I-02 | Minor | CP-1A | Locator | Acquisition costs cited to page:45 | Cite page:8, page:9, page:33 | None | Open, cosmetic |
| I-03 | Minor | CP-1A | Locator | Net borrowings 185.3 cited to page:4 | Cite page:15, page:47 | None | Open, cosmetic |
| I-04 | Minor | CP-1A | Locator | Trailing adjusted EBITDA cited to page:23 | Cite EX-99.1 Q3 page:11 | None | Open, cosmetic |
| I-05 | Minor | CP-1A | Locator | Filer status cited to 10-K page:80 | Cite 10-K page:2 | None | Open, cosmetic |
| I-06 | Minor | CP-0 | Statement | Ratings said to be printed only at September 30, 2026 | Correction in CP-1 and CP-1A | None | Cleared by later handoffs |
| I-07 | Minor | CP-1 | Definition | Debt on carrying value; principal larger by 17.6 | Gross delta logged here | None | Cleared |
| I-08 | Material | CP-1, CP-2 | Source gap | Covenant levels and covenant EBITDA unsupplied | Obtain executed agreement | Restricts compliance conclusions | Open |
| I-09 | Material | CP-1, CP-2 | Lineage | Adjusted EBITDA is management non-GAAP; FY2025 value has no issued schedule in the pack | Keep management label; obtain Q4 2025 release | Qualifies leverage trend | Qualified |
| I-10 | Minor | CP-2 | Wording | Segments said not to move together on two periods of evidence | Qualify | Slight | Open |
| I-11 | Material | CP-2 | Legal | Security of senior notes not stated; mix shown as not stated rather than unsecured | Obtain indentures | Restricts ranking conclusions | Qualified |
| I-12 | Minor | CP-2 | Assumption | Guidance range holds net debt constant | Labelled assumption | None | Cleared |
| I-13 | Minor | CP-1 | Omission | Expense reimbursement of up to 30 omitted | Added in CP-1A | None | Cleared |
| I-14 | Minor | CP-1A | Conflict | Winchester share of sales 26 against 25.4 percent | Logged | None | Cleared |
| I-15 | Material | CP-1A, CP-2 | Source gap | Merger agreement and Huntsman data absent | Obtain documents | Restricts combined-company conclusions | Open |
| I-16 | Minor | CP-1 | Inference | Recovery zone bond maturity inferred | Confirm from bond documents | None | Qualified |
| I-17 | Material | CP-1A | Source gap | Beneficial owners and synergy targets not supplied | Obtain proxy | Restricts ownership statements | Open |

### Auditability assessment

| Auditability dimension | Assessment | Evidence | Risk mechanic | Credit implication | Remediation needed |
| --- | --- | --- | --- | --- | --- |
| Locator precision | Good, with five page errors | 12 lineage rows opened and 5 imprecise locators found | A wrong page slows audit but does not change values | Figures reliable | Correct locators |
| Calculation reproducibility | Strong | All ten calculation rows recomputed | Inputs and formulas are printed in the handoffs | Leverage conclusions reproducible | None |
| Definition clarity | Weak on covenant | 10-K and 10-Q describe the leverage test differently | Headroom cannot be tested | Compliance claim unsupportable | Executed agreement |
| Management versus filing authority | Mixed | Adjusted EBITDA from releases; statements from filings | Management add-backs can shift ratios | Trend rests on company measure | Keep label |
| Legal document coverage | Weak | No credit agreement, indentures or merger agreement | Ranking and merger terms rest on summaries | Restricts structural conclusions | Obtain documents |

### Gaps ledger

| Gap ID | Gap | Missing evidence or citation | Why it matters | Impact on output | Consequence for confidence | Required follow-up source |
| --- | --- | --- | --- | --- | --- | --- |
| G-01 | Covenant levels | Executed credit agreement and amendments | Headroom and breach sensitivity | No headroom claim supported | Holds status at Restricted | Credit agreement, February 19, 2026 and October 27, 2026 amendments |
| G-02 | Senior note terms | Indentures | Ranking against secured bank debt | Ranking not assessable | Reduces confidence in structure | Indentures |
| G-03 | Merger documents and Huntsman data | Merger Agreement, S-4/A, Huntsman filings | Combined leverage and closing risk | No combined-company claim | Limits event-risk conclusions | Form 8-K of June 16, 2026, S-4/A, Huntsman filings |
| G-04 | Adjusted EBITDA schedule for FY2025 | Q4 2025 release | Trend base | Trend labelled management basis | Medium confidence | Q4 2025 earnings release |
| G-05 | Ownership and synergies | Proxy statement | Control and merger value | Ownership not stated | Limits governance view | 2026 proxy statement |

### Research integrity grade

QA status: Restricted. Committee status: Restricted, meaning the standalone Q3 2026 financial base, liquidity and the facts of the merger as the company summarises them may be used, while covenant compliance, note ranking and combined-company credit may not. The confidence score script is not available in this host run, so no score or band is asserted. Severity counts: 0 Critical, 5 Material (I-08, I-09, I-11, I-15, I-17) and 12 Minor. No source dated after 2026-11-05 was used. No handoff contains a peer ranking, instrument recommendation or recovery conclusion.

## Calculations

Recomputation performed in this module, each from the cited inputs and agreeing with the handoffs:

- Leverage: 3,013.1 / 536.6 = 5.615 and 2,798.3 / 536.6 = 5.215; FY2025 2,827.3 / 651.8 = 4.338 and 2,659.7 / 651.8 = 4.080; Q1 2,996.1 / 552.4 = 5.424 and 2,803.9 / 552.4 = 5.076; Q2 3,029.1 / 567.6 = 5.337 and 2,851.7 / 567.6 = 5.024.
- Trailing adjusted EBITDA: 468.9 + 651.8 - 584.1 = 536.6; 277.5 + 651.8 - 361.7 = 567.6; 86.2 + 651.8 - 185.6 = 552.4.
- Cash interest: 129.4 + 177.9 - 137.1 = 170.2; 79.1 + 177.9 - 85.9 = 171.1; 48.1 + 177.9 - 65.3 = 160.7. Cover: 536.6 / 170.2 = 3.15x; 177.9 basis 651.8 / 177.9 = 3.66x.
- Liquidity: 214.8 + 1,029.6 = 1,244.4; revolver 1,200.0 - 170.0 - 0.4 = 1,029.6.
- Debt stack: 669.3 + 515.3 + 600.0 + 528.1 + 170.0 + 465.0 + 83.0 = 3,030.7; less 17.6 deferred costs equals 3,013.1; variable-rate 528.1 + 170.0 + 465.0 + 83.0 = 1,246.1.
- FY2025 adjusted EBITDA: -101.1 + 183.9 - 60.0 + 521.6 = 544.4; 544.4 + 33.4 + 75.0 - 1.0 = 651.8.
- Free cash flow: 69.7 - 106.6 = -36.9; 474.2 - 226.3 = 247.9; 390.9 - 169.4 = 221.5.
- Chlor Alkali bridge: -72.2 - 55.3 - 42.0 - 36.1 - 32.1 - 12.1 + 59.2 = -190.6, equal to 80.2 - 270.8.
- Claim counts: 16 claims = 6 directly sourced + 7 calculated + 1 assumption-based + 1 analyst inference + 1 conflict. Issues: 17 = 0 Critical + 5 Material + 12 Minor.
- Principal basis leverage: 3,030.7 / 536.6 = 5.648, shown as 5.65x.
- Interest expense basis cover: 536.6 / 176.7 = 3.04x.

## Gaps

The gaps ledger lists five follow-up sources. Limits of this validation: it checked locators and figures against the seven pinned sources by opening cited pages and recomputing; it did not and could not check claims about documents not in the pack, such as the credit agreement, indentures and merger agreement. The check of page references was run on every cited figure in the four handoffs, and values not found on a cited page were reviewed one by one; those were derived values or the five locator errors logged above.

## Next module

This is the final module of the minimum set. The run proceeds to delivery of the report. Carry to any reader: committee use is restricted to the standalone financial base; the five locator errors are cosmetic; the open items are the executed debt documents, the merger agreement, Huntsman data, the proxy statement and the Q4 2025 earnings release.
