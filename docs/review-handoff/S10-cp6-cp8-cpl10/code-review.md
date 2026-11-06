SECTION: S10-cp6-cp8-cpl10   PASS: code-review
COVERAGE: src/deploy_workflow/owners/cp6.py (read fully by me; all four files were reviewed whole by the code-review skill's forked reviewer) / src/deploy_workflow/owners/cp8.py, src/deploy_workflow/owners/cpl10.py, src/deploy_vii/cp6_committee.py (I skimmed them and read every region a finding touches: the validators, upstream adapters, composition and claims) / none not read

Independence note: the skill's output did not mention the adversarial pass. I did not read adversarial.md or the scratch/ repro files. My repros are in the cr/ subfolder of my section folder.
Skill note: the code-review skill ran at high effort on the four files. There is no git diff here, so it reviewed the files whole. It reported 10 items. I refuted 3 of them and dropped 2 low-value ones (see "Checked and sound"). I added C01 from my own review.

### S10-cp6-cp8-cpl10-C01  [high] [CONFIRMED]  correctness (currency)
- Location: `src/deploy_workflow/owners/cpl10.py:416-429` (`Upstream.__post_init__`), with the check only at `:441-449` (`RunUpstream.__post_init__`) and the branch at `:1392-1393` (`cpl10_upstream`)
- Defect: the CP-1 money operands' currency is checked only in `RunUpstream`, which is built only for a non-USD run. The plain USD `Upstream` (no run context, or a USD context whose T4.14 register states no currency) accepts operands in any currency and stamps every derived cell USD.
- Failure scenario: a run with no context (or a USD context and no register currency) binds CP-1 T4.10 facts in EUR. TL10.2 then shows `from_value` and `to_value` as EUR (copied from CP-1) and `change` as USD in the same row. The mismatch is silent: no UpstreamError and no issue.
- Evidence: `cd /home/user/final-workflow && PYTHONPATH=src:.:tests .venv/bin/python <section>/cr/c_cpl10_ccy.py` prints `TL10.2.cash.change (3.75, 'MILLIONS', 'USD')`, `TL10.2.cash.from_value (16.25, 'MILLIONS', 'EUR')`, `TL10.2.cash.to_value (20, 'MILLIONS', 'EUR')`. No error is raised when `Upstream` is built.
- Fix direction: move the known-money currency check into `Upstream.__post_init__` against `self.currency.currency`, so the USD default is checked as well.

### S10-cp6-cp8-cpl10-C02  [medium] [CONFIRMED]  correctness (unchecked analyst text in claims and limitations)
- Location: `src/deploy_workflow/owners/cpl10.py:1191-1206` (`_text_issues`), `:1209-1224` (`_overall_issues`), `:1227-1248` (`_gap_issues`)
- Defect: `overall.limitation` is only checked for blank text, and gap text only for blanks and digits. Neither field goes through `prose_issues` (the figure and reference check) or the `PROHIBITED` check (recommend/recovery/covenant), although both are analyst text. The method (`methods/cpl10.md`) says "the analyst writes no figure" and refuses prohibited words in analyst text.
- Failure scenario: an Insufficient Information overall with limitation `"We recommend a covenant reset at 5.2x; recovery is 40% at most."` validates. It is stored verbatim as the `TL10.3.overall` claim limitation. The same sentence in `overall.rationale` is refused with `Bare figure: 5.2x` and two prohibited-conclusion issues. A gap `"Recovery prospects support a recommend-hold under the covenant"` also validates and becomes the own limitation `Gap (Material): ...`.
- Evidence: `PYTHONPATH=src:.:tests .venv/bin/python <section>/cr/c_cpl10_limitation.py` prints `limitation issues: []`, the claim `('TL10.3.overall', 'We recommend a covenant reset at 5.2x; ...')`, `rationale issues: ['overall.rationale: Bare figure: 5.2x', '...prohibited conclusion: recommend', '...covenant']`, then `gap issues: []`.
- Fix direction: add `overall.limitation` (when present) and the gap text fields to the `_text_issues` list, or at least apply the `PROHIBITED` check and the figure check to them.

### S10-cp6-cp8-cpl10-C03  [medium] [CONFIRMED]  correctness (valid input refused)
- Location: `src/deploy_workflow/owners/cp8.py:670` (`_Checker._decision_text`)
- Defect: `text not in _norm(quote.quote)` normalises only the quote side. A decision field whose text copies the page exactly, with an em/en dash, a curly apostrophe or curly quotes, is refused as `does not occur in the quote`, although the quote itself passes the citation check.
- Failure scenario: the Prior Case page reads `Decision-maker role: Investment Committee — Europe.` The model quotes it and gives the text exactly as printed. The step gets `decision.decision_maker_role: text Investment Committee — Europe does not occur in the quote`. That message is false, and nothing tells the model to switch to ASCII. Retries can be spent and the step can settle invalid. Only the normalised spelling, which the page does not print, passes, and that spelling becomes the T7.1 cell.
- Evidence: `PYTHONPATH=src:.:tests .venv/bin/python <section>/cr/c_cp8_dash.py` prints `'-' ()` for the ASCII page and `'—' ('decision.decision_maker_role: text Investment Committee — Europe does not occur in the quote',)` for the em-dash page. The same check applies to instrument, role and action-bias text.
- Fix direction: compare `_norm(text)` against `_norm(quote.quote)` (keeping the `_wrap_split` guard), or tell the analyst in the issue text that the normalised spelling is required.

### S10-cp6-cp8-cpl10-C04  [low] [CONFIRMED]  correctness (unresolved reference in stored limitation)
- Location: `src/deploy_vii/cp6_committee.py:1302-1320` (`committee_challenge`, the claims tuple)
- Defect: the `T6-FINAL.final_bias` and `T6A.6.vNN` claims store the model's raw limitation with its `{ref|unit}` figure tokens. The table cell for the same limitation is spelled by Python (`out.limit`). `Claim.limitation` is typed plain `str`, not `RunText`, and the sibling cp2a spells stored limitations with `_spelled`, whose docstring says "never as raw braces".
- Failure scenario: limitation `CP-1 shows EBITDA of {T4.10.ebitda.fy2025|US$ m} only`. The T6-FINAL cell reads `... 120 US$ m only` but the claim limitation keeps the literal token. Downstream contexts that read `claim.limitation` (tools/upstream.py, any delivery that prints it) receive raw braces.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/cr/c_cp6_limit.py` prints `issues: ()`, `table limitation cell: CP-1 shows EBITDA of 120 US$ m only`, `claim limitation: CP-1 shows EBITDA of {T4.10.ebitda.fy2025|US$ m} only`.
- Fix direction: store `out.text(limitation)` (the spelled form) in the claim limitation, as cp2a does.

### S10-cp6-cp8-cpl10-C05  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_vii/cp6_committee.py:1359-1366` (`_validate_step`) and `:1281-1283` (`committee_challenge`)
- Defect: `_validate_step` calls `validate_committee`, then `committee_challenge`, which calls `validate_committee` again. That repeats two pydantic JSON round-trips, every prose tokenisation and the CP-2, CP-3 and CP-5 scans. `submit_cp6_step` and the probe each run `_validate_step` twice, so a submission is validated four times.
- Failure scenario: settle and verifier replay cost twice what they need to, and more for large CP-5 registers. Results are not affected.
- Evidence: `<section>/cr/c_cp6_limit.py` (last line) counts `validate_committee calls per _validate_step: 2`.
- Fix direction: split out a private `_compose(pack, submission, upstream)` that `_validate_step` calls after its single `validate_committee`. Keep the public `committee_challenge` guard.

### S10-cp6-cp8-cpl10-C06  [low] [CONFIRMED]  simplification
- Location: `src/deploy_workflow/owners/cp8.py:2294-2298` (`_bound`), `src/deploy_workflow/owners/cpl10.py:1342-1346` (`_bound`), `src/deploy_vii/cp6_committee.py:608-612` (`_bound_module`); also `cp6_module`, `cp8_module`, `cpl10_module`
- Defect: three copies of "find the attempt's bound input by id, then `store.result(sha)`", and three copies of the Module builder with a submission tail input. They differ only in wording and exception type.
- Failure scenario: maintenance only. A guard added to one copy (for example a bound-status check) has to be repeated in the other two.
- Evidence: the code was read side by side. The helpers have the same structure.
- Fix direction: a shared helper in `deploy_workflow.owners` (next to `probe_one_step`) that takes the error type as a parameter, so cpl10 keeps raising `UpstreamError`.

### Out of scope (one line each, optional)
- `src/deploy_workflow/cpos_handoffs.py:55` uses `claim.plain`, which does not exist on `deploy_vii.contracts.Claim` (`hasattr(Claim(...), 'plain')` is False). Any head with a claim would raise AttributeError when the handoff is written.

### Checked and sound (short bullets: what you attacked that held)
- CP-8 `_PROHIBITED` matching "buyer" and "seller" is deliberate and pinned: `tests/test_method_cp8.py:964` ("The buyer held the loan" -> `prohibited conclusion: buy`, "the limit"). The skill's over-match finding is refuted as a defect.
- CP-L10 substring matching of prohibited words is a documented, accepted limit (`methods/cpl10.md`, ruling L10-b, pinned refusal r10). Not reported.
- CP-6 `_validate_step` lets `cp6_upstream` ValueErrors through (the skill's finding). It can only be triggered by a malformed attempt or a tampered blob. `current_inputs` always binds the required heads, and blobs are canonical, validated Modules. It also matches the cp3/cp5 `_validate_step` siblings. Dropped.
- `Upstream.blocked_upstream` unioning bound blocked inputs is not fully redundant (`Upstream` is also built directly, for example in tests with `blocked=frozenset()`). Dropped. Un-cached `@property` recomputation is a minor cost. Dropped.
- CP-8 derive: mid = (bid + offer)/2/100 under the EXACT context; variance None vs 0 is kept; `breached` is strict (equal is not a breach); hit_rate is None when nothing is labelled; a split bid/offer date makes the mid not calculable.
- CP-8 `cp8_upstream` with CP-6 bound: the CP-6 edge is `block`, so a blocked CP-6 head is never bound and `settled_call` cannot raise on it.
- CP-L10 operand binding refuses zero or several label matches, a known operand with no amount, a unit mismatch and mixed scales. Missing is never read as 0.
