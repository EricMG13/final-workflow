## Request

Financial statement extraction, definition review and credit-metric read (CP-1) for Caesars Entertainment, Inc. (CZR), as of 2026-11-05, pathway credit_snapshot, reporting currency USD, USD millions unless stated. Current period Q3 2026 (quarter and nine months ended September 30, 2026; balance sheet at September 30, 2026); prior period FY2025 (year and balance sheet at December 31, 2025). Cutoff 2026-11-05; the latest evidence used is the Q3 10-Q signed October 27, 2026 and the Q3 earnings release dated October 27, 2026. No outside knowledge is used. Entity perimeter throughout: Caesars Entertainment, Inc. and its consolidated subsidiaries as presented in the filed statements, including noncontrolling interests. The run context carries no borrower, parent, guarantor, rating, quote or market input; those are Not supplied.

## Sources

### Issuer sources relied on

| Source (exact name) | sha256 | Used for |
|---|---|---|
| 10-K_2025-12-31_czr-20251231.htm.jsonl | bc64a6b58a2e5481a0cfade7eea5b0ab2abc3801003c4d6cb677785a5aa59468 | FY2025 and FY2024 statements (pages 99-102), Adjusted EBITDA reconciliation (pages 77-78), market risk table (page 95), debt note (pages 122-123), financing obligation note (pages 117-118), liquidity (page 80) |
| 10-Q_2026-09-30_czr-20260930.htm.jsonl | 020dbbd4c466f93db126b9e9ea0f09672470d3e5caa33fd667f739807400c48f | Q3 and nine-month 2026 statements (pages 2-5), debt note (pages 15-21), merger (pages 7-9, 38), MD&A (pages 41-54) |
| 10-Q_2026-06-30_czr-20260630.htm.jsonl | c1584ea1247740f06c0dd4b0a8964b1753f8cc5c74266698804a67fd5a8dafb5 | Not relied on for figures in this module (CP-0 indexed it) |
| 10-Q_2026-03-31_czr-20260331.htm.jsonl | 5678521031e1645ef46bac311c4cabf43977488c6d11dfa25cc00a4f23b2d8a8 | Q1 2026 net loss attributable and total net loss labels (page 3) |
| EX-99.1_2026-10-27_ex991-2026q3ceiearningsrel.htm.jsonl | 72e92043d95db7701dbaee10509a03094dd97f5a7811f25a956ad12661393bcd | Q3 2026 segment results, net debt and liquidity (pages 1-2), reconciliation (page 6) |
| EX-99.1_2026-07-28_ex991-2026q2ceiearningsrel.htm.jsonl | 89cd5ad8c7a0d45cdf4a8f6462fc3964a9e7d04aae46811b1f50bebeb80c1762 | Q2 2026 net debt and liquidity (page 2) |
| EX-99.1_2026-04-28_ex991-2026q1ceiearningsrel.htm.jsonl | 7471385a5ad76519a93a6fc4a1f0048a88c7bfb7676d6a0b6e78c8e1a9e19c13 | Q1 2026 results, net debt and liquidity (pages 1-2) |

### Run context (not issuer evidence)

| Source | sha256 |
|---|---|
| context (czr.json) | 0172f1f774353a9014a5593b1df2824463fdefe668659f701d2701a1f5a162de |

### Handoffs supplied

| Module | sha256 |
|---|---|
| CP-0 | 68c2aa991decb0a068a7686c52c5f7ef75f0c9f53a26c05730a18c0d745ad39e |

The CP-0 handoff rated CP-1 READY_WITH_LIMITATIONS. Its limitations are carried: pending merger, no executed debt or lease documents, release-versus-filing label care, text-only extraction.

## Findings

### Reported basis and what the statements show

