# CP-1 — Financial base: Bausch Health Companies Inc. (bhc)

## Request

- Issuer: Bausch Health Companies Inc. (issuer id `bhc`), as of 2026-11-05, information cutoff 2026-11-05 (context). Reporting currency USD, in millions unless stated. Current period Q3 2026, prior period FY2025 (context).
- Run: `bhc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`. This module builds the reported financial base: statements, debt, liquidity, maturities, coverage and leverage, with every derived number shown in `## Calculations`.
- Execution: host session. The host searched and read the pinned files and wrote this answer. No provider was called.
- Perimeter: the statements are consolidated Bausch Health Companies Inc., which includes Bausch + Lomb (about 87% owned, Q3 10-Q page:9). Where a source splits Bausch Health (excl. B+L) from Bausch + Lomb, the split is shown. Bausch + Lomb is an unrestricted subsidiary of the parent's debt group (Q3 10-Q page:40).
- Period labels used: Q3 2026 (three months to September 30, 2026), nine months 2026 and nine months 2025 (to September 30), FY2025 (year to December 31, 2025), LTM Q3 2026 (twelve months to September 30, 2026, built as FY2025 plus nine months 2026 less nine months 2025). The same construction gives LTM at March 31 and June 30, 2026.

## Sources

Issuer sources relied on (page-numbered text extractions pinned by CP-OS; `page:N` is the extraction chunk, not a printed page):

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_bhc-20251231.htm.jsonl | dd4233546d8f09a0a7172210eae9b856cf06217c0da999f68b6e9a8283f6671d | Form 10-K for FY2025: audited statements, debt note, interest paid, lease note |
| 10-Q_2026-03-31_bhc-20260331.htm.jsonl | 2ab4f9a58a29bd8e4f27c1aaa3b34a916ad63a6c5e24a2f2cf1f677d2bf1adb3 | Form 10-Q for Q1 2026: statements, debt, liquidity |
| 10-Q_2026-06-30_bhc-20260630.htm.jsonl | 9bd8cebbf75325a6e2424a90dc4ffd52c51b1a73535e612ffb413df53a0d5061 | Form 10-Q for Q2 2026: statements, debt, liquidity |
| 10-Q_2026-09-30_bhc-20260930.htm.jsonl | bbe6464eac7c28eba7ae73d3d4c1550a00ee295236fd32b72332e63bba1b2690 | Form 10-Q for Q3 2026: statements, financing note, covenants, maturities, subsequent events |
| EX-99.1_2026-04-29_ex991-q1x2026.htm.jsonl | a03142c8b51f52ce0bcea39df704d05d1ec6cd25d01c476f43f591aef5327135 | Q1 2026 earnings release (management, non-GAAP) |
| EX-99.1_2026-07-29_ex991-q22026.htm.jsonl | b572ec3ee8791446c7753f44c437564f85dc7c22a9282dc8fe3094943c7ca9ed | Q2 2026 earnings release (management, non-GAAP) |
| EX-99.1_2026-10-28_ex991-q32026.htm.jsonl | d176e2b2337e8c9ee765792690a4c9894f8e78c9eadadca91a11afce842a8bb9 | Q3 2026 earnings release: adjusted EBITDA reconciliation, guidance |
| context | ce3ba040ad702f7a097a4705cf09e05a5541c48113a20eaf4b83ee334242bc43 | User run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | f3a9713066d902ea831e33ca5e21c7518220ff0fc6d8658f54808a4e8892a5bd | Source readiness; carried forward: consolidated perimeter includes Bausch + Lomb, debt documents not supplied, covenant ratio not supplied |

Correction to the supplied handoff (it cannot be edited): CP-0 says Bausch + Lomb is "issuer of the B+L Senior Secured Notes". The Q3 10-Q shows Bausch + Lomb issued the 8.375% Senior Secured Notes due October 2028, while the floating rate notes due January 2031 were issued by its subsidiaries Bausch + Lomb Netherlands B.V. and Bausch & Lomb Incorporated (page:35).

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Reported debt is high but leverage on a derived earnings basis improved through 2026 as earnings rose and cash built; debt maturities cluster in 2028 to 2031, and Bausch + Lomb sits inside the consolidated numbers. | Medium | No adjusted EBITDA for the fourth quarter of 2025, no interim cash interest and no covenant calculation, so leverage and cover rest on a derived measure. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Consolidated debt to derived EBITDA before goodwill impairments fell at each measured date, from 6.18x at FY2025 to 5.15x at Q3 2026. | Direction is favourable, but gross leverage is still above five times and rests on an earnings measure built from the statements. | Medium |
| Cash interest cover can only be computed for FY2025, at 1.81x; interim cash interest is not printed. | Cover is modest on a cash basis and the 2026 trend cannot be confirmed from the pack. | Medium |
| At September 30, 2026 cash was 2,485 and undrawn revolver capacity was 1,135, but part belongs to Bausch + Lomb. | Liquidity available to the parent group is lower than the consolidated total. | High |
| Maturities are 3,766 in 2028, 1,667 in 2029, 4,123 in 2030 and 3,896 in 2031; 643 of 2027 notes are to be redeemed in cash. | Redemption removes most of the 2027 maturities; refinancing risk moves to 2028 to 2031. | High |
| The revolver covenant levels are printed but the reported ratio and the step-up date are not. | Covenant headroom cannot be verified from the pack. | High |

