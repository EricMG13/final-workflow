SECTION: S08-cp3   PASS: code-review
COVERAGE: src/deploy_workflow/owners/cp3.py, src/deploy_vii/inputs/rv_quotes.py (read fully by me; all five read fully by the forked code-review reviewer) / src/deploy_workflow/owners/cp3c.py, src/deploy_workflow/owners/cp3d.py, src/deploy_vii/cp3_relative_value.py (I read the validator, composer, operand and context-reader regions to verify each finding) / none not read

Independence note: the code-review skill ran as a forked reviewer. It read docs/review-handoff/S08-cp3/adversarial.md even though it was told not to, and it said four of its findings repeat that file's A07, A06, A01 and A09. Those four are C02, C04, C07 and C05 below. I did not read adversarial.md, any repro file from the earlier pass, or docs/review-handoff/**. I checked every finding again with my own scripts (the cr_*.py files in this folder). The forked reviewer's own scripts were saved outside this folder (scratchpad/fx.py and p.py), and I did not use them.

### S08-cp3-C01  [high] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cp3c.py:967` (check_currency), via `_millions_read` at :912-921
- Defect: check_currency requires every facility's T4.18 `annual_amortisation` to be in the reporting currency. CP-2D (`cp2d.py:~2152`) requires the same field to be in the facility's own stated currency. So a facility in another currency with a known amortisation makes CP-3C raise, and it never reaches the FX_REASON gap that `_facility` is meant to produce.
- Failure scenario: a USD run (cash_closing in USD) has a EUR term loan whose amortisation CP-1 records in EUR, as CP-2D requires. `compute()` raises `ValueError: CP-3C term-loan.annual_amortisation: currency 'EUR' is not 'USD'`, so CP-3C cannot settle. The intended result is the "Not calculable: facility term-loan is in EUR, not USD; no FX conversion is applied" gaps. The existing test test_c6_a_facility_in_another_currency... passes only because its EUR facility keeps a USD-stamped amortisation, which CP-2D would refuse. When cash_closing is not known, `reporting_currency()` can also pick EUR from this fact.
- Evidence: `cd /home/user/final-workflow && PYTHONPATH=src:.:tests .venv/bin/python <folder>/cr_c01_eur_amort.py` prints: baseline (amortisation stamped USD) ok, 21 own gaps; with the amortisation in EUR: `ValueError CP-3C term-loan.annual_amortisation: currency 'EUR' is not 'USD'`.
- Fix direction: leave out of `_millions_read` (and of the reporting-currency choice) the amortisation of any facility whose `terms.currency` differs from the reporting currency, or check it against the facility's own currency, so that `_facility` produces the FX gap.

### S08-cp3-C02  [high] [CONFIRMED]  correctness
- Location: `src/deploy_vii/cp3_relative_value.py:1057` (_market_row) and `:1543-1560` (_market, T3.3 "As of" cell)
- Defect: `MarketEvidence.as_of` is free model text. It is never parsed, never compared with the quoted span and never compared with `run.as_of`, yet T3.3 shows it as the quote's date. Model-cited pack quotes also never get the STALE_DAYS cap or limitation that context rows get.
- Failure scenario: the quote reads "Dealer quotation on January 9, 2026 ..." and the run as-of is 2026-01-10. If as_of is "January 9, 2031" (after the run), "the close", or "March 1, 2019" (seven years old), validation returns no issues, T3.3 shows the row as Observed with that date, and no stale limitation or confidence cap is added. Context rows get all of these checks: ISO date, not after the run, stale after 30 days.
- Evidence: `<folder>/cr_c04_asof.py` prints, for each of the three values, `issues: () | T3.3 m01: ('Observed', '<value>') | stale limitation: False`.
- Fix direction: require as_of to be a parseable date that occurs in the cited quote and is not after run.as_of, and apply the STALE_DAYS line and cap to pack quotes the same way `_stale_text` does for context rows.

### S08-cp3-C03  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/cp3_relative_value.py:1166-1175` (_cap_reasons) and `:1650-1657` (_evidence_limitations)
- Defect: the "indicative talk only" cap is worked out from `evidence.strength()` over all market evidence in the submission, not from what the preference's basis cites. A preference that rests only on indicative talk can therefore be published at High.
- Failure scenario: CP-2 is accepted and the preference's `basis.quotes` keeps only the page:2 indicative-talk quote, with confidence High. The page:1 observed row is still listed in market_evidence, so the strength is {observed, indicative_talk}. Validation passes, T3.4 shows High, and no "indicative talk only" limitation is added. The instrument-level check (`_talk_only`) does look at the basis, so the two rules disagree.
- Evidence: `<folder>/cr_c02b_talk_high_accepted.py` prints `talk-only basis -> issues: ()` and `T3.4 confidence: High | 'indicative talk only' limitation: False`.
- Fix direction: also cap the preference when `_talk_only(row.basis, evidence)` is true, keeping the submission-wide caps.

