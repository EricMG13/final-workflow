# Review sections — final-workflow @ a313b50

18 sections, 132,602 source lines. Every Python, JS, HTML, CSS, PowerShell and Go source file in `src/`, `apps/` and root `workflow.py` is in exactly one section (S18 added after the first pass found the Go server). Tests are context, not review scope.

| Section | Lines | Files | Scope |
|---|---:|---:|---|
| S01-orchestration | 8,740 | 18 | CP-OS orchestration, launch, CPDR, run pathway, run inputs, replay, host, context input |
| S02-module-framework | 8,294 | 19 | Module (owner) framework, owner rendering, shared bases, prompt composition |
| S03-model-provider | 10,300 | 27 | Model provider layer (providers, loop, Copilot adapter, budget, pricing, record, redact, transport) and model-testing harness |
| S04-delivery | 9,304 | 20 | Separate delivery process: Markdown/handoff adapters, report view, renderers, charts, browser assets |
| S05-cp0-cp1 | 7,578 | 7 | CP-0 and CP-1 family analytical modules |
| S06-cp2-ade | 8,088 | 5 | CP-2, CP-2A, CP-2D, CP-2E analytical modules and CP-2 synthesis |
| S07-cp2-gh | 6,151 | 2 | CP-2G and CP-2H analytical modules |
| S08-cp3 | 8,202 | 5 | CP-3, CP-3C, CP-3D relative value modules, RV quotes input |
| S09-cp4-cp5 | 6,770 | 5 | CP-4/CP-4C legal and CP-5 integrity modules |
| S10-cp6-cp8-cpl10 | 5,702 | 4 | CP-6 committee, CP-8 run comparison, CP-L10 modules |
| S11-earnings-financial | 10,817 | 12 | Earnings and financial statement workflows, statement composition, series, unit maps, PDF/XBRL/HTML text parsing |
| S12-vii-financial-engine | 8,752 | 28 | deploy_vii financial calculation engine: model package, financial/period reconciliation, statements, cash bridge, FX, distressed figures |
| S13-vii-canonical-context | 8,274 | 14 | deploy_vii canonical tables/audit/gaps/KPIs, quotes, portfolio input, business/source context, narrative and prose |
| S14-vii-live-runtime | 7,382 | 9 | deploy_vii live runtime: live tools, submission, prompts, schema, settings, execution, envelope |
| S15-vii-readiness-bindings | 5,418 | 34 | deploy_vii readiness, preparation, registry, contracts, model interface, bindings |
| S16-research-tools | 5,703 | 15 | Research (webfetch, intake, peers, tables, evidence, dossier) and source/upstream tools |
| S17-issuer-library | 5,434 | 24 | Issuer Library app: engine store/bridge, web UI, packaging, designs, validation |
| S18-issuer-library-server | 1,693 | 9 | Issuer Library Go server: HTTP server and CSP, request guards, jobs, discovery, settings, platform |

## S01-orchestration — CP-OS orchestration, launch, CPDR, run pathway, run inputs, replay, host, context input

- `src/deploy_workflow/owners/cpos.py`
- `src/deploy_workflow/owners/cpos_launch.py`
- `src/deploy_workflow/owners/cpdr.py`
- `src/deploy_workflow/run_pathway.py`
- `src/deploy_workflow/run_inputs.py`
- `src/deploy_workflow/workflow.py`
- `src/deploy_workflow/replay.py`
- `src/deploy_workflow/cpos_handoffs.py`
- `src/deploy_workflow/cpos_status.py`
- `src/deploy_workflow/run_scopes.py`
- `src/deploy_workflow/platform_io.py`
- `src/deploy_workflow/identity_check.py`
- `src/deploy_workflow/host.py`
- `src/deploy_workflow/context.py`
- `src/deploy_workflow/context_cites.py`
- `src/deploy_workflow/context_periods.py`
- `src/deploy_workflow/__init__.py`
- `workflow.py`

## S02-module-framework — Module (owner) framework, owner rendering, shared bases, prompt composition

- `src/deploy_workflow/owner_workflow.py`
- `src/deploy_workflow/owner_rendering.py`
- `src/deploy_workflow/owners/pins.py`
- `src/deploy_workflow/owners/valuation_basis.py`
- `src/deploy_workflow/owners/period_basis.py`
- `src/deploy_workflow/owners/blank.py`
- `src/deploy_workflow/owners/cp0_attachments.py`
- `src/deploy_workflow/owners/__init__.py`
- `src/deploy_workflow/prompts/__init__.py`
- `src/deploy_workflow/prompts/absence_rule.py`
- `src/deploy_workflow/prompts/compose.py`
- `src/deploy_workflow/prompts/coverage_rule.py`
- `src/deploy_workflow/prompts/digest.py`
- `src/deploy_workflow/prompts/factory.py`
- `src/deploy_workflow/prompts/fence.py`
- `src/deploy_workflow/prompts/g8.py`
- `src/deploy_workflow/prompts/p5.py`
- `src/deploy_workflow/prompts/rules.py`
- `src/deploy_workflow/prompts/tools.py`

