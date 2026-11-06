## Request

Issuer: ELDORADO GOLD CORP /FI (Eldorado Gold Corporation, ticker EGO). As-of date: 2026-11-05. Cutoff: 2026-11-05. Pathway: credit_snapshot, host mode, minimum module set. Reporting currency: USD. Current period: Q3 2026 (quarter ended September 30, 2026). Prior period: FY2025.

Question for this module: what is the financial base of the issuer at the latest reported date, which reported facts are printed and which figures must be calculated, and what remains restricted? Reported facts, calculations and interpretation are kept apart below. Chart-data tables are in US$ million (leverage and interest cover in x). The financial statements print US$ thousand and the news release prints US$ million to one decimal; unit conversions are stated where used.

The upstream readiness handoff (CP-0) rated the source set READY_WITH_LIMITATIONS. Its gaps G1 to G10 are carried forward here, in particular G1 (no audited FY2025 statements), G2 (no management discussion), G5 (no issuer-reported covenant ratios) and G6 (provisional Foran allocation).

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 (as pinned) | Used for |
| --- | --- | --- |
| 40-F_2025-12-31_ego-20251231_d2.htm.jsonl | 2d84dc109f346979ffc12a8e05f174bb9ee3c9bd6fcc72c5f9456622e3a05ce3 | Checked for financial statements and debt text; none present (cover document only) |
| 6-K-EX-99.1_2026-03-31_eldoradogoldreportsfirstqu.htm.jsonl | 3b31b8f45b42d214b8f1d541ff63602490ab0a53167940d88fa15730bc28a118 | Q1 2026 narrative (cash movement) |
| 6-K-EX-99.1_2026-03-31_unauditedcondensedconsolid.htm.jsonl | 6ab28f2649ba0274d424a4a577f9d317100b3de9ac89fbdc0f56e73f18e3f38e | March 31, 2026 balance sheet, debt note, revolving facility availability |
| 6-K-EX-99.1_2026-06-30_eldoradogoldreportsq22026f.htm.jsonl | 1bf15cab552e9fcdd05ecc97d7c3b6b694607e1283203ea2fc40315ad381fe66 | Q2 2026 narrative |
| 6-K-EX-99.1_2026-06-30_unauditedcondensedconsolid.htm.jsonl | 8eec4357e5c66f092a21b76dc3bc3ec04482a3d8fa39d15deb38a763bed500e0 | June 30, 2026 balance sheet, debt note, revolving facility availability |
| 6-K-EX-99.1_2026-09-30_eldoradogoldreportsq32026f.htm.jsonl | 6528e78e0161f7a2d85b02006c1c676359a3ab495a586ed79cf2e7d97da5afc6 | Q3 2026 highlights, Adjusted EBITDA, free cash flow, guidance, prior-year debt |
| 6-K-EX-99.1_2026-09-30_unauditedcondensedconsolid.htm.jsonl | f32fd44e1756d4bad20e63e1b631e75cf54a1931414a7ce2b1f905276f2ab561 | Primary source: statements, debt, commitments, finance costs, Foran, segments |

The run context (sha256 a8b2bf5acce83dbd54227ec6757e97e8686f295cadb3f91a9fecf63c4f1d9423) is dated settings only, not issuer evidence.

### Supplied handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 21d8009ba1529b289ca644e38929935dc362f898e9ec412caa46c0a9aef62eb8 | Source readiness, gap list G1 to G10 carried into the Gaps section |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Third quarter 2026 earnings are strong on higher gold prices, but capital spending far exceeds operating cash flow. Cash fell and debt rose sharply after the Foran acquisition. Leverage cannot be stated on a trailing basis. | Medium | No full-year 2025 statements, so trailing earnings, trailing leverage and the full-year comparison cannot be built. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Nine-month 2026 operating cash flow is well below capital spending, including capitalised interest, and company-defined free cash flow is negative. | The gap is funded by cash, revolver draws and acquired debt, so liquidity is being consumed. | High |
| Debt rose from the December 2025 level to the September 2026 level, driven by the revolver draw, the overrun facility draw and debt assumed with Foran. | Higher debt lifts interest burden before Skouries and McIlvenna Bay reach commercial production. | High |
| Liquidity as cash plus undrawn revolver fell from December 2025 to September 2026, and a separate cash reserve for project loan repayments is excluded. | Headroom is thinner while capital projects remain unfinished; excluded restricted cash is not available for general use. | Medium |
| Debt maturities are spread, with the largest bucket in the third year, where the senior notes and revolver both fall due. | Refinancing is concentrated in a single year window; the project loan amortises from December 2026. | Medium |
| Adjusted EBITDA covered cash interest several times over in each period computed, but the measure is company-defined and not the covenant definition. | Cover looks comfortable, yet covenant headroom cannot be confirmed from the pack. | Medium |