Caesars reports FY2025 net revenues of $11,486 million, an operating income of $1,858 million, interest expense, net of $2,304 million and a net loss attributable to Caesars of $(502) million (10-K page 99). Adjusted EBITDA was $3,624 million for FY2025 against $3,739 million before pre-disposition adjustment ($3,723 million after) for FY2024 (10-K page 78). The business earns positive operating income and a positive Adjusted EBITDA but reports net losses because interest expense, net, which includes the expense on the VICI and GLPI lease financing obligations, exceeds operating income in every period shown for FY2025, FY2024, nine months 2026 and nine months 2025.

In Q3 2026 net revenues were $2,940 million against $2,869 million (up 2.5%), while Adjusted EBITDA fell to $865 million from $884 million, a 2.1% decline, and the reported Adjusted EBITDA margin fell to 29.4% from 30.8% (10-Q Q3 page 41). Segment drivers named by the filing: Las Vegas Adjusted EBITDA $343 million versus $379 million on "fewer city-wide convention events and lower leisure customer visitation"; Regional $524 million versus $506 million, helped by the consolidation of Caesars Windsor from March 3, 2026; Caesars Digital $44 million versus $28 million; Corporate and Other $(63) million versus $(47) million on higher insurance captive costs (10-Q Q3 pages 41-48).

Debt fell over the nine months: total outstanding indebtedness $11,659 million at September 30, 2026 versus $11,905 million at December 31, 2025; net debt $10,795 million versus $11,018 million (Q3 release page 2). Cash and cash equivalents were $864 million; total liquidity including revolver capacity was $2,947 million. The Q3 10-Q states that "the Company was in compliance with all of the applicable financial covenants described above" (Note 6).

### Financials and credit metrics