## S03-model-provider — Model provider layer (providers, loop, Copilot adapter, budget, pricing, record, redact, transport) and model-testing harness

- `src/deploy_workflow/model/__init__.py`
- `src/deploy_workflow/model/adapter.py`
- `src/deploy_workflow/model/budget.py`
- `src/deploy_workflow/model/copilot.py`
- `src/deploy_workflow/model/copilot_adapter.py`
- `src/deploy_workflow/model/handoff.py`
- `src/deploy_workflow/model/loop.py`
- `src/deploy_workflow/model/pricing.py`
- `src/deploy_workflow/model/providers.py`
- `src/deploy_workflow/model/record.py`
- `src/deploy_workflow/model/redact.py`
- `src/deploy_workflow/model/reply_classes.py`
- `src/deploy_workflow/model/transport.py`
- `src/deploy_workflow/model/turn.py`
- `src/deploy_workflow/model_testing/__init__.py`
- `src/deploy_workflow/model_testing/__main__.py`
- `src/deploy_workflow/model_testing/budget.py`
- `src/deploy_workflow/model_testing/cases.py`
- `src/deploy_workflow/model_testing/configs.py`
- `src/deploy_workflow/model_testing/faults.py`
- `src/deploy_workflow/model_testing/mapping.py`
- `src/deploy_workflow/model_testing/pathway.py`
- `src/deploy_workflow/model_testing/records.py`
- `src/deploy_workflow/model_testing/report.py`
- `src/deploy_workflow/model_testing/run.py`
- `src/deploy_workflow/model_testing/scoring.py`
- `src/deploy_workflow/model_testing/slice_budget.py`

## S04-delivery — Separate delivery process: Markdown/handoff adapters, report view, renderers, charts, browser assets

- `src/deploy_workflow/markdown_delivery.py`
- `src/deploy_workflow/handoff_delivery.py`
- `src/deploy_workflow/model_handoff_delivery.py`
- `src/deploy_workflow/rendering.py`
- `src/deploy_workflow/financial_rendering.py`
- `src/deploy_workflow/reader_summary.py`
- `src/deploy_vii/report_view.py`
- `src/deploy_vii/render.py`
- `src/deploy_vii/delivery.py`
- `src/deploy_vii/cp1_render.py`
- `src/deploy_vii/charts.py`
- `src/deploy_vii/display.py`
- `src/deploy_vii/interface_view.py`
- `src/deploy_vii/register_view.py`
- `src/deploy_vii/statement_view.py`
- `src/deploy_vii/table_markdown.py`
- `src/deploy_vii/assets/app.css`
- `src/deploy_vii/assets/app.js`
- `src/deploy_vii/assets/shell.html`
- `src/deploy_vii/assets/tokens.css`

## S05-cp0-cp1 — CP-0 and CP-1 family analytical modules

- `src/deploy_workflow/owners/cp1a.py`
- `src/deploy_workflow/owners/cp1b.py`
- `src/deploy_workflow/owners/cp1c.py`
- `src/deploy_workflow/owners/cp1d.py`
- `src/deploy_vii/cp0_workflow.py`
- `src/deploy_vii/cp1_workflow.py`
- `src/deploy_vii/cp1_quality.py`

## S06-cp2-ade — CP-2, CP-2A, CP-2D, CP-2E analytical modules and CP-2 synthesis

- `src/deploy_workflow/owners/cp2.py`
- `src/deploy_workflow/owners/cp2a.py`
- `src/deploy_workflow/owners/cp2d.py`
- `src/deploy_workflow/owners/cp2e.py`
- `src/deploy_vii/cp2_synthesis.py`

## S07-cp2-gh — CP-2G and CP-2H analytical modules

- `src/deploy_workflow/owners/cp2g.py`
- `src/deploy_workflow/owners/cp2h.py`

## S08-cp3 — CP-3, CP-3C, CP-3D relative value modules, RV quotes input

- `src/deploy_workflow/owners/cp3.py`
- `src/deploy_workflow/owners/cp3c.py`
- `src/deploy_workflow/owners/cp3d.py`
- `src/deploy_vii/cp3_relative_value.py`
- `src/deploy_vii/inputs/rv_quotes.py`