### Financial base view

The financial base at September 30, 2026 is one of strong reported profitability alongside heavy investment and rising leverage. Nine-month 2026 revenue is above the prior year because the average realised gold price is higher, while gold sold is lower (the release attributes the revenue increase to price, partly offset by volume), and Adjusted EBITDA is also higher. At the same time, cash capital spending, including capitalised interest, exceeds operating cash flow, so cash has fallen and debt has risen, partly through the Foran acquisition (debt assumed) and partly through revolver draws. The base is usable for a snapshot with these limits: trailing (LTM) EBITDA and so trailing leverage are not supplied because FY2025 full-year figures are absent; interest cover is shown on matched nine-month and quarter bases only; and covenant headroom cannot be computed because the covenant definitions and issuer-reported ratios are not supplied. The September 30, 2026 balance sheet also includes the Foran acquisition on a provisional fair-value basis, and Skouries and McIlvenna Bay are not yet in commercial production, so period earnings do not yet carry their full contribution while debt and interest do.

### Chart data: leverage

| Period | Total debt / EBITDA | Net debt / EBITDA | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Q3 2026 (LTM to September 30, 2026) | Not supplied: LTM EBITDA needs FY2025 full-year EBITDA, which is not in the pack | Not supplied: LTM EBITDA needs FY2025 full-year EBITDA, which is not in the pack | x | No trailing figure is stated. Total debt is the carrying amount of 1,985.426 and net debt is that amount less unrestricted cash of 396.828 (US$m), see Calculations. |
| Nine months 2026 EBITDA annualised (not LTM) | 1.67 | 1.34 | x | Illustrative only: nine-month Adjusted EBITDA of 892.0 (US$m, non-IFRS) multiplied by 4/3 equals 1,189.3 against debt at September 30, 2026. Assumes constant run-rate; includes Foran only from April 14, 2026; Skouries not yet contributing. Net debt excludes restricted cash of 71.898. |
| FY2025 (December 31, 2025) | Not supplied: FY2025 Adjusted EBITDA is not in the pack | Not supplied: FY2025 Adjusted EBITDA is not in the pack | x | Debt of 1,275.052 and cash of 869.356 (US$m) are printed in the Q3 2026 statements as the comparative balance sheet. |

### Chart data: interest cover

| Period | EBITDA / cash interest | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Q3 2026 | 9.81 | x | Q3 2026 Adjusted EBITDA 275.2 divided by interest paid 13.165 plus capitalised interest paid 14.879 (US$m). Company-defined Adjusted EBITDA, not the covenant definition. |
| Nine months 2026 | 11.96 | x | Nine-month Adjusted EBITDA 892.0 divided by interest paid 28.611 plus capitalised interest paid 45.943 (US$m). Excluding capitalised interest the ratio would be 31.18x. |
| Q3 2025 | 11.15 | x | Q3 2025 Adjusted EBITDA 196.3 (continuing operations) divided by interest paid 9.174 plus capitalised interest paid 8.437 (US$m). |
| Nine months 2025 | 11.88 | x | Nine-month 2025 Adjusted EBITDA 571.1 (continuing operations) divided by interest paid 19.601 plus capitalised interest paid 28.457 (US$m). |
| FY2025 | Not supplied: FY2025 Adjusted EBITDA and cash interest are not in the pack | x | Full-year statements and reconciliation are in exhibits not supplied. |

### Chart data: liquidity

