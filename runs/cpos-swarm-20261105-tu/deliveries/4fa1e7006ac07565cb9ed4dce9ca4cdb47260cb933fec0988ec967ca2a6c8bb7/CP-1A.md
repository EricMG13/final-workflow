# CP-1A business and transaction context: TELUS CORP (tu)

## Request

- Issuer: TELUS CORP (issuer id `tu`; registrant "TELUS Corporation"), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run: `tu-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, module CP-1A (transaction, ownership, business and operating model, timeline, governance behaviour, capital allocation). Execution: host session; no provider call.
- Reader question: which transaction, business, ownership and operating facts matter most to a creditor of TELUS Corporation? Decision drivers: transaction and ownership structure; business and operating model; credit-relevant history or change.
- Periods and units: figures follow the CP-1 handoff (C$ millions unless stated; Q2 2026 means the three months ended June 30, 2026). Where this handoff repeats a CP-1 figure it uses the same value and period. Nothing is dated after the cutoff.
- Category tags used on every fact row: Documentary Fact (a cited source states it), Management Language (management's characterisation, quoted and qualified), Analyst Interpretation (this analyst's reading of cited evidence), Insufficient Information (evidence missing; the missing datapoint is stated).
- Prohibited and not done: peer ranking, instrument recommendation, expected recovery outcome. External knowledge is not used. No sponsor is involved in the sources and none is inferred.
- Upstream handoffs: the CP-0 source readiness handoff and the CP-1 financial base handoff. Their limits are carried: no annual information form, no audited FY2025 statements, no June 30, 2026 interim notes, no agreements, no named ratings, restated segments and perimeter changes across vintages.

## Sources

Locators are `page:N`, the chunk number in the pinned text file. Citations read `[LABEL page:N "quote"]`.

| Label | Source (exact name) | sha256 | Role in this handoff |
| --- | --- | --- | --- |
| F40 | 40-F_2025-12-31_tu-20251231x40f.htm.jsonl | b0f2582e02ab1590b79f57963d19432006a5c182a75869a932135c754b75fcd3 | Form 40-F cover document: registrant identity, auditor, exhibit list |
| Q3FS | 6-K-EX-99.1_2025-09-30_tm2525674d1_ex99-1.htm.jsonl | 436bedaf1f4dce1c7e6eb59881bfd06b2eda28c728cd8f139c3e87e5b19f9141 | Interim statements and notes, September 30, 2025: TELUS Digital privatization, Terrion, Workplace Options |
| REL4Q25 | 6-K-EX-99.1_2026-02-12_tm261121d3_ex99-1.htm.jsonl | 86a3aab6322382ed8099639d74b8a5a665cd61822ab77656954f6c33682e6312 | News release, fourth quarter 2025: CEO succession, 2026 targets, operating indicators |
| Q1FS | 6-K-EX-99.1_2026-03-31_tm2610993d1_ex99-1.htm.jsonl | 786ff091c72b6c68ad509f7615fb77cb4d9d97ec151a629884165ec7501f67f6 | Interim statements and notes, March 31, 2026: corporate history, debt terms, share capital |
| REL1Q26 | 6-K-EX-99.1_2026-05-08_tm2610993d2_ex99-1.htm.jsonl | 4a46a2ffd615b6354baf9f5fba0823218c2071cb4a3fa919c80e6fdbc83658f3 | News release, first quarter 2026 |
| REL2Q26 | 6-K-EX-99.1_2026-07-31_tm2615221d2_ex99-1.htm.jsonl | 159e10207755e982fc8e0761482d512b4d2a82246d4508c8eb2d2f1f129bbd5c | News release, second quarter 2026: strategic priorities, dividend reset, guidance |
| MDA2Q26 | 6-K-EX-99.2_2026-06-30_tu-20260630xex99d2.htm.jsonl | df34bf40fbe3d3b13f773ae380315ed0a4e21b523c7736a3fcf69277289ecba4 | MD&A, second quarter 2026: business, capital allocation, regulation |
| context | context | 444f0b1a3ec6fedd71ff422ee4a294e2ddb38e2b78bcbad2de66f2441a8d4efa | User run settings; not issuer evidence |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 544c6cab38ea7d4384375d826af7a24e93016625e263a47b8911621b1695f02d | Source readiness; its gaps are carried |
| CP-1 | 7a6e3bd7a6bb660a29791a2e6e8ec9a696df0f9a3647070b9101f36f2ca71b2f | Financial base; figures repeated here match it |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| TELUS is a listed Canadian telecom with health and digital segments. The creditor-relevant change is a buy-in of TELUS Digital minorities, tower equity sold at Terrion, a dividend reset and weaker guidance; no sponsor is identified. | Medium | The annual information form, deal documents and later events are not supplied, so ownership detail and asset-sale terms cannot be confirmed. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| TELUS bought out the minority holders of TELUS Digital on October 31, 2025 and sold minority equity in the Terrion tower subsidiary in 2025. | Digital cash flows are now fully inside the group but its impairment and weaker demand add pressure; outside holders share Terrion cash flows. | Medium |
| Management reset the dividend, lowered 2026 guidance and moved the leverage target date to year-end 2028. | Cash retained for debt reduction rises, but the date and objective range have been moved twice in six months. | Medium |
| No sponsor, leveraged buyout or creditor-adverse action is documented; the main documented actions are minority equity at a subsidiary and asset sale processes. | Behaviour reads supportive or mixed on documents alone; asset sale terms are not supplied. | Medium |
| Reported customer and health-coverage counts are not comparable across releases and one health figure fell by about ten million between two quarters without explanation. | Operating indicators cannot be trended reliably until definitions are reconciled. | Medium |
| Wholesale fibre access rules and appeals, and a coming spectrum auction, can change competition and capital needs. | Regulatory outcomes affect revenue durability and spectrum cash calls; none is quantified. | Low |

### Business and transaction view

TELUS Corporation is a British Columbia company and one of Canada's largest telecommunications groups, with three reporting segments: TELUS technology solutions (mobile, fixed data and voice, security and automation, agriculture and consumer goods technology), TELUS Health (employee and family assistance programs, benefits administration, virtual care) and TELUS Digital (digital solutions, AI and data, trust and safety, customer experience management). The sources describe no controlling shareholder, no sponsor and no pending change of control; ownership detail beyond the share count and a Canadian-ownership voting restriction is not supplied. The creditor-relevant structure is a parent that issues all identified senior notes, commercial paper and junior subordinated notes and is effectively subordinated to obligations of, or guaranteed by, its subsidiaries, with a subsidiary (Terrion) holding minority outside equity. The relevant history is a 2025 reshaping of the perimeter: the acquisition of Workplace Options in May 2025, the establishment of Terrion in July 2025 with outside equity, and the buy-in of the TELUS Digital minority on October 31, 2025, followed in 2026 by a 2,135 impairment of TELUS Digital, a management transition, a dividend reset, lower guidance and asset sale processes. Business risk is anchored by a large mobile and fibre base with declining ARPU at a decelerating rate, partly offset by growth in connected devices and internet connections. As an analyst reading, TELUS Digital depends on external clients and intersegment work, and Health earnings were built partly by acquisition. The view is restricted by the absence of the annual information form, the transaction agreements and any filing after July 31, 2026.

### Company and operating model

| Area | Fact | Category | Evidence | Credit relevance |
| --- | --- | --- | --- | --- |
| Core activities | TELUS provides mobile and fixed voice and data services, healthcare technology and services, agriculture and consumer goods technology, and digital experiences | Documentary Fact | [Q1FS page:3 "TELUS Corporation is one of Canada’s largest telecommunications companies"] | Diversified but telecom-dominated earnings base |
| Segments | Three reportable segments: TTech, TELUS Health, TELUS Digital; segmented reporting restated from January 1, 2026 after the TELUS Digital privatization | Documentary Fact | [MDA2Q26 page:9 "Effective January 1, 2026, we are retrospectively restating our segmented reporting information"] | Pre-2026 segment data are not like-for-like |
| TTech revenue model | Network revenue and equipment sales from mobile, data (internet protocol, television, hosting, managed IT, security and automation), voice and equipment | Documentary Fact | [MDA2Q26 page:28 "The TELUS technology solutions segment (TTech) includes: network revenues and equipment sales arising from mobile technologies"] | Recurring service revenue with equipment margin exposure |
| TTech scale, Q2 2026 | Mobile network revenue 1,743 and fixed data services 1,175 in Q2 2026, against 1,723 and 1,170 in Q2 2025 (restated) | Documentary Fact | [REL2Q26 page:21 "Mobile network revenue 1,743 1,723 1"] | Mobile growth is small; fixed data is flat |
| Pricing pressure | Mobile phone ARPU of $56.36 declining at a decelerating rate of 0.4 per cent; blended mobile phone churn of 1.08 per cent versus 1.06 per cent | Management Language | [REL2Q26 page:1 "ARPU of $56.36"] | Revenue per user is not growing; value-focused loading |
| Network and capital intensity | 5G network covered about 34.2 million Canadians (over 92 per cent of population); about 3.8 million households and businesses connected to fibre; spectrum investment of over $8.5 billion since mid-2013 | Documentary Fact | [MDA2Q26 page:23 "From mid-2013 through June 30, 2026, we invested over $8.5 billion to acquire wireless spectrum licences"] | Heavy, recurring capital and spectrum cash calls |
| TELUS Health | Employee and family assistance programs, benefits administration, virtual care and pharmacy; 158.9 million healthcare lives covered at June 30, 2026 | Documentary Fact | [REL2Q26 page:5 "healthcare lives covered were 158.9 million as of the end of the second quarter of 2026"] | Acquisition-built earnings; lives-covered counts are not comparable across releases (see Conflicts) |
| TELUS Digital | Four service lines: digital solutions, AI and data solutions, trust and safety, customer experience management; Q2 2026 revenue 774 including intersegment against 827 restated | Documentary Fact | [REL2Q26 page:21 "TELUS Digital Operating revenues and other income 774"] | Revenue declining; relies on external clients and intersegment work |
| Digital demand | Management expects AI services growth not to offset demand ramp-downs and churn in legacy services for certain hyperscale customers | Management Language | [MDA2Q26 page:65 "demand ramp-downs and more pronounced churn"] | Customer concentration and automation risk in one segment |
| Geography | TELUS operates in more than 45 countries and generates over $20 billion in annual revenue | Management Language | [REL2Q26 page:22 "operating in more than 45 countries and generating over $20 billion in annual revenue"] | Core wireline and wireless assets are Canadian; Digital and Health are global |
| Cost structure | Restructuring and other costs assumption for 2026 revised to approximately $900 million from approximately $500 million | Management Language | [MDA2Q26 page:65 "approximately $900 million, from approximately $500 million"] | Cost programs are consuming earnings and cash |
| Capital spending | 2026 capital expenditures guidance raised to approximately $2.6 billion from approximately $2.3 billion | Management Language | [REL2Q26 page:10 "Capital expenditures Approximately $2.3 billion Approximately $2.6 billion"] | Lower free cash flow guidance of approximately $1.8 billion |
| Working capital | Not disclosed as a driver beyond cash flow commentary; supply chain financing program exists | Insufficient Information | Working capital days and program size at June 30, 2026 are Not supplied; CP-1 notes 29 of payables in the program at March 31, 2026 | Limits cash conversion analysis |

### Company profile

| Item | Value | Category | Evidence |
| --- | --- | --- | --- |
| Legal name and form | TELUS Corporation, a British Columbia company | Documentary Fact | [F40 page:1 "British Columbia, Canada"] |
| Incorporation history | Incorporated October 26, 1998 as BCT.TELUS Communications Inc.; current name from May 3, 2000 | Documentary Fact | [Q1FS page:3 "incorporated under the Company Act (British Columbia) on October 26, 1998"] |
| Country and sector | Country: Canada. Sector: radiotelephone communications (context sector field; the Form 40-F lists classification code 4812) | Documentary Fact | [F40 page:1 "Primary Standard Industrial Classification Code Number"] and the context |
| Listing | Common Shares listed on the New York Stock Exchange under TU (the Form 40-F) and the Toronto Stock Exchange under T (the release) | Documentary Fact | [REL2Q26 page:1 "TELUS Corporation (TSX: T, NYSE: TU)"] |
| Principal subsidiaries | TELUS Communications Inc. and TELUS Health Inc., wholly owned at March 31, 2026 | Documentary Fact | [Q1FS page:4 "Our principal subsidiaries"] |
| Subsidiaries with outside equity | Terrion (tower partnership, TELUS holds 50.1 per cent) | Documentary Fact | [Q3FS page:64 "retained a 50.1% voting and economic interest in Terrion"] |
| Common Shares outstanding | 1,575 million at June 30, 2026 and 1,589 million at July 31, 2026 | Documentary Fact | [MDA2Q26 page:64 "Common Shares 1,575"] |
| Voting restriction | Holders vote one vote per Common Share, provided no less than 66-2/3 per cent of Common Shares are owned by Canadians | Documentary Fact | [Q1FS page:47 "no less than 66-2/3%"] |
| Controlling holder and top holders | Not supplied; the Form 40-F does not report holders and the annual information form and proxy are not in the pack | Insufficient Information | Missing datapoint: holders above a threshold; it matters for control and event risk |
| Auditor | Deloitte LLP | Documentary Fact | [F40 page:4 "Deloitte LLP (PCAOB ID No. 1208), as external auditor"] |
| Chief executive | Victor Dodig, President and Chief Executive Officer, effective July 1, 2026, succeeding Darren Entwistle, who was to retire on June 30, 2026 | Documentary Fact | [REL4Q25 page:13 "Darren Entwistle will retire on June 30, 2026"] |
| Chief financial officer | Gopi Chande named in the July 31, 2026 release; the May 8, 2026 release named Doug French | Documentary Fact | [REL2Q26 page:3 "Gopi Chande, Chief Financial Officer"] and [REL1Q26 page:4 "Doug French, Executive Vice-president and CFO said"] |
| Workforce | About 100,000 team members (management statement) | Management Language | [REL2Q26 page:3 "our 100,000 passionate"] |
| Fiscal year end | December 31 | Documentary Fact | [F40 page:1 "For the fiscal year ended December 31, 2025"] |

### Transaction summary and new debt issues

TELUS is not the subject of a sponsor buyout, merger or refinancing in the pinned sources, so no deal-level use of proceeds, sponsor or closing condition applies; one Insufficient Information row stands for any transaction after July 31, 2026, which is Not supplied. The completed transactions that shape the creditor's perimeter are these. First, the TELUS Digital privatization: on June 12, 2025 TELUS Corporation submitted a non-binding indication of interest to the board of TELUS International (Cda) Inc. [Q3FS page:63 "submitted a non-binding indication of interest"], signed a definitive agreement on September 2, 2025 at "for a price per share of US$4.50" [Q3FS page:64 "for a price per share of US$4.50"], payable in cash, Common Shares or a combination subject to a 25 per cent cap on shares, and closed on October 31, 2025 [Q3FS page:64 "The transaction closed October 31, 2025"]. The final cash and share mix and the cash outlay are Not supplied in the pinned sources. Second, Terrion: a wireless tower infrastructure partnership established on July 24, 2025 that issued equity to an outside holder for net cash proceeds of 1,246 [Q3FS page:65 "Net cash proceeds $ 1,261"], after which TELUS keeps 50.1 per cent voting and economic interest and holds a call option exercisable in whole in September 2027 if there is a partner dispute or after September 2057 at generally the greater of fair value and a multiple on invested capital [Q3FS page:64 "call option"]. The outside holder is not named in the pinned sources. The Terrion non-controlling interest was 792 at September 30, 2025 and non-controlling interests were 808 at June 30, 2026 (CP-1). Third, Workplace Options: TELUS acquired 100 per cent on May 1, 2025 [Q3FS page:44 "On May 1, 2025, we acquired 100% of Workplace Options"], with cash consideration of 453 funded in part by 280 (US$200 million) of preferred shares issued by a subsidiary to a private equity investor; the preferred shares were later exchanged for a US$200 million promissory note and the note was repaid in Q2 2026 with a prepayment premium of 51 (CP-1). Fourth, liability management: tender offers in June and December 2025 that bought back senior notes (series CL, CU, CW, CAB, CAE and U.S. dollar notes), with gains on purchase of long-term debt of 222 in Q3 2025 and 81 in Q4 2025 [MDA2Q26 page:29 "Gain on purchase of long-term debt"], the full redemption of the 3.75% Series CV notes on January 16, 2026, the redemption of 500 of the 2.75% Series CZ notes on May 8, 2026, and the payment of the remaining 300 of that series at maturity after June 30, 2026 (CP-1). Fifth, equity and distributions: the dividend reset announced July 31, 2026 and the end of the dividend reinvestment plan discount effective October 1, 2026 [REL2Q26 page:4 "representing a reset of 55 per cent to an annualized amount of $0.75 per share"]; no shares were repurchased under the normal course issuer bid in the quarter [MDA2Q26 page:26 "we did not repurchase or cancel any shares pursuant to our NCIB"]. Sixth, asset monetization: management says it is in discussions on TELUS Health non-core assets and is advancing the monetization of non-core real estate, with proceeds directed to debt reduction [REL2Q26 page:4 "the company remains active in the market on TELUS Health-related non-core assets"]. Assets, buyers, prices and timing are Not supplied, so no leverage effect can be estimated.

New debt issues in the pinned sources, as printed in the March 31, 2026 debt note (all unsecured and issued by TELUS Corporation unless stated): fixed-to-fixed rate junior subordinated notes issued in 2025 and December 2025 comprising Series CAR 6.25 per cent (1,500 outstanding, due July 2055), Series CAS 6.75 per cent (925, due July 2055), U.S. dollar Series A 6.625 per cent (US$700 million, due October 2055), Series B 7.000 per cent (US$800 million, due October 2055), Series C 6.375 per cent (US$800 million, due June 2056), Series D 6.625 per cent (US$700 million, due June 2056), Series CAT 5.375 per cent (400, due June 2056) and Series CAU 5.875 per cent (400, due June 2056) [Q1FS page:45 "Series CAT"]. The Series C, D, CAT and CAU notes were issued in December 2025. The junior subordinated notes are subordinated to all senior indebtedness, receive one-half equity credit in leverage ratios in the initial post-issuance decade, and carry a repurchase offer at 102 per cent upon a rating event (CP-1). No new senior note series issued in the first half of 2026 is itemized in the pinned sources; long-term debt issued in that half is described in the MD&A mainly as commercial paper activity with a commercial paper balance of $2.1 billion (US$1.5 billion) at June 30, 2026 [MDA2Q26 page:56 "a balance of $2.1 billion (US$1.5 billion) at June 30, 2026"]. Sustainability-linked note series (CAF, CAG, CAJ, CAK, CAN and the 3.40 per cent U.S. dollar series) were issued before 2025 and the debt table refers to trigger events and step-ups for them (CP-1 debt register).

### Ownership and control

- Controlling shareholder or sponsor: Not supplied and none indicated. Category: Insufficient Information for any holder above a threshold. The issuer is a listed company with a Canadian-ownership restriction on voting [Q1FS page:47 "no less than 66-2/3%"].
- Subsidiary equity: Terrion has outside equity and a call option held by TELUS (above). The outside holder's rights over distributions, governance and exit are Not supplied beyond the call option, so the claim ranking between Terrion's creditors, the outside holder and TELUS Corporation cannot be set.
- Prior ownership: until October 31, 2025 TELUS Digital had public minority holders and a non-controlling interest of 1,649 at September 30, 2025 in TELUS Corporation's consolidated equity (CP-1).
- Dividend recapitalization history: none documented. Capacity to distribute: the indentures limit security on indebtedness, sale-leaseback transactions and new indebtedness by TELUS and certain subsidiaries, and do not restrict dividends in the text supplied [Q1FS page:39 "The notes’ indentures contain covenants"]. The full covenant package is Not supplied.

### Timeline

| Date | Event | Category | Evidence |
| --- | --- | --- | --- |
| Oct 26, 1998 | Incorporation as BCT.TELUS Communications Inc. | Documentary Fact | [Q1FS page:3 "incorporated under the Company Act (British Columbia) on October 26, 1998"] |
| Mid-2013 to Jun 30, 2026 | Over $8.5 billion invested in wireless spectrum | Documentary Fact | [MDA2Q26 page:23 "From mid-2013 through June 30, 2026, we invested over $8.5 billion to acquire wireless spectrum licences"] |
| May 1, 2025 | Workplace Options acquired | Documentary Fact | [Q3FS page:44 "On May 1, 2025, we acquired 100% of Workplace Options"] |
| Jun 12, 2025 | Indication of interest for the TELUS Digital minority | Documentary Fact | [Q3FS page:63 "submitted a non-binding indication of interest"] |
| Jul 24, 2025 | Terrion established and outside equity issued | Documentary Fact | [Q3FS page:64 "retained a 50.1% voting and economic interest in Terrion"] |
| Sep 2, 2025 | Definitive agreement for the TELUS Digital minority at US$4.50 per share | Documentary Fact | [Q3FS page:64 "for a price per share of US$4.50"] |
| Oct 31, 2025 | TELUS Digital privatization closed | Documentary Fact | [Q3FS page:64 "The transaction closed October 31, 2025"] |
| Dec 2025 | Junior subordinated notes Series C, D, CAT, CAU issued; senior note tender offer | Documentary Fact | [Q1FS page:45 "Series CAT"] |
| Jan 2026 | 3800 MHz spectrum acquired in the residual auction | Documentary Fact | [MDA2Q26 page:53 "residual auction that concluded in January 2026"] |
| Feb 12, 2026 | CEO succession announced | Documentary Fact | [REL4Q25 page:13 "Darren Entwistle will retire on June 30, 2026"] |
| Jun 30, 2026 | Impairment of intangible assets and goodwill of 2,135 in the TELUS Digital unit | Documentary Fact | [REL2Q26 page:5 "See Note 18(b) of the interim consolidated financial statements for additional details"] |
| Jul 1, 2026 | New CEO effective | Documentary Fact | [REL4Q25 page:13 "appointed Victor Dodig"] |
| Jul 30 to 31, 2026 | Dividend reset, DRIP discount removal, revised guidance, three strategic priorities announced | Documentary Fact | [REL2Q26 page:4 "representing a reset of 55 per cent to an annualized amount of $0.75 per share"] |
| Oct 1, 2026 | Reset dividend payable; DRIP discount removed (dated in the release; outcome not supplied) | Management Language | [REL2Q26 page:4 "payable on October 1, 2026"] |
| Oct 2027 | Millimetre wave spectrum auction scheduled (future event) | Documentary Fact | [MDA2Q26 page:66 "Auction bidding starts October 19, 2027"] |
| After Jul 31, 2026 | Third-quarter 2026 results referenced for November; nothing supplied | Insufficient Information | [REL2Q26 page:3 "A more detailed outline of the capital returns framework and corporate strategy will be provided with TELUS' third quarter 2026 results in November"] |

### Governance and behaviour

Assessment is issuer-level and documented actions only; no sponsor identity is used.

| Behaviour | Documented action | Category | Legal capacity, willingness, feasibility |
| --- | --- | --- | --- |
| Supportive: deleveraging | Dividend cut by 55 per cent; DRIP discount removed; stated target of about 3.0-times or lower by year-end 2028 | Management Language | Willingness: stated and acted on for the dividend. Capacity: dividends are board discretion in the text supplied. Feasibility: free cash flow guidance of approximately $1.8 billion and capital expenditures of approximately $2.6 billion |
| Supportive: equity-like funding | Junior subordinated notes with one-half equity credit; minority equity sold at Terrion | Documentary Fact | Willingness: documented. Feasibility: depends on rating agency treatment, which is Not supplied |
| Neutral or mixed: policy moves | Leverage objective range moved from 2.2 to 2.7 times (Q1FS) to 2.5 to 3.0 times (MD&A); target year moved from year-end 2027 to year-end 2028; free cash flow payout guideline moved to 45 to 60 per cent of trailing twelve-month free cash flow | Documentary Fact | Capacity: policies are non-binding. Willingness: the targets have been repeatedly reset; feasibility depends on asset monetization not yet quantified |
| Neutral or mixed: distributions above cash after capital | The ratio of common dividends declared to cash from operations less capital expenditures was 109 per cent for the twelve months to June 30, 2026 [MDA2Q26 page:59 "capital expenditures 109 107"] | Documentary Fact | Action reversed by the dividend reset after quarter-end |
| Extraction-oriented or creditor-adverse | None documented in the pinned sources: no priming, uptier, drop-down, non-pro-rata exchange or collateral release; the Terrion structure is a minority equity sale, not a creditor-adverse transfer, on the text supplied | Insufficient Information | Missing datapoints: Terrion governance, any guarantees or asset transfers; the executed agreements are Not supplied |

Evidence quality: High for the filed statements and MD&A (primary, dated, issuer-specific); Medium for news releases (management-prepared and attributed). No Low or Insufficient material was relied on for a factual claim.

### Capital allocation and disclosure

- Dividends: quarterly dividend declared of $0.4184 per share through Q2 2026, reset to $0.1875 per share for the declared third-quarter dividend. Mechanism: lower cash dividends (864 paid in H1 2026 per CP-1) increase cash available for debt repayment; the issuer states approximately $2.7 billion in cumulative cash savings through 2028 directed to deleveraging (management estimate).
- Capital expenditures and spectrum: capital expenditures guidance raised; spectrum payments of 373 in the first six months of 2026 and an auction in October 2027 are cash calls that can delay deleveraging. Mechanism: spectrum is financed with debt and cash; the issuer says spectrum acquisitions increased the leverage ratio by approximately 0.6 and the junior subordinated notes equity credit decreased it by 0.5 [MDA2Q26 page:59 "the acquisition of spectrum licences increased the ratio by approximately 0.6"].
- Acquisitions and disposals: Workplace Options (cash 453) in 2025; asset monetization under way in 2026. Appetite for further acquisitions is not inferred from one deal.
- Disclosure for monitoring: the debt schedule and maturity schedule are dated March 31, 2026; covenant certificates, credit agreements and an add-back bridge are Not supplied (severity Medium).

### Conflicts and logged discrepancies

These are logged as found and are not reconciled.

| Item | Source A | Source B | Effect |
| --- | --- | --- | --- |
| TTech customer connections | [REL4Q25 page:7 "Our total TTech subscriber base of 21.2 million connections"] | [REL2Q26 page:5 "Our TTech subscriber base of 17.9 million connections"] | The MD&A says television, security and automation and residential voice subscribers are no longer reported from January 1, 2026 [MDA2Q26 page:13 "will no longer report TV, security and automation and residential voice subscribers"]. Counts across the two vintages are not comparable |
| Healthcare lives covered | [REL1Q26 page:10 "Healthcare lives covered were 169.6 million as of the end of the first quarter of 2026"] | [REL2Q26 page:5 "healthcare lives covered were 158.9 million as of the end of the second quarter of 2026"] | The count was 161.2 million at December 31, 2025 [REL4Q25 page:7 "healthcare lives covered were 161.2 million"], 169.6 million at March 31, 2026 and 158.9 million at June 30, 2026. The fall of 10.7 million between the last two quarter-ends has no explanation in the pinned sources. Treat the counts as management operating indicators, not trendable |
| Leverage objective and target date | [Q1FS page:8 "Our long-term objective range for this ratio is 2.2 – 2.7 times"] | [MDA2Q26 page:27 "Net debt to EBITDA – excluding restructuring and other costs ratio of 2.5 to 3.0 times"] | The objective range shifted and the 3.0-times target date moved to year-end 2028 from year-end 2027. Later source controls current policy; earlier ranges are history |
| Free cash flow guidance | [REL1Q26 page:1 "Consolidated Free Cash Flow of approximately $2.45 billion"] | [REL2Q26 page:2 "full-year free cash flow is anticipated to be approximately $1.8 billion"] | Superseded guidance, not a document conflict |

### Credit translations

1. Perimeter and structural subordination. Evidence: the buy-in of the TELUS Digital minority closed October 31, 2025 and Terrion has outside equity with TELUS holding 50.1 per cent [Q3FS page:64 "retained a 50.1% voting and economic interest in Terrion"]; the senior notes are effectively subordinated to obligations of, or guaranteed by, subsidiaries (CP-1). Mechanism: cash generated in Terrion is shared with the outside holder, and any creditors of Terrion (its own debt is Not supplied) would rank ahead of the parent's notes, while TELUS Digital cash flows now fully accrue to the group but carry impairment and demand risk. Implication: a creditor of the parent depends on upstreaming from subsidiaries; guarantor and Terrion terms are Not supplied, so the structural position cannot be completed. The counter-evidence is that the parent issues all identified senior debt and TELUS Communications Inc. and TELUS Health Inc. are wholly owned.
2. Revenue durability and margin. Evidence: mobile network revenue 1,743 against 1,723, fixed data services 1,175 against 1,170, TELUS Digital revenue down to 774 from 827, and ARPU declining at a decelerating rate. Mechanism: growth is subscriber-led with flat unit pricing, so incremental margin depends on cost programs, which management has enlarged (restructuring assumption of approximately $900 million). Implication: free cash flow is exposed to price competition and Digital demand; management lowered 2026 guidance. The counter-evidence is subscriber growth in connected devices and internet.
3. Capital allocation and deleveraging path. Evidence: dividend reset, capital expenditures guidance of approximately $2.6 billion, asset sale processes without terms, and a leverage target moved to year-end 2028. Mechanism: debt reduction depends on lower dividends and unquantified proceeds while capital intensity is higher in 2026 and a spectrum auction follows in October 2027. Implication: leverage tolerance is limited near term; monitor the next release for the capital returns framework and any asset sale agreements. The counter-evidence is the investment-grade wording and covenant headroom reported in CP-1.
4. Regulatory risk to revenue durability. Evidence: the wholesale fibre access framework requires aggregated access to TELUS fibre networks and is under appeal, with hearings likely late 2026 or early 2027 [MDA2Q26 page:67 "The appeal and judicial review will be heard together, likely in late 2026 or early 2027"]. Mechanism (analyst interpretation): wholesale access can reduce retail fibre share and price. Implication: outcome is uncertain and unquantified in the pinned sources; the issuer does not state a financial effect.

### Consumers

| Consumer | Readiness | What to take from this handoff | Why it matters | Gap | Required action |
| --- | --- | --- | --- | --- | --- |
| CP-2 | Ready with limitations | Perimeter changes, Terrion minority and call option, dividend reset, guidance changes, asset monetization, management transition, regulatory items, conflicts | Business risk and capital allocation drive the credit view with the CP-1 figures | Annual information form, Terrion and guarantee terms, holders, agreements, ratings not supplied | Carry gaps; do not state a structural ranking beyond the sources |
| CP-5 | Ready with limitations | Quote-level citations for each row; the logged conflicts and superseded guidance | Operating indicators and policy ranges change across vintages | Original HTML not supplied; healthcare lives covered and connection counts unreconciled | Treat the four logged items as open until reconciled by the issuer's later filings |

## Calculations

No new calculation. Figures repeated from CP-1 or a source are copied unchanged: Terrion net cash proceeds 1,246 are the printed net figure from the Terrion equity table (1,261 issue less 15 other). The change in healthcare lives covered between quarter-ends is a difference of the two printed values: 169.6 less 158.9 = 10.7 million. The dividend cut of 55 per cent and the annualized 0.75 and 1.6736 are copied from the release.

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Annual information form not supplied: business description, competition, ownership, governance and risk factors by the issuer's own annual text | Medium | CP-2, CP-5 | Supply Exhibit 99.3 of the Form 40-F |
| Holders above a threshold and any control rights not supplied | Medium | CP-2 | Supply the proxy circular or annual information form ownership section |
| Terrion governance, outside holder identity and distribution rights, guarantees and subsidiary debt not supplied | High | CP-2 | Supply the Terrion partnership terms or the filing attaching them |
| TELUS Digital privatization consideration mix and cash outlay not supplied | Medium | CP-2 | Supply the arrangement agreement or closing disclosure |
| Asset sale processes for TELUS Health non-core assets and real estate: assets, buyers, prices and timing not supplied | High | CP-2 | Supply any agreement or announcement after July 31, 2026 |
| Healthcare lives covered and connection counts not comparable across vintages; the 169.6 to 158.9 million movement unexplained | Medium | CP-5 | Obtain the issuer's reconciliation |
| Nothing after July 31, 2026 supplied, including third-quarter 2026 results | Medium | CP-2, CP-5 | Supply later filings or confirm none |
| Executed financing agreements and named ratings not supplied | Medium | CP-2 | Supply credit agreements, indentures and rating reports |

## Next module

CP-2 (fundamental credit synthesis) is next, then CP-5. CP-2 should combine this handoff's perimeter, Terrion, capital allocation and conflict rows with the CP-1 definition dependence of leverage, the March 31, 2026 date of the debt register, and the missing agreements. CP-5 should check that the figures repeated here (1,246 Terrion net proceeds, 2,135 impairment, 3.0-times target at year-end 2028, dividend 0.1875 and 0.4184) match their sources and CP-1, and carry the four logged discrepancies as open.
