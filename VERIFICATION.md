# Verification record

Keep one running record here. A pass applies only to the stated scope. Preserve
earlier run artifacts; record a new attempt when instructions or outputs change.

The [current remaining-module record](runs/cpos-sol-remaining-20261105/verification.json)
contains the settled CP-6 timeout cost, the corrected TDG annual publication, the
live CP-8 comparison and checks of the five broader report bundles. The older
entries below retain their historical case scope.

Older entries are in [docs/VERIFICATION-ARCHIVE.md](docs/VERIFICATION-ARCHIVE.md), verbatim and in their original order; new entries go here.

## 2026-11-08 — Phase 6: verification record split (branch `claude/verification-archive`)

Moved the sections dated before 2026-11-07, verbatim and in original order, to docs/VERIFICATION-ARCHIVE.md by `git mv`; 2026-11-07 entries stay here.
Proof, exit 0: `diff <(git show HEAD^2:VERIFICATION.md | tail -n +10) <(cat <(tail -n +12 VERIFICATION.md | sed '1,8d') <(tail -n +5 docs/VERIFICATION-ARCHIVE.md))` on the merge with main after #35-#42 (HEAD^2 = that main; the `sed` drops this entry).
Line counts: VERIFICATION.md 359 (with this entry), docs/VERIFICATION-ARCHIVE.md 5655.
Merged after #35-#42; their entries stay in this file.
Not verified: none beyond the gates.

## 2026-11-08 — Phase 5: LTM Adj EBITDA and quarter-end leverage (branch `claude/model-ltm`)

Scope: Tasks 9-10 and the end batch (da425880..853c9ee1), stacked on Phase 4; macOS only.
Phase diff: 760 changed lines (cap 800). **Deterministic retained-data** check: TDG
`runs/cpos-tdg-model-001` inputs and quarter handoff `runs/tdg-003`, no provider call.
- Answer key (checked by hand before dispatch): LTM 4,173 + 1,061 − 912 = 4,322; quarter secured
  20,192. The plan's "4.7x" is "4.67x" in the store's format (two places).
- Controller live check (real app, retained data): classifiable model Q1 FY2025 LTM 4,322, senior
  4.67x, FY2024 senior 4.80x; full TDG model Q1 FY2025 LTM 4,322, senior n.a. "the debt register has
  a row that cannot be classified", total/net leverage "needs quarter-end total carrying debt, which
  the model does not derive".
- Reviews: Task 9 mx-precise + mx-adversary, one fix round (required secured rows, LTM span, Total
  rows, one Net column, repeated bridge row, duplicate windows, operand reasons, hidden text),
  re-review pass; Task 10 mx-precise approve; end batch (LTM span 364-371; senior fallback text);
  phase mx-architect approve.
- Gates: `validate.py full` exit 0; `tools/quality_gate.py` exit 0; pytest 265 passed.
- Follow-ups on `claude/register-hardening` (owner asked to apply them): escaped pipes, subtotal and
  emphasised labels, an anchor without its table, label spacing, hidden text inside a table, the
  WINDOW_MISSING wording and the LTM start date.

Not verified: Windows/Edge rendering; any issuer other than TDG; a non-Q1 year-to-date window with
real data; in-app runs still publish no model (Decision 10); the weekly full suite.

## 2026-11-08 — Phase 4: derived rows in calculation.json (branch `claude/model-derived-rows`)

Scope: Tasks 7-8 (5139dc9f..60c101c7), the Low batch 33be4f6c and the end commit; macOS only.
Phase diff against origin/main: 652 changed lines (cap 800). **Deterministic retained-data**
check: TDG `runs/cpos-tdg-model-001` inputs, no provider call; not a live model run.
- Answer-key correction: the plan said FY2024 senior secured debt 13,932 and 3.34x. The register's
  8 secured rows (486+8642+2077+2727+1438+984+2180+1486) give 20,020 and 4.80x (20020/4173); the
  store derives the same total.
