SECTION: S15-vii-readiness-bindings   PASS: adversarial
COVERAGE: read fully: readiness.py, downstream_readiness.py, model_readiness.py, preparation.py, registry.py, contracts.py, model_interface.py, cp_model_workflow.py, context_binding.py, bindings/__init__.py, bindings/shipped.py, bindings/cp0.py, cp1.py, cp1a.py, cp1b.py, cp8.py, cp_model.py / skimmed (checked by script only: table literals vs producers, slot overlaps per Pathway): bindings/cp1c, cp1d, cp2, cp2a, cp2d, cp2e, cp2g, cp2h, cp3, cp3c, cp3d, cp4, cp4c, cp5, cp6, cpdr, cpl10 / not read: none
Scratch scripts: R/S15-vii-readiness-bindings/work/ (R = review root)

### S15-vii-readiness-bindings-A01  [medium] [CONFIRMED]  control flow / crash on corrupt input
- Location: `src/deploy_vii/preparation.py:466-487` (prepare_source except list), and the per-page handler at `:228` (_pdf_pages)
- Defect: prepare_source catches only a fixed list of exception types. zlib.error and RuntimeError (xlsx), and AttributeError and pypdf LimitReachedError (pdf) escape it, so a corrupt source crashes the caller instead of becoming an `unreadable` Source.
- Failure scenario: one damaged PDF or XLSX among the issuer files makes `prepare()` raise, and no pack is written for the good sources either. The CLI (`deploy_workflow/context.py:918`, catches only ValueError/FileExistsError) and `run_inputs._require_ready` (which should raise SourceUnreadable) show a raw traceback instead of a typed refusal.
- Evidence: `work/fuzz_pdf.py`: 1,500 byte mutations of a valid 3-page PDF gave 32 LimitReachedError and 21 AttributeError escapes. `work/fuzz_xlsx.py`: 3,000 mutations gave 774 zlib.error and 1 RuntimeError ("File ... is encrypted"). `work/repro_prepare_abort.py` (good.txt + one bad file) printed: `crash_error.xlsx -> prepare raised zlib.error ; pack written: False`. The same happened for AttributeError.pdf, LimitReachedError.pdf and RuntimeError.xlsx.
- Fix direction: in prepare_source (and the PDF per-page try), also catch `zlib.error`, `RuntimeError`, `EOFError` and `pypdf.errors.PyPdfError`, or catch any extractor `Exception`, and record the source as unreadable with its limitation.

### S15-vii-readiness-bindings-A02  [medium] [CONFIRMED]  readiness gate accepts unavailable evidence
- Location: `src/deploy_vii/downstream_readiness.py:229-243` (_evidence_tags), used at `:290-298` (validate_downstream_review)
- Defect: the docstring says "Only compatible, available numeric evidence can support sufficient inputs", but only the kpi, statement_* and observation kinds are checked for null values. A `computation` record whose `value.amount` is None (operation "unavailable") is still tagged `computation`.
- Failure scenario: the CP-1 readiness model marks CP-2's `calculation_register` (group `{computation}`) "sufficient" while citing only unavailable computations, and the validator accepts it. The consumer row can then reach ready or ready_with_limitations, even though the register it depends on has no computed values. `fcf_build`'s computation group can be met the same way.
- Evidence: `work/repro_unavailable_computation.py` printed: `unavailable kpi tags: set()` / `unavailable computation tags: {'computation'} (expected empty)` / `calculation_register satisfied by unavailable computation: True`.
- Fix direction: in _evidence_tags, return an empty set for `computation` (and other numeric kinds, such as historical_value and canonical_value) whose `value.amount` is None.

