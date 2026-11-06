# Whole-app review: final report

Base commit `a313b50` (main, 2026-11-06). Scope: every `.py/.js/.html/.css/.ps1/.go` file under
`src/`, `apps/` and root `workflow.py`, split into 18 sections (`SECTIONS.md`). Two independent
passes per section (adversarial protocol, then the `code-review` skill at effort high), then one
independent cross-review (model: Fable) over all findings that re-ran every critical and high repro.
Nothing in this report changed code; fixes are a separate branch (see "Status").

## Summary

- **257 findings, 253 agreed** by the cross-review (2 disagreed, 2 need evidence). After its
  severity changes: **4 critical, 49 high, 94 medium, 106 low**. All 47 critical/high repros
  reproduced when re-run; 180 of the 210 medium/low were re-run, 28 settled by code reading, 2
  timing-only items taken from the report.
- **42 duplicate groups**: mostly an adversarial/code-review pair that found the same defect in a
  section, plus 11 cross-section root causes (below). Deduplicated, the agreed set is about 190
  distinct defects.
- **The three worst problems** (cross-review's words, condensed):
  1. *Units, currency, scale and sign are stamped by Python from model text or a default and
     never checked against the cited source.* CP-1D bridge (S05-C01, critical: EUR thousands
     published as USD millions), CP-1D basis amounts (S05-A01), CP-2E rows (S06-A04 thousands as
     millions; S06-A03/C01 interest sign), CP-3D levels (S08-A03/A04 percent read as price, bp as
     percent), the research peer sheet (S16-A01/A02/C01/C02), and the shared substring matcher
     `quotes.quoted` (S13-A03/C05) that verifies "2.50:1.00" against "12.50:1.00".
  2. *Period arithmetic and labelling in the deploy_vii engine is wrong for whole classes of
     inputs.* CFS balances summed as flows (S12-A01, critical: Q2 closing cash 20 instead of 520),
     a signed tax refund flipped to an outflow (S12-A02, raised to critical), trailing ratios
     labelled with the quarter's dates (S13-C01, raised to critical), leap-year and Q1 to Q2
     pairs refused (S11-A04), annual columns verified as Q4 (S11-A01), structural BLOCKs hidden
     as WARN (S13-A01/C02).
  3. *Validators that accept a model answer and then wedge or mislead.* CP-2D cannot settle for
     an issuer without a facility schedule (S06-A01); CP-4C passes validation then raises after
     the paid response is retained (S09-A04/C02); CP-5 flags every verbatim copy table as a
     figure mismatch (S09-A01/C01); CP-2G accepts an unchecked break metric and unvalidated
     limitation text (S07-A01/A02); the CP-8 run comparison has no code-level diff (S01-A03 and
     claim 2 below).

## The two claims the handoff asked to verify (see `CLAIMS.md`)

1. *"`cpos_handoffs.transport()` is only called from a test, so modules never get upstream
   handoffs."* Fact confirmed, conclusion refuted. The Markdown transport path in
   `cpos_handoffs.py` is dead outside `tests/test_cpos_app.py` (and broken: `retain()` reads a
   `claim.plain` attribute that does not exist). Production modules receive upstream handoffs
   through `owners/cpos.py` `HandoffTask.handoffs`, serialised in `model/handoff.py:414-416` and
   required by the launcher's checker. Net: a low-severity dead-code finding (S01-C06); S02-A03
   is withdrawn (DISAGREE, no trigger).
2. *"The CP-8 run comparison has no code-level diff of the two bundles."* Confirmed.
   `run_comparison` verifies bundle integrity, hands both bundles to the model, and
   `comparison_files` checks only the answer's shape (one seven-row dimension table) plus the
   generic citation checker. The Decimal diff in `owners/cp8.py` belongs to the decision-ledger
   module and is not on this path. AGENTS.md says CP-8 compares values, periods, assumptions and
   more; today that comparison is entirely the model's text. Medium; one lead finding with
   S01-A03 (same or swapped bundles accepted).

## Independence caveat

The `code-review` skill forks a reviewer that inherits the calling agent's context. Although
each agent was told not to, the forked reviewer read the section's `adversarial.md` in S02, S04,
S08, S11, S13 and S16 (and `SECTIONS.md` in S01). The calling agents did not read it, re-verified
every finding themselves, and S11 and S13 deliberately dropped findings that only came from the
adversarial pass. Effect: the code-review pass's overlap with the adversarial pass is understated
in those six sections, and its independence there is partial. S05, S06, S07, S09, S10, S12, S14,
S15, S17 and S18 ran clean.

## Disagreements and open rulings

- **S07-cp2-gh-A05 (DISAGREE, methodology question).** EBITDA 0 or zero interest makes the
  leverage/coverage break "Not calculable" rather than a certain breach. That is the frozen
  oracle's rule (`cases/cp2g-owner/builder/build.py` NC_E/NC_I/NC_D, pinned by the G-8 tests)
  and follows "missing is never 0". Whether a certain-direction breach should be settled from the
  signs before dividing is a ruling for the user, not a code defect.
- **S08-cp3-C08 (low).** Interest cover with negative EBITDA publishes a negative multiple while
  sibling ratios show n.m. Ruling C-2 may intend this; the fixer is told to skip if unsettled.
- **S02-module-framework-A03 (DISAGREE).** No reachable trigger (dead transport, claim 1).
- **NEEDS-EVIDENCE.** S03-C01 (how the real Copilot runtime reacts to a tool call it was not
  offered; adapter side reproduced) and S18-A05 (ProgramData policy-file trust depends on the
  host's Windows ACLs).

## Citation corrections before this is handed on

Four findings cite line numbers that do not exist in the file: S17-A08 and S17-C12
(`packaging/runtime.py` has 74 lines), S18-A05 and S18-A09 (`settings.go` 79 lines,
`platform_windows.go` 62 lines). The defects are real (verified by the cross-review at the real
locations: e.g. `loadConfig` at `settings.go:24-37`). S10-A05's root cause is the CP-8 registry
entry in `owner_workflow.py`, an S02 file.

## Known failing tests at base (not caused by this work)

Unchanged from `HANDOFF.md`: six collection failures (`tests/product/test_inputs_portfolio*.py`,
`tests/prompts`, `tests/research/test_attach.py`, `test_consumer_block.py`,
`tests/test_owner_rendering.py`), `test_method_cp5.py::test_upstream_oracles_are_the_manifest_pins`,
`test_connect_cp2d.py::test_module_trace_lists_every_offered_cp1_fact`,
`tests/research/test_contracts.py::test_decision_amendment_states_two_anchors`,
`test_connect_cpl10.py::test_navigator_with_cp1_unrun_equals_the_oracle_state`, and
`tests/model/test_gate.py` (missing ruling file in this checkout).

## Status

- **Quality gate (step 5): done.** `tools/quality_gate.py` on branch `claude/quality-gate`,
  draft PR #18, CI run passed. Changed code only: ruff with E501/C901 at 15/PLR0911-15, format,
  strict mypy. Thresholds and sources in `docs/QUALITY-GATE.md`.
- **Fixes: in progress** on `claude/review-fixes` (based on the gate branch), by section, in
  waves: critical and high (53 agreed findings in 12 sections) first, then medium, then low.
  Each fix is reproduced before and after, gets a hand-derived regression test, passes the gate,
  and is reviewed by a second model before merge. One consolidated VERIFICATION.md entry
  follows at the end.
- **Where everything is:** `ALL-FINDINGS.md` (every report), `findings.json` (index),
  `FABLE-REVIEW.md` (verdict table, repro log, duplicate groups, disagreements),
  `FINAL-TABLES.md` (counts and the ranked critical/high table), `CLAIMS.md`, and each
  `SNN/adversarial.md`, `SNN/code-review.md` with their repro scripts.

## Counts after the independent review

| Final severity | Adversarial | Code review | Total |
|---|---:|---:|---:|
| critical | 2 | 2 | 4 |
| high | 31 | 18 | 49 |
| medium | 47 | 47 | 94 |
| low | 28 | 78 | 106 |
| **agreed** | 108 | 145 | 253 |

Not agreed: 2 disagreed, 2 need evidence (of 257 findings).

## Per section (agreed findings, final severity)

| Section | critical | high | medium | low | total |
|---|---:|---:|---:|---:|---:|
| S01-orchestration | 0 | 0 | 8 | 2 | 10 |
| S02-module-framework | 0 | 0 | 3 | 4 | 7 |
| S03-model-provider | 0 | 0 | 4 | 5 | 9 |
| S04-delivery | 0 | 2 | 8 | 8 | 18 |
| S05-cp0-cp1 | 1 | 1 | 8 | 5 | 15 |
| S06-cp2-ade | 0 | 5 | 4 | 4 | 13 |
| S07-cp2-gh | 0 | 2 | 2 | 5 | 9 |
| S08-cp3 | 0 | 12 | 4 | 6 | 22 |
| S09-cp4-cp5 | 0 | 6 | 3 | 5 | 14 |
| S10-cp6-cp8-cpl10 | 0 | 2 | 6 | 3 | 11 |
| S11-earnings-financial | 0 | 6 | 5 | 5 | 16 |
| S12-vii-financial-engine | 2 | 1 | 5 | 6 | 14 |
| S13-vii-canonical-context | 1 | 6 | 6 | 7 | 20 |
| S14-vii-live-runtime | 0 | 0 | 2 | 6 | 8 |
| S15-vii-readiness-bindings | 0 | 0 | 4 | 6 | 10 |
| S16-research-tools | 0 | 4 | 4 | 8 | 16 |
| S17-issuer-library | 0 | 0 | 9 | 12 | 21 |
| S18-issuer-library-server | 0 | 2 | 9 | 9 | 20 |

## Critical and high findings (agreed), ranked

| ID | Final | Was | Dup of | Category | Location |
|---|---|---|---|---|---|
| S05-cp0-cp1-C01 | critical |  |  | correctness | `src/deploy_workflow/owners/cp1d.py:501` (parse_bridge); amounts are stamped at `cp1d.py:1027` and onward |
| S12-vii-financial-engine-A01 | critical |  |  | period arithmetic / balance summed as fl | `src/deploy_vii/statement_history.py:226-247` (statement_history: every non-BS item goes through `history._Ser |
| S12-vii-financial-engine-A02 | critical | high |  | sign convention / explicit signed inflow | `src/deploy_vii/statement_output.py:113-118` (`_cell`), `src/deploy_vii/statement_validation.py:404-411` (`acc |
| S13-vii-canonical-context-C01 | critical | high |  | correctness | `src/deploy_vii/canonical_kpis.py:311-342` (_kpi_rows); shown at `src/deploy_vii/canonical_tables.py:512` (T4. |
| S04-delivery-A01 | high |  |  | units/limitations lost at the delivery b | `src/deploy_workflow/markdown_delivery.py:84-138` (literal_module, how prose is split from tables) and `:517-5 |
| S04-delivery-C01 | high |  |  | correctness | `src/deploy_workflow/markdown_delivery.py:590-604` (markdown_files, partial-selection bindings) with `:747-772 |
| S05-cp0-cp1-A01 | high |  | S05-cp0-cp1-C01 | quantity family / currency of a model-ci | `src/deploy_workflow/owners/cp1d.py:588` (`_basis_amounts`), `:784` (`_shape_issue`), `:759` (`_outcome`), `:1 |
| S06-cp2-ade-A01 | high |  |  | control flow / unsatisfiable validation | `src/deploy_workflow/owners/cp2d.py:1862` (submission_issues, WALL_DATE_ISSUE), with `maturity_date_refs` buil |
| S06-cp2-ade-A02 | high |  |  | periods / row reading | `src/deploy_workflow/owners/cp2e.py:778-797` (`_Check.row`) |
| S06-cp2-ade-A03 | high |  | S06-cp2-ade-C01 | numbers / sign of outflows | `src/deploy_workflow/owners/cp2e.py:502` (`_row_decimal`) and `cp2e.py:778-797` (`_Check.row`), used by `deriv |
| S06-cp2-ade-A04 | high |  |  | units / scale | `src/deploy_workflow/owners/cp2e.py:778-797` (`_Check.row`), `cp2e.py:739-746` (`_Check.code`), and the stampi |
| S06-cp2-ade-C01 | high |  | S06-cp2-ade-A03 | correctness | `src/deploy_workflow/owners/cp2e.py:233` (`_rate_shock`), operand read at `:502` (`_row_decimal`), `:548`, `:5 |
| S07-cp2-gh-A01 | high |  |  | response validation / wrong break metric | `src/deploy_workflow/owners/cp2g.py:842-846` (`_metric_check`), `:887-894` (`_break_issues`), `:2030` (`_tests |
| S07-cp2-gh-A02 | high |  |  | invented content passes validation (limi | `src/deploy_workflow/owners/cp2g.py:826-829` (`_limitation_issues`), used at `:925, :929, :936`; stored as `Cl |
| S08-cp3-A01 | high |  |  | quote handling / conditional quote treat | `src/deploy_workflow/owners/cp3d.py:816` (`_observation_level`), `:796` (`_labelled`), `:2008` (`own_limitatio |
| S08-cp3-A02 | high |  |  | wrong instrument passes validation (CP-3 | `src/deploy_workflow/owners/cp3d.py:1112` (`submission_issues`), `:937` (`_check_observations`), `:979` (`_che |
| S08-cp3-A03 | high |  |  | price vs yield vs spread: units of a quo | `src/deploy_workflow/owners/cp3d.py:796` (`_labelled`), `:845` (bound `0 < value <= 200`), `:650` (`_point`) |
| S08-cp3-A04 | high |  |  | bp vs percent: margin and reference-rate | `src/deploy_workflow/owners/cp3d.py:958` (`_check_quoted_numeral`), `:1025-1034` (reference level), `:710` (`i |
| S08-cp3-A05 | high |  | S08-cp3-C06 | stale or future-dated sheet quotations a | `src/deploy_workflow/owners/cp3d.py:852` (`_observation_date`), `:402` (`_stale_lines`, context rows only), `: |
| S08-cp3-A06 | high |  | S08-cp3-C02 | CP-3 market-evidence `as_of` is model te | `src/deploy_vii/cp3_relative_value.py:1060` (`_market_row`, no `as_of` check), `:1557` (`_market`, `out.said(r |
| S08-cp3-A07 | high |  | S08-cp3-C04 | CP-3 accepts another facility's context  | `src/deploy_vii/cp3_relative_value.py:1099` (`_basis_issues`), `:1138` (`_instrument_issues`) |
| S08-cp3-C01 | high |  |  | correctness | `src/deploy_workflow/owners/cp3c.py:967` (check_currency), via `_millions_read` at :912-921 |
| S08-cp3-C02 | high |  | S08-cp3-A06 | correctness | `src/deploy_vii/cp3_relative_value.py:1057` (_market_row) and `:1543-1560` (_market, T3.3 "As of" cell) |
| S08-cp3-C04 | high | medium | S08-cp3-A07 | correctness | `src/deploy_vii/cp3_relative_value.py:1099-1117` (_basis_issues) |
| S08-cp3-C06 | high | medium | S08-cp3-A05 | correctness | `src/deploy_workflow/owners/cp3d.py:852-862` (_observation_date) and `:402-416` (_stale_lines) |
| S08-cp3-C07 | high | low | S08-cp3-A01 | correctness | `src/deploy_workflow/owners/cp3d.py:796-813` (_labelled/_label_ok) |
| S09-cp4-cp5-A01 | high |  | S09-cp4-cp5-C01 | integrity check false positive (verbatim | `src/deploy_vii/cp5_integrity.py:107` (`REFERENCE_TABLES`), `:386-430` (`identity_groups`); producer side `src |
| S09-cp4-cp5-A02 | high |  |  | response validation: threshold may come  | `src/deploy_vii/cp4_legal.py:538-568` (`_threshold_issues`), `:571-602` (`_covenant_issues`) |
| S09-cp4-cp5-A03 | high |  |  | period / step-down: one step of a schedu | `src/deploy_vii/cp4_legal.py:302-334` (`parse_threshold`, run on `threshold_text` only), `:538-568`, `:917-948 |
| S09-cp4-cp5-A04 | high |  | S09-cp4-cp5-C02 | CP-4C passes validation, then raises ins | `src/deploy_workflow/owners/cp4c.py:1034-1109` (`content_issues`, which has no CP-4 head check), `:1589-1603`  |
| S09-cp4-cp5-C01 | high |  | S09-cp4-cp5-A01 | correctness | `src/deploy_vii/cp5_integrity.py:107` (`REFERENCE_TABLES`), used by `identity_groups` at :400/:413 and `_Check |
| S09-cp4-cp5-C02 | high | medium | S09-cp4-cp5-A04 | correctness | `src/deploy_workflow/owners/cp4c.py:436-441` (`CP4_FACTS`), `:536` (`Cp4Head.fact`), `:2417` (`_references`, r |
| S10-cp6-cp8-cpl10-A01 | high |  |  | Numbers / quote parsing: wrong figure bo | `src/deploy_workflow/owners/cp8.py:470-494` (`_labelled`), called from `_observation` at `cp8.py:769` |
| S10-cp6-cp8-cpl10-A02 | high |  |  | Missing vs empty: the renderer crashes w | `src/deploy_workflow/owners/cpl10.py:878` and `:900-902` (`_scope_rows`: `supported = ", ".join(...)` written  |
| S11-earnings-financial-A01 | high |  |  | period / guard bypass | `src/deploy_workflow/financial_workflow.py:1582-1583` (`_hit`, "balance" spec), used by `_mapped_columns` 1697 |
| S11-earnings-financial-A02 | high |  |  | quantity scale (shares) | `src/deploy_workflow/statement_compose.py:226-246` (`_header_scale`), used by `resolve_typed_row` 207-208 and  |
| S11-earnings-financial-A03 | high |  | S11-earnings-financial-C02 | HTML parsing: silent row drop | `src/deploy_workflow/statement_lines.py:38-39,96-115` (`_NUMTOK`, `respace`), feeding `line_table` |
| S11-earnings-financial-A04 | high |  |  | period handling (leap year / quarter len | `src/deploy_workflow/earnings.py:348-353` (`build_earnings_delta_in`) |
| S11-earnings-financial-C01 | high |  |  | correctness | `src/deploy_workflow/financial_series.py:111-113` (_periods) |
| S11-earnings-financial-C02 | high |  | S11-earnings-financial-A03 | correctness | `src/deploy_workflow/statement_lines.py:39,100-104` (_NUMTOK, respace) |
| S12-vii-financial-engine-C01 | high |  |  | correctness | `src/deploy_vii/financial_reconciliation.py:302-367` (`_debt`) |
| S13-vii-canonical-context-A01 | high |  | S13-vii-canonical-context-C02 | gap severity / hidden disagreement | `src/deploy_vii/canonical_audit.py:491-527` (absent_input_limitation); used at canonical_audit.py:626-638 and  |
| S13-vii-canonical-context-A02 | high |  | S13-vii-canonical-context-C03 | wrong analytical conclusion (governance  | `src/deploy_vii/business_context.py:844-873` (governance_sponsor_score); rendered at business_context.py:1500- |
| S13-vii-canonical-context-A03 | high | medium | S16-research-tools-A01 | citation verification accepts numeric fr | `src/deploy_vii/quotes.py:105-118` (quoted) |
| S13-vii-canonical-context-C02 | high | medium | S13-vii-canonical-context-A01 | correctness | `src/deploy_vii/canonical_audit.py:493-526` (absent_input_limitation); used at `canonical_audit.py:630-640` an |
| S13-vii-canonical-context-C03 | high | medium | S13-vii-canonical-context-A02 | correctness | `src/deploy_vii/business_context.py:858-866` (governance_sponsor_score) |
| S13-vii-canonical-context-C05 | high | medium | S13-vii-canonical-context-A03 | security | `src/deploy_vii/quotes.py:110-123` (quoted) |
| S16-research-tools-A01 | high |  |  | Identity / quote anchoring (wrong figure | `src/deploy_workflow/research/peers.py:295` (`_amount_cell` -> `amount_from_quote`), with the check at `peers. |
| S16-research-tools-A02 | high |  |  | Units / currency / period invented or un | `src/deploy_workflow/research/peers.py:298-308` (`_amount_cell`), `peers.py:90-96` (`LocatedFigure`) |
| S16-research-tools-C01 | high |  | S16-research-tools-A01 | correctness | `src/deploy_workflow/research/peers.py:295` (_amount_cell), with the only quote check at `peers.py:207` (_figu |
| S16-research-tools-C02 | high |  | S16-research-tools-A02 | correctness | `src/deploy_workflow/research/peers.py:298-308` (_amount_cell), `peers.py:90-96` (LocatedFigure), `peers.py:18 |
| S18-issuer-library-server-A01 | high |  | S18-issuer-library-server-C01 | timeouts / lost review response | `apps/issuer-library/main.go:85` (run: `http.Server{... WriteTimeout: 180 * time.Second}`) versus `apps/issuer |
| S18-issuer-library-server-C01 | high |  | S18-issuer-library-server-A01 | correctness | `apps/issuer-library/main.go:85` (run, http.Server WriteTimeout 180s), together with `apps/issuer-library/jobs |
