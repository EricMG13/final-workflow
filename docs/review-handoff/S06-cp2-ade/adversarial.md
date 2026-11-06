SECTION: S06-cp2-ade   PASS: adversarial
COVERAGE: read fully: src/deploy_workflow/owners/cp2.py, src/deploy_vii/cp2_synthesis.py / mostly read: cp2d.py (calc core, limitations, cells, validation, stage 2 selection, composer, submit; tables/claims 1278-1700 skimmed), cp2a.py (calc core, break points, validation, stage 2, reconciliation, crossings, limitations; composer 878-1000 and 1260-1320 skimmed), cp2e.py (calc core, inputs, validator, stage 2; tables/claims 942-1770 skimmed) / not read: cp2e.py reader (2121-2180), cp2d.py reader (2874-2958)

Repro scripts: R/S06-cp2-ade/repro/ (R = review root). Run as
`cd /workspace/final-workflow && PYTHONPATH=src:.:tests .venv/bin/python <script>`.

### S06-cp2-ade-A01  [high] [CONFIRMED]  control flow / unsatisfiable validation
- Location: `src/deploy_workflow/owners/cp2d.py:1862` (submission_issues, WALL_DATE_ISSUE), with `maturity_date_refs` built only from T4.18 rows in `select_cp1` (`cp2d.py:2185-2189`).
- Defect: the maturity_wall assessment must cite a T4.18 maturity_date fact, but when CP-1 has no T4.18 facility row the set of citable maturity dates is empty, so no submission can ever pass.
- Failure scenario: an issuer with no debt facilities (CP-1 `_facilities` emits T4.18 rows only per `book.facilities`, `model_interface.py:470`), or a CP-1 run that extracted no schedule. Every CP-2D response is rejected with "the maturity_wall assessment must cite T4.18 maturity_date", even an Insufficient Information wall assessment with a stated limitation. CP-2D cannot settle, and each paid attempt or retry is wasted. The Stage 1 core handles these cases (SCHEDULE_MISSING, the known-zero rule for an empty schedule with zero debt), but the validator never lets a submission reach them. The tests cover them only through `compose_bridge` and never through `select_cp1` plus validation.
- Evidence: `repro/r01_cp2d_no_schedule.py` shows the baseline issues as `()`. With the T4.18 schedule removed, and again with zero debt and an empty schedule, `maturity_refs= set()` and the issues are `('the maturity_wall assessment must cite T4.18 maturity_date',)`.
- Fix direction: require the maturity-date citation only when the selection offers at least one T4.18 maturity_date, or exempt an Insufficient Information wall assessment.

### S06-cp2-ade-A02  [high] [CONFIRMED]  periods / row reading
- Location: `src/deploy_workflow/owners/cp2e.py:778-797` (`_Check.row`)
- Defect: the statement-row check takes the row's last token as the FY value. It checks only that the page header ends in the FY column and never that the row has as many values as the header has columns.
- Failure scenario: a row whose FY cell is blank or was dropped in extraction (`Levered free cash flow  2.25  2.25  2.25  2.25` under `Period  Q1 2025 ... Q4 2025  FY 2025`). The validator accepts value_text `2.25`, and T2F.1 records the Q4 2025 quarter value as FCF for `FY 2025: 2025-01-01 to 2025-12-31` (true FY: 9.00). The FCF-after-shock values in the downstream tables use it.
- Evidence: in `repro/r02_cp2e_rows.py` (a2) the issues are `()` and the output is `T2F.1 Levered free cash flow [('2.25', 'FY 2025: 2025-01-01 to 2025-12-31'), ...]`.
- Fix direction: require the row's value count to equal the header's period-column count, and take the value at the FY column's index.