### S15-vii-readiness-bindings-A03  [low] [CONFIRMED]  absence-claim guard gap
- Location: `src/deploy_vii/readiness.py:240-263` (_PAGE_RANGE / absent_page_ranges), used by coverage_issues/absence_issues
- Defect: only page ranges are recognised, so a claim that one page or a list of pages is absent is never compared with extraction coverage. Rule source_readiness.f says "Never call a page or locator absent when that coverage lists it".
- Failure scenario: a CP-0 limitation "page:7 is missing" passes validation although page 7 is retained. The false limitation reaches the T8 limits, Module limitations and the Limitations rail.
- Evidence: `absent_page_ranges('page:7 is missing') -> ()`, `('Pages 3 and 4 are missing') -> ()`, `('pp. 3-5 missing') -> ()`, while `('pages 3-5 are missing') -> ((3, 5),)`.
- Fix direction: also match a single `page[s] N` / `page:N` reference, and comma or "and" lists, as (N, N) ranges in the same absence clause.

### Out of scope (one line each, optional)
- `deploy_vii/execution.py:current_inputs`: CP-5's fan-in makes every selected analyst a required graph input, so one analyst that CP-0 judged CONDITIONAL (no head) leaves CP-5 unrunnable ("Required upstream is unrun") instead of restricted. Not reproduced.

### Checked and sound (short bullets: what you attacked that held)
- readiness.validate_review:
  - The pack hash is bound.
  - Every pack source and every planned live consumer is assessed exactly once.
  - Aliases are refused.
  - READY requires verified sources with no limitations, and no gap may name a READY consumer.
  - With issuer_confirmed=false, no consumer can be runnable.
  - Citations are checked against status, sha, locator and quote.
  - A blank quote is refused.
  - A non-ready consumer needs limitations; CONDITIONAL also needs missing_source.
  - Unknown readiness never defaults to pass, and T8 writes "DO NOT RUN" for anything below READY_WITH_LIMITATIONS.
- execution.current_inputs requires exactly `Run <id>` from the CP-0 head; the NOT_CONSUMERS set matches its exemption set.
- downstream_readiness._assess_consumers:
  - An unassessed requirement or gap gives not_ready.
  - A context/context_binding BLOCK gap cannot be excluded.
  - kpi_dashboard "sufficient" requires every KPI to be known.
  - Duplicate requests are rejected.
- model_readiness._evaluate:
  - Duplicate or unknown quarter ids are flagged.
  - Fewer than 4 quarters are flagged.
  - Contiguity, the fiscal-slot sequence and the 364-371 day window are checked.
  - A missing value or a conflicting value (amount None) means missing, never zero.
  - Mandatory check types are present for each quarter; conflicts block.
- preparation:
  - Path traversal and symlinks outside the root are refused (resolve + is_relative_to).
  - The size cap is enforced.
  - The sha256 of the raw bytes is taken.
  - The completion marker is written last; load_pack re-hashes the originals.
  - XLSX: DTD/entity and external relationships are refused, duplicate ZIP members are refused, and the expansion cap uses the declared size (zipfile truncates output to it).
- registry:
  - 25 module ids, no duplicate ids or aliases, and every required/optional/edge-rule target is a known id.
  - Cycles are detected; aliases canonicalise; retained keys must be canonical.
  - StepChain/checked_chains reject duplicate steps, cells and modules.
- contracts: Fact numeric requires unit+period; known/missing semantics hold; validate_tables rejects omitted or duplicated facts and coordinate mismatches; Source ready requires hash+spans.
- model_interface:
  - Facility amounts keep the facility currency.
  - Rates and bps carry no currency; effective_tax_rate is decimal_fraction.
  - Null amounts become missing/not_applicable facts with reasons plus InterfaceGap.
  - KPI/segment/addback "template" fields are stable per id (financial_validation enforces this).
- cp_model_workflow:
  - Basis step indices are correct (CP1_STEPS has 4 steps, so quality is index 4).
  - The output directory must be new; failures interrupt the attempt.
  - Verify re-derives all three files from the journal.
- bindings:
  - Every bound table literal exists in a producer (CP-1B's are built dynamically).
  - No two overlapping bindings land in one block or in two blocks composed by the same Pathway.
  - CP-1A's row-scoped binding matches the producer's single row.
  - Render fails closed on unbound facts.
- context_binding: entity, dimension and period scope are required for every financial observation citation; pro forma needs a matching located event.
