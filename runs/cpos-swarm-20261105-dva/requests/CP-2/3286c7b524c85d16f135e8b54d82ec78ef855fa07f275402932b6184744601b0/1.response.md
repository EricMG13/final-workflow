# CP-2 — Fundamental credit synthesis: DAVITA INC. (dva)

## Request

DAVITA INC. (issuer id `dva`), as of 2026-11-05, pathway `credit_snapshot`, asks for the fundamental credit view from the upstream financial base and the business and transaction context. Scope is the consolidated company in USD millions for FY2025 and the first three quarters of 2026, with no peer ranking, instrument recommendation or recovery conclusion.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_dva-20251231.htm.jsonl | e8c363b79225d32d92e8856c1234363883b84595e0f356cf12128301c572a94b | Audited FY2025 statements; covenant text, contractual obligations, interest rate sensitivity, lease schedule |
| 10-Q_2026-03-31_dva-20260331.htm.jsonl | 7063ac673c62a3a12d361c8ab9f216c83e6406eb95937f85ad2f6c47a221fe01 | Q1 2026 balance sheet and liquidity |
| 10-Q_2026-06-30_dva-20260630.htm.jsonl | 5aed5931f3b50f8efc4d5398264cb7a317623aeb269a49968c33246ed0273365 | Q2 2026 balance sheet, liquidity and maturities |
| 10-Q_2026-09-30_dva-20260930.htm.jsonl | 99b4bb0c8f87c03db2290c95cfd812d4622509e8fdbcdce46d84afcedef79236 | Q3 2026 debt note, maturities, caps, liquidity, share repurchases |
| EX-99.1_2026-05-05_dva33126ex991.htm.jsonl | c5727d9383becddd69bf1cd80efadc8ee72012f8313405a8b1414b2f74143fa7 | Q1 2026 release: leverage ratio (supporting) |
| EX-99.1_2026-08-04_dva63026ex991.htm.jsonl | e55a9fe053fe9f69274156863d81212ffe989a931913bc64dfc65b70fd8151a2 | Q2 2026 release: leverage ratio (supporting) |
| EX-99.1_2026-10-29_dva93026ex991.htm.jsonl | b062a4dfa0aa9b3cce4ee385c1a8aad8546180810a3acbc585a968f93eadfc64 | Q3 2026 release: leverage ratio, covenant maximum, guidance (supporting) |
| context | 888318ae2603a71d9f443112e6d0298861b2ea95d8c8a8118da68f80c88bfe70 | User run settings; not issuer evidence |

| Handoff | sha256 | Use |
| --- | --- | --- |
| CP-0 | 3ecf1492bb810c2e90133183ed7699bad1c56c1780a9f8736f0e2c4391db50f2 | Source readiness and limits |
| CP-1 | 3cfbf98d548042fd31ec6ebfe100057e48caebe480e0597af9abd9a0b0ee8fc9 | Financial base: debt, liquidity, maturities, covenant picture, claims outside debt |
| CP-1A | 9451150fe7d243d9c2cc5ebdabe9029317cc1a59d7b1fd0e9903edffd39634aa | Business and ownership context, payor concentration, capital allocation, timeline |

Locators are `page:N` of the pinned `.jsonl` text of each source. Tags: [10-K] annual report, [Q1 10-Q], [Q2 10-Q], [Q3 10-Q] quarterly reports, [Q1 ER], [Q2 ER], [Q3 ER] earnings releases. This answer relies on CP-1 and CP-1A for figures and facts; it cites source pages only where it adds a fact or a calculation.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| DaVita is a stable, cash-generative credit whose leverage is rising because buybacks exceed free cash flow. Covenant-basis leverage is 3.38x against a 5.00x maximum, and liquidity is adequate. Refinancing risk is concentrated in 2030 and 2031. | Medium | The credit agreement, indentures and guarantor list are not supplied, so covenant definitions and headroom are company-reported figures that cannot be verified. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Liquidity was USD 1,915.6 million at Q3 2026, cash plus undrawn revolver, down from USD 2,176.4 million at FY2025. | Cover for scheduled principal through 2029 is ample, but the cushion narrowed. | High |
| Buybacks of USD 870.2 million in nine months 2026 exceeded free cash flow of USD 672 million, and total debt rose to USD 10,832.2 million. | Shareholder returns, not deleveraging, set the leverage path. | Medium |
| Debt maturing in 2030 and 2031 is USD 8,335.4 million, 77% of the total, and notes there carry coupons of 4.625% and 3.75%. | Refinancing at recent issue coupons would raise interest cost. | Medium |
| Covenant-basis leverage of 3.38x leaves 1.62x of headroom to the 5.00x maximum on company figures. | Headroom looks wide but the definitions cannot be verified. | Low |
| U.S. dialysis earned 97.3% of segment margin, and commercial payors, 26% of U.S. dialysis revenue, generate nearly all profit. | Earnings depend on commercial mix and Medicare rate setting. | High |

