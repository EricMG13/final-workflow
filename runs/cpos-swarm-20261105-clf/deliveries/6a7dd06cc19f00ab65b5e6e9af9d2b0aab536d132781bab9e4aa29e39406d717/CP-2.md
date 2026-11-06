# CP-2 — Fundamental credit synthesis: CLEVELAND-CLIFFS INC. (clf)

## Request

- Issuer: CLEVELAND-CLIFFS INC. (issuer id `clf`, NYSE: CLF), as of 2026-11-05, information cutoff 2026-11-05. Reporting currency USD; amounts are US$ millions unless a row says otherwise. Current period Q3 2026; prior period FY2025 (context `run`).
- Run: `clf-2026-11-05-credit_snapshot-host`, pathway `credit_snapshot`, requested modules CP-1, CP-1A, CP-2 and CP-5. This is CP-2, the fundamental credit synthesis.
- Execution: host session. No provider was called.
- Reader question: what is the fundamental credit view, and which strengths, weaknesses, findings and risks drive it? Decision drivers: business risk (from CP-1A), financial risk and liquidity (from CP-1 figures), and the gaps that limit both.
- Evidence rule: the basis is upstream only. This answer reads no source text and quotes none. Every figure is a CP-1 or CP-1A figure, cited by the handoff section that holds it, or a calculation shown in `## Calculations`. Page locators from the issuer filings are not repeated here; they are in CP-1 and CP-1A.
- Category tags: Documentary Fact (a CP-1A Documentary Fact row or a CP-1 figure states it), Management Language (management's characterisation carried by a CP-1A row, qualified, not adopted), Analyst Interpretation (reading of the cited basis), Insufficient Information (basis missing; the missing datapoint and why it matters are stated).
- Prohibited and not done: no peer ranking, no instrument recommendation, no recovery conclusion. Recovery prospects appear only as a mechanic.

## Sources

Issuer sources pinned for this run (this answer relies on them only through the handoffs below):

| Source | sha256 |
| --- | --- |
| 10-K_2025-12-31_clf-20251231.htm.jsonl | 4c221bc0965bff2fddf7c4bff630fa79a69227de30709426ec9a8c89ce97e2df |
| 10-Q_2026-03-31_clf-20260331.htm.jsonl | cdb78421e299c29e406bbc729a020af9f5e9e2600a8725769f4fc9cce3f48238 |
| 10-Q_2026-06-30_clf-20260630.htm.jsonl | e0ba1bee447b92cbe2b9ad67268169c4ba2e392089bcf206be2b86a11c01f94b |
| 10-Q_2026-09-30_clf-20260930.htm.jsonl | c3188e1da0b49175580c8c9484ba8f4a1c413725f4f518851b880884f79957d1 |
| EX-99.1_2026-04-20_clf-202603318xkex991.htm.jsonl | b9c8fc8d9b4361337a220b73ac602738ac2f0a283bbd73c7b1429c171ac6000c |
| EX-99.1_2026-07-23_clf-202606308xkex991.htm.jsonl | 6e73622f8701012d98293b6d350054a601691c0c525be23eff4b4255d0c4ab32 |
| EX-99.1_2026-10-19_clf-202609308xkex991.htm.jsonl | e6cabc90a6962f04fc1da1253ad4fc1e70365df28408b401d69ed58092c0c0e1 |
| context | 9824d18b9e3851ae3ee2ee1eb294b36a7465c031f02ec1e26c0d1341d4ae46e3 |

Supplied handoffs:

| Module | sha256 | Use |
| --- | --- | --- |
| CP-0 | a3ac66d14ed58e324a2e51f64f8df6ffab5558cd2acad9a6736446039b68520e | Source readiness; status READY_WITH_LIMITATIONS for this module; inherited limitations: no executed debt documents, ratings or market data; earnings presentations not supplied |
| CP-1 | febe06aea238831d2c068e9106ca38dc5907ecb1605c542b2cdb6b84313cc844 | Financial base: chart data (leverage, interest cover, liquidity, debt maturities), financials and credit metrics, debt register, liquidity build, claims outside debt, calculations |
| CP-1A | 310fc2953d3ffb8e3cbbb069d2eb18d26a5197d7f3356b5971f1ef80566e3459 | Business and transaction context: company and operating model, company profile, transaction summary, governance register, timeline, credit translations, conflicts |

Consistency check across the handoffs: no numeric inconsistency was found between CP-1 and CP-1A. CP-1A's two corrections to CP-0 and CP-1 are adopted here: general asset-sale processes were described in the 10-K and the first-quarter 10-Q although the specific property sale is not, and CP-1's table of claims outside debt omitted the Stelco employee benefit commitment and the MinnTac purchase option price. CP-1A also logged that the closure wording for three Pennsylvania and Illinois sites differs between the 10-K and the 10-Q; this answer does not rely on either wording.

## Findings

### Reader summary

| Bottom line | Confidence | Main limitation |
| --- | --- | --- |
| Cleveland-Cliffs' credit is a leveraged cyclical recovery: total debt to LTM Adjusted EBITDA of 7.93x, interest cover of 1.84x on cash interest and liquidity of $3,246 million, with no senior note due before 2029 but a 2028 ABL. | Medium | Ratings, covenant terms, indentures, ownership and the sources of expected debt reduction are not supplied, and the improved view rests on one strong quarter. |

| Finding | Creditor impact | Confidence |
| --- | --- | --- |
| LTM Adjusted EBITDA of $972 million compares with $37 million for FY2025; leverage fell from 25.20x to 7.93x since March 31, 2026, mainly through earnings rather than repayment. | The deleveraging is real but early and price-dependent, so a reversal in steel prices would quickly reverse it. | High |
| Liquidity is $3,246 million and the nearest maturity is the $834 million ABL due 2028; senior notes start maturing in 2029 at $1,268 million. | Near-term refinancing risk is low, but notes due 2029 to 2034 total $6,643 million and need earnings to hold. | High |
| Interest cover is 1.84x on cash interest and 1.61x on net interest expense on an LTM basis. | Thin cover leaves little cushion for an earnings reversal; excluding non-cash pension credits lifts leverage to 10.80x. | Medium |
| Operating cash flow less capital expenditure was negative $332 million in nine months 2026, and expected fourth-quarter debt reduction relies on unverified property sale proceeds. | Repayment capacity is unproven, and the POSCO agreement and asset sales are unquantified, so no deleveraging source can be relied on. | Medium |
| The business is cyclical and automotive-linked, with about 35-40% of flat-rolled shipments on fixed price contracts and labor agreements expiring in 2026. | Margins swing with steel prices and contract resets, and labor or contract outcomes could affect cash flow and ABL availability. | Medium |

### Credit view

The fundamental credit view is of a leveraged, cyclical steel producer in the early stage of an earnings recovery, with adequate liquidity and a back-ended maturity profile but thin interest cover and no verified source of near-term debt repayment. Leverage at September 30, 2026 was 7.93x total debt and 7.85x net debt to LTM Adjusted EBITDA of 972, down from 25.20x and 25.05x at March 31, 2026, and the improvement came from quarterly Adjusted EBITDA rising from 95 to 286 to 612 across 2026 while debt principal moved only from 7,837 to 7,712. Liquidity of 3,246 is the sum of cash of 77 and ABL capacity of 3,169, set by a borrowing base that moves with receivables and inventory. The ABL, at 834, is the only maturity before 2029 and is secured; the nine unsecured note series follow, with 1,268 due in 2029. Interest cover of 1.84x on cash interest and 1.61x on net interest expense is thin, and Adjusted EBITDA includes non-service pension and OPEB credits worth 258 over the LTM, which are non-cash. The business risk is tied to steel prices, automotive contract resets, labor agreements expiring in 2026 and a footprint that has been trimmed through idlings. Three potential transactions (POSCO, property and non-core asset sales, and the MinnTac option) are unquantified or unresolved and are treated as unverified rather than as support. The view is Analyst Interpretation with Medium confidence. It is not an instrument view and states no recovery outcome.

### Credit assessment

| Dimension | Assessment | Category | Basis (handoff section) | Confidence |
| --- | --- | --- | --- | --- |
| Business risk | Moderate to elevated: strong vertical integration and an automotive franchise, offset by price cyclicality, labor renewals and idled capacity | Analyst Interpretation | CP-1A Company and operating model; Credit translations | Medium |
| Financial risk | High: 7.93x total and 7.85x net debt to LTM Adjusted EBITDA; falling quickly on earnings | Documentary Fact for the ratios; Analyst Interpretation for the grade | CP-1 Chart data: leverage; Financials and credit metrics | Medium |
| Liquidity | Adequate: 3,246 including ABL capacity of 3,169; no committed facility maturing within twelve months of September 30, 2026 | Documentary Fact | CP-1 Chart data: liquidity; Liquidity build and covenant status | High |
| Refinancing | Back-ended: only the 834 ABL before 2029; 6,643 due in 2029 to 2034 | Documentary Fact | CP-1 Chart data: debt maturities | High |
| Debt service | Thin: 1.84x on cash interest, 1.61x on net interest expense | Documentary Fact | CP-1 Chart data: interest cover; Calculations | Medium |
| Structure and creditor control | Unsecured notes sit behind a secured ABL; management cites about 3,000 of secured note capacity; indentures not supplied | Documentary Fact for the ABL ranking; Management Language for the capacity | CP-1 Debt register; CP-1A governance register | Medium |
| Covenant headroom | Not calculable: the springing fixed charge test of 1.0 to 1.0 was not applicable; trigger and definition not supplied | Insufficient Information | CP-1 Liquidity build and covenant status | Not assessable |
| Governance and ownership | Public company; no sponsor identified; documented actions lean supportive of creditors (buybacks stopped after 2024; equity raised in 2025 to repay the ABL); holder list not supplied | Documentary Fact for the actions; Insufficient Information for ownership | CP-1A governance register; Company profile | Medium |

### Thesis

Cleveland-Cliffs is a leveraged cyclical steelmaker whose creditworthiness now depends on holding the 2026 earnings recovery long enough to turn a thin interest cover and 7.93x leverage into real debt reduction, while liquidity of 3,246 and a 2029-weighted maturity profile give it time to do so.

### Key findings

Leverage fell sharply but through earnings, not repayment. LTM Adjusted EBITDA of 972 replaced 37 for FY2025 as the denominator, with quarterly Adjusted EBITDA of 95, 286 and 612 in 2026 (CP-1 Chart data: leverage; Calculations). Because the LTM window still contains weak 2025 quarters, each strong quarter lowers the multiple mechanically, so the 7.93x level is a transition value. If Q3 2026 earnings were annualized, an illustration only, total debt to Adjusted EBITDA would be 3.15x, and the gap between that and 7.93x shows how much of the credit view depends on the recovery persisting. Debt principal fell only from 7,837 at March 31, 2026 to 7,712 at September 30, 2026. Category: Documentary Fact for the figures, Analyst Interpretation for the reading.

Interest cover is thin and earnings quality needs a caveat. Cover is 1.84x on cash interest of 529 and 1.61x on net interest expense of 604 over the LTM (CP-1 Chart data: interest cover). Adjusted EBITDA includes non-service pension and OPEB credits of 258 over the LTM, equal to 26.5% of Adjusted EBITDA, and these are non-cash while cash pension and OPEB payments were 116 in nine months 2026; excluding them gives leverage of 10.80x (CP-1 Interpretation; Calculations). LTM Adjusted EBITDA could fall by about 45.6% before cover on cash interest reached 1.0x, and EBITDA less capital expenditure covers cash interest only 0.70x. The mechanism is that capital expenditure and interest together absorb more than operating earnings, so debt cannot fall from operations alone until earnings rise further. Category: Analyst Interpretation on documented figures.

Cash conversion is the weak point. Operating cash flow less capital expenditure was negative 332 in nine months 2026 and negative 485 over the LTM, but positive 72 in Q3 2026 (CP-1 Financials and credit metrics). Receivables rose in a rising-price phase (CP-1A Company and operating model, working capital row), so earnings growth was partly absorbed by working capital. Implication: ABL borrowings of 834 remain well above the 452 at December 31, 2025, and liquidity of 3,246 is below the 3,270 at December 31, 2025, despite the earnings recovery. Category: Documentary Fact and Analyst Interpretation.

Liquidity is adequate and refinancing is back-ended. Cash of 77 and ABL capacity of 3,169 give 3,246, and the only maturity before 2029 is the 834 ABL, due June 2028 or earlier if certain other material debt is near maturity (CP-1 Debt register). The senior notes total 6,878 across nine series, with 1,268 due in 2029 and 6,643 across 2029 to 2034, equal to 86.1% of total debt principal (Calculations). The mechanism is that ABL availability depends on a borrowing base of receivables, inventory and mobile equipment, so liquidity moves with working capital and steel prices, not only with the commitment of 4,750. Category: Documentary Fact.

Structure favours secured lenders, and capacity to add more exists. The ABL has first priority on receivables, inventory and certain mobile equipment and second priority on substantially all other assets, while the notes are unsecured and guaranteed only by domestic subsidiaries (CP-1 Debt register; CP-1A governance register). Management states about 3,000 of secured note capacity (Management Language, carried by CP-1A) that could add debt ranking ahead of the unsecured notes, but no use of it is documented and the indentures are not supplied. Loss-given-default mechanic: priority of claim, not an expected recovery, is what this evidence supports; no recovery outcome is stated. Category: Documentary Fact and Management Language.

Deleveraging sources are management language. Management expects a major debt reduction in the fourth quarter from free cash flow and property sale proceeds, a fourth quarter Adjusted EBITDA of about 715 and 2027 Adjusted EBITDA above 4,000 (CP-1 Latest quarter and events after). With net debt of 7,635 held constant, annualizing the 715 guidance would give net debt to Adjusted EBITDA of 2.67x and the 4,000 outlook would give 1.91x (Calculations, illustrations only). The POSCO Memorandum of Understanding is non-binding and subject to definitive terms, the asset sale processes disclose no buyer, price or timing, and the identity of the property sale is not disclosed (CP-1A Transaction summary). The leverage target is worded differently in two releases (CP-0 conflict 2). Category: Management Language; the illustrations are Analyst Interpretation.

Other claims on cash sit outside the debt figure. Finance lease liabilities of 402 at December 31, 2025, unconditional purchase obligations of 13,954 at December 31, 2025, surety instruments of 336 and an employee benefit commitment of 158 at September 30, 2026 are all outside the 7,712 of debt (CP-1 Claims outside the debt figure; CP-1A Transaction summary). Including finance leases of 402, mixed-date, debt to Adjusted EBITDA would be 8.35x. A potential cash call of 500 if Stelco exercises its MinnTac option by January 31, 2027 would reduce liquidity to 2,746 if met from existing liquidity, an assumption (Calculations). Category: Documentary Fact; sensitivities are Analyst Interpretation.

### Strengths and weaknesses

Strengths. Liquidity of 3,246, with the 834 ABL as the only maturity before 2029, gives time to execute the recovery, and the 2027 notes were redeemed in October 2025 (CP-1 Chart data; CP-1A Transaction summary). Vertical integration supplies most iron ore, coke, scrap and direct reduced iron internally, which the issuer says makes costs more predictable (Management Language), and the automotive franchise is 30% of 2025 revenue, with about 35-40% of flat-rolled shipments on fixed price contracts that give partial visibility (CP-1A Company and operating model). The loss-making slab contract that was about 10 percent of sales volume expired in December 2025, and CP-1A records a favorable mix effect of about 100 in Q3 2026 Steelmaking revenue. Documented behaviour toward creditors leans supportive: no buybacks since 2024 and a 2025 equity offering of 75 million shares that repaid ABL borrowings (CP-1A governance register). Earnings momentum is documented: quarterly Adjusted EBITDA of 95, 286 and 612, with price the main driver (CP-1A operating model, price and volume effect row). Category: Documentary Fact except where marked Management Language.

Weaknesses. Leverage of 7.93x total and 7.85x net debt to LTM Adjusted EBITDA and interest cover of 1.84x leave little margin, and the improvement rests on one strong quarter against a weak 2025 base. Adjusted EBITDA includes non-cash pension credits worth 258 over the LTM, and cash flow after capital expenditure was negative 332 in nine months 2026. The business depends on steel prices and automotive contracts, labor agreements at most steel sites and all iron ore mines expire in 2026 with negotiations ongoing, and six operations were idled or closed in 2025 with further idlings in 2026, creating idle costs that Adjusted EBITDA excludes (CP-1A Company and operating model; Credit translations). The ABL is secured and ranks ahead of the unsecured notes, management cites about 3,000 of secured note capacity, and guarantors are domestic subsidiaries only. Covenant headroom, indentures, ratings, ownership and customer concentration are not supplied. Category: Documentary Fact and Analyst Interpretation; missing items are Insufficient Information.

### Key credit risks

| # | Risk | Mechanic | Credit implication | Severity | Category | Basis |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Earnings reversal with high leverage | A fall in HRC or contract prices reduces LTM Adjusted EBITDA, which the 7.93x multiple and 1.84x cash interest cover depend on | Default risk rises quickly: a drop of about 45.6% in LTM Adjusted EBITDA would take cash interest cover to 1.0x | Critical | Analyst Interpretation | CP-1 leverage and cover tables; Calculations |
| 2 | Cash conversion and working capital | Rising prices build receivables before cash is collected, and capital expenditure guidance is unreconciled between 700 and 1,000 | Debt reduction lags earnings; ABL borrowings stay higher and liquidity lower than at December 31, 2025 | Material | Analyst Interpretation | CP-1 Financials; CP-1A operating model |
| 3 | Unverified deleveraging sources | Fourth-quarter debt reduction depends on free cash flow and an unidentified property sale; the POSCO Memorandum of Understanding is non-binding | Leverage targets cannot be relied on; monitoring should track filings after October 20, 2026 | Material | Management Language | CP-1A Transaction summary |
| 4 | Structural subordination and secured capacity | Secured ABL ranks first on its collateral and second on other assets; about 3,000 of secured note capacity could add senior debt | Loss given default for unsecured notes is sensitive to use of secured capacity; no use is documented and indentures are not supplied | Material | Documentary Fact; Management Language | CP-1 Debt register; CP-1A governance register |
| 5 | Labor and operating disruption | Agreements at most steel sites and all iron ore mines expire in 2026; idled capacity carries idle costs outside Adjusted EBITDA | A stoppage or cost step-up would hit margins and cash flow in an integrated system | Material | Documentary Fact | CP-1A operating model |
| 6 | Earnings quality | Non-service pension and OPEB credits of 258 sit inside LTM Adjusted EBITDA | Cash earnings are lower than reported; leverage is 10.80x without the credit | Material | Analyst Interpretation | CP-1 Interpretation |
| 7 | Contingent cash calls | MinnTac option at 500 exercisable to January 31, 2027; employee benefit commitment of 158; purchase obligations of 13,954 at December 31, 2025 | Potential liquidity use of up to 500 beyond operations; commitments reduce flexibility | Minor to Material | Documentary Fact | CP-1A Transaction summary; CP-1 Claims outside debt |
| 8 | Covenant opacity | The only covenant described is a springing fixed charge test that was not applicable; its trigger and definition are not supplied | Headroom cannot be monitored; a liquidity fall could activate a test whose terms are unknown | Material | Insufficient Information | CP-1 Liquidity build and covenant status |

### Evidence quality and inherited limitations

All figures are drawn from filed statements and releases through CP-1 and CP-1A. Management outlook statements (fourth-quarter Adjusted EBITDA about 715, 2027 above 4,000, leverage target) are Management Language and are used only in labelled illustrations. CP-0 status for this module is READY_WITH_LIMITATIONS; CP-1A's readiness judgment of this module is READY_WITH_LIMITATIONS; no Critical gap or Critical disclosure signal from CP-1A restricts this module beyond the limits listed in `## Gaps`. Confidence is therefore Medium and not High.

## Calculations

All inputs are CP-1 or CP-1A figures in US$ millions unless stated. Ratios are rounded half-even to two decimals; percentages to one decimal.

| Figure | Formula and inputs | Result |
| --- | --- | --- |
| Total debt / LTM Adjusted EBITDA, Sep 30, 2026 | 7,712 / 972 (CP-1) | 7.93x |
| Net debt / LTM Adjusted EBITDA | 7,635 / 972 (CP-1) | 7.85x |
| Cover on cash interest | 972 / 529 (CP-1) | 1.84x |
| Cover on net interest expense | 972 / 604 (CP-1) | 1.61x |
| Liquidity | 77 + 3,169 (CP-1) | 3,246 |
| Notes due 2029 to 2034 | 1,268 + 750 + 1,175 + 1,425 + 900 + 1,125 (CP-1 debt maturities) | 6,643 |
| Share of total debt principal due 2029 to 2034 | 6,643 / 7,712 | 86.1% |
| Senior notes total | 7,712 - 834 | 6,878 |
| Fall in LTM Adjusted EBITDA before cash interest cover reaches 1.0x | (972 - 529) / 972 = 443 / 972 | 45.6% |
| EBITDA less capital expenditure over cash interest | (972 - 601) / 529 = 371 / 529 | 0.70x |
| Non-service pension and OPEB credits as share of LTM Adjusted EBITDA | 258 / 972 (CP-1: 223 + 192 - 157 = 258) | 26.5% |
| Total debt / Adjusted EBITDA excluding the pension credit | 7,712 / (972 - 258) = 7,712 / 714 (CP-1) | 10.80x |
| Debt plus finance leases over LTM Adjusted EBITDA, mixed dates | (7,712 + 402) / 972 = 8,114 / 972; finance leases are as of December 31, 2025 | 8.35x |
| Illustration: annualized Q3 2026 Adjusted EBITDA | 7,712 / (612 x 4) = 7,712 / 2,448 (CP-1) | 3.15x |
| Illustration: net debt over annualized management fourth-quarter outlook | 7,635 / (715 x 4) = 7,635 / 2,860; 715 is management guidance, not a reported figure | 2.67x |
| Illustration: net debt over management 2027 outlook | 7,635 / 4,000; 4,000 is the management floor "above 4,000", not a forecast | 1.91x |
| Adjusted EBITDA needed for 2.5x net debt at current net debt | 7,635 / 2.5 | 3,054 |
| Liquidity after a MinnTac option payment, if met from existing liquidity | 3,246 - 500; an assumption, not a statement of intent | 2,746 |
| Liquidity change since December 31, 2025 | 3,246 - 3,270 (CP-1) | -24 |
| ABL borrowings change since December 31, 2025 | 834 - 452 (CP-1) | 382 |

Illustrations use constant net debt and are not forecasts. They show what the management outlook would imply, not what will occur.

## Gaps

| Gap | Why it matters | Affects | Severity | Action |
| --- | --- | --- | --- | --- |
| Indentures, ABL credit agreement and covenant certificate not supplied; springing covenant trigger and fixed charge definition not printed; headroom Not calculable | Covenant-based monitoring and structural analysis cannot be done | Covenant headroom, structure, CP-5 | Material | Supply executed documents |
| Ratings, market capitalization, quotes and peers not supplied | No external view of default risk or market access | Assessment confidence | Minor for this scope | Keep as Not supplied |
| Ownership: holder list and control rights not supplied; no sponsor identified | Support behaviour and control rights cannot be assessed beyond documented actions | Governance | Material | Supply the proxy statement |
| Customer names and concentration not disclosed | Size of contract and customer loss risk cannot be stated | Business risk | Material | Supply if available |
| POSCO agreement terms, the property sale, other asset sales and the MinnTac exercise decision not disclosed | Deleveraging and contingent cash calls cannot be quantified | Financial risk, liquidity | Material | Supply later 8-Ks |
| Events from October 20, 2026 to 2026-11-05 not supplied | The view may be stale for recent events | All | Material | Supply later 8-Ks or confirm none |
| Lease balances, pension funded status and purchase commitments only as of December 31, 2025; the third-quarter purchase commitment table is absent from the extracted text | Other claims at the latest date cannot be stated | Financial risk | Minor | Use year-end values with date labels |
| Adjusted EBITDA is a management measure and includes non-cash pension credits; net debt and the leverage target are not defined by any filing | Reported leverage can be read differently by definition | Financial risk | Material | Show reported and ex-credit multiples |
| Unreconciled differences: capital expenditure outlook horizons; closure versus idling wording; strategy wording change on sell-side processes; leverage target wording | Narrative reliance is limited | CP-5 | Minor | Keep as logged conflicts |
| Only one strong quarter supports the improved leverage; guidance is management language | The recovery may not persist | Assessment | Material | Re-run with the next quarter's filing |

## Next module

- CP-5: review the evidence trace of the key findings, the credit assessment table and the key credit risks. Check that each cited figure resolves to a CP-1 or CP-1A section and that illustrations built on management outlook are labelled. Check that the 45.6%, 0.70x, 26.5%, 8.35x, 2.67x and 1.91x figures follow from the Calculations table, and that the mixed-date finance lease figure is labelled.
- Carry as restrictions: covenant terms and indentures not supplied; ratings and market data not supplied; ownership and customer concentration not disclosed; POSCO, property sale and MinnTac items unquantified; events after October 20, 2026 Not supplied.
