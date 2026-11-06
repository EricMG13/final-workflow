# CP-2 — Fundamental credit synthesis: CCO HOLDINGS LLC (cco-holdings-llc)

## Request

CCO HOLDINGS LLC (issuer id `cco-holdings-llc`), as of 2026-11-05, pathway `credit_snapshot`, asks for the fundamental credit view from the upstream financial base and the business and transaction context. Scope is the consolidated issuer in USD millions for FY2024, FY2025 and the first half of 2026, with no peer ranking, instrument recommendation or recovery conclusion.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_ccoh-20251231.htm.jsonl | 98fc08971e7b602f253b4465dc2493c7d1fd2140d7f51b96e967ed5fb3218118 | Audited FY2025 statements; Item 7A fixed and variable rate maturity table; principal and interest schedule; covenants; letters of credit and commitments |
| 10-Q_2025-09-30_ccoh-20250930.htm.jsonl | bf1745dd3dbecf91195f9fef9fea0cafc9d8a639b8157c8bb3d02dd7240529a1 | September 30, 2025 balance sheet and availability (used through the upstream handoff) |
| 10-Q_2026-03-31_ccoh-20260331.htm.jsonl | 213317fa77d5c45445d49d044bc961ab9dfa41083289474b65a9c5985c9bbe1b | March 31, 2026 balance sheet, availability, February 2026 redemptions |
| 10-Q_2026-06-30_ccoh-20260630.htm.jsonl | 9af8d8232114d58e6ac96035eb67adc4aa9622876079128a14eacfcc389f347e | Latest statements, debt classes, availability, guarantor and distribution text, Cox text |
| EX-99.1_2026-01-30_chtrex991earningsrelease12.htm.jsonl | cb5b5ac26ab78f0a85b295e8b2969a94081a4aecc513efb234aeefb51019e762 | Parent-level release (supporting, not used for figures) |
| EX-99.1_2026-04-24_chtrex991earningsrelease33.htm.jsonl | 483c56fedf60126a16d804e1d36760024be2164b76b1c1509864a6a063bd22be | Parent-level release (supporting, not used for figures) |
| EX-99.1_2026-07-24_chtrex991earningsrelease63.htm.jsonl | 07d1723b22b814c108cba78554e38a4e4a76d8f38c9cdfecbd3804011635822c | Parent-level release (supporting, not used for figures) |
| context | 1a68c05f8e4415af1307ec03597fe0b094afc35e94c83b63b62cbe99d897f95e | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 4b95775bd75ac91b4fbe8df3dddfba01cd62f5117bd68b1e969812d6f8d7022a | Source readiness and limits |
| CP-1 | ff0983c08cacf687da932db43c595db40bb04809c1727a1f0dd3c0f49ce24118 | Financial base: debt, claims outside debt, liquidity, maturities, ratios, covenants |
| CP-1A | 3048375e165e0ded201371434ad4c76f341e1547488630bb18fd2b88082c4ed7 | Business, ownership, Cox and Liberty Broadband terms, governance behaviour, conflicts |

Locators in tables are `page:N` of the pinned `.jsonl` text, not printed page numbers. Consistency with upstream: this answer agrees with CP-0, CP-1 and CP-1A and corrects none. It adds the 10-K Item 7A table of fixed and variable rate debt by maturity year (10-K page:105), which confirms the variable-rate maturity components that CP-1 had derived by difference (642 in 2028, 279 in 2029, 8,068 in 2030) and the finding that the Revolving Loan B was undrawn at year-end (variable-rate 2027 maturities of 305 equal the term loan amortisation alone). It also adds a few new calculations, all shown below.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| CCO Holdings is a large, cash-generative but leveraged cable credit: debt is 4.22x EBITDA and cash interest cover is 4.43x, with USD 3,985 million of liquidity. Its unsecured notes sit behind secured debt, and the Cox closing is unresolved. | Medium | Executed debt documents, covenant ratios after December 31, 2025, the Cox financing and anything after July 24, 2026 are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Debt of USD 93,845 million is 4.22x last-twelve-months Adjusted EBITDA of USD 22,251 million, slightly above 4.17x at December 31, 2024, as EBITDA slips. | Leverage rises slowly without any borrowing; a further EBITDA decline of 10% at constant debt would take it to 4.69x. | High |
| Distributions to parent of USD 5,898 million exceeded free cash flow of USD 5,070 million over the last twelve months. | Cash leaves for the parent's buybacks, so debt reduction depends on the parent's policy, which the filings say is a stated range, not a covenant. | High |
| USD 26,734 million of unsecured notes rank behind USD 67,111 million of secured debt, which is 3.02x EBITDA, while total debt is 4.22x. | Unsecured holders attach at 3.02x and detach at 4.22x, and any Cox debt that joins the secured group would sit ahead of them. | High |
| Debt maturing is USD 7,279 million in 2029 and USD 13,868 million in 2030, and early 2026 refinancing added about USD 58 million of annual coupon. | Refinancing is concentrated in 2029 and 2030, and each refinancing at current coupons raises cash interest. | Medium |
| The Cox Transactions are pending and the post-closing perimeter and financing are not described beyond expectations in the 10-Q. | The credit profile could change materially at closing, so the view is conditional until the structure is known. | Medium |