## S09-cp4-cp5 — CP-4/CP-4C legal and CP-5 integrity modules

- `src/deploy_workflow/owners/cp4.py`
- `src/deploy_workflow/owners/cp4c.py`
- `src/deploy_workflow/owners/cp5.py`
- `src/deploy_vii/cp4_legal.py`
- `src/deploy_vii/cp5_integrity.py`

## S10-cp6-cp8-cpl10 — CP-6 committee, CP-8 run comparison, CP-L10 modules

- `src/deploy_workflow/owners/cp6.py`
- `src/deploy_workflow/owners/cp8.py`
- `src/deploy_workflow/owners/cpl10.py`
- `src/deploy_vii/cp6_committee.py`

## S11-earnings-financial — Earnings and financial statement workflows, statement composition, series, unit maps, PDF/XBRL/HTML text parsing

- `src/deploy_workflow/earnings_workflow.py`
- `src/deploy_workflow/earnings.py`
- `src/deploy_workflow/financial_workflow.py`
- `src/deploy_workflow/statement_compose.py`
- `src/deploy_workflow/financial_series.py`
- `src/deploy_workflow/restructuring_series.py`
- `src/deploy_workflow/liquidity_series.py`
- `src/deploy_workflow/statement_lines.py`
- `src/deploy_workflow/unit_maps.py`
- `src/deploy_workflow/pdf_headers.py`
- `src/deploy_workflow/inline_xbrl.py`
- `src/deploy_workflow/html_text.py`

## S12-vii-financial-engine — deploy_vii financial calculation engine: model package, financial/period reconciliation, statements, cash bridge, FX, distressed figures

- `src/deploy_vii/model/__init__.py`
- `src/deploy_vii/model/_cells.py`
- `src/deploy_vii/model/dates.py`
- `src/deploy_vii/model/debt.py`
- `src/deploy_vii/model/frame.py`
- `src/deploy_vii/model/history.py`
- `src/deploy_vii/model/metrics.py`
- `src/deploy_vii/model/periods.py`
- `src/deploy_vii/model/registers.py`
- `src/deploy_vii/model/statements.py`
- `src/deploy_vii/financial_reconciliation.py`
- `src/deploy_vii/period_reconciliation.py`
- `src/deploy_vii/financial_periods.py`
- `src/deploy_vii/financial_model.py`
- `src/deploy_vii/financial_adapter.py`
- `src/deploy_vii/financial_validation.py`
- `src/deploy_vii/financial_contracts.py`
- `src/deploy_vii/statement_extract.py`
- `src/deploy_vii/statement_validation.py`
- `src/deploy_vii/statement_history.py`
- `src/deploy_vii/statement_output.py`
- `src/deploy_vii/cash_bridge.py`
- `src/deploy_vii/balance_movement.py`
- `src/deploy_vii/expense_composition.py`
- `src/deploy_vii/facility_fx.py`
- `src/deploy_vii/distressed_figures.py`
- `src/deploy_vii/calculation_trace.py`
- `src/deploy_vii/audit_basis.py`

## S13-vii-canonical-context — deploy_vii canonical tables/audit/gaps/KPIs, quotes, portfolio input, business/source context, narrative and prose

- `src/deploy_vii/canonical_tables.py`
- `src/deploy_vii/canonical_audit.py`
- `src/deploy_vii/canonical_gaps.py`
- `src/deploy_vii/canonical_kpis.py`
- `src/deploy_vii/quotes.py`
- `src/deploy_vii/inputs/portfolio.py`
- `src/deploy_vii/inputs/__init__.py`
- `src/deploy_vii/business_context.py`
- `src/deploy_vii/source_context.py`
- `src/deploy_vii/narrative.py`
- `src/deploy_vii/narrative_projection.py`
- `src/deploy_vii/prose.py`
- `src/deploy_vii/quality.py`
- `src/deploy_vii/__init__.py`

## S14-vii-live-runtime — deploy_vii live runtime: live tools, submission, prompts, schema, settings, execution, envelope

- `src/deploy_vii/live/__init__.py`
- `src/deploy_vii/live/context.py`
- `src/deploy_vii/live/prompts.py`
- `src/deploy_vii/live/schema.py`
- `src/deploy_vii/live/settings.py`
- `src/deploy_vii/live/submission.py`
- `src/deploy_vii/live/tools.py`
- `src/deploy_vii/execution.py`
- `src/deploy_vii/envelope.py`

## S15-vii-readiness-bindings — deploy_vii readiness, preparation, registry, contracts, model interface, bindings

