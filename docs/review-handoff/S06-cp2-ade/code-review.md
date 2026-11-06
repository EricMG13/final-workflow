SECTION: S06-cp2-ade   PASS: code-review
COVERAGE: 5 files reviewed whole by the code-review skill (forked, effort high): src/deploy_workflow/owners/cp2.py, cp2a.py, cp2d.py, cp2e.py, src/deploy_vii/cp2_synthesis.py. I read cp2.py in full myself and read the cp2a/cp2d/cp2e/cp2_synthesis sections behind each finding / none skimmed only / none not read

Independence note: I gave the forked reviewer the independence constraint before it started. Its output did not mention any adversarial finding. I did not read adversarial.md, the repro folder or docs/review-handoff/**.

### S06-cp2-ade-C01  [high] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cp2e.py:233` (`_rate_shock`), operand read at `:502` (`_row_decimal`), `:548`, `:584` (`operands_of`)
- Defect: CP-2E reads the "Cash interest paid" statement row with its printed sign ("(45)" becomes -45) and never reverses it. It then computes interest after the shock as `i + g` and coverage as `EBITDA / i`. CP-1 stores this outflow as a negative number (ruling A7), and CP-2A negates it ("sign reversed", cp2a.py:252-254). CP-2E does not.
- Failure scenario: a cash flow statement prints interest paid as an outflow in parentheses, which is common. The validator requires `value_text` to be the row's last token exactly, so the model cannot correct the sign. Interest (45) with a 200bp shock on 300 floating gives base coverage n.m. ("cash interest is negative") and interest after the shock of -39, so the shock looks like it reduces interest. Interest (20) with a 1000bp shock gives interest after the shock of 10 and a known coverage after the shock of 20.0x. The correct figures are 50 and 4.0x. These values go into T2F.3, the CP-2E-RATE claims and `cp2e_reader.cov_after`.
- Evidence: script `c01_interest_sign.py` in this section folder, run as `PYTHONPATH=src:. .venv/bin/python …/c01_interest_sign.py`. With token "45": cov_base 4.44, interest_after 51, cov_after 3.92. With "(45)": cov_base not_applicable "cash interest is negative", interest_after -39, cov_after n.m. With "(20)" and 1000bp: `interest_after 10 | cov_after known 20`.
- Fix direction: put the interest operand on an outflow-positive basis (negate a parenthesised or negative cash-interest row, as CP-2A does), or refuse a negative interest row with an explicit issue, before computing `_rate_shock`.

### S06-cp2-ade-C02  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cp2d.py:1712` (`_judgments`), schema at `:100-124`
- Defect: CP-2D requires and checks the analyst's `assessments[].text`, `credit_implication` and `limitation`, plus `minimum_cash.rationale` and `minimum_cash_absence.reason` / `follow_up`, but does not write any of them into the module. T2E.6 keeps only each section's category, and no table, claim or limitation carries the rest. CP-2E (T2F.6) and CP-3C (T3D.6) both carry their analysts' assessment text and credit implication into a table.
- Failure scenario: the model submits a maturity-wall assessment with a credit implication, or an Insufficient Information limitation. The settled CP-2D head, its Markdown handoff and delivery show only "Maturity wall: Analyst Interpretation". The analytical conclusion and its stated limitation are lost before CP-3C and delivery read the head, and delivery cannot show them without inventing them.
- Evidence: script `c02_cp2d_prose.py` in this section folder (fixture from test_connect_cp2d, real OwnerWorkflow submit, needs `tests` on PYTHONPATH). Output: `submit: valid`. For liquidity_runway, maturity_wall and funding_gap, both text and credit_implication print `present in module: False`, as does `minimum_cash.rationale`. T2E.6 rows are only Horizon, Minimum cash and the three categories. The cases/cp2d-owner oracle has frozen this omission.
- Fix direction: carry each assessment's text, credit implication and limitation, plus the minimum-cash rationale or absence reason, into T2E.6 as analyst_judgment cells (and the limitation into own limitations), and update the oracle.

### S06-cp2-ade-C03  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/cp2_synthesis.py:868` (`credit_synthesis`, claim `T2.1.assessment`)
- Defect: the claim's `limitation` is `submission.assessment.limitation` stored raw, with its `{fact|unit}` figure references unresolved. The same text in the T2.1 cell and in the own limitation is spelled through `_Composer.text`. `prose_issues` checks only `claim.text`.
- Failure scenario: the assessment limitation reads "Leverage of {T4.10.lev|x} rests on LTM figures only." Consumers that show `claim.limitation` as it is stored then display the raw reference syntax where the figure should be: app.js "Limitation", tools/upstream.py, cp5_integrity and cp6_committee.
- Evidence: script `c04_cp2_claim_limitation.py` in this section folder. Output: `claim.limitation : Leverage of {T4.10.lev|x} rests on LTM figures only.`, while the own limitation and the T2.1 cell read `Leverage of 4.20x rests on LTM figures only.`
- Fix direction: store `out.text(limitation)` in the claim, or validate claim limitations as prose like claim text.

### S06-cp2-ade-C04  [low] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cp2a.py:982-985` (`_Composer.tables`), with `_operands` at `:1037`
- Defect: column headers come from the first row's fact labels. T2B.2's "value" facts are labelled with the row label, so the value column of the whole Base operands table is headed "EBITDA".
- Failure scenario: every CP-2A head shows T2B.2 with columns "EBITDA | Source". Cash interest, free cash flow, total debt, cash and net debt all appear under an "EBITDA" header in rendered tables and in any reader that goes by column label.
- Evidence: script `c03_cp2a_t2b2_header.py` in this section folder (needs `tests` on PYTHONPATH). Output: `T2B.2 Base operands columns: [('value', 'EBITDA'), ('source', 'Source')]`. T2B.3, for comparison, has per-column labels.
- Fix direction: add a FIXED_COLUMNS entry for T2B.2, e.g. ("value", "Value") and ("source", "Source").

### S06-cp2-ade-C05  [low] [CONFIRMED]  simplification
- Location: `src/deploy_workflow/owners/cp2a.py:1631`, `src/deploy_workflow/owners/cp2d.py:2278`, `src/deploy_vii/cp2_synthesis.py:~395` (`_stale_issues`)
- Defect: three copies of the stale-input wording exist alongside `cp2h.stale_issues(bound=, current=)`, and they have already drifted. cp2a and cp2h clip the `current_inputs` refusal text; cp2d and cp2_synthesis do not.
- Failure scenario: a long refusal text produces a clipped issue in CP-2A but an unclipped one in CP-2 and CP-2D (`bounded_issues` in `submit_step` still caps it at the journal), and any future wording change must be made in four places.
- Evidence: the source of the four functions, compared side by side (`grep -n "def _stale_issues" -A14`). Only cp2a and cp2h call `clipped`.
- Fix direction: have all four modules call one shared `stale_issues(bound, current)`.

### S06-cp2-ade-C06  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_workflow/owners/cp2a.py:1735-1741` (`_validate_step`), `:1675` (`downside_report`), `:1425` (`compute`)
- Defect: one valid step validates the same submission three times. `_validate_step` calls `validate_downside`, `downside_report` calls it again, and `compute` runs `validate` again. Each pass rebuilds `_inputs`, the CP-1 scans and the pin parsing. In submit, the whole `_validate_step` also runs a second time after `submit_step`. cp2d and cp2_synthesis follow the same pattern.
- Failure scenario: every submit, probe and verifier replay repeats the prose binding, the base-operand scans over all CP-1 facts and the pin checks two to four times. This costs CPU only; the results do not change.
- Evidence: the call chain in the cited lines.
- Fix direction: validate once, then pass the checked inputs into an internal compose function. Keep the public gate for external callers.

### Out of scope (one line each, optional)
- `src/deploy_workflow/owners/cp2h.py` and `cp1d.py` `submit` share CP-2E's pattern of always calling `submit_step`. CP-OS treats that state as torn anyway (see below), so I am not reporting it.

### Checked and sound (short bullets: what you attacked that held)
- Skill finding refuted: CP-2E `submit` lacks the CP-2D resume guard. If the process dies after a valid step but before `finish`, `OwnerWorkflow._resume_pending` raises torn for every single-step module (`done >= len(steps)`), CP-2D included. Window (a), where a pending step is resumed, works through `submit_step`'s own pending-resume branch. No reachable difference.
- Skill finding refuted: T2E.1 copies carry `value_class` "calculated" with no calculation. This is deliberate and frozen in cases/cp2d-owner/expected.json: the twelve-month flows are CP-1 calculated values, and the copies keep their CP-1 citations.
- Skill finding refuted: CP-2A `fcf_to_debt` is missing rather than not_applicable on a quarter base. The `ratio()` helper also puts a missing operand ahead of QUARTER_REASON for every ratio, so a missing base FCF giving "missing" is consistent.
- Not reported: `cp2e_reader` does not gate on head status. Nothing in src calls it (D3 is open), and it returns `status` to the caller.
- Held: CP-2E `_ratio` and `_combine` keep missing distinct from zero (a known zero floating amount gives a known zero gross; a missing floor gives missing). FX shock arithmetic and hedge netting are sound. CP-2D's `submit` payload-identity and resume guards are sound. CP-2 composer spelling of figure references in cells and own limitations is sound.
