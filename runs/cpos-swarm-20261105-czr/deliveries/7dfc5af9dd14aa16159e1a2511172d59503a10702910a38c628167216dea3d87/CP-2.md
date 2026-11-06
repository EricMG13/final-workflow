# CP-2 — Fundamental credit synthesis: Caesars Entertainment, Inc. (czr)

## Request

Caesars Entertainment, Inc. (issuer id `czr`), as of 2026-11-05, pathway `credit_snapshot`, asks for the fundamental credit view from the upstream financial base and the business and transaction context. Scope is the consolidated company in USD millions for FY2025 and the first three quarters of 2026, with no peer ranking, instrument recommendation or recovery conclusion.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_czr-20251231.htm.jsonl | bc64a6b58a2e5481a0cfade7eea5b0ab2abc3801003c4d6cb677785a5aa59468 | Audited FY2025 statements; lease schedule and covenant text used for the lease maturities |
| 10-Q_2026-03-31_czr-20260331.htm.jsonl | 5678521031e1645ef46bac311c4cabf43977488c6d11dfa25cc00a4f23b2d8a8 | Q1 2026 balance sheet and liquidity table |
| 10-Q_2026-06-30_czr-20260630.htm.jsonl | c1584ea1247740f06c0dd4b0a8964b1753f8cc5c74266698804a67fd5a8dafb5 | Q2 2026 balance sheet and liquidity table |
| 10-Q_2026-09-30_czr-20260930.htm.jsonl | 020dbbd4c466f93db126b9e9ea0f09672470d3e5caa33fd667f739807400c48f | Q3 2026 debt note, covenants, liquidity, market risk, merger note |
| EX-99.1_2026-04-28_ex991-2026q1ceiearningsrel.htm.jsonl | 7471385a5ad76519a93a6fc4a1f0048a88c7bfb7676d6a0b6e78c8e1a9e19c13 | Q1 2026 release (supporting) |
| EX-99.1_2026-07-28_ex991-2026q2ceiearningsrel.htm.jsonl | 89cd5ad8c7a0d45cdf4a8f6462fc3964a9e7d04aae46811b1f50bebeb80c1762 | Q2 2026 release (supporting) |
| EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm.jsonl | 72e92043d95db7701dbaee10509a03094dd97f5a7811f25a956ad12661393bcd | Q3 2026 release; net debt and liquidity (supporting) |
| context | fb12b9963cea633059e88f881abb925ca379a0e095eca4255a6e391fb14bd7dc | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | c01a0b9e9e4166e7f52e7361ee900e87238ecbbd00650638eadf7c06ae6c64f6 | Source readiness and limits |
| CP-1 | 6f42bc51c5bc5a08912d413aa5d25707c1ac86c243459556cabc2f214da86103 | Financial base: debt, leases, liquidity, maturities, ratios |
| CP-1A | d8c3812ab1cbd44380e397ef49c9c4d183e8a7183258fd41e4491f94ed87bb42 | Business, ownership, merger terms, governance behaviour, conflicts |

Locators in tables are `page:N` of the pinned `.jsonl` text, not printed page numbers. Consistency with upstream: this answer agrees with CP-0, CP-1 and CP-1A. It adds the lease payment schedule from the annual report and a few new calculations, all shown below; it corrects no earlier handoff.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Caesars is liquid but lease-burdened: debt-only leverage of 3.26x looks moderate, while cash interest cover including lease rent is 1.69x. The pending acquisition leaves the future of the existing debt open. | Medium | Merger financing, covenant ratio values and the debt documents are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Liquidity was USD 2,947 million at Q3 2026 with the revolver undrawn, and no notes mature before 2029. | The near-term cushion is adequate, and the refinancing pressure is in 2029 and 2030. | Medium |
| Lease financing obligations of USD 13,188 million sit outside debt and take leverage to 6.95x. | Fixed lease claims outweigh the debt claims and limit room to absorb weaker earnings. | Medium |
| Adjusted EBITDA for nine months 2026 was USD 2,672 million against USD 2,723 million, with Las Vegas weaker and Regional and Digital stronger. | Earnings are slipping while fixed charges are stable. | Medium |
| The acquisition needs antitrust and gaming approvals, and the sources do not describe its financing or how existing debt is treated. | Change-of-control effects on the notes and loans cannot be assessed. | Low |