| Item (USD millions unless stated) | FY2024 | FY2025 | 9M 2025 | 9M 2026 | Q3 2025 | Q3 2026 | LTM Q3 2026 (calculated) | Source locators |
|---|---|---|---|---|---|---|---|---|
| Net revenues | 11,245 | 11,486 | 8,570 | 8,803 | 2,869 | 2,940 | 11,719 | 10-K p99; 10-Q Q3 p2-3; LTM see Calculations |
| Operating income | 2,304 | 1,858 | 1,527 | 1,470 | 513 | 457 | Not calculated | 10-K p99; 10-Q Q3 p3 |
| Depreciation and amortization | 1,324 | 1,417 | 1,073 | 1,068 | 352 | 366 | Not calculated | 10-K p99; 10-Q Q3 p2-3 |
| Adjusted EBITDA (company definition, before lease financing rent) | 3,739 (3,723 after pre-disposition EBITDA, net) | 3,624 | 2,723 | 2,672 | 884 | 865 | 3,573 | 10-K p78; Q3 release p6; 10-Q Q3 p50 |
| Adjusted EBITDA margin (reported, quarter and YTD) | Not supplied | 31.6% (calculated 3,624 / 11,486) | 31.8% | 30.4% | 30.8% | 29.4% | 30.5% (calculated) | 10-Q Q3 p41; Calculations |
| Interest expense, net (includes lease financing obligation interest) | 2,366 | 2,304 | 1,729 | 1,712 | 576 | 570 | 2,287 | 10-K p99; 10-Q Q3 p3 |
| Net loss attributable to Caesars | (278) | (502) | (252) | (283) | (55) | (123) | Not calculated | 10-K p99; 10-Q Q3 p3 |
| Net cash provided by operating activities | 1,075 | 1,302 | 998 | 942 | Not supplied (YTD only) | Not supplied (YTD only) | 1,246 | 10-K p101; 10-Q Q3 p4 |
| Purchase of property and equipment (capex) | 1,296 | 805 | 648 | 507 | Not supplied (YTD only) | Not supplied (YTD only) | 664 | 10-K p101; 10-Q Q3 p4 |
| Free cash flow after capex (CFO less purchase of property and equipment) | Not calculated | 497 | 350 | 435 | Not supplied | Not supplied | 582 | Calculations |
| Cash interest paid for debt | 1,052 | 813 | 652 | 580 | Not supplied | Not supplied | 741 | 10-K p101; 10-Q Q3 p5 |
| Cash interest paid for rent on GLPI and VICI leases | 1,324 | 1,349 | 1,009 | 1,030 | Not supplied | Not supplied | 1,370 | 10-K p101, p117; 10-Q Q3 p5 |
| Income taxes paid, net | 48 | 81 | 61 | 14 | Not supplied | Not supplied | 34 | 10-K p101; 10-Q Q3 p5 |
| Distributions to noncontrolling interest owners | 16 | 102 | 76 | 65 | Not supplied | Not supplied | 91 | 10-K p101; 10-Q Q3 p5 |
| Cash and cash equivalents (balance, period end) | 866 | 887 | 836 | 864 | Not supplied | 864 | 864 at September 30, 2026 | 10-K p99; 10-Q Q3 p2, p5 |
| Restricted cash (current, period end) | 95 | 85 | 87 | 94 | Not supplied | 94 | 94 at September 30, 2026 | 10-K p99; 10-Q Q3 p2, p5 |
| Total debt, face value (aggregate principal) | Not supplied | 11,905 | Not supplied | 11,659 | Not supplied | 11,659 | 11,659 at September 30, 2026 | 10-K p122; 10-Q Q3 p16 |
| Total debt, book value | 12,154 | 11,792 | Not supplied | 11,563 | Not supplied | 11,563 | 11,563 at September 30, 2026 | 10-K p122; 10-Q Q3 p16 |
| Net debt (company: total outstanding indebtedness less cash and cash equivalents) | Not supplied | 11,018 | Not supplied | 10,795 | Not supplied | 10,795 | 10,795 at September 30, 2026 | Q3 release p2 |
| Long-term financing obligations (VICI and GLPI failed sale-leasebacks, balance sheet) | 12,899 | 13,096 | Not supplied | 13,188 | Not supplied | 13,188 | 13,188 at September 30, 2026 | 10-K p99; 10-Q Q3 p2 |
| Total stockholders' equity | 4,376 | 3,686 | 3,975 (September 30, 2025) | 3,446 | Not supplied | 3,446 | 3,446 at September 30, 2026 | 10-K p99; 10-Q Q3 p3-4 |
| Total available liquidity (cash plus net revolver capacity) | Not supplied | 2,833 | Not supplied | 2,947 | Not supplied | 2,947 | 2,947 at September 30, 2026 | 10-K p80; Q3 release p2 |
| Total debt (face) to LTM Adjusted EBITDA (x, calculated) | Not calculated | 3.29x (on FY2025) | Not calculated | Not calculated | Not calculated | Not calculated | 3.26x | Calculations |
| Net debt to LTM Adjusted EBITDA (x, calculated) | Not calculated | 3.04x (on FY2025) | Not calculated | Not calculated | Not calculated | Not calculated | 3.02x | Calculations |
| Adjusted EBITDA to interest expense, net (x, calculated; interest includes lease financing interest) | Not calculated | 1.57x | Not calculated | Not calculated | Not calculated | Not calculated | 1.56x | Calculations |
| Adjusted EBITDA to cash interest paid for debt (x, calculated) | Not calculated | 4.46x | Not calculated | Not calculated | Not calculated | Not calculated | 4.82x | Calculations |
| Adjusted EBITDA less cash rent on GLPI and VICI leases (calculated) | Not calculated | 2,275 | Not calculated | Not calculated | Not calculated | Not calculated | 2,203 | Calculations |
| Total debt (face) to Adjusted EBITDA less cash rent (x, calculated) | Not calculated | 5.23x | Not calculated | Not calculated | Not calculated | Not calculated | 5.29x | Calculations |
| Net debt to Adjusted EBITDA less cash rent (x, calculated) | Not calculated | 4.84x | Not calculated | Not calculated | Not calculated | Not calculated | 4.90x | Calculations |
| Adjusted EBITDA to (cash interest on debt plus cash rent) (x, calculated) | Not calculated | 1.68x | Not calculated | Not calculated | Not calculated | Not calculated | 1.69x | Calculations |