- Controller live check (real app, retained data): Forecast grid FY2024 revenue growth 20.58%, gross
  margin 58.84%, Adj EBITDA margin 52.56%, Adj EBITDA growth 22.92%, senior secured leverage 4.80x;
  FY2023 growth 21.29% / 28.31%; FY2022 growth n.a.; FY2022/23 senior n.a.
- Reviews: Task 7 mx-precise approve; Task 8 mx-precise + mx-adversary, one fix round, re-review
  approve; phase mx-architect approve (two Low, fixed in the end commit: register problems resolve
  in the store's order, a negative divisor reads "a divisor is zero or negative").
- Gates after the end commit: targeted pytest (241 passed) exit 0; `tools/quality_gate.py` exit 0;
  `validate.py full` exit 0 (node 275, python 526, go, ruff).
- Owner items (predate the change): an escaped `\|` in a register cell parses differently in the
  store; subtotal rows such as "Secured notes subtotal" are counted by both readers; `op_prefer`
  ignores a recorded unit (accepted, Decision 7).

Not verified: Windows/Edge rendering of the new cells; a 52/53-week issuer other than the
constructed periods; in-app runs still publish no model (Decision 10); the weekly full suite.

## 2026-11-08 — Resume a stopped run (branches claude/resume-core, claude/resume-run)

Scope: Tasks 4-6 of the deferred-features plan.
- Resume creates a new reviewed job; only cap and max turns may change. A stopped run's accepted
  modules are replayed without a call.
- Replayed bytes come from CP-OS's accepted record, `requests/<m>/<fp>/<n>.response.md`, with an
  issue-free review and a matching sha.
- A module is kept only while its sources (context included), upstream, instructions and model
  setting match and the current checker accepts it. The prefix ends at the first mismatch; the
  review names the reason.
- Resume copies only the job's listed regular files and never follows symlinks. Start recomputes the
  review id from the plan it will run, before any call. The stopped run's folders are never written.
- Reviews: mx-precise 1 Medium (sources the answer never saw); mx-adversary 3 Mediums (replay from
  the app's copy; instructions and model not pinned; Start re-reading after the id matched);
  re-review 1 Medium (an edited copy blocked Start). All fixed in 2 rounds.
- Probes exit 0: adv3-instructions, adv3-start-toctou(-sources), adv3-resume-id, adv3-context,
  adv3-stopped-run-untouched, p3-sources-changed, rr3-accepted-selection, rr3-start-record-window,
  rr3-checker-at-review, rr3-corrupt-record, rr3-copy-edges.
- Superseded by the design change: adv3-replay-bytes (the controller confirmed the replayed bytes
  equal the model's accepted answer, not the edit), rr3-copy-start, adv3-go's whole-tree-copy case,
  p3-copyfs-symlink.
- Not verified: a real paid resume; the Go-to-Python engine path end to end (the Go tests use
  fakeEngine); Windows.

## 2026-11-08 — Native Windows notice (branch `claude/native-toast`)

Scope: Task 3 of the deferred-features plan.
- Behaviour: when a run finishes, the server waits up to 75 s for a run-list poll that arrives after
  the finish, and shows a Windows toast only if none arrives. This gives exactly one notice whether a
  tab is watching, the tab is in the background, or no tab is open. The 75 s replaces the plan's 15 s,
  because Edge and Chrome slow a hidden tab's polling to about once a minute.
- How the toast is shown: PowerShell, located through `GetSystemDirectoryW`, runs a fixed script. The
  text reaches it only through environment variables. The child gets an allowlisted environment with
  no provider keys. A 20 s timeout applies, and any failure is logged and never affects the run. On
  other platforms nothing is launched.
- Reviews: mx-precise and mx-adversary each found two Medium issues: provider keys in the child
  process, global swaps in the tests that raced, a test that did not wait, and background tabs getting
  a double notice. All four were fixed in one round. The re-review passed.
- Probes exit 0: `adv2-env`, `adv2-race`, `adv2-tests-launch` (0 real launches), `adv2-injection`,
  `adv2-child`, `p2-case-a-window`.
- Not verified: the toast on real Windows; `GetSystemDirectoryW` at runtime; real hidden-tab
  throttling; a notice pending while the app quits; managed-machine policy (Constrained Language Mode,
  security alerts on PowerShell launches).

## 2026-11-08 — Run activity page (branch `claude/run-activity`)

Scope: Tasks 1-2 of `docs/superpowers/plans/2026-11-08-deferred-features.md`; macOS only, in-app browser pane.
- Page: `GET /api/runs/events?id=` serves a run's `events.jsonl`; the Run activity page lists the events,
  recorded spend and stop reason; a cut or oversize log shows its complete events and says the record is incomplete.
- Review: mx-precise approved; probe `p1-events.sh` exits 0.
- First paid live run, started by the owner on 2026-11-08: `web-625c3c5138d54dcbfb84b9bd963e48c3`, CP-0 + CP-1,
  sol-medium gpt-6.1-sol, cap USD 10, hold USD 5.73. Each module had one rejected draft, was repaired and accepted;
  the report was delivered; spend USD 0.58813770. Coverage entries: CP-0 18, CP-1 37; both modules recorded as
  `live-provider`. The front line "Source readiness: confidence Medium; …" leads the report. The app showed `● 0/2`,
  then `● 1/2` and the reload prompt. The Run activity page at this branch listed every event of that run.
- Not verified: Windows Edge; the look of `.activity-log`; a real 4 MiB log.

## 2026-11-07 — Phase 3 and branch end: identity, handoffs once, manifests once, workspace cache (branch `claude/system-design-remaining-calls-e06c23`)

Scope: Tasks 7-10 (commits ec18373f..3976be83), the end batch 9b3215fa and the final batch 398ae209;
macOS only. The live test used a copy of the retained app run `web-04cd5a…` (retained data, no
provider call).
- Payload probe `adv-security-handoff-hardlinks`: the workspace payload falls from 560 MB to 20.1 MB
  at 28 hardlinked runs.
- Cache live test (real app at 3976be83, in-app pane): `/api/workspace` 196,096 bytes; 82 ms, then
  5 and 11 ms from the cache; appending a run file gave one rerun (84 ms), then 4 ms. Overview
  renders through hydrate.
- Task reviews (Fable): Tasks 7, 8, 9, 10 Approved; Task 10 race probes `task10-races.go/.sh` exit 0.
- `validate.py` full exit 0 at 3976be83 (node 273, python 521, go test/vet incl. windows, amd64/arm64
  builds, ruff). The diff ec18373f..3976be83 is 800 lines, at the cap.
- End batch 9b3215fa: probes 0; quick 0; quality gate 0 (230 passed).
- Whole-branch Fable review (0c596eac..9b3215fa): Ready to merge. Its three Lows were fixed in
  398ae209 and the controller reran the probes (`branch-stop-reason-unknown-charge.py`,
  `branch-stop-in-delivery.sh`, `branch-double-gaps-heading.py`): 0, 0, 0.
- Final: `validate.py` full exit 0 at 398ae209 (node 275, python 523, go test/vet incl. windows,
  amd64/arm64 builds, ruff); `tools/quality_gate.py` exit 0.
- Owner items: `tests/test_retained_planning.py::test_issuer_identity_cannot_be_assembled_across_title_and_request`
  fails at base 0c596eac and is not in `tests/nightly-known-failures.txt`; `_literal_tables` is not
  fence-aware (pre-existing, cannot cause a false failure); Task 10 `clear()` waits behind an
  in-flight store run (latency only); Task 8/9 Info notes.
- Not verified: the browser gate (`FW_PLAYWRIGHT_PYTHON` unset); the
  workspace reload on Windows; any provider run.

## 2026-11-07 — Phase 2: delivery gaps, coverage record, front lines (branch `claude/system-design-remaining-calls-e06c23`)

Scope: Tasks 4-6 (commits 74c66963..ec18373f, 799 changed lines) and the banner fix a46f6976 that
the owner prompted ("Looks like wrong frontend"); macOS only.
- Live test (deterministic retained-data rebuild, not a model run): the handoffs CP-0, CP-1 and
  CP-1A of `runs/web-04cd5a5d02ea7d1dea714a8a6632cd21` rebuilt at ec18373f into a scratch copy with
  the launcher's front routes; `runs/` untouched. The coverage check passes (CP-0 14, CP-1 32, CP-1A
  22 entries). CP-1 limitations are 2 fixed plus 9 gap rows, matching the 9 data rows of its Gaps
  table (independent awk count). The first view came from a scratch static server, not the app;
  `#delivery-limits` had no class and rendered unstyled. a46f6976 gives it `class="banner"`
  (RED/GREEN test; quick 0; quality gate 0), then it was viewed in the real Issuer Library app.
- Reviews (Fable): Task 4 Approved (probe `task4-hostile-gaps.py` 0); Task 5 passed after 2 fix
  rounds (5 probes 0); Task 6 passed after 1 round (`task6-manifest-roundtrip.py` and `-v2` 0).
- `validate.py` full exit 0 at ec18373f (python 513, node 271, go, ruff).
- Finding: the in-app pane does not paint sandboxed iframes (srcdoc probe: sandbox, not painted;
  no sandbox, painted); the report frame is equally blank on main. The in-app report frame therefore
  still needs checking in Edge/Chrome on Windows.
- Owner item: `tests/test_retained_planning.py::test_issuer_identity_cannot_be_assembled_across_title_and_request`
  fails at HEAD with src reverted and at base 0c596eac, and is not in `tests/nightly-known-failures.txt`.
- Not verified: the report frame in the real app on Windows (Edge/Chrome); a model-written handoff
  through the new coverage check (only retained handoffs); `validate.py` full after a46f6976 (quick
  and quality gate only); the browser gate (`FW_PLAYWRIGHT_PYTHON` unset).

## 2026-11-07 — Phase 1: run event log and app run watcher (branch `claude/system-design-remaining-calls-e06c23`)

Scope: Tasks 1-3 and the cleanup (commits 7afa9551..74c66963), 940 changed lines, over the 800-line
PR cap (tests about 350); macOS only. Natural split for the owner: Task 1 | Tasks 2-3.
- Live test, SYNTHETIC: an event log written into a scratch workspace, read by the real Go server and
  the real UI in the in-app pane. Running showed title "● 1/2 · Issuer library · Issuer Library",
  rail "Run running, 1 of 2 modules" and "turn 1 of 24", "USD 0.26 of a USD 10 cap; the next call
  holds USD 5.73". A stop(budget) was seen by the 5 s watcher (title "!", "Run stopped").
  The real worker-to-events path is covered by fakes only. The notification was not exercised
  (pane permission "denied").
- The paid live CP-OS run (CP-0 and CP-1, cap USD 10) was denied by the permission classifier and
  was not run; it remains an owner decision. The review step (no model call) ran live: hold 5.73,
  provider_ready true.
- Reviews (Fable): Task 1 fixed once (event writes made fail-open; probe v2 0); Task 2 Approved;
  Task 3 fixed once (notification click with a draft open; probe 0); cleanup Approved (probe
  `cleanup-external-gate.sh` 0).
- Gates: `validate.py` full first failed on ruff only (RUF100 on `noqa` that `tools/quality_gate.py`
  requires; the two gates disagreed); after 74c66963 (ruff `external` codes, unused `on_start`
  removed) it exits 0. The first full run otherwise passed (node 271, python 507, go).
- Owner items: the paid live run; the 940-line size above.
- Not verified: the real worker writing events under a provider; the notification; the Windows UI;
  the browser gate (`FW_PLAYWRIGHT_PYTHON` unset).

## 2026-11-07 — First nightly run triaged (branch `claude/nightly-disk`)

Scope: nightly run 42351518717 on main 3bff5e8, its runner faults and its 94 failures not on
`tests/nightly-known-failures.txt`. Offline in this container; CI reruns only, no provider call.
- Runner: two shards' disks filled (each workflow store holds about 120 MB of issuer sources and
  pytest kept every `tmp_path`); one shard ended with exit -11 (no trace: its log is an artifact the
  proxy cannot fetch). Fix: a passing test's `tmp_path` is deleted, unused runner toolchains are
  dropped, 8 shards instead of 6, and each shard prints its log's last 400 lines to the job log.
  Module and session fixtures' directories stay (some are shared across modules). A
  `workflow_dispatch` with `tests` (and `ref`) reruns only those ids. The full-run fix itself is not
  yet proven: it needs the next full run.
- Triage: CI reruns of the 92 slow failures on this branch (42369485755) and at 5dd01ec, before
  the review fixes (42369487867). 89 fail at 5dd01ec with the same message, most of them fixtures
  whose publication is refused in the CP-OS and S1A suites; they go on the known list. One fast
  failure fails at 5dd01ec too (known list).
- Regressions from the review fixes, fixed: CP-2D's pinned-assumptions label now follows the
  analyst's stated limitations (S06-C02; T4 L2/L3); the CP-2E FY-header test passes the pack's
  currency; the CP-DR off byte-identity test undoes the deliberate S13-A04/C07 and S14-C04 CP-0
  sentences with their strip helpers, and run.json and the run tree then equal the unchanged
  checkpoint 65d1a180 fixture.
- Review (model matrix): a Sonnet review of each commit. It added the rerun-id guard; its module
  fixture cleanup was reverted because it deleted directories later modules reuse
  (`tests/cpdr_runs.py` `closed_run`, the session prompt pack). The second review confirmed.
- Checks (fast, `timeout 300`): `tests/test_nightly_tests.py` 10 passed;
  `tests/test_periods_currency_misc.py` passed; the three regression nodes 9 passed;
  `tests/test_method_cp2d.py` and `tests/test_connect_cp2d.py` 434 passed, 2 failed (known list);
  `cases/pins.py --check` 219 paths; quality gate 0 findings. Not run: the workflow YAML lint (the
  linter download was refused); the full suite (next scheduled run).
- Schedule (user ruling, 2026-11-07): weekly, Sunday 01:00 UTC, since a full run takes about 17
  runner-hours of this private repository's Actions minutes.

## 2026-11-07 — Confidence review of the whole app

Scope: 14 slices of the app at a313b50, each reviewed by a Sonnet agent and checked in the main
session. A patch was kept only when its new test failed on the a313b50 source and passed after.
Merged with main after `claude/review-fixes`, which had fixed several of the same defects; main's
versions were kept for the run-list order and review write timeout (`jobs.go`), the stray
`CP-1a.md` (`store.py`), the gate key list (`validate.py`), the `rv_quotes` exponent, the
calendar-quarter delta core (`earnings.py`, owner ruling: delta core only, B19 unchanged) and
R5b. `cpos_handoffs.py` was deleted on main, so its UTF-8 fix lapses. Fixes this entry adds:
- a stale status reply no longer overwrites another run's screen (`actions.js`);
- the budget's directory fsync goes through `platform_io` (`budget.py`); Windows refuses
  `os.open` on a directory, so a paid run would have stopped creating its budget (simulated);
- `search_source` matches on the page itself (U+0130, `handoff.py`);
- journal writes retry through `platform_io.replace` (`execution.py`);
- the CP-2 `**Key risks:**` line is kept among limitations (`handoff_delivery.py`);
- `_scale_of` keys on the resolved scale label (owner ruling, `report_view.py`), clearing the
  T4.9 `mixes amount units` refusal.
Rejected: joining split negatives `(1,234 )` (0 of 43,461 corpus lines; breaks the spacing
invariant); chart text at the handoff's precision (display-only; stops a retained delivery
verifying).
Open for the owner: a leftover `run.json.tmp` blocks a resume; `os.rename` at
`run_inputs.py:581`; `_stated` drops a cell's note; CP-1D reads `25bps` as 25; `.copilot-home`
depends on the launcher's working directory; an undecodable source leaves its module folder, so
a rerun says `cpos_live_already_started`; 25 of 27 retained deliveries do not verify under
current code (as at a313b50).
Checks after the merge: `tools/quality_gate.py` 0 findings in 10 changed files;
`cases/pins.py --check` matches 219 paths; 371 of 373 affected Python tests pass, and the 2
failures (`test_cp2e_refuses_the_fy_2025_header_under_fy_2026`, `test_no_hardcoded_period_left`)
fail on a clean main tree too; the nine web test files (191) and `go vet`/`go test` pass.
GitNexus: this repo is not indexed.
Not verified: real Windows; any provider; the whole suite; `test_financial_workflow.py` after the
merge (it passed 21 before it, agent-run, and exceeds the five-minute limit).