| Period | Cash | Undrawn committed facilities | Reporting unit | Basis and limitation |
| --- | --- | --- | --- | --- |
| Q3 2026 (September 30, 2026) | 396.828 | 274.7 | US$m | Unrestricted cash and cash equivalents. Undrawn is the reported available balance on the revolving credit facility (limit 600.0, drawn 325.0, letter of credit nil). Excludes restricted cash of 71.898 held in the project loan debt service reserve. The undrawn amount of the euro 30.0 million project VAT facility is not printed and is excluded. Accordion of up to 100.0 is uncommitted and excluded. |
| Q2 2026 (June 30, 2026) | 554.562 | 300.0 | US$m | Reported available balance on the revolving facility (limit 450.0, drawn 100.0, letter of credit about 49.7). Cash is the balance sheet amount. |
| Q1 2026 (March 31, 2026) | 629.724 | 158.1 | US$m | Reported available balance on the revolving facility (limit 350.0, letter of credit about 191.6). |
| FY2025 (December 31, 2025) | 869.356 | 106.6 | US$m | Reported available balance on the revolving facility (limit 350.0, letter of credit about 243.0). |

### Chart data: debt maturities

| Period | Debt maturing | Reporting unit | Basis and limitation |
| --- | --- | --- | --- |
| Within 1 year of September 30, 2026 | 141.053 | US$m | Principal only, interest excluded, from the commitments table; undiscounted, so it differs from the carrying amount of the current portion of debt (148.472). |
| Year 2 | 142.547 | US$m | As above. |
| Year 3 | 958.795 | US$m | Commitments table amounts of 458.795 plus senior notes principal of 500.0 due September 1, 2029, which the table omits. Includes the revolving facility of 325.0 maturing March 1, 2029. |
| Year 4 | 162.446 | US$m | Commitments table. |
| Year 5 | 354.725 | US$m | Commitments table; includes the Sprott balloon at maturity September 30, 2031. |
| Over 5 years | 258.176 | US$m | Commitments table; Term Facility final instalments to December 31, 2032 and government contributions. |

### Financials and credit metrics

