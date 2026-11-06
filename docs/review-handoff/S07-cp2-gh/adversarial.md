SECTION: S07-cp2-gh   PASS: adversarial
COVERAGE: src/deploy_workflow/owners/cp2g.py, src/deploy_workflow/owners/cp2h.py (read fully) / tests/test_method_cp2g.py, tests/test_method_cp2h.py (helpers used for repros), cp2a.py break/scenario code, context.py ratings validation, execution.submit_step, owner_workflow resume (skimmed) / tests/test_connect_cp2g.py, tests/test_connect_cp2h.py, tests/test_owner_cp2h.py (not read)

What the modules do (from the code). CP-2G is a three-year forward credit model. It starts from CP-1's T4.10 LTM base and seven analyst driver paths, and applies one CP-2A scenario as the downside. It outputs revenue, EBITDA, FCF, a debt and cash roll-forward, liquidity, leverage, coverage and FCF/debt, then tests CP-2A's break register for the first year each break is reached. CP-2H is a ratings-trigger module, not a funding/refinancing module. It parses one agency source (register, combined scale, trigger terms) or a context-file register, tests each trigger against CP-2G's T2H.6 ratios (current and forward headroom, first year reached, counts), computes notch divergence between agencies, and takes the analyst's migration view per agency. Neither module models maturities, maturity buckets or refinancing. CP-2G states this and leaves it to CP-2D and CP-3C, so the maturity-bucket attack surface does not exist in this section.

Baseline: `pytest tests/test_method_cp2g.py tests/test_method_cp2h.py` gives 780 passed.
Repro command for every script: `cd /workspace/final-workflow && PYTHONPATH=src:.:tests .venv/bin/python <script>`. All scripts are in `<review root>/S07-cp2-gh/repro/`.

### S07-cp2-gh-A01  [high] [CONFIRMED]  response validation / wrong break metric
- Location: `src/deploy_workflow/owners/cp2g.py:842-846` (`_metric_check`), `:887-894` (`_break_issues`), `:2030` (`_tests`)
- Defect: the analyst names the metric for each CP-2A watch break. That metric is checked only by reproducing CP-2A's required decline. When the check cannot run, the metric is accepted unchecked (returns `True, cause`) and becomes the metric the break is tested on. The check cannot run when CP-2A stressed a different base period, when CP-2A has no known required decline, or when a base operand is missing.
- Failure scenario: CP-2A's base period is a quarter. The oracle has `Q3 25` and `Q4 25` CP-2A cases, so this is reachable. The analyst swaps b03 to `interest_coverage` (CP-2A: "Total leverage watch level" 2.5x) and b05 to `total_leverage` (CP-2A: "Interest coverage watch level" 2.0x). There are no issues. T2H.7 shows the leverage test tested as coverage. The downside first year for b03 flips from FY2026 to "Not reached by FY2028". CP-4C reads these first years through `cp2g_reader`.
- Evidence: `repro/a01_metric_swap.py` -> `issues: ()`, then `b03 Total leverage watch level | metric: Interest coverage | level: 2.5 | ... down: Not reached by FY2028`. With the correct metric (`repro/probe_cp2g.py`) b03 down is `FY2026`. The only signal is a limitation saying the metric "could not be checked".
- Fix direction: take the metric from CP-2A (expose the watch metric, or read the `T2B.6.*.required_decline` formula or lineage) and refuse a mismatch. If it is unknowable, settle the break as Not calculable rather than computing it on the analyst's unchecked choice.

### S07-cp2-gh-A02  [high] [CONFIRMED]  invented content passes validation (limitations)
- Location: `src/deploy_workflow/owners/cp2g.py:826-829` (`_limitation_issues`), used at `:925, :929, :936`; stored as `Claim.limitation` at `:2390-2391, :2406, :2483`
- Defect: CP-2G checks the analyst's `limitation` texts only for blankness. They get no `prose` bare-figure check, no prohibited-conclusion check and no probability-phrase check. CP-2A (`cp2a.py:661, :706`) and CP-2H (`cp2h.py:1769-1779`) do check limitations. Module validation (`prose.prose_issues`) checks only `claim.text`.
- Failure scenario: `base_drivers.revenue_growth.limitation`, `downside.limitation` or `assessment.limitation` is set to "Management guided FY2026 EBITDA of 41.7 million; the probability-weighted expected value implies the issuer will be downgraded." It passes and is stored verbatim as the limitation of claims T2H.3.revenue_growth, T2H.3.downside and T2H.3.assessment, which delivery renders. The same text as a rationale is refused ("Bare figure: 41.7", "probability-weighted").
- Evidence: `repro/a06_limitation.py` -> `issues: ()`, and three claims carry the text. As a rationale: `('downside.rationale: Bare figure: 41.7', ...probability weighting...)`.
- Fix direction: validate every non-None limitation the way CP-2H's `_limitation` does: `prose.check(text, refs=(), ...)`, `prohibited_issues` and the probability phrases.