## 2026-11-07 — Fixes for the whole-app review findings (branch `claude/review-fixes`)

Scope: the 253 agreed findings of the whole-app review (`docs/review-handoff/` on
`claude/review-handoff`): 4 critical, 49 high, 94 medium, 106 low after the cross-review.
326 files against `claude/quality-gate` (src/deploy_workflow 95, src/deploy_vii 45,
apps/issuer-library 28, tests, five case oracles rebuilt by their own builders and re-pinned).
No change under runs/ or deliverables/. Offline only: no provider call, network fetch or key.
Method (user): a model matrix. Each batch was fixed by one model and reviewed by the other
(Opus/Sonnet). The reviewer confirmed or repaired each commit, ran a rewrite tournament and
adversarial tests, and committed separately. Every merge passed the changed-code gate
(`tools/quality_gate.py`, 0 findings at the end over 253 changed files) and targeted fast tests
only (each pytest call under `timeout 300`; no test_owner_*, nothing promoting CP-0/CP-1). Frozen
prompt digests: each deliberate wording change has a strip helper (`tests/prompts/s*_strip.py`),
and the digest failures equal main's 26 by name. The rule-list golden sha256 section was refreshed
after wave 1 and again at the end, each in its own commit. `cases/pins.py --check` matches 219
paths.