### S06-cp2-ade-A03  [high] [CONFIRMED]  numbers / sign of outflows
- Location: `src/deploy_workflow/owners/cp2e.py:502` (`_row_decimal`) and `cp2e.py:778-797` (`_Check.row`), used by `derive_sensitivity` (`cp2e.py:268`).
- Defect: a "Cash interest paid" row printed as an accounting-parenthesised outflow is accepted and read as negative interest. Nothing rejects or normalises the sign, so the rate shock is added to a negative base.
- Failure scenario: the page prints `Cash interest paid  (1.25) ... (5.00)` (the same pack prints capex outflows in parentheses). CP-2E then publishes interest after a +100 bp shock as a known value of -4.5 instead of 5.5, and -4 instead of 6 at +200 bp, and marks base coverage n.m. as "cash interest is negative". The figure is wrong in sign and magnitude, not shown as a gap.
- Evidence: in `repro/r02_cp2e_rows.py` (b) the issues are `()`, the interest operand is `-5.00`, and the output is `shock 100 ... interest_after Value(state='known', amount=Decimal('-4.5'))`.
- Fix direction: normalise the interest outflow to its absolute value with a recorded sign note (as CP-1's SIGN_NORMALISED does), or refuse a negative interest row with a journaled issue.

### S06-cp2-ade-A04  [high] [CONFIRMED]  units / scale
- Location: `src/deploy_workflow/owners/cp2e.py:778-797` (`_Check.row`), `cp2e.py:739-746` (`_Check.code`), and the stamping in `_materialise` (`cp2e.py:1093`, `MILLIONS_SCALE`).
- Defect: CP-2E never reads the page's unit statement. Every quoted row value and the facility balance are stamped as millions of the quoted reporting currency.
- Failure scenario: a financial source that states "Currency: USD; amounts in thousands." passes validation, and T2F.1 shows `Total debt` 50.00 with unit MILLIONS and scale 1e6, which is 1000x the source. The CP-2D and CP-2A adapters refuse non-million CP-1 facts (`_usd_millions`, `_in_millions`), but CP-2E reads the pack directly and has no equivalent guard.
- Evidence: in `repro/r02_cp2e_rows.py` (c2) the currency quote is `'Currency: USD; amounts in thousands.'`, the issues are `()`, and the output is `T2F.1 Total debt [('50.00', 'MILLIONS', Decimal('1000000')) ...]`. The trigger is narrower on real pages, because `_ROW_NUM` rejects thousands separators.
- Fix direction: require the quoted reporting-currency line, or the page header, to state the unit, and refuse any unit other than millions, as the CP-1 adapters do.

### S06-cp2-ade-A05  [medium] [CONFIRMED]  control flow / resume wedge
- Location: `src/deploy_workflow/owners/cp2d.py:1840-1841` (submission_issues bounds only the sign of minimum_cash), with the crash in `amount_text` (`cp2d.py:851`, `format_value`) reached from `_judgments` via `liquidity_bridge` in `_validate_step` (`cp2d.py:2796-2808`).
- Defect: a finite but huge `minimum_cash.amount` (JSON `1e300`, or the string `"1E+300"`) passes every validator issue, and composition then raises `ValueError: Number is too large to display exactly` inside `submit_step`.
- Failure scenario: a model response with `"amount": 1e300`. `cp2d.submit` raises, the attempt stays `pending` with the step `pending`, and every resume re-validates and raises again, so the ticket can only be interrupted. The module docstring says "nothing that passes submission_issues raises". An absurd `1E+40` also settles without any issue.
- Evidence: `repro/r05_cp2d_huge_minimum.py` prints `1e300 shape: () validator issues: ()`, then `submit raised: ValueError Number is too large to display exactly`, then `attempt after: pending ['pending']`, then `resume raised: ValueError ...`.
- Fix direction: add a validator issue that bounds minimum_cash (digits and exponent, for example to the display limit) so the step is rejected instead of crashing.

### S06-cp2-ade-A06  [medium] [CONFIRMED]  limitation preservation / gap propagation
- Location: `src/deploy_vii/cp2_synthesis.py:427-438` (`_propagation_issues`) and the limitation built at `cp2_synthesis.py:779`.
- Defect: a Critical CP-1A gap counts as "restated" by any gaps row whose cp1a_refs name it. Neither the row's severity nor its text is checked, so CP-2 can downgrade the gap to Minor and replace its wording.
- Failure scenario: CP-1A records the Critical gap `gaps_ledger.g01` "No debt maturity schedule". CP-2 answers with a gaps row of severity `Minor` and gap text "Minor wording point" citing that ref. Validation passes, the T2.12 gaps ledger shows Minor, and CP-2's own limitation reads `Gap (Minor): Minor wording point`. The Signal also carries no detail for gaps_ledger and T2D.7 sources, so CP-2 itself never carries the Critical gap's text.
- Evidence: `repro/r03_cp2_severity.py` prints `signals: (Signal(source='gaps_ledger', ref='gaps_ledger.g01', status='Critical', ...),)`, `issues: ()` and `limitations: ('Gap (Minor): Minor wording point', ...)`.
- Fix direction: require a restating gaps row to carry severity Critical, and have Python add the cited CP-1A gap's own Gap cell to CP-2's limitation instead of relying on the model's wording.

### S06-cp2-ade-A07  [medium] [CONFIRMED]  currency identity
- Location: `src/deploy_workflow/owners/cp2e.py:739-746` (`_Check.code`) and `cp2e.py:2028-2033` (the context comparison runs only when a run context exists).
- Defect: without a run context, `reporting_currency` accepts any `[A-Z]{3}` token that occurs in any quoted line on a financial page. Every money fact is then stamped with that code, and `debt_foreign` is derived from it.
- Failure scenario: the model quotes "There is no revolving credit facility: RCF commitment ..." with code_text `RCF`. Validation passes and all facts carry currency `RCF`. Because the debt currency `USD` differs from `RCF`, the whole facility is treated as foreign and the FX shock produces a known non-zero debt change.
- Evidence: `repro/r06_cp2e_currency.py` prints `issues: ()` and `currencies stamped: ['RCF']`.
- Fix direction: validate the code against a closed ISO 4217 list, require the quote to be a reporting-currency statement (for example "Currency: XXX"), and fall back to the default basis currency check when there is no context.

### Out of scope (one line each, optional)
- `tests/test_connect_cp2d.py::test_module_trace_lists_every_offered_cp1_fact` fails at HEAD: it expects `"19 US$"` and gets `"19 US$ m"`. The shared spelling helper changed and the test assertion was not updated.
- The full owner and pins test run (`tests/test_owner_cp2[ade]*.py`, `test_connect_cp2[de].py`) was still running under shared CPU load when this report was written, so it has no result here. The method tests for cp2a, cp2d and cp2e and `test_connect_cp2a` passed: 1239 passed, with the one failure above.

### Checked and sound (short bullets: what you attacked that held)
- CP-2A stress and break-point algebra, derived by hand: E(1-s), I(1+k), F-Es-Ik, D/E', (D-C)/E', E'/I'. b01 s*=F/E, b02 s*=(E-I)/E, leverage s*=(LE-D)/LE, coverage s*=(E-LI)/E all match the code. Zero or negative denominators become gaps. A quarter base is never annualised. Base reconciliation against CP-1 ratios is exact (same CONTEXT).
- CP-2A operand units: `offered_bases` refuses any known operand that is not millions of the run currency. A missing operand is never 0. DECLINE and LEVEL patterns bound the inputs, and a level of 0 is refused.
- CP-2D arithmetic: missing propagates as the first gap in formula order and never defaults to 0. Undisclosed, conflicting and not-applicable revolver states keep separate reasons. Zero or negative total debt makes the ratio not_applicable. Month arithmetic clamps end-of-month. Pre-D0 maturities become gaps. A non-USD or unstated-currency facility blocks wall totals with no FX conversion. The CP-1 adapter refuses non-million or wrong-currency facts and two facts for one binding. NaN, Infinity and the float 1e400 are refused by the schema.
- CP-2D validator: horizon bounds, a negative minimum, both or neither of minimum_cash and its absence, exactly one row per section, digits in text, the forbidden-conclusion list and basis refs outside the view are all enforced.
- CP-2 synthesis: the model cannot introduce numbers. Figures appear only as `{ref|unit}` references to CP-1 `referencable` facts, which Python spells and copies verbatim into `cp1_references`, and bare figures are refused by `prose.issues`. cp1a_refs must be settled catalogue rows. A blocked CP-1A or any signal caps confidence below High. A BLOCKED or absent readiness judgment of CP-2 becomes an own limitation. Inherited limitations come from settlement. An empty required register becomes a missing cell plus an own limitation, not invented content.
- Stale and provenance checks: refusals of `current_inputs` are reported as issues, never swallowed (CP-2, CP-2D, CP-2A).
- CP-2E quote checks: a figure must occur once, unsigned, and labelled in the quote. The page context is checked so a quote edge cannot truncate a longer number. The facility balance cannot exceed total debt, and shock bounds and strictly increasing order are enforced.