### Credit view

CCO HOLDINGS LLC is a large, cash-generative but leveraged cable credit whose earnings are eroding slowly and whose structure and pending acquisition decide its direction. The strongest support is USD 22,251 million of last-twelve-months Adjusted EBITDA at a 40.91% margin, cash interest cover of 4.43x and liquidity of USD 3,985 million, with little principal due before 2028. The weakest point is USD 93,845 million of debt at 4.22x, of which USD 26,734 million of unsecured notes sit behind USD 67,111 million of secured debt (3.02x), while distributions to the parent exceeded free cash flow. What decides the outcome is the Cox closing: how it is financed, whether Cox debt joins the guaranteed and secured group, and the parent's leverage policy afterwards. None of that is in the sources after July 24, 2026.

### Credit assessment

| Assessment | Category | Confidence | Basis |
| --- | --- | --- | --- |
| Fundamental view: stable operating cash generation and adequate liquidity with a long-dated debt profile, offset by leverage above 4x, slowly falling EBITDA, parent cash leakage above free cash flow, structurally and effectively subordinated unsecured notes and an unresolved acquisition. Not a rating and not a recommendation. | Analyst Interpretation | Medium (below High because executed documents, current covenant values, the Cox financing and post-July 2026 events are not supplied) | CP-1 leverage, cover, liquidity, maturity and distribution figures; CP-1A structure, transaction, governance and conflict rows |

### Key findings

First, leverage is steady near 4.2x and drifting up through earnings, not borrowing. CCO HOLDINGS LLC had total debt of USD 93,845 million and net debt of USD 93,560 million at June 30, 2026, which are 4.22x and 4.20x of last-twelve-months Adjusted EBITDA of USD 22,251 million, against 4.17x and 4.16x at December 31, 2024 [CP-1]. Debt fell USD 772 million in the half while last-twelve-months EBITDA fell from USD 22,611 million at FY2025, so the ratio rose from 4.18x. At constant debt, an EBITDA decline of 5%, 10% or 15% would take the ratio to 4.44x, 4.69x or 4.96x (calculated, illustrative). These are principal-debt ratios on company Adjusted EBITDA before the management fees that the covenants add back; they are not the covenant ratios, which the 10-K printed only at December 31, 2025: 4.0x against a 6.0x indenture maximum and 2.8x against 5.0x and 4.0x at Charter Operating [CP-1; Documentary Fact and Analyst Interpretation].

Second, earnings are eroding on revenue, not cost. Q2 2026 revenue was USD 13,526 million against USD 13,766 million and Adjusted EBITDA USD 5,428 million against USD 5,668 million, a fall of 4.2%; operating costs excluding stock compensation were flat at USD 8,098 million despite USD 65 million of Cox transition expenses [CP-1]. Internet customers fell by 172,000 in the quarter while mobile lines rose by 406,000, Internet revenue fell 3.2% and video revenue 9.7%, and mobile service revenue rose 18.9% [CP-1A]. The business faces fibre overlap from AT&T and Verizon in about 27% and 16% of the footprint and fixed wireless competition [CP-1A]. The mechanism is that a low-lock-in subscription base loses revenue faster than a largely fixed network cost base can adjust, so leverage rises as EBITDA falls (Analyst Interpretation).