| Severity | Fixed | Partly fixed | Kept as is by user ruling | Already fixed by an earlier fix | Not a defect / not reachable |
|---|---|---|---|---|---|
| critical | 4 | 0 | 0 | 0 | 0 |
| high | 45 | 4 | 0 | 0 | 0 |
| medium | 91 | 2 | 0 | 1 | 0 |
| low | 94 | 3 | 4 | 2 | 3 |

User rulings (2026-11-07), applied through the same matrix with a review each:
- S12-A02: option B, fail closed. A positive `signed` amount on an outflow-linked line is refused.
  A printed magnitude uses `outflow_magnitude`. A refund is recorded as missing with its reason, and
  the coverage gate accepts that withheld line. `o2-synthetic` was corrected through its builder.
- S10-A05: a native CP-8 that CP-0 commands is recorded as refused (superseded, pointing to CP-OS
  `run_comparison`) and the run finishes with a verified receipt.
- S18-C03: a per-launch secret held in memory only. The one-time launch ticket expires after 120 s
  and is exchanged for a SameSite=Strict session cookie. Same-site and cross-site requests are
  refused. A relaunch asks an idle library to quit through an owner-only request file and then
  opens a fresh link; a busy library answers with what is running.
- S18-C08: a workspace switch is refused while a review is in flight.
- S08-C08: interest covers are n.m. when adjusted EBITDA is ≤ 0.
- S08-C09: an Insufficient Information preference has an empty ordering.
- S13-A07: the financial-synthesis scope is gated per dimension.
- S09-A08: a "Same definition" naming a document missing from the pack must be "Not determinable".
- S09-C04: the source-refusal wording is corrected.
- S09-A04 remainder: CP-4C picks the secured facility by T4.18 status. Its other upstream faults
  are typed issues. A hopeless facility issue is refused at begin (no model call); the verifier
  recomputes the reason from that snapshot's CP-1 head.
