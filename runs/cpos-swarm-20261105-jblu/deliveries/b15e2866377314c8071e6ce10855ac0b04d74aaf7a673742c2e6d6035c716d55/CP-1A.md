# CP-1A — Business and transaction context: JETBLUE AIRWAYS CORP (jblu)

## Request

- Issuer: JETBLUE AIRWAYS CORP (registrant "JETBLUE AIRWAYS CORPORATION", ticker JBLU). As-of date 2026-11-05; information cutoff 2026-11-05.
- Pathway `credit_snapshot`, reporting currency USD, current period Q3 2026, prior period FY2025 (context). Amounts are US$ millions unless stated.
- Reader question: which transaction, business, ownership and operating facts matter most to the creditor, with the chain evidence, risk mechanic, credit implication. Decision drivers: transaction and ownership structure; business and operating model; credit-relevant history or change.
- Scope limits: no peer ranking, no instrument recommendation, no recovery conclusion. Sector and country labels come from the run context, which is not issuer evidence; every other fact is cited to a pinned filing. Fact categories used: Documentary Fact, Management Language, Analyst Interpretation, Insufficient Information.

## Sources

Hashes are the sha256 of the pinned text extractions named by CP-OS. A locator `page:N` is the extraction chunk number, not the printed page.

| Source | sha256 | Use in this handoff |
| --- | --- | --- |
| 10-K_2025-12-31_jblu-20251231.htm.jsonl | 5eaf617accf854e4d3e9a550a2ff2955ebfa71253742ee07dd6faac0b2e32a8c | Business description, network, loyalty, labor, history, financings, Spirit termination, equity matters |
| 10-Q_2026-03-31_jblu-20260331.htm.jsonl | 23aa04d969e5d0170c0af37c935f385dfb36e65e5eefd81c73b6d9abfad792fa | Not relied on for any fact below |
| 10-Q_2026-06-30_jblu-20260630.htm.jsonl | 909f0d616195258039c6cade15d6ec9c2498b992386b681904fa4366c00d0fca | Not relied on for any fact below |
| 10-Q_2026-09-30_jblu-20260930.htm.jsonl | acf402823b4f024901754bb305241f6c703d6a3c7b62a75b67703d555b0a8e99 | Latest operating, fleet, labor, litigation, financing and subsequent-event facts |
| EX-99.1_2026-04-28_ex991-earningsreleaseq12026.htm.jsonl | d4d4219d15ba6a638e2373e8ae55aa1c8d909855e1454637cd8095dcf728854e | Not relied on for any fact below |
| EX-99.1_2026-07-28_ex991-earningsreleaseq22026.htm.jsonl | 802f55be8bbdb2947fd6f1ea1be406ca4f8ca6aa8c3d778ecad7cf301e68ccf6 | Management 2028 earnings-per-share target (attributed as Management Language) |
| EX-99.1_2026-10-26_ex991-earningsreleaseq32026.htm.jsonl | 698b07a0502ae526f90cdcc0cd39f907723cfed08c5317bc057549e3a8aec7de | Management outlook, operating statistics, BlueFirst start date (attributed as Management Language) |
| context | 31c25d56081dda135cad8e796a84043b049461aaa2d0b6432dd4792f868c14f8 | Sector, country and run settings; not issuer evidence. Sponsor, parent and guarantor fields are blank |

| Supplied handoff | sha256 |
| --- | --- |
| CP-0 | 5f1fd6d78bb06a0ae2ac09089d15d4162bd31f1324bf5098e03d0142b1a1dcc0 |
| CP-1 | 58c5892d83fe67883e53348fce2c2bb7681059206834d241a6a44bac68076eb9 |

CP-1 figures are referenced here as "CP-1" and are not restated or corrected. CP-1 uses computed EBITDA and carrying-value debt; this handoff keeps those bases.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| JetBlue is a point-to-point East Coast airline with no sponsor or controlling holder identified and no pending merger; the credit story is fuel-exposed operations funded by asset-backed debt, with the TrueBlue loyalty financing the key structural feature. | Medium | Ownership detail sits in an unsupplied proxy statement and debt agreements are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| No controlling holder or sponsor is identified; the Spirit merger was terminated in March 2024 and no acquisition is pending. | No sponsor extraction or deal-funding risk is evident, but ownership detail is incomplete. | Medium |
| Costs are concentrated in fuel and labor; fuel is unhedged and the pilot contract has been amendable since February 2025. | Fuel and wage shocks hit margins directly and cash conversion depends on liquidity. | High |
| The loyalty program is pledged as first-lien collateral for the TrueBlue notes and term loan. | A key cash-generating asset is committed to secured lenders, which matters for unsecured claims. | Medium |
| New 2026 secured financing is aircraft-backed, with a further increment expected in the fourth quarter of 2026. | Asset-backed funding continues, while use of proceeds is not stated in detail. | Medium |

