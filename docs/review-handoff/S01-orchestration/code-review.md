SECTION: S01-orchestration   PASS: code-review
COVERAGE: The code-review skill (forked, effort high) reviewed all 18 files in files.txt. I verified its candidates by hand. Files I read fully: cpos_handoffs.py, cpos_status.py, run_scopes.py, platform_io.py, identity_check.py, context_periods.py, context_cites.py, __init__.py, workflow.py (repo root). Files I skimmed: owners/cpos.py (lines 66-540 and 640-790), owners/cpos_launch.py (lines 66-80, 276-336 and 520-640), run_pathway.py (lines 219-337, 377-400, 560-720 and 1040-1287), src/deploy_workflow/workflow.py (lines 120-200 and 478-689), host.py (lines 1-60 and 1080-1327), context.py (lines 1-200, 262-560 and 720-870), replay.py (lines 590-648). Files I did not read: owners/cpdr.py, run_inputs.py (the skill's pass covered them and raised nothing there).

### S01-orchestration-C01  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/run_pathway.py:1143` (run_pathway), `:1255-1279` (_resume_pathway), `:978` (_walk)
- Defect: A run started with `through=<module>` does not record `through` anywhere (not in cap.json), and `through` is refused together with `resume=True`. So the only way to resume a killed `through` run drives the whole remaining plan, including the publisher.
- Failure scenario: `run_pathway(..., through="CP-1")` on a live config is killed before CP-1 settles. Then `run_pathway(..., resume=True)` passes the identity checks and calls `_run_pathway(..., resume=True)` with `through=None`. `_drive_resumed` runs plain `walk.run()` through CP-1A, CP-2, ... and the publisher. That makes paid calls the user never asked for (still bounded by the cap) and writes a receipt and a publication for a run meant to stop after CP-1.
- Evidence: `PYTHONPATH=src:.:tests .venv/bin/python -m pytest -q -p no:cacheprovider c_tests/test_c01_through_lost_on_resume.py -s --rootdir=.` printed `cap.json: {'cap_usd': '5', 'mode': 'offline'}`; `run_pathway(..., through="CP-0", resume=True)` raised `UnknownThrough`; and `resume walk kwargs: {'through': None, 'resume': True}`. Script: `<section>/c_tests/test_c01_through_lost_on_resume.py`.
- Fix direction: Record `through` in cap.json (create-once) and have `_resume_pathway` pass the recorded value back into `_run_pathway`, or refuse to resume a run that recorded a `through`.

### S01-orchestration-C02  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cpos.py:207-216` (_handoff) via `src/deploy_workflow/workflow.py:153-160` (_put)
- Defect: `_put` writes in place (`open("xb")`, no temp file, rename or fsync). On resume, `_handoff` treats any existing `N.response.md` as the complete retained answer.
- Failure scenario: The process is killed while a paid response is being written. Resume then reads the truncated bytes as the module's answer and never calls the executor. If the cut falls after `## Next module`, the six-heading check passes. With a permissive checker, the truncated handoff is accepted and becomes the current upstream and delivery input. If the cut falls earlier, the module fails permanently (`cpos_module_failed`), and a torn `request.json` or `review.json` gives a permanent `identity_mismatch` or JSONDecodeError instead.
- Evidence: `c_tests/test_c03_torn_put.py` printed `executor called on resume: False` and `full len 9524 accepted len 8486 equal: False` (1 passed). Script: `<section>/c_tests/test_c03_torn_put.py`.
- Fix direction: Make `_put` atomic (write a temp file in the same folder, fsync, `os.link` or `os.replace` only if the target is absent, then fsync the directory), so a retained file is either complete or missing.

### S01-orchestration-C03  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cpos_launch.py:299-312` (_issuer_files)
- Defect: An HTML filing is pinned under the key `<name>.jsonl`. A sibling file that really is named `<name>.jsonl` (also an accepted suffix) is pinned under the same key and silently replaces the HTML entry.
- Failure scenario: An issuer folder holds `10-K.html` and an older extract `10-K.html.jsonl`. The manifest keeps only the `.jsonl` file. The converted 10-K text is written to `source-text/` but nothing references it, and the 10-K is not listed under "Ignored". Modules analyse the wrong or older text, and the readiness summary hides the loss. Source identity is not preserved.
- Evidence: `PYTHONPATH=src:. .venv/bin/python <section>/c04_html_jsonl_key_collision.py` printed `pinned keys: ['10-K.html.jsonl']`, `pinned path: ../issuer/10-K.html.jsonl`, `converted written but unreferenced: ['source-text/10-K.html.jsonl']` and `ignored: ()`.
- Fix direction: Refuse the launch with `LaunchRefused` when a key is already in `pinned`, or choose a converted-key form that cannot collide.

### S01-orchestration-C04  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/run_pathway.py:614-621` (_write_run_json)
- Defect: `run.json.tmp` is created with `O_EXCL` and is never cleaned up when the write fails. A temp file left by an earlier attempt makes every later `run.json` write raise `FileExistsError`, and no caller catches it.
- Failure scenario: The process is killed, or hits ENOSPC/EIO, between `os.open` and `os.replace`. `run.json.tmp` stays and `run.json` does not exist, so a resume passes `_check_identity`. The resume then drives the walk and calls `_stop` or `_finish_run`, which crashes with `FileExistsError`. That happens on every resume after any further spend, so the run can never record an outcome until someone deletes the file by hand.
- Evidence: `c_tests/test_c02_stale_tmp.py` (killed fixture, then a stale `run.json.tmp`, then `run_pathway(..., resume=True)`) gave `FileExistsError: [Errno 17] File exists: '.../run/run.json.tmp'` at `run_pathway.py:616`. Script: `<section>/c_tests/test_c02_stale_tmp.py`.
- Fix direction: Use a unique temp name (`mkstemp` in `run_dir`), or unlink a stale `run.json.tmp` under the held flock before creating it, and unlink the temp file on failure.

### S01-orchestration-C05  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cpos.py:218-225` (_handoff)
- Defect: The docstring says "reusing this directory rechecks retained answers", but the new verdict is written with the create-once `_put` to the same `N.review.json`. If the recheck's issues differ from the stored ones, it raises an opaque `WorkflowError("identity_mismatch")` and does not apply the new verdict.
- Failure scenario: The repo already records one false rejection (test_campaign_recipient_check, a live CP-2 false rejection). A live module (max_attempts=1) was falsely rejected by a checker bug. After the checker is fixed, rerunning the same state directory cannot accept the retained, already-paid response: it raises `identity_mismatch` with no executor call. The only option is a new directory, which re-pays every module. A tightened checker also surfaces as `identity_mismatch` and not as the new issue text.
- Evidence: `c_tests/test_c06_recheck_review_conflict.py` printed `first run: cpos_module_failed: CP-0: false rejection by a buggy check` and then `rerun with fixed checker raised WorkflowError: identity_mismatch executor calls: 0`. Script: `<section>/c_tests/test_c06_recheck_review_conflict.py`.
- Fix direction: Retain each recheck verdict as a new revision (for example keyed by the issues' hash) and act on the current verdict, keeping earlier reviews as evidence.

### S01-orchestration-C06  [low] [CONFIRMED]  simplification
- Location: `src/deploy_workflow/cpos_handoffs.py:22-31,141-209`; `src/deploy_workflow/run_pathway.py:677-683` (_render)
- Defect: `ACTIVE` is set only by `transport()`, and nothing in src/ calls `transport()`; the only caller is tests/test_cpos_app.py:375. The CP-OS Markdown transport branch of `_render` is therefore dead in production. If it were ever enabled, it would skip `verify_owner_rendered_slice` and use a non-idempotent `destination.mkdir()`, so a resume after a crash mid-delivery would stop with `delivery: [Errno 17]`.
- Failure scenario: Someone enables the transport. Delivery is then unverified, and a crash during `deliver` can never complete on resume. Until then, the code adds a per-prompt hook (`prompt_messages`) and a second delivery route next to the real one.
- Evidence: `grep -rn "transport()" --include=*.py src apps tests` matches only `tests/test_cpos_app.py:375`; `deliver` calls `destination.mkdir()` with no `exist_ok` and no verify step.
- Fix direction: Remove the unused transport branch, or wire it in deliberately with the same verify and idempotent staging as `run_handoffs` (staging folder, then verify, then `platform_io.replace`).

### S01-orchestration-C07  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_workflow/replay.py:614` (replay_module)
- Defect: Each replayed module builds a new `_Earlier(earlier)`. That re-reads and re-authenticates the earlier run's whole audit tree, which `check_replay` (replay.py:391) has already loaded once.
- Failure scenario: A rerun that replays N modules reads and hashes the earlier run's calls, submissions and snapshots N+1 times. That is local I/O only and the results are correct.
- Evidence: code inspection: `check_replay` builds `retained = _Earlier(replay_from)` and `replay_module` builds `retained = _Earlier(earlier)` again per module.
- Fix direction: Keep the authenticated `_Earlier` on the `ReplayPlan` (or pass it in), and keep the cheap `check_same_pack` re-check per module.

### Out of scope (one line each, optional)
- None found that I could confirm.

### Checked and sound (short bullets: what you attacked that held)
- NaN or Infinity tool arguments over `serve_json_lines`: `host._json_arguments` runs `_detached(allow_nan=False)`, so the call is refused with `{}` arguments and the session continues. A follow-up valid call returned `ok` at sequence 2 (refuted repro kept as `c_tests/refuted_nan_wedges_transport.py`).
- `identity_check.compare` returning `not_supplied` when the context names a borrower but CP-1 has no borrower row: this matches the independent oracle (`cases/context-identity-periods/expected.json`, `ctx-match@E`), so I dropped it.
- `run_handoffs` retained-handoff staleness compares `upstream` with all prior handoffs: consistent, because `HandoffTask.handoffs` supplies all prior handoffs to the module. Not a defect.
- `run_live_comparison` bare `finally: _release`: the config is always `sol-medium` (an HTTP `LiveAdapter`), so `_release` is a no-op and cannot mask the stop.
- `_handoff` refusing `cpos_interrupted` after a request without a response: an intentional never-resend guard (the executor also refuses `cpos_live_already_started`). Not reported.
- cpos_launch generic checker's "any one source sha256" rule: a heuristic, since the checker cannot know which sources a module relied on. Not a defect.
- `context_periods.resolve` and `quarters_ending_at` (year rollover, ambiguous fiscal years return None); `context_cites` offset walk (escape refusal, uniqueness, BOM); context `_num_message` bounds (Decimal, no float); `cpos_status.atomic_json` temp cleanup; platform_io lock and replace retries.
