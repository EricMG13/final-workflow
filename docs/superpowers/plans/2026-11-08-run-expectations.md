# Run Expectations, Primary Transactions and Credit Filters Implementation Plan

> **For agentic workers:** Steps use checkbox (`- [ ]`) syntax. Subagents are permitted for
> implementation, review and verification (`AGENTS.md`); expected values are never written by the
> agent that writes the code they check. Revised 2026-11-08 after an adversarial review (record at
> the end).

**Goal:** Before Start, tell the user what each module is expected to produce from the files and
the context they supplied, why, and what would improve it, and require them to accept the listed
limitations, so fewer runs are repeated. The user states the issue classification and the facility
terms in the context. Primary (new-issue) runs become useful before closing: CP-4 reviews draft and
offering documents as Provisional, and pro forma leverage keeps unrealised add-backs out of the
base. Readers who only want reports can find them in the Issuer Library by credit and market
information. Each phase ends with a live checkpoint that proves the applied changes with real model
output.

**Architecture:** One offline rule set in Python, inside the CP-OS launcher's existing review.
Expected outcomes come first from what the user **declared** in the context (legal documents,
management bridge, portfolio workbook, prior case, quotes, ratings, facility terms). A conservative
document-kind guess from each file's name and first pages only adds a `Check` when nothing
supports a declaration. The bridge returns the expectations; the app shows them first on the Review
step. Start requires a separate acceptance of the counted items, which is recorded in the run folder
before any provider call. No new orchestration layer and no model call before Start. Primary method
changes are launcher instructions plus fixed handoff tables, checked in each module's own repair
loop. The selected method files are not edited, and each correction is recorded in
`METHODOLOGY-REVIEW.md`. Each finished run writes a `library.json` manifest pinning its credit and
market facts to exact lines of its handoffs and context snapshot. The app's existing discovery admits
it under the approved example's rules, and the Library ports that example's screening design. The
library filters on admitted values, links each to its pinned line, and never calculates a figure.

**Tech Stack:** Python 3.13 (stdlib, pydantic), Go, plain browser JavaScript; jsdom test-only.

**Delivery:**
- Four PRs, one per phase, each at most 800 changed lines excluding fixtures.
- Phase 4 does not wait for Phase 3's live checkpoints, except its pro forma basis, which ships only
  after live check C2 passes.

**Beta V1:** these four PRs are the final UX changes before the first beta release.
- Scope is frozen. Any other UX change waits until after the beta.
- Every merged PR leaves `main` releasable, and nothing half-built is visible to a beta user.
- Phase 3 merges only after C3 passes, so unproven method instructions never reach the beta.
- The release gate at the end decides readiness.

## Decisions

### Facts the plan builds on (verified 2026-11-08)

| Finding | Decision |
|---|---|
| No offline code classifies documents. `_issuer_files` skips hidden, `_` and `~$` files, then parses every file and refuses unreadable or textless ones (`cpos_launch.py:299-346`). `_pages` already yields per-page text: PDF pages, xlsx sheets, 12,000-character chunks for text and CSV, and 3,000-character rows for HTML. HTML page 1 begins "Visible text of `<file name>`" | Keep `pages[:3]` for the guess at no extra cost. The guess skips that HTML header line, so a file name is never read as cover text |
| The context already declares `attachments.legal_documents` (executed, draft or none; the form preselects executed), and booleans for `management_bridge`, `portfolio_workbook` and `prior_case` (`context.py:238-243`). The launcher never reads them; modules see them only inside the context file | The declarations drive the expected outcomes. The guess adds a `Check` only when a declaration has no supporting file. The legal-documents choice loses its preselected default |
| App runs send every file to every module (`owners/cpos.py:404`) and the whole context as source `context`. The review already lists ignored files and omitted sections (`bridge.py:283-285`) | Expectations inform; they never block a run or filter sources |
| Several outcomes cited in the first draft come from owner-path code that app runs never execute: `cp2h.py` "Rating register not found", `cp3_relative_value.py` (imported only by the owner path), `cp3d.py` and `cp1d.py`. On app runs each module is a model reading `instructions/<module>.md`, checked by `cpos_launch.checker` | Every rule is derived from the instruction text a module is actually sent, plus the launcher checker. A rule taken from owner code is labelled as such. Rules are labelled **per method**, **observed offline** or **observed live** |
| Only 4 retained runs are launcher runs with a context: `cpos-launch-live-001`, `cpos-launch-live-002`, `cpos-launch-cp2-reader-001` and `web-04cd…`. All are TDG as of 2024-09-30, Credit Snapshot, with at most CP-0, CP-1, CP-1A and CP-2. The other 17 runs with `workflow.json` are host or replay campaigns without a context | The back-test reports its true sample. It adds contexts reconstructed for campaign cases with real outcomes, labelled "reconstructed context": LMI intercreditor, ARCC executed indenture, TDG executed notes and Ford ratings. Live checks carry the proof |
| `READER_PERSONA` ("specialising in high yield credit and leveraged loans", `cpos_launch.py:214-223`) goes to every module; the methods sent are leveraged-finance framed; none mentions investment grade. The context file, which will include the classification, reaches every module | Investment grade gives one **information** item for the whole run ("methods and persona are written for high-yield and leveraged-loan credit"), not counted as a limitation. Whether the classification changes conclusions is tested live (A-ab), not asserted |
| The launcher omits `what-changed` in every pathway except Covenant & Refinancing (computed from `_layout`) | Structural omissions are information, not counted limitations, so acceptance does not fire on every run |
| `Run` has no run type (`contracts.py:83-96`); `_instructions` and `checker` see only `Run` and the layout | Pass the run type and legal-documents declaration from `prepare` into `_instructions`. Primary-only checks follow from Primary-only layout routes, which `checker` already receives. `Run` is unchanged |
| No general per-module instruction mechanism exists beyond `OPENING`, `READER_STANDARD_MODULES` and route selectors. Chart routes accept only S.1–S.4 and RV.1 in x, US$m or % (`handoff_delivery.py:108-142`) | Add a per-module instruction mapping in the same style. New fixed tables get their own route and checker, copying the `chart_issues` pattern (plain numbers or `Not supplied:`) |
| `review_id` already covers the context bytes, the job and every engine source file | Expectations are not added to `review_id` |
| 78 files in `cases/` carry `schema: context/1`, 35 of them named `context*.json`; `Contract` forbids unknown keys and requires declared ones; `_omit_absent_cutoff` (`context.py:82-89`) shows how an optional field keeps older files byte-identical | New fields are optional in the reader and omitted from the dump when empty, so fixtures, pins and goldens stay byte-identical. A file that uses a new field needs this version or later; the README says so |
| The app already admits per-run manifests `runs/<id>/library.json` under the approved example's rules and serves them at `/api/catalogue` (`discovery.go:45-130, 261-296`; `model.go`). The Library screen ignores them (`boot.js:11-15`), and app runs write none. `store.py` only recognises the shape of `Chart data:` tables | The bridge writes the manifest for each finished app run (Task 12), and the Library ports the example's screening onto those records (Task 13). `store.py` is unchanged for the library |
| CP-1's chart tables hold one row per period, with units fixed at x, US$m or % | Manifest metrics come from the last annual or LTM row. A non-USD issuer's monetary rows are `Not supplied` and write no metric; a rule says so |
| `tests/test_run_expectations.py` and `tests/product/test_context.py` are not in `validate.py`'s `PYTHON_TESTS` | Each task adds its tests there |
| A launcher run's delivery bundle must hold `report.html`, `view.json`, `report-view.json` and `delivery.json`, plus byte-identical copies of each handoff. When the HTML Model is published it adds `model.html`, `model-view.json`, `model-report-view.json` and `calculation.json` (`owners/cpos.py:648-691`). App runs drop CP-MODEL, and the retained web run records `cp_model_published: false` | Live checks require the report bundle. On app runs the HTML Model and `calculation.json` are recorded as **not published**, which is a known beta limitation; it is not a failure. Publishing them from app runs is an owner decision outside these UX changes |
| `designs/browser_check.py` already walks the library, reports, every section, deliveries and settings, fitted screens, chart style, the data-flow check and New run, and records every console, page, HTTP and exception fault in `faults.json`. `designs/flow_check.py` traces hashes and numbers from sources to handoffs, deliveries and the report | Every live run is followed by the browser walk over a workspace holding it, plus `flow_check`. Each phase extends the walk for its own screens; no new test tool |