Third, cash flow after capital spending is thin and is distributed to the parent. Last-twelve-months free cash flow was USD 5,070 million, or 5.40% of principal debt, after capital expenditure of USD 12,064 million, which is 54.22% of EBITDA [CP-1; calculated]. EBITDA less capital expenditure of USD 10,187 million covers cash interest of USD 5,024 million 2.03x (calculated). Distributions to the parent were USD 5,898 million over the last twelve months and USD 6,794 million in FY2025, against free cash flow of USD 5,070 million and USD 5,827 million, a shortfall of USD 828 million and USD 967 million (calculated); principal debt rose USD 838 million in FY2025 [CP-1]. In the first half of 2026 distributions of USD 2,460 million were close to free cash flow of USD 2,492 million. The 10-Q says the issuer and its subsidiaries are "the primary source" of funding for Charter's buybacks through distributions [CP-1A]. This is a policy choice, limited by an indenture leverage test (4.0x against 6.0x at December 31, 2025) and by Charter's stated 4.0x to 4.5x net leverage range, not by a hard cap (Analyst Interpretation).

Fourth, the unsecured notes are structurally and effectively subordinated, and the layers are thin in turns of EBITDA. Of USD 93,845 million of principal debt, USD 67,111 million (71.5%) is senior secured notes, debentures and credit facilities guaranteed by CCO Holdings and the operating group, and USD 26,734 million is CCO Holdings senior unsecured notes with no subsidiary guarantee [CP-1; CP-1A]. Secured debt is 3.02x of EBITDA and total debt 4.22x, so the unsecured notes occupy the part of the capital structure between 3.02x and 4.22x (calculated). Between December 31, 2025 and June 30, 2026, unsecured notes fell USD 516 million while credit facilities rose USD 504 million, so debt shifted from unsecured to secured [CP-1; CP-1A]. This is a mechanic, not a recovery view: collateral coverage is not computed and executed documents are not supplied.

Fifth, liquidity is adequate and near-term maturities are modest, but refinancing concentrates in 2029 and 2030. Cash of USD 285 million and availability of about USD 3,700 million give liquidity of USD 3,985 million, which is 3.99x the USD 999 million current portion of debt (calculated) [CP-1]. Availability fell from about USD 4,600 million at March 31, 2026 as credit facility debt rose USD 788 million. Scheduled principal was USD 1,055 million for 2026 and USD 3,555 million for 2027 at December 31, 2025; after the February 2026 redemptions of USD 750 million and USD 2,250 million these become USD 305 million and USD 1,305 million before 2026 amortisation already paid and the unallocated repurchases, with 2028 at USD 5,392 million, 2029 at USD 7,279 million and 2030 at USD 13,868 million [CP-1]. The 2029 and 2030 amounts together are USD 21,147 million, 22.35% of year-end principal debt (calculated). The Revolving Loan B of about USD 960 million matures on August 31, 2027, within twelve months of the as-of date, and the equipment installment plan facility's revolving period is subject to renewal around the as-of date (inference from the November 2025 amendment) [CP-1].

Sixth, refinancing and floating-rate exposure raise cost over time. The 87% of debt that was fixed at December 31, 2025 had an average rate of 5.07%, and the 13% that floats had a forward-implied average of 5.36%; Item 7A describes only cross-currency swaps on the sterling notes and no interest rate derivatives (10-K page:105). A 1.00% move on the USD 12,453 million of credit facility debt would change annual interest by about USD 125 million, 2.5% of last-twelve-months cash interest of USD 5,024 million (calculated, before floors). The January 2026 notes carry 7.000% and 7.375% coupons against 5.500% and 5.125% on the USD 3,000 million redeemed, an annual coupon increase of about USD 58 million before the interest saved on the USD 1,249 million of repurchases, whose coupons are not disclosed (calculated). The 10-K scheduled USD 4,817 million of interest for 2026 and USD 4,646 million for 2027 on the year-end debt before those events (10-K page:160).

Seventh, the Cox Transactions and the Liberty Broadband Combination are the largest open items. The issuer's 10-Q expects Cox's unsecured notes to become guaranteed and secured debt, Cox entities to become Obligors and all or part of about USD 4.2 billion of new debt to do the same; the cash consideration is USD 4.0 billion in the 10-K and about USD 4.2 billion in the 2026 10-Qs, which tracks Charter Holdings' cash payment moving from USD 500 million to USD 650 million, and the assumed Cox net debt and finance leases are USD 12.4 billion in the 10-Qs and USD 12.6 billion on a pro forma basis in the 10-K [CP-1A]. The filings do not say where Cox earnings will sit relative to the issuer, who issues the new debt, or whether any approval has been received. That is a missing datapoint, not an adverse finding; it decides whether the issuer's secured layer grows while its own EBITDA base does not (Insufficient Information and Analyst Interpretation).