### Credit view

Caesars Entertainment, Inc. is a liquid but lease-burdened credit: debt-only leverage of 3.26x looks moderate, yet fixed-charge cover is thin and the change of control leaves the debt outlook open. The strongest support is liquidity of USD 2,947 million, an undrawn revolver and a first notes maturity only in 2029. The weakest point is fixed charges: USD 13,188 million of lease financing obligations sit outside debt, lifting leverage to 6.95x and holding cash interest cover to 1.69x while Adjusted EBITDA slipped to USD 2,672 million for nine months 2026. What decides the outcome is how the pending acquisition is financed and whether the existing notes and loans stay in place, which the supplied sources do not say.

### Credit assessment

| Assessment | Category | Confidence | Basis |
| --- | --- | --- | --- |
| Fundamental view: adequate liquidity and a moderate debt-only profile, offset by thin all-in fixed-charge cover, softening Las Vegas earnings and an unresolved change of control. Not a rating and not a recommendation. | Analyst Interpretation | Medium (below High because the merger financing, covenant definitions and agreements are not supplied) | CP-1 debt, lease, liquidity and ratio figures; CP-1A transaction, segment and governance rows |

### Key findings

First, liquidity is adequate. Caesars Entertainment, Inc. held USD 864 million of unrestricted cash and USD 2,083 million of revolver availability on the company basis at September 30, 2026, together USD 2,947 million, and the CEI revolver was undrawn after USD 160 million was drawn at December 31, 2025 [CP-1]. No notes mature before 2029. Debt falling due is USD 28 million in the remainder of 2026, USD 114 million in 2027 and USD 646 million in 2028, which is mostly the CEI Term Loan A of USD 609 million; the CEI revolver and that term loan both mature on January 31, 2028. Nothing matures within twelve months of the as-of date beyond scheduled amortisation, so the 2028 date becomes a current-year issue from early 2027 (Documentary Fact and Analyst Interpretation).

Second, the lease structure is the main fixed claim. Long-term financing obligations to VICI and GLPI of USD 13,188 million sit outside the USD 11,659 million of debt, and the lease payment schedule at December 31, 2025 shows USD 1,392 million in 2027, USD 1,424 million in 2028 and USD 1,446 million in 2029 [CP-1; annual report]. Lease cash interest of about USD 1,371 million over the last twelve months compares with USD 741 million of cash interest on debt. Adjusted EBITDA excludes this rent, so total debt plus financing obligations over Adjusted EBITDA is 6.95x against 3.26x for debt alone, and Adjusted EBITDA over all cash interest is 1.69x. Adjusted EBITDA less purchases of property and equipment of USD 664 million gives USD 2,909 million against USD 2,112 million of cash interest, or 1.38x (calculated). Net loss attributable to Caesars was USD 533 million over the last twelve months.

Third, leverage is flat to slightly better on debt and slightly worse once leases are counted. Debt-only leverage moved from 3.29x at FY2025 to 3.26x at Q3 2026 as debt fell by USD 246 million, while the lease-inclusive ratio moved from 6.90x to 6.95x because the financing obligation grew by USD 92 million and last-twelve-months Adjusted EBITDA fell from USD 3,624 million to USD 3,573 million [CP-1]. The company explains that in the early years of these leases cash payments are below the interest expense recognised, so the obligation increases.

Fourth, earnings are mixed by segment. Las Vegas Adjusted EBITDA was USD 1,179 million for nine months 2026 against USD 1,281 million, attributed by the company to fewer city-wide convention events and lower leisure visitation, while Regional rose to USD 1,447 million from USD 1,385 million, helped by the Caesars Windsor consolidation from March 3, 2026, and Caesars Digital rose to USD 181 million from USD 151 million [CP-1; CP-1A]. Las Vegas carries the highest segment margin, so its softness weighs more than its revenue share of 35.3% suggests (Analyst Interpretation).