| Metric (US$ thousand unless stated) | Q3 2026 | Nine months 2026 | Q3 2025 | Nine months 2025 | December 31, 2025 | Source |
| --- | --- | --- | --- | --- | --- | --- |
| Revenue (metal sales) | 511,860 | 1,531,744 | 434,727 | 1,241,696 | Not supplied: full year not in pack | Q3 statements page:1 |
| Production costs | 199,821 | 572,822 | 164,140 | 474,609 | Not supplied | Q3 statements page:1 |
| Depreciation and amortization in cost of sales | 58,722 | 166,959 | 62,829 | 188,961 | Not supplied | Q3 statements page:1 |
| Earnings from mine operations | 253,317 | 791,963 | 207,758 | 578,126 | Not supplied | Q3 statements page:1 |
| Earnings from operations | 217,314 | 705,151 | 170,720 | 460,852 | Not supplied | Q3 statements page:2 |
| Finance costs, net of capitalised interest | 13,531 | 37,660 | 8,221 | 21,134 | Not supplied | Q3 statements page:2 |
| Capitalised interest | 22,131 | 57,668 | 13,430 | 35,665 | Not supplied | Q3 statements page:17 |
| Total finance costs before capitalisation | 35,662 | 95,328 | 21,651 | 56,799 | Not supplied | Q3 statements page:17 |
| Income tax expense | 91,605 | 257,114 | 53,917 | 54,604 | Not supplied | Q3 statements page:2 |
| Net earnings from continuing operations | 117,791 | 426,198 | 56,176 | 269,969 | Not supplied | Q3 statements page:2 |
| Adjusted EBITDA (US$ million, non-IFRS) | 275.2 | 892.0 | 196.3 | 571.1 | Not supplied | Q3 release page:24 |
| Net cash from operating activities, continuing operations | 134,812 | 425,747 | 170,208 | 458,786 | Not supplied | Q3 statements page:3 |
| Additions to property, plant and equipment | 429,103 | 1,210,017 | 242,517 | 592,207 | Not supplied | Q3 statements page:3 |
| Capitalised interest paid (investing) | 14,879 | 45,943 | 8,437 | 28,457 | Not supplied | Q3 statements page:3 |
| Interest paid (financing) | 13,165 | 28,611 | 9,174 | 19,601 | Not supplied | Q3 statements page:4 |
| Dividends paid | 19,619 | 54,103 | Nil (printed as a dash) | Nil (printed as a dash) | Not supplied | Q3 statements page:4 |
| Purchase of shares for cancellation | Nil (printed as a dash) | 83,895 | 78,793 | 123,381 | Not supplied | Q3 statements page:4 |
| Free cash flow, company-defined (US$ million, non-IFRS) | (191.1) | (654.3) | (87.4) | (178.4) | Not supplied | Q3 release page:13 |
| Cash and cash equivalents, end of period | 396,828 | 396,828 | 1,043,935 | 1,043,935 | 869,356 | Q3 statements page:1 and page:4 |
| Restricted cash, current | 71,898 | 71,898 | Not supplied | Not supplied | Nil (printed as a dash) | Q3 statements page:1 |
| Debt, current portion | 148,472 | 148,472 | Not supplied | Not supplied | 47,968 | Q3 statements page:1 |
| Debt, non-current | 1,836,954 | 1,836,954 | Not supplied | Not supplied | 1,227,084 | Q3 statements page:1 |
| Total debt, carrying amount | 1,985,426 | 1,985,426 | 1,258,500 (printed in US$ million as 1,258.5) | 1,258,500 (printed in US$ million as 1,258.5) | 1,275,052 | Q3 statements page:11; Q3 release page:13 |
| Lease liabilities, current plus non-current | 14,203 | 14,203 | Not supplied | Not supplied | 14,599 | Q3 statements page:1 |
| Total assets | 10,616,882 | 10,616,882 | 6,485,400 (printed in US$ million as 6,485.4) | 6,485,400 (printed in US$ million as 6,485.4) | 6,727,297 | Q3 statements page:1; Q3 release page:13 |
| Total equity | 6,966,697 | 6,966,697 | Not supplied | Not supplied | 4,283,079 | Q3 statements page:1 |
| Revolving facility available balance (US$ million) | 274.7 | 274.7 | Not supplied | Not supplied | 106.6 | Q3 statements page:14 |

Columns for Q3 2026 and nine months 2026 repeat the same balance at September 30, 2026 for point-in-time rows. Q3 2025 and nine months 2025 columns for balance rows refer to September 30, 2025, taken only from the release's comparative column.

### Debt by instrument

| Instrument | Carrying amount, September 30, 2026 (US$ thousand) | Carrying amount, December 31, 2025 (US$ thousand) | Terms as printed |
| --- | --- | --- | --- |
| Senior Notes (net of fees and initial redemption option) | 499,059 | 498,846 | 6.25% senior unsecured notes due September 1, 2029, principal 500.0 million; guaranteed by four wholly-owned subsidiaries; restricts distributions and material asset sales |
| Senior Notes redemption option derivative asset | (4,160) | (14,703) | Embedded derivative, deducted in the debt total |
| Senior Secured Credit Facility (revolver) | 321,628 | Nil (not drawn) | Limit 600.0 million after August 12, 2026 amendment; maturity March 1, 2029; drawn 325.0 million; covenants interest cover at least 3.00x and net leverage at most 3.50x on rolling four quarters |
| Commercial Loan Facility (Term Facility) | 528,486 | 544,426 | EUR 480.4 million, six-month Euribor plus fixed margin, 70% of variable exposure swapped; non-recourse to Eldorado Gold Corporation; secured by Skouries and Hellas Gold operating assets |
| RRF Facility (Term Facility) | 207,331 | 211,568 | EUR 100.0 million at 3.04% and EUR 100.0 million at 4.06% fixed |
| Overrun Facility (Term Facility) | 68,130 | Nil | EUR 60.0 million contingent facility, fully drawn in Q2 2026, Euribor-based |
| VAT Facility | 14,477 | 34,915 | EUR 30.0 million revolving; matures the earlier of June 30, 2027 or 18 months after Skouries completion |
| Sprott Credit Facility (net of redemption option derivative of 42,495) | 355,548 | Nil | Assumed with Foran; 250 million plus 44.9 million capitalised interest; floating, 6.95% plus the greater of three-month SOFR and 2.00%; matures September 30, 2031; secured by acquired Foran assets with a Company guarantee |
| Equipment Finance Facility | 35,296 | Nil | Assumed with Foran; C$50.1 million; fixed 3.20% plus five-year CAD swap rate at draw; 60-month repayment |
| Government contribution obligations | 2,126 | Nil | Repayable government grants assumed with Foran; the commitments table shows 7,199 undiscounted |
| Total debt | 1,985,426 | 1,275,052 | Current portion 148,472 |