Eighth, covenant headroom looks wide at the last printed date but cannot be measured now. At December 31, 2025 the indenture leverage of 4.0x was 2.0 turns below the 6.0x maximum, and the Charter Operating ratios of 2.8x were 2.2 turns and 1.2 turns below the 5.0x total and 4.0x first lien tests, equivalent to EBITDA cushions of about 33%, 44% and 30% at constant debt (calculated from rounded ratios) [CP-1]. A proxy using Adjusted EBITDA plus management fees of about USD 1,400 million gives 2.81x for secured debt and 3.94x for total debt, close to the printed figures. No ratio is printed after December 31, 2025 and definitions and baskets are not supplied (Insufficient Information).

### Strengths and weaknesses

Strengths. (1) Scale and stable margin: USD 22,251 million of last-twelve-months Adjusted EBITDA at a 40.91% margin across 41 states, with revenue of USD 54,396 million (Documentary Fact; CP-1, CP-1A). (2) Debt service capacity: cash interest cover of 4.43x and EBITDA less capital expenditure covering cash interest 2.03x (Documentary Fact and calculation; CP-1). (3) Liquidity and a long-dated profile: USD 3,985 million of liquidity, USD 305 million and USD 1,305 million of scheduled principal for 2026 and 2027 after the February 2026 redemptions, and 67.08% of year-end principal debt due after 2030 (Documentary Fact and calculation; CP-1). (4) Mostly fixed-rate debt: 87% of principal at year-end, which limits rate sensitivity to about USD 125 million per 1.00% on the floating part (Documentary Fact and calculation; CP-1). (5) Visible covenant room at the last printed date: 4.0x against 6.0x and 2.8x against 5.0x and 4.0x at December 31, 2025 (Documentary Fact; CP-1). (6) Growth segments: mobile lines up 1,684 thousand over twelve months and mobile service revenue up 18.9% in Q2 2026 (Documentary Fact; CP-1A). (7) Clean audited disclosure: an unqualified KPMG LLP opinion on FY2025 and regular debt, guarantor and reconciliation disclosure (Documentary Fact; CP-1A).

Weaknesses. (1) Leverage above 4x and rising slowly: 4.22x on debt and 4.34x including the equipment installment plan facility and short-term borrowings, with Adjusted EBITDA down 4.2% in Q2 2026 (Documentary Fact and calculation; CP-1). (2) Cash leakage above free cash flow: USD 5,898 million of distributions against USD 5,070 million over the last twelve months, and free cash flow down to USD 2,492 million from USD 3,249 million in the half (Documentary Fact; CP-1). (3) Subordinated unsecured notes: USD 26,734 million behind USD 67,111 million of secured debt, with debt shifting toward secured credit facilities in 2026 (Documentary Fact and Analyst Interpretation; CP-1, CP-1A). (4) Refinancing concentration and cost: USD 21,147 million due in 2029 and 2030 and about USD 58 million more annual coupon on the early 2026 refinancing (Documentary Fact and calculation; CP-1). (5) Capital intensity and intangible-heavy assets: capital expenditure of USD 12,064 million is 54.22% of EBITDA, and franchises and goodwill are 63.34% of total assets, with a fair-value cushion of more than 10% at the last impairment test (Documentary Fact; CP-1, CP-1A). (6) Competition and customer losses: Internet and video customers falling against fibre and fixed wireless entrants (Documentary Fact and Management Language; CP-1A). (7) Opaque post-closing structure and missing documents: Cox financing, perimeter and approvals not supplied; indentures, credit agreement and covenant definitions not supplied (Insufficient Information; CP-0, CP-1A). (8) Claims outside debt of USD 1,596 million of equipment installment plan financing and USD 1,155 million of short-term borrowings, USD 725 million of supply chain finance and USD 1,276 million of operating leases that are not in the debt figure (Documentary Fact; CP-1).

### Debt and claims inventory

