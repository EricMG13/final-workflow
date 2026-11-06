# Review handoff: resume here

This file tells a new Claude session what to do next. The first session stopped
because its account hit a weekly usage limit. Nothing in `src/` or `apps/` changed.
This branch adds only `docs/review-handoff/`. Delete or condense it after the work
is done (AGENTS.md: keep one concise verification record).

Base commit: `a313b50` (main). Read `AGENTS.md` first. Its rules still apply.

## What the user asked for

1. Split the app into sections.
2. Run an adversarial review on each section with high-effort Opus 5.5 subagents.
3. Repeat step 2 with the `/code-review` skill.
4. Have one Fable subagent (`model: fable`) review all findings when both passes are done.
5. Check quality gates (readability, maintainability, complexity) of similar projects.
   Use them for code changes. Use the standard library where possible.

## State (updated 2026-11-06, second session)

| Step | State |
|---|---|
| 1. Sections | Done. 18 sections, `SECTIONS.md`. |
| 2. Adversarial pass | **Done, 18 of 18.** S18 (Go server) added this session: 9 findings. |
| 3. `/code-review` pass | **Done, 18 of 18.** 5 or 6 agents at a time. See the independence caveat in `FINAL-REPORT.md`. |
| 4. Fable review | **Done.** `FABLE-REVIEW.md`: 253 of 257 agreed, 47 of 47 critical/high repros re-run, 22 severities changed, 42 duplicate groups. |
| 5. Quality gates | **Done.** `tools/quality_gate.py` on `claude/quality-gate`, draft PR #18, CI passed. |
| Final report | **Done.** `FINAL-REPORT.md` (summary, claims, caveats, rulings, tables). |
| Fixes | **In progress** on `claude/review-fixes`, by section, critical/high first. The user asked for the gate, then fixes. |

Totals: 257 findings (`findings.json`); after the cross-review 4 critical, 49 high, 94 medium,
106 low agreed. `python3 collect.py` rebuilds `ALL-FINDINGS.md` and the index.

## How to resume

Replace `<REVIEW_ROOT>` in the `PROTOCOL-*.md` files with a folder in your scratchpad.
Copy this folder there first. Repro scripts run as
`cd <repo> && PYTHONPATH=src:. .venv/bin/python <script>`. Some also need `tests` on `PYTHONPATH`.

1. **Budget.** 18 parallel Opus-high agents used the whole weekly limit. Run 5 or 6
   agents at a time. Tell the user the cost before you start.
2. **S18 adversarial.** Run one agent on `S18-issuer-library-server/files.txt`
   with `PROTOCOL-common.md` and `PROTOCOL-adversarial.md`. Go needs toolchain 1.26,
   which downloads on first use. Copy `apps/issuer-library` to scratch and run
   `go vet ./... && go test ./...` there. Both passed on a copy.
   Never run go inside the repo folder.
3. **`/code-review` pass.** No `/adversarial-review` skill exists. The adversarial pass used
   `PROTOCOL-adversarial.md` instead. The `code-review` skill does exist (use it at
   effort `high`). Run one agent per section, read-only, without `--fix` or `--comment`.
   Tell each agent not to read `adversarial.md`, so the pass stays independent.
4. **Fable review.** Run `python3 collect.py`. Give the merged `ALL-FINDINGS.md` to one
   agent with `model: fable`. For each finding it must say agree, disagree or needs
   evidence. It must also flag duplicates and wrong severity. It must re-run the repro of
   each critical and high finding itself.
5. **Final report.** Merge, deduplicate (see root causes), rank, and add the verdicts.
   Then ask the user whether to fix. Fixes need the AGENTS.md steps: confidence-review and
   rewrite-tournament after code changes, and a quality gate on changed code.

## Root causes that span sections

- `deploy_vii/quotes.py` `quoted()` accepts any substring. A fragment of a number counts as a
  verified quote. Seen in S13-A03, S16-A01 and the S09 threshold findings.
- Units, currency and period often come from model text and are never checked against the
  cited source (S16-A02, S06-A04, S05-A01, S08-A03/A04, S10-A04).
- Minus-signed, parenthesised or split-parenthesis negatives are dropped without a flag in
  several parsers (S11-A03, S12-A04). The opposite case: S06-A03 reads an outflow with the wrong sign.
- Fixed display precision hides small amounts (S04-A02).
- Model-written limitation and gap text is often not validated (S07-A02, S06-A06).

## Claims to verify before you rely on them

- S02 reported that `cpos_handoffs.transport()` is called only from `tests/test_cpos_app.py`,
  so modules may never get upstream Markdown handoffs in production. S01 found that `cpos.py`
  uses its own retained-response path. Check the real data flow before you report it.
- S10 reported that the CP-8 run comparison (`cpos.run_comparison`, `handoff_delivery.comparison_files`)
  has no code-level diff of the two bundles. A model answer of "no change" would pass.
  That conflicts with AGENTS.md. Confirm it.
- S14 reported latent problems with no caller today: `load_settings` accepts infinite or
  negative caps and needs a credential file path (AGENTS.md says keys come only from the
  environment). Product callers build `ToolRules()` with no floors.