### Financial base view

The financial base can be built from filed documents: audited FY2025 statements, unaudited Q1, Q2 and Q3 2026 statements, and a complete debt table with maturities. Consolidated revenue was 8,317 for nine months 2026 against 7,470 for nine months 2025. Operating income was 773 against 1,339, because nine months 2026 includes a 1,426 goodwill impairment (Q3 10-Q page:6). Before that charge, the derived EBITDA (net income plus tax plus net interest plus depreciation and amortization) was 3,039 for nine months 2026 against 2,397 for nine months 2025. Q3 2026 derived EBITDA of 1,266 matches the release's reported EBITDA line (Q3 release page:24).

Consolidated principal debt was 20,168 at September 30, 2026 against 20,232 at December 31, 2025, so the balance moved little; leverage improved because the earnings denominator rose and cash rose from 1,309 to 2,485. Of the 20,168, Bausch Health (excl. B+L) carries 15,103 and Bausch + Lomb carries 5,065 (page:127 to page:128), and the covenant group excludes Bausch + Lomb's earnings and net debt (page:40). A consolidated ratio therefore mixes two credit groups. Parent-group net debt fell from 14,198 at December 31, 2025 to 13,130 at September 30, 2026, and by 521 in Q3 2026 alone, consistent with the release's statement of more than 500 of net debt reduction (Q3 release page:1).

Two limits shape every ratio below. First, the pack has no adjusted EBITDA for the fourth quarter of 2025 (the 10-K prints none), so an LTM adjusted EBITDA is not calculable; the ratios use the statement-derived EBITDA before goodwill impairments, which is not the covenant definition. Second, the 10-Qs print no total cash interest paid, so interim cash interest cover is Not supplied; only FY2025 interest paid of 1,810 (10-K page:319) allows a cash cover figure.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 6.18 | 5.78 | x | Principal debt 20,232 (net of cash and equivalents 1,309) over FY2025 derived EBITDA before goodwill impairments of 3,276. Consolidated incl. Bausch + Lomb; not the covenant definition; lease obligations excluded. |
| LTM Q1 2026 | 5.84 | 5.47 | x | Principal debt 20,212, cash and equivalents 1,299, LTM derived EBITDA before goodwill impairments 3,458. Same basis and limits. |
| LTM Q2 2026 | 5.66 | 5.15 | x | Principal debt 20,239, cash and equivalents 1,825, LTM derived EBITDA before goodwill impairments 3,573. Same basis and limits. |
| LTM Q3 2026 | 5.15 | 4.51 | x | Principal debt 20,168, cash and equivalents 2,485, LTM derived EBITDA before goodwill impairments 3,918. Same basis and limits; adjusted EBITDA based ratio is Not calculable (no fourth quarter 2025 adjusted EBITDA). |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| FY2025 | 1.81 | x | Derived EBITDA before goodwill impairments 3,276 over interest paid 1,810 (10-K page:319), which includes 276 of interest recorded as a reduction of the 2022 Secured Notes premium. Consolidated. |
| LTM Q1 2026 | Not supplied: the 10-Q does not print interest paid for the period | x | An LTM cash interest figure needs interest paid for three months 2026 and 2025, which the Q1 10-Q does not print. See Calculations for a P&L interest basis. |
| LTM Q2 2026 | Not supplied: the 10-Q does not print interest paid for the period | x | Same limitation for the six month periods in the Q2 10-Q. |
| LTM Q3 2026 | Not supplied: the 10-Q does not print interest paid for the period | x | Same limitation for the nine month periods in the Q3 10-Q; a partial figure (contractual interest on certain notes) is printed, not a total. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| FY2025 | 1309 | 1132 | US$m | Cash and cash equivalents at December 31, 2025 (restricted cash 16 excluded). Undrawn: Bausch Health 2030 Revolving Credit Facility 468 (500 commitment less 32 letters of credit, 10-K page:274) plus B+L 2030 Revolving Credit Facility 664 (10-K page:278). Consolidated; Bausch + Lomb cash 397 (incl. restricted) and its 664 revolver availability are generally not available to the parent. |
| Q1 2026 | 1299 | 1137 | US$m | Cash and cash equivalents at March 31, 2026. Undrawn: 469 (500 commitment less 31 letters of credit) plus B+L 668 (Q1 10-Q page:30, page:34). Consolidated; Bausch + Lomb cash 279 (incl. restricted). |
| Q2 2026 | 1825 | 1087 | US$m | Cash and cash equivalents at June 30, 2026. Undrawn: 469 plus B+L 618 (Q2 10-Q page:31, page:35). Consolidated; Bausch + Lomb cash 378 (incl. restricted). |
| Q3 2026 | 2485 | 1135 | US$m | Cash and cash equivalents at September 30, 2026. Undrawn: 469 (500 commitment less 31 letters of credit) plus B+L 666 (Q3 10-Q page:32, page:36). Consolidated; Bausch + Lomb cash 515 (incl. restricted) and its revolver are generally not available to the parent. |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Remainder of 2026 | 15 | US$m | Principal at September 30, 2026 (Q3 10-Q page:42): Bausch Health 8, Bausch + Lomb 7. |
| 2027 | 701 | US$m | Bausch Health 673, Bausch + Lomb 28 (page:127). Includes the 643 of 8.50% notes due January 2027 that the company announced it will redeem on November 30, 2026 (page:76); that redemption is a subsequent event, not reflected in the 701. |
| 2028 | 3766 | US$m | Bausch Health 2,326, Bausch + Lomb 1,440. |
| 2029 | 1667 | US$m | Bausch Health 1,639, Bausch + Lomb 28. |
| 2030 | 4123 | US$m | Bausch Health 3,995, Bausch + Lomb 128. Includes the 2030 Term Loan B Facility. |
| 2031 | 3896 | US$m | Bausch Health 462, Bausch + Lomb 3,434. |
| Thereafter | 6000 | US$m | Bausch Health only; the 10.00% Senior Secured Notes due April 2032 (page:27). |