### Business and transaction view

JetBlue is a Delaware-incorporated, publicly listed US airline with one reportable segment, a point-to-point network centered on the Northeast corridor, six focus cities, and a loyalty program and co-brand card relationship that sit inside the TrueBlue secured financing. No sponsor, controlling holder or parent is identified in the supplied sources, and the context sponsor field is blank. There is no pending merger or acquisition: the merger agreement with Spirit Airlines was terminated on March 1, 2024, and the only 2026 acquisition is a set of 22 LaGuardia slots for a stated aggregate price, completed in October 2026 after the quarter end. The transaction relevant to creditors is financing, not ownership change: secured aircraft financing in April 2026 (fully drawn at September 30, 2026, with a further increment expected in the fourth quarter of 2026) and the earlier 2024 TrueBlue, equipment note and convertible issues. Operating risk is driven by fuel with no hedges, labor cost with open pilot and inflight negotiations, Northeast air traffic and weather disruption, and engine availability. Management language on a return to profitability in 2027 and an earnings target for 2028 is forward-looking and is recorded as Management Language, not as fact. Limits: ownership detail and the debt agreements are not supplied, and use of proceeds for the 2026 financing is not stated.

### Company and operating model

| Area | Fact or measure | Category | Locator | Risk mechanic and credit implication |
| --- | --- | --- | --- | --- |
| Business | Scheduled passenger airline serving 112 destinations as of December 31, 2025 ("New York's Hometown Airline") | Documentary Fact | 10-K page:9 | Single reportable segment (10-K page:159) means no diversification across businesses; all credit capacity rests on air transportation cash flow. |
| Network | Predominantly point-to-point; 95% of routes touch at least one of six focus cities: New York metropolitan area, Boston, Fort Lauderdale-Hollywood, Orlando, Los Angeles and San Juan | Documentary Fact | 10-K page:11 | Concentration in congested Northeast airspace exposes completion and cost to weather and air traffic control constraints (Q3 10-Q page:31 describes Q3 2026 disruption). |
| Geography by capacity (FY2025 share of available seat miles) | Transcontinental 26.0%; Caribbean and Latin America 36.5%; Florida 25.4%; other (East, Central, West) 7.0%; Transatlantic 5.1% | Documentary Fact | 10-K page:12 | Leisure and VFR weighting gives seasonality; 10-K notes leisure carriers face high seasonality (page:12). |
| Revenue model | Passenger and other revenue; fares in core, EvenMore and Mint cabins; ancillary through the website, global distribution systems and Paisly vacation packages; domestic first class (BlueFirst) planned | Documentary Fact | 10-K page:10, page:11; Q3 10-Q page:6 | Premium and loyalty initiatives aim to lift yield; they are unproven and partly capex-funded, so near-term cash conversion is not helped. |
| Loyalty and co-brand | TrueBlue program; co-branded cards in the United States issued with Barclaycard on the Mastercard network; loyalty points liability at September 30, 2026 of 1,342 | Documentary Fact | 10-K page:14, page:15; Q3 10-Q page:10 | Loyalty cash and collateral support the TrueBlue notes and term loan; the same asset cannot also support unsecured claims. |
| Partnerships | Blue Sky collaboration with United Airlines announced May 2025; cross-merchandising from February 2026; more than 1.1 billion TrueBlue points redeemed on United flights | Documentary Fact (Management Language for the benefits) | 10-K page:13; Q3 10-Q page:31 | Revenue benefit is management-stated and unquantified in the sources; treat as upside not base case. |
| Fuel | No outstanding fuel hedging contracts at September 30, 2026; a hypothetical 10% fuel price increase would raise aircraft fuel expense by approximately $376 million over the next 12 months | Documentary Fact | Q3 10-Q page:53 | Unhedged fuel passes oil moves straight to operating margin; recovery depends on fare actions (management says it recaptured approximately 87% of higher Q3 fuel cost, Q3 release page:1, Management Language). |
| Labor | 49% of active full-time-equivalent crewmembers are union represented; pilots 21% and inflight 28%; pilot contract amendable since February 2025 with negotiations ongoing; inflight contract amendable December 13, 2026; TWU won dispatcher election, negotiations begin December 2026 | Documentary Fact | Q3 10-Q page:19, page:20 | Open contracts are a cost-escalation risk and a strike or slowdown risk (listed in the risk factors) bearing on margin and cash conversion. |
| Fleet | Operating fleet of 298 aircraft at September 30, 2026 (A220 67, A320 129, A321 63, A321neo 39): 288 owned and 10 leased; average age 12 years; 2 further aircraft held for sale | Documentary Fact | Q3 10-Q page:47 | Owned fleet supports secured borrowing (pledged net book value $8.0 billion, Q3 10-Q page:11) but leaves refinancing exposed to aircraft values. |
| Capital spending | Committed flight equipment expenditures of 5,372 including 77 aircraft deliveries; management expects annual capital expenditures below $1 billion through the end of the decade | Documentary Fact (Management Language for the expectation) | Q3 10-Q page:17, page:33 | Large fixed commitments reduce flexibility; deferral of deliveries has been used to protect cash (Q3 10-Q page:43). |
| Engine availability | Two aircraft grounded for lack of engine availability at September 30, 2026; management expects groundings to stay in single digits through 2026; IAE supplemental agreements of July 27, 2026 give credits of up to $105 million through December 31, 2027 | Documentary Fact | Q3 10-Q page:33 | Capacity loss and shop-visit delay hit revenue; the credits are vendor consideration, not cash. |
| Working capital | Working capital deficit of $1.6 billion at September 30, 2026, driven by air traffic liability; air traffic liability current 1,925 and non-current 771 | Documentary Fact | Q3 10-Q page:46, page:6 | Customer prepayments fund operations; a demand shock or processor holdback would drain cash quickly. |
| Credit card processors | Agreements contain no covenants but allow processors to withhold cash reserves; no collateral requirement at present | Documentary Fact | Q3 10-Q page:18 | A holdback right is a liquidity trigger in stress; not currently invoked per the filing. |

