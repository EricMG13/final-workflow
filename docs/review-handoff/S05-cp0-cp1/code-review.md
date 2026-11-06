SECTION: S05-cp0-cp1   PASS: code-review
COVERAGE: src/deploy_workflow/owners/cp1a.py, src/deploy_workflow/owners/cp1b.py, src/deploy_vii/cp0_workflow.py, src/deploy_vii/cp1_workflow.py, src/deploy_vii/cp1_quality.py read fully / src/deploy_workflow/owners/cp1c.py, src/deploy_workflow/owners/cp1d.py skimmed (parsers, composer entry points, submit/validate/probe, tie-out, bridge parsing and amount stamping read closely) / none not read

The code-review skill was run at `high` on all 7 files (forked execution). It returned 10 candidates. I verified each one, dropped 2 as refuted (listed under "Checked and sound"), merged 1 into C09 and added 2 from my own reading (C01, C04). Repro scripts are in `<section>/cr/`. Every script runs as `cd /home/user/final-workflow && PYTHONPATH=src:.:tests .venv/bin/python <script>`.

### S05-cp0-cp1-C01  [critical] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cp1d.py:501` (parse_bridge); amounts are stamped at `cp1d.py:1027` and onward
- Defect: `parse_bridge` checks only that some page:1 line *starts with* the period basis line (`Basis: FY2025 (January 1-December 31, 2025)`). It never reads the currency or unit clause that follows. Every bridge amount is then recorded as `MILLIONS` in the run currency. cp1c's `_basis` does require the `(currency, "amounts in millions")` clause (round 2 C3).
- Failure scenario: a management bridge page reads `Basis: FY2025 (January 1-December 31, 2025); EUR; amounts in thousands; ...`. The page parses and composes. Its EUR-thousand amounts become USD-million facts (T1D.1 claimed, T1D.2 basis and onward). The module adds no limitation. Wrong currency and a 1000x unit error flow silently into the CP-1D handoff and the deliverables.
- Evidence: `cr/cr_c_bridge_unit.py`. The genuine and forged pages parse to the same items. The forged compute gives `T1D.1.a01.claimed amount_exact '3' unit MILLIONS currency USD` and `T1D.2.a01.basis '1.8' MILLIONS USD`. The limitations do not mention EUR or thousands.
- Fix direction: parse the basis line's clauses, as `cp1c._basis` does, and refuse ("Bridge table not found") unless they hold exactly the run's currency and `amounts in millions`.

### S05-cp0-cp1-C02  [high] [CONFIRMED]  correctness (resume/idempotency)
- Location: `src/deploy_workflow/owners/cp1b.py:482` (submit); the same pattern is in `cp1c.py:3288` and `cp1d.py:2546`
- Defect: `submit` always calls `store.submit_step`. If the process dies after the valid step is journaled but before `store.finish`, nothing can resume it. This includes the case where the second `_validate_step` raises. `submit_cp0_review` and `promote_cp1` both handle exactly this window.
- Failure scenario: a crash happens between the valid-step write and `finish`. A retry with the same payload raises `ValueError("Submit the next module step in order")` because the one-step sequence is already complete. On reopen, `OwnerWorkflow._resume_pending` sees `done >= len(steps)` and raises `_torn("journal")`. The CP-1B/1C/1D attempt can never settle, although its retained valid step could be finished deterministically.
- Evidence: `cr/cr_c03_onestep_resume.py`. It runs cp1b.submit's real control flow on a real journal, with the module identity and validator pointed at CP-0's one-step chain. CP-1B's real fixture needs an 11-26 min CP-1 promotion, so it was not used. Output: `first submit: simulated crash` / `journal after crash: attempt pending ['valid']` / `retry via cp1b.submit pattern RAISES: Submit the next module step in order` / `submit_cp0_review on the same journal resumes: finished ()`.
- Fix direction: as `submit_cp0_review` does, skip `submit_step` when the attempt already holds a valid step with the same payload hash, then recompute and `finish`. Put this in one shared one-step helper.

