## Request

Issuer: BIOMARIN PHARMACEUTICAL INC (issuer id bmrn; Nasdaq ticker BMRN). As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Pathway: credit_snapshot. Reporting currency: USD. The filed statements are in thousands of US dollars and the MD&A and releases in millions; this handoff keeps thousands in the financial tables and US$m only where a chart selector asks for it. Current period: Q3 2026 (quarter ended 2026-09-30). Prior period named by the context: FY2025.

Scope of this module: the financial base for the credit snapshot. It sets out the reported statements, the derived earnings, leverage, interest cover, liquidity and maturity figures with every derivation shown, the debt register, claims outside debt, covenants, and the limits that the upstream source-readiness handoff carried forward (perimeter break from the Amicus acquisition, no executed legal documents, no printed covenant ratios, no combined pro forma earnings). It gives no investment opinion. The reporting entity is BioMarin Pharmaceutical Inc. and its wholly owned subsidiaries, consolidated (Q3 10-Q page:11). Period labels used throughout: FY2025 (year to 2025-12-31); 9M 2025 and 9M 2026 (nine months to 2025-09-30 and 2026-09-30); Q3 2025 and Q3 2026 (three months); LTM Q3 2026 (derived as FY2025 + 9M 2026 - 9M 2025). The context's blanks (borrower, parent, guarantors, ratings, quotes, deal terms) are treated as not supplied, never as zero.

## Sources

### Issuer sources relied on

The locator `page:N` is the extraction chunk, not the printed page. The sha256 is the pinned file hash.

| Source name | sha256 | Use in this handoff |
| --- | --- | --- |
| 10-K_2025-12-31_bmrn-20251231.htm.jsonl | ea07c0b0ced62ce928418e33e7850bb4f7657797e8c0bf5f5000905677fe1e06 | Audited FY2025 statements (page:181-184), leases (page:203-204), 2027 Notes terms (page:206), debt risk factor (page:99), cash and investments (page:159) |
| 10-Q_2026-03-31_bmrn-20260331.htm.jsonl | 2a99ceccd25eef82b99d8805175210aaa89ec2399f72c136d49401e8ef68101d | Q1 2026 statements (page:8-10), 2024 revolver and escrow (page:13, page:17, page:39) |
| 10-Q_2026-06-30_bmrn-20260630.htm.jsonl | ab3790f631c592e337d10380a75780f5e20242f4c9bb7ba84f7627e0f0826177 | Six-month 2026 statements (page:8, page:10), debt at 2026-06-30 (page:20), revolver termination (page:43) |
| 10-Q_2026-09-30_bmrn-20260930.htm.jsonl | d37c2b4920de3198d70881c8f1da80a4e23e61a15cd3750a74ed566c3cf812ae | Latest statements (page:8-10), acquisitions (page:14-18), debt (page:22-25), commitments (page:32-33), subsequent events (page:34), liquidity and covenants (page:45-52) |
| EX-99.1_2026-05-04_earningsrelease-4may26ex991.htm.jsonl | 4342224974b87cfa461fd3f7cf30a3f9e47704c85d4929187beb8b8d81373433 | Q1 release; cross-check of Q1 revenue only (page:1) |
| EX-99.1_2026-08-06_earningsrelease-6aug26ex991.htm.jsonl | 5716fe1e56e2ba465f10bd50a733773a00cfbe4f0196fc4b254c96006e5e867a | Q2 release; context only (page:1) |
| EX-99.1_2026-11-02_earningsrelease-2nov26ex991.htm.jsonl | 9fad7cb025a49338e77589bbc1ee8b206ca16d3ad7a77a9450a90d585d60fed5 | Q3 release: management highlights, non-GAAP reconciliation, updated guidance (page:4-5, page:11-12); management claims, not filed statements |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 91b63adad7def6728b9cd684c48c1a1c49d1718a8dc5d8773455a7dcffcc69fa | Run settings only; not issuer evidence |

### Supplied handoffs