### Debt structure and maturities (facility level, September 30, 2026)

From the Q3 10-Q Note 6 (pages 15-16), face value in USD millions: CEI Revolving Credit Facility, maturing 2028, $2,250 million commitment, $0 drawn; CEI Term Loan A, 2028, variable, 609; CVA Revolving Credit Facility, 2029, $25 million commitment, $0 drawn; CVA Delayed Draw Term Loan, 2029, variable, 371; CEI Term Loan B, 2030, variable, 2,012; CEI Term Loan B-1, 2031, variable, 2,828; CEI Senior Secured Notes due 2030, 7.00%, 2,000; CEI Senior Secured Notes due 2032, 6.50%, 1,500; CEI Senior Notes due 2029 (unsecured), 4.625%, 1,200; CEI Senior Notes due 2032 (unsecured), 6.00%, 1,100; Special Improvement District Bonds, 2037, 4.30%, 38; long-term notes and other payables 1. Total face is 11,659 and total book value is 11,563. The facility-level detail agrees to the company's "Annual maturities of long-term debt" total of 11,659.

Scheduled principal: remaining 2026, 28; 2027, 114; 2028, 646; 2029, 1,574; 2030, 3,962; thereafter, 5,335. The two secured term loans and the secured notes fall in 2030 and 2031 to 2032; the CEI Revolving Credit Facility and CEI Term Loan A mature on January 31, 2028. Estimated interest payments over the same periods total 3,120 (10-Q Q3 page 16). Variable-rate borrowings were $5.8 billion, "approximately 50% of consolidated long-term debt", with weighted average rates of 6.12% variable and 6.18% fixed (page 54). The 10-K sensitivity at December 31, 2025 was about $61 million of annual interest per 100 basis points of Term SOFR (10-K page 95).

Covenants as disclosed: the CEI Revolving Credit Facility and CEI Term Loan A carry a maximum net total leverage ratio of 6.50:1 and a minimum fixed charge coverage ratio of 2.0:1; after Term Loan A repayment the revolver covenants are tested "solely to the extent that certain testing conditions are satisfied"; the Caesars Virginia facilities carry a maximum net total leverage ratio of 4:1 and a minimum fixed charge coverage ratio of 1.05:1 on the operations of Caesars Virginia, with no CEI guarantee; the company states compliance at September 30, 2026 (10-Q Q3 pages 20-21). The GLPI Leases require "a minimum adjusted revenue to rent ratio of 1.20:1" (10-K page 118). Covenant headroom is not calculable: covenant EBITDA, fixed charge and net total leverage definitions are not in the supplied sources.

### Definition risks and interpretation

1. Adjusted EBITDA is before lease financing rent. The company defines it so that it "excludes the expense associated with certain of our leases as these transactions were accounted for as financing obligations and the associated expense is included in interest expense." Cash paid on those leases was $1,030 million in the nine months of 2026 and $1,349 million in FY2025. Debt-to-EBITDA ratios on the company definition therefore do not capture the rent burden that sits ahead of equity and unsecured creditors; the rent-adjusted ratios in the table are separate, labelled calculations and are not company or covenant measures.
2. Interest expense, net mixes cash and non-cash items: it includes lease financing interest that for early lease years exceeds cash paid, which the 10-K says increases the failed-sale-leaseback obligation, and it includes amortization of deferred financing costs (135 in the nine months of 2026). Cash interest paid for debt is the cleaner debt-service measure.
3. Net debt is the company's definition and excludes restricted cash of $113 million (Q3 release) and the long-term financing obligations of $13,188 million.
4. LTM and Q4 2025 are derived, not reported. The company does not print a discrete Q4 2025 or LTM figure in the supplied sources.
5. Comparability: Caesars Windsor consolidation from March 3, 2026 moved its results from Managed and Branded to Regional, and Grand Bazaar was acquired on May 1, 2026; neither prior-year period was restated in the pages read.
6. Label hazard at Q1 2026: the release headline "GAAP net loss of $98 million" is the figure the 10-Q prints as "Net loss attributable to Caesars $ (98)", while total net loss including noncontrolling interests was $(83) million. This module uses the attributable label.
7. Released figures were checked against filings where both exist for the same period: Q3 and nine-month revenue, Adjusted EBITDA, interest expense, net loss attributable and the Adjusted EBITDA reconciliation agree between the Q3 release and the Q3 10-Q; FY2025 Adjusted EBITDA of 3,624 appears in the 10-K only.