### Credit view

DaVita Inc. is a stable but increasingly shareholder-oriented credit: leverage is moderate and covenant headroom wide, yet leverage is rising because buybacks outrun free cash flow. The strongest support is recurring dialysis demand, with U.S. dialysis earning 97.3% of segment margin, USD 1,915.6 million of cash and undrawn revolver, and no year of scheduled principal above USD 160.4 million until 2030. The weakest point is capital allocation: USD 870.2 million of buybacks in nine months 2026 exceeded free cash flow of USD 672 million while covenant-basis leverage rose to 3.38x from 3.26x, and 77% of debt falls due in 2030 and 2031. What decides the outcome is commercial payor mix and Medicare rates, and whether management keeps leverage inside its range.

### Credit assessment

| Assessment | Category | Confidence | Basis |
| --- | --- | --- | --- |
| Fundamental view: a large, recurring-revenue dialysis business with moderate leverage and adequate liquidity, offset by rising leverage from buybacks, falling unit margin, commercial-payor profit concentration and a heavy 2030 to 2031 maturity wall. Not a rating and not a recommendation. | Analyst Interpretation | Medium (below High because the credit agreement, indentures and guarantor list are not supplied) | CP-1 debt, liquidity, maturity and ratio figures; CP-1A segment, payor, ownership and capital-allocation rows |

### Key findings

First, DaVita Inc. earns its profit in one place. U.S. dialysis produced USD 1,588.1 million of USD 1,632.4 million of segment operating margin in nine months 2026, or 97.3%, and non-hospital commercial payors are 26% of U.S. dialysis revenue and 11% of patients but generate nearly all profit [CP-1A]. Revenue visibility is high because dialysis is recurring, but price is set by Medicare and by negotiated commercial rates, so a shift in commercial mix moves earnings sharply. Revenue per treatment rose 2.7% in nine months 2026 while patient care costs per treatment rose 3.0%, and the share of commercial revenue slipped to 31.9% from 32.5% (Documentary Fact and Analyst Interpretation).

Second, leverage is moderate but rising. Total debt principal was USD 10,832.2 million at September 30, 2026, up USD 487.7 million from December 31, 2025, while cash and cash equivalents fell to USD 495.6 million from USD 676.4 million [CP-1]. Covenant-basis net leverage rose to 3.38x from 3.26x on Consolidated EBITDA of USD 3,042 million, and total debt over that EBITDA is 3.56x. The 10-K says leverage stayed within a 3.0x to 3.5x target range throughout 2025 and prints no 2026 target [CP-1A]. On a stricter EBITDA of operating income plus depreciation and amortization plus impairment (USD 2,880.9 million) total debt is 3.76x. Debt expense over the last twelve months was USD 593.7 million, and Consolidated EBITDA over it is 5.12x (expense basis, because interim cash interest is not printed).

Third, DaVita Inc. returns more cash to shareholders than it keeps. Share repurchases cost USD 870.2 million in nine months 2026 against company free cash flow of USD 672 million and operating cash flow less capital additions of USD 898.4 million, which means buybacks absorbed 96.9% of the latter, and net debt issuance was USD 490 million [CP-1]. Free cash flow after buybacks was therefore negative USD 198.2 million for the period (calculated). Total equity is a deficit of USD 358.5 million. The company pays no cash dividend, the Board has authorised USD 4,000 million of repurchases in two steps since September 2024, and about USD 1,212 million remained available at October 27, 2026 [CP-1A; Q3 10-Q page:19]. The credit facilities restrict repurchases, but many of those limits fall away while leverage is below 4.00x, which it is at 3.38x (Analyst Interpretation).