| Module | sha256 | How used |
| --- | --- | --- |
| CP-0 | 519d600f8cd9aa5d9447d6aad10dd44114b4ff6da47448fda0a16df0ed1715f3 | Source readiness: READY_WITH_LIMITATIONS for this module. Its limits are carried forward: perimeter break from 2026-04-27, no executed legal documents, covenant ratios not printed, guarantors unnamed, no pro forma combined earnings, IPR&D reclassified in 2026, extraction fidelity not reviewed. Its debt and liquidity figures were reopened against the sources and agree with them; where this handoff adds to it, the addition is stated under Gaps |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Debt rose from 600,000 thousand to 4,235,000 thousand after the Amicus acquisition. Cash is 736.0 million plus an undrawn 600.0 million revolver. Leverage on trailing filed earnings looks high but includes only part of Amicus and large research charges. | Medium | No combined earnings base, covenant ratios or legal documents are supplied, so true run-rate leverage and covenant headroom cannot be measured. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| The 2026 financing added 5.5% notes in February and secured term loans in April; the 2027 convertible notes mature in May 2027. | A 660.0 million repayment falls due in 2027 on a derived schedule; the next large maturities are in 2031 and 2033. | High |
| Trailing earnings from filed statements understate the combined business: Amicus counts from 2026-04-27 only, and Q3 carries a 287,685 thousand acquired research charge. | Reported leverage of 11.18x likely overstates run-rate leverage; adjusted figures are shown but are analyst-derived. | Medium |
| Cash fell from 1,311,679 thousand to 736,007 thousand as investments were liquidated to fund the deal. | Liquidity now rests on cash plus the undrawn revolver, subject to covenant compliance. | High |
| Maintenance tests of 3.50x net leverage and 3.00x interest coverage apply to the Term Loan A and revolver; compliance is stated but ratios are not printed. | Headroom is not measurable from the pack. | High |
| Cash interest paid so far understates the new interest burden, because the first coupon date on the 2034 Notes was August 15, 2026. | Cover of 5.43x on cash interest flatters the run-rate position. | Medium |

### Financial base view

