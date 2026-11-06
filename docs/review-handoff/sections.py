import json, subprocess, sys
from pathlib import Path
W = "src/deploy_workflow/"; O = W + "owners/"; V = "src/deploy_vii/"; A = "apps/issuer-library/"
S = {
 "S01-orchestration": ("CP-OS orchestration, launch, CPDR, run pathway, run inputs, replay, host, context input",
   [O+f for f in ["cpos.py","cpos_launch.py","cpdr.py"]] + [W+f for f in ["run_pathway.py","run_inputs.py","workflow.py","replay.py","cpos_handoffs.py","cpos_status.py","run_scopes.py","platform_io.py","identity_check.py","host.py","context.py","context_cites.py","context_periods.py","__init__.py"]] + ["workflow.py"]),
 "S02-module-framework": ("Module (owner) framework, owner rendering, shared bases, prompt composition",
   [W+"owner_workflow.py", W+"owner_rendering.py"] + [O+f for f in ["pins.py","valuation_basis.py","period_basis.py","blank.py","cp0_attachments.py","__init__.py"]] + ["src/deploy_workflow/prompts/"]),
 "S03-model-provider": ("Model provider layer (providers, loop, Copilot adapter, budget, pricing, record, redact, transport) and model-testing harness",
   ["src/deploy_workflow/model/", "src/deploy_workflow/model_testing/"]),
 "S04-delivery": ("Separate delivery process: Markdown/handoff adapters, report view, renderers, charts, browser assets",
   [W+f for f in ["markdown_delivery.py","handoff_delivery.py","model_handoff_delivery.py","rendering.py","financial_rendering.py","reader_summary.py"]] + [V+f for f in ["report_view.py","render.py","delivery.py","cp1_render.py","charts.py","display.py","interface_view.py","register_view.py","statement_view.py","table_markdown.py"]] + ["src/deploy_vii/assets/"]),
 "S05-cp0-cp1": ("CP-0 and CP-1 family analytical modules",
   [O+f for f in ["cp1a.py","cp1b.py","cp1c.py","cp1d.py"]] + [V+f for f in ["cp0_workflow.py","cp1_workflow.py","cp1_quality.py"]]),
 "S06-cp2-ade": ("CP-2, CP-2A, CP-2D, CP-2E analytical modules and CP-2 synthesis",
   [O+f for f in ["cp2.py","cp2a.py","cp2d.py","cp2e.py"]] + [V+"cp2_synthesis.py"]),
 "S07-cp2-gh": ("CP-2G and CP-2H analytical modules", [O+"cp2g.py", O+"cp2h.py"]),
 "S08-cp3": ("CP-3, CP-3C, CP-3D relative value modules, RV quotes input",
   [O+f for f in ["cp3.py","cp3c.py","cp3d.py"]] + [V+"cp3_relative_value.py", V+"inputs/rv_quotes.py"]),
 "S09-cp4-cp5": ("CP-4/CP-4C legal and CP-5 integrity modules",
   [O+f for f in ["cp4.py","cp4c.py","cp5.py"]] + [V+"cp4_legal.py", V+"cp5_integrity.py"]),
 "S10-cp6-cp8-cpl10": ("CP-6 committee, CP-8 run comparison, CP-L10 modules",
   [O+f for f in ["cp6.py","cp8.py","cpl10.py"]] + [V+"cp6_committee.py"]),
 "S11-earnings-financial": ("Earnings and financial statement workflows, statement composition, series, unit maps, PDF/XBRL/HTML text parsing",
   [W+f for f in ["earnings_workflow.py","earnings.py","financial_workflow.py","statement_compose.py","financial_series.py","restructuring_series.py","liquidity_series.py","statement_lines.py","unit_maps.py","pdf_headers.py","inline_xbrl.py","html_text.py"]]),
 "S12-vii-financial-engine": ("deploy_vii financial calculation engine: model package, financial/period reconciliation, statements, cash bridge, FX, distressed figures",
   ["src/deploy_vii/model/"] + [V+f for f in ["financial_reconciliation.py","period_reconciliation.py","financial_periods.py","financial_model.py","financial_adapter.py","financial_validation.py","financial_contracts.py","statement_extract.py","statement_validation.py","statement_history.py","statement_output.py","cash_bridge.py","balance_movement.py","expense_composition.py","facility_fx.py","distressed_figures.py","calculation_trace.py","audit_basis.py"]]),
 "S13-vii-canonical-context": ("deploy_vii canonical tables/audit/gaps/KPIs, quotes, portfolio input, business/source context, narrative and prose",
   [V+f for f in ["canonical_tables.py","canonical_audit.py","canonical_gaps.py","canonical_kpis.py","quotes.py","inputs/portfolio.py","inputs/__init__.py","business_context.py","source_context.py","narrative.py","narrative_projection.py","prose.py","quality.py","__init__.py"]]),
 "S14-vii-live-runtime": ("deploy_vii live runtime: live tools, submission, prompts, schema, settings, execution, envelope",
   ["src/deploy_vii/live/", V+"execution.py", V+"envelope.py"]),
 "S15-vii-readiness-bindings": ("deploy_vii readiness, preparation, registry, contracts, model interface, bindings",
   [V+f for f in ["readiness.py","downstream_readiness.py","model_readiness.py","preparation.py","registry.py","contracts.py","model_interface.py","cp_model_workflow.py","context_binding.py"]] + ["src/deploy_vii/bindings/"]),
 "S16-research-tools": ("Research (webfetch, intake, peers, tables, evidence, dossier) and source/upstream tools",
   ["src/deploy_workflow/research/", "src/deploy_workflow/tools/"]),
 "S17-issuer-library": ("Issuer Library app: engine store/bridge, web UI, packaging, designs, validation",
   [A]),
}
exts = (".py",".js",".html",".css",".ps1",".sh",".bat")
def expand(p):
    P = Path(p)
    if P.is_dir(): return sorted(str(x) for x in P.rglob("*") if x.is_file() and x.suffix in exts and "__pycache__" not in x.parts)
    assert P.exists(), p
    return [p]
allf = set(subprocess.check_output("find src apps -type f \\( -name '*.py' -o -name '*.js' -o -name '*.html' -o -name '*.css' -o -name '*.ps1' -o -name '*.sh' -o -name '*.bat' \\) -not -path '*/__pycache__/*'", shell=True, text=True).split()) | {"workflow.py"}
seen = {}; out = {}
for k,(d,ps) in S.items():
    fs = [f for p in ps for f in expand(p)]
    for f in fs:
        if f in seen: print("DUP", f, seen[f], k)
        seen[f] = k
    n = sum(len(Path(f).read_text(errors="ignore").splitlines()) for f in fs)
    out[k] = {"title": d, "paths": ps, "files": fs, "lines": n}
    print(f"{k:28} {n:6} lines {len(fs):3} files  {d}")
print("UNASSIGNED:", sorted(allf - set(seen)))
json.dump(out, open(sys.argv[1], "w"), indent=1)