### S07-cp2-gh-A03  [medium] [CONFIRMED]  wrong comparison (rating scope/instrument mixed in notch divergence)
- Location: `src/deploy_workflow/owners/cp2h.py:1464-1529` (`_divergence`), `:430-464` (`context_register`)
- Defect: T2R.8 compares any two register rows in notches and names the "Lower rated" agency. It never checks that both rows rate the same thing: the page register's `instrument`, or the context row's `scope` (`issuer` vs `facility`).
- Failure scenario: Alder's issuer rating BB is compared with Brook's senior secured notes Ba1. The result is "1 notch apart, Alder Ratings lower rated", and the claim says "The two agencies' ratings are 1 notches apart". A secured-instrument rating is usually notched above the issuer rating, so the divergence conclusion is wrong. The same happens for a context S&P `issuer` row against a Moody's `facility` row. The scope is mentioned only in a limitation line.
- Evidence: `repro/a03_scope_mix.py` -> `notches known 1`, `lower_rated known Alder Ratings`. `repro/a04_context_scope.py` (b) -> `[('S&P','issuer','BB',12), ("Moody's",'facility','Ba1',11)] notches: 1`.
- Fix direction: compare only rows with the same instrument/scope. Otherwise make notches, lower_rated and outlook_match not_applicable, with the reason.

### S07-cp2-gh-A04  [medium] [CONFIRMED]  analyst conclusion unconstrained by computed outcomes and evidence
- Location: `src/deploy_workflow/owners/cp2h.py:1782-1820` (`_view_issues`)
- Defect: the per-agency `view` is checked only as an enum. It is never compared with that agency's trigger outcomes. `evidence` is checked only for being a quote on some page of any in-scope source, not for concerning that agency.
- Failure scenario: positive case. Alder has three downgrade triggers reached in the FY2026/27 downside and publishes no upgrade trigger. Setting both views to "Upgrade potential" gives no issues, and T2R.7 settles "Upgrade potential". Brook's view can cite only Alder's register line, and Alder's view can cite only a financial-statement line; both still give no issues.
- Evidence: `repro/a02_view.py` -> `downgrade_down: ('t02','t03','t04')`, `issues ... (): ()`, `T2R.7.a01.view 'Upgrade potential'`. `repro/a02b_evidence.py` -> `issues: ()`.
- Fix direction: refuse a direction that contradicts the computed outcomes, at minimum "Upgrade potential" with no upgrade trigger published for that agency, or with downgrade-only reached outcomes and no reached upgrade. Require at least one evidence quote from that agency's own register or terms line.

### S07-cp2-gh-A05  [medium] [CONFIRMED]  breach reported as "Not calculable" (zero/negative denominator)
- Location: `src/deploy_workflow/owners/cp2g.py:319-329, :535-539` (`_ratio`, `_year`) and `:618-650` (`test_breaks`); consumed by `cp2h.py:1258-1263, :1346-1408`
- Defect: a ratio with a zero or negative denominator is settled as missing. Every break or trigger on it then becomes "Not calculable", even when the direction is certain:
  - With positive debt and EBITDA at or below zero, total and net leverage are past any positive "above" level.
  - With zero interest, coverage cannot be "below" a level.
- Failure scenario: the downside is CP-2A's "Total loss of earnings" (decline 1). FY2026 EBITDA is 0 and debt is 50. CP-2G b03/b04 (leverage) become "Not calculable", so the downside first-break claim lists FCF/coverage/liquidity only. In CP-2H, Alder's "Total debt to EBITDA Above 2.75x" and Brook's "Net debt to EBITDA Above 2.25x" downgrade triggers are counted as `not_calculable_down` rather than reached. The `fixture_debt_repaid` case (interest 0 from FY2027) likewise makes both coverage breaks "Not calculable" instead of not reached. Because the oracle pins this behavior, the tests pass.
- Evidence: `repro/a05_total_loss.py` -> `b03 total_leverage Not calculable ... (ZERO_OR_NEGATIVE_DENOMINATOR)`, `CP-2H t01 Not calculable`, `'downgrade_down': ('t02','t03')`, `'not_calculable_down': ('t01','t04','t05')`. `repro/a05b_debt_repaid.py` -> `b02 coverage Not calculable`.
- Fix direction: decide the test from the signs before dividing: positive debt with EBITDA at or below zero means leverage "above" is reached; zero interest with positive EBITDA means coverage "below" is not reached. Keep the ratio cell itself missing. This needs an oracle/ruling change, not a silent edit.