### S05-cp0-cp1-C03  [medium] [CONFIRMED]  security (integrity)
- Location: `src/deploy_vii/cp1_workflow.py:626-635` (cp1_binding_issues)
- Defect: the receipt's `registers_sha256` and `quality_report_sha256` are compared with the envelope's own values, not with the `CP1Handoff` that promotion recorded in the journal. The envelope's `quality`, `gap_limitations`, `registers_sha256` and `journal` are therefore never tied to the journal. The docstring says the binding defeats "a consistently rewritten pair".
- Failure scenario: someone rewrites `envelope.md`/`envelope.json` with a higher QA confidence, no gap limitations and different registers, and recomputes the receipt's file hashes and `quality_report_sha256`. The module blob is unchanged, so its hash still equals `head.result_sha256`. `read_cp1_envelope`, used by `cp1_render`, `financial_rendering` and `financial_workflow`, accepts the pair and renders the forged QA and limitations.
- Evidence: `cr/cr_c02_envelope_forgery.py`. Genuine export: `qa_status=Restricted score=59 gap_limitations=2 registers=1d35fcf8e1b6`. Forged export: `FORGED ACCEPTED: qa_status=Restricted score=95 band=High gap_limitations=0 registers=000000000000`.
- Fix direction: load the promoted attempt's `quality` step output (`CP1Handoff`), as `write_cp1_envelope` does. Require the envelope's `registers_sha256`, `quality.content_hash()`, `gap_limitations` and `journal == attempt.inputs` to equal the recorded values.

### S05-cp0-cp1-C04  [medium] [CONFIRMED]  correctness (period invariant)
- Location: `src/deploy_workflow/owners/cp1c.py:1206-1241` (_tie_out / _tie_out_settled)
- Defect: the issuer line of the peer sheet is compared with CP-1's LTM ratio without checking that its period end is CP-1's period end. The difference is stamped with CP-1's period and Python writes `Reconciled` or `Differs`.
- Failure scenario: the peer summary's issuer line is dated `2023-06-30` and CP-1 is `LTM Q4 25: 2025-01-01 to 2025-12-31`. T1C.6 still reports `difference 0` with period `LTM Q4 25` and result `Reconciled`. A tie-out across different periods is presented as reconciled. When the figures differ, it reads `Differs` with no period caveat.
- Evidence: `cr/cr_c_tieout_period.py`. The issuer row's period_end is shifted to 2023-06-30 after parsing, which is equivalent to such a page. Output: `T1C.6.adjusted_ebitda_margin.sheet ... period: Twelve months to 2023-06-30`, `...difference | amount: 0 | period: LTM Q4 25: 2025-01-01 to 2025-12-31`, `...result | text: Reconciled`. No limitation names the mismatch.
- Fix direction: when the issuer line's period end differs from `inputs.basis.ltm_end`, set the difference and result cells to Not compared with a period-mismatch reason. Python must not claim reconciliation.

### S05-cp0-cp1-C05  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/cp1_quality.py:69` (_module_status)
- Defect: `_module_status` returns `restricted` whenever `narrative.limitations` is non-empty. `canonical_narrative` (`narrative.py:444-453`) always fills it with four fixed disclaimer lines, so `complete` cannot be returned. This contradicts the docstring, which says only the module's own findings restrict (decision 0007).
- Failure scenario: a clean CP-1 run has narrative status `candidate`, no gaps and source gate `pass`. It still gets `module_status=restricted`. `assess_quality` caps the score at 59 with `qa_status="Restricted"`, and every promoted CP-1 head gets the `CP-1 QA Restricted` limitation and settles `restricted`, never `accepted`.
- Evidence: `cr/cr_c01_module_status.py`, run on the real promoted synthetic case. Output: `narrative.status=candidate gaps=0 limitations=4 -> module_status=restricted` and, with the boilerplate removed, `limitations=0 -> complete`. Existing tests always expect "Restricted" (`tests/test_financial_workflow.py:1034` caps at 59 unconditionally), so this is not covered.
- Fix direction: base `module_status` on `narrative.status` and gaps only. Do not count the fixed disclaimer limitations, which are not findings.

### S05-cp0-cp1-C06  [low] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cp1b.py:335-337` (_default_pairs)
- Defect: the fiscal year filter uses `str.isdigit()` without the `isascii()` guard that `_prior_year` and `_earlier_series` use, then calls `int()`.
- Failure scenario: `FinancialPeriod` accepts a T4.14 `fiscal_year` text of `2025²`, because `fiscal_year_number` reads 2025. `"2025²".isdigit()` is True and `int()` raises ValueError. This happens in `view()`'s else-branch, outside any mapping, so the `read_inputs` view crashes instead of offering no pairs.
- Evidence: `cr/cr_c05_fiscal_year_digit.py`. Output: `fiscal_year_number accepts: 2025 | isdigit: True | isascii: False`, `_prior_year (guarded): None`, `_default_pairs RAISES: invalid literal for int() with base 10: '2025²'`.
- Fix direction: add `isascii()` to the filter, as the sibling helpers do.

