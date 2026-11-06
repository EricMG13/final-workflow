# Fable review of all 257 findings (repo a313b50 + docs/review-handoff, read-only)

## Summary

Verdicts over all 257 findings: **253 AGREE, 2 DISAGREE, 2 NEEDS-EVIDENCE**. I re-ran every one of the 47 critical/high repros myself (45 Python scripts or Go tests, plus the live Go binary for S18-A01) and all 47 reproduced; of the 210 medium/low findings, 180 were re-run (patching four scripts whose paths pointed at the old `/workspace` checkout), 28 were settled by reading the cited code, and 2 timing-only efficiency items were taken from the report. I changed **22 severities**: 16 raised (2 to critical: S12-A02 signed-refund flip and S13-C01 quarter period label on trailing ratios; S13-A03 to high, S13-C06 and S16-C05 to medium on their own merits; 11 duplicates lifted to their group's level) and 6 lowered for reachability (S05-C02, S10-C01, S11-C07, S12-C02, S17-C03, S18-A03). I found **42 duplicate groups** (listed below), mostly adversarial/code-review pairs within a section, plus six that span sections (substring quote matching, `splitlines` locators, raw `{ref}` claim limitations, dead CP-OS transport, repeated validation per submit, copy-pasted owner helpers). Four findings cite line numbers that do not exist in the file (S17-A08, S17-C12, S18-A05, S18-A09: `runtime.py` has 74 lines, `settings.go` 79, `platform_windows.go` 62); their defects are real but the citations must be fixed before the report is handed on. S10-A05's root cause (the CP-8 registry entry) lives in `owner_workflow.py`, an S02 file. The three worst problems in the codebase: (1) **units, currency, scale and sign are stamped by Python from model text or a default and never checked against the cited source** — the same hole appears in the CP-1D bridge (S05-C01 critical, deterministic 1000x + wrong currency), CP-1D basis amounts (S05-A01), CP-2E rows (S06-A04 thousands as millions, S06-A03/C01 interest sign), CP-3D levels (S08-A03/A04 percent read as price, bp as %), the research peer sheet (S16-A01/A02/C01/C02) and the shared `quotes.quoted` substring matcher (S13-A03/C05) that lets "2.50:1.00" verify against "12.50:1.00"; (2) **period arithmetic and labelling in the deploy_vii engine is wrong for whole classes of inputs** — CFS balances summed as flows (S12-A01 critical: Q2 closing cash 20 instead of 520), a signed tax refund flipped to an outflow (S12-A02), trailing ratios labelled with the quarter's dates (S13-C01), leap-year and Q1->Q2 pairs refused by the earnings delta (S11-A04), annual columns verified as Q4 under dated headers (S11-A01), and structural BLOCKs hidden as WARN "absent input" (S13-A01/C02); (3) **validators that accept a model answer and then wedge or mislead** — CP-2D can never settle for an issuer without a facility schedule (S06-A01), CP-4C passes validation then raises after the paid response is retained (S09-A04/C02), CP-5 flags every verbatim copy table as a figure mismatch (S09-A01/C01), CP-2G accepts an unchecked break metric and unvalidated limitation text (S07-A01/A02), and the CP-8 run comparison has no code-level diff at all (S01-A03 and CLAIMS #2, which I confirm: `comparison_files` checks table shape and citations only).

## Findings table

| id | verdict | severity_in | severity_out | duplicate_of | basis | note |
|---|---|---|---|---|---|---|
| S01-orchestration-A01 | AGREE | medium | medium (KEEP) | S01-orchestration-C03 | rerun | Same key collision as C03; c04 script printed pinned keys ['10-K.html.jsonl'], converted text unreferenced, ignored (). |
| S01-orchestration-A02 | AGREE | medium | medium (KEEP) | S01-orchestration-C02 | rerun | Script hard-codes /workspace path; same torn-_put defect shown by C02's test_c03_torn_put (executor not called, truncated bytes accepted). |
| S01-orchestration-A03 | AGREE | medium | medium (KEEP) | - | rerun | Same bundle as prior and current published a 'checked' CP-8 comparison; also the only indexed trace of CLAIMS #2 (no code diff). |
| S01-orchestration-C01 | AGREE | medium | medium (KEEP) | - | rerun | Test showed through not in cap.json, UnknownThrough on resume, resume walk kwargs through=None. |
| S01-orchestration-C02 | AGREE | medium | medium (KEEP) | - | rerun | test_c03_torn_put passed: executor called on resume False, truncated bytes accepted. |
| S01-orchestration-C03 | AGREE | medium | medium (KEEP) | S01-orchestration-A01 | rerun | Reproduced; source identity lost silently when a sibling <name>.jsonl exists. |
| S01-orchestration-C04 | AGREE | medium | medium (KEEP) | - | rerun | FileExistsError at run_pathway.py:616 on every resume after a stale run.json.tmp. |
| S01-orchestration-C05 | AGREE | medium | medium (KEEP) | - | rerun | Rerun with fixed checker raised WorkflowError identity_mismatch at cpos.py:225 with no executor call. |
| S01-orchestration-C06 | AGREE | low | low (KEEP) | - | code-read | transport() called only from tests; CLAIMS addendum: path also broken (claim.plain). Dead-code finding, low is right. |
| S01-orchestration-C07 | AGREE | low | low (KEEP) | - | code-read | replay.py:391 and :614 both build _Earlier; local I/O only. |
| S02-module-framework-A01 | AGREE | medium | medium (KEEP) | - | rerun | Unrelated gaps containing 'bridge'/'portfolio' and 'illegal_documents' satisfy the gate; oracle regex pins the token rule. |
| S02-module-framework-A02 | AGREE | low | low (KEEP) | - | rerun | U+02C2, U+2039, U+1438, U+276E, U+3008, U+2329, U+16B2 accepted; model impact unprovable offline. |
| S02-module-framework-A03 | DISAGREE | low | low (KEEP) | S01-orchestration-C06 | rerun | Trigger is the dead transport path (ACTIVE never set in production); CLAIMS #1 confirms handoffs flow via HandoffTask instead. |
| S02-module-framework-C01 | AGREE | medium | medium (KEEP) | - | rerun | FenceError from a REPAIR issue quoting <<<CONTEXT; model echo can end the run. |
| S02-module-framework-C02 | AGREE | medium | medium (KEEP) | - | rerun | Both raw lines raised UnicodeDecodeError with no answer and no fault record. |
| S02-module-framework-C03 | AGREE | low | low (KEEP) | S02-module-framework-A01 | rerun | Legal substring rule is the legal half of A01. |
| S02-module-framework-C04 | AGREE | low | low (KEEP) | S02-module-framework-A02 | rerun | Same confusable set accepted. |
| S02-module-framework-C05 | AGREE | low | low (KEEP) | - | rerun | _capture calls per render_owner_slice: 6. |
| S03-model-provider-A01 | AGREE | medium | medium (KEEP) | - | rerun | EUR/JPY/None currency scored as match against USD golden; model-testing only, medium is right. |
| S03-model-provider-A02 | AGREE | medium | medium (KEEP) | - | rerun | Escaped key kept in calls.jsonl error field for {"error":str}/{"detail":...} shapes; narrow trigger, raw archive guarded, medium stands. |
| S03-model-provider-A03 | AGREE | medium | medium (KEEP) | - | rerun | Live hold 6.72 vs offline ContextTooLong at 400K tokens. |
| S03-model-provider-A04 | AGREE | low | low (KEEP) | S03-model-provider-C03 | rerun | Traceback with /home/user/final-workflow path recorded (script checked old /workspace string); copilot stub crashed but C03 shows session.error path. |
| S03-model-provider-C01 | NEEDS-EVIDENCE | medium | medium (KEEP) | - | rerun | Adapter side reproduced (IdleTimeout / UnparsableReply); needs the real Copilot runtime's event sequence for an unoffered tool. |
| S03-model-provider-C02 | AGREE | medium | medium (KEEP) | - | rerun | Live sent_usage ModelMismatch exported and replayed as sent_unknown. |
| S03-model-provider-C03 | AGREE | low | low (KEEP) | S03-model-provider-A04 | rerun | session.error keeps C:\Users\Jane Doe path; _paths_in gives <path>et/project/x.js. |
| S03-model-provider-C04 | AGREE | low | low (KEEP) | - | code-read | pricing.py:174-189 repeats all twelve _SOL fields. |
| S03-model-provider-C05 | AGREE | low | low (KEEP) | - | code-read | turn.py:132 check cannot fail after CONFIG_PROVIDERS check; four literal provider lists. |
| S03-model-provider-C06 | AGREE | low | low (KEEP) | S03-model-provider-C02 | code-read | Design concern; C02 is its one concrete symptom. |
| S04-delivery-A01 | AGREE | high | high (KEEP) | - | rerun | Block scale None, note None, 'EUR thousands' nowhere in the financials block; unit lost at the boundary. |
| S04-delivery-A02 | AGREE | medium | medium (KEEP) | - | rerun | attacks5: 0.004 -> '0.00', 0.125 -> '0.13x'; attacks4 path stale but model_handoff_delivery.py:468 decimals=0 confirms HTML Model side. |
| S04-delivery-A03 | AGREE | medium | medium (KEEP) | - | rerun | Sign-flipped, unit-swapped and scale-swapped summaries all ACCEPTED. |
| S04-delivery-A04 | AGREE | low | low (KEEP) | - | rerun | attacks1 A1 categories left->right newest-first. |
| S04-delivery-A05 | AGREE | low | low (KEEP) | S15-vii-readiness-bindings-C05 | rerun | 6 citations drift after U+2028; same splitlines root cause as S15-C05. |
| S04-delivery-A06 | AGREE | low | low (KEEP) | - | rerun | 'DRAFT: internal estimate 999 ... -->' published in report.html. |
| S04-delivery-A07 | AGREE | low | low (KEEP) | - | rerun | EUR m rows charted as US$m on the direct delivery path; cpos_launch gate catches it on the launch path. |
| S04-delivery-C01 | AGREE | high | high (KEEP) | - | rerun | ValidationError 'Tab labels are distinct'; 'Earnings view' routes exist in retained earnings_update run and catalog.json. |
| S04-delivery-C02 | AGREE | medium | medium (KEEP) | - | rerun | Three pipe lines dropped from every fact; '#1 risk' became an empty heading. |
| S04-delivery-C03 | AGREE | medium | medium (KEEP) | - | rerun | Two same-named ### Notes merged into one prose table. |
| S04-delivery-C04 | AGREE | medium | medium (KEEP) | - | rerun | Stanford accepted for issuer Ford; alias 'AB' matched 'lab'. |
| S04-delivery-C05 | AGREE | medium | medium (KEEP) | - | rerun | Axis labels ['0','1','1'] for 0/0.5/1.0 ticks. |
| S04-delivery-C06 | AGREE | medium | medium (KEEP) | - | rerun | All three raw tables titled with the bold Assessment paragraph. |
| S04-delivery-C07 | AGREE | medium | medium (KEEP) | - | rerun | Four list items collapsed into one fact. |
| S04-delivery-C08 | AGREE | low | low (KEEP) | - | rerun | Table route into metric-strip accepted; row reachable only via passport field. |
| S04-delivery-C09 | AGREE | low | low (KEEP) | S04-delivery-A02 | rerun | 7.2500% / 1,234.57; same fixed-decimals root cause as A02 (markdown_delivery.py:381-385). |
| S04-delivery-C10 | AGREE | low | low (KEEP) | - | rerun | 'Not supplied: undisclosed' -> ValueError in build_model but a gap in charts. |
| S04-delivery-C11 | AGREE | low | low (KEEP) | - | code-read | String-patching of DEST confirmed at markdown_delivery.py:797-801; rail highlight on model.html unverified without a browser. |
| S05-cp0-cp1-A01 | AGREE | high | high (KEEP) | S05-cp0-cp1-C01 | rerun | Percent, count, EUR and bps numerals all ACCEPTED as USD MILLIONS basis; same basis-unit family as C01. |
| S05-cp0-cp1-A02 | AGREE | medium | medium (KEEP) | S05-cp0-cp1-C04 | rerun | 2023-12-31 issuer line vs LTM 2025 -> Reconciled with CP-1 period. |
| S05-cp0-cp1-A03 | AGREE | medium | medium (KEEP) | - | rerun | 2027-12-31 and 2012-12-31 peers Included, n=4, no period limitation beyond one partial-comparability line. |
| S05-cp0-cp1-A04 | AGREE | medium | medium (KEEP) | - | rerun | BLOCK check with calculated_value None -> Calculated weight 9. |
| S05-cp0-cp1-A05 | AGREE | medium | medium (KEEP) | S05-cp0-cp1-C03 | rerun | Forged envelope accepted with gap_limitations () and swapped registers hash. |
| S05-cp0-cp1-A06 | AGREE | low | low (KEEP) | - | rerun | Contradictory Basis lines -> USD MILLIONS accepted. |
| S05-cp0-cp1-C01 | AGREE | critical | critical (KEEP) | - | rerun | EUR-thousands bridge parses identically to USD-millions; T1D facts stamped USD MILLIONS, no limitation. Critical stands (deterministic 1000x + currency). |
| S05-cp0-cp1-C02 | AGREE | high | medium (LOWER: fails closed (torn refusal, no wrong output), millisecond crash window, same pattern in six other one-step owners) | - | rerun | Retry raised 'Submit the next module step in order'; cp0 path resumed. cp1c:3288/cp1d:2546 confirmed same pattern. |
| S05-cp0-cp1-C03 | AGREE | medium | medium (KEEP) | S05-cp0-cp1-A05 | rerun | FORGED ACCEPTED: score=95 band=High gap_limitations=0. |
| S05-cp0-cp1-C04 | AGREE | medium | medium (KEEP) | S05-cp0-cp1-A02 | rerun | difference 0 stamped LTM Q4 25, result Reconciled across periods. |
| S05-cp0-cp1-C05 | AGREE | medium | medium (KEEP) | - | rerun | candidate/0 gaps/4 boilerplate limitations -> restricted; 0 limitations -> complete. Every CP-1 capped at 59. |
| S05-cp0-cp1-C06 | AGREE | low | low (KEEP) | - | rerun | _default_pairs raises on '2025²'. |
| S05-cp0-cp1-C07 | AGREE | low | low (KEEP) | - | report-only | Timing-only repro (11 s) not rerun; call pattern plausible from cp1_workflow.py:256-283. |
| S05-cp0-cp1-C08 | AGREE | low | low (KEEP) | - | rerun | compute parses/composes 2x, _checked path 3x. |
| S05-cp0-cp1-C09 | AGREE | low | low (KEEP) | S05-cp0-cp1-C02 | code-read | Byte-identical one-step bodies in cp1b/cp1c/cp1d; the C02 fix must be made three times. |
| S06-cp2-ade-A01 | AGREE | high | high (KEEP) | - | rerun | maturity_refs set() -> unsatisfiable 'must cite T4.18 maturity_date' with no schedule or zero debt. |
| S06-cp2-ade-A02 | AGREE | high | high (KEEP) | - | rerun | Row with FY cell absent accepted; Q4 2.25 recorded as FY 2025 FCF. |
| S06-cp2-ade-A03 | AGREE | high | high (KEEP) | S06-cp2-ade-C01 | rerun | (5.00) read as -5.00; interest_after -4.5 known. |
| S06-cp2-ade-A04 | AGREE | high | high (KEEP) | - | rerun | 'amounts in thousands' quote accepted; Total debt 50.00 stamped MILLIONS scale 1e6. |
| S06-cp2-ade-A05 | AGREE | medium | medium (KEEP) | - | rerun | 1e300 passes validator, submit raises, attempt stays pending on every resume. |
| S06-cp2-ade-A06 | AGREE | medium | medium (KEEP) | - | rerun | Critical CP-1A gap restated as 'Gap (Minor): Minor wording point' with no issue. |
| S06-cp2-ade-A07 | AGREE | medium | medium (KEEP) | - | rerun | Currency 'RCF' stamped on every fact without a run context. |
| S06-cp2-ade-C01 | AGREE | high | high (KEEP) | S06-cp2-ade-A03 | rerun | (20) with 1000bp -> interest_after 10, cov_after known 20.0x. |
| S06-cp2-ade-C02 | AGREE | medium | medium (KEEP) | - | rerun | Assessment text, credit_implication, rationale all absent from the settled module. |
| S06-cp2-ade-C03 | AGREE | low | low (KEEP) | S10-cp6-cp8-cpl10-C04 | rerun | claim.limitation keeps raw {T4.10.lev\|x}; same pattern as cp6 (S10-C04). |
| S06-cp2-ade-C04 | AGREE | low | low (KEEP) | - | rerun | T2B.2 value column headed 'EBITDA'. |
| S06-cp2-ade-C05 | AGREE | low | low (KEEP) | S07-cp2-gh-C03 | code-read | Only cp2a/cp2h clip the refusal text (grep -c clipped: 1,0,1,0); copy-paste helper theme. |
| S06-cp2-ade-C06 | AGREE | low | low (KEEP) | S07-cp2-gh-C01 | code-read | cp2a.py:1733-1743 validates then downside_report validates again; repeated-validation theme. |
| S07-cp2-gh-A01 | AGREE | high | high (KEEP) | - | rerun | Swapped metrics pass; b03 down flips FY2026 -> Not reached by FY2028 vs control probe. |
| S07-cp2-gh-A02 | AGREE | high | high (KEEP) | - | rerun | Bare figure + probability text accepted as limitation on three claims; refused as rationale. |
| S07-cp2-gh-A03 | AGREE | medium | medium (KEEP) | - | rerun | Issuer BB vs secured notes Ba1 -> notches 1, lower_rated Alder. |
| S07-cp2-gh-A04 | AGREE | medium | medium (KEEP) | - | rerun | All views flipped to Upgrade potential with three downgrade triggers reached: issues (). |
| S07-cp2-gh-A05 | DISAGREE | medium | medium (KEEP) | - | rerun | Behaviour reproduced but it is the oracle-pinned 'missing is never 0' rule (cases/cp2g-owner build.py NC_E); a methodology ruling question, not a code defect. |
| S07-cp2-gh-A06 | AGREE | low | low (KEEP) | - | rerun | Issuer+facility rows for one agency -> 'Rating register not found'. |
| S07-cp2-gh-A07 | AGREE | low | low (KEEP) | - | rerun | 'Stable' vs 'stable ' -> Different. |
| S07-cp2-gh-C01 | AGREE | low | low (KEEP) | - | rerun | content_issues 6, compute 2 per submit (123 ms). |
| S07-cp2-gh-C02 | AGREE | low | low (KEEP) | S07-cp2-gh-C01 | rerun | validate 6, _compose 8, select_cp1 66 per submit. |
| S07-cp2-gh-C03 | AGREE | low | low (KEEP) | - | rerun | AST-identical stale_issues/_run_text_issues/SynthesisGap in cp2g, cp2h, cp4c. |
| S08-cp3-A01 | AGREE | high | high (KEEP) | - | rerun | 'Indicative ... subject to confirmation and not firm' bid/offer accepted; DM 28.3 bp as if firm. |
| S08-cp3-A02 | AGREE | high | high (KEEP) | - | rerun | Southgate Notes levels bound to Northbridge Term Loan: DM 279.7 bp, PD 30.98%. |
| S08-cp3-A03 | AGREE | high | high (KEEP) | - | rerun | 'bid 6.25%' -> price 0.0625, DM 2356.7 bp; '175 bps' -> DM -1885.3. |
| S08-cp3-A04 | AGREE | high | high (KEEP) | - | rerun | margin 3.25% read as 3.25 bp; SOFR 430 bps read as 430%; yield_mid 4.3032. |
| S08-cp3-A05 | AGREE | high | high (KEEP) | S08-cp3-C06 | rerun | 2019 and 2027 quotation dates accepted, no stale line. |
| S08-cp3-A06 | AGREE | high | high (KEEP) | S08-cp3-C02 | rerun | as_of 'January 9, 2031' and 'the close' shown in T3.3. |
| S08-cp3-A07 | AGREE | high | high (KEEP) | S08-cp3-C04 | rerun | term-loan basis cites notes-2031 context rows; issues (). |
| S08-cp3-A08 | AGREE | medium | medium (KEEP) | - | rerun | Sub-span of a talk sentence submitted as Observed. |
| S08-cp3-A09 | AGREE | medium | medium (KEEP) | S08-cp3-C05 | rerun | cash_interest=+40 -> cover n.m. but pro_forma_cover 20.0000. |
| S08-cp3-A10 | AGREE | low | low (KEEP) | - | rerun | InvalidOperation escapes validate_rv_bytes. |
| S08-cp3-A11 | AGREE | low | low (KEEP) | - | rerun | Price 0 and case-variant duplicate -> OK: 2 rows. |
| S08-cp3-A12 | AGREE | low | low (KEEP) | - | rerun | template exists: False. |
| S08-cp3-C01 | AGREE | high | high (KEEP) | - | rerun | EUR amortisation -> ValueError; cp2d.py:2150-2156 confirmed to require the facility's own currency, so the contract conflict is real. |
| S08-cp3-C02 | AGREE | high | high (KEEP) | S08-cp3-A06 | rerun | Three as_of values accepted, no stale limitation. |
| S08-cp3-C03 | AGREE | medium | medium (KEEP) | - | rerun | Talk-only basis published at High with no 'indicative talk only' limitation. |
| S08-cp3-C04 | AGREE | medium | high (RAISE: same defect as A07 (other facility's quote becomes an instrument's market basis)) | S08-cp3-A07 | rerun | Relabelled rows accepted; T3.1 basis cites c01/c02 of notes-2031. |
| S08-cp3-C05 | AGREE | medium | medium (KEEP) | S08-cp3-A09 | rerun | paid -2.00, pf cover 10.0000x from the sign error. |
| S08-cp3-C06 | AGREE | medium | high (RAISE: same defect as A05 (stale/future sheet quotes accepted)) | S08-cp3-A05 | rerun | 2019 quote: 4009 days, no limitation; 2027 quote accepted. |
| S08-cp3-C07 | AGREE | low | high (RAISE: same defect as A01 (conditional quote drives DM/PD)) | S08-cp3-A01 | rerun | Indicative quote validates; CP-3 TALK_MARKERS would refuse it. |
| S08-cp3-C08 | AGREE | low | low (KEEP) | S08-cp3-A09 | rerun | Negative EBITDA -> interest cover -6.0000x while payable/EBITDA is n.m. |
| S08-cp3-C09 | AGREE | low | low (KEEP) | - | rerun | Insufficient Information preference keeps a full ordering with no market basis. |
| S08-cp3-C10 | AGREE | low | low (KEEP) | S07-cp2-gh-C01 | rerun | validate 2, catalogue 25, context 3 per compute. |
| S09-cp4-cp5-A01 | AGREE | high | high (KEEP) | S09-cp4-cp5-C01 | rerun | Identical value/unit/period copy under CP-4 T4F.2 -> figure_identity mismatch; cp1_references control (). |
| S09-cp4-cp5-A02 | AGREE | high | high (KEEP) | - | rerun | Threshold 6.00x from legal-other accepted under legal-covenants: headroom 5.00, Within threshold. |
| S09-cp4-cp5-A03 | AGREE | high | high (KEEP) | - | rerun | Step-down quote, threshold_text '4.00x' accepted; 2025 metric tested against the later step. |
| S09-cp4-cp5-A04 | AGREE | high | high (KEEP) | S09-cp4-cp5-C02 | rerun | content_issues () then compute raised 'rating is Adequate ... fails closed'; execution.py:853-857 writes the step before the validator. |
| S09-cp4-cp5-A05 | AGREE | medium | medium (KEEP) | - | rerun | 'no greater than 0.75x' with >= -> Within threshold; control 'not more than' refused. |
| S09-cp4-cp5-A06 | AGREE | medium | medium (KEEP) | S13-vii-canonical-context-A04 | rerun | 'five hundred million US dollars' accepted; digit form refused. Root cause prose.bare_figures (S13). |
| S09-cp4-cp5-A07 | AGREE | medium | medium (KEEP) | - | rerun | cash_flow_quality supported by a facility_id ref: issues (). |
| S09-cp4-cp5-A08 | AGREE | low | low (KEEP) | - | code-read | MARKERS is a two-phrase closed list (cp4.py:27), deliberately excluding 'defined in'. |
| S09-cp4-cp5-C01 | AGREE | high | high (KEEP) | S09-cp4-cp5-A01 | rerun | T4F.2 net_leverage_reported, cp2g_references and cp2a_references copies all flagged. |
| S09-cp4-cp5-C02 | AGREE | medium | high (RAISE: same wedge family as A04: ValueError out of the step validator after the paid response is retained) | S09-cp4-cp5-A04 | rerun | content_issues RAISED for a 2-basket head; swapped baskets pass then compute raises. |
| S09-cp4-cp5-C03 | AGREE | low | low (KEEP) | S09-cp4-cp5-C02 | rerun | Facilities offered while the note says name no facility; feeds C02. |
| S09-cp4-cp5-C04 | AGREE | low | low (KEEP) | - | code-read | LEGAL_AUTHORITIES includes draft (cp4_legal.py:91); messages at :488/:494 say 'executed or filed'. |
| S09-cp4-cp5-C05 | AGREE | low | low (KEEP) | - | code-read | T4F.3 prints str(t.result.amount) (:1196) while T4.9 shows x100 POINTS (:983-985). |
| S09-cp4-cp5-C06 | AGREE | low | low (KEEP) | S07-cp2-gh-C01 | rerun | python_checks called 3x per compute and per view_body. |
| S10-cp6-cp8-cpl10-A01 | AGREE | high | high (KEEP) | - | rerun | offer=98.00 (the bid) accepted; T7.4 mid 0.98, magnitude 87.5 bp. |
| S10-cp6-cp8-cpl10-A02 | AGREE | high | high (KEEP) | - | rerun | topics_supported '' known; report_view._cell raised 'Text is displayed from non-empty text alone'. |
| S10-cp6-cp8-cpl10-A03 | AGREE | medium | medium (KEEP) | - | rerun | 'High' from 'Highly uncertain' accepted; invented prior confidence published. |
| S10-cp6-cp8-cpl10-A04 | AGREE | medium | medium (KEEP) | - | rerun | USD/EUR quarters subtracted, change 0 USD, Stable; claim-level prose check refuses later with a misleading cause. |
| S10-cp6-cp8-cpl10-A05 | AGREE | medium | medium (KEEP) | - | rerun | Registry title 'Prior/current deliverable comparison' runs decision_ledger (prior_case). Root cause partly in owner_workflow.py registry (S02). |
| S10-cp6-cp8-cpl10-C01 | AGREE | high | medium (LOWER: same defect as A04; settlement's claim prose check still refuses Material/Watch topics, so it mostly fails closed) | S10-cp6-cp8-cpl10-A04 | rerun | from/to EUR, change USD in one TL10.2 row with no UpstreamError. |
| S10-cp6-cp8-cpl10-C02 | AGREE | medium | medium (KEEP) | S07-cp2-gh-A02 | rerun | 'We recommend a covenant reset at 5.2x' accepted as limitation, refused as rationale. |
| S10-cp6-cp8-cpl10-C03 | AGREE | medium | medium (KEEP) | - | rerun | Em-dash text refused with a false 'does not occur in the quote'. |
| S10-cp6-cp8-cpl10-C04 | AGREE | low | low (KEEP) | S06-cp2-ade-C03 | rerun | Claim limitation keeps raw {T4.10.ebitda.fy2025\|US$ m}. |
| S10-cp6-cp8-cpl10-C05 | AGREE | low | low (KEEP) | S07-cp2-gh-C01 | rerun | validate_committee 2x per _validate_step. |
| S10-cp6-cp8-cpl10-C06 | AGREE | low | low (KEEP) | S07-cp2-gh-C03 | code-read | Three _bound copies; copy-paste helper theme. |
| S11-earnings-financial-A01 | AGREE | high | high (KEEP) | - | rerun | Annual IS columns mapped to q4-2024 verified: True under a dated header. |
| S11-earnings-financial-A02 | AGREE | high | high (KEEP) | - | rerun | Three 'except per share ...' phrasings give THOUSANDS/MILLIONS to share rows; correct UNITS refused, wrong THOUSANDS composed. |
| S11-earnings-financial-A03 | AGREE | high | high (KEEP) | S11-earnings-financial-C02 | rerun | '(250 )' and U+2212 rows unchanged by respace and absent from line_table. |
| S11-earnings-financial-A04 | AGREE | high | high (KEEP) | - | rerun | fy-2024->fy-2025, q1->q2 and q1-2024->q1-2025 all REFUSED incompatible_periods; earnings.py:350 exact-days check confirmed. |
| S11-earnings-financial-A05 | AGREE | medium | medium (KEEP) | - | rerun | Missing optional id -> ValueError; declared windows-1252 -> UnicodeDecodeError out of parse. |
| S11-earnings-financial-A06 | AGREE | low | low (KEEP) | - | rerun | '(in millions of US$)' verifies against a EUR book. |
| S11-earnings-financial-C01 | AGREE | high | high (KEEP) | - | rerun | YTD or LTM T4.14 period -> ValueError 'Unsupported historical chart period type'. |
| S11-earnings-financial-C02 | AGREE | high | high (KEEP) | S11-earnings-financial-A03 | rerun | €/£ lines not respaced; only 'Cost of sales' survives. |
| S11-earnings-financial-C03 | AGREE | medium | medium (KEEP) | S11-earnings-financial-C01 | rerun | 'Incomplete same-date facility snapshot alias' raised. |
| S11-earnings-financial-C04 | AGREE | medium | medium (KEEP) | S11-earnings-financial-C01 | rerun | Trailing four quarters across FY boundary raise. |
| S11-earnings-financial-C05 | AGREE | medium | medium (KEEP) | - | rerun | 750 != 50 with outflow_magnitude investing/financing rows; unit_check_failed. |
| S11-earnings-financial-C06 | AGREE | medium | medium (KEEP) | - | rerun | -10 -> -5 gives growth -0.5 known. |
| S11-earnings-financial-C07 | AGREE | medium | low (LOWER: usually fails closed; a wrong binding needs a book period ending on the 20th) | - | rerun | 'June 2024  June 2023' -> June 20 dates. |
| S11-earnings-financial-C08 | AGREE | low | low (KEEP) | S11-earnings-financial-C01 | rerun | EUR book raises 'Unsupported chart currency, unit or perimeter'. |
| S11-earnings-financial-C09 | AGREE | low | low (KEEP) | - | rerun | _page_units called 5x per source per inputs(). |
| S11-earnings-financial-C10 | AGREE | low | low (KEEP) | - | code-read | Every is_year branch returns before pdf_headers.py:287; residue/full assigned then overwritten. |
| S12-vii-financial-engine-A01 | AGREE | critical | critical (KEEP) | - | rerun | Q2 24 closing_cash 20 Calculated (hand: 520), opening_cash 0 (hand: 500); statement_history.py:233 uses _Series('flow') for all T4.5 items. |
| S12-vii-financial-engine-A02 | AGREE | high | critical (RAISE: deterministic sign flip of a correctly recorded signed inflow on an outflow account, no model error needed, silent in FFO/LTM) | - | rerun | source 15 normalized -15 'negative absolute source amount'; reconciliation term -15. |
| S12-vii-financial-engine-A03 | AGREE | medium | medium (KEEP) | - | rerun | Decimal('1234') exponent 0 -> tolerance 0.5, difference -0.4 PASS. |
| S12-vii-financial-engine-A04 | AGREE | medium | medium (KEEP) | S12-vii-financial-engine-C04 | rerun | Minus-signed rows absent from data and omitted lists. |
| S12-vii-financial-engine-A05 | AGREE | medium | medium (KEEP) | - | rerun | '1.234' parsed as Decimal('1.234') unflagged; reachability needs a European-format source. |
| S12-vii-financial-engine-A06 | AGREE | low | low (KEEP) | - | code-read | distressed_figures.py:93-100 groups DR.2 rows by point.category; report_view.py:461 enforces cell count. Plausible, low. |
| S12-vii-financial-engine-C01 | AGREE | high | high (KEEP) | - | rerun | DEBT_TOTAL_EX_LEASES BLOCK with tl-b 'Not supplied' while adapter gives tl-b 0 at 2025-06-30. |
| S12-vii-financial-engine-C02 | AGREE | medium | low (LOWER: no production caller passes exclude_unrealised=True (cp1_workflow.py:145 default); latent) | - | rerun | NOT_STATED placeholder rows exclude a REALIZED add-back under the house variant. |
| S12-vii-financial-engine-C03 | AGREE | medium | medium (KEEP) | - | rerun | gross_profit/ebit note None after 'sign normalised' cogs; COMPONENT_MISSING reason lost. |
| S12-vii-financial-engine-C04 | AGREE | medium | medium (KEEP) | S12-vii-financial-engine-A04 | rerun | '-120 -80' row missing from both lists; last-column sign decides omitted listing. |
| S12-vii-financial-engine-C05 | AGREE | low | low (KEEP) | - | rerun | PF column: opening 100 + non_cash 5 vs closing 175; pro_forma_column has no callers. |
| S12-vii-financial-engine-C06 | AGREE | low | low (KEEP) | - | report-only | 8.4 s timing not rerun; per-call effective_accounts rebuild confirmed in code. |
| S12-vii-financial-engine-C07 | AGREE | low | low (KEEP) | S13-vii-canonical-context-C11 | code-read | model_report calls kernel_registers directly and via historical_report (financial_periods.py:327). |
| S12-vii-financial-engine-C08 | AGREE | low | low (KEEP) | - | code-read | Four 'toordinal() > 1' sites; _SCALE_FACTORS duplicates STATEMENT_UNIT_FACTORS. |
| S13-vii-canonical-context-A01 | AGREE | high | high (KEEP) | S13-vii-canonical-context-C02 | rerun | BLOCK with all inputs present downgraded to WARN 'Absent input ... Expense presentation is unknown'. |
| S13-vii-canonical-context-A02 | AGREE | high | high (KEEP) | S13-vii-canonical-context-C03 | rerun | 4 supportive dims + unlabelled recap -> composite 1 Low with high_action True. |
| S13-vii-canonical-context-A03 | AGREE | medium | high (RAISE: a 12.50x covenant recorded as 2.50x through cp4_legal is a wrong covenant result on a realistic model error, same class as S09-A02/A03) | S16-research-tools-A01 | rerun | '2.50:1.00' quoted in '12.50:1.00' True; parse_threshold gives 2.50 multiple. |
| S13-vii-canonical-context-A04 | AGREE | medium | medium (KEEP) | - | rerun | '3 of 4 quarters', 'seven times', '2024 basis points' pass prose.check. |
| S13-vii-canonical-context-A05 | AGREE | medium | medium (KEEP) | - | rerun | 'FY2025 revenue reached {rev-fy2023}' renders 812 US$ m, fact period FY2023. |
| S13-vii-canonical-context-A06 | AGREE | medium | medium (KEEP) | S13-vii-canonical-context-C04 | rerun | statement adjusted_ebitda 45 vs canonical None COMPONENT_MISSING 'derived from components'. |
| S13-vii-canonical-context-A07 | AGREE | low | low (KEEP) | - | code-read | narrative.py:233-235 grants scope on any KPI amount; _kpi_rows emits _SCALARS rows (:329). |
| S13-vii-canonical-context-A08 | AGREE | low | low (KEEP) | - | rerun | Percent-formatted %NAV cash read as 0.025; no production consumer. |
| S13-vii-canonical-context-A09 | AGREE | low | low (KEEP) | - | rerun | Hidden row/sheet read, negative pct_nav accepted. |
| S13-vii-canonical-context-C01 | AGREE | high | critical (RAISE: deterministic wrong period label (quarter dates) on every quarter-column trailing ratio in T4.9/T4.10, a final-deliverable period identity error) | - | rerun | value 5, display_basis is quarter basis True, operands basis rolling True. |
| S13-vii-canonical-context-C02 | AGREE | medium | high (RAISE: same defect as A01 (structural BLOCK hidden as WARN absent input)) | S13-vii-canonical-context-A01 | rerun | Both blockers -> WARN with sum 110 vs reported 150 hidden. |
| S13-vii-canonical-context-C03 | AGREE | medium | high (RAISE: same defect as A02 (risk level High->Low on more favourable evidence)) | S13-vii-canonical-context-A02 | rerun | 4 supportive dims -> 1 Low high_action True. |
| S13-vii-canonical-context-C04 | AGREE | medium | medium (KEEP) | S13-vii-canonical-context-A06 | rerun | canonical None COMPONENT_MISSING vs model 45. |
| S13-vii-canonical-context-C05 | AGREE | medium | high (RAISE: same defect as A03) | S13-vii-canonical-context-A03 | rerun | Three substring cases True. |
| S13-vii-canonical-context-C06 | AGREE | low | medium (RAISE: wrong period role for every Q4 = FY - 9M and Q2 = H1 - Q1 construction in a deliverable register) | - | rerun | Q4 24 row lists same-year 9M YTD under Prior-Year Stub. |
| S13-vii-canonical-context-C07 | AGREE | low | medium (RAISE: same defect as A04) | S13-vii-canonical-context-A04 | rerun | '3 of 4 quarters' and '2024 basis points' pass; '5x' flagged. |
| S13-vii-canonical-context-C08 | AGREE | low | low (KEEP) | - | rerun | '[UK]' -> Unresolved reference; 'Acme [Holdings Ltd' makes Claim raise. |
| S13-vii-canonical-context-C09 | AGREE | low | low (KEEP) | - | rerun | T4.12 rows: 2, second self-referential. |
| S13-vii-canonical-context-C10 | AGREE | low | low (KEEP) | - | rerun | evidenced-row issue raised: False for Insufficient Information with no citations. |
| S13-vii-canonical-context-C11 | AGREE | low | low (KEEP) | - | code-read | canonical_gaps.py:426 kernel_registers plus canonical_kpis/reconcile_periods each via historical_report. |
| S14-vii-live-runtime-A01 | AGREE | medium | medium (KEEP) | - | rerun | 8000 terms: 44.9 s, result bytes equal to query bytes; linear in term count. |
| S14-vii-live-runtime-A02 | AGREE | low | low (KEEP) | - | rerun | 5-line read 5,000,599 bytes; 6-line 36 KB read refused. |
| S14-vii-live-runtime-C01 | AGREE | medium | medium (KEEP) | - | rerun | After A->B->A pack revert every head stale and begin refused; replace_pack has no production caller (medium is right). |
| S14-vii-live-runtime-C02 | AGREE | low | low (KEEP) | - | rerun | label_candidates line_no 4/5 for row 104; production path rebases, so low. |
| S14-vii-live-runtime-C03 | AGREE | low | low (KEEP) | - | rerun | Longest issue 2,000,078 chars vs 600 cap elsewhere. |
| S14-vii-live-runtime-C04 | AGREE | low | low (KEEP) | - | code-read | prompts.py:1197 rule 2 names only SOURCE blocks; REPAIR block (:1229) has no data rule. |
| S14-vii-live-runtime-C05 | AGREE | low | low (KEEP) | S07-cp2-gh-C01 | rerun | rules() called 2x per submit. |
| S14-vii-live-runtime-C06 | AGREE | low | low (KEEP) | - | rerun | pack 4, cp3_upstream 3 per dispatch. |
| S15-vii-readiness-bindings-A01 | AGREE | medium | medium (KEEP) | - | code-read | Fuzz artifacts gone (crash_error.xlsx missing); preparation.py:452-462 except tuple confirmed to omit zlib.error/RuntimeError/LimitReachedError. |
| S15-vii-readiness-bindings-A02 | AGREE | medium | medium (KEEP) | - | rerun | Unavailable computation tagged {'computation'}; calculation_register satisfied. |
| S15-vii-readiness-bindings-A03 | AGREE | low | low (KEEP) | - | rerun | 'page:7 is missing', 'Pages 3 and 4', 'pp. 3-5' -> () ; 'pages 3-5' -> ((3,5),). |
| S15-vii-readiness-bindings-C01 | AGREE | medium | medium (KEEP) | - | rerun | Both true absence claims flagged as contradicting coverage. |
| S15-vii-readiness-bindings-C02 | AGREE | medium | medium (KEEP) | - | rerun | [1,'x'] min_length 3: real too_short suppressed. |
| S15-vii-readiness-bindings-C03 | AGREE | low | low (KEEP) | - | rerun | 0 -> amount '-0' value_class source; display '-0'. |
| S15-vii-readiness-bindings-C04 | AGREE | low | low (KEEP) | - | rerun | Cell without r -> unreadable blocked KeyError('r'). |
| S15-vii-readiness-bindings-C05 | AGREE | low | low (KEEP) | S04-delivery-A05 | rerun | Form feed shifts 'Net debt 42' to line:3; same splitlines root cause as S04-A05. |
| S15-vii-readiness-bindings-C06 | AGREE | low | low (KEEP) | - | rerun | Empty Notes sheet 'retained', no empty limitation. |
| S15-vii-readiness-bindings-C07 | AGREE | low | low (KEEP) | - | rerun | 300 citations over 50,000 spans: 0.83 s. |
| S16-research-tools-A01 | AGREE | high | high (KEEP) | - | rerun | '20', '0.0', '2025', '-12' quoted from '...: 200.0' all compose as known TDR.6 amounts. |
| S16-research-tools-A02 | AGREE | high | high (KEEP) | - | rerun | Three-months EUR-thousands span declared USD millions: issues [], fact 200.0 MILLIONS USD 'Twelve months to'. |
| S16-research-tools-A03 | AGREE | medium | medium (KEEP) | S16-research-tools-C04 | rerun | UnicodeEncodeError escapes fetch for 'www..example.com' and a 64-char label (unshare -n). |
| S16-research-tools-A04 | AGREE | low | low (KEEP) | S16-research-tools-C07 | rerun | 'Reuters' vs 'Reuters '/'reuters' count as independent. |
| S16-research-tools-A05 | AGREE | low | low (KEEP) | S16-research-tools-C09 | rerun | Claim id 'total' emitted as a total row; validate_tables ok. |
| S16-research-tools-A06 | AGREE | low | low (KEEP) | S16-research-tools-C08 | rerun | NUL path -> raw ValueError (via c_intake_review). |
| S16-research-tools-C01 | AGREE | high | high (KEEP) | S16-research-tools-A01 | rerun | '20', '0.0', '00' -> known amounts; peers.py:295 reads amount from the quote. |
| S16-research-tools-C02 | AGREE | high | high (KEEP) | S16-research-tools-A02 | rerun | unit=thousands currency=EUR over a USD-millions span: issues (), 200.0 THOUSANDS EUR. |
| S16-research-tools-C03 | AGREE | medium | medium (KEEP) | - | rerun | 'USD\|x' passes review then PackUnusable for the whole pack; 'USD ' silently drops the peer. |
| S16-research-tools-C04 | AGREE | medium | medium (KEEP) | S16-research-tools-A03 | rerun | check_url accepts 'www..example.com'; fetch RAISED UnicodeEncodeError. |
| S16-research-tools-C05 | AGREE | low | medium (RAISE: look-ahead evidence (body published after the cutoff) admitted into a historical run breaks period integrity) | - | rerun | Stale Last-Modified accepted with body 'Published: 2025-09-01' past cutoff; today-dated header over-refuses. |
| S16-research-tools-C06 | AGREE | low | low (KEEP) | S16-research-tools-A04 | rerun | Same bytes under two families pass as independent. |
| S16-research-tools-C07 | AGREE | low | low (KEEP) | S16-research-tools-A04 | rerun | 'Reuters'/'reuters' and 'Reuters ' -> []. |
| S16-research-tools-C08 | AGREE | low | low (KEEP) | S16-research-tools-A06 | rerun | RAW ValueError lstat: embedded null character. |
| S16-research-tools-C09 | AGREE | low | low (KEEP) | S16-research-tools-A05 | rerun | peer_id total -> total-styled TDR.4 row. |
| S16-research-tools-C10 | AGREE | low | low (KEEP) | - | rerun | Redirect to example.com:8443 followed; body taken as evidence. |
| S17-issuer-library-A01 | AGREE | medium | medium (KEEP) | - | rerun | Patched path: RuntimeError -> spent_usd 7.42; BrokenPipeError -> failed with no spent_usd, progress 0. |
| S17-issuer-library-A02 | AGREE | medium | medium (KEEP) | - | rerun | deliveries/link -> outside folder listed as acme-001/deliveries/link/CP-9.md; text leaked. |
| S17-issuer-library-A03 | AGREE | medium | medium (KEEP) | S17-issuer-library-C02 | rerun | Directory CP-notes.md -> rc 1 stdout empty; unlisted CP-2.md shown as Built from. |
| S17-issuer-library-A04 | AGREE | medium | medium (KEEP) | S17-issuer-library-C04 | rerun | CP-1x.md hides the whole run (IndexError). |
| S17-issuer-library-A05 | AGREE | medium | medium (KEEP) | - | code-read | screen.js:186 interpolates ${p.exact}/${p.label} without esc(); browser harness not rerun (needs Chromium), CSP limits to markup spoofing. |
| S17-issuer-library-A06 | AGREE | medium | medium (KEEP) | - | rerun | runs/frontier-2020 overwrites curated key silently; Ford Otosan view relabelled TransDigm Latest. |
| S17-issuer-library-A07 | AGREE | low | low (KEEP) | S17-issuer-library-C03 | code-read | views.js:121 data-evidence and routeHref (:206-212) unescaped; CSP blocks script, markup only. |
| S17-issuer-library-A08 | AGREE | low | low (KEEP) | - | rerun | Offline fake bundle keeps pypdf-OLD.dist-info and stale module. Cited lines 79-106 exceed the 74-line file (bundle is at :30-69). |
| S17-issuer-library-C01 | AGREE | medium | medium (KEEP) | - | rerun | CP-2-request.md listed as output; CP-2 default None in a retained run. |
| S17-issuer-library-C02 | AGREE | medium | medium (KEEP) | S17-issuer-library-A03 | rerun | workspace_store raised IsADirectoryError; good deliverable lost too. |
| S17-issuer-library-C03 | AGREE | medium | low (LOWER: markup-only injection under the app CSP from a hostile filename on a shared workspace; same root cause as A07) | S17-issuer-library-A07 | rerun | Rendered chart HTML breaks out of data-evidence attribute. |
| S17-issuer-library-C04 | AGREE | low | medium (RAISE: same defect as A04 (one odd filename hides every output of the run)) | S17-issuer-library-A04 | rerun | runs shown [] with IndexError issue. |
| S17-issuer-library-C05 | AGREE | low | low (KEEP) | - | rerun | BOM handoff -> 1 unstructured section, charts 0. |
| S17-issuer-library-C06 | AGREE | low | low (KEEP) | - | rerun | draft=1 with new-run hidden: confirm calls 0, reloads 1. |
| S17-issuer-library-C07 | AGREE | low | low (KEEP) | - | rerun | 'Not supplied: reported in EUR m' -> 'Not available'. |
| S17-issuer-library-C08 | AGREE | low | low (KEEP) | - | rerun | copilot True in the cleaned environment. |
| S17-issuer-library-C09 | AGREE | low | low (KEEP) | - | code-read | browser_check.py:355 ends in 'or True'. |
| S17-issuer-library-C10 | AGREE | low | low (KEEP) | - | code-read | --rb-ink-2 defined only in context-form.html; index.html loads screen.css alone. |
| S17-issuer-library-C11 | AGREE | low | low (KEEP) | - | rerun | 616 reads for 127 files, 11.1 MB vs 2.3 MB unique. |
| S17-issuer-library-C12 | AGREE | low | low (KEEP) | S17-issuer-library-A08 | rerun | Confirmed by A08's offline repro; cited lines 124-149 exceed the 74-line file. |
| S17-issuer-library-C13 | AGREE | low | low (KEEP) | - | rerun | c09_names_drift shows only runtime alias entries differ; hand-copied map confirmed. |
| S18-issuer-library-server-A01 | AGREE | high | high (KEEP) | S18-issuer-library-server-C01 | rerun | Real binary, 190 s fake review: curl (52) Empty reply, http=000, status.json reviewed, review.json present. |
| S18-issuer-library-server-A02 | AGREE | medium | medium (KEEP) | S18-issuer-library-server-C06 | rerun | turkish-I x6 inserted at 199 vs 205; U+023A x40 and invalid UTF-8 panic slice bounds. |
| S18-issuer-library-server-A03 | AGREE | medium | low (LOWER: reached only by hand-authored or legacy manifests (CP-OS writer emits metrics {}), no production writer) | - | rerun | All six fragment cases admitted (12.3 from (12.3), -12 from a date, 1.234 from 1.234,5). |
| S18-issuer-library-server-A04 | AGREE | medium | medium (KEEP) | S18-issuer-library-server-C05 | rerun | Newest running job absent from 30-row list. |
| S18-issuer-library-server-A05 | NEEDS-EVIDENCE | medium | medium (KEEP) | - | code-read | loadConfig reads and unmarshals with no owner/ACL check (settings.go:24-37), but ProgramData default ACL behaviour needs a Windows host; cited lines :316-338/:456 exceed the 79/62-line files. |
| S18-issuer-library-server-A06 | AGREE | low | medium (RAISE: same defect as C04: another issuer's delivery shown and counted as the run's verified deliverable (source identity)) | S18-issuer-library-server-C04 | rerun | run case-a shows delivery for run_id other-run / issuer ZZZ. |
| S18-issuer-library-server-A07 | AGREE | low | low (KEEP) | - | rerun | status after restart: running, activeJobs=0. |
| S18-issuer-library-server-A08 | AGREE | low | medium (RAISE: same defect as C02; a false 409 after a failed spawn hides the real state and orphans the reviewed run) | S18-issuer-library-server-C02 | rerun | first=503 then second=409 'already been started'. |
| S18-issuer-library-server-A09 | AGREE | low | low (KEEP) | - | rerun | BOM policy refused: invalid character 'ï'; cited settings.go:332 exceeds the 79-line file. |
| S18-issuer-library-server-C01 | AGREE | high | high (KEEP) | S18-issuer-library-server-A01 | rerun | Scaled test: client EOF, orphaned job reviewed, /api/runs/list []. |
| S18-issuer-library-server-C02 | AGREE | medium | medium (KEEP) | S18-issuer-library-server-A08 | rerun | 503 then 409 after repair; worker never ran. |
| S18-issuer-library-server-C03 | AGREE | medium | medium (KEEP) | - | code-read | server.go:58-62 gate is Host/Origin/Sec-Fetch-Site only; port derived from crc32 of state path (main.go:47). Design confirmed; cross-user exploit needs a shared host. |
| S18-issuer-library-server-C04 | AGREE | medium | medium (KEEP) | S18-issuer-library-server-A06 | rerun | Foreign delivery under runs/case-a/deliveries available=true issue ''. |
| S18-issuer-library-server-C05 | AGREE | medium | medium (KEEP) | S18-issuer-library-server-A04 | rerun | web-0aaa... running job absent from 30 rows. |
| S18-issuer-library-server-C06 | AGREE | medium | medium (KEEP) | S18-issuer-library-server-A02 | rerun | Injected before '</tr></tab' for Turkish dotted I; invalid UTF-8 past </body>. |
| S18-issuer-library-server-C07 | AGREE | low | low (KEEP) | - | rerun | /api/catalogue timed out while a stalled client held RLock during ServeContent. |
| S18-issuer-library-server-C08 | AGREE | low | low (KEEP) | - | rerun | settings 200 during review; start 409 'Review this run before starting'. |
| S18-issuer-library-server-C09 | AGREE | low | low (KEEP) | S18-issuer-library-server-C04 | rerun | Same folder listed as missing and available. |
| S18-issuer-library-server-C10 | AGREE | low | low (KEEP) | - | rerun | run() error logged nowhere; library.log empty. |
| S18-issuer-library-server-C11 | AGREE | low | low (KEEP) | - | rerun | refreshLocked held the write lock 890 ms with 4x60 MiB files. |
| S18-issuer-library-server-C12 | AGREE | low | low (KEEP) | - | code-read | jobs.go:298 io.ReadAll up to 64 MiB per part before write and hash. |

## Repro log (every critical and high finding, re-run by me)

All Python commands ran from `/home/user/final-workflow` with `.venv/bin/python`; `R` is the review root. Full outputs are in `R/fable/log/`.

```
# S04-delivery-A01
PYTHONPATH=src:. .venv/bin/python R/S04-delivery/t/attacks6.py
{'title': 'Financials and credit metrics', 'note': None, 'scale': None, ... 'columns': ('FY2023', 'FY2024')}
EUR thousands anywhere in financials block: False

# S04-delivery-C01
PYTHONPATH=src:. .venv/bin/python R/S04-delivery/cr/r01_dup_tabs.py
ValidationError 1 validation error for Block  Value error, Tab labels are distinct

# S05-cp0-cp1-A01
PYTHONPATH=src:.:tests .venv/bin/python R/S05-cp0-cp1/repro_cp1d_basis_unit.py
percent ACCEPTED: basis 2 MILLIONS USD | accepted 2 MILLIONS | fraction 0.666...
currency ACCEPTED: basis 1.50 MILLIONS USD ...   bps ACCEPTED: basis 1 MILLIONS USD ...

# S05-cp0-cp1-C01 (critical)
PYTHONPATH=src:.:tests .venv/bin/python R/S05-cp0-cp1/cr/cr_c_bridge_unit.py
forged basis line: 'Basis: FY2025 (January 1-December 31, 2025); EUR; amounts in thousands; ...'
fact: {'fact_id': 'T1D.1.a01.claimed', 'amount_exact': '3', 'unit': 'MILLIONS', 'currency': 'USD', 'status': 'known'}
limitations mention EUR/thousands: False

# S05-cp0-cp1-C02
PYTHONPATH=src:.:tests .venv/bin/python R/S05-cp0-cp1/cr/cr_c03_onestep_resume.py
journal after crash: attempt pending ['valid']
retry via cp1b.submit pattern RAISES: Submit the next module step in order

# S06-cp2-ade-A01
PYTHONPATH=src:.:tests .venv/bin/python R/S06-cp2-ade/repro/r01_cp2d_no_schedule.py
no T4.18 schedule ... maturity_refs= set()  issues: ('the maturity_wall assessment must cite T4.18 maturity_date',)

# S06-cp2-ade-A02 / A03 / A04
PYTHONPATH=src:.:tests .venv/bin/python R/S06-cp2-ade/repro/r02_cp2e_rows.py
(a2) issues: ()  T2F.1 Levered free cash flow [('2.25', 'FY 2025: 2025-01-01 to 2025-12-31'), ...]
(b)  issues: ()  interest operand: -5.00 ... shock 100 ... interest_after Value(state='known', amount=Decimal('-4.5'))
(c2) currency quote: 'Currency: USD; amounts in thousands.'  issues: ()  T2F.1 Total debt [('50.00', 'MILLIONS', Decimal('1000000')) ...]

# S06-cp2-ade-C01
PYTHONPATH=src:.:tests .venv/bin/python R/S06-cp2-ade/c01_interest_sign.py
interest token (45) cov_base not_applicable 'cash interest is negative'  shock 200 ... interest_after -39
outflow-presented interest (20), 1000bp: interest_after 10 | cov_after known 20

# S07-cp2-gh-A01
PYTHONPATH=src:.:tests .venv/bin/python R/S07-cp2-gh/repro/a01_metric_swap.py   (control: probe_cp2g.py)
issues: ()
b03 Total leverage watch level | metric: Interest coverage | level: 2.5 | ... down: Not reached by FY2028   (control: FY2026)

# S07-cp2-gh-A02
PYTHONPATH=src:.:tests .venv/bin/python R/S07-cp2-gh/repro/a06_limitation.py
issues: ()   [('T2H.3.revenue_growth', 'Management guided FY2026 EBITDA of 41.7 million; the probability-weighted ...'), ...]
as rationale: ('downside.rationale: Bare figure: 41.7', ...)

# S08-cp3-A01 / A02 / A03 / A05
PYTHONPATH=src:.:tests .venv/bin/python R/S08-cp3/repro_cp3d.py
A1 indicative/subject-to bid-offer accepted as observed: issues=[]  dm_mid 28.3 pd_mid 0.0368
A2 quote 7 years before run as-of: issues=[]  years 10.98 dm_mid 10.2
A3 quote one year after run as-of 2026-01-10: issues=[]  years 2.98 dm_mid 37.8
A4 bid quoted as yield 6.25% read as price: issues=[]  bid 0.0625 dm_bid 2356.7 pd_bid 0.9561
A4b bid quoted as 175 bps read as price: issues=[]  bid 1.75 dm_bid -1885.3
A5 other instrument's quotation bound to Northbridge Term Loan: issues=[]  mid 0.88875 dm_mid 279.7 pd_mid 0.3098

# S08-cp3-A04
PYTHONPATH=src:.:tests .venv/bin/python R/S08-cp3/repro_cp3d_units.py R/S08-cp3
A6 margin 3.25% read as 3.25 bp; SOFR 430 bps read as 430%: issues=[]   margin_bp 3.25 yield_mid 4.3032 dm_mid 31.5

# S08-cp3-A06 / A07
PYTHONPATH=src:.:tests .venv/bin/python R/S08-cp3/repro_cp3.py
A  as_of after run as-of: issues=[]  T3.3 m01 [..., 'Observed', 'Dealer quotation on January 9, 2026 ...', 'January 9, 2031']
A2 as_of not a date at all: issues=[]  T3.3 m01 [..., 'the close']
C  term-loan cites context rows c01/c02 that quote notes-2031: issues=[]  T3.1 i01 ... Market evidence context c01 (observed)

# S08-cp3-C01
PYTHONPATH=src:.:tests .venv/bin/python R/S08-cp3/cr_c01_eur_amort.py
EUR amortisation: ValueError CP-3C term-loan.annual_amortisation: currency 'EUR' is not 'USD'

# S08-cp3-C02
PYTHONPATH=src:.:tests .venv/bin/python R/S08-cp3/cr_c04_asof.py
'January 9, 2031' issues: () | T3.3 m01: ('Observed', 'January 9, 2031') | stale limitation: False   (same for 'the close', 'March 1, 2019')

# S09-cp4-cp5-A01
PYTHONPATH=src:.:tests .venv/bin/python R/S09-cp4-cp5/repro/a_cp5_copy_tables.py
identical value/unit/period: True True True
FINDING: figure_identity fact_id interface-fact:abc | differs in table_id, row_id, field between CP-1, CP-4   control (cp1_references): ()

# S09-cp4-cp5-A02 / A03
PYTHONPATH=src:.:tests .venv/bin/python R/S09-cp4-cp5/repro/b_cp4_threshold.py
A2 step-down ... threshold_text '4.00x': T4.9.r01.threshold = 4.00x  headroom = 3.00  Within threshold on the CP-1 metric
A3 document_id legal-covenants, threshold from legal-other: T4.9.r01.threshold = 6.00x  headroom = 5.00  Within threshold on the CP-1 metric

# S09-cp4-cp5-A04
PYTHONPATH=src:.:tests .venv/bin/python R/S09-cp4-cp5/repro/e_cp4c_failclosed_after_validation.py
content_issues (...): ()
compute raised ValueError: CP-4C: the CP-4 lender protection rating is 'Adequate'; ... fails closed (round 8 A-2 #4)

# S09-cp4-cp5-C01
PYTHONPATH=src:.:tests .venv/bin/python R/S09-cp4-cp5/cr/c01_t4f2_identity.py ; ... c01b_cp4c_refs_identity.py
figure_identity fact_id net_leverage_reported | differs in table_id, row_id between CP-1, CP-4
cp2g_references ... findings: 2 (T2H.4.b26.ebitda, T2H.4.d26.ebitda)   cp2a_references ... findings: 2

# S10-cp6-cp8-cpl10-A01
PYTHONPATH=src:.:tests .venv/bin/python R/S10-cp6-cp8-cpl10/scratch/cp8_labelled.py
issues with offer=98.00: ()   T7.3.loan_offer.realized_value 0.98   T7.4.loan_mid.realized 0.98   T7.4.loan_mid.magnitude 87.5

# S10-cp6-cp8-cpl10-A02
PYTHONPATH=src:.:tests .venv/bin/python R/S10-cp6-cp8-cpl10/scratch/cpl10_allmissing.py
issues: ()   topics_supported: '' known calculated
report_view._cell raised: ValueError Text is displayed from non-empty text alone

# S10-cp6-cp8-cpl10-C01
PYTHONPATH=src:.:tests .venv/bin/python R/S10-cp6-cp8-cpl10/cr/c_cpl10_ccy.py
TL10.2.cash.change (Decimal('3.75'), 'MILLIONS', 'USD')   TL10.2.cash.from_value (Decimal('16.25'), 'MILLIONS', 'EUR')

# S11-earnings-financial-A01
PYTHONPATH=src:.:tests .venv/bin/python R/S11-earnings-financial/repro/is_header_balance.py
mapped: (frozenset({'q4-2024', 'fy-2024'}), frozenset({'fy-2023'}))   model maps annual IS columns to q4-2024 / fy-2023 -> verified: True

# S11-earnings-financial-A02
PYTHONPATH=src:.:tests .venv/bin/python R/S11-earnings-financial/repro/header_scale.py ; ... share_scale_compose.py
BAD shares scale 'THOUSANDS'  expected 'UNITS'  (in thousands, except per share and share data)
model scale UNITS    : composed=0 left=['source_quantity_refused', ...]   model scale THOUSANDS: composed=2

# S11-earnings-financial-A03
PYTHONPATH=src:.:tests .venv/bin/python R/S11-earnings-financial/repro/html_rows.py
3 'Operating loss $ (250 ) $ (10 )' -> 'Operating loss $ (250 ) $ (10 )'   4 'Other expense −45 −30' -> unchanged
rows: 2 'Revenue' ... 5 'Net loss' ...   (rows 3 and 4 absent, no flag)

# S11-earnings-financial-A04
PYTHONPATH=src:.:tests .venv/bin/python R/S11-earnings-financial/repro/earnings_leap.py
fy-2024 fy-2025 REFUSED incompatible_periods   q1-2025 q2-2025 REFUSED incompatible_periods   q1-2024 q1-2025 REFUSED incompatible_periods

# S11-earnings-financial-C01
PYTHONPATH=src:.:tests .venv/bin/python R/S11-earnings-financial/c01_series.py
plus YTD six-month period 2025-01-01..2025-06-30 -> RAISES ValueError Unsupported historical chart period type
plus LTM period ending 2025-09-30 -> RAISES ValueError Unsupported historical chart period type

# S11-earnings-financial-C02
PYTHONPATH=src:.:tests .venv/bin/python R/S11-earnings-financial/c04_euro_lines.py
€ line_table rows: [('Cost of sales', (Decimal('-800'), Decimal('-700')))]   DVII on pre-spaced euro lines: ['Revenue', 'Operating profit']

# S12-vii-financial-engine-A01 (critical)
PYTHONPATH=src:.:tests .venv/bin/python R/S12-vii-financial-engine/repro/cfs_closing_cash_history.py
('Q2 24', 'QUARTER') opening_cash 0 Calculated calculated
('Q2 24', 'QUARTER') closing_cash 20 Calculated calculated        (hand values: 500 and 520)

# S12-vii-financial-engine-A02
PYTHONPATH=src:.:tests .venv/bin/python R/S12-vii-financial-engine/repro/signed_refund_flip.py
statement_output: source 15 normalized -15 negative absolute source amount
reconciliation term: original 15 amount -15

# S12-vii-financial-engine-C01
PYTHONPATH=src:.:tests .venv/bin/python R/S12-vii-financial-engine/c_repro/c02_issued_on.py
financial_reconciliation DEBT_TOTAL_EX_LEASES at 2025-06-30: BLOCK None [('tl-a', 100, None), ('tl-b', None, 'Not supplied')]
adapter facility rows at 2025-06-30: [('tl-a', 100), ('tl-b', 0)]

# S13-vii-canonical-context-A01
PYTHONPATH=src:.:tests .venv/bin/python R/S13-vii-canonical-context/work/absent_input.py
status BLOCK difference None explanation Expense presentation is unknown   all inputs present: True
limitation -> 'Absent input, stated as a limitation on a public filed pack (rulings item 82): Expense presentation is unknown'   severity -> WARN

# S13-vii-canonical-context-A02
PYTHONPATH=src:.:tests .venv/bin/python R/S13-vii-canonical-context/work/governance_score.py
3 supportive dims + recap (no dimension): composite=Not Scorable level=High high_action=True
4 supportive dims + recap (no dimension): composite=1 level=Low high_action=True

# S13-vii-canonical-context-C01
PYTHONPATH=src:tests:. .venv/bin/python R/S13-vii-canonical-context/cr/c_ltm_basis.py
value: 5   display_basis is quarter basis: True   operands basis is rolling: True

# S16-research-tools-A01
PYTHONPATH=src:.:tests:tests/research .venv/bin/python R/S16-research-tools/scripts/peer_quote_substring.py
quote='20'   issues=[] status=known amount=20 unit=MILLIONS period='Twelve months to 2025-12-31'
quote='2025' issues=[] status=known amount=2025 ...   quote='-12' issues=[] status=known amount=-12 ...

# S16-research-tools-A02
PYTHONPATH=src:.:tests:tests/research .venv/bin/python R/S16-research-tools/scripts/peer_unit_period.py
issues: []   fact: 200.0 MILLIONS USD 1000000 'Twelve months to 2025-12-31'

# S16-research-tools-C01 / C02
PYTHONPATH=src:.:tests:tests/research .venv/bin/python R/S16-research-tools/cr/c_peer_quote.py
quote='20': issues=() -> amount=20 status=known   quote='0.0': issues=() -> amount=0.0 status=known
unit=thousands currency=EUR: issues= () -> 200.0 THOUSANDS EUR Twelve months to 2025-12-31

# S18-issuer-library-server-A01 (real binary, fake bridge sleeping 190 s, loopback port 51888)
cd R/S18-issuer-library-server/scratch && bash run_timeout.sh
curl: (52) Empty reply from server   http=000 bytes=0   curl exit=52 elapsed=190s
ws/intake/web-96599a.../status.json: {"state": "reviewed", "message": "Reviewed; no model call has been made.", ...}

# S18-issuer-library-server-C01
cd R/S18-issuer-library-server/cr-gocopy && GOTOOLCHAIN=auto go test -count=1 -run TestCR_WriteTimeoutLosesSlowReview -v .
client error: Post ".../api/runs/review": EOF   orphaned job web-80f3... status={"state": "reviewed", ...}   /api/runs/list = []
--- PASS: TestCR_WriteTimeoutLosesSlowReview (2.05s)
```

Medium/low reruns (not listed line by line; outputs in `R/fable/log/`): S01 (`c04`, `a04`, `a06`, `a07`, the four `c_tests`), S02 (all a0x/c0x), S03 (repro + cr), S04 (`attacks1/3/5`, `r02`-`r11`), S05 (all remaining), S06 (`r03`, `r05`, `r06`, `c02`-`c04`), S07 (all), S08 (all), S09 (all), S10 (all), S11 (`ixbrl`, `c03`-`c09`), S12 (all), S13 (all), S14 (`tools_attack`, `c01`-`c06`), S15 (`repro_unavailable_computation`, `absent_page_ranges`, `c_*`), S16 (all, `idna_crash` under `unshare -n`), S17 (all, four adversarial scripts re-pathed into `R/fable/s17/`), S18 (`TestAttack*` in gocopy: 7 of 8 fail as designed; `TestCR_*` in cr-gocopy: 10 pass as designed).


## Duplicate groups

Each group is one root cause (or one shared pattern); the first id is the one I would keep as the lead finding. Severity after my review is the group's.

**Cross-section groups**

1. **Substring quote matching accepts fragments of numbers** (`deploy_vii/quotes.py quoted`): S16-research-tools-A01, S16-research-tools-C01, S13-vii-canonical-context-A03, S13-vii-canonical-context-C05 — high. (S18-issuer-library-server-A03's Go `numericToken` is the same idea in a different codebase; listed separately, low.)
2. **Unit / currency / scale of a cited amount is stamped from a default or model text and never checked against the source**: S05-cp0-cp1-C01 (lead, critical), S05-cp0-cp1-A01, S06-cp2-ade-A04, S08-cp3-A03, S08-cp3-A04, S16-research-tools-A02, S16-research-tools-C02 — a pattern, not one code path; each needs its own fix.
3. **`str.splitlines()` used for `line:N` locators** (breaks on U+2028, form feed and friends): S04-delivery-A05, S15-vii-readiness-bindings-C05 — low.
4. **`Claim.limitation` stored with raw `{ref|unit}` tokens while the cell is spelled**: S06-cp2-ade-C03, S10-cp6-cp8-cpl10-C04 — low.
5. **Dead CP-OS Markdown transport** (`cpos_handoffs.transport()` only called from a test; also broken via `claim.plain`, CLAIMS addendum): S01-orchestration-C06, S02-module-framework-A03 (DISAGREE: no trigger) — low.
6. **Repeated validation/composition per submit** (validate -> report -> compute each re-validates): S07-cp2-gh-C01 (lead), S07-cp2-gh-C02, S05-cp0-cp1-C08, S06-cp2-ade-C06, S08-cp3-C10, S09-cp4-cp5-C06, S10-cp6-cp8-cpl10-C05, S14-vii-live-runtime-C05 — low efficiency.
7. **Copy-pasted owner helpers** (`_stale_issues`, `_run_text_issues`, `_bound`, one-step submit body): S07-cp2-gh-C03 (lead), S06-cp2-ade-C05, S10-cp6-cp8-cpl10-C06, S05-cp0-cp1-C09 — low.
8. **Bare-figure guard bypass in model prose** (`prose.bare_figures` ignores number words, "N of M", years): S13-vii-canonical-context-A04 (lead), S13-vii-canonical-context-C07, S09-cp4-cp5-A06 — medium.
9. **Model-written limitation text validated only for blankness**: S07-cp2-gh-A02 (lead, high), S10-cp6-cp8-cpl10-C02 — same hole in two owners.
10. **Kernel registers rebuilt several times per build**: S13-vii-canonical-context-C11, S12-vii-financial-engine-C07 — low.
11. **CP-8 comparison integrity**: S01-orchestration-A03 (same/swapped bundles accepted) plus CLAIMS #2 (no code-level diff in `comparison_files`, reported only as an S10 out-of-scope line and not indexed) — medium; worth one lead finding.

**Within-section pairs (adversarial / code-review found the same defect)**

12. S01-A01 / S01-C03 — HTML filing pinned under `<name>.jsonl` key collision (medium).
13. S01-A02 / S01-C02 — non-atomic `_put`, torn response accepted on resume (medium).
14. S02-A01 / S02-C03 — CP-0 attachment gap matched by bare word / substring (medium).
15. S02-A02 / S02-C04 — fence lookalike check misses non-NFKD confusables (low).
16. S03-A04 / S03-C03 — Copilot session.error paths unscrubbed, `_paths_in` prefix bug (low).
17. S03-C02 / S03-C06 — Copilot refusal reply-kind drift and its design cause (medium/low).
18. S04-A02 / S04-C09 — fixed display decimals for token-sourced cells (medium).
19. S05-A02 / S05-C04 — T1C.6 tie-out ignores the peer line's period (medium).
20. S05-A05 / S05-C03 — envelope hashes compared with themselves, forged QA accepted (medium).
21. S05-C02 / S05-C09 — one-step submit cannot resume, copied in three owners (medium/low).
22. S06-A03 / S06-C01 — CP-2E parenthesised interest read negative (high).
23. S07-C01 / S07-C02 — CP-2G/CP-2H repeated validation (low; also group 6).
24. S08-A01 / S08-C07 — CP-3D indicative/conditional quote used for DM/PD (high).
25. S08-A05 / S08-C06 — CP-3D sheet quotation date not compared with run as-of (high).
26. S08-A06 / S08-C02 — CP-3 `as_of` is unchecked model text (high).
27. S08-A07 / S08-C04 — CP-3 context row of another facility accepted as basis (high).
28. S08-A09 / S08-C05 / S08-C08 — CP-3C negates cash interest without a sign check; negative EBITDA cover (medium/low).
29. S09-A01 / S09-C01 — CP-5 `REFERENCE_TABLES` exempts only `cp1_references` (high).
30. S09-A04 / S09-C02 / S09-C03 — CP-4C positional CP-4 reads raise inside the validator after the paid response (high).
31. S10-A04 / S10-C01 — CP-L10 USD `Upstream` never checks operand currency (medium).
32. S11-A03 / S11-C02 — `respace` knows only `$` and plain parentheses; rows dropped silently (high).
33. S11-C01 / S11-C03 / S11-C04 / S11-C08 — `financial_series` raises instead of returning an unsupported reason; report render fails (high).
34. S12-A04 / S12-C04 — `statement_extract` drops minus-signed rows from both data and `omitted` (medium).
35. S13-A01 / S13-C02 — structural BLOCK downgraded to WARN "Absent input" (high).
36. S13-A02 / S13-C03 — governance adverse-action override lost with 4+ scored dimensions (high).
37. S13-A06 / S13-C04 — canonical adjusted EBITDA sums NOT_SOURCED add-back cells (medium).
38. S16-A03 / S16-C04 — IDNA `UnicodeEncodeError` escapes `fetch` (medium); S16-A04 / S16-C07 / S16-C06 — family independence by raw label or duplicate bytes (low); S16-A05 / S16-C09 — `total` row id (low); S16-A06 / S16-C08 — NUL path (low).
39. S17-A03 / S17-C02 — `built_from` outside the fail-open try (medium); S17-A04 / S17-C04 — `output_label` crash hides the run (medium); S17-A07 / S17-C03 — unescaped output id in attributes (low); S17-A08 / S17-C12 — stale wheels kept in the bundle (low).
40. S18-A01 / S18-C01 — WriteTimeout 180 s shorter than the 10-minute review (high).
41. S18-A02 / S18-C06 — `</body>` offset from `bytes.ToLower` (medium); S18-A04 / S18-C05 — run list is name order, not recency (medium); S18-A06 / S18-C04 / S18-C09 — run-internal delivery identity unchecked and duplicated (medium); S18-A08 / S18-C02 — `start.claim` survives a failed spawn (medium).
42. S09-A02 / S09-A03 — threshold text accepted from any quote / any step of a schedule (high): two symptoms of `_threshold_issues` checking only `threshold_text in quotes`.


## Disagreements

**S02-module-framework-A03 (low, PLAUSIBLE) — DISAGREE.** The finding says the O1/O2 prompt rules do not cover the CP-OS handoff message that `cpos_handoffs.prompt_messages` appends. That message is only appended while `cpos_handoffs.ACTIVE` is set, and `transport()` is called nowhere outside `tests/test_cpos_app.py:375` (I re-grepped `src`, `apps`, `tests`, `workflow.py`), so no production module ever receives it; CLAIMS #1 confirms upstream handoffs reach modules through `HandoffTask.handoffs` and `model/handoff.py:414-416` instead. There is no reachable trigger; the real finding is the dead and broken transport path, already recorded as S01-orchestration-C06.

**S07-cp2-gh-A05 (medium) — DISAGREE.** The behaviour reproduces exactly as described (EBITDA 0 with debt 50 gives leverage breaks "Not calculable"; zero interest gives coverage breaks "Not calculable"), but it is the rule the independent oracle specifies (`cases/cp2g-owner/builder/build.py` NC_E/NC_I/NC_D and `first_result`, pinned by the G-8 tests) and it follows the project's "missing is never 0" invariant for an undefined ratio. Whether a certain-direction breach should be settled from the signs before dividing is a methodology ruling to raise with the user, not a code defect; the code-review pass of the same section reached the same conclusion. I would carry it to the final report as an open ruling question, not as a finding to fix.

**NEEDS-EVIDENCE (two findings).** S03-model-provider-C01: the adapter side is reproduced with the fake client (an announced tool call that reaches no handler ends as IdleTimeout or UnparsableReply), but whether the real Copilot runtime goes quiet or answers the tool error itself for a tool it was not offered cannot be settled offline; a recorded runtime event sequence is needed. S18-issuer-library-server-A05: `loadConfig` indeed trusts any file at the ProgramData policy path with no owner or ACL check (`settings.go:24-37`, not the cited `:316-338`), but whether a standard user can create that folder on a managed Windows host depends on the host's ProgramData ACLs, which cannot be tested here.