### Financials and credit metrics

| Metric (US$m) | FY2025 | 9M 2025 | 9M 2026 | LTM Q3 2026 | Q3 2025 | Q3 2026 | Basis and locator |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Revenues | 10,266 | 7,470 | 8,317 | 11,113 | 2,681 | 2,941 | Reported. 10-K page:219; Q3 10-Q page:6. LTM is derived. |
| Operating income | 1,813 | 1,339 | 773 | 1,247 | 619 | 983 | Reported. LTM derived. |
| Goodwill impairments | 145 | — (printed nil) | 1,426 | 1,571 | — (printed nil) | — (printed nil) | Reported. LTM derived. |
| Interest expense | 1,604 | 1,207 | 1,196 | 1,593 | 412 | 398 | Reported, gross of interest income. LTM derived. |
| Interest expense, net of interest income | 1,556 | 1,168 | 1,162 | 1,550 | 397 | 385 | Derived; matches release "Interest expense, net" (Q3 release page:24). |
| Provision for income taxes | 247 | 88 | 316 | 475 | 37 | 151 | Reported. LTM derived. |
| Net income (loss) | 120 | 223 | (725) | (828) | 181 | 446 | Reported. LTM derived. |
| Net income (loss) attributable to Bausch Health | 157 | 269 | (729) | (841) | 179 | 436 | Reported. LTM derived. |
| Depreciation and amortization | 1,208 | 918 | 860 | 1,150 | 306 | 284 | Cash flow statement line (10-K page:220; Q3 10-Q page:7); Q3 values equal nine months less six months. |
| EBITDA (derived) | 3,131 | 2,397 | 1,613 | 2,347 | 921 | 1,266 | Net income plus tax plus net interest plus D&A. Agrees to release EBITDA for 9M 2025, 9M 2026 and both Q3 columns (Q3 release page:24). |
| EBITDA before goodwill impairments (derived) | 3,276 | 2,397 | 3,039 | 3,918 | 921 | 1,266 | Derived EBITDA plus goodwill impairments. Used for ratios. Asset impairments (FY2025 8; 9M 2026 13) not added back. |
| Adjusted EBITDA, management definition, incl. noncontrolling interest | Not supplied: no fourth quarter 2025 release in the pack | 2,565 | 3,323 | Not calculable: needs fourth quarter 2025 | 1,019 | 1,350 | Q3 release page:24. Non-GAAP. Attributable to Bausch Health: 2,489, 3,217, 986, 1,305. |
| Net cash provided by operating activities | 1,400 | 905 | 1,714 | 2,209 | 405 | 813 | Cash flow statements (10-K page:221; Q3 10-Q page:8). Q3 columns from the Q3 release page:27; the 10-Q implies 814 for Q3 2026 (nine months 1,714 less six months 900). |
| Purchases of property, plant and equipment | 397 | 305 | 252 | 344 | 91 | 66 | Cash flow statements; Q3 columns derived as nine months less six months (6M 2025 214; 6M 2026 186, Q2 10-Q page:8). |
| Operating cash flow less capex (derived) | 1,003 | 600 | 1,462 | 1,865 | 314 | 747 | Derived; not the company's adjusted cash flow measure. |
| Interest paid (cash) | 1,810 | Not supplied: not printed in 10-Qs | Not supplied: not printed in 10-Qs | Not supplied | Not supplied | Not supplied | 10-K page:319. Includes 276 recorded as a reduction of premium. |

### Balance sheet and debt position