| Claim | Amount (US$m) | Date | Inside the debt figure? | Security, guarantors, maturity | Locator |
| --- | --- | --- | --- | --- | --- |
| CCO Holdings senior notes (13 series at year-end; co-issuer CCO Holdings Capital Corp.) | 27,250 at Dec 31, 2025; 26,734 for the class at Jun 30, 2026 | Jun 30, 2026 | Yes | Senior unsecured; no subsidiary guarantee; structurally subordinated; 2026 series redeemed; 2027 series 1,000 remains before any repurchases; two series due 2033 and 2036 issued January 2026 (3,000); final series 2036 | 10-K page:102, page:155; 10-Q Jun 2026 page:10 to page:11, page:33 |
| Charter Operating senior notes (29 series) | 44,500 at Dec 31, 2025 | Dec 31, 2025 | Yes | Senior secured, first-priority liens; guaranteed by CCO Holdings and the operating subsidiaries; 2028 to 2063 | 10-K page:103, page:156 |
| Time Warner Cable, LLC notes and debentures (8 series, incl. sterling 842 and 876) and Time Warner Cable Enterprises LLC debentures (1,000) | 9,918 and 1,000 at Dec 31, 2025 | Dec 31, 2025 | Yes | Guaranteed by CCO Holdings, Charter Operating and the operating subsidiaries; rank with the collateral liens; 2031 to 2042 and 2033 | 10-K page:103, page:158 to page:159 |
| Senior secured notes and debentures (class total) | 54,658 | Jun 30, 2026 | Yes | Sum of the two rows above after 2026 repurchases (sterling remeasured to 829 and 862) | 10-Q Jun 2026 page:10 to page:11 |
| Charter Operating credit facilities (Terms A-6, A-7, B-3, B-4, B-5 and Revolving Loans B and C) | 12,453 principal | Jun 30, 2026 | Yes | Guaranteed by CCO Holdings and the operating subsidiaries; secured on substantially all assets and pledged equity; maturities 2027 to 2031; Revolving Loan C up to 5,500 to March 15, 2030; Revolving Loan B about 960 to August 31, 2027 | 10-Q Jun 2026 page:10 to page:11; 10-K page:157 to page:158 |
| Total debt (principal) | 93,845 | Jun 30, 2026 | n/a | Carrying value 93,959; fair value 83,550 | 10-Q Jun 2026 page:10 |
| Equipment installment plan financing facility (CCO EIP Financing, LLC) | 1,596 | Jun 30, 2026 | No | Senior secured by installment receivables of 2.3 billion and restricted cash 90; not guaranteed by the group; capacity 2.0 billion; final maturity November 3, 2029 | 10-Q Jun 2026 page:11 to page:12, page:35 |
| Short-term borrowings (deferred payment program) | 1,155 | Jun 30, 2026 | No | Unsecured vendor payment obligations with interest, inside accrued liabilities | 10-Q Jun 2026 page:9 to page:10 |
| Supply chain finance obligations | 725 | Jun 30, 2026 | No | Vendor obligations extended through third-party financing; no collateral | 10-Q Jun 2026 page:10 |
| Operating lease liabilities | 1,276 (undiscounted 1,515) | Dec 31, 2025 | No | Real estate, dark fiber, colocation; 2026 payments 331 | 10-K page:153 to page:154 |
| Cross-currency derivative liability | 442 | Jun 30, 2026 | No | Swaps on 1.275 billion pounds sterling of notes; maturities June 2031 and July 2042; marked to market | 10-Q Jun 2026 page:13; 10-K page:162 |
| Contractual obligations (programming, content, devices, network; company and parent companies) | 17,122; 4,503 due in 2026 | Dec 31, 2025 | No | Issuer share not separable | 10-K page:182 |
| Letters of credit and surety bonds | 364 (26 under the facility) and 474 | Dec 31, 2025 | No | Casualty collateral; 26 reduces facility availability | 10-K page:157, page:182 |
| Mortgage note on the Stamford headquarters building | about 256 | Jun 30, 2026 | Not stated | Guaranteed by the Obligor Group and ranks equally with the collateral liens | 10-Q Jun 2026 page:34 |
| Unfunded unqualified pension plan | 17 | Dec 31, 2025 | No | Qualified plan settled in 2025 | 10-K page:184 |
| Accrued interest | 1,279 | Jun 30, 2026 | No | Current liability | 10-Q Jun 2026 page:9 |
| Cox Transactions: cash purchase price and assumed net debt and finance leases (parent-level; not yet issuer claims) | about 4,200 and about 12,400 (10-K: 4,000 and 12,600 pro forma) | Jun 30, 2026 | No | Cox notes expected to become guaranteed and secured debt; part or all of the new debt may do the same; payer and issuer of new debt not stated | 10-Q Jun 2026 page:9, page:27, page:34; 10-K page:28, page:64 |
| Litigation | Not quantified | Dec 31, 2025 | No | No range given; company does not expect a material effect from the disclosed investigation | 10-K page:182 to page:183 |