### Latest-quarter changes

Compared with Q3 2025, revenue grew and Adjusted EBITDA contracted, so margin compressed by 1.4 percentage points on reported figures; net loss attributable widened to $(123) million from $(55) million. Sequentially, the releases show net revenues of 2,870 (Q1), 2,993 (Q2) and 2,940 (Q3), and Adjusted EBITDA of 887, 920 and 865. Net debt moved from 11,050 at March 31, 2026 to 10,842 at June 30, 2026 and 10,795 at September 30, 2026; cash rose to 965 at June 30 and returned to 864. Nine-month operating cash flow was lower than the prior year (942 versus 998) and capital spending lower (507 versus 648), with $98 million of cash paid for asset acquisitions and no share repurchases in 2026 against $179 million in the nine months of 2025. The Q3 10-Q records transaction costs for the pending merger of $12 million in Q3 and $22 million in the nine months. The merger itself is a CP-5 matter.

## Calculations

All inputs are USD millions from the cited locators; results are rounded to the stated precision. These are derived figures, not reported by the company.

- Implied Q4 2025 net revenues = FY2025 11,486 (10-K p99) less 9M 2025 8,570 (10-Q Q3 p3) = 2,916.
- Implied Q4 2025 Adjusted EBITDA = FY2025 3,624 (10-K p78) less 9M 2025 2,723 (Q3 release p6) = 901.
- LTM net revenues to September 30, 2026 = Q4 2025 2,916 + 9M 2026 8,803 = 11,719.
- LTM Adjusted EBITDA = 901 + 2,672 = 3,573. LTM margin = 3,573 / 11,719 = 30.49%, shown as 30.5%. FY2025 margin = 3,624 / 11,486 = 31.55%, shown as 31.6%.
- LTM interest expense, net = FY2025 2,304 less 9M 2025 1,729 plus 9M 2026 1,712 = 2,287.
- LTM cash interest paid for debt = 813 - 652 + 580 = 741.
- LTM cash interest paid for rent on GLPI and VICI leases = 1,349 - 1,009 + 1,030 = 1,370. The 10-K line is labelled "Cash interest paid for rent related to financing obligations" and equals the sum of the VICI (1,236) and GLPI (113) cash interest in the lease note (10-K p117), so it is treated as comparable to the 10-Q line "GLPI and VICI Leases"; the 10-Q separately reports 7 for the nine months of 2026 and 6 for 2025 of "other financing obligations", which are excluded here.
- LTM income taxes paid = 81 - 61 + 14 = 34. LTM distributions to noncontrolling interests = 102 - 76 + 65 = 91.
- LTM net cash provided by operating activities = 1,302 - 998 + 942 = 1,246. LTM purchase of property and equipment = 805 - 648 + 507 = 664. LTM free cash flow after capex = 1,246 - 664 = 582. After LTM noncontrolling distributions of 91 the figure is 491. FY2025 = 1,302 - 805 = 497; 9M 2025 = 998 - 648 = 350; 9M 2026 = 942 - 507 = 435. These exclude acquisition of intangible assets and cash paid for asset acquisitions.
- Total debt (face) / LTM Adjusted EBITDA = 11,659 / 3,573 = 3.263x. Net debt / LTM Adjusted EBITDA = 10,795 / 3,573 = 3.021x. FY2025: 11,905 / 3,624 = 3.285x; 11,018 / 3,624 = 3.040x.
- Adjusted EBITDA / interest expense, net: LTM 3,573 / 2,287 = 1.562x; FY2025 3,624 / 2,304 = 1.573x.
- Adjusted EBITDA / cash interest paid for debt: LTM 3,573 / 741 = 4.822x; FY2025 3,624 / 813 = 4.458x.
- Adjusted EBITDA less cash rent: LTM 3,573 - 1,370 = 2,203; FY2025 3,624 - 1,349 = 2,275.
- Total debt / (Adjusted EBITDA less cash rent): LTM 11,659 / 2,203 = 5.292x; FY2025 11,905 / 2,275 = 5.233x. Net debt: LTM 10,795 / 2,203 = 4.900x; FY2025 11,018 / 2,275 = 4.843x.
- Adjusted EBITDA / (cash interest on debt + cash rent): LTM 3,573 / (741 + 1,370 = 2,111) = 1.693x; FY2025 3,624 / (813 + 1,349 = 2,162) = 1.676x.
- Change in total debt, face, since December 31, 2025 = 11,659 - 11,905 = -246; change in net debt = 10,795 - 11,018 = -223; change in cash = 864 - 887 = -23.
- Checks: maturity ladder 28 + 114 + 646 + 1,574 + 3,962 + 5,335 = 11,659 agrees to total face value. Liquidity 864 + 2,250 + 25 - 96 - 40 - 56 = 2,947 agrees to the release. Quarterly revenues 2,870 + 2,993 + 2,940 = 8,803 and Adjusted EBITDA 887 + 920 + 865 = 2,672 agree to the nine-month figures.
- Covenant headroom: Not calculable. The net total leverage and fixed charge coverage covenant definitions are not supplied, and the ratios above use the company's Adjusted EBITDA, not covenant EBITDA.