Fifth, refinancing risk is concentrated. Maturities of USD 1,574 million in 2029 and USD 3,962 million in 2030 together are USD 5,536 million, 47.5% of face debt of USD 11,659 million, and variable-rate borrowings of USD 5.8 billion are about half of debt with no derivatives held [CP-1]. A move of 1.00% in the base rate would change annual cash interest on that variable debt by about USD 58 million (calculated, before any floors), against USD 741 million of cash interest on debt over the last twelve months.

Sixth, the pending acquisition is the largest open item. The agreement was signed on May 27, 2026 at USD 31.00 per share in cash, stockholders approved it on September 22, 2026, and closing needs antitrust and gaming approvals, with an initial end date of May 27, 2027, extendable to November 27, 2027 [CP-1A]. A USD 200 million fee is payable by the company in specified circumstances and a USD 450 million fee by the buyer in others. The sources do not describe merger financing, the equity contribution, rollover terms or the treatment of the CEI Credit Agreement, the notes or the Caesars Virginia facilities at closing. That is a missing datapoint, not an adverse finding (Insufficient Information).

Seventh, covenant headroom cannot be measured. The CEI revolver and Term Loan A carry a maximum net total leverage ratio of 6.50:1 and a minimum fixed charge coverage ratio of 2.0:1, the Caesars Virginia facilities 4:1 and 1.05:1, and the GLPI Leases a minimum adjusted revenue to rent ratio of 1.20:1, with compliance stated at September 30, 2026 but no ratio values printed. The ratios computed here are not covenant ratios and must not be compared with those levels (Insufficient Information).

### Strengths and weaknesses

Strengths. (1) Liquidity and no near-term maturity wall: USD 2,947 million of liquidity against USD 142 million of scheduled principal through 2027, with the revolver undrawn (Documentary Fact; CP-1). (2) Diversified footprint and a growing digital segment: 54 properties in 20 jurisdictions, Regional at 50.1% and Las Vegas at 35.3% of FY2025 net revenues, and Caesars Digital Adjusted EBITDA up to USD 181 million for nine months 2026 (Documentary Fact; CP-1A). (3) Conservative capital return and debt direction: no cash dividends, no share repurchases in nine months 2026, debt down USD 246 million since FY2025 and asset sale proceeds applied to redeeming the 2027 notes (Documentary Fact; CP-1A). (4) Moderate debt-only leverage of 3.26x and debt-only cash interest cover of 4.82x (Analyst Interpretation on company Adjusted EBITDA; CP-1). (5) Stockholder approval of the merger removes one execution uncertainty (Documentary Fact; CP-1A).

Weaknesses. (1) Fixed lease claims outside debt: USD 13,188 million of financing obligations and about USD 1,371 million a year of rent cash interest, leaving all-in cover of 1.69x and lease-inclusive leverage of 6.95x (Documentary Fact and calculation; CP-1). (2) Earnings drift and net losses: Adjusted EBITDA of USD 2,672 million against USD 2,723 million and a net loss attributable to Caesars of USD 283 million for nine months 2026, with the Las Vegas segment, which has the highest margin, declining (Documentary Fact; CP-1, CP-1A). (3) Refinancing concentration in 2029 and 2030 of USD 5,536 million and about half of debt at floating rates (Documentary Fact and calculation; CP-1). (4) Opaque post-closing structure: merger financing and debt treatment undisclosed, and the buyer named differently in the filings and the releases (Insufficient Information; CP-1A). (5) Covenant and agreement evidence missing: levels printed without ratio values, definitions or executed documents (Insufficient Information; CP-0, CP-1). (6) The Adjusted EBITDA add-backs, including transaction costs and other of USD 64 million for nine months 2026, are management defined, and the company says its definition may differ from those in its debt and lease agreements (Management Language; CP-1).