- CP-4 missing-document check: "set forth in", "specified in" and "ascribed to" also count as
  pointers, and memorandum and prospectus as document nouns.
- S04-C11: the Model rail highlight is fixed.
- CP-2E accepts "$m", "US$m" and "USDm" as millions, and refuses a unit statement that names a
  currency other than the run's reporting currency. CP-1D matches its Basis clause without regard
  to case, and its second-currency guard reads ISO 4217 codes only.
- Refund handling: `outflow_magnitude` is refused on a line whose label states an inflow (outside a
  "net of" clause), and an accounts row cannot contradict a withheld line.
- S14-A02: the read-window bound is confirmed, superseding the PF-R7 exemption (recorded in
  `cases/pilot-fixes/read-window.json`).
- S15-C05: splitlines numbering is canonical (documented in `preparation.text_content`).
- Kept as is: S03-C06, S05-C07, S13-C10 and the fail-closed confirmations.

Partly fixed: S07-A01 (strict xfail `test_a01_quarter_cp2a_swapped_metric_is_refused`), S11-A03,
S13-A03/C05, S01-A03, S06-A06, S07-C03, S05-C09, S09-C06. Also fixed: three defects reviewers found next to fixed findings
(non-UTF-8 lines in the source and financial servers, now one shared `workflow.read_line` that
the owner server also uses; lone surrogates in research manifests; the CP-4 stored claim
limitation).
Branch review (one final reviewer over the whole branch, report only): verdict merge, no blocker
or high finding; conflict resolutions coherent; every composed-prompt difference across the 12
step contracts maps to a named finding. Its low items were fixed through the matrix: comments
opened mid-line are hidden too, financial_workflow (and owner_workflow through it) uses the atomic
`workflow._put`, and the CP-4 context.py pin test is renamed to what it checks.
Known-failure list: 45 more base failures found during the waves and confirmed on
`claude/quality-gate` were added (`tests/model` ruling files, `tests/prompts` fence/compose,
coverage rule, prompt-set digest, the 26 frozen-message digest failures, one o2 citation test, the
financial-workflow full-component fixture and two research consumer-block stubs). The Issuer
Library launch secret and relaunch quit request also need Windows and browser acceptance: the
launch link and cookie in the report frames, the state-folder ACL check, the polling watcher,
port rebinding and the dialogs.
Not verified here (slow or not runnable in this container; the nightly run covers the pytest
ones): every `test_owner_*` suite, including those touched by replay reuse, owner rendering, CP-0
attachments and the shared `read_line`; test_run_pathway*, test_run_inputs, test_cp1_hybrid_offline,
test_financial_workflow and test_host_h1 as a whole; the Issuer Library jsdom suites and
browser_check; the Windows path of the S18-A07 worker lock (compiled and vetted only). Retained-data
checks were deterministic replays of retained outputs, not live runs.