The financial base is usable for the credit snapshot but it is a two-perimeter base, and every ratio must be read with that in mind. FY2025 is the audited pre-Amicus company with 600,000 thousand of convertible notes, net cash after investments and a derived EBITDA of 489,035 thousand. From 2026-04-27 the company consolidates Amicus, funded by 850,000 thousand of 5.5% notes, 2,800,000 thousand of secured term loans (since reduced to 2,785,000 thousand by one quarterly repayment on each loan) and cash on hand, so principal debt at 2026-09-30 is 4,235,000 thousand. Earnings on the new perimeter are only partly in the trailing twelve months. On the filed numbers, derived EBITDA for LTM Q3 2026 is 378,821 thousand, which gives total debt to EBITDA of 11.18x and net debt to EBITDA of 9.24x. Two items depress that EBITDA and are not recurring in the same way: the LTM includes impairment of assets and a ROCTAVIAN inventory write-off of 119,208 booked in the fourth quarter of 2025 (10-K page:155), and it includes acquired IPR&D expense of 287,685 thousand in Q3 2026. Adding those back, as an analyst-derived measure and not a company figure, gives 922,962 thousand, total debt to EBITDA of 4.59x and net debt to EBITDA of 3.79x. Neither figure is pro forma for a full year of Amicus, and the covenant definition, which is not printed, may differ from both. Cash interest cover is 5.43x on the filed LTM basis but cash interest of 69,721 thousand is not a run-rate: annualised Q3 coupon interest is 210,732 thousand. Liquidity at 2026-09-30 is cash of 736.0 million plus 600.0 million undrawn on the senior secured revolver, a total of 1,336.0 million. The 2027 Notes of 600,000 thousand are the next large maturity and are due in May 2027. The company states that the compliance tests on Term Loan A and the revolver were met. The view is therefore a clear debt and liquidity picture with an unresolved earnings run-rate, and the earnings gap is the main limit on every leverage conclusion.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 1.23 | -2.97 | x | EBITDA is income from operations 409,478 plus depreciation and amortization 79,557 = 489,035 thousand USD (10-K page:182-183). Debt is principal of the 2027 Notes, 600,000 (10-K page:99). Net debt subtracts cash 1,311,679 and investments 741,172, so a negative value is net cash. Pre-Amicus. EBITDA is after 125,012 impairment, 119,208 ROCTAVIAN write-off and 220,963 acquired IPR&D; adding these back gives 0.63x and -1.52x |
| LTM Q1 2026 | 3.73 | -1.99 | x | LTM = FY2025 + Q1 2026 - Q1 2025; EBITDA 389,124. Debt is 600,000 + 850,000 of 2034 Notes at 2026-03-31, with the Amicus close still to come (Q1 10-Q page:17). Net debt subtracts cash 2,222,435 only; the 850,000 restricted escrow is not deducted (Q1 10-Q page:8, page:13). Adding back as above gives 1.70x and -0.91x |
| LTM Q2 2026 | 14.06 | 11.17 | x | LTM = FY2025 + 6M 2026 - 6M 2025; EBITDA 302,232. Debt 4,250,000 at 2026-06-30 (Q2 10-Q page:20); cash 874,005. Amicus is in the debt for the full amount but in earnings for two months only. Adding back as above gives 5.56x and 4.42x |
| LTM Q3 2026 | 11.18 | 9.24 | x | LTM = FY2025 + 9M 2026 - 9M 2025; EBITDA 378,821 thousand USD. Debt 4,235,000 (Q3 10-Q page:22); cash 736,007 (page:8); net debt 3,498,993. Amicus in earnings from 2026-04-27 only, and no pro forma EBITDA is supplied. Adding back impairment 137,248, write-off 119,208 and acquired IPR&D 287,685 (analyst-derived, not a company measure) gives EBITDA 922,962, 4.59x and 3.79x. The covenant ratio is defined differently and is not printed |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 67.50 | x | EBITDA 489,035 divided by cash paid for interest 7,245 thousand USD (10-K page:184). Pre-Amicus; the only debt was the 1.25% convertible notes |
| LTM Q1 2026 | Not supplied: the Q1 2026 10-Q prints cash paid for income taxes but not cash paid for interest, for either Q1 2026 or Q1 2025 | x | The LTM cash interest cannot be built without the Q1 amounts (Q1 10-Q page:10) |
| LTM Q2 2026 | 41.27 | x | EBITDA 302,232 divided by LTM cash interest 7,324 = 7,245 + 3,716 - 3,637 (Q2 10-Q page:10). Term loan interest began only in late April 2026 and the 2034 Notes coupon was first paid on 2026-08-15, so this ratio predates the new interest burden |
| LTM Q3 2026 | 5.43 | x | EBITDA 378,821 divided by LTM cash interest 69,721 = 7,245 + 66,048 - 3,572 (Q3 10-Q page:10). Not a run-rate: accrued interest of 37,480 was unpaid at 2026-09-30 (page:20) and Amicus is in EBITDA from 2026-04-27 only. Annualised Q3 coupon interest of 210,732 gives 1.80x on this EBITDA and 4.38x on the 922,962 adjusted EBITDA (analyst-derived) |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 1311.7 | 600.0 | US$m | Cash and cash equivalents 1,311,679 thousand (10-K page:182). Undrawn is the 2024 unsecured revolver of 600.0 million, nothing outstanding (10-K page:99). Short-term investments 248.9 and long-term investments 492.2 are excluded from the cash column (10-K page:159); total with investments is 2,652.9 including the revolver. Letters of credit under the revolver: none stated |
| Q1 2026 | 2222.4 | 600.0 | US$m | Cash 2,222,435 thousand (Q1 10-Q page:8). Undrawn is the 2024 revolver, nothing outstanding at 2026-03-31 (Q1 10-Q page:39). Restricted cash equivalents of 850.0 million held in escrow for the Amicus consideration are excluded (Q1 10-Q page:13) |
| Q2 2026 | 874.0 | 600.0 | US$m | Cash 874,005 thousand (Q2 10-Q page:8). Undrawn is the 2026 revolver, nothing outstanding at 2026-06-30 (Q2 10-Q page:43); the 2024 revolver was terminated (page:43). Availability is subject to borrowing conditions |
| Q3 2026 | 736.0 | 600.0 | US$m | Cash 736,007 thousand (Q3 10-Q page:8), no investments held (page:45). Undrawn 600.0 million of the 2026 Revolving Facility, matures April 2031 (page:25, page:48), subject to compliance with the credit agreement. Total 1,336.0 million. No letters of credit drawn on the revolver are stated; the 10-K notes standby letters of credit secured by restricted investments, amount not supplied (10-K page:202) |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q4 2026 | 15.0 | US$m | Term Loan A 10.0 and Term Loan B 5.0 quarterly amortization (Q3 10-Q page:24). Derived schedule; the payment dates are not printed and are assumed to fall at calendar quarter ends, consistent with one payment each made in Q3 2026 |
| 2027 | 660.0 | US$m | 2027 Notes 600.0 due May 2027 (page:22) plus four quarters of term loan amortization, 40.0 on Term Loan A and 20.0 on Term Loan B. The notes are convertible at 137.47 per share (10-K page:206); if not converted they are payable in cash (page:48) |
| 2028 | 60.0 | US$m | Term loan amortization only, 40.0 plus 20.0 |
| 2029 | 60.0 | US$m | Term loan amortization only |
| 2030 | 60.0 | US$m | Term loan amortization only |
| 2031 | 640.0 | US$m | Term Loan A remaining 620.0 including the first-quarter payment, due 2031-04-27 (page:24), plus Term Loan B amortization 20.0. The 600.0 million revolver also matures in April 2031 and is undrawn |
| 2032 | 20.0 | US$m | Term Loan B amortization only |
| 2033 | 1870.0 | US$m | Term Loan B remaining balance including the first-quarter payment, due 2033-04-27 (page:24) |
| 2034 | 850.0 | US$m | 5.5% senior unsecured notes due 2034-02-15 (page:25). Schedule total 4,235.0 equals principal at 2026-09-30; excludes any mandatory prepayments, which are not described in the pack |

### Financials and credit metrics

Thousands of USD unless the row says otherwise. LTM Q3 2026 is derived. Q3 cash flow items are not printed, because the cash flow statement is year to date; the Q3 EBITDA cells are derived by difference.