| Item (US$m) | Dec 31, 2025 | Mar 31, 2026 | Jun 30, 2026 | Sep 30, 2026 | Locator |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents | 1,309 | 1,299 | 1,825 | 2,485 | Balance sheets (10-K page:218; Q3 10-Q page:5) |
| Restricted cash | 16 | 13 | 13 | 3 | Same |
| Principal debt obligations | 20,232 | 20,212 | 20,239 | 20,168 | Debt tables (10-K page:269; Q1 page:26; Q2 page:27; Q3 page:27) |
| Debt net of premiums, discounts and issuance costs | 20,817 | 20,764 | 20,741 | 20,637 | Same; equals current plus non-current long-term debt on the balance sheet |
| Current portion of long-term debt | 225 | 889 | 866 | 866 | Balance sheets |
| Financial leases, current plus non-current | 34 | 31 | 38 | 78 | Balance sheets; outside the debt figure |
| Bausch Health (excl. B+L) principal debt | 15,126 | 15,118 | 15,111 | 15,103 | Maturity tables (10-K page:173; Q1 page:113; Q2 page:123; Q3 page:127) |
| Bausch + Lomb principal debt | 5,106 | 5,094 | 5,128 | 5,065 | Same |
| Bausch Health cash, cash equivalents and restricted cash | 928 | 1,033 | 1,460 | 1,973 | Same locators |
| Bausch + Lomb cash, cash equivalents and restricted cash | 397 | 279 | 378 | 515 | Same locators |
| Total (deficit) equity | 377 | (1,082) | (802) | (341) | Balance sheets |
| Bausch Health shareholders' deficit | (554) | (2,059) | (1,771) | (1,328) | Balance sheets |

### Debt instruments at September 30, 2026

Principal and carrying amounts are from the Q3 10-Q table at page:27. Issuer, security and guarantor text is from pages 29 to 40 as cited.

| Instrument | Maturity | Principal | Carrying | Issuer and security as printed |
| --- | --- | --- | --- | --- |
| 2030 Revolving Credit Facility (commitment 500) | April 2030 | — | — | 126NumberCo borrower; no borrowings, 31 letters of credit issued (page:32). Secured by first lien on 126NumberCo assets incl. 211,963,893 Bausch + Lomb shares; guaranteed by the Company and loan guarantors (page:31). |
| 2030 Term Loan B Facility | October 2030 | 2,962 | 2,865 | 126NumberCo; same security; term SOFR plus 6.25% (page:32) |
| 4.875% Secured Notes | June 2028 | 803 | 800 | Company; guaranteed by the BHC Existing Note Guarantors (page:38) |
| 11.00% First Lien Secured Notes | September 2028 | 888 | 1,067 | Company; same guarantors; carried at premium (page:38, page:41) |
| 14.00% Second Lien Secured Notes | October 2030 | 352 | 556 | Company; carried at premium. Guarantor and lien text not located in the pages read |
| 10.00% Senior Secured Notes | April 2032 | 6,000 | 6,246 | 126NumberCo; first lien on 126NumberCo assets incl. Bausch + Lomb Share Collateral; guaranteed by the Company, the BHC Existing Note Guarantors and NumberCo Note Guarantors (page:37) |
| 8.50% Senior Unsecured Notes | January 2027 | 643 | 643 | Bausch Health Americas, Inc. ("BHA"): the subsidiary announced redemption of "all of its outstanding" notes (page:76); to be redeemed November 30, 2026 |
| 7.00% Senior Unsecured Notes | January 2028 | 171 | 171 | Unsecured; issuer (Company or BHA) not stated in the table (page:39, page:130) |
| 5.00% Senior Unsecured Notes | January 2028 | 433 | 432 | Same |
| 6.25% Senior Unsecured Notes | February 2029 | 821 | 818 | Same |
| 5.00% Senior Unsecured Notes | February 2029 | 452 | 450 | Same |
| 7.25% Senior Unsecured Notes | May 2029 | 336 | 335 | Same |
| 5.25% Senior Unsecured Notes | January 2030 | 779 | 775 | Same |
| 5.25% Senior Unsecured Notes | February 2031 | 463 | 460 | Same |
| B+L 2030 Revolving Credit Facility (commitment 800) | June 2030 | 100 | 100 | Bausch + Lomb; 34 letters of credit, 666 available (page:36) |
| B+L January 2031 Refinancing Term Facility | January 2031 | 2,788 | 2,761 | Bausch + Lomb; 7.65% stated rate at September 30, 2026 (page:37); secured by substantially all assets of Bausch + Lomb and material subsidiaries (page:36) |
| B+L 8.375% Secured Notes | October 2028 | 1,400 | 1,390 | Bausch + Lomb (page:35) |
| B+L January 2031 Secured Notes (EUR 675 floating) | January 2031 | 765 | 756 | Bausch + Lomb Netherlands B.V. and Bausch & Lomb Incorporated; 6.31% at September 30, 2026 (page:35) |
| Other | Various | 12 | 12 | Not attributed in the table; see Calculations |
| Total | | 20,168 | 20,637 | Printed total (page:27) |