### Company profile

| Item | Value | Category | Locator |
| --- | --- | --- | --- |
| Legal entity | JetBlue Airways Corporation, Delaware, incorporated August 1998, service from February 11, 2000 | Documentary Fact | 10-K page:1, page:9 |
| Sector and country | Air Transportation, Scheduled; United States | Documentary Fact from the run context (not issuer evidence) | context |
| Listing | Common stock, NASDAQ, symbol JBLU | Documentary Fact | 10-K page:1 |
| Headquarters | 27-01 Queens Plaza North, Long Island City, New York | Documentary Fact | 10-K page:1 |
| Shares outstanding | 377,351,854 at September 30, 2026 (370,119,668 at January 31, 2026) | Documentary Fact | Q3 10-Q page:1; 10-K page:2 |
| Holders of record | Approximately 350 as of January 31, 2026 | Documentary Fact | 10-K page:80 |
| Employees | Approximately 23,000 crewmembers (10-K); average 19,882 full-time equivalents in Q3 2026 | Documentary Fact | 10-K page:9; Q3 release page:8 |
| Ownership | No sponsor, controlling holder or parent identified in the supplied sources; principal holders are in the 2026 proxy statement, which is not supplied | Insufficient Information | 10-K page:166 (Item 12 incorporates the proxy statement by reference) |
| Dividends and buybacks | "We have not paid cash dividends on our common stock and have no current intention to do so"; no share repurchase program | Documentary Fact | 10-K page:80 |
| Auditor | Ernst & Young LLP, auditor since 2001; opinion that the FY2025 statements present fairly, in all material respects, and an unqualified opinion on internal control | Documentary Fact | 10-K page:108, page:109 |
| Strategy framework | JetForward, announced July 2024: reliable service, East Coast leisure network, products and perks, secure financial future | Documentary Fact | 10-K page:9 |
| Management targets | Return to sustained operating profitability in 2027; at least $1.00 earnings per share and positive free cash flow in 2028 | Management Language | Q3 release page:1; Q2 release page:1 |
| Guidance | FY2026 adjusted operating margin of (4.5%) to (6.5%), interest expense approximately $590 million, capital expenditures approximately $850 million | Management Language | Q3 release page:3 |
| Equity-linked instruments | Warrants issued to the U.S. Treasury under payroll support programs; 2.50% convertible senior notes due 2029 | Documentary Fact | 10-K page:131, page:135 |

