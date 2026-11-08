# Run Expectations, Accepted Limitations and Credit Filters Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax. Subagents are permitted for
> implementation, review and verification (`AGENTS.md`); expected values are never written by the
> agent that writes the code they check.

**Goal:** Before Start, tell the user what each module is expected to produce from the files and
context they supplied, why, and what would improve it, and require them to accept the listed
limitations. Users should not discover a forgotten file or a weaker module outcome only after a
paid run, so re-runs fall. The user also states the issue classification, investment grade or
high yield, in the context's issuer identity section, and the expectations use it. Readers who
only want reports can then find them in the Issuer Library by credit information (classification,
rating, leverage, interest cover, currency, run completeness), not just by sector and workflow.

**Architecture:** One offline rule set in Python, inside the CP-OS launcher's existing review.
`prepare()` already reads every source's pages. It now also guesses each file's document kind
from its name and first pages, and derives one expected outcome per module from those guesses,
the context (including the issue classification) and the module dependencies. The bridge returns
both in the review. The app shows them first on the Review step. Start requires a separate
acceptance whenever anything is below Ready. The acceptance and the expectations are written into
the run folder before any provider call. No new orchestration layer, no model call, no change to
what modules conclude. The workspace reader (`engine/store.py`) then gathers per-run credit facts
from what is already written: the run's context, CP-1's fixed chart tables, the run folder and its
`expectations.json`. The library filters on those values and links each one to its evidence; it
never calculates a figure.

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
| The context form's "What this run will do" panel holds a separate JS copy of some rules | Leave the form's other rules unchanged; a test fails if the overlapping rules (quotes/talk, legal documents, ratings, non-USD, issue classification) disagree |
| `startRun` accepts only `{id, review_id, confirm}` (`jobs.go:716-751`) | Add `accept_limitations`; required only when the review lists any limitation |
| The context has no investment-grade/high-yield field (`context.py:92-103`) | Add `identity.issue_classification`: `investment_grade` or `high_yield`, chosen in the issuer identity section |
| The selected methods are written for high-yield and leveraged-loan issuers (e.g. `cp-2d…/SKILL.md:161`, `cp-2g…/SKILL.md:181`, `cp-3…/SKILL.md:361`, `CP-4_RUNBOOK.md:15`, `cp-6…/SKILL.md:176`); none branches on investment grade | The classification changes expectations, not analysis: for an investment-grade issuer, each module whose method is framed for high yield shows `Limited` with that reason. Adapting methods for investment grade is a separate methodology decision (`METHODOLOGY-REVIEW.md`), out of scope |
| 35 saved context files in `cases/` and the pinned owner-oracle contexts (`cases/PINS.json`) have no such field; `Contract` forbids unknown keys and requires declared ones | Required in the form (no preselected default, so nobody is silently misclassified); optional in the reader, where `""` means **not stated**. Schema stays `context/1`; existing fixtures and pins are not edited |
| Library filters are sector, workflow, as-of year, content and module, plus search (`views.js:328-341`); none is credit information | Add a **Credit** filter group and credit columns; keep the existing filters under **More filters** |
| `store.py` already parses CP-1's fixed chart tables (`Chart data: leverage`, `interest cover`, `liquidity`, `debt maturities`) with period, unit and basis (`store.py:463-478`) | Leverage, interest cover and liquidity filters read those values exactly as written, latest period; no recalculation |
| Only 2 of 44 retained runs hold the fixed leverage table; older handoffs use varying headers | Older runs show **Not recorded**; no guessing from old tables. Each filter shows its coverage ("recorded for 2 of 44 runs") |
| No handoff has a parsed ratings table; CP-2H runs only in Distressed & Restructuring | Ratings come from the run's context (user-entered, dated, labelled so). A fixed CP-2H register table is a later plan |
| `store.py` imports only the standard library so a page load does not pay for the engine (`jobs.go:56-57`) | Read the context fields it needs with a small stdlib parser, reached through `workflow.json`'s `context` source and checked against its sha256; a test proves it agrees with `load_context` on every case fixture |
| An issuer's runs span years (e.g. Berkshire 2008-2017) | Credit filters apply to each issuer's **latest run** by default, with "Any run" as an option, so an old figure never qualifies an issuer silently |
| Amounts carry a currency and unit; ratios do not | Ratio filters work across currencies. Amount filters (liquidity) require choosing one currency first. No FX conversion |