## 2026-11-07 — Nightly full-suite run; gate fix for duplicate module names

Scope: `.github/workflows/nightly-tests.yml`, `tools/nightly_tests.py`,
`tests/test_nightly_tests.py`, `tests/nightly-known-failures.txt`, a docs/QUALITY-GATE.md section,
one AGENTS.md bullet, and a fix in `tools/quality_gate.py`. No analytical code changed.
Decision (user): while working, fast targeted tests only; the full suite, slow tests included,
runs nightly at 01:00 UTC in GitHub Actions (user chose Actions over a Claude cloud session and
UTC). Six pytest shards balanced by file size, `live`/`browser` excluded, provider keys removed,
300 minutes per shard; Go `vet` and `test -race`; a report job fails only on a failure missing
from the known list or an unfinished shard. The known list is seeded with the 24 base failures
documented in the review handoff; the first run will show any other pre-existing failure as new.
Gate fix: two changed files with one module name (two `builder/build.py`) made mypy exit 2, and
the gate raised before its per-file fallback; the fallback now runs first. Found by the S13 fix
review. `tests/test_quality_gate.py` gains the case: it raises GateError on the old gate and
passes on the new one.
Checks: `tests/test_nightly_tests.py` 9 passed and `tests/test_quality_gate.py` 8 passed (fast,
`timeout 300`); the workflow parses (jobs pytest, report, go; schedule `0 1 * * *`); the gate on
this change exits 0. Not verified: the workflow has not run. Scheduled runs start once it is on
`main`; its first run establishes the real known-failure list and duration.