- `src/deploy_vii/readiness.py`
- `src/deploy_vii/downstream_readiness.py`
- `src/deploy_vii/model_readiness.py`
- `src/deploy_vii/preparation.py`
- `src/deploy_vii/registry.py`
- `src/deploy_vii/contracts.py`
- `src/deploy_vii/model_interface.py`
- `src/deploy_vii/cp_model_workflow.py`
- `src/deploy_vii/context_binding.py`
- `src/deploy_vii/bindings/__init__.py`
- `src/deploy_vii/bindings/cp0.py`
- `src/deploy_vii/bindings/cp1.py`
- `src/deploy_vii/bindings/cp1a.py`
- `src/deploy_vii/bindings/cp1b.py`
- `src/deploy_vii/bindings/cp1c.py`
- `src/deploy_vii/bindings/cp1d.py`
- `src/deploy_vii/bindings/cp2.py`
- `src/deploy_vii/bindings/cp2a.py`
- `src/deploy_vii/bindings/cp2d.py`
- `src/deploy_vii/bindings/cp2e.py`
- `src/deploy_vii/bindings/cp2g.py`
- `src/deploy_vii/bindings/cp2h.py`
- `src/deploy_vii/bindings/cp3.py`
- `src/deploy_vii/bindings/cp3c.py`
- `src/deploy_vii/bindings/cp3d.py`
- `src/deploy_vii/bindings/cp4.py`
- `src/deploy_vii/bindings/cp4c.py`
- `src/deploy_vii/bindings/cp5.py`
- `src/deploy_vii/bindings/cp6.py`
- `src/deploy_vii/bindings/cp8.py`
- `src/deploy_vii/bindings/cp_model.py`
- `src/deploy_vii/bindings/cpdr.py`
- `src/deploy_vii/bindings/cpl10.py`
- `src/deploy_vii/bindings/shipped.py`

## S16-research-tools — Research (webfetch, intake, peers, tables, evidence, dossier) and source/upstream tools

- `src/deploy_workflow/research/__init__.py`
- `src/deploy_workflow/research/anchors.py`
- `src/deploy_workflow/research/brief.py`
- `src/deploy_workflow/research/contracts.py`
- `src/deploy_workflow/research/dossier.py`
- `src/deploy_workflow/research/evidence.py`
- `src/deploy_workflow/research/intake.py`
- `src/deploy_workflow/research/peers.py`
- `src/deploy_workflow/research/review.py`
- `src/deploy_workflow/research/steps.py`
- `src/deploy_workflow/research/tables.py`
- `src/deploy_workflow/research/webfetch.py`
- `src/deploy_workflow/tools/__init__.py`
- `src/deploy_workflow/tools/source.py`
- `src/deploy_workflow/tools/upstream.py`

## S17-issuer-library — Issuer Library app: engine store/bridge, web UI, packaging, designs, validation

- `apps/issuer-library/designs/browser_check.py`
- `apps/issuer-library/designs/build.py`
- `apps/issuer-library/designs/fake_engine/bridge.py`
- `apps/issuer-library/designs/fake_engine/store.py`
- `apps/issuer-library/engine/bridge.py`
- `apps/issuer-library/engine/store.py`
- `apps/issuer-library/packaging/Smoke-test.ps1`
- `apps/issuer-library/packaging/build.py`
- `apps/issuer-library/packaging/runtime.py`
- `apps/issuer-library/packaging/smoke_test.py`
- `apps/issuer-library/packaging/sync_assets.py`
- `apps/issuer-library/validate.py`
- `apps/issuer-library/web/actions.js`
- `apps/issuer-library/web/boot.js`
- `apps/issuer-library/web/brand.css`
- `apps/issuer-library/web/context-embed.css`
- `apps/issuer-library/web/context-embed.js`
- `apps/issuer-library/web/context-form.html`
- `apps/issuer-library/web/index.html`
- `apps/issuer-library/web/report-adapter.css`
- `apps/issuer-library/web/report-adapter.js`
- `apps/issuer-library/web/screen.css`
- `apps/issuer-library/web/screen.js`
- `apps/issuer-library/web/views.js`

## S18-issuer-library-server — Issuer Library Go server: HTTP server and CSP, request guards, jobs, discovery, settings, platform

- `apps/issuer-library/discovery.go`
- `apps/issuer-library/jobs.go`
- `apps/issuer-library/main.go`
- `apps/issuer-library/model.go`
- `apps/issuer-library/platform_other.go`
- `apps/issuer-library/platform_windows.go`
- `apps/issuer-library/server.go`
- `apps/issuer-library/settings.go`
- `apps/issuer-library/go.mod`