**Outcomes, worst first:** `Will refuse` (the module's handoff is expected to be rejected or blocked) ·
`Gap` (a section will state the input as not supplied) · `Limited` (runs with reduced confidence or
scope) · `Check` (no file was recognised as the needed kind, or two inputs disagree; fine if the user
knows why) · `Ready`. A module inherits `Limited: depends on <title>` from a required producer that
is worse than Ready (edges from `registry.plan()` data). Items about the whole run, such as the
issue classification, are listed under **This run** above the modules.

**Wording rule:** every expectation reads as a forecast: "Expected from your files and context. CP-0
confirms during the run; the model may still find less." A guessed kind is shown as "Likely: credit
agreement (found 'CREDIT AGREEMENT' on page 1)", never as fact.

**Rejected:** blocking Start for a missing file (users may knowingly accept gaps); a model call to
classify files (paid execution must stay a separate explicit action); a second checker beside
CP-OS (`AGENTS.md`: no competing orchestration layer); a new schema version or a required reader
field (saved files and pinned fixtures must load unchanged); inferring the classification from
ratings without asking (ratings are optional and may be split or stale).

**Out of scope (later plans):** files-first run check with pathway ratings, phased context stages,
context prefill from filings, post-run expected-versus-actual reporting in Run activity,
investment-grade variants of the methods, a fixed ratings register table written by CP-2H,
credit metrics for runs that predate the fixed chart tables, saved named filter views.

## Global Constraints

- Offline only. No provider call in any task; gates run with provider keys removed.
- `runs/`, `deliverables/`, `data/public-corpus/`, `cases/` fixtures and predecessor repositories
  are read, never written.
- Expected values (document-kind key, rating-scale table, high-yield-framed method list, rule
  outcomes) are hand-written and committed before the code they check, by someone other than the
  code's author.
- Missing is never zero. "Not supplied" and "not stated" stay visible. No new score or aggregate.
  A missing or not-meaningful figure never satisfies a numeric filter.
- The library reads values modules wrote; it never calculates, converts currency or rescales units.
- Excel stays input-only. No new dependency.
- Branch `claude/intelligent-babbage-b0309i`. Commit per task; push at each checkpoint. No PR unless
  the owner asks.
- One short `VERIFICATION.md` entry per checkpoint. No other review files.

## Validation Schedule

| When | Command | Passes when |
|---|---|---|
| Every task | Named focused tests, each under `timeout 300` | New test seen failing for the stated cause, then exit 0 |
| Every commit | `uv run python tools/quality_gate.py` and `python3 apps/issuer-library/validate.py quick` | Exit 0 |
| **Checkpoint A** (after Task 5) | Back-test report (Task 5) | Every disagreement explained or its rule fixed |
| **Checkpoint B** (after Task 8) | `validate.py full`, then `validate.py browser` | Exit 0; owner accepts the Context and Review screens |
| **Checkpoint C** (after Task 11) | `validate.py full`, then `validate.py browser` | Exit 0; owner accepts the Library screen |

Before each checkpoint: confidence-review (doubts, causes, adversarial cases, fixes) and
rewrite-tournament in post-edit mode on `guess_kind`, `expectations`, the rating-scale check,
the Review renderer, the credit-facts reader and `filterLibrary`.

**Stop rules:** a failing gate stops the next task. Two failed fix rounds on one defect go to the
owner with both outcomes. Never loosen a test to pass.

## Review Focus

1. **A 10-K whose exhibit index names the credit agreement:** classed financial report, not credit
   agreement; CP-4 shows `Check`, not `Ready` (Task 2).
2. **A draft credit agreement only:** CP-4 `Will refuse`, with "drafts are refused" and the fix (Task 3).
3. **Earnings update with one period's statements:** CP-1B `Limited` naming the missing period, not
   `Ready` (Task 3).
4. **Non-USD issuer (Erste):** CP-2D `Limited` for non-USD facilities; no USD labels invented (Task 3).
5. **Investment-grade issuer on Credit Snapshot:** each module with a high-yield-framed method shows
   `Limited` with that reason; a high-yield issuer on the same files shows none of these (Task 3).
6. **Ratings disagree with the choice:** context ratings all BBB+ with high yield selected → `Check`;
   split ratings (BBB- and Ba1) → no flag (Task 3).
7. **An older context.json without the field:** loads in the reader as not stated (`Check` under This
   run); loads in the form with the choice empty and the Issuer step marked to fix (Tasks 1, 3).
8. **Hostile file names or context text:** rendered as inert text on the Review step (Task 7).
9. **Stale acceptance:** inputs changed after acceptance; Start refuses and asks for a new review (Task 6).
10. **Missing is not a pass:** "Net leverage below 4x" excludes runs with no figure or "n.m."
    and says how many it hid; it never treats them as 0x (Task 10).
11. **Old figure, newer run:** an issuer whose latest run has no figure does not match on an older
    run's figure unless "Any run" is chosen (Task 10).
12. **Mixed currencies:** a liquidity filter in USD never shows a EUR issuer's amount (Task 10).
13. **Tampered context:** a context whose bytes no longer match `workflow.json`'s sha256 gives
    Not recorded and an entry in Settings issues, not its values (Task 9).
14. **Split ratings:** BBB- and Ba1 match "Lowest rating: Ba1/BB+ or worse" and show both agencies (Task 10).

---

## Phase 1: context field and rule set (offline)

### Task 1: Issue classification in the context

**Files:** modify `docs/templates/context-form.html`, `docs/templates/README.md`,
`apps/issuer-library/web/context-embed.js`, `src/deploy_workflow/context.py`,
`tests/product/test_context.py`, `apps/issuer-library/web/context-embed.test.cjs`; regenerate
`apps/issuer-library/web/context-form.html` with `apps/issuer-library/packaging/sync_assets.py`.

- [ ] Form: an "Issue classification" choice directly after Issuer ID, tagged Required, with no
      option preselected. Cards: **Investment grade** ("Rated BBB-/Baa3 or above, or managed as
      investment grade") and **High yield** ("Below investment grade, including leveraged loans").
      Help line: "The workflow's methods are written for high-yield and leveraged-loan issuers."
- [ ] `build()` emits `identity.issue_classification`; `fill()` reads it, leaving the choice empty
      (and the Issuer step marked to fix) when an older file lacks it; review summary and panel
      show it, the panel adding the investment-grade limitation.
- [ ] Embed: the choice stays visible in the Issuer section; it is not moved into "Additional issuer
      details" (the embed currently moves every identity fieldset there).
- [ ] Reader: `Identity.issue_classification: Literal["", "investment_grade", "high_yield"] = ""`;
      any other value refused, naming the path.
- [ ] Tests: older file loads as `""`; each valid value round-trips; invalid value refused; the
      existing form-output and parity tests cover the new field; the field is visible in the embed;
      `cases/PINS.json` unchanged.

### Task 2: Document-kind guess

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

### Task 3: Rules and expected outcomes

**Files:** modify `src/deploy_workflow/run_expectations.py`, `tests/test_run_expectations.py`;
create `tests/fixtures/run-expectations/rating-scale.json`, `tests/fixtures/run-expectations/hy-framed-methods.json`.

- [ ] Hand-write first: the rating scale (S&P and Fitch `BBB-` and above, Moody's `Baa3` and above
      are investment grade; outlook and watch ignored; agency "Other" or an unreadable rating is not
      counted) and the list of modules whose method files in `METHODS` are framed for high yield,
      read from the text each module is actually sent (found so far: CP-2D, CP-2E, CP-2G, CP-3,
      CP-4, CP-6; confirm against `METHODS`).
- [ ] `Rule(scope, condition, outcome, reason, fix_file, fix_context, basis, evidence)`; one table;
      `scope` is a module or `run`.
- [ ] Initial rules, each verified against its method/owner text before it is written:

| Scope | When | Outcome |
|---|---|---|
| Run | Issue classification not stated (older context file) | Check |
| Run | Context ratings all investment grade but high yield selected, or all below but investment grade selected | Check |
| Run | Distressed & Restructuring with investment grade | Check |
| Each high-yield-framed module | Investment grade selected | Limited |
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

- [ ] `expectations(ordered, guesses, context, edges) -> tuple[Expectation]`; run-level items first,
      then modules in `ordered`; dependency inheritance as in Decisions.
- [ ] Tests: hand-written expected outcomes for Review Focus 2-7 and one clean case per pathway for
      each classification, each labelled synthetic.

### Task 4: Launcher and bridge carry the expectations

**Files:** modify `src/deploy_workflow/owners/cpos_launch.py`, `apps/issuer-library/engine/bridge.py`,
`apps/issuer-library/designs/fake_engine/bridge.py`, `tests/test_cpos_launch.py`, `tests/test_cpos_app.py`.

- [ ] `_issuer_files` keeps the first 3 pages per pinned source for `guess_kind`; nothing else
      changes in what is pinned or refused.
- [ ] `Prepared` gains `documents` and `expectations` (defaulted, so other callers are unaffected).
- [ ] `review()` adds `issue_classification`, `documents`, `expectations`, `limitations` (count
      below Ready) and includes the expectations in `review_id` material.
- [ ] Tests: review output shape; unchanged refusals; changed expectations change `review_id`.

### Task 5: Back-test against retained launcher runs (Checkpoint A)

**Files:** create `tools/expectations_backtest.py`; add a dated entry to `VERIFICATION.md`.

- [ ] For each of the 21 retained runs with `workflow.json`, compute expectations from its pinned
      sources and context, read-only, and compare with what its accepted handoffs actually state.
      Their contexts predate the field, so the classification rules are reported as not testable.
- [ ] Report per rule: agreed, disagreed, not testable. Label it "deterministic retained-data
      report", with issuer and date per run; never call it live proof.
- [ ] Fix or relabel every disagreeing rule (`evidence: per method only`) before Phase 2.

## Phase 2: acceptance and the Review screen

### Task 6: Start requires and records acceptance

**Files:** modify `apps/issuer-library/jobs.go`, `apps/issuer-library/jobs_test.go`,
`apps/issuer-library/engine/bridge.py`, `tests/test_cpos_app.py`.

- [ ] `startRun` reads `limitations` from `review.json`; when above 0 and `accept_limitations` is
      not true, answer 400 "Accept the listed limitations before starting"; no claim is made.
- [ ] Go writes `intake/<id>/acceptance.json` `{review_id, accepted_limitations, at}` before the worker starts.
- [ ] `bridge.start` checks it against the approved `review_id`, then writes
      `runs/<id>/expectations.json` (expectations, documents, classification, acceptance) before any
      provider call.
- [ ] Resume recomputes expectations and needs a fresh acceptance.
- [ ] Tests: refused without acceptance; zero limitations works with the old request; stale review
      refused; file written before the worker's first call.

### Task 7: Review step shows expectations first

**Files:** modify `apps/issuer-library/web/actions.js`, `apps/issuer-library/web/screen.css`,
`apps/issuer-library/web/new-run.test.cjs`.

- [ ] The context summary line and the Review header show the classification ("Investment grade" /
      "High yield" / "Not stated").
- [ ] An "Expected outcomes" table opens the Review step: **This run** items, then module title,
      outcome, reason, fix, and a "Why we expect this" disclosure with the rule's basis and evidence label.
- [ ] "Files recognised" list: each file's likely kind and signal, or "Not recognised".
- [ ] A second checkbox, "I accept these N limitations", appears only when N > 0; Start is enabled
      only when both boxes are ticked. "Edit folder & budget" and "Edit context" stay one click away.
- [ ] All text set through `textContent`. Tests: rendering, checkbox gating, inert hostile text.

### Task 8: Help, README and checkpoint B

**Files:** modify `apps/issuer-library/README.md` (New run section), Help text in
`apps/issuer-library/web/views.js`, `VERIFICATION.md`.

- [ ] Describe the classification, expected outcomes as forecasts, and what acceptance records.
- [ ] Run Checkpoint B gates; record results with their actual scope.

## Phase 3: credit filters in the Issuer Library

**Library layout.** One table, one row per issuer showing its latest run, expandable to all runs
as today. Columns: Issuer · Classification · Lowest rating · Net leverage · Interest cover ·
Currency · As of · Completeness · Report. Each figure shows its period ("4.2x · FY2025") and opens
the evidence inspector on the handoff line it came from. Columns sort; Not recorded sorts last.
"Open report" is the row's main action, for readers who only want the report.

**Filters.**

| Group | Filter | Control | Source |
|---|---|---|---|
| Credit | Classification | Investment grade · High yield · Not stated | Context |
| Credit | Lowest rating | At or above / at or below a notch, on the shared rating scale | Context ratings |
| Credit | Net leverage, total leverage | Min / max (x) | CP-1 `Chart data: leverage` |
| Credit | Interest cover | Min / max (x) | CP-1 `Chart data: interest cover` |
| Credit | Liquidity (cash + undrawn) | Min / max, after choosing a currency | CP-1 `Chart data: liquidity` |
| Coverage | Currency | Recorded reporting currencies | Context |
| Coverage | Completeness | Report written · with accepted limitations · stopped · partial | Run folder, `expectations.json` |
| Coverage | As of | Year (existing) | `workflow.json` |
| Coverage | Runs | Latest run per issuer (default) · Any run | — |
| More filters | Sector, workflow, content, module | Existing controls | Existing |

Each numeric filter shows coverage and what it hid: "Net leverage recorded for 2 of 44 runs ·
12 without a figure hidden · Show them". Active filters stay chips, and the whole filter state
is kept in the URL hash so a view can be bookmarked or shared.

### Task 9: Credit facts in the workspace reader

**Files:** modify `apps/issuer-library/engine/store.py`; create
`tests/fixtures/library-credit/expected.json` and a focused test beside the existing store tests;
update `apps/issuer-library/designs/fake_engine/store.py`.

- [ ] Hand-write expected values first, from named handoff lines in the two retained runs with
      fixed chart tables, plus synthetic runs labelled synthetic.
- [ ] Per run, a `credit` record: `classification`, `currency`, `ratings` (agency, rating, outlook,
      as-of, "entered by user"), `metrics` (each: exact text, number, period, unit, output id, line,
      or a state `not_recorded` / `not_meaningful` with its reason), `completeness` (requested and
      accepted module counts, report written, run state, accepted-limitation count).
- [ ] Context read through `workflow.json`'s `context` source, inside the workspace, links refused,
      sha256 checked; any problem gives Not recorded plus a Settings issue.
- [ ] Latest-period column only; "n.m.", negatives in brackets, dashes and units parsed per the
      chart table's own `Reporting unit`; anything else is `not_meaningful`, never a number.
- [ ] Tests: hand-written values; stdlib context parse agrees with `load_context` on every
      `cases/` context fixture; rating scale equals Task 3's table; Review Focus 13.

### Task 10: Library columns and credit filters

**Files:** modify `apps/issuer-library/web/views.js`, `apps/issuer-library/web/screen.js`,
`apps/issuer-library/web/screen.css`, `apps/issuer-library/web/library-workspace.test.cjs`,
`apps/issuer-library/web/screens.test.cjs`.

- [ ] Columns, sorting and evidence links as in the layout above; Not recorded in grey, never 0.
- [ ] `filterLibrary` gains the Credit and Coverage filters; latest-run scope by default; coverage
      and hidden counts; chips and URL hash state.
- [ ] Tests: hand-written expected matches on the jsdom fixture for Review Focus 10-12 and 14;
      keyboard and screen-reader labels on every control; narrow-screen layout.

### Task 11: Help, README and checkpoint C

**Files:** modify Help text in `apps/issuer-library/web/views.js`, `apps/issuer-library/README.md`,
`VERIFICATION.md`.

- [ ] Explain where each figure comes from, that missing figures never match, the latest-run
      default, and that ratings are as entered by the user with their date.
- [ ] Run Checkpoint C gates; record results with their actual scope.

## Done when

- The issuer identity section requires investment grade or high yield, and older context files
  still load.
- The Review step lists an expected outcome for the run and for every module, with reason and fix,
  including the investment-grade limitations.
- Start cannot be pressed past listed limitations without the separate acceptance.
- Every started run folder holds `expectations.json` with what was expected and accepted.
- The back-test report states rule agreement on retained runs, labelled as retained-data evidence.
- The library filters by classification, lowest rating, leverage, interest cover, liquidity,
  currency and completeness; every figure links to its handoff line, and missing figures are
  visible and never match a numeric filter.