| Metric | FY2025 | 9M 2025 | 9M 2026 | LTM Q3 2026 | Q3 2025 | Q3 2026 | Locator and note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Total revenues | 3,221,253 | 2,346,688 | 2,780,562 | 3,655,127 | 776,133 | 1,024,646 | 10-K page:181; Q3 10-Q page:8; LTM derived |
| Cost of sales | 717,442 | 441,733 | 603,210 | 878,919 | 140,085 | 205,416 | Same; 9M 2026 includes inventory step-up amortization of 29.2 million (page:17) |
| Research and development, excluding acquired IPR&D | 700,967 | 508,554 | 566,273 | 758,686 | 188,515 | 180,525 | FY2025 derived as 921,930 less 220,963 because the 10-K shows R&D including IPR&D (10-K page:181, page:225) |
| Acquired IPR&D | 220,963 | 220,963 | 287,685 | 287,685 | 220,963 | 287,685 | Q3 10-Q page:8; Inozyme in Q3 2025 (10-K page:225); Alesta in Q3 2026 (page:18) |
| Selling, general and administrative | 1,153,017 | 706,810 | 987,482 | 1,433,689 | 268,415 | 333,643 | 10-K page:181; Q3 10-Q page:8 |
| Intangible asset amortization | 19,386 | 14,540 | 177,433 | 182,279 | 4,847 | 99,458 | Same |
| Income (loss) from operations | 409,478 | 454,088 | 158,479 | 113,869 | (46,692) | (82,081) | 10-K page:182; Q3 10-Q page:8 |
| Depreciation and amortization (cash flow) | 79,557 | 59,119 | 244,514 | 264,952 | 18,487 | 130,465 | 10-K page:183; Q3 10-Q page:10; Q3 cells derived as 9M less 6M (Q2 10-Q page:10) |
| EBITDA, derived: income from operations plus D&A | 489,035 | 513,207 | 402,993 | 378,821 | (28,205) | 48,384 | Analyst-derived; the company reports no EBITDA. After impairments and acquired IPR&D |
| Interest expense | 10,899 | 8,121 | 133,881 | 136,659 | 2,579 | 55,628 | 10-K page:182; Q3 10-Q page:8; 9M 2026 includes a bridge commitment fee of 22,813 (page:23) |
| Net income (loss) | 348,901 | 395,474 | 27,458 | (19,115) | (30,744) | (122,831) | Same |
| Net cash provided by operating activities | 827,994 | 728,350 | 576,974 | 676,618 | Not supplied: year-to-date statement only | Not supplied: year-to-date statement only | 10-K page:184; Q3 10-Q page:10 |
| Purchases of property, plant and equipment | 103,038 | 62,316 | 78,032 | 118,754 | Not supplied: year-to-date statement only | Not supplied: year-to-date statement only | Same |
| Operating cash flow less capex (derived) | 724,956 | 666,034 | 498,942 | 557,864 | Not supplied: year-to-date statement only | Not supplied: year-to-date statement only | Derived; before 5,067,630 paid for Amicus and 277,881 for IPR&D in 9M 2026 (page:10) |
| Cash paid for interest | 7,245 | 3,572 | 66,048 | 69,721 | Not supplied: year-to-date statement only | Not supplied: year-to-date statement only | 10-K page:184; Q3 10-Q page:10 |
| Cash paid for income taxes | 96,205 | 70,208 | 74,378 | 100,375 | Not supplied: year-to-date statement only | Not supplied: year-to-date statement only | Same |

### Discrete quarters of 2026

| Quarter | Total revenues | Income (loss) from operations | Locator and note |
| --- | --- | --- | --- |
| Q1 2026 | 766,208 | 129,640 | Q1 10-Q page:8; before the Amicus close |
| Q2 2026 | 989,708 | 110,920 | Q2 10-Q page:8; Amicus from 2026-04-27 |
| Q3 2026 | 1,024,646 | (82,081) | Q3 10-Q page:8; includes 287,685 acquired IPR&D and 99,458 intangible amortization |

### Balance sheet at 2026-09-30

Total assets are 11,569,231 thousand against 7,594,022 at 2025-12-31. Intangible assets, net, rose from 213,837 to 4,777,247 and goodwill from 196,199 to 666,367 (Q3 10-Q page:8). Total liabilities are 5,313,199 against 1,507,023 and total stockholders' equity is 6,256,032 against 6,086,999 (page:9). Inventory rose from 1,298,883 to 1,796,069, including a fair value step-up of approximately 228.0 million on acquired inventory (page:8, page:17). Deferred tax assets are 897,787 against 1,508,697 (page:8). Current debt is 658,717 and long-term debt 3,514,974, net of discount and costs (page:9). The company has no segment reporting beyond one segment (page:27).

### Debt register at 2026-09-30