Fourth, liquidity is adequate and the near-term maturity profile is light. Cash of USD 495.6 million plus USD 1,420.0 million of undrawn revolver is USD 1,915.6 million, 4.2 times the USD 451.7 million of scheduled principal due from the rest of 2026 through 2029 (calculated). No facility expires within twelve months of the as-of date; the revolver matures November 24, 2030, or March 2, 2030 if the 4.625% senior notes are still outstanding 91 days before their maturity. That springing date puts USD 2,042.5 million of Term Loan A-2 and revolver balances in 2030 ahead of the notes' June 1, 2030 maturity [CP-1].

Fifth, refinancing is concentrated and would reprice. Maturities are USD 4,570.3 million in 2030 and USD 3,765.1 million in 2031, together USD 8,335.4 million or 77% of total debt [CP-1]. The 4.625% senior notes (USD 2,750.0 million) and 3.75% senior notes (USD 1,500.0 million) sit in that window. DaVita Inc. issued its 6.75% senior notes due 2033 in May 2025 [CP-1A]. As an illustration only, replacing those two series at 6.75% would add about USD 103.4 million of annual interest, 17.4% of last-twelve-months debt expense (calculated; not a forecast).

Sixth, covenant headroom looks wide on company figures but cannot be verified. The credit agreement sets a maximum leverage ratio of 5.00:1.00 through December 31, 2028, falling to 4.50:1.00, against a reported 3.38x, so headroom is 1.62x. At constant Consolidated net debt of USD 10,269 million, Consolidated EBITDA could fall to USD 2,053.8 million, a cushion of USD 988.2 million or 32.5%, before the 5.00x maximum; and 15.6% before the 4.00x level below which many restrictions lapse (calculated) [CP-1]. The Consolidated EBITDA definition includes pro forma adjustments, expected cost savings and other add-backs set by an agreement that is not supplied, so these cushions are company-basis (Insufficient Information on the definitions).

Seventh, claims outside the debt figure are large but different in kind. Operating lease liabilities are USD 2,623.3 million, noncontrolling interests subject to put provisions are USD 1,484.3 million, and letters of credit of about USD 184.8 million sit under a separate bilateral facility [CP-1]. Consolidated EBITDA is after lease cost, so adding the lease liability to debt would mix bases and is not done. Distributions to minority partners were USD 243.8 million in nine months 2026 against their income of USD 201.8 million, so part of consolidated EBITDA leaves the group [CP-1; CP-1A].

Eighth, interest rate and policy exposure are bounded but real. Floating-rate debt of USD 894.5 million is not covered by the interest rate caps, which hedge USD 3,500.0 million of notional through 2028 at weighted average strikes of 4.32% to 4.46%, rising to 4.75% in 2029 and 5.25% in 2030 [CP-1]. A one-point rise on the uncovered amount would cost about USD 8.9 million a year before tax (calculated). The 10-K estimates the effect of a 100 basis point rise at about USD 5.3 million of net income for 2025, net of tax and caps [10-K page:142]. Policy and legal risk is larger: a transitional drug add-on payment ends in 2026, an HHS Kidney Care National Plan was issued October 20, 2026, and False Claims Act, California Department of Insurance, District of Columbia and Federal Trade Commission matters are open with accruals described as immaterial [CP-1A]. A China impairment of USD 62.2 million in Q3 2026 shows international reimbursement risk, though international is about 10% of revenue (Documentary Fact; [10-K] page:142).

### Strengths and weaknesses