- S12-A06, S02-A03 and S13-A07 are PLAUSIBLE, not reproduced.

## Known failing tests at base (not caused by this work)

- Six files fail to collect: `tests/product/test_inputs_portfolio*.py` (module `scripts`),
  `tests/prompts` (module `o2_case`), `tests/research/test_attach.py` and
  `test_consumer_block.py` (module `cpdr_consumers`), `tests/test_owner_rendering.py`
  (missing `docs/OWNER-RENDERING-LEASE.md`).
- `tests/test_method_cp5.py::test_upstream_oracles_are_the_manifest_pins` (pin drift).
- `tests/test_connect_cp2d.py::test_module_trace_lists_every_offered_cp1_fact` ("19 US$" vs "19 US$ m").
- `tests/research/test_contracts.py::test_decision_amendment_states_two_anchors` (missing `docs/decisions/0007-*.md`).
- `tests/test_connect_cpl10.py::test_navigator_with_cp1_unrun_equals_the_oracle_state`.
- The Issuer Library unreadable-run test fails only when run as root.

## Quality gates (step 5)

Measured on `a313b50`, `src` plus `apps` (4,866 functions):

| Check | Result |
|---|---|
| `ruff check` with the current config | 91 findings (ISC004 52, SIM905 11, PLC0414 10, TRY004 6, I001 5, BLE001 4, SIM102 2, PYI064 1) |
| `C901` above 10 (ruff default) / 15 / 25 | 180 / 62 / 15 functions |
| `PLR0913` / `PLR0917` / `PLR0912` / `PLR0914` / `PLR0915` / `PLR0916` / `PLR0911` / `PLR1702` (ruff defaults, preview) | 160 / 107 / 94 / 91 / 56 / 50 / 33 / 8 |
| `mypy` strict, `src` + `apps/issuer-library/engine` | 110 errors in 12 files |
| `ruff format --check` | 27 of 271 files would change |

What similar projects do (read from their `pyproject.toml` files):

- pydantic-ai: `C90` on, `mccabe max-complexity = 15`, `PLR` not selected, `BLE001` on, mypy and pyright strict, coverage `fail_under = 100`.
- Home Assistant: `PL` and `C` selected, `mccabe max-complexity = 25`, `PLR0911/12/13/15/17` ignored.
- OpenBB: `PLR` selected, `PLR0913` and `PLR0915` ignored, pylint `max-args 8`, `max-branches 26`, `max-returns 9`, `max-statements 30`.
- LangChain core: `select = ALL`, `C90` and `PLR09` ignored.
- Code Climate defaults: method complexity 5, method lines 25, file lines 250, arguments 4.
- SonarQube rule S3776 (cognitive complexity) defaults to 15. That is a rule default, not a gate
  condition. The Sonar docs host was not reachable, so the exact "Sonar way" gate conditions are unverified.

Recommendation (not implemented, ask the user first): gate **changed code only**, because
180 existing functions exceed the ruff default. Use tools the repo already has (ruff is a dev
dependency), so no new dependency. A stdlib `ast` plus `git diff -U0` script can limit the
check to touched functions. Start with `C901` at 15 and `PLR0911/12/13/15` at ruff defaults.
Keep mypy strict and `ruff format` for changed files. Do not add radon, xenon or wily
without the user's approval.

## Top findings (critical and high)

Full text, repro and fix direction are in each `SNN/adversarial.md`.