## Calculations

All inputs are printed in the cited sources; results are calculated here, not printed. Q3 statements means 6-K-EX-99.1_2026-09-30_unauditedcondensedconsolid.htm.jsonl and Q3 release the Q3 2026 earnings release.

1. Total debt at September 30, 2026: 148,472 current plus 1,836,954 non-current equals 1,985,426 (US$ thousand), which matches the printed debt note total. The movement from December 31, 2025 is 1,985,426 less 1,275,052 equals 710,374, which equals the sum of instrument-level changes in the debt note.
2. Net debt at September 30, 2026: 1,985,426 less unrestricted cash 396,828 equals 1,588,598. If restricted cash of 71,898 is also deducted, 1,516,700. Net debt at December 31, 2025: 1,275,052 less 869,356 equals 405,696 (no restricted cash was held then).
3. Illustrative leverage (not LTM): Adjusted EBITDA nine months 2026 of 892.0 times 4/3 equals 1,189.3 (US$m). Total debt 1,985.426 divided by 1,189.3 equals 1.67x. Net debt 1,588.598 divided by 1,189.3 equals 1.34x. The method is a straight-line scale-up and is not a trailing twelve-month figure; no figure is stated for LTM because FY2025 EBITDA is not supplied.
4. Interest cover (US$m): Q3 2026 275.2 / (13.165 + 14.879 = 28.044) equals 9.81x. Nine months 2026 892.0 / (28.611 + 45.943 = 74.554) equals 11.96x. Q3 2025 196.3 / (9.174 + 8.437 = 17.611) equals 11.15x. Nine months 2025 571.1 / (19.601 + 28.457 = 48.058) equals 11.88x. Excluding capitalised interest paid, nine months 2026 is 892.0 / 28.611 equals 31.18x. Cash interest here is cash paid on debt: interest paid in financing activities plus capitalised interest paid in investing activities. Adjusted EBITDA is the company's non-IFRS measure.
5. Liquidity at September 30, 2026: 396.828 plus 274.7 equals 671.528 (US$m). At June 30, 2026: 554.562 plus 300.0 equals 854.562. At March 31, 2026: 629.724 plus 158.1 equals 787.824. At December 31, 2025: 869.356 plus 106.6 equals 975.956. Restricted cash is excluded in every period. The printed available balance was used rather than facility limit less drawn amount: at September 30, 2026 600.0 less 325.0 equals 275.0 against 274.7 printed; the 0.3 difference is not explained in the sources.
6. Debt maturity buckets (US$m): sum of the Q3 commitments table rows by column, plus 500.0 senior notes in year 3. Year 1: 0 + 115.532 + 15.628 + 9.242 + 0.651 = 141.053. Year 2: 100.887 + 31.255 + 9.816 + 0.589 = 142.547. Year 3: 325.000 + 92.480 + 31.255 + 10.060 + 500.0 = 958.795. Year 4: 126.109 + 31.255 + 5.082 = 162.446. Year 5: 168.145 + 185.467 + 1.113 = 354.725. Over 5 years: 252.217 + 5.959 = 258.176. Total 2,017.742 versus the sum of principal amounts 500.0 + 325.0 + 855.369 + 294.860 + 35.313 + 7.199 = 2,017.741 (rounding). The principal total exceeds the carrying total of 1,985.426 because carrying amounts are net of unamortised fees and redemption option derivative assets and, for government contributions, discounted. Bucket years are measured from the September 30, 2026 balance sheet date; the table's own bucket definition is assumed to run from that date.
7. Cash flow gap, nine months 2026 (US$ thousand): operating cash flow 425,747 less additions to property, plant and equipment 1,210,017 less capitalised interest paid 45,943 equals negative 830,213 before acquisitions, financing and dividends. The company-defined free cash flow is negative 654.3 (US$m); the difference reflects the company's own definition (non-IFRS) and is not reconciled here.
8. Cash movement check: opening cash 869,356 less net decrease 472,528 equals closing 396,828, matching the cash flow statement.
9. Income statement checks: earnings from mine operations 253,317 less the expense block below it (exploration 17,116, standby 6,318, general and administrative 11,177, share-based payments 3,763, write-down 1,569, foreign exchange gain 4,029, acquisition costs 89, net 36,003) equals earnings from operations 217,314 for Q3 2026. For nine months 2026: 791,963 less 86,812 equals 705,151. Earnings from operations plus other income 5,613 less finance costs 13,531 equals pre-tax earnings 209,396 for Q3 2026; nine months 2026 705,151 plus 15,821 less 37,660 equals 683,312. All match the printed totals.
10. Effective tax rate on continuing operations, nine months 2026: 257,114 / 683,312 equals 37.6%. Nine months 2025: 54,604 / 324,573 equals 16.8%, which includes a deferred tax recovery of 89,390 (note 12). The two rates are not comparable without that item.