Strengths. (1) Recurring, non-discretionary demand and scale: 3,269 centers and about 298,100 patients, with U.S. dialysis 84.9% of segment revenue and 97.3% of segment margin, and no commercial payor above 10% of U.S. dialysis revenue (Documentary Fact; CP-1A). (2) Adequate liquidity: USD 1,915.6 million of cash and undrawn revolver with no facility expiring within twelve months of the as-of date (Documentary Fact; CP-1). (3) Light near-term maturities: scheduled principal of USD 31.4 million, USD 113.0 million, USD 160.4 million and USD 146.9 million for the rest of 2026 through 2029, with the first final maturity in 2030 (Documentary Fact; CP-1). (4) Wide company-basis covenant headroom of 1.62x and a 0.62x margin below the 4.00x restriction-relief level (Analyst Interpretation on company figures; CP-1). (5) Low maintenance capital intensity: maintenance and development capital expenditure of USD 431 million against depreciation and amortization of USD 510.8 million in nine months 2026 (Documentary Fact; CP-1). (6) Transparent leverage disclosure each quarter, an audited FY2025 with an unqualified opinion, and no creditor-adverse transaction found in the documented history (Documentary Fact and Insufficient Information; CP-1A).

Weaknesses. (1) Rising leverage from capital returns: buybacks of USD 870.2 million exceeded free cash flow of USD 672 million, net debt issuance was USD 490 million and total equity is a deficit (Documentary Fact and calculation; CP-1, CP-1A). (2) Profit concentration: one segment earns 97.3% of segment margin and commercial payors generate nearly all profit while commercial revenue grew only 1.2% against 4.0% for Medicare and Medicare Advantage (Documentary Fact and Analyst Interpretation; CP-1A). (3) Unit-margin squeeze: patient care costs per treatment up 3.0% against revenue per treatment up 2.7%, with wage, supply and insurance inflation and union organizing (Documentary Fact; CP-1A). (4) Back-ended, repricing maturity wall: 77% of debt in 2030 and 2031, a springing March 2, 2030 date for USD 2,042.5 million of bank debt, and low-coupon notes that would refinance at higher rates (Documentary Fact and calculation; CP-1). (5) Cash leakage to minority partners and puttable interests of USD 1,484.3 million (Documentary Fact; CP-1, CP-1A). (6) Unverified definitions: Consolidated EBITDA and the covenant ratio are company-computed, and cash interest cover exists only for FY2025 (Insufficient Information; CP-1). (7) Regulatory, litigation and policy exposure with no quantified downside (Insufficient Information; CP-1A).

### Debt and claims inventory

| Claim | Amount (US$m) | Date | Inside the debt figure? | Security, guarantors, maturity | Locator |
| --- | --- | --- | --- | --- | --- |
| Term Loan A-2 | 1,962.5 | Sept 30, 2026 | Yes | Senior secured; guaranteed; November 24, 2030 (March 2, 2030 if 4.625% notes remain); SOFR + 1.50% | [Q3 10-Q] page:11; [10-K] page:183 |
| Term Loan B-2 | 2,352.0 | Sept 30, 2026 | Yes | Senior secured; guaranteed; May 9, 2031; SOFR + 1.75% | [Q3 10-Q] page:11 |
| Revolving line of credit (1,500.0 commitment) | 80.0 drawn | Sept 30, 2026 | Yes | Senior secured; guaranteed; November 24, 2030 (March 2, 2030 if 4.625% notes remain) | [Q3 10-Q] page:11, page:14 |
| 4.625% Senior Notes | 2,750.0 | Sept 30, 2026 | Yes | Senior unsecured; subsidiary guarantors party to the indenture; June 1, 2030 | [Q3 10-Q] page:11; [10-K] page:213 |
| 3.75% Senior Notes | 1,500.0 | Sept 30, 2026 | Yes | Senior unsecured; February 15, 2031 | [Q3 10-Q] page:11 |
| 6.875% Senior Notes | 1,000.0 | Sept 30, 2026 | Yes | Senior unsecured; September 1, 2032 | [Q3 10-Q] page:11 |
| 6.75% Senior Notes | 1,000.0 | Sept 30, 2026 | Yes | Senior unsecured; guaranteed by domestic subsidiaries that guarantee the credit facilities; July 15, 2033 | [Q3 10-Q] page:11; [10-K] page:184 |
| Acquisition obligations and other notes payable | 36.2 | Sept 30, 2026 | Yes | Security not stated; 2026 to 2038 | [Q3 10-Q] page:11 |
| Financing lease obligations | 151.6 | Sept 30, 2026 | Yes | Lease obligations; 2027 to 2039 | [Q3 10-Q] page:11 |
| Total debt principal outstanding | 10,832.2 | Sept 30, 2026 | n/a | Carrying value 10,769.1 after 63.1 of discount and financing costs | [Q3 10-Q] page:11 |
| Operating lease liabilities (current 438.1 plus long-term 2,185.2) | 2,623.3 | Sept 30, 2026 | No | Dialysis facility leases; undiscounted payments 3,001.1 at December 31, 2025 | [Q3 10-Q] page:3; [10-K] page:188 |
| Noncontrolling interests subject to put provisions | 1,484.3 | Sept 30, 2026 | No | Temporary equity; 1,408 of 1,532 fell in the 2026 column at December 31, 2025, plus 66 off balance sheet | [Q3 10-Q] page:3; [10-K] page:135 |
| Letters of credit, separate bilateral secured facility | 184.8 | Sept 30, 2026 | No | Contingent; do not reduce the revolver; capacity not stated | [Q3 10-Q] page:14 |
| Supplier minimum purchase commitments | 961.1 (2026), 956.2 (2027), 752.6 (2028), 577.3 (2029), 445.9 (2030) | Dec 31, 2025 | No | Shortfall payable to supplier; not updated in the 10-Qs | [10-K] page:195 |
| Working capital funding and milestone investments | 8.2 and 13.0 | Dec 31, 2025 | No | Potential commitments to nonconsolidated businesses | [10-K] page:195 |
| Berkshire repurchase payable (due to related party) | 54.7 | Sept 30, 2026 | No | Settled October 27, 2026 for 69.0 | [Q3 10-Q] page:3, page:19 |
| Legal and regulatory matters | Accruals immaterial | Sept 30, 2026 | No | Open False Claims Act, insurance, antitrust and FTC matters; no estimate | [Q3 10-Q] page:14 to page:17 |
| Pensions, factoring, supply-chain finance | Not found | Sept 30, 2026 | n/a | No obligation line or programme found in the sources | [10-K] page:154 |