### S05-cp0-cp1-C07  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_vii/cp1_workflow.py:256-283` (_stage_registers)
- Defect: every stage prefix is re-validated, and the readiness prefix runs `canonical_downstream_readiness`. Then `canonical_tables` runs the same full chain again. `cp1_quality_inputs` then round-trips all registers through JSON.
- Failure scenario: each `cp1_registers`, `cp1_register_preview` or `promote_cp1` (via `_quality_stage`) recomputes the narrative, downstream and canonical pipeline twice. On the small synthetic case one `cp1_registers` call takes 11.2 s.
- Evidence: `cr/cr_c07_recompute_count.py`. Output: `one cp1_registers call: {'cp1_workflow->canonical_downstream_readiness': 1, 'canonical_tables->canonical_downstream_readiness': 1} 11.24s`.
- Fix direction: build the registers once from the verified readiness output, or call `canonical_tables` once and check it against the retained stage outputs. Keep the fail-closed comparison.

### S05-cp0-cp1-C08  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_workflow/owners/cp1c.py:2589-2629` and `2955-2987` (calculation_issues / compute / _checked)
- Defect: `compute` calls `calculation_issues`, which runs `_sheet_of` and `_compose`, then runs `_sheet_of` and `_compose` again. `_checked` calls `calculation_issues` before `compute`. `submit` runs `_validate_step` twice.
- Failure scenario: one valid CP-1C submission parses the peer sheet and composes every T1C table, lineage and EV table 6 times.
- Evidence: `cr/cr_c08_compose_count.py`. Output: `compute: {'parse_peer_source': 2, '_compose': 2}`, `_checked path: {'parse_peer_source': 3, '_compose': 3}`.
- Fix direction: have `calculation_issues` return the sheet and the composition it built, and let `compute` and `_checked` reuse them.

### S05-cp0-cp1-C09  [low] [CONFIRMED]  simplification
- Location: `src/deploy_workflow/owners/cp1c.py:3251-3304`, `cp1d.py:2508-2562`, `cp1b.py:464-498`; `cp1c.py:1381`
- Defect: the one-step submit-then-finish body, `_with_rules`, `_bounded`, `_stale_issues` and `_bound_module` are copied almost line for line across cp1b, cp1c and cp1d. `cp1c._limitations` also hard-codes the `THIN_LINE` text instead of using the constant. The `line not in limitations` de-duplication in `_compose` against `_ev_limitations` depends on the two strings staying identical.
- Failure scenario: the C02 fix has to be made three times. If `THIN_LINE` or the literal is edited alone, the module emits duplicate thin-universe limitations.
- Evidence: the helpers are byte-identical (`_with_rules` in cp1c:3251 and cp1d:2508). `cp1c.py:1381` repeats the text of `THIN_LINE` from `cp1c.py:100`.
- Fix direction: move the one-step submit/finish/resume and rule wrapping into one shared helper next to `cp1a.probe_one_step`, and use `THIN_LINE` in `_limitations`.

### Out of scope (one line each, optional)
- `src/deploy_vii/narrative.py:444-453` holds the fixed limitations that C05 trips over. The root cause is the consumer in `cp1_quality.py`, so it is reported there.

### Checked and sound (short bullets: what you attacked that held)
- Skill candidate `cp1a.probe_one_step` (StopIteration from `next()`, and a stale head compared with `head_module`): refuted in practice. The only caller (`owner_workflow._verify_settlements:3405`) probes head attempts only, after checking `current_inputs == attempt.inputs`, so the head always exists and is never stale there.
- Skill candidate that `cp1c.parse_peer_source` and `cp1d.parse_bridge` reject a trailing blank line: dropped. The strict 7-field and 4-field rule is the documented table rule (rulings 1C4, 1D4). Supplied page representations carry no terminal LF (case manifest `raw_rule`), and plain-text files become `line:N` spans, not `page:1`.
- `promote_cp1` and `submit_cp0_review` crash windows: both resume from the retained valid step and recompute before `finish`.
- `_recheck_handoff`/`write_cp1_envelope`: the export re-renders the promotion-time envelope and checks the recorded hashes before writing. An existing destination is refused (`exist_ok=False`).
- `is_qa_blocked` regex: built from `re.escape` over `Band` and full-matched. Bands with spaces work.
- cp1c amount and date tokens: ASCII-only regexes, a check that the period end is a real calendar date, and `Not stated` kept as missing (never 0). The Basis clause is checked against the run currency and millions.
- cp1d `_bridge_amount`: `Not stated` stays missing, and the 38-digit bound is enforced.
- `cp1_quality._lineage_basis`: register kinds it does not list raise an error (fail closed). Estimated and Proxy amounts cap at estimate, and amounts with no value are recorded as missing.