### Owner decisions (2026-11-08)

1. Draft review on app runs: **yes**, as Provisional (Task 10).
2. Pro forma for Primary runs: **yes, with unrealised add-backs kept out of the base** and shown
   separately (Task 11).
3. Expected-rating status: **no**; ratings are user-entered.
4. Primary proof case: **no** retained or private case; public pre-closing filings serve as a
   labelled proxy (Task 9).
5. Live testing at each checkpoint of the applied changes: **yes**; each paid run still needs the
   owner's go-ahead at that checkpoint (Global Constraints).
6. User-entered values are used as entered; user-derived issues are the user's to resolve.
7. Library: **reuse the approved `examples/issuer-library` screening design and logic** in the app
   (Phase 4), not new filter code.

### Outcome semantics

| Outcome | Given only when | Counted for acceptance |
|---|---|---|
| `Will refuse` | A declaration, context fact or structure says the module cannot run (e.g. legal documents declared `none` with CP-4 requested) | Yes |
| `Gap` | A context fact or declaration says an input is absent (e.g. no quotes or talk in the context and no quotes file recognised) | Yes |
| `Limited` | A context fact or declaration narrows the module (talk only, non-USD, Provisional legal review) | Yes |
| `Check` | Evidence is only a guess: a declaration has no supporting file, a document's status is unknown, or no file was recognised as needed | Yes, as "check before you start" |
| Information | Structural omissions, investment-grade method fit, inherited rows | No |
| `Ready` | Nothing above applies | No |

- **Inheritance:** a consumer inherits the milder of its producer's outcome and the edge's rule:
  block → `Will refuse`; restrict → `Limited`. Inherited rows are grouped under their producer and
  shown as information. `Check` never propagates.
- **"Run without <module>":** offered only for declaration-based `Will refuse`. It removes the
  module and, transitively, everything that requires it.
- **Wording rule:** every expectation reads as a forecast: "Expected from your declarations, files and
  context; CP-0 confirms during the run; the model may still find less." A guessed kind reads
  "Likely: credit agreement (found 'CREDIT AGREEMENT' on page 1)", never as fact. User-entered
  values are labelled "entered by user".

### Primary transactions

- **CP-4 Provisional scope:** Primary runs, or a declared `draft`. Elsewhere the method's Blocked
  message ("supply the executed document") stands.
- **Final offering memorandum:** after closing it is a summary, not the governing document. It gets
  its own reason, never "terms may change before signing".
- **Authority ranks** follow `REF_CP-4_STEPS.md:340-345`:
  1. Executed agreement or indenture.
  2. Intercreditor agreement.
  3. Compliance certificates.
  4. Offering memorandum.
  5. Covenant-review report.
  6. Lender presentation, term sheet or commitment letter.

  All are document kinds.
- **The Provisional label travels:**
  - Every CP-4 section routed to the report says "Provisional", and so does the Reader summary's main
    limitation.
  - On Primary runs, CP-3, CP-5 and CP-6 label any term taken from a Provisional CP-4 handoff as
    Provisional.