Debt maturities at September 30, 2026 (US$m): remainder of 2026 31.4, 2027 113.0, 2028 160.4, 2029 146.9, 2030 4,570.3, 2031 3,765.1, thereafter 2,045.1 (total 10,832.2) [Q3 10-Q] page:12. At December 31, 2025 the 10-K estimated interest payments on credit facilities and senior notes of 538 for 2026, 1,044 for 2027 to 2028, 947 for 2029 to 2030 and 402 thereafter, total 2,931 ([10-K] page:135); these pre-date the 2026 Term Loan B-2 increase.

### Liquidity by facility

| Component (US$m) | FY2025 | Q1 2026 | Q2 2026 | Q3 2026 | Locator |
| --- | --- | --- | --- | --- | --- |
| Cash and cash equivalents (unrestricted) | 676.4 | 644.2 | 669.0 | 495.6 | Balance sheets |
| Revolver commitment | 1,500.0 | 1,500.0 | 1,500.0 | 1,500.0 | [Q3 10-Q] page:14 |
| less drawn on revolver | 0.0 | (375.0) | (65.0) | (80.0) | Debt notes |
| less letters of credit drawn on the revolver | 0.0 | 0.0 | 0.0 | 0.0 | [Q3 10-Q] page:14 |
| Undrawn revolver | 1,500.0 | 1,125.0 | 1,435.0 | 1,420.0 | [10-K] page:132; [Q1 10-Q] page:40; [Q2 10-Q] page:42; [Q3 10-Q] page:47 |
| Total liquidity (cash plus undrawn revolver) | 2,176.4 | 1,769.2 | 2,104.0 | 1,915.6 | Calculated |
| Excluded: short-term investments | 24.3 | 22.3 | 19.9 | 70.7 | Balance sheets |
| Excluded: restricted cash and equivalents | 81.3 | 82.2 | 82.9 | 83.6 | Balance sheets |
| Memo: letters of credit under the separate bilateral facility (about) | 195 | 207 | 188 | 185 | [10-K] page:132; [Q1 10-Q] page:40; [Q2 10-Q] page:42; [Q3 10-Q] page:47 |

The revolver matures November 24, 2030 (March 2, 2030 under the springing condition), so no committed facility expires within twelve months of the as-of date. The current portion of long-term debt at September 30, 2026 is USD 112.5 million. The sources do not state the capacity of the bilateral letter of credit facility, so its headroom is Not supplied. Including short-term investments, liquidity at September 30, 2026 would be USD 1,986.3 million.

