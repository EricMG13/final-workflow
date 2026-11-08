# Run Expectations and Accepted Limitations Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax. Subagents are permitted for
> implementation, review and verification (`AGENTS.md`); expected values are never written by the
> agent that writes the code they check.

**Goal:** Before Start, tell the user what each module is expected to produce from the files and
context they supplied, why, and what would improve it, and require them to accept the listed
limitations. Users should not discover a forgotten file or a weaker module outcome only after a
paid run, so re-runs fall.

**Architecture:** One offline rule set in Python, inside the CP-OS launcher's existing review.
`prepare()` already reads every source's pages. It now also guesses each file's document kind
from its name and first pages, and derives one expected outcome per module from those guesses,
the context and the module dependencies. The bridge returns both in the review. The app shows
them first on the Review step. Start requires a separate acceptance whenever anything is below
Ready. The acceptance and the expectations are written into the run folder before any provider
call. No new orchestration layer, no model call, no change to what modules conclude.

**Tech Stack:** Python 3.13 (stdlib, pydantic), Go, plain browser JavaScript; jsdom test-only.

**Spec:** the Decisions section below, per the one-record rule in `AGENTS.md`.

## Decisions

| Finding (2026-11-08) | Decision |
|---|---|
| No offline code classifies uploaded files; only the extension is checked (`cpos_launch.py:299-345`) | Add a conservative document-kind guess from file name plus the first 3 pages already parsed in `_issuer_files` |
| App runs give every file to every module; nothing is gated by document kind (`owners/cpos.py:404`) | Expectations inform; they never block a run or filter sources |
| The review already lists ignored files and omitted report sections (`bridge.py:244-287`) but not why a module will be weak | Add per-module expected outcomes with reasons and fixes, shown before the module list |
| Module rules on missing inputs live in owner code and method text (e.g. `cp2h.py:1974-1985`, `cp3d.py:2215`, `cp1d.py:1015`) | Each rule cites its method/owner line and is labelled **observed** (seen in a retained handoff) or **per method only** |
| Retained handoffs show some predicted outcomes ("Insufficient Information" in 300 files, "not calculable" in 58) and not others ("Rating register not found" in 0) | Back-test the rules against the 21 retained launcher runs (`runs/*/workflow.json`), read-only, and report agreement with its actual scope |
| The context form's "What this run will do" panel holds a separate JS copy of some rules | Leave the form unchanged in this increment; a test fails if the overlapping rules (quotes/talk, legal documents, ratings, non-USD) disagree |
| `startRun` accepts only `{id, review_id, confirm}` (`jobs.go:716-751`) | Add `accept_limitations`; required only when the review lists any limitation |