## Gaps

- Covenant EBITDA, net total leverage and fixed charge coverage definitions, baskets and test mechanics: Not supplied (credit agreement and indentures absent). Action: supply executed documents before any headroom statement.
- VICI and GLPI lease terms beyond the 10-K note summaries: Not supplied. The 10-K future-payment schedule (pages 117-118) was read only in part; it shows 2026 minimum payments of 115 (GLPI) and 1,254 (VICI) at December 31, 2025. Action: confirm in CP-2.
- Discrete Q3 2026 and Q3 2025 operating cash flow, capex, cash interest and taxes: Not supplied; the filings give year-to-date only. Quarter-level free cash flow is Not calculable.
- Balance sheet at September 30, 2025 and at December 31, 2024 for debt face value: Not supplied in the sources read; the equity figure at September 30, 2025 comes from the Q3 10-Q equity statement.
- Treatment of existing debt on completion of the pending merger (change of control, refinancing): Not supplied in the sources read. Carried to CP-2 and CP-5.
- No management guidance is quantified in the releases read. The Q1 release quotes the CFO expecting "strong free cash flow in 2026 as a result of continued operating momentum, lower cash interest expense, and lower capex" without a figure; it is a management claim and is not used in any calculation. This refines the CP-0 note that no guidance section was found.
- Prior-period segment restatement for the Caesars Windsor reclassification: not determined.
- Q2 2026 10-Q figures were not extracted in this module; Q2 release liquidity and net debt are quoted only for the sequential trend.
- Extraction fidelity: all figures were read from text conversions; no image or chart was inspected.

## Next module

CP-1A should take the table, the labelled calculations and the definition risks above. The critical caveats to carry are that Adjusted EBITDA excludes lease financing rent, that LTM and Q4 2025 are derived, that covenant headroom is not calculable, and that the merger treatment of debt is unresolved. CP-2 should read the facility table, maturity ladder and the lease financing obligation note.