| Instrument | Issuer or borrower and co-issuer | Principal, thousand USD | Rate | Maturity | Security and ranking | Guarantors | Locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1.25% senior subordinated convertible notes (2027 Notes) | BioMarin Pharmaceutical Inc.; no co-issuer stated | 600,000 | 1.25% fixed, interest paid May 15 and November 15; conversion rate 7.2743 shares per 1,000 principal, 137.47 per share | May 2027 | Senior subordinated (secured status not stated) | Not supplied | Q3 10-Q page:22; 10-K page:206 |
| 5.5% senior unsecured notes (2034 Notes) | BioMarin Pharmaceutical Inc.; no co-issuer stated | 850,000 | 5.5% fixed, paid February 15 and August 15 | 2034-02-15 | Senior unsecured | Not stated in the debt note; a supplemental indenture of 2026-04-27 names unnamed guarantors, and whether it covers these notes is not stated | Q3 10-Q page:25; Q2 10-Q page:118 |
| Term Loan A | BioMarin Pharmaceutical Inc. as Borrower | 790,000 (800,000 original) | Term SOFR plus 1.75% initially, then 1.00% to 1.75% by total net leverage; alternate base rate plus 0.75% initially, then 0.00% to 0.75% | 2031-04-27; 1.25% of original principal each quarter | Senior secured, first-priority liens on substantially all assets of the Company and guarantors | Certain subsidiaries, unnamed | Q3 10-Q page:22-24, page:49-50 |
| Term Loan B | BioMarin Pharmaceutical Inc. as Borrower | 1,995,000 (2,000,000 original) | Term SOFR plus 1.75%; alternate base rate plus 0.75% | 2033-04-27; 0.25% of original principal each quarter | Senior secured, same security | Certain subsidiaries, unnamed | Same |
| 2026 Revolving Facility, 600.0 million | BioMarin Pharmaceutical Inc. | 0 drawn; 600.0 million available | Same basis as Term Loan A | 2031-04-27 | Senior secured | Certain subsidiaries, unnamed | Q3 10-Q page:25, page:48 |
| Total debt principal | | 4,235,000 | | | | | Q3 10-Q page:22 |

Less unamortized discount and deferred offering costs of 61,309 gives total debt, net of 4,173,691 (page:22). Fair value of debt is 4,167,757 (page:22-23). The bridge commitment of up to approximately 3.7 billion was reduced to 2.8 billion on the 2034 Notes issue and then to zero on entry into the term facilities (page:25). The 2024 unsecured revolver was terminated in April 2026 (Q2 10-Q page:43). The 2027 Notes are labelled senior subordinated and the term loans are first-priority secured (page:22, page:50); the full ranking of the unsecured 2034 Notes against subsidiary debt is not determinable without the guarantor list and the indentures. Of the debt, 2,785,000 is variable rate; a 100 basis point rise adds approximately 27.9 million to annual interest expense (page:52).

### Interest and run-rate evidence

Interest expense on debt for Q3 2026 was 55,233 against 2,388 in Q3 2025; coupon interest was 52,683, accretion of discount 2,063 and amortization of issuance costs 487 (Q3 10-Q page:23). Annualising the Q3 coupon interest gives 210,732 thousand. This is a derived indication of the new cost of debt, not a forecast, because the variable rate and the balances change.

### Claims outside debt

| Claim | Amount | Inside or outside the debt figure | Locator |
| --- | --- | --- | --- |
| Lease liabilities | FY2025 total 45,697 (operating 45,145, financing 552); at 2026-09-30 the current portion is 16,519 and about 53.8 million of lease liabilities were recognized on the Amicus acquisition; the total at 2026-09-30 is not supplied | Outside debt | 10-K page:203-204; Q3 10-Q page:17, page:20 |
| Firm purchase commitments | 768.8 million, of which 291.1 million in 2026 and the rest in 2027 | Outside debt | Q3 10-Q page:33, page:51 |
| Contingent license and milestone payments judged reasonably possible | 485.5 million, of which up to 7.5 million within twelve months | Outside debt | Q3 10-Q page:32 |
| Dimerix license for BMN 820 | Up to 510.0 million in milestones plus tiered royalties; may overlap the 485.5 million above, which is not stated | Outside debt | Q3 10-Q page:32 |
| Alesta milestones | Up to 215 million | Outside debt | Q3 10-Q page:18 |
| BMN 450 license (October 2026) | Upfront 70.0 million expected as Q4 2026 acquired IPR&D expense; up to 405.0 million further milestones plus royalties | Outside debt; subsequent event | Q3 10-Q page:34 |
| Restructuring accrual | 47,739 unpaid at 2026-09-30 | Outside debt, in accrued liabilities | Q3 10-Q page:30 |
| Accrued interest | 37,480 | Outside debt principal | Q3 10-Q page:20 |
| Foreign exchange forward contracts | 34,433 liability | Outside debt | Q3 10-Q page:20 |
| DOJ subpoena on sponsored testing programs for VIMIZIM and NAGLAZYME | Not quantified; company cannot assure the outcome | Outside debt | Q3 10-Q page:32 |
| Nonqualified deferred compensation plan | Liability 49,998 matched by plan assets 49,998 | Outside debt | Q3 10-Q page:20 |
| Pension and retiree medical, factoring, supply-chain finance | None disclosed: searches for pension, postretirement, retiree, factoring, supply chain financing and securitization found nothing relevant in the Q3 10-Q or the 10-K | Not applicable | All pinned sources searched |
| Unrecognized tax benefits | Stated as not materially changed from the 10-K; the amount is not extracted here | Outside debt | Q3 10-Q page:51 |