| ID | Sev | Verdict | Category | Location |
|---|---|---|---|---|
| S12-vii-financial-engine-A01 | critical | CONFIRMED | period arithmetic / balance summed as flow | `src/deploy_vii/statement_history.py:226-247` (statement_history: every non-BS item goes t |
| S04-delivery-A01 | high | CONFIRMED | units/limitations lost at the delivery boundary | `src/deploy_workflow/markdown_delivery.py:84-138` (literal_module, how prose is split from |
| S05-cp0-cp1-A01 | high | CONFIRMED | quantity family / currency of a model-cited amou | `src/deploy_workflow/owners/cp1d.py:588` (`_basis_amounts`), `:784` (`_shape_issue`), `:75 |
| S06-cp2-ade-A01 | high | CONFIRMED | control flow / unsatisfiable validation | `src/deploy_workflow/owners/cp2d.py:1862` (submission_issues, WALL_DATE_ISSUE), with `matu |
| S06-cp2-ade-A02 | high | CONFIRMED | periods / row reading | `src/deploy_workflow/owners/cp2e.py:778-797` (`_Check.row`) |
| S06-cp2-ade-A03 | high | CONFIRMED | numbers / sign of outflows | `src/deploy_workflow/owners/cp2e.py:502` (`_row_decimal`) and `cp2e.py:778-797` (`_Check.r |
| S06-cp2-ade-A04 | high | CONFIRMED | units / scale | `src/deploy_workflow/owners/cp2e.py:778-797` (`_Check.row`), `cp2e.py:739-746` (`_Check.co |
| S07-cp2-gh-A01 | high | CONFIRMED | response validation / wrong break metric | `src/deploy_workflow/owners/cp2g.py:842-846` (`_metric_check`), `:887-894` (`_break_issues |
| S07-cp2-gh-A02 | high | CONFIRMED | invented content passes validation (limitations) | `src/deploy_workflow/owners/cp2g.py:826-829` (`_limitation_issues`), used at `:925, :929,  |
| S08-cp3-A01 | high | CONFIRMED | quote handling / conditional quote treated as ex | `src/deploy_workflow/owners/cp3d.py:816` (`_observation_level`), `:796` (`_labelled`), `:2 |
| S08-cp3-A02 | high | CONFIRMED | wrong instrument passes validation (CP-3D) | `src/deploy_workflow/owners/cp3d.py:1112` (`submission_issues`), `:937` (`_check_observati |
| S08-cp3-A03 | high | CONFIRMED | price vs yield vs spread: units of a quoted leve | `src/deploy_workflow/owners/cp3d.py:796` (`_labelled`), `:845` (bound `0 < value <= 200`), |
| S08-cp3-A04 | high | CONFIRMED | bp vs percent: margin and reference-rate units n | `src/deploy_workflow/owners/cp3d.py:958` (`_check_quoted_numeral`), `:1025-1034` (referenc |
| S08-cp3-A05 | high | CONFIRMED | stale or future-dated sheet quotations accepted  | `src/deploy_workflow/owners/cp3d.py:852` (`_observation_date`), `:402` (`_stale_lines`, co |
| S08-cp3-A06 | high | CONFIRMED | CP-3 market-evidence `as_of` is model text, unch | `src/deploy_vii/cp3_relative_value.py:1060` (`_market_row`, no `as_of` check), `:1557` (`_ |
| S08-cp3-A07 | high | CONFIRMED | CP-3 accepts another facility's context quote as | `src/deploy_vii/cp3_relative_value.py:1099` (`_basis_issues`), `:1138` (`_instrument_issue |
| S09-cp4-cp5-A01 | high | CONFIRMED | integrity check false positive (verbatim copy re | `src/deploy_vii/cp5_integrity.py:107` (`REFERENCE_TABLES`), `:386-430` (`identity_groups`) |
| S09-cp4-cp5-A02 | high | CONFIRMED | response validation: threshold may come from the | `src/deploy_vii/cp4_legal.py:538-568` (`_threshold_issues`), `:571-602` (`_covenant_issues |
| S09-cp4-cp5-A03 | high | CONFIRMED | period / step-down: one step of a schedule teste | `src/deploy_vii/cp4_legal.py:302-334` (`parse_threshold`, run on `threshold_text` only), ` |
| S09-cp4-cp5-A04 | high | CONFIRMED | CP-4C passes validation, then raises inside the  | `src/deploy_workflow/owners/cp4c.py:1034-1109` (`content_issues`, which has no CP-4 head c |
| S10-cp6-cp8-cpl10-A01 | high | CONFIRMED | Numbers / quote parsing: wrong figure bound to a | `src/deploy_workflow/owners/cp8.py:470-494` (`_labelled`), called from `_observation` at ` |
| S10-cp6-cp8-cpl10-A02 | high | CONFIRMED | Missing vs empty: the renderer crashes when no t | `src/deploy_workflow/owners/cpl10.py:878` and `:900-902` (`_scope_rows`: `supported = ", " |
| S11-earnings-financial-A01 | high | CONFIRMED | period / guard bypass | `src/deploy_workflow/financial_workflow.py:1582-1583` (`_hit`, "balance" spec), used by `_ |
| S11-earnings-financial-A02 | high | CONFIRMED | quantity scale (shares) | `src/deploy_workflow/statement_compose.py:226-246` (`_header_scale`), used by `resolve_typ |
| S11-earnings-financial-A03 | high | CONFIRMED | HTML parsing: silent row drop | `src/deploy_workflow/statement_lines.py:38-39,96-115` (`_NUMTOK`, `respace`), feeding `lin |
| S11-earnings-financial-A04 | high | CONFIRMED | period handling (leap year / quarter length) | `src/deploy_workflow/earnings.py:348-353` (`build_earnings_delta_in`) |
| S12-vii-financial-engine-A02 | high | CONFIRMED | sign convention / explicit signed inflow flipped | `src/deploy_vii/statement_output.py:113-118` (`_cell`), `src/deploy_vii/statement_validati |
| S13-vii-canonical-context-A01 | high | CONFIRMED | gap severity / hidden disagreement | `src/deploy_vii/canonical_audit.py:491-527` (absent_input_limitation); used at canonical_a |
| S13-vii-canonical-context-A02 | high | CONFIRMED | wrong analytical conclusion (governance risk lev | `src/deploy_vii/business_context.py:844-873` (governance_sponsor_score); rendered at busin |
| S16-research-tools-A01 | high | CONFIRMED | Identity / quote anchoring (wrong figure accepte | `src/deploy_workflow/research/peers.py:295` (`_amount_cell` -> `amount_from_quote`), with  |
| S16-research-tools-A02 | high | CONFIRMED | Units / currency / period invented or unverified | `src/deploy_workflow/research/peers.py:298-308` (`_amount_cell`), `peers.py:90-96` (`Locat |