## Gaps

| ID | Gap | Effect | Treatment |
| --- | --- | --- | --- |
| G1 (from CP-0) | FY2025 full-year statements and Adjusted EBITDA not supplied | LTM EBITDA, LTM leverage and FY2025 interest cover are Not supplied | Shown as Not supplied; only matched nine-month and quarter bases are given |
| G2 (from CP-0) | Management discussion and the liquidity section it contains not supplied | Liquidity is assembled from statement notes only; undrawn amount of the euro 30.0 million VAT facility is not printed | Excluded from liquidity, stated in the table |
| G5 (from CP-0) | Issuer-reported covenant ratios and Term Facility covenant levels not printed | Covenant headroom is Not calculable; only the revolver levels (3.00x and 3.50x) are printed, with definitions not supplied | Not calculable: definition and reported figures missing. The computed leverage and cover are not covenant ratios |
| G6 (from CP-0) | Foran allocation is preliminary | Acquired debt, goodwill and property values may change within the measurement period | Carried as provisional |
| G11 | Cash interest definition is the analyst's (interest paid plus capitalised interest paid); the interest income and any interest accrued but unpaid are not considered | Cover could differ on other definitions | Both bases shown in Calculations |
| G12 | Revolver availability differs from limit less drawn by 0.3 (US$m) at September 30, 2026 and similar small amounts at other dates, with no explanation | Liquidity could differ by that amount | Printed availability used |
| G13 | The effect of the Skouries and McIlvenna Bay build-out cannot be separated from the operating mines beyond the release's own free cash flow excluding those projects (98.3 in Q3 2026, US$m) | Underlying cash generation of the operating mines is only a management-attributed figure | Not used in metrics |
| G14 | Only the Senior Notes fair value (491.9 million at September 30, 2026, observable prices in inactive markets) is printed; other debt is at amortised cost with fair value approximating carrying amount | No market-implied yield on the other instruments | Not calculable |
| G15 | Lease obligations of 24,595 undiscounted (commitments table) versus 14,203 recorded lease liabilities; other claims outside debt (asset retirement obligations 145,575 total, employee benefit obligations 14,514) are not in the debt figures | Total claims are wider than debt | Shown separately, excluded from debt |

## Next module

Proceed to CP-1A (business and transaction context) using this handoff and the CP-0 handoff. CP-1A should consume the Foran acquisition facts (April 14, 2026 completion, consideration and provisional allocation), the debt and Skouries and McIlvenna Bay capital and commissioning status, and carry gaps G1, G2, G5 and G6. CP-2 should treat the leverage and cover tables as matched-period bases only and keep LTM leverage and covenant headroom as Not supplied or Not calculable until the audited FY2025 statements and management discussion are provided.