### Debt and claims inventory

| Claim | Amount (US$m) | Date | Inside the debt figure? | Security, guarantors, maturity | Locator |
| --- | --- | --- | --- | --- | --- |
| CEI Revolving Credit Facility (2,250 commitment) | 0 drawn | Sept 30, 2026 | Yes | Senior secured; subsidiary guarantors; January 31, 2028 | Q3 10-Q page:15 and page:17 |
| CEI Term Loan A | 609 | Sept 30, 2026 | Yes | Senior secured; subsidiary guarantors; January 31, 2028 | Q3 10-Q page:15 and page:18 |
| CEI Term Loan B | 2,012 | Sept 30, 2026 | Yes | Senior secured; subsidiary guarantors; February 6, 2030 | Q3 10-Q page:16 and page:18 |
| CEI Term Loan B-1 | 2,828 | Sept 30, 2026 | Yes | Senior secured; subsidiary guarantors; February 6, 2031 | Q3 10-Q page:16 and page:19 |
| CEI Senior Secured Notes due 2030 (7.00%) | 2,000 | Sept 30, 2026 | Yes | Senior secured; subsidiary guarantors; February 15, 2030 | Q3 10-Q page:16 and page:19 |
| CEI Senior Secured Notes due 2032 (6.50%) | 1,500 | Sept 30, 2026 | Yes | Senior secured; subsidiary guarantors; February 15, 2032 | Q3 10-Q page:16 and page:20 |
| CEI Senior Notes due 2029 (4.625%) | 1,200 | Sept 30, 2026 | Yes | Senior unsecured; subsidiary guarantors; October 15, 2029 | Q3 10-Q page:16 and page:20 |
| CEI Senior Notes due 2032 (6.00%) | 1,100 | Sept 30, 2026 | Yes | Senior unsecured; subsidiary guarantors; October 15, 2032 | Q3 10-Q page:16 and page:20 |
| CVA Delayed Draw Term Loan (up to 400) and CVA Revolving Credit Facility (25, undrawn) | 371 | Sept 30, 2026 | Yes | Secured by Caesars Virginia assets; no CEI guarantee; April 26, 2029 | Q3 10-Q page:15, page:19 and page:21 |
| Special Improvement District Bonds (4.30%) and long-term notes and other payables | 39 | Sept 30, 2026 | Yes | Bonds due 2037; security not stated | Q3 10-Q page:16 |
| Total debt (face value) | 11,659 | Sept 30, 2026 | n/a | Book value 11,563 | Q3 10-Q page:16 |
| Long-term financing obligations (VICI and GLPI failed sale-leasebacks) | 13,188 | Sept 30, 2026 | No | VICI Leases (18 casinos) and GLPI Leases (six casinos); at December 31, 2025 GLPI 1,284 and VICI 11,705, 107 not itemised | Q3 10-Q page:2 and page:36; 10-K page:117 |
| Operating lease liability | 742 | Dec 31, 2025 | No | Real estate and equipment leases | 10-K page:115 |
| Finance lease liabilities | 147 | Dec 31, 2025 | No | Equipment and real estate | 10-K page:116 |
| Sports sponsorship and partnership obligations | 309 | Sept 30, 2026 | No | Contracts through 2040 | Q3 10-Q page:15 |
| Self-insurance liability | 244 | Sept 30, 2026 | No | Within accrued other liabilities | Q3 10-Q page:15 |
| Defined-benefit pension plans (Tropicana Atlantic City: assets 33, obligations 22) | 22 | Dec 31, 2025 | No | Small; multi-employer plan withdrawal liability not found | 10-K page:140 to page:141 |
| Merger termination fee payable by the company | 200 | contingent | No | Only in specified circumstances | Q3 10-Q page:9 |
| Litigation and the Data Incident | Not material | Sept 30, 2026 | No | Company states liabilities are not material | Q3 10-Q page:15; 10-K page:121 |