Weighted average stated rate of interest on outstanding debt 8.55% at September 30, 2026 against 8.54% at December 31, 2025; weighted average rate reported in the financial statements 7.61% (page:41, page:131). The 2022 Exchange premium accounting means interest expense is lower than contractual interest.

### Claims outside the debt figure

- Financial leases: current 17 and non-current 61 at September 30, 2026 (balance sheet page:5), against 11 and 23 at December 31, 2025. The increase includes a failed sale-leaseback of Bausch + Lomb assets, with 33 (EUR) sold and leased back (page:43). The company calls such items "other financial liabilities" recorded in Financial leases and Non-current portion of long-term debt (page:43), so part of this is inside the debt figure and the split is not printed.
- Operating leases and total lease liabilities: 10-K page:301 shows total lease liabilities of 262 at December 31, 2025 (accrued and other current 61, other non-current 167, financial leases 11 and 23). The Q3 10-Q prints no lease note; operating lease balances at September 30, 2026 are Not supplied.
- Receivables sales: Bausch + Lomb sold receivables for cash proceeds of 26 in nine months 2026 under a true-sale arrangement, all collected and remitted by September 30, 2026 (page:43). The arrangement is outside debt.
- Contingent consideration: acquisition-related contingent consideration of 199 is non-current at September 30, 2026 (254 at December 31, 2025), and the company expects contingent consideration and milestone payments of about 40 in Q4 2026 (page:133).
- Legal: accrued current loss contingencies of 28 at September 30, 2026 (page:50, page:134); legal matters and related fees in accrued liabilities 28 against 178 at December 31, 2025 (page:27). Payments of accrued legal settlements were 176 in nine months 2026 against 198 (page:8). Unreserved items include a Luxembourg tax assessment of EUR 271.7 million excluding interest, for which the company concludes no reserve is required (page:48). Litigation outcomes after the filing date are Not supplied.
- Pensions: no pension note in the Q3 10-Q; the only pension item is a pension adjustment of (11) in accumulated other comprehensive loss (page:45). Pension obligations are Not supplied for September 30, 2026.
- Accrued interest: accrued interest of 391 at September 30, 2026 against 253 at December 31, 2025 (page:26), inside accrued and other current liabilities, outside the debt figure.
- Subsequent events (Q3 10-Q page:76, page:133), all after September 30, 2026: lump-sum payment of about 75 to the former Bausch + Lomb chief executive; 50 share repurchase authorization dated October 24, 2026; redemption of about 643 of 8.500% Senior Notes due 2027 scheduled for November 30, 2026, funded from cash; Bausch + Lomb agreement of October 8, 2026 to acquire ophthalmic surgical manufacturing businesses for about 85 upfront.

### Covenants and ratings

- Revolver maintenance tests (2030 Revolving Credit Facility, page:34): Blended First Lien Leverage Ratio not greater than 4.25:1.00 before the Covenant Step Up Date and 5.75:1.00 on and after it; minimum liquidity of 400 on and after the Covenant Step Up Date. The step-up date is defined in the 2025 Credit Agreement, which is not supplied, and no source prints the reported ratio; the company states compliance at September 30, 2026 (page:29). Headroom is Not calculable.
- The revolver matures at the earlier of April 8, 2030 and 91 days before the scheduled maturity of indebtedness above 1,000 in aggregate principal of the Company or 126NumberCo (page:32). Bausch Health (excl. B+L) has 2,326 of principal due in 2028 (page:127), so this earlier-maturity trigger may apply before April 2030; how the aggregate is measured needs the agreement, which is not supplied.
- No facility of the parent group matures within twelve months of September 30, 2026: the 2030 Revolving Credit Facility matures April 2030 and the B+L 2030 Revolving Credit Facility June 2030 (page:27).
- Bausch + Lomb term facilities carry financial covenants (page:28); levels are not printed.
- Ratings at October 28, 2026 (page:131): Moody's Caa2 corporate, Caa1 senior secured, Ca senior unsecured, outlook stable; S&P B- corporate, B- senior secured, CCC+ senior unsecured, outlook negative; Fitch B corporate, BB senior secured, Rating Watch Evolving. Bausch + Lomb: Moody's B1 stable, S&P B with developing outlook. No change to either corporate rating in Q3 2026 (page:132).

### Segment revenue, Q3 2026

Management release, reported basis (Q3 release page:2): Salix 831 against 716; International 299 against 286; Solta Medical 165 against 140; Diversified 271 against 258; Bausch + Lomb 1,375 against 1,281. Bausch Health (excl. B+L) is 1,566 against 1,400. The five segments sum to the consolidated 2,941 against 2,681.

### Interpretation

