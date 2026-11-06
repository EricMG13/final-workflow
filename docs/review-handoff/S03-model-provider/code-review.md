SECTION: S03-model-provider   PASS: code-review
COVERAGE: 4 read fully (model/copilot.py, model/copilot_adapter.py, model/redact.py, model/pricing.py) / 5 skimmed (model/record.py, model/turn.py, model/loop.py, model/reply_classes.py, model/adapter.py; the code-review skill also skimmed every other file under model/ and model_testing/) / 0 not opened at all, but the remaining model_testing/* files (budget, cases, configs, faults, mapping, pathway, records, report, run, scoring, slice_budget) and model/budget.py, handoff.py, providers.py, transport.py got only the skill's skim

The code-review skill ran at high effort on src/deploy_workflow/model and src/deploy_workflow/model_testing (8 angles). It concentrated on the Copilot adapter (PR #15). I checked its 10 candidates myself: 6 are kept below, 4 were dropped (see "Checked and sound"). The repro scripts are in /tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S03-model-provider/cr/. They reuse the FakeClient/Rig from tests/model/test_copilot_adapter.py and were run as: cd /home/user/final-workflow && PYTHONPATH=src:.:tests .venv/bin/python <script>

### S03-model-provider-C01  [medium] [PLAUSIBLE]  correctness
- Location: `src/deploy_workflow/model/copilot_adapter.py:900-915` (`_boundary`), used by `_collect` at line 790
- Defect: on a tool turn, the call only finishes once every announced tool call has reached one of the adapter's handlers (`len(calls) >= numToolCalls`). If the runtime never sends a call to a handler (the model names a tool that was not offered, or the arguments fail the runtime's schema check), the call never finishes cleanly.
- Failure scenario: the model calls `read_page` while only `read_pages` is offered, and assistant.usage says numToolCalls=1. No handler runs. Either the runtime goes quiet, so the call ends as `IdleTimeout` after idle_s (120 s by default) with the charge held, or the runtime answers the tool error itself and makes a second model call. A second assistant.usage then ends the call as `UnparsableReply` sent_unknown. In both cases the CP-OS handoff stops (`cpos_live_stopped`). The HTTP adapters instead return the call to the loop, which answers the model with an error and carries on.
- Evidence: `cr/c_unknown_tool.py` prints `runtime_silent -> sent_usage IdleTimeout no further event within the IdleTimeout bound` and `runtime_continues -> sent_unknown UnparsableReply more than one assistant.usage event`. The adapter's side is reproduced with the fake client. It stays PLAUSIBLE because I could not check offline which event sequence the real Copilot runtime emits for a tool it was not given.
- Fix direction: when usage plus the tool.execution_start events name a call that has no handler (unknown name, or no invocation by session.idle or by a later tool.execution_complete/usage), finish the call and return those tool calls as a normal turn (or as a typed error that is not a charge), so the loop can answer them the way the HTTP path does.

### S03-model-provider-C02  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/model/copilot_adapter.py:840-844` (`_settle`, refusal branch). Effect seen in `src/deploy_workflow/model/record.py:619-632` (`_error_response`)
- Defect: a Copilot refusal (ModelMismatch / ByokRouted / AutoRouted / ToolCallMismatch) is always returned as `sent_usage`, even when its Usage has no counts and no billed cost. The other two Copilot paths downgrade that case to sent_unknown (`copilot._session_error` line 145, `_timeout_reply` line 874). Export writes such a record as `sent_unknown`, so a replay does not reproduce the reply kind the live run recorded.
- Failure scenario: the runtime sends assistant.usage with `model: "other-model"` and no token fields or copilotUsage. Live, the reply is `sent_usage ModelMismatch Usage(all None)` and the record has cost_status unknown. `export_recording` then writes kind `sent_unknown`, and `RecordedAdapter` replays `sent_unknown`. The recorded run and its replay disagree on the reply class.
- Evidence: `cr/c_kind_drift.py` prints `live direct: sent_usage ModelMismatch Usage(input_tokens=None, ...) None` / `record: ModelMismatch 200 unknown` / `exported response kind: sent_unknown` / `replayed: sent_unknown ModelMismatch`.
- Fix direction: in `_settle`'s refusal branch, return `sent_unknown` when `outcome.usage == Usage()` and `billed_usd is None`, as the other two paths do.

### S03-model-provider-C03  [low] [CONFIRMED]  security
- Location: `src/deploy_workflow/model/copilot.py:138-143` (`_session_error`). Also `src/deploy_workflow/model/copilot_adapter.py:396-407` (`_paths_in`)
- Defect: the adapter deliberately removes local paths and profile directories from exception text (`_scrub` + `_ABSOLUTE_PATH`), but runtime `session.error` message text gets only key redaction and goes into the reply message (and so the call record's `error`) unchanged. Separately, `_paths_in` replaces private paths as case-insensitive substrings with no boundary check, so a path that is a prefix of a longer one is only partly replaced.
- Failure scenario: session.error `ENOENT: C:\Users\Jane Doe\AppData\Local\copilot\copilot.js` is recorded with the username and paths intact. `_paths_in("... /home/janet/project/x.js", ["/home/jan"])` gives `<path>et/project/x.js`.
- Evidence: `cr/c_paths.py` prints `session.error reply: sent_unknown SessionError | runtime: ENOENT: C:\Users\Jane Doe\AppData\Local\copilot\copilot.js and /home/jane/.copilot/x` and `_paths_in: cannot open <path>et/project/x.js`. Note: the raw event body archived for that call also keeps the message, so the same text is in raw/ too. No credentials are involved, only local usernames and paths.
- Fix direction: pass session.error detail through the same path scrubber before `_snippet` (for example a scrub hook that parse_events accepts), and anchor `_paths_in` matches so they end at a separator or at the end of a token.

### S03-model-provider-C04  [low] [CONFIRMED]  simplification
- Location: `src/deploy_workflow/model/pricing.py:174-189` (`PRICES["copilot-sol-medium"]`)
- Defect: the entry copies all twelve fields of `_SOL` by hand and only adds `reservation_output_tokens=128_000`.
- Failure scenario: a later change to `_SOL` (rates, the 272K long-context threshold, the context ceiling) leaves the Copilot hold and charge sizing on old numbers without any error.
- Evidence: code comparison of lines 135-153 with 174-189; every field is identical apart from reservation_output_tokens.
- Fix direction: `dataclasses.replace(_SOL, reservation_output_tokens=128_000)`.

### S03-model-provider-C05  [low] [CONFIRMED]  simplification
- Location: `src/deploy_workflow/model/turn.py:132` (`ModelSpec.__post_init__`), `src/deploy_workflow/model/record.py:71` (`_PROVIDERS`), `src/deploy_workflow/model_testing/configs.py:13` (`Provider`)
- Defect: the provider list is written out as a literal in four places instead of being derived from `turn.Provider`. The check at turn.py:132 can never fail, because the lines just before it already require `provider == CONFIG_PROVIDERS[config_id]`.
- Failure scenario: adding a provider means editing every literal. Missing `record._PROVIDERS` means `_withheld` never asks the new provider's parser whether a key survived decoding, which weakens the KeyReflected check on archived bodies.
- Evidence: code inspection (turn.py:124-133, record.py:71/362, configs.py:13, turn.py:15).
- Fix direction: derive from `typing.get_args(turn.Provider)` (or `set(CONFIG_PROVIDERS.values())`) and drop the check that cannot fail.

### S03-model-provider-C06  [low] [PLAUSIBLE]  simplification
- Location: `src/deploy_workflow/model/record.py:594-607` and `640-653` (`_error_response`, `_refuse_forged_error`), with the matching `adapter._reply_from_error_json`
- Defect: Copilot-only cases are special branches in shared export/replay code: null-status sent_usage limited to USAGE_TIMEOUTS, and an ADAPTER_REFUSALS + provider=="copilot" exemption from the forged-body check. The record/reply model does not represent them once.
- Failure scenario: every new adapter reply class has to be added consistently to writer, exporter and reader. C02 is one place where they already differ.
- Evidence: code inspection. It is a design concern with no separate failing input beyond C02.
- Fix direction: model adapter refusals as a 200-ok turn the loop stopped on (the existing LOOP_STOPS / stopped_ok path), so export, replay and the forged-body check need no Copilot exemptions.

### Out of scope (one line each, optional)
- tests/model/test_gate.py fails because ruling file `2026-11-02-model-testing-live.md` is missing from this checkout (reported by the skill's run of tests/model: 199 passed, 2 skipped, 1 failed). The cause is test data, not code in this section.

### Checked and sound (short bullets: what you attacked that held)
- complete()/close() race (complete reads `_closed` outside the lock): it is real only with a concurrent caller. The only production caller, `cpos.run_live_handoffs`, closes the adapter after the executor returns on the same thread, so I dropped it.
- close() sets `_released=True` before raising release notes: by then the loop is already stopped and closed, so a retry could do nothing. The only state that can be retried (loop thread still alive) raises before `_released` is set. The docstring overstates this, but there is no functional defect, so I dropped it.
- GH_TOKEN/GITHUB_TOKEN in KEY_ENV_NAMES makes their exact values redaction targets for every provider. That is a deliberate tightening of credential protection, and false KeyReflected needs an unrealistic short placeholder value, so I dropped it (protocol rule 6).
- Copilot charge parsing `_billed_usd`: exact Decimal built from digits, rejects bool, negative, non-integral and oversized values, and never uses float.
- The runtime process environment is an allowlist (`runtime_environment`): no provider keys or GH_TOKEN pass through; the token goes only through `github_token`.
- `_timeout_reply` keeps a key-bearing body out of the record (`_REFLECTED_RAW`) and treats two usage events as an unknown charge.
- The SDK's `AssistantUsageData.model` is a required field, so a usage event with no model (one of the skill's original scenarios) cannot reach the adapter. C02 was re-run with a valid but mismatching model.
- Copilot reservations price output at the 128K model maximum (`reservation_output_tokens`), because the runtime cannot enforce max_output_tokens. The hold stays bounded.