### Key credit risks

| Risk | Mechanic | Credit implication | Severity |
| --- | --- | --- | --- |
| Commercial payor mix and rate setting | Commercial payors generate nearly all profit from 11% of patients; enhanced premium tax credits expired at the end of 2025, and Medicare rates are set by CMS | A small shift in mix or an adverse rate change cuts EBITDA much more than revenue | Critical |
| Capital allocation versus leverage | Buybacks exceeded free cash flow in nine months 2026 and were part-funded by net debt issuance; many restrictions lapse below 4.00x | Leverage can drift toward 4.00x by choice; the cushion to 5.00x is company-basis | Material |
| 2030 and 2031 refinancing | 77% of debt matures in two years; USD 2,042.5 million of bank debt springs to March 2, 2030 if the 4.625% notes are not retired | Market access and rates decide the cost; low-coupon notes would reprice | Material |
| Covenant visibility | Consolidated EBITDA add-backs and definitions sit in an unsupplied agreement; only the ratio and maximum are printed | Headroom cannot be verified; an EBITDA decline could reach a test not visible here | Material |
| Unit-cost inflation | Wages, supplies, insurance and benefits outgrew revenue per treatment; union organizing continues | Margin erosion lowers cover on fixed debt service | Material |
| Legal and regulatory exposure | Open government inquiries and class action; HHS plan and expiring transitional drug payment | Unquantified downside to earnings and cash | Material |
| Minority cash leakage | Distributions to noncontrolling interests exceed their income; puts of USD 1,484.3 million | Cash available to the parent is lower than consolidated EBITDA suggests | Minor |
| International and rates | China impairment; USD 894.5 million of floating debt uncovered by caps | Bounded effect today; protection thins after 2028 | Minor |

### Event calendar after the as-of date

| Date | Event | Source note |
| --- | --- | --- |
| December 31, 2026 | 2023 interest rate cap agreements mature; 2025 caps become effective; maximum strike rates on the 2024 caps rise from 4.50% to 4.75% and from 4.00% to 4.25% | [Q3 10-Q] page:12 to page:13 |
| End of 2026 | Transitional drug add-on payment period for phosphate binders is set to expire | [10-K] page:13 |
| January 15, 2027 | 6.75% Senior Notes interest payment date (interest is paid January 15 and July 15) | [10-K] page:184 |
| Calendar year 2027 | CMS payment rule for ESRD estimated at plus 2.7% (status stated as both final and proposed) | [Q3 10-Q] page:37 |
| December 31, 2027 | Term Loan A-2 amortization steps up from 12.5 to 25.0 per quarter from March 31, 2028; 2025 cap strikes step up | [10-K] page:181; [Q3 10-Q] page:13 |
| December 31, 2028 | Maximum leverage ratio steps down from 5.00:1.00 to 4.50:1.00 | [10-K] page:183 |
| March 2, 2030 | Term Loan A-2 and revolver due if the 4.625% notes remain outstanding 91 days before maturity | [Q3 10-Q] page:11 |
| June 1, 2030 | 4.625% Senior Notes mature | [Q3 10-Q] page:11 |
| November 24, 2030 | Term Loan A-2 and revolver mature | [Q3 10-Q] page:11 |
| 2031 | 3.75% Senior Notes (February 15) and Term Loan B-2 (May 9) mature | [Q3 10-Q] page:11 |

These are contract terms and scheduled dates, not events that have occurred. Nothing is supplied after October 29, 2026, and the date of the Q4 2026 results is Not supplied.

## Calculations

All inputs are USD millions from CP-1, CP-1A or the cited pages; ratios are on company Consolidated EBITDA and are not covenant ratios unless stated.