- Evidence: LTM derived EBITDA before goodwill impairments rose from 3,276 (FY2025) to 3,918 (LTM Q3 2026) while principal debt moved from 20,232 to 20,168 and cash from 1,309 to 2,485.
- Mechanism: the improvement is earnings and cash driven. Gross debt is flat, so gross leverage of 5.15x at Q3 2026 depends on earnings continuing at the higher level; the company's own guidance for full year adjusted EBITDA of 4,315 to 4,415 (Q3 release page:4) is a management forecast, not a reported figure.
- Perimeter: Bausch + Lomb contributes 328 of the Q3 2026 adjusted EBITDA of 1,350 and 5,065 of the 20,168 debt (Q3 release page:28; page:127). Its cash and revolver availability are generally not available to the parent group (page:127, page:131). Parent-group net debt is 13,130 against consolidated net debt of 17,683.
- Interest burden: net interest expense of 1,162 for nine months 2026 is a P&L figure reduced by premium amortization; contractual interest is higher. Interest paid in FY2025 was 1,810 against net interest expense of 1,556. The company expects about 561 of interest payments in Q4 2026 (page:133) and the Remaining Secured Notes alone carry 4,017 of scheduled interest payments from the remainder of 2026 to 2032 (page:130).
- Credit implication: leverage is falling but remains high for a group rated Caa2 and B- at the corporate level. Cover on cash interest in FY2025 was 1.81x. The risk is concentrated in 2028 to 2031 maturities and in the structural separation between the parent group and Bausch + Lomb.

## Calculations

All amounts US$ millions. Inputs are the cited printed figures.

### Derived EBITDA and LTM

| Period | Net income (loss) | Provision for taxes | Interest expense less interest income | D&A | EBITDA | Goodwill impairments | EBITDA before goodwill impairments |
| --- | --- | --- | --- | --- | --- | --- | --- |
| FY2025 | 120 | 247 | 1,604 less 48 = 1,556 | 1,208 | 3,131 | 145 | 3,276 |
| 3M 2026 | (1,431) | 77 | 402 less 10 = 392 | 295 | (667) | 1,426 | 759 |
| 3M 2025 | (86) | 39 | 330 less 11 = 319 | 305 | 577 | — | 577 |
| 6M 2026 | (1,171) | 165 | 798 less 21 = 777 | 576 | 347 | 1,426 | 1,773 |
| 6M 2025 | 42 | 51 | 795 less 24 = 771 | 612 | 1,476 | — | 1,476 |
| 9M 2026 | (725) | 316 | 1,196 less 34 = 1,162 | 860 | 1,613 | 1,426 | 3,039 |
| 9M 2025 | 223 | 88 | 1,207 less 39 = 1,168 | 918 | 2,397 | — | 2,397 |

Arithmetic: FY2025 120 + 247 + 1,556 + 1,208 = 3,131. 9M 2026 (725) + 316 + 1,162 + 860 = 1,613. 9M 2025 223 + 88 + 1,168 + 918 = 2,397. Q3 2026 446 + 151 + 385 + 284 = 1,266. Sources: 10-K page:219, page:220; Q1 10-Q statements; Q2 10-Q page:6 to page:7; Q3 10-Q page:6 to page:7. The 9M 2026, 9M 2025 and Q3 EBITDA figures equal the release's EBITDA line (Q3 release page:24), which supports the D&A and interest definitions.

LTM EBITDA = FY2025 + current year to date − prior year to date:

| LTM to | EBITDA | Goodwill impairments | EBITDA before goodwill impairments |
| --- | --- | --- | --- |
| March 31, 2026 | 3,131 + (667) − 577 = 1,887 | 145 + 1,426 − 0 = 1,571 | 1,887 + 1,571 = 3,458 |
| June 30, 2026 | 3,131 + 347 − 1,476 = 2,002 | 1,571 | 2,002 + 1,571 = 3,573 |
| September 30, 2026 | 3,131 + 1,613 − 2,397 = 2,347 | 1,571 | 2,347 + 1,571 = 3,918 |

Other LTM Q3 2026 flows: revenues 10,266 + 8,317 − 7,470 = 11,113; operating income 1,813 + 773 − 1,339 = 1,247; net income 120 − 725 − 223 = (828); attributable 157 − 729 − 269 = (841); provision for taxes 247 + 316 − 88 = 475; gross interest expense 1,604 + 1,196 − 1,207 = 1,593; net interest 1,556 + 1,162 − 1,168 = 1,550; D&A 1,208 + 860 − 918 = 1,150; operating cash flow 1,400 + 1,714 − 905 = 2,209; capex 397 + 252 − 305 = 344; operating cash flow less capex 2,209 − 344 = 1,865.

### Leverage and net debt (consolidated)

| Date | Principal debt | Cash and equivalents | Net debt | LTM EBITDA before goodwill impairments | Debt / EBITDA | Net debt / EBITDA |
| --- | --- | --- | --- | --- | --- | --- |
| Dec 31, 2025 | 20,232 | 1,309 | 18,923 | 3,276 | 6.18x | 5.78x |
| Mar 31, 2026 | 20,212 | 1,299 | 18,913 | 3,458 | 5.84x | 5.47x |
| Jun 30, 2026 | 20,239 | 1,825 | 18,414 | 3,573 | 5.66x | 5.15x |
| Sep 30, 2026 | 20,168 | 2,485 | 17,683 | 3,918 | 5.15x | 4.51x |

Net debt deducts cash and cash equivalents only; restricted cash (16, 13, 13, 3) and financial leases are excluded.