### Covenants

| Test | Level and step-down | Applies to | Reported figure and headroom | Definition note |
| --- | --- | --- | --- | --- |
| Maximum Total Net Leverage Ratio | 3.50 to 1.00, with a temporary increase to 4.00 to 1.00 in connection with certain acquisitions | Term Loan A and the 2026 Revolving Facility | Company states compliance at 2026-09-30; the ratio is not printed, so headroom is not calculable (Q3 10-Q page:50) | Defined in the 2026 Credit Agreement, which is not supplied. The net debt over EBITDA of 9.24x on filed LTM EBITDA, and 3.79x on adjusted EBITDA, are analyst measures on a part-year Amicus perimeter and are not the covenant ratio |
| Minimum Interest Coverage Ratio | 3.00 to 1.00 | Term Loan A and the 2026 Revolving Facility | Compliance stated; ratio not printed; headroom not calculable | Same; the 5.43x cash interest cover above uses cash paid for interest and is not the covenant ratio |
| Other covenants | Customary limits on debt, liens, investments, restricted payments, asset sales and affiliate transactions, with exceptions | 2026 Credit Agreement; the 2034 Notes indenture has similar customary covenants (page:25) | Not quantified | Executed documents not supplied |

The filing attaches the maintenance tests to Term Loan A and the revolver and does not mention them for Term Loan B. The terminated 2024 revolver carried a similar pair of tests, with compliance stated at 2026-03-31 (Q1 10-Q page:39). No ratings are supplied and none are disclosed in any pinned source for the company or its debt.

### Latest quarter and after

Q3 2026 events with amounts: the Alesta acquisition closed on 2026-08-31 for 303.4 million total consideration, with 282.3 million recorded as acquired IPR&D (Q3 10-Q page:18); the Ascendis settlement of 2026-08-30 grants BioMarin royalties (Q3 release page:3); term loan repayments totaled 15,000 in the nine months (page:10); and Amicus integration restructuring severance was 29,478 in Q3 (page:30). After quarter end: the October 2026 BMN 450 license (page:34); on 2026-11-02 the company lowered full-year revenue guidance from 3,875 to 3,925 million to 3,800 to 3,900 million and non-GAAP diluted EPS guidance from 4.90 to 5.10 to 2.80 to 3.10, citing order timing and two acquired IPR&D charges, with the Alesta and BMN 450 pre-tax charges estimated at about 320 million and 83 million for 2026 (Q3 release page:5). These are management claims. The guidance midpoint implies growth of about 20 percent over FY2025 revenue of 3,221.3 million, consistent with the release (3,850 divided by 3,221.253). Upcoming regulatory dates are 2027-02-28 for full approval of VOXZOGO in achondroplasia and 2027-05-30 for hypochondroplasia (Q3 release page:2), scheduled dates and not facts. No event after 2026-11-05 is used.

### Pro forma and perimeter

Amicus contributed revenue of 336,422 and a net loss of 239,383 for 2026-04-27 to 2026-09-30 (Q3 10-Q page:17). Pro forma revenue as if Amicus had been owned from 2025-01-01 is 3,009,554 for 9M 2026 and 2,795,686 for 9M 2025, with pro forma net loss of 256,017 and 57,533 (page:17). No pro forma EBITDA, interest or FY2025 figure is supplied, so a combined LTM EBITDA is Not calculable from the pack.

### Definition review

EBITDA is not reported by the company. This handoff defines it as income from operations plus the depreciation and amortization line of the cash flow statement. That D&A line is larger than the intangible amortization shown in operating expenses (177,433 in 9M 2026) and appears to include it, but the filing does not itemize the line. Inventory step-up amortization is recognized in cost of sales (29.2 million in 9M 2026, page:17) and is not separately identified in the D&A line, so EBITDA here is probably after step-up. The company's non-GAAP income adds back amortization, stock-based compensation, step-up and acquisition and restructuring costs, but does not add back acquired IPR&D (Q3 release page:12), so management itself treats the IPR&D charge as an operating cost. The adjusted EBITDA used above is therefore an analyst construct and a stricter test is the unadjusted one. Adjusted EBITDA also relies on the ROCTAVIAN inventory write-off appearing only in FY2025: no such line appears in the 2026 or 9M 2025 cash flow statements, so it is treated as nil there with that limitation; the 10-K places the write-off in the fourth quarter of 2025 (10-K page:155).

## Calculations

All inputs are in thousands of USD and come from the cited filed statements. Derived figures are analyst calculations.