### S08-cp3-C04  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_vii/cp3_relative_value.py:1099-1117` (_basis_issues)
- Defect: a cited context row is only checked for existence. Its `facility_id` is never compared with the instrument row that cites it.
- Failure scenario: CP-1 has two facilities and the context file's rows c01/c02 belong to notes-2031. The term-loan instrument cites c01/c02 in `basis.context_rows`. Validation passes, and the T3.1 Term Loan basis shows "Market evidence context c01 (observed); ... c02 (indicative talk)", with the other facility's dealer levels and citations as the Term Loan's market basis.
- Evidence: the fixtures have one CP-1 facility, so `<folder>/cr_c03_context_facility.py` relabels the built context rows to `notes-2031` by wrapping `context_evidence`, which is what a second facility's rows would look like. It prints `issues: ()`, the instrument facility as term-loan, the rows' facility as notes-2031, and the T3.1 basis cell citing c01/c02.
- Fix direction: in `_instrument_issues`, refuse a `basis.context_rows` id whose `ContextRow.facility_id` differs from the instrument's `facility_id`.

### S08-cp3-C05  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cp3c.py:1087` (compose_operands) together with `:825-849` (compose_refinancing)
- Defect: CP-1 `cash_interest` is negated with no sign check. A positive stored value becomes negative interest paid. The base cover is then correctly "not meaningful", but the pro forma interest nets the step-up against the negative figure and prints an ordinary-looking multiple. CP-2A (`cp2a.py:252`) expects positive stored values and treats them as not meaningful.
- Failure scenario: cash_interest = +2.00 (the magnitude convention), adjusted EBITDA 30, step-up 1000 bp. Paid = -2.00, added = 5, pro forma = 3.00. Interest cover is n.m., but pro forma cover is 10.0000x, a strong figure produced by the sign error.
- Evidence: `<folder>/cr_c07_interest_sign.py` prints `paid -2.00 added 5 pro forma 3.00 | cover Gap('Not meaningful: cash interest paid is zero or negative ...') | pf cover 10.0000`.
- Fix direction: when the negated cash interest is zero or negative, carry the NM_INTEREST gap into pro_forma_interest and pro_forma_interest_cover, or refuse a positive CP-1 outflow.

### S08-cp3-C06  [medium] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cp3d.py:852-862` (_observation_date) and `:402-416` (_stale_lines)
- Defect: a bid/offer quoted from a pack source (not the context file) is never compared with the run as-of. A quote dated after the run is accepted, and a years-old quote gets no stale line. Only context-file observations get the STALE_DAYS rule.
- Failure scenario: run as-of 2026-01-10 and the quote "Dealer quotation on January 9, 2019: bid 98.50 and offer 99.25." Validation passes, DM/PD are computed over 4009 days to maturity, and no stale limitation is shown. A quote dated January 9, 2027 (after the run) is also accepted.
- Evidence: `<folder>/cr_c08_cp3d_dates.py` prints `January 9, 2019 issues: () days to maturity: 4009 | stale/date limitation: []` and the same for 2027 (1087 days).
- Fix direction: refuse an observation dated after `run_as_of`, and add the stale line for any bid/offer more than STALE_DAYS before it, whatever its source.

### S08-cp3-C07  [low] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cp3d.py:796-813` (_labelled/_label_ok)
- Defect: CP-3D accepts as executable bid/offer levels a quote that calls itself indicative and not firm. It has no equivalent of CP-3's TALK_MARKERS check, so the same span that CP-3 refuses as an observed row drives CP-3D's DM and PD.
- Failure scenario: "Indicative dealer quotation on January 9, 2026, subject to confirmation and not firm: bid 98.50 and offer 99.25." validates, and T3E reports bid 98.50%, offer 99.25% and DM 28.3 bp.
- Evidence: `<folder>/cr_c05_cp3d_indicative.py` prints `CP-3D issues: ()`, T3E.1 levels 98.50% and 99.25%, T3E.3 DM 28.3 bp, and `CP-3 talk markers in the same quote: ['indicative']`.
- Fix direction: refuse, or limit, a bid/offer whose quote contains a TALK_MARKERS phrase, as CP-3 does for observed rows.

