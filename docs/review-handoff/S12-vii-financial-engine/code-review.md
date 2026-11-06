SECTION: S12-vii-financial-engine   PASS: code-review
COVERAGE: 28 files read fully by the code-review skill's forked reviewer, which ran at high and reviewed whole files (there is no diff). I read these fully while verifying: model/statements.py, model/debt.py, model/_cells.py, model/registers.py, model/frame.py, facility_fx.py, distressed_figures.py. I read these in part: financial_reconciliation.py (1-560), financial_adapter.py, period_reconciliation.py (1-80, 160-440), model/history.py (1-120, 297-555), financial_model.py, financial_periods.py (40-275), statement_extract.py (1-140, 380-420), statement_validation.py (340-408), statement_output.py (15-35). / 0 files not read

Independence note: The skill ran as a fork and was told not to read docs/review-handoff/**, adversarial.md or repro/. Its output does not mention adversarial findings. All my scratch scripts are in c_repro/ in my section folder. I did not open repro/ or adversarial.md.

### S12-vii-financial-engine-C01  [high] [CONFIRMED]  correctness
- Location: `src/deploy_vii/financial_reconciliation.py:302-367` (`_debt`)
- Defect: The source debt check ignores `FacilityObservation.issued_on`. A facility that has no row at a date before its issue date becomes a "Not supplied" term, so DEBT_TOTAL_EX_LEASES is BLOCK for every period before the issuance. The kernel adapter (`financial_adapter._facilities:115-121`) and the period reconciliation that reads its `fac:` cells treat the same facility as 0 with a `facility-issuance:` source.
- Failure scenario: Term loan TL-B is issued on 2025-10-01 and has rows only at 2025-12-31 and 2026-06-30. Validation explicitly supports this shape (`financial_validation.py:205-225`). At 2025-06-30, TL-A is 100 and reported total_debt is 100. `_debt` gives BLOCK with calculated None. The adapter gives TL-B = 0, so the same period would PASS. The two reconciliation reports disagree, and the false BLOCK feeds `model_readiness` (`reconcile_financials` -> BLOCK findings).
- Evidence: `cd /home/user/final-workflow && PYTHONPATH=src:.:tests .venv/bin/python <section>/c_repro/c02_issued_on.py` -> `DEBT_TOTAL_EX_LEASES at 2025-06-30: BLOCK None [('tl-a', 100, None), ('tl-b', None, 'Not supplied')]` and `adapter facility rows at 2025-06-30: [('tl-a', 100), ('tl-b', 0)]`.
- Fix direction: Add one shared helper for "a facility's carrying value at a date" (zero, with the issuance source, when issued_on > end_date and no row exists). Use it in both `_debt` and `financial_adapter._facilities`.

### S12-vii-financial-engine-C02  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/financial_adapter.py:203-224` (`_addbacks`), consumed by `src/deploy_vii/model/statements.py:173-179` (`excluded_addbacks`)
- Defect: For every component-less period where an add-back has no row, the adapter creates a row with `realization_status="NOT_STATED"` and a null amount. This includes balance-sheet PERIOD_END dates. `excluded_addbacks` excludes any add-back with any NOT_STATED row, so with `exclude_unrealised=True` nearly every add-back CP-1 disclosed as REALIZED is dropped.
- Failure scenario: A restructuring add-back of 12 is disclosed only for FY2025 as REALIZED, and the book has four balance-sheet dates and an H1 YTD. The adapter writes NOT_STATED/None rows for all five of those periods. `model_report(..., exclude_unrealised=True)` then leaves the realized 12 out of FY adjusted EBITDA and turns off the comparison with CP-1's stated figure. That is a silently lower adjusted EBITDA in the house variant. No production caller passes True today (`cp1_workflow.py:145` uses the default), so the impact is latent.
- Evidence: `PYTHONPATH=src:.:tests .venv/bin/python <section>/c_repro/c04_addback_notstated.py` -> rows `bs-2024-12-31 NOT_STATED None ... fy-2025 REALIZED 12 ... h1-2026 NOT_STATED None` and `excluded with exclude_unrealised=True: ['restr']`.
- Fix direction: Decide realisation status from CP-1's own rows only, for example by not giving synthesized gap rows a realisation status that counts for exclusion, or by skipping PERIOD_END periods. Keep the null amount, so a missing add-back figure still stays missing.

### S12-vii-financial-engine-C03  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/model/statements.py:157-170` (`_stated`)
- Defect: `_stated` replaces the host cell's note with `DIFFERS` or None. This wipes the notes `calc` put on gross profit, EBIT, EBITDA and adjusted EBITDA: SIGN_NORMALISED, UNSPANNED, and the "why missing" reason. The module docstring and `history` say every sum keeps those notes. The note flows to `ModelValue.value.note` (`financial_periods._value:249`).
- Failure scenario: (a) CP-1 writes cogs positive (+60), and the account cell is noted "sign normalised". Gross profit 40, EBIT 20 and EBITDA 25 all come out with note=None. (b) An FY whose components do not span it gives revenue COMPONENT_MISSING noted "components do not span the period". Gross profit comes out COMPONENT_MISSING with note=None on the FY and LTM columns, so the Model output loses why the figure is missing.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/c_repro/c01_stated_note.py` -> `cogs cell note: sign normalised`, `gross_profit 40 note= None`, `ebit 20 note= None`. Also `FY:FY25 revenue COMPONENT_MISSING 'components do not span the period' | gross_profit COMPONENT_MISSING None`.
- Fix direction: `replace(host, stated=figure, note=join_notes(host.note, DIFFERS if differs else None))`.

### S12-vii-financial-engine-C04  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/statement_extract.py:394-401` (`_is_omitted_candidate`), with `_cells:257`
- Defect: A printed row whose values use a leading minus (`-120  -80`) or a percent sign (`12.5%  10.0%`) is neither returned as data nor listed in `ExtractedTable.omitted`. `_is_omitted_candidate` requires the last token to match `_NUMERIC_CELL`, so the row disappears without any signal. The module's stated purpose for `omitted` is that a lost value is never silent.
- Failure scenario: A European-style statement page prints `Net loss   -120   -80` under a `2025  2024` header. The extraction returns only the other rows and `omitted=()`, so the model never learns that a printed line was dropped. A row whose last value happens to be positive (`-1,234   2,345`) is listed in `omitted`, so the outcome depends on the sign of the last column.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/c_repro/c03_minus.py` -> lines `Revenue`, `Net loss (alt)` only. `OMITTED (OmittedLine(line_no=6, text='Operating result  -1,234  2,345'),)`. The `-120 -80` and `%` rows are missing from both lists.
- Fix direction: Widen the candidate test so any multi-token line whose last token holds a digit (for example `-?[$€£]?\d[\d,.]*%?`) is recorded in `omitted`. Do not parse such values as data.

### S12-vii-financial-engine-C05  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/model/statements.py:476-508` (`pro_forma_column`), with `_PF_TARGETS:118` and `_PF_BLANK:127`
- Defect: The docstring says the PF-LTM debt roll-forward "keeps the LTM's debt raised and non-cash movements, and closes at the pro forma total debt, so it foots". The code does not do this. A `total_debt` adjustment moves `debt_closing`, `debt_non_cash` stays at the LTM residual, and `debt_raised_net` is blanked to NOT_APPLICABLE, so the roll-forward does not foot.
- Failure scenario: LTM opening 100, raised 20, non-cash 5, closing 125, plus a PF refinancing of +50 to total_debt. The PF column shows opening 100, raised n/a, non-cash 5, closing 175, a gap of 70 with no residual. `pro_forma_column` has no callers today, so this is latent.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/c_repro/c06_pf_rollforward.py` -> `PF: debt_opening 100, debt_raised_net (None,'NOT_APPLICABLE'), debt_non_cash 5, debt_closing 175`. `opening + non_cash = 105 vs closing 175`.
- Fix direction: Before this function gets a caller, either recompute `debt_non_cash` as a residual against the PF closing or show the PF adjustment as its own roll-forward line, and keep `debt_raised_net` as the docstring says.

### S12-vii-financial-engine-C06  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_vii/financial_reconciliation.py:194-215` (`_account`, `_balance`), `src/deploy_vii/statement_validation.py:401-408` (`account_outflow`); also called per period x metric in `financial_adapter._accounts:66-70` and per account and per line in `statement_issues:330,344`
- Defect: Every `_account` and `_balance` call rebuilds `effective_accounts(book)`, which constructs a pydantic `AccountObservation` for each linked statement line, then scans the result linearly. `account_outflow` rescans all statement lines on every call. Cost grows as periods x metrics x lines.
- Failure scenario: A book with 40 quarters and 3,480 linked statement lines takes 8 ms per `effective_accounts`, and 8.4 s for 1,040 `_account` calls, which is one pass of the 26 metrics. `reconcile_financials` makes several such passes, and `statement_issues` is quadratic in the number of lines.
- Evidence: `PYTHONPATH=src:.:tests .venv/bin/python <section>/c_repro/c07_perf.py` -> `one effective_accounts: 8.2 ms`, `1040 _account calls: 8.4 s`.
- Fix direction: Build a per-book `{(period_id, metric): Observation}` index and a set of `(period_id, metric)` outflow-magnitude pairs once, and look values up in them.

### S12-vii-financial-engine-C07  [low] [PLAUSIBLE]  efficiency
- Location: `src/deploy_vii/financial_model.py:263-290` (`model_report`)
- Defect: One `model_report` runs `validate_financial_review` twice, because `kernel_registers` (financial_adapter.py:268) is called directly and again inside `historical_report` (financial_periods.py:327). `normalize_facilities` (FX validation plus a hash of every foreign row) also runs again in the adapter, in `historical_report`, in `model_report` itself and in `trace_cells`. `validate_model_report` then repeats all of it.
- Failure scenario: The work grows with citation count and the number of foreign-facility rows on every Model build and every validation. Nothing is wrong, but it is several times slower than needed.
- Evidence: Not timed, because a full `PreparedPack` and `FinancialReview` fixture is needed. The repeated calls were confirmed by tracing the code at the lines cited.
- Fix direction: Validate and normalise once, then pass the registers, normalizations and evidence down to `historical_report`, `_metric_rows` and `trace_cells`.

### S12-vii-financial-engine-C08  [low] [CONFIRMED]  simplification
- Location: `src/deploy_vii/statement_output.py:22-26` (`_SCALE_FACTORS`). The opening-day rule `start_date - 1 day if toordinal() > 1` appears at `financial_reconciliation.py:523-527` and `:618-622`, `period_reconciliation.py:279-283` and `cash_bridge.py:91`.
- Defect: `_SCALE_FACTORS` is a copy of `financial_contracts.STATEMENT_UNIT_FACTORS`, and the opening-balance date rule is written out four times.
- Failure scenario: If one copy changes, the reconciliations read opening balances on different dates, or a statement output scales differently from the contracts.
- Evidence: `grep -n "toordinal() > 1" src/deploy_vii/*.py` finds 4 sites. `financial_contracts.py:77-81` holds the same three factors.
- Fix direction: Import `STATEMENT_UNIT_FACTORS` and add one `opening_day(start_date)` helper.

### Out of scope (one line each, optional)
- None.

### Checked and sound (short bullets: what you attacked that held)
- Dropped one skill finding, period_reconciliation `_source_periods` expanding only the immediate `component_period_ids`. An unspanned construction already has a null reported value and BLOCKs. For nested YTDs the check still compares independent source equations, so I could not show a wrong verdict.
- `facility_fx.normalize_facilities`: it refuses stale, reversed or duplicate quotes, a conflicting rate or amount on a same-date alias gives null, and the arithmetic is exact Decimal under the 38-digit context.
- `_cells.calc` and `history._sum`: missing versus NOT_SOURCED is kept, and a partial sum never becomes a figure except for sparse items, which is by design.
- `debt._opening_debt`: a facility issued after the opening date is not treated as a gap, and a partly written opening stack is COMPONENT_MISSING.
- `_check` in financial_reconciliation: it never forces a difference to fit tolerance, and a structural blocker nulls the calculated value.
- `distressed_figures`: a missing or unsettled fact becomes a gap cell with its G#, never 0, and an incompatible unit raises an error.
