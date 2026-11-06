# CP-1A business and transaction context: TENET HEALTHCARE CORP (thc)

## Request

- Issuer: TENET HEALTHCARE CORP (issuer id `thc`; registrant as filed: Tenet Healthcare Corporation, NYSE: THC), as of 2026-11-05, information cutoff 2026-11-05 (context).
- Run `thc-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, reporting currency USD, in millions unless stated. Current period Q3 2026; prior period FY2025.
- Reader question: which transaction, ownership, business and operating facts matter most to a creditor? Decision drivers: transaction and ownership structure; business and operating model; credit-relevant history or change.
- Execution: host session; no provider call. Locators are `page:N`, the chunk number in the pinned `.jsonl` text, not the printed page. Figures that come from the accepted financial handoff are labelled "CP-1 figure".
- Prohibited by the method and respected here: no peer ranking, no instrument recommendation, no recovery conclusion.
- Fact categories: Documentary Fact (the cited source states it), Management Language (management's characterisation, never adopted), Analyst Interpretation, Insufficient Information.

## Sources

| Source | sha256 | Role |
| --- | --- | --- |
| 10-K_2025-12-31_thc-20251231.htm.jsonl | f11b8c51ccd0de901ead39554fe597e277a823a504d6f5879743322f2e033f67 | Business description, hospital table, history, debt note, Conifer subsequent event, risk factors |
| 10-Q_2026-03-31_thc-20260331.htm.jsonl | ae2f3d08760ee554a01678cce38fd15c1f6dcfb4f1eb937aa8f7c46189f0123b | Omnibus Agreement as first reported in a quarterly report |
| 10-Q_2026-06-30_thc-20260630.htm.jsonl | a8d86c65c6d20d928c4d4325b82f5d466ad3837698345b3d3bc00c8145f3cd72 | Q2 2026 statements and notes (read for continuity) |
| 10-Q_2026-09-30_thc-20260930.htm.jsonl | e79732f4107be2e25480e8b1b80ad38188b6eb8362209287bd06381751951a29 | Latest quarterly report: segments, payer mix, regulation, refinancing, Conifer |
| EX-99.1_2026-04-30_thc-20260331ex991earningsr.htm.jsonl | 5ea4e9008424f03304d19bf4ecd566569d118ac8a64e8cca9032f7ad6a5e6de8 | Q1 2026 release; management statements |
| EX-99.1_2026-07-23_thc-20260630ex991earningsr.htm.jsonl | 03d054c86dcde38802e070349b77939f6a497570e6b4a7e4537e884b4aff9ae1 | Q2 2026 release; management statements |
| EX-99.1_2026-10-29_thc-20260930ex991earningsr.htm.jsonl | de8966425c6d51c46fec7968d415d855247be5599cd3f04bbba535aedb3bc95d | Q3 2026 release; segment results, outlook, management language |
| context | 0ee21d145e164a59cd564e90c45b59adffc7b68df2c1b6fb4dcb72027505ffb5 | User run settings (sector, country, ticker); not issuer evidence |

| Handoff module | sha256 | Use |
| --- | --- | --- |
| CP-0 | 7380c434050643b1a54d0163daac1ad648692a43ba1556324f37ec4ffc476d9e | Readiness and limits: Omnibus Agreement, 8-K, proxy statement and indentures not supplied; releases are management claims |
| CP-1 | 7b6f055847726910c3eaf6ffe5f0c19c7c490df99bdf5c479f4eef99e9429c40 | Financial base: leverage 2.65x total and 2.11x net on LTM Q3 2026, cash interest cover 6.03x, liquidity 4,574, debt structure, refinancing facts |

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Tenet is a large, geographically concentrated hospital operator with a growing, high-margin surgery business. The main change is the CommonSpirit exit from Conifer and the September 2026 refinancing, with steady share buybacks. | Medium | Ownership, board and shareholder-return policy documents, the CommonSpirit agreement and the indentures are not supplied. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| Two segments, hospitals and ambulatory surgery, with ambulatory earnings partly owned by physician and other partners. | Consolidated earnings overstate what reaches the issuer's creditors; noncontrolling distributions are a priority cash call. | High |
| The CommonSpirit agreements end a long revenue cycle contract and bring 1.900 billion of payments over three years, plus a receivable and one-time revenue. | Cash is supportive but the revenue is non-recurring and the lost contract removes recurring client revenue. | Medium |
| Revenue depends on managed care, Medicaid supplemental payments and policy; coverage changes began to cut exchange admissions in 2026. | Payer-mix and policy risk can compress margins even with moderate leverage. | Medium |
| Documented behaviour is refinancing and buybacks; no creditor-adverse action appears in the supplied text, but legal capacity for shareholder payments is described inconsistently. | Distribution capacity cannot be sized until the executed documents are read. | Low |

### Business and transaction view

Tenet is a diversified US healthcare services company with two reporting segments: Hospital Operations and Services, which at September 30, 2026 ran 51 acute care and specialty hospitals in eight states plus 135 outpatient facilities and the Conifer revenue cycle business, and Ambulatory Care, which holds interests in surgery centers and surgical hospitals through USPI. The business is revenue-durable in the sense that demand for hospital and surgical care is non-discretionary and managed care contracts reprice with commercial rate increases, but the revenue base is exposed to government payment policy and to the shift of patients between payer classes. The one transaction that matters to creditors in the period is the January 2026 set of agreements with CommonSpirit Health, which returned Conifer to full Tenet ownership, ends the revenue cycle contract with CommonSpirit by the end of 2026 and delivers a payment stream of 1.900 billion over three years, of which 540 million was settled by offset on January 27, 2026. The second is the September 2026 refinancing of 2,000 of 2027 secured and 2028 unsecured notes into 2034 unsecured notes. No ownership change, sponsor or leveraged transaction is disclosed; the issuer is a listed company that repurchases its shares. The view is Medium confidence: documentary facts about segments, facilities, agreements and debt are strong, but control rights, board composition, shareholder-return policy and the full CommonSpirit and indenture documents are not in the supplied set.

### Company and operating model

| Area | Fact | Category | Locator | Credit translation |
| --- | --- | --- | --- | --- |
| Core activities | Two segments: Hospital Operations and Services, and Ambulatory Care (USPI); 51 hospitals in eight states and 135 outpatient facilities at September 30, 2026 | Documentary Fact | Q3 10-Q page:26 | Revenue is split by facility type; Hospital Operations produced 12,548 of 16,627 net operating revenues in 9M 2026 (Q3 10-Q page:24), the larger earnings and cash base |
| Ambulatory footprint | USPI held interests in 535 surgery centers (406 consolidated) and 25 surgical hospitals (seven consolidated) in 37 states | Documentary Fact | Q3 release page:3 | Only consolidated facilities flow into revenue; unconsolidated ones feed equity earnings of 180 in 9M 2026 and management fees, so cash reaching the issuer differs from system-wide size |
| Geography and concentration | Hospitals in Arizona, California, Florida, Massachusetts, Michigan, South Carolina, Tennessee and Texas; about 74% of Hospital Operations outpatient centers are in Arizona and Texas | Documentary Fact | 10-K page:4 to page:6 | State Medicaid policy and local events hit a concentrated footprint; the 10-K itself says these concentrations increase the risk from adverse local economic, regulatory or environmental conditions (10-K page:6) |
| Revenue streams | Payer mix of hospital net patient service revenue, 9M 2026: Medicare 15.2%, Medicaid 11.9%, managed care 68.5%, uninsured 0.1%, indemnity and other 4.3% | Documentary Fact | Q3 10-Q page:34 | Managed care dominates; commercial pricing and exchange volumes drive margin |
| Concentration of payers | The top 10 managed care payers generated 66% of managed care net patient service revenues in 9M 2026; national payers 51% | Documentary Fact | Q3 10-Q page:39 | A few payers set rates; contract renegotiation is the key revenue-visibility risk |
| Government supplemental revenue | Medicaid revenue included 1.107 billion of disproportionate-share and other supplemental program revenue in 9M 2026, against 1.023 billion in 9M 2025 | Documentary Fact | Q3 10-Q page:37 | Supplemental payments are policy-dependent; reductions or delays hit cash conversion |
| Pricing and volume drivers | Q3 2026 Hospital net operating revenues rose on higher patient volumes and pricing strength, partly offset by a less favorable payer mix | Documentary Fact | Q3 10-Q page:30 | Growth in 2026 relies on volume and price while exchange admissions fall |
| Coverage change | Enhanced marketplace provisions expired at the end of 2025 and admissions among exchange patients decreased in 2026, an unfavorable payer-mix shift | Documentary Fact | Q3 10-Q page:35 and page:36 | Mix erosion is margin pressure; charity and uninsured admissions rose 26.0% in Q3 2026 (page:29) |
| Policy overhang | The One Big Beautiful Bill Act's key provisions take effect from 2027: Medicaid work requirements, caps on state-directed payments, limits on provider taxes; management states it cannot estimate the impact | Management Language | Q3 10-Q page:36 | Timing sits inside the 2028 to 2030 maturity window; supplemental-payment risk is a credit uncertainty, not a quantified loss |
| Cost structure | Salaries, wages and benefits 6,578, supplies 2,928 and other operating expenses 3,480 in 9M 2026, labour the largest line; about 20% of Hospital Operations employees are unionized | Documentary Fact | Q3 10-Q page:2; 10-K page:12 | Labour is the dominant cost; Hospital Operations salaries fell 2.1% in Q3 2026 (page:32), a margin driver to monitor for sustainability |
| Capital spending | Purchases of property and equipment 546 in 9M 2026; FY2026 capital expenditure outlook 700 to 800 | Documentary Fact; outlook is Management Language | Q3 10-Q page:49; Q3 release page:4 | Capex is modest against operating cash flow of 3,507 for the period (CP-1 figure) |
| Joint-venture and partner economics | Redeemable noncontrolling interests of 2,179 are mostly Ambulatory Care (2,134), which also accounts for 341 of the 342 net income available to redeemable noncontrolling interests in 9M 2026; distributions to noncontrolling interests of 614 were paid in 9M 2026 (CP-1 figure LTM 838) | Documentary Fact | Q3 10-Q page:4 and page:20 | Partners are paid before creditors in practice; EBITDA less these distributions is a sensitivity (3.18x total debt in CP-1) |
| Working capital | Accounts receivable 2,595 at September 30, 2026 against 2,565 at December 31, 2025; revolver is a borrowing base on receivables, inventory and Medicaid supplemental payments | Documentary Fact | Q3 10-Q page:2 and page:13 | Liquidity access scales with receivables quality and supplemental-payment timing |
| Operating adjustments | Q3 2026 Adjusted EBITDA includes a 147 favorable net impact from the revenue cycle transition | Management Language | Q3 release page:2 | Headline earnings are lifted by a non-recurring timing item (CP-1 sensitivity: 2.73x total, 2.18x net) |

### Company profile

| Attribute | Value | Category | Locator |
| --- | --- | --- | --- |
| Legal name and domicile | Tenet Healthcare Corporation, Nevada; headquarters Dallas, Texas | Documentary Fact | Q3 10-Q page:1 |
| Sector | Services-General Medical & Surgical Hospitals, NEC | Documentary Fact (context field, not issuer evidence) | context |
| Country | United States | Documentary Fact (context field) | context |
| Listing | Common stock on the New York Stock Exchange (THC) and the 6.875% Senior Notes due 2031 (THC31) | Documentary Fact | Q3 10-Q page:1 |
| Licensed beds | 12,494 at December 31, 2025 | Documentary Fact | 10-K page:5 |
| Hospital ownership | Sole ownership of 46 of 50 hospitals at December 31, 2025; two majority owned by a Tenet subsidiary; two leased from third parties | Documentary Fact | 10-K page:3 |
| People | Nearly 100,000 employees at December 31, 2025, about 5,600 of them at the Global Business Center in the Philippines | Documentary Fact | 10-K page:9 and page:10 |
| Share count | 79,588 thousand shares outstanding at October 23, 2026, against 86,952 thousand at December 31, 2025 | Documentary Fact | Q3 10-Q page:1; 10-K page:120 |
| Controlling holder or sponsor | None disclosed in the supplied text; the context sponsor field is blank | Insufficient Information | context; 10-K page:2 |
| Directors, executive officers and beneficial owners | Part III items are listed in the table of contents at a page reference; the board and holder tables are not in the supplied text | Insufficient Information | 10-K page:2 |
| Auditor | Auditor since 2007; unqualified opinion dated February 17, 2026 | Documentary Fact | 10-K page:118; page:113 |
| Recent segment revenue | Hospital Operations 4,260 and Ambulatory Care 1,371 of 5,631 in Q3 2026 | Documentary Fact | Q3 10-Q page:29 |

### Transaction summary and new debt issues

CommonSpirit and Conifer. The 10-K describes the position at December 31, 2025: Tenet owned 76.2% of Conifer Health Solutions and CommonSpirit Health held 23.8%, and "In January 2026, we completed a strategic transaction with CommonSpirit Health" that returned Conifer to full ownership effective January 1, 2026 (10-K page:6). The quarterly reports give the terms. On January 27, 2026 the parties agreed to conclude the revenue cycle contract by December 31, 2026, to a payment by CommonSpirit of an aggregate 1.900 billion in annual installments over three years of which 540 million was satisfied on January 27, 2026 by offsetting the 540 million due to CommonSpirit, and to Conifer's redemption of CommonSpirit's minority interest for 540 million effective January 1, 2026 (Q3 10-Q page:5). The residual claim is carried as a non-interest-bearing promissory note of 1.360 billion with three annual payments of approximately 453 million, the first two due in January 2027 and January 2028 and the last, with unpaid principal, in January 2029; carrying value at September 30, 2026 was 434 current and 828 long-term (Q3 10-Q page:10). The redemption cut redeemable noncontrolling interests by 846 and raised additional paid-in capital by 306 in the nine months (Q3 10-Q page:20). Revenue from contract termination of 646 in Q3 2026 and 1,472 in 9M 2026 is shown as a separate statement line, and the quarterly report says the transition will be substantially complete by October 30, 2026 rather than December 31, 2026, producing a cumulative catch-up that raised revenue from contract termination by 233 and net operating revenues by 97 (Q3 release page:2); those are management statements dated October 29, 2026, and the October 30 completion is a subsequent event to the September 30 balance sheet. Mechanics for creditors: the receivable is an asset payable by CommonSpirit over 2027 to 2029, the 540 offset inflates both operating inflows and a financing outflow in 9M 2026 (CP-1), and the lost contract removes the recurring Conifer revenue from CommonSpirit facilities after 2026. The amount of that recurring revenue and its margin are not disclosed in the supplied text, so the earnings effect of the loss cannot be sized. Full ownership also removes CommonSpirit as a minority holder of a subsidiary (Analyst Interpretation).

New debt issue, September 2026. Tenet issued 2,000 of 6.250% senior unsecured notes due September 2034 in a private placement, with interest payable March 15 and September 15 from March 15, 2027, and used the net proceeds with cash on hand to redeem all 1,500 of 5.125% senior secured first lien notes due November 2027 and 500 of the 1,750 of 6.125% senior unsecured notes due October 2028 (Q3 10-Q page:13; Q3 release page:2). A loss from early extinguishment of debt of 5 was recognised in Q3 2026 (Q3 10-Q page:3). The Forty-Third Supplemental Indenture is dated September 22, 2026 (Q3 10-Q page:53) but is not supplied, so the covenant package, guarantees, call schedule and change-of-control terms of the new notes are Not supplied; the located text does not say whether the new notes are guaranteed. Management says the exchange "reduced our secured debt and refinanced a portion of our near-term maturities" (Q3 10-Q page:50, Management Language). The documentary effect is lower secured debt, 8,300 of first lien notes against 9,800 at December 31, 2025 (CP-1 debt table), a longer maturity profile and a higher-coupon replacement for the 5.125% secured notes. The effect on unsecured creditors is that unsecured notes outstanding rise from 2,862 to 4,362 at the expense of the secured tranche; ranking remains: secured notes and revolver ahead of unsecured to the extent of collateral (10-K page:146).

Earlier issue, November 2025. Tenet issued 1,500 of 5.500% senior secured first lien notes due 2032 and 750 of 6.000% senior unsecured notes due 2033, executed a new 1,900 revolver and used proceeds with cash to redeem all 1,500 of 6.250% second lien notes due February 2027 and 750 of 6.125% senior notes due 2028 (10-K page:145 and page:146). The pattern across both issuances is liability management without a priming or non-pro-rata transaction in the supplied text.

Shareholder returns. Repurchases were 1,615 in 9M 2026 and 7.99 million shares (Q3 release page:2); the board added 2,000 of authorization in June 2026 and 1,875 remained at September 30, 2026 (Q3 10-Q page:53). Share count fell from 86,952 thousand to 79,588 thousand. No dividend on common stock appears in the cash-flow statements supplied.

### Ownership, governance and behaviour

| Behaviour row | Evidence | Category | Locator | Dimension and legal capacity, willingness, feasibility |
| --- | --- | --- | --- | --- |
| Maturity extension and secured debt reduction | September 2026 and November 2025 refinancings cut near-term maturities and, in 2026, secured debt | Documentary Fact | Q3 10-Q page:13; 10-K page:145 | Supportive. Capacity: new indenture not supplied. Willingness: documented. Feasibility: liquidity 4,574 and net leverage 2.11x (CP-1 figures) |
| Buybacks funded from operating cash flow | 1,615 repurchased in 9M 2026 with cash falling from 2,883 to 2,674 | Documentary Fact | Q3 10-Q page:4; page:2 | Neutral or Mixed. Capacity: see conflict below. Willingness: documented and expanded by a 2,000 authorization. Feasibility: operating cash flow less capex of 2,961 covered 9M 2026 buybacks in the statements (CP-1) |
| Distributions to partners | Distributions to noncontrolling interests of 614 in 9M 2026 plus purchases of noncontrolling interests of 583 | Documentary Fact | Q3 10-Q page:4 | Neutral or Mixed. Contractual partner economics; terms of put rights Not supplied |
| Transparent reporting | Quarterly reports, releases with reconciliations, segment Adjusted EBITDA and a stated covenant-compliance sentence | Documentary Fact | Q3 10-Q page:51; Q3 release page:8 | Supportive on disclosure; covenant levels are only in the annual report |
| Creditor-adverse actions (priming, uptier, drop-down, non-pro-rata exchange, collateral release) | None found in the supplied text on a search of all seven filings for exchange offers, uptiers, drop-downs and unrestricted-subsidiary language | Insufficient Information (absence in supplied text only) | all sources | No adverse behaviour is documented; the executed documents may permit more than the notes describe |
| Ownership and control | Public company; the control rights and holder base are in Part III and the proxy statement, which are not supplied | Insufficient Information | 10-K page:2 | Not assessable: no sponsor or controlling holder can be named from the supplied text |

### Timeline

| Date | Event | Category | Locator |
| --- | --- | --- | --- |
| January to September 2024 | Sales of hospitals in South Carolina, California and Alabama (the Divested Hospitals); gains of 2.916 billion and sale proceeds of 4.981 billion recognised in 2024; income tax of 855 million arose from the sales | Documentary Fact | 10-K page:139; page:91; page:100; page:97 |
| December 2024 | Palm Springs lease-purchase agreement executed; ownership of certain facilities transfers in May 2057 | Documentary Fact | 10-K page:144 |
| September 2025 | Florida Coast Medical Center opened | Documentary Fact | 10-K page:3 |
| November 2025 | New revolver, 1,500 secured and 750 unsecured notes issued; second lien notes redeemed | Documentary Fact | 10-K page:145; page:146 |
| January 1 and 27, 2026 | Conifer minority redemption effective; Omnibus Agreement entered into with CommonSpirit | Documentary Fact | Q3 10-Q page:5 |
| June 2026 | Board authorized an additional 2,000 of share repurchases | Documentary Fact | Q3 10-Q page:53 |
| August 2026 | Nacogdoches Medical Center South Campus opened in Texas | Documentary Fact | Q3 10-Q page:27 |
| September 2026 | 2,000 of 6.250% notes due 2034 issued; 2027 secured notes redeemed and part of 2028 unsecured notes redeemed | Documentary Fact | Q3 10-Q page:13 |
| After September 30, 2026 (subsequent) | Revenue cycle transition expected to be substantially complete by October 30, 2026; shares outstanding counted on October 23, 2026; third quarter results and a raised 2026 outlook released October 29, 2026 | Management Language for the outlook and transition completion | Q3 10-Q page:30; page:1; Q3 release page:1 |

### Conflicts

- One conflict is logged and not reconciled. The 10-K risk factors say the credit agreement, the letter of credit facility "and the indentures governing our outstanding notes contain" covenants that "restrict our ability to pay dividends, incur additional debt and sell assets" (10-K page:50, quoted in part below), while the debt note says that for the secured notes indentures "there are no restrictions on our ability or the ability of our subsidiaries to incur additional indebtedness, make restricted payments, pay dividends or make distributions in respect of capital stock" (10-K page:148). The two statements are not necessarily inconsistent, because the risk factor also covers the credit agreement, which the debt note says includes limits on debt, asset sales and prepayments, but they leave the issuer's capacity for shareholder distributions unresolved. Downstream effect: any view on buyback sustainability or restricted-payment capacity must be treated as unproven until the executed credit agreement and indentures are read.
- Not a conflict: the 10-K says the Conifer transaction was completed in January 2026, while the quarterly reports say the agreements were entered into on January 27, 2026 with the redemption effective January 1, 2026; these describe an effective date and a signing date. The 1.900 billion headline and the 1.360 billion note receivable differ because 540 million was settled by offset.
- Not a conflict: hospital count rose from 50 at December 31, 2025 to 51 at September 30, 2026, explained by the Nacogdoches South Campus opening in August 2026 (Q3 10-Q page:27).

### Credit translations

1. Revenue durability. Evidence: managed care is 68.5% of hospital net patient service revenue and the top 10 payers provide 66% of managed care revenue (Q3 10-Q page:34 and page:39). Mechanic: a payer-concentrated, price-driven revenue base is stable in volume but exposed to contract renegotiation and to payer-mix erosion, which the filing says began in 2026 as exchange admissions fell. Implication: leverage of 2.65x total and 2.11x net (CP-1 figures) is moderate for the earnings level, but a payer-mix shock would hit EBITDA before it hits liquidity of 4,574. Counter: the conflict above does not affect this view.
2. Cash conversion and non-recurring items. Evidence: 1,472 of contract-termination revenue, a 147 favorable Q3 2026 Adjusted EBITDA effect and 540 of operating cash flow from the settlement (Q3 10-Q page:2, page:49; Q3 release page:2). Mechanic: one-time CommonSpirit items raise reported profit and operating cash flow in 2026 without recurring in 2027, while the receivable pays out through January 2029. Implication: headline earnings and free cash flow overstate run-rate capacity; monitoring should use the sensitivity figures in CP-1.
3. Partner leakage and refinancing posture. Evidence: noncontrolling distributions of 614 in 9M 2026 and a series of refinancings that extend maturities (Q3 10-Q page:4, page:13). Mechanic: cash is paid to physician and other partners and to shareholders before debt reduction, while debt is rolled rather than repaid. Implication: deleveraging is earnings-driven, so any earnings shock reverses it; refinancing risk is low through 2027 and rises from 2028. Counter: the logged conflict leaves restricted-payment capacity unproven.
4. Key uncertainty. Evidence: OBBBA provisions beginning in 2027 and Medicaid disproportionate-share reductions scheduled from October 1, 2027 (Q3 10-Q page:35 and page:36). Mechanic: supplemental payments of 1.107 billion in 9M 2026 depend on state programs that federal changes can cut or delay. Implication: this is the largest unquantified policy risk and the evidence set cannot size it.

### Consumer judgments

| Consumer | Readiness | Take from this handoff | Why it matters | Gap | Required action |
| --- | --- | --- | --- | --- | --- |
| CP-2 | Ready with limitations | Segments, concentrations, payer mix, Conifer terms, refinancing, partner economics, the logged dividend-capacity conflict, behaviour rows | Business risk side of the credit view and the explanation for non-recurring earnings | Ownership, board, indentures and the CommonSpirit documents not supplied | Carry Medium confidence; treat restricted-payment capacity as unproven; use CP-1 sensitivities |
| CP-5 | Ready with limitations | Every locator above plus the one logged conflict and the CP-1 labelled figures | Traceability of the Conifer and refinancing claims and of the management-language rows | Text conversion only; outlook and transition-completion statements are management claims | Trace each Management Language row to its release page and check the conflict quotes against page:50 and page:148 of the 10-K |

## Calculations

No new calculation. CP-1A states figures only as located in the sources or as labelled CP-1 figures; no figure here is derived by this module. One arithmetic cross-check of a stated claim: first lien notes of 8,300 at September 30, 2026 against 9,800 at December 31, 2025 follows from the CP-1 debt table (600 + 1,400 + 1,450 + 2,000 + 1,350 + 1,500 = 8,300 and 8,300 + 1,500 = 9,800), and unsecured notes of 4,362 against 2,862 (1,250 + 362 + 750 + 2,000 and 1,750 + 362 + 750).

## Gaps

| Gap | Severity | Affected consumers | Remediation |
| --- | --- | --- | --- |
| Omnibus Agreement, RCM agreement and the 8-K dated February 2, 2026 not supplied; recurring Conifer revenue from CommonSpirit not disclosed | High | CP-2 | Supply the agreements; until then the earnings effect of the contract loss is Not calculable |
| Indentures, including the Forty-Third Supplemental Indenture, and the credit agreement not supplied; shareholder-distribution capacity unresolved | High | CP-2, CP-5 | Supply executed documents |
| Proxy statement and Part III information (board, holders, control rights) not supplied | Medium | CP-2 | Supply the proxy statement |
| Put-right terms for redeemable noncontrolling interests not supplied | Medium | CP-2 | Supply partnership terms or note disclosure |
| Slide deck and supplemental disclosures not supplied | Low | CP-2 | Supply if narrative strategy evidence is needed |
| Covenant compliance certificate and add-back bridge not supplied (the release reconciliation is the only bridge) | Medium | CP-2 | Supply certificate |
| Events from October 30, 2026 to the cutoff Not supplied | Medium | CP-2, CP-5 | Supply later filings or confirm none |
| No ratings or market data in the context | Low | CP-2 | Not required for this scope |

## Next module

- CP-2: use the business risk rows, the Conifer mechanics, the partner-leakage point and the logged conflict as stated; do not cite shareholder-return capacity as established; take financial figures only from the CP-1 handoff.
- CP-5: validate the Management Language rows (outlook, transition completion, and "reduced our secured debt") against their release or quarterly report pages, and the conflict quotes against page:50 and page:148 of the 10-K; confirm that every figure labelled as a CP-1 figure matches that handoff.