### S07-cp2-gh-A06  [low] [CONFIRMED]  realistic context refused with a misleading reason
- Location: `src/deploy_workflow/owners/cp2h.py:453-457` (`context_register`)
- Defect: the context schema allows one agency to appear with both an `issuer` and a `facility` row (`context.py:611-616` has no uniqueness rule). CP-2H refuses the whole register as "Rating register not found", which blocks CP-2H for the run even though the issuer rows are present.
- Failure scenario: the context has S&P issuer BB, S&P facility BB+ and Moody's issuer Ba2. CP-2H's single issue is "Rating register not found".
- Evidence: `repro/a04_context_scope.py` (a) -> `refused: Rating register not found`.
- Fix direction: select the issuer-scope row per agency (or key the register by agency and scope, together with A03), or refuse with a reason that names the duplicate scope.

### S07-cp2-gh-A07  [low] [CONFIRMED]  outlook compared as raw text
- Location: `src/deploy_workflow/owners/cp2h.py:1442-1461` (`_outlook_match`)
- Defect: context outlooks are free text (not validated in `context.py`) and are compared with `==`, so case and whitespace differences read as different outlooks.
- Failure scenario: S&P "Stable" vs Moody's "stable " gives T2R.8 outlook_match "Different".
- Evidence: `repro/a07_outlook.py` -> `'outlook_match': 'Different'` (both ratings at the same position).
- Fix direction: normalise case and whitespace before comparing, or validate outlook against an enum in the context.

### Out of scope (one line each, optional)
- `owner_workflow._resume_pending` raises `_torn("journal")` for a pending attempt whose only step is already valid (a crash between the valid step and `finish`). CP-2H's `submit` also has no CP-2G-style resume branch, so a resubmit fails with "Submit the next module step in order". Neither path recovers that window.
- CP-2H's page-mode parse rule hard-codes the scale header `Position  Alder Ratings  Brook Credit`. The context path still needs a page:3 terms block in the synthetic format. A real issuer's agency material therefore cannot reach the trigger tests, which is a functional-proof scope limit.

### Checked and sound
- Forecast arithmetic checked by hand on the positive case:
  - revenue x (1+g), EBITDA = revenue x margin x (1-s)
  - interest = opening debt x rate x (1+k)
  - closing debt = opening debt - repayment
  - closing cash = opening cash + FCF - distributions - repayment
  - leverage, coverage and FCF/debt formulas
  - exact decimal context with the Inexact trap. These match the CP-2A shock semantics (`cp2a.stress`).
- CP-2A break-decline recipes (`break_decline`) are identical to `cp2a.break_points`, and both are correctly rounded at 38 digits, so equality reproduces.
- Sign handling: CP-1 outflows are negated once, so a working-capital release stays an inflow in CFO.
- Units: CP-1 and CP-1D books are forced to the run currency at MILLIONS and scale 1e6, otherwise they raise. The CP-2H percent threshold is shifted exactly to a fraction, and headroom is expressed in pp by `scaleb(2)`.
- Periods: forecast years exist only for calendar fiscal years (`require_calendar`; a 52/53-week or July-June base is refused). CP-2H checks every CP-2G T2H.6 fact's unit and period against the run basis. CP-1D in another period is not compared.
- Missing vs zero: missing operands propagate with their root reason in formula order. A known zero stays known. CP-2G `not_applicable`/`missing` copies keep the upstream status and limitation.
- CP-2H source parse: an unknown metric, a malformed threshold, a duplicate term, an agency or position twice, a terms agency that is unrated or absent, a duplicate header line, and an off-calendar date are all refused (fail closed).
- Bare figures and probability or rating-call phrases in rationale and gap text are refused in both modules. Stale upstreams and a refused basis are returned alone. Blocked required upstreams cannot be bound (`current_inputs` + `edge_rule` "block").