Debt maturities by year at December 31, 2025 (US$m, principal): 2026 1,055 (fixed 750 and variable 305), 2027 3,555 (fixed 3,250 and variable 305), 2028 5,392 (fixed 4,750 and variable 642), 2029 7,279 (fixed 7,000 and variable 279), 2030 13,868 (fixed 5,800 and variable 8,068) and thereafter 63,468 (fixed 61,118 and variable 2,350), total 94,617 (10-K page:105, page:160). Scheduled interest on that debt was 4,817, 4,646, 4,456, 4,212, 3,659 and 36,628 thereafter, total 58,418 (10-K page:160), giving principal plus interest of 5,872 for 2026, 8,201 for 2027, 9,848 for 2028, 11,491 for 2029 and 17,527 for 2030 (calculated). These totals pre-date the January and February 2026 transactions and the Q2 2026 repurchases.

### Liquidity by facility

| Component (US$m) | Dec 31, 2025 | Jun 30, 2026 | Locator |
| --- | --- | --- | --- |
| Cash and cash equivalents (unrestricted) | 218 | 285 | 10-K page:140; 10-Q Jun 2026 page:5 |
| Charter Operating revolving commitments (Revolving Loan B about 960; Revolving Loan C up to 5,500) | 6,460 | Not supplied: facility split not printed | 10-K page:157 |
| less revolving loans outstanding | (2,100 on Revolving Loan C; 2,007 implied by the principal tie-out) | Not supplied | 10-K page:157 |
| less letters of credit drawn on the facility | (26) | Not supplied | 10-K page:157, page:182 |
| Availability under the Charter Operating credit facilities, as printed | about 4,400 (rebuild 4,334 to 4,427) | about 3,700 | 10-K page:92, page:104; 10-Q Jun 2026 page:11, page:27 |
| Liquidity (cash plus printed availability) | 4,618 | 3,985 | Calculated |
| Restricted cash, excluded | 121 | 90 | 10-K page:142; 10-Q Jun 2026 page:7 |
| Equipment installment plan facility headroom, not counted | 2,000 capacity less 1,447 | 2,000 capacity less 1,596 (404 undrawn, subject to receivables) | 10-K page:161; 10-Q Jun 2026 page:12 |

Expiries within twelve months of the as-of date (to November 5, 2027): the Revolving Loan B of about USD 960 million on August 31, 2027; the remaining USD 1,000 million of 5.125% notes due May 1, 2027 (calculated); about USD 305 million of annual term loan amortisation; and the renewal of the equipment installment plan facility's twelve-month revolving period (date not printed). The Revolving Loan C of up to USD 5,500 million runs to March 15, 2030, so the principal revolving capacity is not near expiry. Facility-level availability at June 30, 2026 and the letters of credit under it are not printed.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity |
| --- | --- | --- | --- |
| Cox closing, financing and perimeter | Cox notes and new debt are expected to join the guaranteed and secured group while Cox earnings may sit outside the issuer; pre-closing covenants limit new debt | Secured claims ahead of the unsecured notes could grow without a matching EBITDA base in the issuer's statements; no pro forma leverage can be computed | Critical |
| Subordination of the unsecured notes | USD 26,734 million of unsecured notes sit behind USD 67,111 million of secured debt, and 2026 repurchases of unsecured notes were funded alongside credit facility growth | Attachment at 3.02x and detachment at 4.22x leave little room before the unsecured layer is affected; the layer moves with any secured issuance | Material |
| Revenue and EBITDA erosion | Internet and video customers fall against fibre and fixed wireless entrants; costs are largely fixed | Leverage rises as EBITDA falls (4.69x at a 10% decline, 4.96x at 15%, constant debt) | Material |
| Parent cash leakage | Distributions exceeded free cash flow by USD 828 million over the last twelve months; the issuer is the primary funder of Charter's buybacks | Net debt reduction depends on a policy range, not a cap; policy may change after the Cox closing | Material |
| Refinancing in 2029 and 2030 | USD 21,147 million falls due in two years; new notes carry higher coupons | Cash interest rises with each refinancing and depends on market access | Material |
| Covenant visibility | Ratios printed only at December 31, 2025; definitions, baskets and management-fee add-back not supplied | Headroom now is unknown; the computed ratios are not covenant ratios | Material |
| Floating-rate exposure | About 13% of principal floats and no interest rate derivatives are described | About USD 125 million per 1.00% move before floors | Minor |
| Subsidised build and intangible assets | Build-out milestone penalties are possible; franchises and goodwill are 63.34% of assets with a fair-value cushion of more than 10% | Capital is committed ahead of subsidy receipt; an impairment would be non-cash | Minor |