No factoring or supply-chain finance programme was found in the seven sources. Debt maturities by year at September 30, 2026 (US$m): remainder of 2026 28, 2027 114, 2028 646, 2029 1,574, 2030 3,962, thereafter 5,335 (Q3 10-Q page:16). Estimated interest payments follow in the same table: 160, 780, 740, 700, 440 and 300 (total 3,120), giving total debt service of 188, 894, 1,386, 2,274, 4,402 and 5,635.

### Liquidity by facility

| Component (US$m) | Q3 2026 | Locator |
| --- | --- | --- |
| Cash and cash equivalents (unrestricted) | 864 | Q3 10-Q page:2 |
| CEI Revolving Credit Facility commitment, undrawn | 2,250 | Q3 10-Q page:50 |
| less letters of credit drawn on it | (96) | Q3 10-Q page:19 and page:50 |
| less reserves for specific permitted uses | (40) | Q3 10-Q page:17 and page:50 |
| less regulatory commitment | (56) | Q3 10-Q page:19 and page:50 |
| CVA Revolving Credit Facility commitment, undrawn | 25 | Q3 10-Q page:50 |
| Total liquidity on the company basis | 2,947 | Q3 release page:2 |
| Of which revolver availability | 2,083 | Calculated |
| Restricted cash, excluded | 94 | Q3 10-Q page:2 |

No facility expires within twelve months of the as-of date: the CEI revolver matures on January 31, 2028 and the CVA revolver on April 26, 2029. Restricted cash and the 40 and 56 held back are not counted as free liquidity in the company's own table.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity |
| --- | --- | --- | --- |
| Fixed charge burden of leases | Rent is paid ahead of debt service and is not in Adjusted EBITDA; the financing obligation rises while payments are below recognised interest | Thin all-in cover of 1.69x means a modest EBITDA decline sharply reduces cover; lessor remedies are not supplied | Critical |
| Change of control and undisclosed financing | Buyer financing and the treatment of existing debt are not described; the filings list the risk of increased leverage | Debt could be repaid, assumed or re-levered; the outcome cannot be judged from the sources | Critical |
| Las Vegas softening | Convention and leisure visitation fall, hotel occupancy 89.1% against 91.6% in Q3 2026 | Highest-margin segment, tied to the VICI Las Vegas lease, weakens | Material |
| Refinancing in 2029 and 2030 | USD 5,536 million falls due in two years and about half of debt floats | Market access and rates decide the cost; a stable owner or a deal failure changes who bears it | Material |
| Covenant visibility | Levels printed, ratios not; Adjusted EBITDA definition differs from agreements | Headroom is unknown; an EBITDA decline could reach a test not visible here | Material |
| Regulatory and execution risk of the merger | Antitrust and gaming approvals, possible asset sales, litigation | Delay or failure extends the standalone case; a USD 200 million fee could fall on the company | Material |

### Event calendar after the as-of date

| Date | Event | Source note |
| --- | --- | --- |
| Nov 2026 | VICI lease CPI escalation takes effect each November | Q3 10-Q page:51 |
| Feb 2027 | The CEI revolver and Term Loan A (maturity January 31, 2028) fall within twelve months | Q3 10-Q page:18 |
| May 27, 2027 | Initial end date of the Merger Agreement (extendable to Aug 27 and Nov 27, 2027) | Q3 10-Q page:8 |
| June 26, 2027 | Ticking fee date for merger consideration | Q3 10-Q page:7 |
| Nov 2027 | Next VICI variable rent adjustment lease year begins | Q3 10-Q page:51 |

These are contract terms and scheduled dates, not events that have occurred. Nothing is supplied after October 27, 2026.

## Calculations

All inputs in USD millions from CP-1 or the cited pages. Ratios are on company Adjusted EBITDA and face debt and are not covenant ratios.