### Transaction summary and new debt issues

No acquisition, merger, sponsor transaction or dividend recapitalisation is pending in the supplied sources. The historical transaction is the proposed combination with Spirit Airlines: the merger agreement was terminated by a termination agreement dated March 1, 2024, JetBlue paid a $69 million breakup fee on March 5, 2024, and prepayments to Spirit shareholders totalling $425 million were written off (10-K page:161, page:162). The related appeal over plaintiffs' attorneys' fees is stayed because of Spirit's bankruptcy filings (10-K page:162). In July 2026 JetBlue was selected as successful bidder for 22 operating authorizations at LaGuardia previously operated by Spirit for an aggregate purchase price of $58.5 million, and completed the acquisition in October 2026 after regulatory approval (Q3 10-Q page:44); this occurred after the September 30, 2026 balance sheet date and is a subsequent event, not part of Q3 2026 facts.

New debt in 2026: on April 14, 2026 JetBlue entered into an agreement for up to $500 million of debt financing secured by certain owned A321, A320 and A220 aircraft, fully borrowed by September 30, 2026, with maturities ranging from 2033 through 2036 and interest rates based on U.S. Treasury rates plus a margin; the agreement provides a further $250 million of incremental aircraft-secured financing, access requirements were satisfied during Q3 2026, and "Funding is expected in the fourth quarter of 2026, subject to the completion of customary funding mechanics" (Q3 10-Q page:13, page:14). On April 1, 2026 the 0.50% convertible senior notes were paid in full ($325 million of principal), partly from the Citibank escrow (Q3 10-Q page:13). The use of proceeds of the April 2026 financing is not stated in the sources, and the specific lender, security package and covenants of the agreement are not supplied (Insufficient Information). The August 2024 financings that remain outstanding are the TrueBlue senior secured notes (9.875% coupon, due September 2031, co-issued with JetBlue Loyalty, LP and guaranteed by the Guarantors), the TrueBlue term loan facility due 2029 and the 2.50% convertible senior notes due 2029 (10-K page:129, page:130, page:135). Liquidity effect and amounts outstanding are in CP-1; this handoff adds no new amounts.

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| August 1998; February 11, 2000 | Incorporated in Delaware; commenced service | Documentary Fact | 10-K page:9 |
| July 2020; August 18, 2023 | Northeast Alliance with American Airlines formed; permanently enjoined effective August 18, 2023; wind-down substantially complete | Documentary Fact | Q3 10-Q page:21 |
| March 1, 2024; March 5, 2024 | Spirit merger agreement terminated; $69 million breakup fee paid | Documentary Fact | 10-K page:161 |
| July 2024 | JetForward framework announced | Documentary Fact | 10-K page:9 |
| August 2024 | TrueBlue notes and term loan; 2.50% convertible senior notes | Documentary Fact | 10-K page:129, page:130, page:135 |
| February 28, 2025 | First Amendment to TrueBlue term loan sets margin of SOFR plus 4.75% | Documentary Fact | 10-K page:130 |
| April 28, 2025 | American Airlines sued JetBlue in Texas over a Northeast Alliance revenue-sharing agreement; an accrual has been recorded | Documentary Fact | Q3 10-Q page:22 |
| May 2025 | Blue Sky collaboration with United Airlines announced | Documentary Fact | 10-K page:13 |
| October 27, 2025 | Citibank escrow agreement to keep the revolver expiry at October 21, 2029; $100 million funded before December 31, 2025 | Documentary Fact | 10-K page:137 |
| April 1, 2026 | 0.50% convertible senior notes paid in full | Documentary Fact | Q3 10-Q page:13 |
| April 14, 2026 | Agreement for up to $500 million of aircraft-secured financing | Documentary Fact | Q3 10-Q page:13 |
| July 27, 2026 | Supplemental support agreements with IAE (RTX) | Documentary Fact | Q3 10-Q page:33 |
| July 2026 (completed October 2026) | LaGuardia slots acquisition, aggregate purchase price $58.5 million | Documentary Fact; completion is a Subsequent event | Q3 10-Q page:44 |
| October 9, 2026 | Opposition to class certification filed in the Northeast Alliance antitrust matter | Documentary Fact; Subsequent event | Q3 10-Q page:21 |
| Fourth quarter of 2026 | Expected funding of the additional $250 million secured financing | Management Language (forward-looking) | Q3 10-Q page:14 |
| December 2026 | BlueFirst initial service planned; inflight contract amendable December 13, 2026 | Management Language (forward-looking); Documentary Fact for the contract date | Q3 release page:3; Q3 10-Q page:19 |