### Event calendar after the as-of date

| Date | Event | Source note |
| --- | --- | --- |
| Not supplied | Cox Transactions closing, end date and approvals; Liberty Broadband Combination closing | 10-Q Jun 2026 page:27 to page:28; end date not printed in the pack |
| Around Nov 2026 | Equipment installment plan facility's twelve-month revolving period renewal (inference from the November 2025 amendment; date not printed) | 10-K page:161; 10-Q Jun 2026 page:12 |
| May 1, 2027 | Remaining 1,000 of 5.125% senior notes due 2027 mature (calculated) | 10-K page:102; 10-Q Mar 2026 page:11 |
| Aug 31, 2027 | Revolving Loan B commitment of about 960 matures | 10-K page:157 |
| End of 2027 | Network evolution programme expected to be largely complete (management expectation) | 10-K page:7 |
| Feb 1, Feb 15 and Mar 15, 2028 | 2,500 of 5.000% CCO Holdings notes, 1,000 of 3.750% and 1,250 of 4.200% Charter Operating notes mature; Term A-6 final maturity Aug 31, 2028 | 10-K page:102 to page:103, page:157 |
| 2029 and 2030 | 7,279 and 13,868 of year-end maturities, including Revolving Loan C and Terms A-7, B-3 and B-4 in 2030 | 10-K page:105, page:160 |

These are contract terms and scheduled dates, not events that have occurred. Nothing is supplied after July 24, 2026.

## Calculations

All inputs in USD millions from CP-1 or the cited pages. Ratios use principal debt and company Adjusted EBITDA and are not covenant ratios.

- Restated from CP-1: total debt / LTM Adjusted EBITDA 93,845 / 22,251 = 4.22x; net debt 93,560 / 22,251 = 4.20x; secured debt 67,111 / 22,251 = 3.02x; cash interest cover 22,251 / 5,024 = 4.43x; margin 22,251 / 54,396 = 40.91%.
- EBITDA sensitivity at constant debt 93,845: -5% EBITDA 21,138 gives 4.44x; -10% 20,026 gives 4.69x; -15% 18,913 gives 4.96x; -20% 17,801 gives 5.27x.
- Cash conversion: capital expenditure 12,064 / 22,251 = 54.22%; EBITDA less capital expenditure 22,251 - 12,064 = 10,187, or 45.78% of EBITDA; cover of cash interest 10,187 / 5,024 = 2.03x; cash interest / EBITDA 5,024 / 22,251 = 22.58%; free cash flow / EBITDA 5,070 / 22,251 = 22.79%.
- Free cash flow less distributions: LTM 5,070 - 5,898 = -828; FY2025 5,827 - 6,794 = -967; 6M 2026 2,492 - 2,460 = +32.
- Liquidity: 285 + 3,700 = 3,985; December 31, 2025 218 + 4,400 = 4,618; liquidity / current portion of debt 3,985 / 999 = 3.99x. Rebuild at year-end: 960 + 5,500 = 6,460; 11,949 - 9,942 term loans = 2,007 drawn; 6,460 - 2,007 - 26 = 4,427; using 2,100 drawn, 6,460 - 2,100 - 26 = 4,334. Equipment installment plan facility: 2,000 - 1,596 = 404.
- Maturity concentration: 2029 and 2030 7,279 + 13,868 = 21,147; 21,147 / 94,617 = 22.35%. After 2030: 63,468 / 94,617 = 67.08%. Year-end fixed rate 82,668 / 94,617 = 87.37% (printed approximately 87%); June 30, 2026 notes 26,734 + 54,658 = 81,392, or 86.73% of 93,845, and credit facilities 12,453 = 13.27%.
- Adjusted 2026 and 2027 scheduled principal: 1,055 - 750 = 305; 3,555 - 2,250 = 1,305 (CP-1).
- Floating-rate sensitivity: 1.00% of credit facility debt 12,453 = 124.5 (about 125); of year-end variable debt 11,949 = 119.5; of the equipment installment plan facility 1,596 = 16.0. 124.5 / 5,024 = 2.48% of LTM cash interest.
- Coupon change on the early 2026 refinancing: new 1,750 x 7.000% + 1,250 x 7.375% = 122.5 + 92.2 = 214.7; retired 750 x 5.500% + 2,250 x 5.125% = 41.3 + 115.3 = 156.6; difference 58.1 per year (gross, before the saving on the 1,249 of repurchases, series and coupons unknown).
- Principal plus interest by year from the 10-K: 2026 1,055 + 4,817 = 5,872; 2027 3,555 + 4,646 = 8,201; 2028 5,392 + 4,456 = 9,848; 2029 7,279 + 4,212 = 11,491; 2030 13,868 + 3,659 = 17,527.
- Covenant headroom from printed December 31, 2025 ratios: indenture 6.0 - 4.0 = 2.0 turns, 1 - 4.0 / 6.0 = 33%; credit facility total 5.0 - 2.8 = 2.2 turns, 1 - 2.8 / 5.0 = 44%; first lien 4.0 - 2.8 = 1.2 turns, 1 - 2.8 / 4.0 = 30% (constant debt; ratios rounded).
- Capital structure layers (June 30, 2026): secured 54,658 + 12,453 = 67,111, 71.5% of 93,845; unsecured 26,734, 28.5%.
- Cox cash components: 3,500 + 500 = 4,000 (10-K); 3,500 + 650 = 4,150, stated as about 4,200 (10-Qs).

