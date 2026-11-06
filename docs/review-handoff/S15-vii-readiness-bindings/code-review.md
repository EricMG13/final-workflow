SECTION: S15-vii-readiness-bindings   PASS: code-review
COVERAGE: 34 files read fully by the code-review skill fork (high), all files in files.txt; read fully by me: src/deploy_vii/readiness.py, src/deploy_vii/context_binding.py, src/deploy_vii/bindings/__init__.py / skimmed by me: preparation.py (text and xlsx paths, prepare_source, prepare, load_pack), cp_model_workflow.py (publish/verify and helpers), model_interface.py (_observed, T4.15 rows), registry.py (dependencies/plan/edge_rule), downstream_readiness.py (_requests, validate_downstream_review), contracts.py (Run/Source/Fact) / not read by me: the per-module binding maps bindings/cp*.py and shipped.py, model_readiness.py (the skill fork covered them and reported nothing there)

Independence note: the skill output did not mention any adversarial findings. I did not read adversarial.md, repro/ or a0*.py files. My section folder already held a work/ directory from the earlier pass. I saw its file names in a directory listing but did not open any of them. My scripts are in cr/.

### S15-vii-readiness-bindings-C01  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/readiness.py:322-336` (coverage_issues), with `absence_issues` at :276-298
- Defect: A CONDITIONAL consumer's `missing_source` names a source that is not in the pack. It is still checked against the consumer's attached sources, or against every ready paged source when nothing is attached. An uncited gap description is checked against every paged source. So a true statement that pages of a missing document are absent counts as a contradiction of the pack's own coverage.
- Failure scenario: The pack holds a 100-page annual report (ready) and a compliance certificate (missing). CP-4 is CONDITIONAL with source_ids=() and missing_source "Compliance certificate pages 1-20 not supplied". Separately, gap g1 (no citations) says "Facility agreement pages 30-45 not supplied". validate_review emits "Absence claim contradicts extraction coverage: page:1 to page:20 retained in annual-report", plus the same for pages 30-45. A correct readiness review is rejected and uses up its one repair, and CP-0 can end blocked.
- Evidence: `cd /home/user/final-workflow && PYTHONPATH=src:. .venv/bin/python <section>/cr/c_coverage.py` prints both "Absence claim contradicts extraction coverage" lines. Script: `/tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S15-vii-readiness-bindings/cr/c_coverage.py`
- Fix direction: Do not check `missing_source` against coverage, because it is about a source outside the pack. Check uncited gap descriptions only when they name a pack source, not by defaulting to every paged source.

### S15-vii-readiness-bindings-C02  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/readiness.py:94-128` (shape_issues / _container_too_short / _echoed)
- Defect: shape_issues drops a tuple/list `too_short` error whenever any item inside that container also fails. It assumes the length error only echoes the item failures. Pydantic also raises `too_short` when the input really is shorter than min_length, and that real error is then never shown.
- Failure scenario: shape_issues builds the repair issues for many owners (cp1b, cp1c, cp2a, cp2h, cp4c, ...). Take cp4c `treatments` (min_length=2). The model returns one treatment with a bad field. The repair prompt only mentions the bad field. The model fixes that field, the payload is rejected again for too_short, which it was never told about, and the one within-attempt repair is gone.
- Evidence: `cd /home/user/final-workflow && PYTHONPATH=src:. .venv/bin/python <section>/cr/c_too_short.py` shows: [1,'x'] with min_length=3: pydantic gives [(('a',1),'int_type'), (('a',),'too_short')] but shape_issues gives only ('a.1: Input should be a valid integer',). [1,2,'x'] (the real echo case) is suppressed correctly. Script: `/tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S15-vii-readiness-bindings/cr/c_too_short.py`
- Fix direction: Suppress the container error only when it is an echo, meaning the valid-item count (ctx actual_length) plus the number of distinct failed item indexes reaches ctx min_length. Read ctx for this one check, so the printed text stays stable.

### S15-vii-readiness-bindings-C03  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/model_interface.py:201-211` (_observed)
- Defect: An outflow is negated with `amount.copy_abs().copy_negate()`, which turns a zero into Decimal('-0') (or '-0.00'). Because -0 == 0, the cell is still labelled value_class 'source' with no normalisation note, even though its stored lexeme now differs from source_amount.
- Failure scenario: An outflow metric is reported as 0 for a period (for example dividends paid). The T4.15 fact gets amount "-0", source_amount "0" and value_class "source", and `render.display` shows "-0" in the deliverable. That is a changed source figure labelled as the unchanged source value.
- Evidence: `cd /home/user/final-workflow && PYTHONPATH=src:. .venv/bin/python <section>/cr/c_negzero.py` shows `0 -> {"amount":"-0","value_class":"source","source_amount":"0"}`, `0.00 -> "-0.00"`, and display('-0') gives '-0'. Script: `/tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S15-vii-readiness-bindings/cr/c_negzero.py`
- Fix direction: Negate only non-zero amounts (`-abs(x) if x else x`), so a source zero keeps its exact lexeme.

