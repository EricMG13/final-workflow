# Host analyst checklist

For an agent answering CP-OS modules in host mode (`cpos_launch --config host`). An accepted
answer cannot be replaced, and the automated check covers structure only. Every rule below comes
from a defect that passed that check in the five-issuer Sonnet pilot of 2026-11-06
(`runs/cpos-launch-swarm-*-001/review.json`) or in the draft reviews of its stopped rerun.

Write each answer to a draft file first. Work through **Before you submit** on the draft, then
copy it to the Answer path.

## While you write

1. **Perimeter.** Name the issuer's reporting entity. When the issuer is a subsidiary in a
   combined filing (American Airlines, Inc. inside American Airlines Group), use the issuer's own
   statements for debt, earnings, leverage and coverage. Give the parent's only as context, and
   label it.
2. **Debt, all of it.** List every instrument with issuer and co-issuer, amount, rate, maturity,
   security and guarantors, as the notes print them. Count series from the table, not from
   memory. Put the maturity wall by year.
3. **Claims outside debt.** Set out lease financing obligations, finance and operating leases,
   pensions and retiree medical, purchase and capacity commitments, factoring and supply-chain
   finance, and litigation or consent-decree funding. For each, say whether it is inside or outside
   the debt figure. Examples: Caesars' VICI and GLPI leases, Chemours' consent decree.
4. **Liquidity.** Compute it from the printed inputs: unrestricted cash plus undrawn facilities,
   net of letters of credit drawn on them, by facility. Show each input and its locator. Note
   facilities that expire within twelve months.
5. **Covenants.** Give each maintenance test, its level and any step-down, the issuer's reported
   figure and the headroom. Say which definition differs from the metric you computed.
6. **Latest quarter and after.** Cover the quarter's financing events, amendments, merger terms
   and milestones, consent decrees, disasters and subsequent events up to the cutoff, with amounts.
7. **Periods.** Label every figure: Q3 2026, nine months 2026, LTM, FY2025, or restated FY2025.
   Do not mix a nine-month amount into a full-year sentence.

## Before you submit

8. **Search before "not supplied".** Before writing "not supplied", "not printed", "not read" or
   "not calculable", search every pinned source's text for the term and its synonyms. For example,
   for letters of credit also search "LC", "EDC" and "standby". Write it only if nothing is found,
   and name the input that is missing. A gap the sources can fill is a defect.
9. **Open every locator.** For each citation, open the cited page or line and confirm the figure,
   note number and wording are there. A page is the source chunk shown as `page:N`, not a printed
   page.
10. **Directions and superlatives.** For every "rose", "fell", "record", "highest", "largely
    undrawn" or "most", find the sentence or the two figures that support it. If none, delete it
    or state the figures.
11. **Recompute.** Recompute every derived number (sums, net debt, ratios, growth, headroom) from
    the cited figures, and check that the inputs share a period and a perimeter.
12. **Consistency.** Check the answer against the upstream handoffs. Where it corrects one, say so
    plainly in this answer; the earlier handoff cannot be edited.
13. **Cutoff.** Make sure nothing dated after the cutoff is used as fact. A future date in a
    contract term is fine when it is labelled as one.