## Gaps

| Gap | Why it matters | Affects | Severity | Action |
| --- | --- | --- | --- | --- |
| Cox Transaction Agreement, financing, end date, approvals, post-closing perimeter and issuer of the new debt not supplied; nothing after July 24, 2026 | Determines whether secured claims grow ahead of the unsecured notes and whether Cox earnings are inside the issuer | Credit view, structure | High | Obtain the agreement, proxy statement, financing commitments and later 8-K filings |
| Executed indentures, Charter Operating credit agreement and intercreditor agreement not supplied | Definitions, baskets, release provisions, change-of-control and cross-default terms cannot be tested | Covenants, structure | High | Obtain executed documents |
| Covenant ratios after December 31, 2025, covenant EBITDA bridge and the management fee amount (only to 0.1 billion) not supplied | Current headroom cannot be measured; computed ratios are not covenant ratios | Covenant risk | High | Obtain compliance certificates |
| Current series-level debt schedule and mapping of the 1,249 of repurchases not supplied | The current maturity ladder and coupon cost cannot be rebuilt exactly | Refinancing | Medium | Obtain a current debt schedule |
| Facility-level availability and letters of credit at June 30, 2026 not printed; availability printed to 0.1 billion | Liquidity is accurate to about 50 | Liquidity | Medium | Obtain facility schedule |
| Whether the 256 mortgage note is in the debt figure, issuer share of the 17,122 contractual obligations and operating leases after December 31, 2025 not stated | Fixed claims outside debt may be understated | Claims outside debt | Medium | Obtain issuer-level commitments |
| Entity structure chart is an image and was not extracted | Ownership percentages and debt by entity unconfirmed | Structure | Medium | Check the filed 10-K chart |
| Credit ratings and agency actions not stated; no market prices or peer data used | Not required for this scope | Relative value (not in scope) | Low | None |
| Adjusted EBITDA is a company non-GAAP measure with management-defined add-backs | Leverage and cover could differ on other definitions | Ratios | Medium | Treat ratios as indicative |

## Next module

- CP-5: trace each CP-2 figure to its CP-1 or CP-1A figure or page locator; mark as calculated the sensitivity, cash conversion, concentration, coupon change, liquidity cover and headroom rows in the Calculations section; check the sign and direction of every comparison, including the rise in leverage from 4.17x to 4.22x, the fall in availability from about USD 4,600 million to USD 3,700 million and the 10% EBITDA sensitivity of 4.69x.
- Downstream use: carry the unresolved Cox structure, the missing executed documents and covenant values, and the subordination of the unsecured notes as restrictions; do not treat the principal-debt ratios as covenant ratios; make no recovery, instrument or relative-value conclusion from this answer.