- **CP-1D:** Primary runs add it to the default modules. The review shows the extra module, and the
  user can remove it. CP-4 is told not to use CP-1D figures as covenant capacity (CP-1D's own rule).
- **Pro forma, by module and by dependency:**
  - CP-1A records **Sources and uses** as documented.
  - CP-2, which requires CP-0, CP-1 and CP-1A, writes **Pro forma capitalisation** from CP-1's debt
    register plus CP-1A's changes.
  - CP-2 also writes the **EBITDA ladder** and **Pro forma leverage**.
  - CP-1D supplies each add-back's verdict and the amount already in the LTM.
- **EBITDA ladder, written before any code:**
  - (a) Starting EBITDA: CP-1's cited figure, with its definition named (EBIT plus D&A, or the
    issuer's adjusted or "As Defined" figure).
  - (b) Documented acquisition or disposal pro forma adjustments, cited.
  - (c) Unrealised run-rate savings: run-rate claimed minus the amount already in the LTM, per CP-1D.
  - (d) Other management add-backs, by CP-1D verdict (Supported, Challenged, Rejected, Insufficient
    Information).
  - (e) The difference from management's quoted figure: a `calculate` result plus its explanation,
    or `Insufficient Information`.

  The base is (a)+(b). **As marketed** is management's figure as quoted. Nothing is plugged, and no
  haircut is invented.
- **Pro forma capitalisation:**
  - One balance-sheet date and one LTM period, both stated.
  - An explicit cash row: cash to balance sheet, fees and OID per sources and uses.
  - A column per currency; totals only with an FX rate cited from the documents.
  - The user's entered facility size is used and labelled. A different documented size is shown
    beside it and the difference logged, not resolved.
- **Report:** both pro forma tables get table routes on Primary runs through the existing dense-table
  renderer. They are not placed under the dated capital-structure block.

**Rejected:**
- Blocking Start for a missing file.
- A model call to classify files.
- A second checker beside CP-OS.
- A new schema version, or a required reader field.
- Inferring the classification from ratings.
- Checking user entries against each other or against the filings.
- Parsing documents or handoffs for values the user supplies.
- An expected-rating status.
- One blended pro forma figure, an equality check forcing management's figure, or Python arithmetic
  on model-written numbers.
- A reader refusal of talk on non-Primary runs. The form blanks hidden talk fields instead.
- Deleting the form's capability panel. Its rules and Python's now share the same declarations, so a
  parity test is well posed.

**Out of scope (later plans):** files-first run check with pathway ratings, phased context stages,
context prefill from filings, post-run expected-versus-actual in Run activity, investment-grade
variants of the methods, credit metrics for runs that predate the fixed tables, pro forma interest
cover, saved named filter views.

## Global Constraints

- **Paid runs** happen only at the live checkpoints below. Each needs the owner's go-ahead at that
  checkpoint, stating config, modules and cap. The provider key comes only from the launching
  environment. There is no automatic paid retry: a failed live check goes to the repair loop in
  `docs/QUALITY-GATE.md`, and a rerun needs a new go-ahead. Offline gates run with keys removed.
  Results are labelled with their actual scope: issuer, date, older source, synthetic user entries,
  public proxy.
- **Read-only material:** the repository's `runs/`, `deliverables/`, `data/public-corpus/`, `cases/`
  fixtures, `docs/reuse/selected-methods/` and predecessor repositories are read, never written. A
  new case gets its own folder. The app writes only inside its own workspace.
- **Expected values** are hand-written and committed before the code or paid run they check, by
  someone other than the code's author. This covers document-kind keys, rating scale, rule outcomes,
  pro forma keys, live answer keys and library values. Accuracy on real and synthetic files is
  reported separately.
- **Missing is never zero.** "Not supplied", "not stated" and "Not recorded" stay visible. No new
  score or aggregate. A missing, negative-denominator or not-meaningful figure never satisfies a
  numeric filter.
- **Arithmetic:** new module arithmetic uses `calculate`. The library and delivery never calculate,
  convert currency or rescale units.
- **Other limits:** Excel stays input-only. No new dependency.
- **Branch and PRs:** branch `claude/intelligent-babbage-b0309i`, restarted from `main` for each
  phase's PR. Commit per task; push at each checkpoint.
- **Records:** one short `VERIFICATION.md` entry per checkpoint. No other review files.

## Validation Schedule

| When | Command or action | Passes when |
|---|---|---|
| Every task | Named focused tests, registered in `validate.py` `PYTHON_TESTS`, each under `timeout 300` | New test seen failing for the stated cause, then exit 0 |
| Every commit | `uv run python tools/quality_gate.py`, `python3 apps/issuer-library/validate.py quick` | Exit 0 |
| **Checkpoint A** (after Task 5) | Offline: back-test report. **Live: A-live** (and A-ab if the owner wants it) | Every disagreement explained or its rule fixed; the meaning of `Will refuse` set from A-live; required outputs present |
| **Checkpoint B** (after Task 8) | Offline: `validate.py full`, `validate.py browser`. **Live: B-live** | Live pass criteria and required outputs below; owner accepts the Context and Review screens |
| **Checkpoint C** (Tasks 9-11, one module at a time) | **Live: C1** and control C1n after Task 10; **C2** after Task 11; then the pathway runs **C1r** and **C3** | Live pass criteria and required outputs below. Without them, Phase 3 is reported as "instructions only, unproven" and does not merge |
| **Checkpoint D** (after Task 14) | Offline: `validate.py full`, `validate.py browser`. **D-live** (no provider cost) | Exit 0; library values equal the hand key; required frontend outputs present; owner accepts the Library screen |
| **Release gate** (after Checkpoint D) | See "Release gate (beta V1)" | All items pass |

Before each checkpoint: confidence-review (doubts, causes, adversarial cases, fixes) and
rewrite-tournament in post-edit mode on `guess_kind`, `expectations`, the Review renderer, the CP-4
register check, the pro forma table checks, the credit-facts reader, the facility matcher and
`filterLibrary`.

**Stop rules:** a failing gate stops the next task in its phase. Two failed fix rounds on one defect
go to the owner with both outcomes. Never loosen a test to pass.

## Live checkpoints

**How every live check runs:**
- Each paid check runs a **whole pathway related to the change**, through the app as a beta user
  would: `apps/issuer-library/designs/live_check.py`, extended in Task 5 with `--case`, on the real
  engine.
- Exceptions: C1, C1n and C2 are single-module gates, because `AGENTS.md` requires changing one
  module at a time against its actual output. The pathway runs follow them.
- Config is sol-medium unless the owner names another. Each cap exceeds the per-call hold (USD 5.73
  on sol-medium).
- For scale: a CP-0 + CP-1 run spent USD 0.59, and a multi-module, multi-issuer campaign about
  USD 14-20.
- Every answer key is frozen before its run. Each run needs the owner's go-ahead at its checkpoint.

**Required outputs, checked after every live run:**

| Side | Output | Passes when |
|---|---|---|
| Backend | Run folder | `workflow.json`, `instructions/<module>.md` and an accepted `<module>.md` for every requested module, or a recorded stop reason; the completion receipt; spend within the cap in `status.json` and the event log |
| Backend | New records (Phases 2-3) | `expectations.json`, the context snapshot, and the Start receipt with the accepted item ids, all written before the first provider call, with one `review_id` across them |
| Backend | Delivery bundle | `report.html`, `view.json`, `report-view.json`, `delivery.json`, with delivered handoffs byte-identical to the accepted ones. HTML Model and `calculation.json`: recorded as published or as "not published by app runs" (known beta limitation) |
| Backend | Data flow | `flow_check` reports no fault: every upstream hash and text received, every source hash, every handoff number traced to what the module read, every report number found in a handoff |
| Frontend | New run | The walk completes: Context (new fields), Issuer folder & budget, Review (expected outcomes, acceptance), Progress, Open run; the Review's module list equals the run's |
| Frontend | Reading the run | `browser_check`'s real-workspace walk over a workspace holding the run: Library row, Overview, every module section renders, Reports opens the report, Built from hashes match, evidence inspector opens the cited line, Run activity lists events and spend, fitted screens, chart style |
| Frontend | Faults | `faults.json` holds no console, page, HTTP or exception fault outside the documented list, in Chromium and the walk's second engine |

**The checks:**

| Check | Pathway and case | Cap (USD) | Passes when (besides required outputs) |
|---|---|---|---|
| **A-live** refusal through a pathway (A) | **Covenant & Refinancing** on TDG FY2024 public filings, "older source"; no legal files; legal documents declared `none` | 25 | Records whether CP-4 ends as an accepted Blocked handoff or stops the run, what downstream modules and the report then show, and what it cost; the `Will refuse` wording and "Run without" fix are set from it; forecast equals outcome for every module |
| **A-ab** classification A/B (A, optional) | **Credit Snapshot** on the same files, twice: investment grade, then high yield | 25 each | Conclusions unchanged, or the "information only" decision is revised |
| **B-live** Secondary through the app (B) | **Relative Value** on TDG FY2024, Secondary, high yield, one TDG notes facility row and one observed quote labelled "synthetic user entry", through the app UI with acceptance | 30 | Start without acceptance returns 400 with no claim and no ledger entry; each module's outcome equals its forecast or the rule is fixed; coupon and maturity are used only as "entered by user", never cited as filing evidence; CP-3 treats the row as terms, not talk; CP-1 chart values match retained `cpos-launch-cp2-reader-001` or the variance is recorded; the Library shows "with accepted limitations" |
| **C1** CP-4 Provisional gate (C) | Mattress Firm pre-closing (Task 9); CP-0, CP-1, CP-4 | 10 | CP-4 does not stop at the gate; the register lists each document with status and authority rank; `DRAFT_LIMITATION` appears verbatim; at least 8 keyed terms match the key, each labelled Provisional; no document is called executed; the main limitation names Provisional |
| **C1n** control (C) | The same case without its lender presentation; CP-0, CP-1, CP-4 | 10 | Blocked, as forecast |
| **C2** pro forma gate (C) | Mattress Firm pre-closing; CP-0, CP-1, CP-1A, CP-1D, CP-2 | 15 | Sources and uses and pro forma debt equal the key; cash row, one balance-sheet date and one LTM period; base EBITDA equals the key with no double count; As marketed equals management's quoted figure, any difference explained, never plugged; CP-2's pro forma debt cites CP-1A's total |
| **C1r** after-closing control (C) | **Covenant & Refinancing** on Mattress Firm after closing: the executed Term Loan and ABL Credit Agreements, Secondary, "older source". Fallback: retained TDG executed notes (`runs/tdg-004`, read-only) | 30 | CP-4 Completed with no draft limitation; each C1 term marked TBD or indicative is compared with the executed term (e.g. margin "TBD" against LIBOR + 4.00-4.25%) |
| **C3** Primary through the app (C) | **Credit Snapshot plus CP-1D** on Mattress Firm pre-closing, Primary, through the app UI | 30 | The report shows both pro forma tables or an explicit gap; every report section drawing on CP-4 says Provisional; CP-6 never treats a draft term as executed; CP-5 flags claims that depend on drafts |
| **D-live** library (D) | No new run: the workspace holding the A, B and C runs and the retained runs with fixed chart tables, opened in the ported screening Library | 0 | Every live run's `library.json` is admitted with no rejection; each screened value equals a hand key from the actual handoff and context lines, including pro forma metrics and facilities and quotes as entered; the example's filters, sorting and run detail behave as specified, and their evidence links open the pinned line; coverage and hidden counts are right. Labelled "actual retained model output, downstream consumption" |

Caps total USD 150, or USD 200 with A-ab; expected spend is far lower.

**EDGAR access:** granted on 2026-11-08 through the owner's personal environment `final-workflow`
(www.sec.gov, efts.sec.gov and data.sec.gov). Requests identify themselves as "final-workflow
research" with the owner's email, as EDGAR requires and as the owner authorised. They stay well
under EDGAR's 10 requests per second.

## Release gate (beta V1)

Run once after Checkpoint D, on the `main` commit to be released:

1. All four PRs merged, and each phase's checkpoint recorded in `VERIFICATION.md`.
2. `validate.py full`, `validate.py browser` and `validate.py suite`. No failure beyond
   `tests/nightly-known-failures.txt`. While GitHub Actions starts no jobs, these local runs stand
   in for CI, and the record says so.
3. **RC-live:** if code changed after C3, one more whole-pathway run on the release candidate
   (Credit Snapshot, TDG FY2024, cap USD 30), with every required output checked.
4. The packaged app on Windows: the owner runs `Smoke-test.ps1`, then opens the app in Edge, creates a
   run up to the Review step, opens a live run's report and the Library filters.
5. Help and README describe exactly what the beta does, including known limitations: the HTML Model
   and `calculation.json` are not published by app runs; Primary terms are Provisional before
   closing; metrics are Not recorded for older runs.
6. Owner sign-off.

## Review Focus

1. **Declaration drives:** legal documents declared `draft` and nothing recognised on pages 1-3: CP-4
   `Limited` (Provisional), plus a `Check` ("no draft recognised"). Never `Will refuse` (Task 3).
2. **Non-recognition stays a Check:** a 10-K whose exhibit index names the credit agreement, with legal
   documents declared `executed`: classed financial report; CP-4 `Check`; no "Run without" (Tasks 2, 3).
3. **False drafts:** an executed credit agreement whose page 1 has "PRELIMINARY STATEMENTS" is not
   marked draft; an unmarked EDGAR exhibit has `executed=None` and gives `Check` (Task 2).
4. **Amendment alone:** CP-4 `Limited` ("base agreement not recognised"), never `Ready` (Task 3).
5. **Non-USD issuer (Erste):** CP-2D `Limited`; CP-1 chart strip `Limited` (US$m only); no USD labels
   invented (Task 3).
6. **Investment grade:** one information item for the run; no per-module rows; not counted (Task 3).
7. **Acceptance does not fire on structure alone:** a clean Covenant & Refinancing run with everything
   declared and recognised counts 0 items; a Credit Snapshot whose only item is `what-changed`
   counts 0 (Tasks 3, 7).
8. **Older context:** loads with new fields not stated and dumps byte-identical; the form marks the
   classification to fix; a resume keeps the stopped run's context bytes and does not ask (Tasks 1, 6).
9. **Hidden fields:** switching Primary → Secondary in the form blanks talk fields before `build()`
   (Task 1).
10. **Hostile text:** file names and context text render inert on the Review step and in the library;
    a hostile URL hash value is ignored (Tasks 7, 14).
11. **Stale acceptance:** inputs changed after acceptance; Start refuses and asks for a new review (Task 6).
12. **CP-4 register without the limitation:** a register lists a draft, term sheet or lender
    presentation and the answer lacks `DRAFT_LIMITATION`: repair requested (Task 10).
13. **Final offering memorandum on a Secondary run:** reason "summary, not the governing document";
    no "may change before signing" (Task 10).
14. **Pro forma ladder:** run-rate claimed 50, 20 already in the LTM, a Rejected add-back of 10, an
    acquired EBITDA of 40: base = (a) + 40; unrealised 30 shown; Rejected 10 shown; management's
    figure quoted; difference explained; nothing plugged (Task 11).
15. **Private deal, no filings:** the Reported row is `Not supplied: no filed financial statements`;
    the module is accepted, not looped to max turns (Task 11).
16. **Bases never blend:** a ladder row missing its source or definition, or a pro forma debt not citing
    CP-1A, is sent back for repair (Task 11).
17. **Missing is not a pass:** "Net leverage below 4x" excludes runs with no figure, `Not supplied` or
    a negative value, and says how many it hid (Task 13).
18. **Leverage basis:** the Leverage column and filter read only CP-1's chart metric and show its basis
    text. The pro forma keys never fill it. With "All bases" chosen, the panel says definitions
    differ, as in the example (Task 13).
19. **Latest run:** the latest as-of date among runs with a written report; a newer stopped run is
    shown but used only under "Any run" (Task 13).
20. **Ratings:** "(P)B2" and "B+(EXP)" place as B2 and B+ and keep their text; SD, RD and "/LD" place as
    D; NR, WD and WR are not on the scale; issuer scope by default; BBB- and Ba1 match "BB+/Ba1 or
    below" (Task 13).
21. **Facilities:** two facilities never combine to match one filter; talk 325-375 matches "350-400";
    a Secondary bond with bid 98.50 / ask 99.00 and no price matches "price 98.75-100" and not
    "above 99.50"; margin 375 matches a margin filter but not a margin-talk filter (Task 13).
22. **Context snapshot:** editing the intake context after a run does not change what the library
    shows for that run, because the manifest pins the run's own snapshot (Tasks 6, 12).
23. **Private-side material:** a run whose context `case_kind` is private carries a "Private-side"
    label in the library (Task 13).
24. **Manifest admission:** every live run's manifest is admitted with no "Run metadata rejected" gap;
    a manifest value absent from its pinned line is rejected by the existing rule (Task 12).

---

## Phase 1 (PR 1): context fields and rule set

### Task 1: Context fields, declarations and compatibility

**Files:** modify `docs/templates/context-form.html`, `docs/templates/README.md`,
`apps/issuer-library/web/context-embed.js`, `src/deploy_workflow/context.py`,
`tests/product/test_context.py`, `apps/issuer-library/web/context-embed.test.cjs`,
`apps/issuer-library/validate.py`; regenerate `apps/issuer-library/web/context-form.html` with
`packaging/sync_assets.py`.

- [ ] **Issue classification:**
  - A choice directly after Issuer ID: Required, nothing preselected, and visible (not moved into
    "Additional issuer details").
  - Cards: **Investment grade** and **High yield**. Help: "Classify by the debt this run analyses;
    for split-rated or unrated issuers use your firm's convention. The workflow's methods are
    written for high-yield and leveraged-loan credit."
- [ ] **Legal documents** declaration: required, with nothing preselected. Card text updated to the
      Provisional behaviour. Remove "CP-4 refuses them today" and "draft mode Planned".
- [ ] **Facilities** for every run type: required (at least one row) for Primary, optional
      otherwise. Each row gains optional **Coupon (%)**, **Margin (bps)** and **Maturity**. Spread
      talk, OID talk and tenor show for Primary only, and `build()` blanks them on other run types.
- [ ] **Reader:**
  - `Identity.issue_classification: Literal["", "investment_grade", "high_yield"] = ""`.
  - `DealTerm.coupon_pct` and `margin_bps` are plain non-negative numbers; `maturity` is a date.
  - Every row is validated for every run type: move the checks before the non-Primary return, and
    drop the Primary-only refusal.
  - Empty new fields are omitted on dump (`_omit_absent_cutoff` pattern).
- [ ] **Tests:**
  - An older file loads and dumps byte-identical.
  - Each valid value round-trips, and invalid values are refused.
  - A Secondary context with facility rows loads.
  - Review Focus 8-9.
  - The form/reader parity test covers the new fields.
  - `cases/PINS.json` is unchanged.
  - All tests are registered in `PYTHON_TESTS`.

### Task 2: Document-kind guess

**Files:** create `src/deploy_workflow/run_expectations.py`, `tests/test_run_expectations.py`,
`tests/fixtures/run-expectations/document-key.json`.

- [ ] **Hand-labelled key first:**
  - At least 20 real files, mostly from `runs/*/sources/` (the public corpus holds only 5 TDG
    files). These include the executed ARCC supplemental indenture, the TDG "EXECUTION VERSION"
    indenture lines, the Enel EMTN supplement, HTML filings and a non-English report.
  - Synthetic fixtures only for kinds no retained file has, labelled synthetic.
  - Adversarial entries: "PRELIMINARY STATEMENTS" in an executed agreement; an unmarked EDGAR
    exhibit; an amendment alone; an offering memorandum with audited financial pages; a combined
    PDF; a misleading file name; an empty page; an xlsx workbook.
- [ ] **`guess_kind(name, first_pages) -> Guess(kind, signal, executed, period_end)`:**
  - Kinds: `financial_report, earnings_release, credit_agreement, indenture, amendment,
    intercreditor, compliance_certificate, covenant_review, offering_memorandum, prospectus,
    lender_presentation, information_memorandum, term_sheet, commitment_letter, ratings,
    market_quotes, peer_data, management_bridge, portfolio, prior_decision, unrecognised`.
  - `executed` is `True`, `False` or `None`. "Preliminary Statements" is never a draft signal.
  - `period_end` is read from a financial report's cover where stated.
  - Cover phrases outrank later pages and names; ambiguity gives `unrecognised`.
- [ ] **Tests:** accuracy per kind, reported separately for real and synthetic files; Review Focus
      2-3; HTML header line skipped.

### Task 3: Rules and expected outcomes

**Files:** modify `src/deploy_workflow/run_expectations.py`, `tests/test_run_expectations.py`.

- [ ] **`Rule(scope, condition, outcome, reason, fix, basis, evidence)`:**
  - `scope` is a module or `run`.
  - `basis` cites the instruction text sent on app runs, or is labelled owner-path.
  - `evidence` is `per method`, `observed offline` or `observed live`.
- [ ] **Initial rules**, each verified against `instructions/<module>.md` text before it is written:

| Scope | When | Outcome |
|---|---|---|
| Run | Investment grade selected | Information |
| Run | Report section omitted by this pathway | Information |
| CP-1 | No file recognised as a financial report, earnings release or offering document with financial pages | Check |
| CP-1 chart strip | `reporting_currency` not USD | Limited (charts are US$m only) |
| CP-1C | `valuation.peer_source` is `none`, or `cp_dr_public` without CP-DR | Gap |
| CP-2D | `reporting_currency` not USD | Limited |
| CP-2H | No `ratings` in the context and no ratings file recognised | Gap (method: Insufficient Information) |
| CP-3 | Talk but no observed quote in the context or files | Limited |
| CP-3 | No quotes and no talk in the context, and no quotes file recognised | Gap |
| CP-3D | No quotes in the context and no quotes file recognised | Gap |
| CP-4 | Legal documents declared `none` | Will refuse (outcome text set from A-live) |
| CP-4 | Declared `executed`, none recognised as executed | Check |
| CP-4 | Declared `draft`, or Primary run, with no executed agreement recognised | Limited: Provisional |
| CP-4 | Only an amendment recognised | Limited: base agreement not recognised |
| CP-4 | Secondary or Research run whose governing terms rest on a final offering memorandum | Limited: summary, not the governing document |
| Run | No filed financial report recognised, lender presentation or information memorandum recognised | Check: financials are management claims |
| CP-2 | Primary without CP-1D in the modules | Gap: pro forma base row |
| Portfolio Decision | `portfolio_workbook` declared false | Gap |

- [ ] **`expectations(ordered, guesses, context, registry)`:** returns run-level items first, then
      modules in order, with inheritance and counting as in Outcome semantics. Context values are
      read as entered, and no rule compares one user entry with another.
- [ ] **Tests:** hand-written outcomes for Review Focus 1-7, plus one clean case per pathway per run
      type, labelled synthetic.

### Task 4: Launcher and bridge carry the expectations

**Files:** modify `src/deploy_workflow/owners/cpos_launch.py`, `apps/issuer-library/engine/bridge.py`,
`apps/issuer-library/designs/fake_engine/bridge.py`, `tests/test_cpos_launch.py`, `tests/test_cpos_app.py`.

- [ ] `_issuer_files` keeps `pages[:3]` per pinned source; nothing else changes in what is pinned or
      refused.
- [ ] `Prepared` gains defaulted `documents` and `expectations`. Only `prepare()` builds it.
- [ ] `review()` adds `issue_classification`, `documents`, `expectations`, `counted` (item ids), and
      `without` for each declaration-based `Will refuse`.
- [ ] Tests: output shape, unchanged refusals, `without` closure.

### Task 5: Live-check cases and back-test (Checkpoint A)

**Files:** modify `apps/issuer-library/designs/live_check.py` and its tests; create
`tools/expectations_backtest.py` and `cases/live-tdg-fy2024/`, with sources referenced read-only
from `data/public-corpus/v1/TDG`; add a dated entry to `VERIFICATION.md`.

- [ ] **`live_check.py --case DIR`:**
  - The case folder holds a context, a source list, the modules, a frozen answer key and the
    expected outcomes.
  - It runs a whole pathway through the app UI, then checks every required output (Live
    checkpoints): run folder, delivery bundle, `flow_check`, and `browser_check`'s
    real-workspace walk over a workspace holding the run.
  - `--accept-limitations` drives the acceptance step once Phase 2 exists.
  - With `--rehearse` it runs free on the fake engine, and its scope string says so.
- [ ] **Back-test:**
  - Covers the 4 launcher runs, plus the reconstructed-context campaign cases, labelled.
  - Reports per rule: agreed, disagreed or not testable, with issuer and date. Labelled
    "deterministic retained-data report".
- [ ] **Checkpoint A:** offline gates, then **A-live** (and **A-ab** if wanted) on the owner's go-ahead.
      Set `Will refuse` wording and the rule labels from the results.

## Phase 2 (PR 2): acceptance and the Review screen

### Task 6: Start requires and records acceptance

**Files:** modify `apps/issuer-library/jobs.go`, `apps/issuer-library/jobs_test.go`,
`apps/issuer-library/engine/bridge.py`, `tests/test_cpos_app.py`.

- [ ] **Go side:**
  - `startRun`'s request struct gains `accept_limitations` (unknown fields are refused).
  - When `review.json` counts any items and acceptance is false: answer 400, with no claim made.
- [ ] **`bridge.start`:**
  - Records the accepted item ids in the existing `start-authorization.md` receipt.
  - Copies `expectations.json` from the approved review (never recomputed) into the run folder.
  - Snapshots the context into the run folder before any provider call.
- [ ] **Resume:**
  - Keeps the stopped run's context bytes and needs no new classification.
  - The review states which retained answers re-run and why. Adding CP-1D is one reason.
  - Retained modules show their actual outcome, not a forecast.
- [ ] **Tests:** Review Focus 11 and 22; zero counted items works with the old request; files exist
      before the worker's first call.

### Task 7: Review step shows expectations first

**Files:** modify `apps/issuer-library/web/actions.js`, `apps/issuer-library/web/screen.css`,
`apps/issuer-library/web/new-run.test.cjs`.

- [ ] The context summary line and Review header show the classification ("Investment grade", "High
      yield" or "Not stated").
- [ ] An "Expected outcomes" table opens the Review step:
  - **This run** items come first.
  - Each module row shows its outcome, reason and fix, with a "Why we expect this" disclosure
    giving the basis and evidence label.
  - Inherited rows sit under their producer, and information rows are visibly not counted.
- [ ] "Files recognised" lists each file's likely kind, draft or executed where marked, and its signal,
      or "Not recognised".
- [ ] **Run without <module>** fills Advanced → Modules with `without` and returns to Issuer folder &
      budget.
- [ ] Extra modules (CP-1D on Primary) are named with their reason.
- [ ] "I accept these N items" appears only when N > 0. Start needs both ticks.
- [ ] All text goes through `textContent`. Tests: rendering, gating, inert text, Review Focus 7.

### Task 8: Help, README and Checkpoint B

**Files:** modify `apps/issuer-library/README.md`, Help in `apps/issuer-library/web/views.js`,
`VERIFICATION.md`.

- [ ] Describe the declarations, outcomes as forecasts, counted items, acceptance and the context
      snapshot.
- [ ] Extend `browser_check`'s New run walk: the new context fields, the expected-outcomes table, the
      acceptance gating and "Run without". Rehearse it on the fake engine.
- [ ] Checkpoint B: offline gates, then **B-live** on the owner's go-ahead.

## Phase 3 (PR 3): Primary transactions, one module at a time

### Task 9: Public proxy case

**Files:** create `cases/primary-proxy-<issuer>-<date>/` (sources, context, frozen key); add a dated
entry to `VERIFICATION.md`.

- [ ] **Confirm the case with the owner.** Recommended (screened 2026-11-08 from EDGAR): Mattress
      Firm Holding Corp. (CIK 1419852), an acquisition financing.
  - **Pre-closing:** the Public Lender Presentation of 11 September 2014 (8-K Item 7.01, Exhibit
    99.1, accession 0001104659-14-065798). It holds:
    - sources and uses of USD 821m, including Sleep Train at USD 440m and bolt-ons at USD 66m;
    - pro forma capitalisation from 1.9x to 3.5x total debt / Adjusted EBITDA;
    - acquired EBITDA (USD 32m and USD 5m), USD 17m of synergies (USD 12.5m of USD 20m expected
      within 18 months) and a USD 17m new-store adjustment;
    - a Pro Forma EBITDA reconciliation;
    - summary terms for a USD 720m Term Loan B: 7 years, margin and OID "TBD", 1.00% LIBOR floor,
      101 soft call for 6 months, 1% amortisation, excess-cash-flow sweep with step-downs, no
      financial covenants, USD 250m incremental plus unlimited at 4.0x secured net leverage, and
      50 bps MFN with an 18-month sunset.
  - **Financial base:** 10-K for the year ended 28 January 2014 (0001047469-14-003037); 10-Qs for
    29 April 2014 (0001104659-14-044836) and 29 July 2014 (0001558370-14-000163), the presentation's
    LTM basis.
  - **Context support:** merger 8-K of 29 August 2014 (0001104659-14-064027).
  - **After closing, for C1r:** 8-K of 21 October 2014 (0001104659-14-072654). Exhibit 10.1 is the
    ABL Credit Agreement and Exhibit 10.2 the Term Loan Credit Agreement, both dated 20 October
    2014; margin LIBOR + 4.00–4.25%, maturity 20 October 2021.

  The Confidential Information Memorandum and Marketing Term Sheet that the presentation refers to
  are not public, and the case says so.

  **Second case, without an acquisition (optional):** Everi Holdings' 2017 refinancing lender
  presentation (0001558370-17-002593), not yet screened in detail.
- [ ] Label the case "public proxy for a private primary deal", with issuer, date and "older source"
      where relevant.
- [ ] Hand-write the key before any run:
  - document kinds and expected outcomes;
  - sources and uses and pro forma debt as documented;
  - the EBITDA ladder inputs;
  - at least 8 covenant terms;
  - each add-back's claimed, realised and in-LTM amounts as the documents state them.

### Task 10: CP-4 Provisional review (then C1 and C1n)

**Files:** modify `src/deploy_workflow/owners/cpos_launch.py`, `tests/test_cpos_launch.py`,
`METHODOLOGY-REVIEW.md`.

- [ ] **Instruction text, in Provisional scope only:**
  - CP-4 gets an override paragraph placed with the transport overrides, before the method.
  - It requires a fixed `### Legal document register` (Document, Kind, Status, Authority rank,
    Source), Provisional confidence, `DRAFT_LIMITATION` verbatim, and "Provisional" in every
    routed section and in the main limitation.
  - It never calls a draft executed, and never uses CP-1D figures as capacity.
  - With no legal document at all, the Blocked message stands.
- [ ] **On Primary runs,** CP-3, CP-5 and CP-6 are told to label terms taken from a Provisional CP-4
      handoff as Provisional.
- [ ] **Checkers:**
  - The register is present in Provisional scope.
  - Any non-executed status, or no executed document recognised with any legal or offering document
    pinned, requires `DRAFT_LIMITATION` and "Provisional" in routed sections.
  - A consumer receiving a Provisional CP-4 handoff must say "Provisional".
- [ ] **`METHODOLOGY-REVIEW.md`:** record the source (the Deploy VII owner path's draft admission),
      the reason, and this repository's revision.
- [ ] **Tests:**
  - Review Focus 12-13.
  - An executed-only answer needs no limitation.
  - A Blocked answer with no legal documents passes.
  - Non-Primary runs without a draft declaration are unchanged.
- [ ] **Live:** C1, then control C1n.

### Task 11: Pro forma capitalisation and leverage (then C2)

**Files:** modify `src/deploy_workflow/owners/cpos_launch.py`, `src/deploy_workflow/handoff_delivery.py`
(table routes), `tests/test_cpos_launch.py`, `METHODOLOGY-REVIEW.md`.

- [ ] **Method source:** Deploy V r14's CP-1 pro forma reference if the owner supplies it; otherwise
      this instruction. Record either, with its revision.
- [ ] **Modules:** Primary default modules add CP-1D. An explicit module list is taken as given. The
      review names any absence (Task 3 rule).
- [ ] **Tables:**
  - CP-1A writes `Sources and uses` (as documented; user-entered sizes labelled; differences
    logged).
  - CP-1D's register adds `Amount already in LTM`.
  - CP-2 writes `Pro forma capitalisation`, `EBITDA ladder` and `Pro forma leverage` (Reported;
    Pro forma, excluding unrealised add-backs; As marketed), as designed in Decisions, using
    `calculate`.
- [ ] **Checkers:** structural only.
  - Fixed headers and rows in order.
  - Each cell a plain number or `Not supplied: <reason>`.
  - Citations present; definitions named.
  - CP-2's pro forma debt cites CP-1A's total.
  - A difference line is present.
  - No Python arithmetic on model numbers.
- [ ] **Delivery:** table routes for both pro forma tables on Primary runs, through the dense-table
      renderer; a delivery test from an actual handoff.
- [ ] **Tests:** Review Focus 14-16; non-Primary runs need none of the tables.
- [ ] **Live:** C2. Once Tasks 10 and 11 have both passed their gates, run the pathway checks **C1r**
      (Covenant & Refinancing, after closing) and **C3** (Credit Snapshot plus CP-1D, Primary, through
      the app). Phase 3 merges only after both pass.

## Phase 4 (PR 4): the approved screening library, ported into the app

**Source design (owner decision 7):** `examples/issuer-library`, the user-approved screening
directory: "one local directory of issuer runs, searchable by identity, sector and credit metrics,
with completeness and links to the existing reports". It is ported, not rewritten:
- **Logic:** `logic.js` (`LibraryLogic`: `numberOf`, `hasReport`, `filterRuns`, `sortRuns`).
  - A blank never satisfies a bound.
  - Leverage filters by exact basis ("All bases · definitions differ").
  - Missing values sort last.
  - Nothing is calculated.
- **Screens:** `template.html`, `app.js` and `style.css`.
  - The screening panel: search; sector, workflow, completeness and deliverables; "Credit metrics &
    period" (leverage basis, financial period, leverage and coverage minimum and maximum).
  - The sortable results table: Issuer / run, Sector, Evidence date, Leverage, Coverage,
    Completeness, Deliverable.
  - The selected-run detail: each metric's value, unit, period, basis and pinned source; gaps;
    report history.
- **Tests:** `test_logic.cjs` and `test_dom.cjs` move with the code and keep passing.
- **Style:** the example used the deliverables' Direction C shell. In the app the composition is kept
  and restyled with the app's own tokens (`screen.css`); there is no second palette.

**Data path (already in the backend):**
- Go discovery admits `runs/<id>/library.json` (`issuer-library-run/1`) under the example's rules
  (`discovery.go:45-130, 261-296`):
  - Every metric is an exact value present in its pinned source line (path, sha256, line, quote).
  - Provenance is cited, calculated or synthetic.
  - Ratings are pinned the same way.
  - Completeness comes only from a five-stage checklist (sources, analysis, verification,
    downstream, delivery) whose done items carry verified evidence.
- `/api/catalogue` already serves these runs; the Library screen does not use them (`boot.js:11-15`).
- Retained curated runs are seeded from the example's catalogue (`sync_assets.py:18-20`). App runs
  write no manifest today, so they show nothing.

**What this plan adds to the example:**

| Addition | How |
|---|---|
| Classification, currency, private-side label | Run fields from the context snapshot |
| Lowest rating | Ratings pinned to context snapshot lines; the scale orders them |
| Net and total leverage, interest cover, cash, undrawn facilities | Metrics from the latest annual or LTM row of CP-1's chart tables |
| Pro forma leverage (excluding unrealised add-backs; as marketed) | Separate metric keys from CP-2's table, each with its own basis; never in the default Leverage column |
| Facilities and quotes as entered | A new `facilities` field, provenance `user`, matched within one facility |
| Accepted limitations | Gaps, from `expectations.json` |
| Issuer grouping, latest run by default, Overview and Reports routes, URL hash state | Existing app behaviour, kept |

### Task 12: Run manifest for every finished app run

**Files:** modify `apps/issuer-library/engine/bridge.py`, `apps/issuer-library/model.go`,
`apps/issuer-library/discovery.go`, `apps/issuer-library/discovery_test.go`, `tests/test_cpos_app.py`;
create `tests/fixtures/library-manifest/` (hand-written expected manifests).

- [ ] Hand-write the expected manifests first: one synthetic run and one from the retained CP-1 chart
      handoff (`7f0578…`).
- [ ] After delivery, `bridge.start` writes `runs/<id>/library.json`:
  - **Identity:** identity and sector pinned to context-snapshot lines; date = as-of; currency;
    classification; the private-side flag from `case_kind`.
  - **Chart metrics:** `leverage`, `net_leverage`, `coverage`, `cash` and `undrawn`, from the latest
    annual or LTM row of CP-1's chart tables.
    - Each is pinned to its row's line, with provenance `calculated`.
    - Its basis is the row's "Basis and limitation", its unit the Reporting unit, its period the Period.
  - **Pro forma metrics:** on Primary runs, `leverage_pro_forma` and `leverage_as_marketed`, from
    CP-2's Pro forma leverage rows.
  - **No metric written:** for a `Not supplied` cell, a negative value or a missing table. The run then
    shows Not recorded.
  - **Ratings and facilities:** pinned to context-snapshot lines, with provenance `user`.
  - **Gaps:** the accepted limitations' reasons, plus "HTML Model not published by app runs".
  - **Checklist:**
    - sources: the pinned sources in `workflow.json`;
    - analysis: one item per requested module, done when accepted;
    - verification: the launcher's completion receipt;
    - downstream: delivered copies byte-identical per `delivery.json`;
    - delivery: the verified `report.html`.

    Each done item cites its evidence.
- [ ] **Admission:** `model.go` and `discovery.go` gain `classification`, `private_side`, `facilities`
      and provenance `user`, under the same rule (exact value in the pinned quote). Nothing else in
      admission changes.
- [ ] **Failure isolation:** a manifest failure never changes the run's outcome. It becomes a
      Settings issue, and the run shows Not recorded.
- [ ] **Tests:**
  - Hand-written manifests are admitted unchanged.
  - A changed value or line is rejected (existing rule).
  - A Primary run.
  - A run with no chart table.
  - Review Focus 22 and 24.

### Task 13: Port the screening frontend into the app's Library

**Files:**
- Create `apps/issuer-library/web/screening.js`, from `examples/issuer-library/logic.js`.
- Move and adapt `test_logic.cjs` and `test_dom.cjs` into `apps/issuer-library/web/`.
- Modify `web/boot.js` (expose the catalogue's runs), `web/views.js`, `web/screen.js`,
  `web/screen.css`, `web/library-workspace.test.cjs`, `web/screens.test.cjs`,
  `designs/browser_check.py`, `validate.py` (register the node tests).
- Create `tests/fixtures/library-credit/rating-scale.json`.

- [ ] **Port first:** `LibraryLogic` unchanged, with its existing tests passing in the app, before any
      extension.
- [ ] **Rating scale (hand-written fixture):**
  - S&P/Fitch `AAA`…`D` and Moody's `Aaa`…`C`, notch-aligned.
  - Bottom-of-scale equivalences marked approximate.
  - `(P)` and `(EXP)` read through, with their text kept.
  - SD, RD and `/LD` map to D. NR, WD and WR are off the scale.
- [ ] **Extend `filterRuns`** only for this plan's additions:
  - classification, currency and lowest rating (issuer scope by default);
  - the pro forma metric keys;
  - facility and quote filters matched within one facility: single values inside the filter, talk
    and bid-ask by overlap;
  - accepted limitations;
  - latest run per issuer (default) or any run.
- [ ] **Library screen:**
  - The example's screening panel, results table and selected-run detail, inside the app's rail and
    workspace.
  - Rows join the store's runs by folder id, so each keeps its Overview and Reports routes.
  - Each figure shows value, unit, period and basis; its pinned line opens in the evidence inspector.
- [ ] **Coverage and hidden counts** per filter ("Coverage recorded for 3 of 44 runs · 12 hidden · Show
      them"). The filter state lives in the URL hash, which accepts only known controls and values.
- [ ] **Tests:** all text through `textContent`. The example's tests, plus Review Focus 17-21 and 23,
      keyboard and screen-reader labels, and narrow screens.
- [ ] **Browser walk:** extend `browser_check`'s real-workspace walk to the screening panel, each filter
      group, sorting, the run detail and hash restore.

### Task 14: Help, README, the example's status and Checkpoint D

**Files:** modify Help in `apps/issuer-library/web/views.js`, `apps/issuer-library/README.md`,
`examples/issuer-library/README.md`, `VERIFICATION.md`.

- [ ] **Help and README** explain:
  - each figure's pinned line;
  - the leverage bases, and why unrealised add-backs stay out of the base;
  - that missing values never match;
  - the latest-run rule;
  - that user values show as entered;
  - that completeness comes from the verified checklist.
- [ ] **The example's README** says its screening now lives in the app's Library. The example stays as
      the approved reference, and its tests keep running.
- [ ] **Checkpoint D:** offline gates and **D-live**.

## Done when

- **Context form:** the issuer identity section requires investment grade or high yield, and legal
  documents are declared. Every run type can record facilities, and older context files load and
  dump unchanged.
- **Review step:** lists forecast outcomes driven by declarations, with reasons and fixes.
  Structural and method-fit notes are shown but not counted.
- **Start:** cannot proceed past counted items without the separate acceptance. Every started run
  holds `expectations.json`, its context snapshot and the accepted item ids.
- **Primary runs:**
  - CP-4 reviews drafts and offering documents as Provisional, and the label reaches CP-3, CP-5,
    CP-6 and the report.
  - CP-2 reports the pro forma capitalisation, EBITDA ladder and leverage on three bases, with
    unrealised and unresolved add-backs shown and never counted.
  - C1, C1n, C1r, C2 and C3 have passed, with every required output, recorded with their actual
    scope.
- **Library:** the approved example's screening design, ported into the app.
  - Every finished app run writes a manifest that discovery admits.
  - It filters by classification, rating, leverage on a chosen basis, interest cover, cash, undrawn
    facilities, currency, completeness and the facility and quote terms.
  - Each figure links to its pinned line, user values show as entered, and missing values never match.
  - D-live has passed.
- **Beta V1:** the release gate has passed on the released `main` commit, including the Windows
  smoke test and the owner's sign-off.

## Review record (2026-11-08)

Two independent reviewers checked the merged plan: one fact-checked its claims against the code, the
other attacked its design. Adopted: everything above that differs from the merged version. Rejected,
with reasons, under **Rejected** above.

| Area | Correction adopted |
|---|---|
| Facts | 4 launcher runs, not 21; `store.py` parses no values; CP-3's parser and the `cp2h` refusal are owner-path only; `READER_PERSONA` is high-yield for every module; 78 context fixtures; `Run` has no run type |
| Outcomes | Declarations drive outcomes; non-recognition gives `Check` only; milder-of inheritance; `Check` never propagates; structural and investment-grade items are information, not counted |
| Primary | Provisional scope and propagation to report and downstream modules; final offering memorandum reason; ranks 2-5 as kinds; EBITDA ladder without double counting; structural checks instead of an equality; cash row, dates and FX rule; report table routes |
| Compatibility | Empty new fields omitted on dump; form blanks hidden talk; resume keeps context bytes; a context snapshot at Start |
| Library | Last annual or LTM row; negative leverage not meaningful; cash and undrawn filtered separately; latest run defined; rating-scale edge cases; private-side label; hash validation |
| Library | Owner chose the approved `examples/issuer-library` screening design and logic, fed by the existing manifest admission |
| Process | Live checkpoints A-live, A-ab, B-live, C1, C1n, C2, C1r, C3, D-live, each a related whole pathway except the single-module gates, with frontend and backend required outputs; beta V1 release gate; Phase 3 one module at a time; four PRs; tests registered in `PYTHON_TESTS` |
