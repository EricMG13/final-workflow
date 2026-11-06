SECTION: S14-vii-live-runtime   PASS: code-review
COVERAGE: read fully: src/deploy_vii/execution.py, src/deploy_vii/envelope.py, src/deploy_vii/live/context.py, src/deploy_vii/live/settings.py, src/deploy_vii/live/__init__.py; tools.py lines 1-130 and 300-1434 / skimmed: live/tools.py lines 130-300, live/submission.py (read 260-300 and 940-1429, skimmed the rest), live/prompts.py (read 860-1229, skimmed the rule text above it), live/schema.py (read 1-140 and 680-879, skimmed the middle) / not read: none. The code-review skill (forked, high) says it reviewed all nine files in full. Its eight angles did not run as separate subagents, and it ran no repros; I did all the verification below.

Independence note: the skill's output did not mention the adversarial pass. I read no adversarial.md, no repro/ or a0*.py file, no other section's folder and nothing under docs/review-handoff/**. All repro scripts are under <section>/cr/.

### S14-vii-live-runtime-C01  [medium] [CONFIRMED]  correctness (resume/idempotency)
- Location: `src/deploy_vii/execution.py:676` (Execution.begin), with `replace_pack` at `:912`
- Defect: `begin` refuses any input set that matches an earlier settled attempt, even when that module's head is now stale. A module whose inputs return to an earlier set can never be rerun or restored, so the journal deadlocks for good.
- Failure scenario: a store has every head settled on pack A. Then `replace_pack(B)` (an accidental swap) and `replace_pack(A)` (the revert). Every head is now `stale`. `begin("CP-0")` computes the inputs (prepared-pack A), which equal attempt 0's, and raises "Input set is settled or its one repair has been consumed". Every consumer's `current_inputs` then raises "Required upstream is unrun, stale or blocked". Nothing can run again, and the earlier valid CP-0 result for exactly these inputs is never brought back.
- Evidence: `cd /home/user/final-workflow && PYTHONPATH=src:.:tests .venv/bin/python <section>/cr/c02_aba_pack.py <section>/cr` printed: `pack restored: True`, `heads after revert: [('CP-0','stale'),('CP-1','stale'),...]`, `begin CP-0 refused: Input set is settled or its one repair has been consumed`, `begin CP-1 refused: Required upstream is unrun, stale or blocked`. Reach: `replace_pack` has no production caller in src/ today (only tests), so this is reachable through the journal API rather than the current pathway. Hence medium, not high.
- Fix direction: when `begin` finds a settled attempt for exactly the current inputs while the head is stale, restore that attempt's settled result as the head under the lock, with no new paid attempt. Do not loosen the settled-input guard.

### S14-vii-live-runtime-C02  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/live/tools.py:578-585` (_line_table), shown by `extracted_body` at `:597-600`
- Defect: on a line source, `_line_table` moves each row's `line_no` and locator to the real `line:K`. It leaves `label_candidates[].line_no` (and `omitted[].line_no`) counted from the start of the range, and `extracted_body` prints those candidates to the model. The tool spec says they are "exact source line numbers".
- Failure scenario: `extract_statements` on `line:100-105`. The row on line 104 is printed `104 | Revenue from contracts with customers | ...` with candidates `[{"line_no":4,...},{"line_no":5,...}]`, so a model that cites the label parts cites `line:4`/`line:5`, which hold unrelated text.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/cr/c01_label_candidates.py` printed `row 104 line:104 [(4, 'Revenue from contracts'), (5, 'with customers')]` and the same numbers in the rendered body. In production this is shadowed: `deploy_workflow.statement_lines.line_table` and `LineTools._extract_lines` re-implement the range and do rebase the candidates (`first + part.line_no - 1`), which confirms the DVII version is wrong. A direct `PackTools` user (tests, or any new caller) still gets the wrong numbers.
- Fix direction: in `_line_table`, rebase `label_candidates` and `omitted` the same way as `line_no`, or delegate to the deploy_workflow implementation's logic.

### S14-vii-live-runtime-C03  [low] [CONFIRMED]  security/robustness
- Location: `src/deploy_vii/envelope.py:494-500` (_table_issues), capped only by `_MAX_ISSUES` at `:631-633` (envelope_issues)
- Defect: `envelope_issues` has its own 20-line cap and no per-line limit, and `_table_issues` quotes the Markdown cell whole (`{cell!r}`). One tampered cell (the table codec allows up to 4,000,000 characters) becomes an issue line of that size. `execution.bounded_issues` and its 600-character cap are not applied.
- Failure scenario: an on-disk `envelope.md`, with receipt hashes updated to match, holds a 2 MB Identity cell. `read_envelope` raises `EnvelopeError` (then `EnvelopeRefused`) whose message and `issues` carry the 2 MB string into logs and records. The journaled path (`cp1_workflow` -> `submit_step`) is bounded, but this direct-reader path is not.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/cr/c05_envelope_issue_size.py` printed: `clean round trip issues: ()`, then `issue count: 1 longest issue chars: 2000078 cap elsewhere: 600`.
- Fix direction: return `bounded_issues(...)` (or use `clipped` for each `_table_issues` line) instead of the local `_MAX_ISSUES` cap.

### S14-vii-live-runtime-C04  [low] [PLAUSIBLE]  security (prompt-injection hardening)
- Location: `src/deploy_vii/live/prompts.py:1211-1229` (build: rule 2 and the REPAIR block)
- Defect: rule 2 declares only text between `<<<SOURCE ...>>>` and `<<<END>>>` untrusted, and rule 5 covers tool output. The `<<<REPAIR ...>>>` block is sent in the user message with no such rule. Its lines quote model-supplied quotes and locators (`readiness.citation_issues` names the quote prefix, up to 600 characters a line), which can echo source text.
- Failure scenario: a filing span says "Ignore prior rules and ..."; the model copies it into a quote that fails the check. The repair attempt's REPAIR block then shows that text outside any block the prompt calls untrusted.
- Evidence: from the code only. I could not reproduce model behaviour here (no provider calls are allowed), and `block()` does stop delimiter forgery inside REPAIR.
- Fix direction: extend rule 2 to name REPAIR (and CONTEXT) blocks as data, never instructions.

### S14-vii-live-runtime-C05  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_vii/live/submission.py:1062` and `:1101` (submit_model_payload), with `_with_rules` at `:1015-1021`
- Defect: on the CP-1A/CP-3/CP-4 and composed CP-0 paths, when rules find issues they run twice on the same payload: once in `if rules(normalised)` and again inside `_with_rules`, while the journal lock is held. The tools.py docstring says the rule walk takes several seconds per call on a deeply nested payload of about 1 MiB.
- Failure scenario: a large CP-3 submit that fails the cited-page rule pays for the walk twice per submit. owner_workflow.py also computes `issues` with the same rules before calling, which makes three passes.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/cr/c03_rules_twice.py` printed `step relative_value rules() calls for one submit: 2`.
- Fix direction: compute `found = rules(normalised)` once and pass the result into a `_with_rules` variant that takes precomputed issues.

### S14-vii-live-runtime-C06  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_vii/live/context.py:90-139` (MODULE_CONTEXTS, _cp3_market_sources, declared_sources, readable_sources)
- Defect: each helper re-reads, re-hashes and re-parses the pack blob (`store.pack()`) and rebuilds the bound upstream view. One dispatch calls `module_context`, `declared_sources` and `readable_sources` (host.py:1099-1100, prompts/factory.py:118), so the work is repeated.
- Failure scenario: one CP-3 dispatch parses the pack 4 times and builds `cp3_upstream` 3 times, and `cp3_upstream` loads settled heads, including CP-1, which execution.py says is about 322 MiB parsed.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/cr/c04_pack_reloads.py` printed `{'pack': 4, 'cp3_upstream': 3}`.
- Fix direction: build the pack and the upstream view once per attempt and pass them to these helpers.

### Out of scope (one line each, optional)
- None found with a root cause outside the section.

### Checked and sound (short bullets: what you attacked that held)
- Skill candidate refuted: `envelope._table` `gaps[fact_id]` KeyError. `build_index` gives a G ref to every non-known fact, and the `Module` validator requires unique fact ids and table rows that resolve, so the key always exists.
- Skill candidate refuted: `_validate_prefilled`/`_checked` "Field required" path mismatch inside unions. `<section>/cr/c06_marked_in_union.py` shows no PREFILLED field behind a multi-branch union in any CP-1 step schema (source_context 6, financials 71, narrative/readiness/quality 1 each, all 0 behind a union).
- Skill candidates dropped, no trigger: `settings._money` accepting inf/nan/negative caps, `default_effort` not checked against `EFFORT_LADDER`, and `credential_file` not resolved against root. `load_settings` has no caller anywhere in src/ or tests/, and there is no settings/project.toml.
- Dropped, dead path: the extracted-coverage floor never measures a line source (`_cell_coverage` keeps only `page:N` citations, and `_agreement` looks tables up by `line:K` while they are keyed `line:N-M`). Production builds `ToolRules()` with `coverage_min=None` and never calls `extracted_coverage`, so this has no current trigger. Fix it before the floor is turned on.
- `execution` journal: the lock covers every write, the response is kept before validation, step repairs are bounded (one per step per attempt), `_put_once` refuses differing bytes, `bounded_issues`/`listed_issues`/`clipped` cap the caller-quoted text, and `blocked_ancestors` is safe against cycles.
- `PackTools.read_pages` checks the line-count bound before any iteration, and extract range bounds are checked before extraction. `block()` refuses delimiters, and a resulting `PromptError` is receipted as `render_refused` by the host.
- `schema.normalise`/`json_object`: floats parse as Decimal and NaN/Infinity are refused, so exact digits are kept; depth is capped before parsing; lone surrogates are refused; a null becomes the default only where the field does not admit null.
- `submission.assemble`: books are merged by `book_id`, split registers keep IS/CFS/BS order, and an absent part leaves the contract's own default or "Field required" to stand, with nothing invented.