| Calculation | Inputs | Result |
| --- | --- | --- |
| EBITDA FY2025 | 409,478 (10-K page:182) + 79,557 (page:183) | 489,035 |
| LTM operating income Q1 2026 | 409,478 + 129,640 (Q1 10-Q page:8) - 223,893 (same) | 315,225 |
| LTM D&A Q1 2026 | 79,557 + 16,411 - 22,069 (Q1 10-Q page:9) | 73,899 |
| EBITDA LTM Q1 2026 | 315,225 + 73,899 | 389,124 |
| LTM operating income Q2 2026 | 409,478 + 240,560 - 500,780 (Q2 10-Q page:8) | 149,258 |
| LTM D&A Q2 2026 | 79,557 + 114,049 - 40,632 (Q2 10-Q page:10) | 152,974 |
| EBITDA LTM Q2 2026 | 149,258 + 152,974 | 302,232 |
| LTM operating income Q3 2026 | 409,478 + 158,479 - 454,088 (Q3 10-Q page:8) | 113,869 |
| LTM D&A Q3 2026 | 79,557 + 244,514 - 59,119 (Q3 10-Q page:10) | 264,952 |
| EBITDA LTM Q3 2026 | 113,869 + 264,952 | 378,821 |
| Net debt FY2025 | 600,000 - (1,311,679 + 248,930 + 492,242) | -1,452,851 |
| Net debt Q1 2026 | 1,450,000 - 2,222,435 (restricted 850,000 not deducted) | -772,435 |
| Net debt Q2 2026 | 4,250,000 - 874,005 | 3,375,995 |
| Net debt Q3 2026 | 4,235,000 - 736,007 | 3,498,993 |
| Total debt / EBITDA | 600,000 / 489,035; 1,450,000 / 389,124; 4,250,000 / 302,232; 4,235,000 / 378,821 | 1.23x; 3.73x; 14.06x; 11.18x |
| Net debt / EBITDA | -1,452,851 / 489,035; -772,435 / 389,124; 3,375,995 / 302,232; 3,498,993 / 378,821 | -2.97x; -1.99x; 11.17x; 9.24x |
| Adjusted EBITDA (analyst-derived) FY2025 | 489,035 + 125,012 impairment + 119,208 write-off + 220,963 acquired IPR&D (10-K page:183) | 954,218 |
| LTM impairment Q3 2026 | 125,012 + 15,203 (Q3 10-Q page:10) - 2,967 (same) | 137,248 |
| LTM acquired IPR&D Q3 2026 | 220,963 + 287,685 - 220,963 (Q3 10-Q page:8) | 287,685 |
| Adjusted EBITDA LTM Q3 2026 | 378,821 + 137,248 + 119,208 + 287,685 | 922,962 |
| Adjusted EBITDA LTM Q1 and Q2 2026 | Q1: 389,124 + 122,045 + 119,208 + 220,963; Q2: 302,232 + 122,045 + 119,208 + 220,963, where 122,045 = 125,012 - 2,967 | 851,340; 764,448 |
| Total debt / adjusted EBITDA | 600,000 / 954,218; 1,450,000 / 851,340; 4,250,000 / 764,448; 4,235,000 / 922,962 | 0.63x; 1.70x; 5.56x; 4.59x |
| Net debt / adjusted EBITDA | -1,452,851 / 954,218; -772,435 / 851,340; 3,375,995 / 764,448; 3,498,993 / 922,962 | -1.52x; -0.91x; 4.42x; 3.79x |
| LTM cash interest Q2 2026 | 7,245 + 3,716 - 3,637 | 7,324 |
| LTM cash interest Q3 2026 | 7,245 + 66,048 - 3,572 | 69,721 |
| EBITDA / cash interest | 489,035 / 7,245; 302,232 / 7,324; 378,821 / 69,721 | 67.50x; 41.27x; 5.43x |
| Adjusted EBITDA / cash interest | 954,218 / 7,245; 764,448 / 7,324; 922,962 / 69,721 | 131.71x; 104.38x; 13.24x |
| Annualised Q3 coupon interest | 52,683 x 4 (Q3 10-Q page:23) | 210,732 |
| EBITDA / annualised coupon interest | 378,821 / 210,732; 922,962 / 210,732 | 1.80x; 4.38x |
| Q3 2026 EBITDA by difference | -82,081 + (244,514 - 114,049) | 48,384 |
| Q3 2025 EBITDA by difference | -46,692 + (59,119 - 40,632) | -28,205 |
| LTM operating cash flow less capex | 827,994 + 576,974 - 728,350 less (103,038 + 78,032 - 62,316) | 676,618 less 118,754 = 557,864 |
| Liquidity Q3 2026 | 736,007 cash + 600,000 undrawn revolver | 1,336,007 thousand, 1,336.0 million |
| Maturity schedule | Q4 2026 15; 2027 660; 2028 60; 2029 60; 2030 60; 2031 640; 2032 20; 2033 1,870; 2034 850 (US$m) | 4,235.0, equal to principal |
| Term loan A path | 790.0 - 10.0 (Q4 2026) - 4 x 40.0 (2027 to 2030) | 620.0 due in 2031 |
| Term loan B path | 1,995.0 - 5.0 - 6 x 20.0 (2027 to 2032) | 1,870.0 due in 2033 |
| Debt principal adds | 600,000 + 850,000 + 790,000 + 1,995,000; less 61,309 | 4,235,000; 4,173,691, equals the balance sheet 658,717 + 3,514,974 |
| Repayment tie | (800,000 - 790,000) + (2,000,000 - 1,995,000) | 15,000, equals repayments of borrowings in the cash flow (page:10) |
| Expense block ties to operating income, Q3 2026 | 205,416 + 180,525 + 287,685 + 333,643 + 99,458 = 1,106,727; 1,024,646 - 1,106,727 | -82,081 |
| Expense block ties, 9M 2026 | 603,210 + 566,273 + 287,685 + 987,482 + 177,433 = 2,622,083; 2,780,562 - 2,622,083 | 158,479 |
| Expense block ties, FY2025 | 717,442 + 921,930 + 1,153,017 + 19,386 = 2,811,775; 3,221,253 - 2,811,775 | 409,478 |
| LTM revenue | 3,221,253 + 2,780,562 - 2,346,688 | 3,655,127 |
| Q1 revenue cross-check | 1,755,916 (Q2 10-Q page:8) - 989,708 | 766,208, equals Q1 10-Q and the release's 766 million |
| Variable-rate debt | 790,000 + 1,995,000; 1% of that | 2,785,000; 27,850, consistent with the filing's 27.9 million (page:52) |
| Guidance midpoint growth | 3,850 / 3,221.253 (Q3 release page:5; 10-K page:181) | 1.195, about 20 percent |
| Equity less goodwill and intangibles | 6,256,032 - 666,367 - 4,777,247 | 812,418 |