### Governance and behaviour

- Scope: issuer-level behaviour from documented actions only; no individuals assessed and no inference from identity.
- Distributions: no cash dividends and no repurchase program (10-K page:80); the cash flow statement shows one small treasury stock acquisition line of unstated purpose (Q3 10-Q page:7, nine months 2026). Category: Neutral or Mixed; no distribution to shareholders is documented. Dimension: payout behaviour.
- Use of secured capacity: the loyalty program is first-lien collateral for the TrueBlue notes and term loan, with a co-borrower subsidiary and Guarantors (10-K page:129, page:130); aircraft-secured borrowing continued in 2026 (Q3 10-Q page:13). Category: Neutral or Mixed. Mechanic: secured funding of operating losses converts unencumbered assets into secured claims over time, so unsecured creditors rank behind a larger secured pool; 66% of owned property and equipment and intangibles were pledged or committed to be pledged (Q3 10-Q page:47). This is an observation of structure, not evidence of priming or collateral release, and no non-pro-rata exchange, drop-down or uptier is documented.
- Disclosure: audited and unqualified opinions (10-K page:108); quarterly reports with covenant compliance statement (Q3 10-Q page:47). Category: Supportive on timeliness; Insufficient Information on covenant levels.
- Shareholder pressure: the 10-K states the Company "has been and may continue to be subject to actions from activist shareholders" (10-K page:44). Category: Documentary Fact; no specific activist or demand is identified in the sources, so no behaviour conclusion is drawn.
- Legal capacity versus willingness versus feasibility: legal capacity cannot be assessed because the debt agreements are not supplied; documented willingness is no distributions and continued secured borrowing; feasibility is shown by liquidity and market access in CP-1, which reports declining unrestricted cash and investments, so feasibility of further large debt-funded actions is limited by collateral availability. Evidence quality: High for filings, Low for management outlook statements.

### Conflicts and unreconciled items

- No document conflict is logged between the supplied sources on transaction size, ownership or dates.
- Unreconciled, not a conflict: management claims an unencumbered asset base of approximately $7 billion (Q3 release page:2) while the 10-Q states approximately 66% of owned property and equipment and intangibles are pledged or committed to be pledged (Q3 10-Q page:47) and $8.0 billion net book value is pledged (Q3 10-Q page:11). The definitions differ and the sources do not reconcile them; CP-2 should not rely on the management figure.
- Different bases, not a conflict: the debt note total before issuance costs differs from the carrying value (see CP-0 and CP-1).

### Credit translations

- Revenue durability. Evidence: demand "remained resilient across our network despite higher fares" (Q3 10-Q page:29) and revenue per available seat mile growth reported by management (Management Language). Mechanic: higher yields have offset fuel in part but volumes are flat to slightly higher and load factor fell year on year (Q3 release page:8), so durability depends on pricing power rather than volume. Implication: revenue is exposed to a demand downturn that cannot be offset by cost cuts quickly; CP-2 should treat the pricing recapture of fuel as unproven beyond the reported quarters. No logged conflict counters this.
- Margin and cash-flow risk. Evidence: unhedged fuel, with a 10% fuel price rise equal to approximately $376 million of annual expense (Q3 10-Q page:53), and open labor contracts. Mechanic: operating margin and cash flow absorb fuel and wage shocks directly. Implication: CP-1 shows operating cash flow negative in FY2025 and in both nine-month periods and free cash flow negative in every period shown, so debt service and capital spending are met from liquidity and secured borrowing; monitoring posture is liquidity burn.
- Concentration risk. Evidence: 95% of routes touch six focus cities and operations are centered in the Northeast corridor (10-K page:11, page:15). Mechanic: weather and air traffic control constraints affect a large share of capacity at once. Implication: disruption costs recur and can coincide with peak travel periods.
- Sponsor alignment. Evidence: no sponsor or controlling holder identified; no dividends or repurchases. Mechanic: no sponsor extraction channel is documented. Implication: alignment risk is low on the evidence supplied, but beneficial ownership is Insufficient Information until the proxy statement is supplied.
- Key uncertainties: the terms of the TrueBlue and aircraft financing covenants; the outcome of the antitrust class action and the American Airlines contract claim, for which no loss estimate is given for the former (Q3 10-Q page:21); labor outcomes; fuel path; and the funding of the further $250 million increment.