### S08-cp3-C08  [low] [CONFIRMED]  correctness
- Location: `src/deploy_workflow/owners/cp3c.py:847-848` (interest_cover via _ratio at :513)
- Defect: interest cover is "not meaningful" only when its denominator is zero or negative. A negative adjusted EBITDA therefore gives a negative cover, while every ratio with EBITDA as the denominator is n.m.
- Failure scenario: adjusted EBITDA -30 and cash interest paid 5 give an interest cover of -6.0000x. The COST claim reads "changes interest cover from (6.00)x to (4.29)x", while payable/EBITDA beside it shows n.m.
- Evidence: `<folder>/cr_c07_interest_sign.py` prints `negative EBITDA: interest cover -6.0000 | payable/EBITDA Gap('Not meaningful: adjusted EBITDA is zero or negative ...')` and the COST claim text above.
- Fix direction: return an NM gap for interest cover and pro forma cover when EBITDA is zero or negative, or confirm that ruling C-2 means to publish negative covers.

### S08-cp3-C09  [low] [CONFIRMED]  correctness
- Location: `src/deploy_vii/cp3_relative_value.py:1195-1207` (_preference_issues)
- Defect: an "Insufficient Information" preference is exempt from citing market evidence, but it may still carry a full ordering. A ranking can therefore be published with no market basis.
- Failure scenario: confidence is Insufficient Information, basis.quotes is empty and the ordering is kept. Validation passes, and T3.4 shows the ordering "Northbridge Term Loan" with a basis of CP-2 rows only. With several instruments, an "A > B" ranking is printed even though no market evidence is cited.
- Evidence: `<folder>/cr_c06_insufficient_ordering.py` prints `issues: ()` and T3.4 with ordering 'Northbridge Term Loan', confidence 'Insufficient Information', and a basis made only of CP-2 rows.
- Fix direction: require an empty ordering when confidence is Insufficient Information and no market evidence is cited, or require a market citation whenever an ordering is given.

### S08-cp3-C10  [low] [CONFIRMED]  efficiency
- Location: `src/deploy_workflow/owners/cp3.py:81-84` (compute) together with `src/deploy_vii/cp3_relative_value.py:1667-1670` (relative_value) and `:1226-1236` (_risk_issues)
- Defect: one CP-3 compute runs `validate_relative_value` twice, each time with JSON round-trips and a fresh context parse. `Upstream.catalogue` is a property that rebuilds `cp2_catalogue` for every ref it checks.
- Failure scenario: a submission with 10 risks makes 2 validation passes, 25 catalogue rebuilds and 3 context parses in one compute.
- Evidence: `<folder>/cr_c09_counts.py` prints `counts: {'validate': 2, 'catalogue': 25, 'context': 3} | 21 ms`. The cost is small at this size and grows with the number of refs and risks.
- Fix direction: let `relative_value` accept already-validated evidence (or have compute skip its own pass), and build the catalogue once per call (a local variable or cached_property).

### Out of scope (one line each, optional)
- The CP-3C test fixture test_c6_a_facility_in_another_currency... uses a EUR facility with a USD-stamped amortisation that CP-2D would refuse, so it hides C01 (the test file is outside this section).

### Checked and sound (short bullets: what you attacked that held)
- rv_quotes.validate_rv_bytes: header and extra-column check, formula refusal, number and ISO-date lexemes, Excel serial detection, duplicate key, bid > ask, issuer as provider, damaged ZIP reported and not swallowed, control characters escaped in render().
- CP-3 context reader: duplicate JSON keys refused, citations only for unique one-line spans with exact raw lexemes, rows for facilities not in CP-1 listed as gaps, context quote dates after the run refused, the 30/31-day stale boundary.
- CP-3 forged context rows (model rows quoting source `context`) and a span quoted twice are refused. Observed rows quoting talk markers are refused.
- CP-3C `_ratio` treats denominators <= 0 as n.m. `months_from` and `_add_months` clamp at month end. Missing values stay Gap and never 0. An unsourced reporting currency raises. Facility ids that repeat are refused.
- CP-3D: bid > offer and bid/offer on different dates are refused. A level_text must occur whole in the quote. Maturity must fall after the quotation date. Context bid/offer must pair within one quote row.
- The separate context reader in cp3_relative_value, alongside deploy_workflow.context, is a deliberate layering choice pinned by a parity test, so it is not reported as a simplification.