- Revolver availability, company basis, Q3 2026: 2,250 - 96 - 40 - 56 + 25 = 2,083; plus cash 864 = 2,947 (matches the Q3 release).
- Scheduled principal through 2027: 28 + 114 = 142.
- Share of debt maturing in 2029 and 2030: (1,574 + 3,962) / 11,659 = 5,536 / 11,659 = 47.5%.
- Variable-rate sensitivity: 5,800 x 1.00% = 58 per year, before floors and with no derivatives; 58 / 741 = 7.8% of last-twelve-months cash interest on debt.
- Adjusted EBITDA less purchases of property and equipment, last twelve months: 3,573 - 664 = 2,909. Cover of all cash interest: 2,909 / (741 + 1,371) = 2,909 / 2,112 = 1.38x.
- Cash fixed charges over Adjusted EBITDA: (741 + 1,371) / 3,573 = 59.1%.
- Lease payments by year at December 31, 2025 (GLPI Leases plus VICI Leases): 2027 117 + 1,275 = 1,392; 2028 119 + 1,305 = 1,424; 2029 120 + 1,326 = 1,446; 2030 122 + 1,346 = 1,468; total future payments 4,719 + 48,140 = 52,859. Contract totals, not commitments to pay in those exact amounts after escalators.
- Lease and debt service for 2027: 894 (debt service at September 30, 2026) + 1,392 (lease payments at December 31, 2025) = 2,286; the two dates differ.
- Leverage change: debt 11,905 - 11,659 = 246; financing obligation 13,188 - 13,096 = 92; LTM Adjusted EBITDA 3,573 versus 3,624 = -51.
- Restated from CP-1 for reference: total debt / EBITDA 11,659 / 3,573 = 3.26x; (11,659 + 13,188) / 3,573 = 6.95x; 3,573 / (741 + 1,371) = 1.69x; debt-only cover 3,573 / 741 = 4.82x.

## Gaps

| Gap | Why it matters | Affects | Severity | Action |
| --- | --- | --- | --- | --- |
| Merger financing, equity contribution, rollover terms and treatment of existing debt not supplied | Determines post-closing leverage and whether existing debt survives | Credit view, refinancing | High | Obtain the Merger Agreement exhibit, proxy statement and financing commitments |
| Covenant ratio values and definitions not supplied | Headroom cannot be measured; computed ratios are not covenant ratios | Covenant risk | High | Obtain compliance certificates and the CEI Credit Agreement |
| Executed credit agreement, indentures and VICI and GLPI leases not supplied | Lessor remedies, cross-defaults, change-of-control and lease covenant terms unknown | Structure, claims | High | Obtain executed documents and amendments |
| Lease detail by landlord only at December 31, 2025; 107 of the 13,096 balance not itemised | Later lease cash and balance split cannot be built | Fixed charge analysis | Medium | Request later lease schedule |
| Acquirer identity: Fertitta Gaming Holdco, LLC against Fertitta Entertainment, Inc. | Obligor and support analysis after closing | Change of control | Medium | Confirm from the Merger Agreement |
| Regulatory approvals received to date not stated; nothing supplied after October 27, 2026 | Timing of closing | Event calendar | Medium | Obtain later Form 8-K filings |
| Adjusted EBITDA is management defined; no bridge to covenant EBITDA; no pro forma for Windsor and Grand Bazaar | Leverage and cover could differ | Ratios | Medium | Treat ratios as indicative |
| Guarantor names, restricted group and Special Improvement District Bond security not supplied | Structural subordination analysis | Structure | Medium | Obtain guarantor exhibit and indentures |
| Withdrawal liability for multi-employer pension plans not found | Possible unrecorded claim | Claims outside debt | Low | Request disclosure |
| No external ratings, market prices or peer data; no outside material used | Not required for this scope | Relative value (not in scope) | Low | None |

## Next module

- CP-5: trace each CP-2 figure to its CP-1 figure or page locator; mark the ratios in the Calculations section as calculated (1.38x, 47.5%, 58, 59.1%); confirm the lease schedule figures against 10-K page:117; check the stated sign and direction of every comparison.
- Downstream use: carry the unresolved change of control, the missing covenant ratios and the 6.95x and 1.69x lease-inclusive measures as restrictions; do not treat the debt-only 3.26x as the whole leverage picture.