### Consumers

| Module | Readiness | What it should take from this handoff | Why it matters | Gap and required action |
| --- | --- | --- | --- | --- |
| CP-2 | Ready with limitations | Collateral structure (loyalty program and aircraft), absence of sponsor, labor and fuel exposure, financing timeline | Defines the secured versus unsecured claim structure and the risks to margin | Supply the TrueBlue indenture, term loan and aircraft financing documents; do not use the unreconciled unencumbered asset claim |
| CP-5 | Ready with limitations | Fact categories, locators and the unreconciled items list | Traceability of management language versus filed fact | Spot-check quoted figures against the filed HTML |

## Calculations

All inputs are cited above. No figure from CP-1 is changed.

- Passenger revenue share, nine months 2026: 7,135 / 7,749 = 92.08 percent. Q3 2026: 2,600 / 2,812 = 92.46 percent (Q3 10-Q page:6).
- Fuel share of total operating expenses: Q3 2026 868 / 2,956 = 29.36 percent; nine months 2026 2,352 / 8,258 = 28.48 percent. Salaries, wages and benefits share: Q3 2026 946 / 2,956 = 32.00 percent; nine months 2026 2,717 / 8,258 = 32.90 percent (Q3 10-Q page:6).
- Fleet: 67 + 129 + 63 + 39 = 298 operating aircraft, equal to 288 owned + 10 leased (Q3 10-Q page:47).
- Union representation: 21 + 28 = 49 percent (Q3 10-Q page:19).
- Capacity distribution FY2025: 26.0 + 36.5 + 25.4 + 7.0 + 5.1 = 100.0 percent (10-K page:12).
- Committed deliveries: 33 A220 + 44 A321neo = 77 (Q3 10-Q page:17).
- Share count change from January 31, 2026 to September 30, 2026: 377,351,854 - 370,119,668 = 7,232,186 shares, 1.95 percent of the January figure.
- LaGuardia slots: $58.5 million / 22 = $2.66 million per authorization (an average derived for context only).
- Spirit termination costs: $69 million breakup fee and $425 million total prepayments are separate items in Note 18; they are not summed here because the sources describe the prepayments as written off together with a $25 million reimbursement.

## Gaps

| Gap | Severity | Affected | Remediation |
| --- | --- | --- | --- |
| Principal holders and beneficial ownership are in the 2026 proxy statement, which is not supplied | Medium | Ownership and sponsor alignment | Supply the proxy statement |
| Executed debt and security documents (TrueBlue indenture and term loan, aircraft financing, Citibank agreement) are not supplied | High | Legal capacity, covenant and collateral analysis | Supply the agreements |
| Use of proceeds and lender identity for the April 14, 2026 financing are not stated | Medium | Transaction summary | Supply the related 8-K or agreement |
| Revenue benefit from Blue Sky, BlueFirst and loyalty initiatives is management-stated and not quantified in the filings | Medium | Revenue durability | Obtain management bridge if one exists |
| Unencumbered asset claim of approximately $7 billion not reconciled | Medium | Collateral, secondary liquidity | Obtain appraisal basis and encumbrance schedule |
| Events from October 27, 2026 to 2026-11-05 not supplied | Medium | Subsequent events | Supply later filings or confirm none |
| No debt maturity schedule by instrument beyond the aggregate table, no covenant certificate, no add-back bridge | Medium | Monitoring | Supply with the agreements |

## Next module

CP-2 (credit analysis) follows, then CP-5. CP-2 should use CP-1 metrics and this handoff's collateral, labor, fuel and financing facts, and should keep the unreconciled unencumbered asset claim out of its base case.