### Interest cover

- FY2025 cash basis: 3,276 / 1,810 = 1.81x. Using EBITDA without the goodwill add-back: 3,131 / 1,810 = 1.73x.
- P&L basis (net interest expense, not cash): FY2025 3,276 / 1,556 = 2.11x; LTM Q1 2026 3,458 / 1,629 = 2.12x; LTM Q2 2026 3,573 / 1,562 = 2.29x; LTM Q3 2026 3,918 / 1,550 = 2.53x. LTM net interest: 1,556 + 392 − 319 = 1,629; 1,556 + 777 − 771 = 1,562; 1,556 + 1,162 − 1,168 = 1,550. This basis is flattered by premium accounting, so it is not comparable with the cash basis.

### Liquidity

| Date | Cash and equivalents | Bausch Health 2030 revolver undrawn | B+L 2030 revolver undrawn | Undrawn total | Cash plus undrawn |
| --- | --- | --- | --- | --- | --- |
| Dec 31, 2025 | 1,309 | 500 − 0 − 32 = 468 | 800 − 100 − 36 = 664 | 1,132 | 2,441 |
| Mar 31, 2026 | 1,299 | 500 − 0 − 31 = 469 | 800 − 100 − 32 = 668 | 1,137 | 2,436 |
| Jun 30, 2026 | 1,825 | 500 − 0 − 31 = 469 | 800 − 150 − 32 = 618 | 1,087 | 2,912 |
| Sep 30, 2026 | 2,485 | 500 − 0 − 31 = 469 | 800 − 100 − 34 = 666 | 1,135 | 3,620 |

The B+L figures equal the printed remaining availability (664, 668, 618, 666). For Bausch Health, the printed availability is "approximately 468" at April 29, 2026 (Q1 10-Q page:116) while the March 31, 2026 inputs give 469; the one unit difference is rounding or timing and is not resolved. Bausch Health (excl. B+L) at September 30, 2026: cash, cash equivalents and restricted cash 1,973 plus undrawn 469 = 2,442. This is before the 643 notes redemption on November 30, 2026, which uses cash on hand (page:76).

### Net debt by perimeter

| Date | Bausch Health debt | Bausch Health cash incl. restricted | Bausch Health net debt | Bausch + Lomb debt | Bausch + Lomb cash incl. restricted | Bausch + Lomb net debt |
| --- | --- | --- | --- | --- | --- | --- |
| Dec 31, 2025 | 15,126 | 928 | 14,198 | 5,106 | 397 | 4,709 |
| Mar 31, 2026 | 15,118 | 1,033 | 14,085 | 5,094 | 279 | 4,815 |
| Jun 30, 2026 | 15,111 | 1,460 | 13,651 | 5,128 | 378 | 4,750 |
| Sep 30, 2026 | 15,103 | 1,973 | 13,130 | 5,065 | 515 | 4,550 |

Q3 2026 change in Bausch Health net debt: 13,651 − 13,130 = 521. The two perimeters sum to the consolidated principal debt: 15,103 + 5,065 = 20,168. Perimeter cash includes restricted cash, so these net debt figures differ slightly from the consolidated table above.

### Parent-group leverage, illustrative only

These are not LTM and not covenant measures. Parent debt 15,103, parent net debt 13,130. Q3 2026 adjusted EBITDA of Bausch Health (excl. B+L) is 1,022 (Q3 release page:28); times four is 4,088; 15,103 / 4,088 = 3.69x gross and 13,130 / 4,088 = 3.21x net. On the midpoint of full year 2026 guidance for Bausch Health (excl. B+L) adjusted EBITDA of 3,225 to 3,275 (midpoint 3,250; Q3 release page:4): 15,103 / 3,250 = 4.65x and 13,130 / 3,250 = 4.04x. Guidance is a management forecast.

### Pro forma for the November 30, 2026 redemption

Redeeming 643 of notes from cash reduces both debt and cash by 643 at that date, so net debt is unchanged by the redemption itself. Parent 2027 maturities would fall from 673 to 673 − 643 = 30 and consolidated 2027 maturities from 701 to 701 − 643 = 58. Premium or accrued interest on redemption is not quantified in the sources and is excluded. This is a subsequent event and is not in any September 30, 2026 balance.

### Reconciliations and checks