### S15-vii-readiness-bindings-C04  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/preparation.py:338` (xlsx_content: `cell.attrib["r"]`)
- Defect: The xlsx reader requires the `r` attribute on every `<c>`, but that attribute is optional in OOXML. Some minimal or streaming writers leave it out.
- Failure scenario: A valid workbook whose cells have no `r` raises KeyError('r'). prepare_source catches it, and the whole source is frozen as status 'unreadable' / extraction 'blocked' with "Preparation failed (KeyError): 'r'", even though every value could be read. The issuer evidence is lost for every consumer.
- Evidence: `cd /home/user/final-workflow && PYTHONPATH=src:. .venv/bin/python <section>/cr/c_prep.py` prints `cell without r: unreadable blocked Preparation failed (KeyError): 'r'`. Script: `/tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S15-vii-readiness-bindings/cr/c_prep.py`
- Fix direction: When `r` is absent, work out the address from the row's `r` (or a running row index) and a running column index, as the spec requires.

### S15-vii-readiness-bindings-C05  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/preparation.py:95` (text_content)
- Defect: `line:N` locators are numbered with `str.splitlines()`. That also splits on \f, \v, \x1c-\x1e, \x85 and  , so the locators drift from the file's real newline-delimited line numbers.
- Failure scenario: A pdftotext-style .txt source has a form feed at each page break. Each \f adds one line, so a citation `line:N` in the pack, the CP-0 facts and the deliverable evidence points to a different line of the preserved original. Anyone checking the citation against the original file by line number lands on the wrong line.
- Evidence: c_prep.py: for b"Revenue 10\x0cPage 2 header\nNet debt 42\n", 'Net debt 42' gets locator line:3, but it is line 2 of the file.
- Fix direction: Split on "\n" only (after normalising \r\n and \r), or record the locator semantics explicitly.

### S15-vii-readiness-bindings-C06  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/preparation.py:395-405` (xlsx_content sheet coverage)
- Defect: A sheet's coverage is 'retained' whenever any span was added. Styled blank cells (text "") and merged-range metadata spans also count as spans.
- Failure scenario: A formatted but empty 'Notes' sheet with a merged header is reported as 'retained'. The "sheet:Notes: empty" limitation is never produced, and CP-0's extraction_coverage tells the model that the sheet was extracted.
- Evidence: c_prep.py prints `empty Notes sheet coverage: [('sheet:Data','retained'), ('sheet:Notes','retained')]` and `limitation mentions Notes empty: False`.
- Fix direction: Mark a sheet 'retained' only when it added a non-metadata span with non-blank text or a formula. Otherwise mark it 'empty'.

### S15-vii-readiness-bindings-C07  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_vii/readiness.py:147-170` (citation_issues), called per assessment, consumer, gap and claim in validate_review (:380-470)
- Defect: Every call rebuilds the source index, and each citation's locator is found by a linear scan of source.spans. validate_review and build_readiness also round-trip the whole pack through JSON several times.
- Failure scenario: A 50k-cell workbook with 300 citations takes about 0.85 s per citation_issues call. That cost repeats for each review item that cites the workbook, and again on every repair and in build_readiness.
- Evidence: `<section>/cr/c_perf.py` prints `300 citations over 50000 spans: 0.85s`. Script: `/tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review/S15-vii-readiness-bindings/cr/c_perf.py`
- Fix direction: Build a {source_id: {locator: position}} map once per validate_review and pass it in. Validate the pack once and reuse it in build_readiness.

### Out of scope (one line each, optional)
- None found that is serious.

### Checked and sound (short bullets: what you attacked that held)
- I checked three skill findings in cp_model_workflow.py and did not report them, because callers compensate. publish_cp_model only catches ValueError at store.finish, so an OSError leaves the ticket pending. A CpModelRefused re-raise drops _interrupt's "could not be interrupted" text. Both production callers (financial_workflow.py:2017-2040, owner_workflow.py:2475-2492) catch Exception and interrupt any pending ticket, recording "interruption failed" when that fails. verify_cp_model_publication's possible OSError from store.result or _page needs an unreadable blob or temp dir, and the publish path runs it inside the same catch-all.
- shape_issues correctly drops the spurious too_short when the input length already meets min_length ([1,2,'x']).
- absence_issues / _retains are bounded by the source page count. Negation and locative phrases are filtered as documented.
- validate_financial_context: the dict lookups (periods[...], source_index[...]) are guarded by validate_source_context ("Assess every prepared source exactly once") and validate_financial_review (unknown period checks), which run before them.
- registry.plan/dependencies: an unknown id raises, a cycle raises, and the CP-5 fan-in excludes CP-MODEL as documented.
- validate_bindings: an all-wildcard coordinate is refused, there is no catch-all, and every unbound or doubly bound fact is reported.
- preparation.prepare keeps path containment (resolve plus is_relative_to, absolute paths refused), the byte cap and complete.json written last. load_pack re-hashes the originals.