## Gaps

| Gap | Effect | Remediation |
| --- | --- | --- |
| No pro forma combined EBITDA, interest or FY2025 pro forma; Amicus in earnings from 2026-04-27 only | Leverage on the filed LTM basis overstates run-rate leverage; the adjusted figures are analyst-derived and partial. Combined LTM EBITDA is Not calculable | Obtain a pro forma filing or management bridge; derive downstream and label as derived |
| Covenant ratios and definitions not printed; executed 2026 Credit Agreement and indentures not supplied | Headroom against 3.50x and 3.00x is Not calculable | Add the credit agreement and compliance certificate |
| Guarantors and guarantee status of the 2034 and 2027 Notes not stated | Structural ranking is unresolved | Add the supplemental indenture or subsidiary list |
| Cash paid for interest for Q1 2026 and Q1 2025 not printed | LTM Q1 2026 interest cover is Not supplied | None in the pack |
| Cash interest paid is not a run-rate; accrued interest 37,480 unpaid | Interest cover on cash basis flatters the position | Use the annualised coupon indication, labelled derived |
| Term loan payment dates and any mandatory prepayments, such as excess cash flow sweeps, are not printed | The maturity schedule uses an assumed calendar quarter-end timing and excludes prepayments | Add the credit agreement |
| Total lease liabilities at 2026-09-30 not printed | Lease claims are known for FY2025 only | None in the pack |
| Overlap between the 485.5 million contingent payments, Dimerix and Alesta milestones not stated | Contingent claims are listed separately and not summed | Read the license agreements |
| ROCTAVIAN inventory write-off treated as nil outside FY2025 because no line is printed | Adjusted EBITDA could be understated if a 2026 write-off sits inside another line | Check the cost of sales commentary downstream |
| Consideration for Amicus: the Q1 10-Q estimated about 5.2 billion and about 1.6 billion of cash on hand, the Q3 10-Q states 5,323,561 total and about 1.7 billion of cash (Q1 10-Q page:39; Q3 10-Q page:14, page:47) | Not a conflict in filed amounts: the Q1 text was a pre-close estimate and the Q3 figure is final consideration, with the purchase price allocation still preliminary | Use the Q3 figure |
| The 2027 Notes are called senior subordinated in the filings (Q3 10-Q page:22) but the subordination terms and security status were not read in the 10-K note | Ranking of the 2027 Notes against the 2034 Notes and the term loans is described, not tested; this adds to CP-0, which also gave only the label | Read the 10-K debt note and indenture downstream |
| Ratings, quotes and market data not supplied | No market-implied view | Supply or mark not supplied |
| Non-GAAP and guidance figures are management claims | Not used in the credit metrics | Prefer filed figures |

## Next module

Proceed to CP-1A (business and transaction context) and then CP-2 and CP-5 as the dependency planner orders them. Downstream modules should open this handoff's debt register, maturity table and chart data, use the filed LTM leverage and the adjusted LTM leverage only with their stated limits, carry the covenant, guarantor and pro forma gaps forward, keep the 2026-04-27 perimeter break explicit, and treat the 2027 Notes maturity of 600.0 million in May 2027 as the first large refinancing event. The next evidence action is to obtain the 2026 Credit Agreement, the indentures and a pro forma or management bridge for combined EBITDA.