- Debt table: the instrument rows at September 30, 2026 sum to 20,168: facilities and term loans 2,962 + 100 + 2,788 = 5,850; secured notes 803 + 888 + 352 + 6,000 + 1,400 + 765 = 10,208; unsecured notes 643 + 171 + 433 + 821 + 452 + 336 + 779 + 463 = 4,098; other 12; 5,850 + 10,208 + 4,098 + 12 = 20,168. The parent rows (2,962 + 803 + 888 + 352 + 6,000 + 4,098) sum to 15,103 and the four Bausch + Lomb rows (100 + 2,788 + 1,400 + 765) sum to 5,053; 5,065 − 5,053 = 12, which equals the Other line, so Other appears to belong to Bausch + Lomb but the source does not say so.
- Carrying debt: principal 20,168 plus unamortized premiums, discounts and issuance costs 469 = 20,637 (page:42), equal to current portion 866 plus non-current 19,771 (balance sheet).
- Maturity table sums: 15 + 701 + 3,766 + 1,667 + 4,123 + 3,896 + 6,000 = 20,168; parent 8 + 673 + 2,326 + 1,639 + 3,995 + 462 + 6,000 = 15,103; Bausch + Lomb 7 + 28 + 1,440 + 28 + 128 + 3,434 = 5,065.
- Current portion: the balance sheet shows 866 current debt while principal due in the remainder of 2026 and 2027 is 15 + 701 = 716. The difference of 150 is not explained in the pages read and is not reconciled.
- Expense block, nine months 2026: 2,195 + 50 + 2,602 + 477 + 693 + 1,426 + 32 + 69 = 7,544; 8,317 − 7,544 = 773 operating income. FY2025: 2,949 + 64 + 3,438 + 629 + 1,001 + 145 + 8 + 77 + 142 = 8,453; 10,266 − 8,453 = 1,813.
- Balance sheet, September 30, 2026: assets 7,408 + 2,108 + 3,972 + 9,767 + 1,886 + 343 = 25,484; liabilities 4,749 + 199 + 61 + 19,771 + 340 + 705 = 25,825; equity (1,328) + 987 = (341); 25,825 − 341 = 25,484.
- Cash: beginning 1,325 + net increase 1,163 = 2,488 = cash 2,485 + restricted 3 (page:8).
- Segment revenue Q3 2026: 831 + 299 + 165 + 271 = 1,566; 1,566 + 1,375 = 2,941.
- Cash flow quarterly: Q1 230 + Q2 671 + Q3 813 = 1,714, equal to nine months (Q1 and Q2 releases, Q3 release page:27).

### Conflicts between sources

| Item | Source A | Source B | Treatment |
| --- | --- | --- | --- |
| Interest payments charged against debt premium, nine months 2026 | Q3 10-Q: 111 + 47 = 158 (page:41) and 158 (page:126) | Q3 release: 144 (page:27) | Filing controls: 158. The 14 difference is not explained, and its effect on the release adjusted cash flow from operations (1,793) is not quantified. |
| Operating cash flow Q3 2026 | Q3 release: 813 (page:27) | 10-Q nine months 1,714 less six months 900 = 814 | Rounding; the release quarters sum to 1,714. |
| Bausch Health revolver availability | Printed approximately 468 at April 29, 2026 | 500 less 31 letters of credit at March 31, 2026 = 469 | One unit; 469 used. |

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| No adjusted EBITDA for the fourth quarter of 2025 or FY2025 in any source (searched "Adjusted EBITDA" in the 10-K: only a compensation reference at page:307); LTM adjusted EBITDA Not calculable | High | CP-2, CP-5 | Supply the fourth quarter 2025 release |
| Interest paid not printed in the 10-Qs; interim cash interest cover Not supplied | High | CP-2 | Supply cash flow supplemental disclosure or the fourth quarter 2025 and later releases |
| Covenant ratio, step-up date and liquidity covenant definition Not supplied (credit agreement not in pack); headroom Not calculable | High | CP-2 | Supply 2025 Credit Agreement and compliance calculation |
| Issuer of each Senior Unsecured Note (Company or BHA) not stated in the table; guarantor and lien text for the 14.00% Second Lien Secured Notes not located in the pages read | Medium | CP-2, CP-1A | Supply indentures or the 10-K debt note detail |
| Operating lease and pension balances at September 30, 2026 Not supplied | Medium | CP-2 | Use December 31, 2025 lease table (10-K page:301) as latest; supply interim notes if any |
| Current debt 866 against 716 of principal due by end of 2027 not reconciled | Medium | CP-2 | Read the current portion composition in the debt note |
| Failed sale-leaseback split between financial leases and debt not printed | Low | CP-2 | Supply the Bausch + Lomb 10-Q |
| Bausch + Lomb standalone filings not supplied; its covenant levels not printed | Medium | CP-1A, CP-2 | Supply Bausch + Lomb Form 10-Q and credit agreement |
| Extraction is text only; no check against filed HTML or XBRL | Low | CP-5 | Supply original HTML or XBRL |
| Events from October 29, 2026 to 2026-11-05 not supplied | Medium | CP-2 | Supply later 8-Ks or confirm none |

## Next module

CP-1A follows with the business and transaction context. Carry forward: the consolidated perimeter includes Bausch + Lomb and the parent group excludes it for covenant purposes; derived EBITDA before goodwill impairments is the ratio basis (LTM Q3 2026: 3,918) and adjusted EBITDA is management-defined with no LTM; leverage 5.15x gross and 4.51x net at Q3 2026; the revolver earlier-maturity trigger tied to the 2028 maturities; the November 30, 2026 redemption of 643 of notes; the correction on Bausch + Lomb note issuers above; and the covenant ratio Not supplied.