**Outcomes, worst first:** `Will refuse` (the module's handoff is expected to be rejected or blocked) ·
`Gap` (a section will state the input as not supplied) · `Limited` (runs with reduced confidence or
scope) · `Check` (no file was recognised as the needed kind; fine if the user knows it is there) ·
`Ready`. A module inherits `Limited: depends on <title>` from a required producer that is worse
than Ready (edges from `registry.plan()` data).

**Wording rule:** every expectation reads as a forecast: "Expected from your files and context. CP-0
confirms during the run; the model may still find less." A guessed kind is shown as "Likely: credit
agreement (found 'CREDIT AGREEMENT' on page 1)", never as fact.

**Rejected:** blocking Start for a missing file (users may knowingly accept gaps); a model call to
classify files (paid execution must stay a separate explicit action); a second checker beside
CP-OS (`AGENTS.md`: no competing orchestration layer); changing `context/1` (saved files must load).

**Out of scope (later plans):** files-first run check with pathway ratings, phased context stages,
context prefill from filings, post-run expected-versus-actual reporting in Run activity.

## Global Constraints

- Offline only. No provider call in any task; gates run with provider keys removed.
- `runs/`, `deliverables/`, `data/public-corpus/` and predecessor repositories are read, never written.
- Expected values (document-kind key, rule outcomes) are hand-written and committed before the code
  they check, by someone other than the code's author.
- Missing is never zero. "Not supplied" stays a visible gap. No new score or aggregate rating.
- Excel stays input-only. No new dependency.
- Branch `claude/intelligent-babbage-b0309i`. Commit per task; push at each checkpoint. No PR unless
  the owner asks.
- One short `VERIFICATION.md` entry per checkpoint. No other review files.

## Validation Schedule

| When | Command | Passes when |
|---|---|---|
| Every task | Named focused tests, each under `timeout 300` | New test seen failing for the stated cause, then exit 0 |
| Every commit | `uv run python tools/quality_gate.py` and `python3 apps/issuer-library/validate.py quick` | Exit 0 |
| **Checkpoint A** (after Task 4) | Back-test report (Task 4) | Every disagreement explained or its rule fixed |
| **Checkpoint B** (after Task 7) | `validate.py full`, then `validate.py browser` | Exit 0; owner accepts the Review screen |

Before each checkpoint: confidence-review (doubts, causes, adversarial cases, fixes) and
rewrite-tournament in post-edit mode on `guess_kind`, `expectations` and the Review renderer.

**Stop rules:** a failing gate stops the next task. Two failed fix rounds on one defect go to the
owner with both outcomes. Never loosen a test to pass.

## Review Focus

1. **A 10-K whose exhibit index names the credit agreement:** classed financial report, not credit
   agreement; CP-4 shows `Check`, not `Ready` (Task 1).
2. **A draft credit agreement only:** CP-4 `Will refuse`, with "drafts are refused" and the fix (Task 2).
3. **Earnings update with one period's statements:** CP-1B `Limited` naming the missing period, not
   `Ready` (Task 2).
4. **Non-USD issuer (Erste):** CP-2D `Limited` for non-USD facilities; no USD labels invented (Task 2).
5. **Hostile file names or context text:** rendered as inert text on the Review step (Task 6).
6. **Stale acceptance:** inputs changed after acceptance; Start refuses and asks for a new review (Task 5).

---

## Phase 1: the rule set (Python, offline)

### Task 1: Document-kind guess

**Files:** create `src/deploy_workflow/run_expectations.py`, `tests/test_run_expectations.py`,
`tests/fixtures/run-expectations/document-key.json`.

- [ ] Hand-label the key first: at least 20 real files from `data/public-corpus/` and
      `runs/*/sources/` (annual reports, 10-K/10-Q, an HTML filing, a non-English report, peer
      filings, a portfolio PDF), plus synthetic text fixtures for kinds the corpus lacks (credit
      agreement executed/draft, indenture, ratings letter, quotes sheet, management bridge,
      prior decision), each labelled synthetic.
- [ ] `guess_kind(name, first_pages) -> Guess(kind, signal, executed)` where `kind` is one of
      `financial_report, earnings_release, credit_agreement, indenture, ratings, market_quotes,
      peer_data, management_bridge, portfolio, prior_decision, unrecognised`; `signal` names the
      matched phrase and page; `executed` is `True/False/None` from "EXECUTION VERSION"/"DRAFT" marks.
- [ ] Cover-page phrases outrank later pages and file names; ambiguity returns `unrecognised`.
- [ ] Tests: key accuracy reported per kind; adversarial cases from Review Focus 1, a misleading
      file name, an empty-text page, an `.xlsx` workbook.

### Task 2: Rules and expected outcomes

**Files:** modify `src/deploy_workflow/run_expectations.py`, `tests/test_run_expectations.py`.

- [ ] `Rule(module, condition, outcome, reason, fix_file, fix_context, basis, evidence)`; one table.
- [ ] Initial rules, each verified against its method/owner text before it is written:

| Module | When | Outcome |
|---|---|---|
| CP-1 | No file likely financial report | Check (all modules depend on it) |
| CP-1B | Earnings run and statements for only one period recognised | Limited |
| CP-1C | No peer file and `valuation.peer_source` is `none`, or `cp_dr_public` without CP-DR | Gap |
| CP-1D | No management bridge | Gap |
| CP-2D | `reporting_currency` not USD | Limited |
| CP-2H | No ratings file and no `ratings` in context | Will refuse |
| CP-3 | No observed quotes (file or context), talk only | Limited |
| CP-3 | No quotes and no talk | Gap |
| CP-3D | No quotes file and no context quotes | Gap |
| CP-4 | No credit agreement or indenture | Gap |
| CP-4 | Drafts only | Will refuse |
| Portfolio pathway | No portfolio workbook | Gap |
| Any | Report section omitted by this pathway (`prepared.omitted`) | Gap |

- [ ] `expectations(ordered, guesses, context, edges) -> tuple[Expectation]`; dependency
      inheritance as in Decisions; output order follows `ordered`.
- [ ] Tests: hand-written expected outcomes for Review Focus 2-4 and one clean case per pathway,
      each labelled synthetic.

### Task 3: Launcher and bridge carry the expectations

**Files:** modify `src/deploy_workflow/owners/cpos_launch.py`, `apps/issuer-library/engine/bridge.py`,
`apps/issuer-library/designs/fake_engine/bridge.py`, `tests/test_cpos_launch.py`, `tests/test_cpos_app.py`.

- [ ] `_issuer_files` keeps the first 3 pages per pinned source for `guess_kind`; nothing else
      changes in what is pinned or refused.
- [ ] `Prepared` gains `documents` and `expectations` (defaulted, so other callers are unaffected).
- [ ] `review()` adds `documents`, `expectations`, `limitations` (count below Ready) and includes
      the expectations in `review_id` material.
- [ ] Tests: review output shape; unchanged refusals; changed expectations change `review_id`.

### Task 4: Back-test against retained launcher runs (Checkpoint A)

**Files:** create `tools/expectations_backtest.py`; add a dated entry to `VERIFICATION.md`.

- [ ] For each of the 21 retained runs with `workflow.json`, compute expectations from its pinned
      sources and context, read-only, and compare with what its accepted handoffs actually state.
- [ ] Report per rule: agreed, disagreed, not testable. Label it "deterministic retained-data
      report", with issuer and date per run; never call it live proof.
- [ ] Fix or relabel every disagreeing rule (`evidence: per method only`) before Phase 2.

## Phase 2: acceptance and the Review screen

### Task 5: Start requires and records acceptance

**Files:** modify `apps/issuer-library/jobs.go`, `apps/issuer-library/jobs_test.go`,
`apps/issuer-library/engine/bridge.py`, `tests/test_cpos_app.py`.

- [ ] `startRun` reads `limitations` from `review.json`; when above 0 and `accept_limitations` is
      not true, answer 400 "Accept the listed limitations before starting"; no claim is made.
- [ ] Go writes `intake/<id>/acceptance.json` `{review_id, accepted_limitations, at}` before the worker starts.
- [ ] `bridge.start` checks it against the approved `review_id`, then writes
      `runs/<id>/expectations.json` (expectations, documents, acceptance) before any provider call.
- [ ] Resume recomputes expectations and needs a fresh acceptance.
- [ ] Tests: refused without acceptance; zero limitations works with the old request; stale review
      refused; file written before the worker's first call.

### Task 6: Review step shows expectations first

**Files:** modify `apps/issuer-library/web/actions.js`, `apps/issuer-library/web/screen.css`,
`apps/issuer-library/web/new-run.test.cjs`.

- [ ] An "Expected outcomes" table opens the Review step: module title, outcome, reason, fix,
      and a "Why we expect this" disclosure with the rule's basis and evidence label.
- [ ] "Files recognised" list: each file's likely kind and signal, or "Not recognised".
- [ ] A second checkbox, "I accept these N limitations", appears only when N > 0; Start is enabled
      only when both boxes are ticked. "Edit folder & budget" and "Edit context" stay one click away.
- [ ] All text set through `textContent`. Tests: rendering, checkbox gating, inert hostile text.

### Task 7: Help, README and checkpoint B

**Files:** modify `apps/issuer-library/README.md` (New run section), Help text in
`apps/issuer-library/web/views.js`, `VERIFICATION.md`.

- [ ] Describe expected outcomes as forecasts and what acceptance records.
- [ ] Run Checkpoint B gates; record results with their actual scope.

## Done when

- The Review step lists an expected outcome for every module in the run, with reason and fix.
- Start cannot be pressed past listed limitations without the separate acceptance.
- Every started run folder holds `expectations.json` with what was expected and accepted.
- The back-test report states rule agreement on retained runs, labelled as retained-data evidence.