- Liquidity: Q3 2026 495.6 + 1,420.0 = 1,915.6; FY2025 676.4 + 1,500.0 = 2,176.4; Q1 644.2 + 1,125.0 = 1,769.2; Q2 669.0 + 1,435.0 = 2,104.0; change 1,915.6 - 2,176.4 = -260.8. With short-term investments: 1,915.6 + 70.7 = 1,986.3.
- Scheduled principal, rest of 2026 through 2029: 31.4 + 113.0 + 160.4 + 146.9 = 451.7; liquidity cover 1,915.6 / 451.7 = 4.2x.
- Maturity concentration: 4,570.3 + 3,765.1 = 8,335.4; 8,335.4 / 10,832.2 = 77.0%. Springing exposure: 1,962.5 + 80.0 = 2,042.5.
- Refinancing illustration: 2,750.0 x (6.75% - 4.625%) = 58.4; 1,500.0 x (6.75% - 3.75%) = 45.0; total 103.4; 103.4 / 593.7 (last-twelve-months debt expense) = 17.4%. Uses the 6.75% coupon of the May 2025 issue as the assumed rate; not a forecast.
- Covenant headroom: 5.00 - 3.38 = 1.62x. EBITDA floor at constant net debt: 10,269 / 5.00 = 2,053.8; cushion 3,042 - 2,053.8 = 988.2 = 32.5% of 3,042. Level 4.00x: 10,269 / 4.00 = 2,567.3; cushion 3,042 - 2,567.3 = 474.8 = 15.6%; additional net debt capacity before 4.00x at constant EBITDA: 4.00 x 3,042 - 10,269 = 1,899.0; before 5.00x: 5.00 x 3,042 - 10,269 = 4,941.0.
- Capital allocation: free cash flow after buybacks 672 - 870.2 = -198.2; buybacks over operating cash flow less capital additions 870.2 / 898.4 = 96.9%; free cash flow over total debt (last twelve months) 980 / 10,832.2 = 9.0%.
- Leverage references from CP-1: total debt / Consolidated EBITDA 10,832.2 / 3,042 = 3.56x; reported covenant-basis ratio 10,269 / 3,042 = 3.38x; FY2025 9,648 / 2,960 = 3.26x; sensitivity 10,832.2 / 2,880.9 = 3.76x; Consolidated EBITDA / last-twelve-months debt expense 3,042 / 593.7 = 5.12x.
- Rate sensitivity: uncovered floating debt 894.5 x 1.00% = 8.9 per year before tax. Floating debt: Term Loan A-2 1,962.5 + Term Loan B-2 2,352.0 + revolver 80.0 = 4,394.5; caps 3,500.0; difference 894.5.
- Segment shares: U.S. dialysis margin 1,588.1 / 1,632.4 = 97.3%; revenue 9,004.0 / 10,610.1 = 84.9% (CP-1A).
- Minority leakage: distributions 243.8 against income 201.8, a difference of 42.0.

## Gaps

| Gap | Why it matters | Affects | Severity | Action |
| --- | --- | --- | --- | --- |
| Credit agreement, amendments and indentures not supplied; Consolidated EBITDA definition, add-backs and restricted-payment baskets unverifiable | Headroom, buyback capacity and change-of-control terms cannot be tested | Credit view, covenant risk | High | Obtain the executed documents and covenant compliance certificates |
| Subsidiary guarantor list and guarantor financial information not supplied | Structural subordination and guarantee coverage cannot be assessed | Debt inventory | Medium | Obtain Exhibit 21.1 and guarantor disclosure |
| Interim cash interest paid not printed (FY2025 only) | Cash interest cover cannot be shown for 2026 | Coverage | Medium | Obtain cash-flow supplemental data or use the expense-basis cover, labelled |
| Quantification of legal and regulatory matters | Downside to earnings and cash is unknown | Key credit risks | Medium | Monitor filings; accruals are immaterial |
| Events after October 29, 2026 and the Q4 2026 results date not supplied | Last week before the cutoff and the next reporting date are unknown | Credit view | Medium | Obtain later 8-Ks or confirm none |
| Ratings, market prices and peer data not supplied | Market view of the credit cannot be compared | Credit view | Low | Not required for this scope |
| Operating lease cost for the last twelve months not printed in the 10-Qs | Lease-adjusted leverage cannot be shown on a consistent basis | Leverage | Low | Use FY2025 lease cost for context only |

## Next module

CP-5: trace each figure above to CP-1 or CP-1A or to the `page:N` locators in the tables; treat the calculated rows (liquidity cover, headroom, refinancing illustration, sensitivities) as analyst calculations, and carry the unverified covenant definitions as the main restriction.
