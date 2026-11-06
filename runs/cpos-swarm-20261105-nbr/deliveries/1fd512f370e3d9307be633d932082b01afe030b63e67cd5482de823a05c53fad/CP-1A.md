## Request

- Issuer: NABORS INDUSTRIES LTD (issuer id nbr, NYSE: NBR), the Bermuda holding company that files consolidated statements; Nabors Industries, Inc. ("Nabors Delaware") is the wholly owned borrower under the 2024 Credit Agreement.
- As-of date: 2026-11-05. Evidence cutoff: 2026-11-05. Events after September 30, 2026 are labelled as subsequent events and are not folded into Q3 2026 facts.
- Pathway: credit_snapshot, public case. Reporting currency: USD. Current period Q3 2026; prior period FY2025.
- Task for this module: the business and transaction fact pack a committee reads first, from a creditor perspective: transaction and ownership structure, business and operating model, credit-relevant history and change, issuer-level governance behaviour, credit translations, conflicts and the monitoring gaps. No peer ranking, instrument recommendation or recovery conclusion is given.
- Upstream handoffs used: CP-0 (source readiness) and CP-1 (financial base), both listed in Sources. Figures are quoted from the sources or from CP-1 on the same basis; no CP-1 figure is changed here. CP-1 gap H3 (guarantor lists and ranking), H5 (SANAD venture data), H6 (rig-purchase backstop) and H7 (release-only statements) are carried forward below.
- Category tags used on every fact row: Documentary Fact (the cited source states it), Management Language (management's characterisation, quoted and qualified), Analyst Interpretation (a reading of cited evidence) and Insufficient Information (evidence missing; the missing datapoint and its importance are stated).
- Settings file `context` is user input, not issuer evidence. It lists sector "Drilling Oil & Gas Wells" and country "United States" and leaves sponsor, parent, borrower, guarantors, ratings and deal terms blank; blanks are treated as not supplied, never as none or zero.
- No external material is used. A page locator is the source chunk shown as `page:N`, not a printed page.

## Sources

### Issuer sources relied on

| Cite as | Source name | sha256 | Use in this handoff |
| --- | --- | --- | --- |
| 10-K | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | 427cc2fc64bcd723a27a6c2478a12093e219dc045e02d41b40eab49061568751 | Business description, customers, risk factors, Parker and Quail Tools, related-party notes, share repurchase, exhibit index |
| 10-Q Q1 | 10-Q_2026-03-31_nbr-20260331x10q.htm.jsonl | 11eb9a5886137a3201a1d5b34cd6e8ef50e247d641cd61ec9c9814adc458e187 | Read for debt and covenant continuity; not otherwise cited |
| 10-Q Q2 | 10-Q_2026-06-30_nbr-20260630x10q.htm.jsonl | 6c2a6d1bdbcbd71ad95906094386639f0ffd409dc513dcadc487db645242cb3b | Read for debt continuity; not otherwise cited |
| 10-Q Q3 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | 7e240e48875d03a0d84a20d6f741fc0c9988f286076c7c4d265721b0e0793ce2 | Latest fleet, SANAD, Parker, Quail Tools, SPAC, equity issuance, segment results, concentration |
| ER Q1 | EX-99.1_2026-04-28_tm2612942d1_ex99-1.htm.jsonl | 811d6f2d82a109aad668cd621d65877dd4784a4f2a4d17ed4d8fd9b20e6f9b37 | SANAD newbuild schedule at Q1 2026 |
| ER Q2 | EX-99.1_2026-07-28_tm2621313d2_ex99-1.htm.jsonl | 4fe99e5d4274f6274ec08f0c05beac58f1ab8c742acabe22ed57e9e2bd36a4e7 | SANAD newbuild schedule at Q2 2026; backlog statement |
| ER Q3 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | f9d4d37c25f2acc92f4bf176ff35ad6539e2f40b8c58a320a92c16c59d447e59 | Q3 2026 operating highlights, SANAD schedule, rig suspensions, guidance (all management statements) |

### Context file

| Source name | sha256 | Role |
| --- | --- | --- |
| context | 2447d4a661e92334753a8e1c6e3f04df86843d3399afe1ed1f2ac26814412213 | Run settings only; not issuer evidence |

### Upstream handoffs

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 01371c96badec91a1c024971fd80be337cc1aa2bfcd663093f556e7185d90614 | Perimeter map, source relationships, gaps |
| CP-1 | 52018b6902eb6b45bb6e53a2bf745847730117a063b22f7e4d05d077344c3098 | Financial base: debt by instrument, liquidity, calculated metrics, definition review |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Nabors is a listed drilling contractor with no sponsor. Its credit depends on Saudi Aramco, 30% of FY2025 revenue and half-owner of the SANAD venture. Recent transactions reduced debt, and no debt-funded distribution is documented. | Medium | Beneficial ownership, contract backlog and venture-level financials are not in the pack, and management statements on rig suspensions and guidance are not filed evidence. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Saudi Aramco accounted for about 30% of FY2025 revenue and the three largest customers for 41%; Aramco contracts are per rig, mainly through SANAD. | Revenue visibility and cash conversion depend on one counterparty, so rig suspensions there hit earnings and receivables together. | High |
| The October release says SANAD suspended five rigs, after earlier 2026 reactivations; the filed quarterly report mentions suspension notices only in general terms. | Saudi activity can reverse quickly; treat the suspensions as management statements until a filing confirms them. | Medium |
| Parker was acquired for 4.8 million shares, and Quail Tools, acquired with Parker, was sold in August 2025. | Growth was added without new debt and a business was sold for cash, but FY2025 comparisons include earnings no longer owned. | Medium |
| Management-linked related-party arrangements exist: a profit-sharing venture, a SPAC sponsor entity and director-affiliated services. | Where quantified the amounts are small against earnings; unquantified items are leakage channels to monitor, and no creditor-adverse action is documented. | Medium |
| A change of control can accelerate debt and trigger a call option on Nabors' interest in SANAD. | Control events carry both refinancing and asset-loss risk, yet no controlling holder is identified in the pack. | Medium |

### Business and transaction view

On the filed evidence, Nabors Industries Ltd is an operating drilling contractor and not a sponsor-owned or recently recapitalised credit: no financial sponsor, controlling holder or dividend recapitalisation appears in the pack, and the transactions of the last two years are an equity-funded acquisition (Parker, closed March 11, 2025), a cash sale of the acquired Quail Tools business (August 20, 2025), a bond refinancing (November 10, 2025) and cash-funded note redemptions through Q3 2026. The business risk that matters most to a creditor is concentration: Saudi Aramco is both the largest customer, about 30% of FY2025 operating revenues, and the 50% partner in the consolidated SANAD joint venture, so revenue visibility, receivables, capital spending and a call option on Nabors' own interest all run through one relationship. The operating model is daywork contracting for rigs plus technology and equipment segments, with pricing set by dayrate and volume by rigs working; the filings do not quantify contract backlog or SANAD's own earnings, and the October release states a suspension of five SANAD rigs that the filed quarterly report does not. Governance behaviour is documented through related-party notes and the credit agreement's restricted payment terms rather than through any distribution or priming action; no behaviour in the Extraction-Oriented or Creditor-Adverse categories is evidenced, and ownership percentages cannot be stated because they sit in the proxy statement, which is not in the pack.

### Company and operating model

| Segment | Activities and revenue model | FY2025 operating revenues (US$ thousands) | Q3 2026 operating revenues (US$ thousands) | Q3 2026 adjusted EBITDA (US$ thousands) | Category | Source and locator |
| --- | --- | --- | --- | --- | --- | --- |
| U.S. Drilling | Land rigs in the Lower 48 and Alaska and offshore platform rigs in the Gulf of America; daywork contracts at a dayrate with lower rates for moves and interruptions; volume is average rigs working | 976,644 | 274,925 | 99,391 | Documentary Fact | 10-K page:6 and page:8; 10-K page:122; ER Q3 page:6 |
| International Drilling | Land and platform rigs mainly in the Middle East and Latin America (Saudi Arabia, Kuwait, Argentina, Colombia, Mexico); Saudi Aramco contracts are per rig and mainly run through SANAD | 1,597,765 | 458,544 | 145,718 | Documentary Fact | 10-K page:6 and page:9; 10-K page:122; ER Q3 page:6 |
| Drilling Solutions | Directional steering, performance software, tubular running and managed pressure drilling services, sold with Nabors rigs and to third parties; additive to rig charges; includes Quail Tools until August 20, 2025 | 513,283 | 116,065 | 43,913 | Documentary Fact | 10-K page:6, page:7 and page:8; 10-K page:122; ER Q3 page:6 |
| Rig Technologies | Canrig manufactures and sells top drives, catwalks, wrenches, drawworks and robotic systems, with aftermarket sales and service | 154,036 | 41,747 | 4,987 | Documentary Fact | 10-K page:7; 10-K page:122; ER Q3 page:6 |
| Other reconciling items | Elimination of inter-segment transactions and unallocated corporate costs | (57,035) | (19,087) | (48,466) | Documentary Fact | 10-K page:122; ER Q3 page:6 |
| Total | Four reportable segments; operations in approximately 20 countries | 3,184,693 | 872,194 | 245,543 | Documentary Fact | 10-K page:82; 10-Q Q3 page:3; ER Q3 page:7 |

### Company profile

| Item | Detail | Category | Source and locator |
| --- | --- | --- | --- |
| Registrant and domicile | Nabors Industries Ltd., formed as a Bermuda exempted company on December 11, 2001; principal executive offices in Hamilton, Bermuda; offices also in Houston, Anchorage, Dubai, Bogota, Dhahran and Sandnes. The settings file lists the country as United States; the filings give Bermuda as domicile and head office. Both are recorded, not reconciled | Documentary Fact | E1, E2 |
| Sector and listing | Drilling of oil and gas wells (sector from the settings file); common shares on the NYSE under NBR; warrants expired June 11, 2026 | Documentary Fact | 10-K page:55; 10-Q Q3 page:17 |
| Fleet | 240 actively marketed land rigs and 26 offshore platform rigs at September 30, 2026, against 242 and 27 at December 31, 2025 | Documentary Fact | E3, 10-K page:5 |
| Activity | Average total rigs working rose in Q3 2026 against Q3 2025; U.S. Drilling up 19% and International Drilling up 6% on average rigs working | Documentary Fact | ER Q3 page:1; 10-Q Q3 page:35 |
| Customers | Saudi Aramco about 30% of FY2025 operating revenues; three largest contract drilling customers about 41%; at September 30, 2026 about 41% of net receivables were in Saudi Arabia, 13% in the U.S. and 9% in Mexico | Documentary Fact | E4, E5, E6 |
| Employees | About 13,900 employees at December 31, 2025, about 9,800 outside the U.S. | Documentary Fact | 10-K page:9 |
| Ownership | Publicly traded; about 1,455 holders of record on February 6, 2026; 15,186,515 shares outstanding at October 30, 2026 excluding 1,161,283 held by subsidiaries. No sponsor, parent or controlling holder identified; beneficial ownership percentages are in the proxy statement, which is not in the pack | Insufficient Information | E7, 10-K page:55, 10-Q Q3 page:1 |
| Joint venture | SANAD, onshore drilling in Saudi Arabia, equally owned by Saudi Aramco and Nabors; consolidated because Nabors has the power to direct its most significant activities; Aramco's share is shown in noncontrolling and redeemable noncontrolling interest | Documentary Fact | E8, E9 |
| Borrower and holding structure | Nabors Delaware is the borrower under the 2024 Credit Agreement; Nabors Industries Ltd. is a holding company that relies on dividends and intercompany payments from subsidiaries | Documentary Fact | E10, 10-K page:136 |
| Auditor | PricewaterhouseCoopers LLP, auditor since 1987, with critical audit matters on drilling revenue recognition and Parker asset valuation | Documentary Fact | 10-K page:79 to page:81 |
| Ratings | The settings file supplies none; the 10-Q states that the major U.S. rating agencies have previously downgraded the senior unsecured rating to non-investment grade | Insufficient Information | 10-Q Q3 page:40 |

### Transaction summary and new debt issues

Parker Drilling Company was acquired on March 11, 2025 as a wholly owned subsidiary for consideration of 4.8 million Nabors common shares plus a small cash payment, valued at about 180.6 US$m at the closing share price; the status is closed and the accounting is the acquisition method, with a bargain purchase gain recorded because the share price fell between signing on October 14, 2024 and closing (10-Q Q3 page:9; E11). No debt was raised for the purchase, but Parker's 13% second lien term loan of 177.8 US$m, which carried a change of control repayment trigger, was repaid on March 25, 2025 using the 2024 Credit Agreement (10-K page:105); revolver borrowings of 398.0 US$m in 2025 were fully repaid in 2025 (10-K page:83) and the revolver was undrawn at December 31, 2025, so the acquisition added no permanent secured debt on the filed evidence. Quail Tools, part of the Parker acquisition, was sold to Superior Energy Services, Inc. on August 20, 2025; the 10-K gives net consideration as 625.0 US$m including a working capital adjustment, and the 10-Q gives it as 600.0 US$m plus working capital adjustments, with cash of 375.0 US$m and a seller note of 250.0 US$m in both; the seller note was prepaid in full on October 9, 2025 (E12, E13). That difference is logged as a conflict below and is not reconciled.

On new debt, Nabors issued 700.0 US$m of 7.625% senior priority guaranteed notes due November 2032 on November 10, 2025 and used the net proceeds to redeem all of its 7.375% senior priority guaranteed notes due May 2027, of which 546.1 US$m remained, for about 557.1 US$m in cash including a 10.1 US$m premium (10-K page:104 and page:59). Earlier issues still outstanding are the 1.75% senior exchangeable notes of 250.0 US$m (February 2023), the 9.125% notes, 650.0 US$m outstanding at December 31, 2025 (indenture dated November 20, 2023), and the 8.875% notes of 550.0 US$m (indenture dated July 22, 2024) (10-K page:103 to page:104 and page:135). No new debt was issued in 2026 through the cutoff: the 7.50% senior guaranteed notes due January 2028 were redeemed on January 15, 2026, and 100.0 US$m of the 9.125% notes was redeemed for about 104.9 US$m in cash in the third quarter, taking notes at face value to 2,050.0 US$m (10-K page:103; 10-Q Q3 page:15; CP-1). On April 7, 2026 a joinder increased the credit agreement's letter of credit tranche by 25.0 US$m, and on September 4, 2025 the first amendment let Nabors Delaware repurchase up to 100.0 US$m of equity a year, reducing dividend capacity dollar for dollar (10-Q Q3 page:16). The special purpose acquisition company NETC II, co-sponsored with an entity owned by members of management and directors, failed to complete its planned combination with e2Companies; after litigation, a settlement on October 14, 2025 gave NETC II a secured promissory note from e2 of 29.23 US$m, and 10.6 US$m of settlement income was recorded in Other, net in the nine months ended September 30, 2026 (10-Q Q3 page:30; 10-K page:113).

On August 26, 2026 Nabors issued about 0.4 million common shares for about 5.4 million Series B-1 preferred shares of Quaise Energy, Inc., a noncash exchange valued by reference to 35.0 US$m (10-Q Q3 page:17); this is an equity investment funded with shares, not cash or debt. As subsequent events after September 30, 2026 and before the cutoff, the October 27, 2026 release reports that SANAD deployed its 17th newbuild rig, that one more is scheduled for 2026 and two for the first quarter of 2027, that Nabors signed a multiyear contract to deploy one rig in Venezuela in early 2027, and that SANAD suspended five rigs (E14, E15, E16, E17). These are management statements in a furnished release; the filed 10-Q gives none of these counts. No sponsor, no dividend recapitalisation, no priming or uptier exchange and no debt-funded distribution appears in the pack. Nothing dated after the cutoff is used.

### Fact register

| ID | Area | Fact | Category | Evidence |
| --- | --- | --- | --- | --- |
| R1 | Company | Nabors describes itself as owning "one of the world's largest land-based drilling rig fleets"; the claim is promotional and unquantified | Management Language | E18 |
| R2 | Company | Drilling contracts are typically daywork contracts; term contracts run from six months to five years; customers may terminate single-well contracts on short notice and early termination payments may not fully compensate | Documentary Fact | E19, E20, E21 |
| R3 | Company | Saudi Aramco about 30% of FY2025 operating revenues and the three largest customers about 41%; Aramco contracts are per rig, primarily through SANAD | Documentary Fact | E4, E5, E22 |
| R4 | Operating model | Q3 2026 U.S. Drilling revenue rose on a 19% increase in average rigs working, partly offset by lower dayrates; International Drilling rose on 6% more rigs and improved pricing | Documentary Fact | E23, E24 |
| R5 | Operating model | International Drilling daily adjusted gross margin described by management as a record | Management Language | E25 |
| R6 | Operating model | Management states that leading-edge U.S. rig pricing has continued to increase, supporting wider daily margins | Management Language | E26 |
| R7 | Operating model | Management guides FY2026 consolidated capital spending including a SANAD newbuild program, and states that SANAD newbuild spending in Q3 2026 was below forecast as certain construction milestones shifted to later periods | Management Language | E27, E33 |
| R8 | Operating model | Contract backlog amount, share of term contracts, SANAD stand-alone revenue and earnings, and the split between maintenance and growth capital spending are not disclosed in the pack (status Not disclosed; measure null) | Insufficient Information | E28 |
| R9 | Operating model | The Q2 2026 release says Nabors "extended the duration of our contract backlog" in the Lower 48 without a figure | Management Language | E29 |
| R10 | Ownership | Change of control transactions could accelerate debt principal, require premium payments and trigger a call option to purchase Nabors' interest in SANAD | Documentary Fact | E30 |
| R11 | Ownership | Nabors consolidates SANAD as primary beneficiary; redeemable ownership interests accrue interest, have a twenty-five year maturity and convert to capital on events including accumulated losses | Documentary Fact | E9, 10-Q Q3 page:13 |
| R12 | Ownership | No financial sponsor, parent, controlling holder or dividend recapitalisation history is evidenced; beneficial ownership percentages are not in the pack | Insufficient Information | context; 10-K page:133 |
| R13 | Operating model | In 2024 a large number of Saudi rigs were suspended and the fleet had begun to rebound by the 10-K; during 2026 SANAD reactivated suspended rigs and the October release reports a new suspension of five rigs | Documentary Fact (2024 and 2026 reactivations); Management Language (five suspended rigs) | E31, E32 |
| R14 | Transaction | Parker, Quail Tools, NETC II, notes and Quaise: see the transaction summary above | Documentary Fact | E11 to E17 |

### Timeline

| Date | Event | Category | Evidence |
| --- | --- | --- | --- |
| December 11, 2001 | Nabors formed as a Bermuda exempted company | Documentary Fact | E1 |
| 2016 and 2017 | SANAD formed with Saudi Aramco and capitalised with contributions of about equal value from each owner | Documentary Fact | 10-Q Q3 page:12 and page:13 |
| October 14, 2024 | Parker merger agreement signed (closing price then 77.52 US$ against 37.50 US$ at closing) | Documentary Fact | 10-Q Q3 page:9 |
| March 11, 2025 | Parker acquisition completed; Parker term loan repaid March 25, 2025 | Documentary Fact | E11, 10-K page:105 |
| August 20, 2025 | Quail Tools sold to Superior Energy Services, Inc. | Documentary Fact | E12 |
| September 4, 2025 | First amendment to the 2024 Credit Agreement: equity repurchases up to 100.0 US$m per fiscal year | Documentary Fact | 10-Q Q3 page:16 |
| October 9, 2025 | Seller note of 250.0 US$m prepaid in full | Documentary Fact | E12 |
| October 14, 2025 | NETC II and e2 settlement; e2 issues a 29.23 US$m secured promissory note | Documentary Fact | 10-Q Q3 page:30 |
| November 10, 2025 | 7.625% notes due 2032 issued; 7.375% notes due 2027 redeemed | Documentary Fact | 10-K page:104 |
| January 15, 2026 | 7.50% notes due January 2028 redeemed | Documentary Fact | 10-K page:103 |
| April 7, 2026 | Letter of credit tranche increased by 25.0 US$m | Documentary Fact | 10-Q Q3 page:16 |
| August 26, 2026 | Quaise Energy preferred shares acquired for about 0.4 million common shares | Documentary Fact | 10-Q Q3 page:17 |
| Q3 2026 | 100.0 US$m of 9.125% notes redeemed in cash | Documentary Fact | 10-Q Q3 page:15 |
| Subsequent event, October 27, 2026 | Release: 17th SANAD newbuild rig deployed, five SANAD rigs suspended, Venezuela contract for early 2027 | Management Language | E14 to E17 |
| Subsequent event, November 4, 2026 | Q3 2026 Form 10-Q signed | Documentary Fact | 10-Q Q3 page:46 |

### Governance and sponsor behaviour

Assessed at issuer level and from documented actions only; no individual is assessed.

| Behaviour | Documented action | Category | Scoring dimension | Legal capacity, willingness and feasibility |
| --- | --- | --- | --- | --- |
| Supportive: deleveraging | Notes at face value reduced through cash redemptions in 2025 and 2026 (7.375% notes, 7.50% notes, part of the 9.125% notes), partly offset by the 2025 refinancing issue | Documentary Fact | Capital allocation | Capacity: no restriction cited. Willingness: demonstrated by the redemptions. Feasibility: paid from cash that fell between December 31, 2025 and September 30, 2026 (CP-1) |
| Neutral or Mixed: shareholder distributions | The 9M 2026 and FY2025 cash flow statements show no dividend to Nabors common shareholders and no open-market repurchase; a repurchase program of 400.0 US$m had 278.9 US$m remaining at December 31, 2025 and the same remaining amount is shown for each month of Q3 2026 with no program purchases; subsidiaries hold 1,161,283 shares | Documentary Fact | Capital allocation | Capacity: the credit agreement restricts dividends and permits equity repurchases up to 100.0 US$m a year, reducing dividends dollar for dollar. Willingness: none exercised in Q3 2026. Feasibility: liquidity is lower than at FY2025 (CP-1) |
| Neutral or Mixed: related-party arrangements | Hexegen LLC energy transition vehicle with an entity owned and managed by the Chairman and Chief Executive Officer, 90:10 profit split above a threshold; split-dollar life insurance with no premiums paid since the Sarbanes-Oxley Act; SPAC sponsor co-owned by management and directors with related parties buying warrants; services from a director's affiliated companies of 14.8 US$m in FY2025 | Documentary Fact | Related-party transactions | Capacity: the debt instruments do not contain covenants prohibiting restrictions on subsidiaries' upstream payments (10-K page:48); willingness: arrangements disclosed in notes; feasibility: amounts unquantified except the services cost. Related party revenue of about 1.1 billion US$ in FY2025 arises from rig leases, rig transportation and services with related parties including Saudi Aramco (10-K page:114; see conflict C3) |
| Neutral or Mixed: partner support | Nabors must backstop its share of SANAD's purchases of the first 25 rigs if the venture lacks cash or third-party financing | Documentary Fact | Contingent support | Capacity: contractual. Willingness: not tested. Feasibility: unquantified; the Q3 10-Q does not repeat it (CP-1 H6) |
| Transparent reporting | Quarterly filings give covenant ratios, SANAD balance sheet, receivables sold and concentration; the release gives reconciliations | Documentary Fact | Disclosure | Disclosure gaps: covenant EBITDA definition, guarantor lists, venture earnings |
| Extraction-Oriented or Creditor-Adverse | No dividend recapitalisation, debt-funded distribution, priming, uptiering, drop-down, non-pro-rata exchange or collateral release appears in the pack | Insufficient Information | Creditor protection | Absence of evidence in a minimum pack is not evidence of absence; indentures and credit agreement are not supplied (CP-0 G1) |

### Credit translations

**Revenue durability and concentration.** Evidence: Saudi Aramco about 30% of FY2025 operating revenues, the three largest customers about 41%, contracts per rig through SANAD (E4, E5, E22), and 2026 suspension and reactivation notices in the Middle East (E24, E32). Risk mechanic: per-rig contracts let a customer idle rigs without a contract termination, so a suspension reduces revenue, EBITDA and receivable inflows at once while SANAD's newbuild obligations and Nabors' backstop continue; 41% of receivables sit in Saudi Arabia. Credit implication: debt service capacity depends on one counterparty's rig program, so the monitoring posture should track SANAD rig count and receivables from Saudi Arabia each quarter; the Q3 2026 filed rig counts rose, but management reports five suspended rigs after quarter end. Countering logged item: conflict C3 (Aramco share versus related-party revenue) means the size of the concentration is not fully pinned down.

**Margin and cash-flow risk.** Evidence: daywork dayrate contracts, lower U.S. dayrates offset by volume, improving international pricing, and a management guide that includes a large SANAD newbuild program (E19, E23, E24, E27). Risk mechanic: margin depends on dayrate and rigs working, while SANAD capital spending is front-loaded and its timing has shifted to later periods. Credit implication: free cash flow after capital spending is sensitive to SANAD milestone timing, so the debt reduction already achieved came from cash balances rather than recurring surplus (CP-1).

**Ownership and sponsor alignment.** Evidence: no sponsor or controlling holder is identified; change of control may accelerate debt and trigger a call option on the SANAD interest (E30). Risk mechanic: a control event would hit funding and the asset base together. Credit implication: sponsor alignment cannot be assessed beyond documented actions; behaviour is Supportive on deleveraging and Neutral on related-party items, and the ownership gap is a monitoring item.

**Portfolio change.** Evidence: Parker acquired for shares and Quail Tools sold for cash within six months (E11, E12). Risk mechanic: FY2025 reported earnings include a business sold in August 2025 and a bargain purchase gain, so history overstates the continuing base. Credit implication: LTM figures from CP-1 are the cleaner base; the conflict on the sale price (C1) does not change the cash received of 375.0 US$m and the prepaid seller note of 250.0 US$m.

**Key uncertainties.** Backlog, SANAD earnings, guarantor structure and covenant definitions are not available (R8, CP-1 H2 and H3). Missing evidence is not an adverse conclusion.

### Conflicts logged, not reconciled

| ID | Conflict | Span one | Span two | Downstream effect |
| --- | --- | --- | --- | --- |
| C1 | Net consideration for the Quail Tools sale | 10-K page:59: Net consideration for the sale totals $625.0 million inclusive of a net working capital adjustment | 10-Q Q3 page:12: Net consideration for the sale totaled $600.0 million plus adjustments for net working capital | Sale size differs by 25.0 US$m between documents; cash 375.0 US$m and seller note 250.0 US$m are the same in both. The FY2025 cash flow statement shows proceeds from disposition of 622,856 thousand (10-K page:83); no document explains the 25.0 US$m |
| C2 | Exchangeable notes maturity label | 10-K page:135: 1.750% Senior Exchangeable Notes due 2027 (exhibit index) | 10-K page:103: 1.75% senior exchangeable notes due June 2029 (debt note) | Carried from CP-0 G7 and CP-1 H12; the debt note and quarterly tables control |
| C3 | Size of the Aramco relationship | 10-K page:9: Saudi Aramco accounted for approximately 30% of consolidated operating revenues | 10-K page:114: revenues from related parties totaled $1.1 billion for 2025 | The related-party figure is rounded and spans more than one party or relationship; the second measure on 3,184.7 US$m of revenue is about 34.5% (calculated). The pack does not name other related-party customers |
| C4 | Bargain purchase gain on Parker | 10-Q Q3 page:9: recorded a gain of $113.7 million | 10-Q Q3 page:3: income statement line gain on bargain purchase of 116,499 thousand for the nine months ended September 30, 2025 | Documented as a later adjustment of 2.8 US$m in the quarter ended December 31, 2025 (10-Q Q3 page:10); the nine-month 2025 comparative is not restated |
| C5 | Domicile | Settings file: country United States | 10-K page:54 and 10-Q Q3 page:1: principal executive offices in Hamilton, Bermuda | The legal entity is Bermudian; operations are headquartered administratively in Bermuda with major offices in Houston |

### Consumer assessments

| Consumer | Readiness | Take from this handoff | Why it matters | Gap | Required action |
| --- | --- | --- | --- | --- | --- |
| CP-2 (fundamental credit synthesis) | READY_WITH_LIMITATIONS | Customer concentration and SANAD mechanics, governance behaviour categories, portfolio change, conflicts C1 to C5 | Business risk drivers for the synthesis come from here; FY2025 history includes a divested business | Backlog, SANAD earnings, ownership percentages, guarantor structure | Carry gaps in its gaps ledger; do not state a recovery outcome or peer ranking |
| CP-5 (evidence trace validator) | READY_WITH_LIMITATIONS | Evidence register E1 to E33, category tags and conflicts | Management statements in the release must not be traced as filed facts | Release-only statements (five suspended rigs, guidance) | Treat Management Language rows as attributed; check C1 to C5 are carried as logged |

CP-1 is the upstream module that this handoff consumed, not a consumer; it is not assessed again.

### Monitoring gaps

| Item | Severity | Why it matters |
| --- | --- | --- |
| Debt schedule and maturity schedule: rebuilt from filings in CP-1, no call or put terms | Medium | Refinancing timing |
| Covenant certificate and collateral appraisal: only reported ratios | Medium | Headroom and collateral cover |
| Add-back bridge: the releases reconcile adjusted EBITDA to net income | Low | Available; definitions remain issuer-defined |
| SANAD stand-alone financials, backlog and rig-level contract terms | High | Concentration and cash access |
| Proxy statement (beneficial ownership, related-party detail, director independence) | Medium | Ownership and governance |
| Indentures and credit agreement | Medium | Guarantors, ranking, restricted payments |

### Evidence register

| Ref | Source | Locator | Quote |
| --- | --- | --- | --- |
| E1 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:5 | was formed as a Bermuda exempted company on December 11, 2001 |
| E2 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:54 | Nabors’ principal executive offices are located in Hamilton, Bermuda. |
| E3 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:6 | 240 actively marketed rigs for land-based drilling operations |
| E4 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:9 | One customer, Saudi Aramco, accounted for approximately 30%, 31% and 26% of our consolidated operating revenues |
| E5 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:21 | we received approximately 41%, 43% and 37%, respectively, of our consolidated operating revenues from our three largest contract drilling customers |
| E6 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:41 | approximately 41%, 13% and 9% of our net accounts receivable balance |
| E7 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:55 | there were approximately 1,455 shareholders of record of our common shares |
| E8 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:12 | SANAD is equally owned by Saudi Aramco and Nabors. |
| E9 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:7 | We have the power to direct activities that most significantly impact SANAD’s economic performance |
| E10 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:48 | We are a holding company with no significant assets other than the stock of our subsidiaries. |
| E11 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:59 | On March 11, 2025, Nabors completed its merger with Parker Drilling Company |
| E12 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:12 | On October 9, 2025, Nabors received prepayment in full of the $250.0 million seller note |
| E13 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:59 | Consideration comprised of cash of $375.0 million and a seller note of $250.0 million. |
| E14 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:2 | despite a lower SANAD rig count following the suspension of five rigs |
| E15 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:1 | The SANAD land drilling joint venture successfully deployed its 17th newbuild rig in Saudi Arabia. |
| E16 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:1 | One additional newbuild is scheduled for deployment in 2026 and two in the first quarter of 2027 |
| E17 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:1 | Nabors signed a multiyear contract to deploy one rig in Venezuela in early 2027. |
| E18 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:5 | Nabors owns and operates one of the world’s largest land-based drilling rig fleets |
| E19 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:8 | Our drilling contracts are typically daywork contracts. |
| E20 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:8 | Term contracts generally have durations ranging from six months to five years. |
| E21 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:8 | Such payments may not fully compensate us for the loss of a contract |
| E22 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:9 | Our contracts with Saudi Aramco are on a per rig basis. |
| E23 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:35 | which was partially offset by a decline in day rates |
| E24 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:33 | More recently, certain operators have taken measures to reduce near-term activity |
| E25 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:1 | International Drilling daily adjusted gross margin reached a record $19,060 |
| E26 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:33 | leading-edge rig pricing has continued to increase |
| E27 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:3 | We now expect full-year consolidated capital spending of $710 to $720 million |
| E28 | 10-Q_2026-09-30_nbr-20260930x10q.htm.jsonl | page:42 | Purchase commitments outstanding at September 30, 2026 totaled approximately $296.4 million |
| E29 | EX-99.1_2026-07-28_tm2621313d2_ex99-1.htm.jsonl | page:2 | extended the duration of our contract backlog |
| E30 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:47 | or trigger a call option to purchase our interest in SANAD |
| E31 | 10-K_2025-12-31_nbr-20251231x10k.htm.jsonl | page:58 | In Saudi Arabia specifically, the operating rig fleet has begun to rebound following the activity suspensions in 2024 of a large number of rigs. |
| E32 | EX-99.1_2026-04-28_tm2612942d1_ex99-1.htm.jsonl | page:1 | SANAD reactivated one previously suspended rig |
| E33 | EX-99.1_2026-10-27_tm2628332d1_ex99-1.htm.jsonl | page:2 | SANAD newbuild spending was below forecast as certain construction milestones shifted to later periods. |

## Calculations

| Item | Formula and inputs | Result |
| --- | --- | --- |
| FY2025 segment revenues tie to total | 976,644 + 1,597,765 + 513,283 + 154,036 - 57,035 (10-K page:122) | 3,184,693, equal to the income statement |
| Q3 2026 segment revenues tie to total | 274,925 + 458,544 + 116,065 + 41,747 - 19,087 (ER Q3 page:6) | 872,194, equal to the income statement |
| Q3 2026 segment adjusted EBITDA tie | 99,391 + 145,718 + 43,913 + 4,987 - 48,466 | 245,543, equal to reported |
| International Drilling share of FY2025 revenue | 1,597,765 / 3,184,693 | 50.2% |
| U.S. Drilling, Drilling Solutions, Rig Technologies shares of FY2025 revenue | 976,644 / 3,184,693; 513,283 / 3,184,693; 154,036 / 3,184,693 | 30.7%, 16.1%, 4.8% |
| International Drilling share of Q3 2026 revenue | 458,544 / 872,194 | 52.6% |
| Direct costs as a share of Q3 2026 revenue | 536,577 / 872,194 | 61.5% |
| Parker consideration | 4.8 million shares x 37.50 US$ = 180.0 US$m, plus cash 0.6 US$m | 180.6 US$m, equal to the stated 180,562 thousand |
| Parker net assets less consideration | 294,215 - 180,562 (10-Q Q3 page:10) | 113,653, equal to the gain recorded |
| Quail Tools consideration components | 375.0 + 250.0 | 625.0 US$m; the 10-Q states 600.0 US$m plus working capital adjustments (conflict C1) |
| Shares in aggregate versus outstanding | 16,347,798 - 15,186,515 | 1,161,283 held by subsidiaries, equal to the cover page |
| Related-party revenue as a share of FY2025 revenue (rounded numerator) | 1.1 billion / 3.184693 billion | about 34.5% |
| SANAD newbuild schedule at each release | Q1 release: 15 deployed + 4 scheduled for 2026 = 19; Q2 release: 16 deployed + 3 scheduled for 2026 = 19; Q3 release: 17 deployed + 1 scheduled for 2026 + 2 scheduled for Q1 2027 = 20 | The 2026 end-point moved from 19 to 18 and the total from 19 to 20 |
| Fleet change | Land 242 to 240; offshore 27 to 26 | A net decrease of 2 land and 1 offshore rig between December 31, 2025 and September 30, 2026 |

## Gaps

| ID | Gap | Why it matters | Action |
| --- | --- | --- | --- |
| J1 | Not supplied: beneficial ownership percentages, director independence and proxy related-party detail | Control and alignment cannot be assessed beyond documented actions | Add the 2026 proxy statement if needed |
| J2 | Not disclosed: contract backlog, term share, SANAD stand-alone revenue, EBITDA and cash needs | Concentration, cash access and capital spending visibility | Request venture-level data |
| J3 | Release-only statements (five suspended rigs, SANAD schedule, Venezuela contract, guidance) are not in a filing | Management Language, not filed fact | Confirm in the next filing |
| J4 | Executed Parker merger and Quail Tools sale agreements are not supplied; sale size differs between documents (C1) | Transaction terms and any post-closing obligations cannot be checked | Add the agreements if transaction review is required |
| J5 | Indentures and credit agreement not supplied; guarantor lists, ranking and restricted payment baskets rest on summaries | Behaviour categories on priming and distributions cannot be tested against documents | Carry CP-0 G1 and CP-1 H3 |
| J6 | The rig-purchase backstop for SANAD is in the 10-K but was not found in the Q3 10-Q | Contingent funding after the first 25 rigs is unquantified | Confirm in a later filing |
| J7 | No ratings or market quotes in the settings file | Market access cannot be assessed | Not supplied in context |
| J8 | The settings file country (United States) differs from the filings' domicile (Bermuda) | Identity metadata | Record both; the filings control |

## Next module

CP-2 follows, to synthesise the fundamental credit view from CP-1 and this handoff. It should take from here the Saudi Aramco and SANAD concentration with its suspension and reactivation history, the equity-funded Parker acquisition and cash Quail Tools sale, the governance behaviour categories (Supportive on deleveraging, Neutral or Mixed on related-party items and capital returns, no Extraction-Oriented or Creditor-Adverse action evidenced), and conflicts C1 to C5. It must carry gaps J1 to J8 and CP-1 H2, H3, H5 and H7, state no recovery outcome and no peer ranking, and mark the management statements in the October release as attributed. CP-5 then checks that every Management Language row stays attributed and that each conflict is logged, not reconciled.
