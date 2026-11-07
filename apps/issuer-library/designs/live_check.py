"""Paid walk through the app: TDG, the real engine, a spend cap. Run explicitly; never by a gate.

    <playwright python> live_check.py --cap USD [--config sol-medium] [--modules "CP-1 CP-1A"]
        [--minutes 60] [--out DIR] [--rehearse]

Needs FW_PYTHON and ISSUER_LIBRARY_BINARY. --rehearse serves the fake engine (no provider, no
key) through the same walk and skips the flow and evidence checks, saying so in its scope.
Provider keys reach only the server process's environment.
"""

import argparse
import importlib
import json
import math
import os
import re
import runpy
import subprocess
import sys
import tempfile
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

import flow_check
from faults import redact

HERE = Path(__file__).resolve().parent
R = HERE.parents[2]
PORT = 53920
KEYS = tuple(runpy.run_path(str(R / "src/deploy_workflow/model/redact.py"))["KEY_ENV_NAMES"])
SOURCES = R / "data/public-corpus/v1/TDG"
CONTEXT = R / "runs/cpos-launch-live-002/context.json"
CASE = "TDG as of 2024-09-30"
LITERALS = ("7,940", "6,261")  # filed net sales and cash, USD millions (10-K, 2024-09-30)
REHEARSAL = "rehearsal: fake engine, no provider called; flow and evidence checks skipped"


class Refusal(Exception):
    pass


def live_evidence(run: Path, cap: Decimal, status_spent: str, modules: set[str]) -> list[str]:
    """Faults in the retained provider calls (rules of test_cpos_launch.assert_live_evidence)."""
    rows = [json.loads(n) for n in (run / "live/calls.jsonl").read_text().splitlines() if n]
    found = [f"call {i}: no request_id" for i, r in enumerate(rows) if not r.get("request_id")]
    found += [
        f"call {i}: reported {r.get('reported_model')} != requested {r.get('requested_model')}"
        for i, r in enumerate(rows)
        if r.get("reported_model") != r.get("requested_model")
    ]
    seen = {r["module_id"] for r in rows}
    if seen != modules:
        found.append(f"modules called {sorted(seen)} != accepted {sorted(modules)}")
    charged = sum((Decimal(str(r["settled_usd"])) for r in rows), Decimal(0))
    if not 0 < charged:
        found.append(f"settled spend {charged} is not above zero")
    if charged > cap:
        found.append(f"settled spend {charged} exceeds cap {cap}")
    try:
        if Decimal(status_spent) != charged:
            found.append(f"status spend {status_spent} != settled sum {charged}")
    except InvalidOperation:
        found.append(f"status spend {status_spent!r} is not a number")
    if "CP-1" in modules:
        cp1 = (run / "CP-1.md").read_text()
        found += [f"CP-1 handoff lacks filed value {lit}" for lit in LITERALS if lit not in cp1]
    return found


def parse(argv: list[str]) -> argparse.Namespace:
    class One(argparse.ArgumentParser):
        def error(self, message: str) -> Any:
            raise Refusal(message.splitlines()[0])

    p = One(add_help=False)
    p.add_argument("--cap")
    p.add_argument("--config", default="sol-medium")
    p.add_argument("--modules", default="CP-1 CP-1A")
    p.add_argument("--minutes", type=float, default=60)
    p.add_argument("--out")
    p.add_argument("--rehearse", action="store_true")
    args = p.parse_args(argv)
    try:
        cap = Decimal(args.cap) if args.cap is not None else None
    except InvalidOperation:
        cap = None
    if cap is None or not cap.is_finite() or cap <= 0:
        raise Refusal("--cap USD is required and must be a finite number above zero")
    if not args.rehearse and not any(os.environ.get(k) for k in KEYS):
        raise Refusal(f"no provider key in the environment (one of {', '.join(KEYS)})")
    for name in ("FW_PYTHON", "ISSUER_LIBRARY_BINARY"):
        if not os.environ.get(name):
            raise Refusal(f"{name} is not set")
    if not Path(os.environ["ISSUER_LIBRARY_BINARY"]).is_file():
        raise Refusal("ISSUER_LIBRARY_BINARY is not a file")
    if not (math.isfinite(args.minutes) and args.minutes > 0):
        raise Refusal("--minutes must be above zero")
    args.cap = cap
    return args


def built_count(text: str) -> int:
    match = re.search(r"Built from (\d+) handoffs", text)
    return int(match.group(1)) if match else -1


def walk(bc: Any, page: Any, args: argparse.Namespace, ws: Path, summary: dict[str, Any]) -> None:
    note = bc.note
    fill_form(page, args)
    page.check("#run-confirm")
    if page.is_disabled("#start-run"):
        note(False, "Start stays disabled after review (provider not configured?); no spend")
        return
    page.click("#start-run")  # the one paid step; never retried
    page.wait_for_selector("#progress-step:not([hidden])")
    page.wait_for_selector("#open-run:not([hidden])", timeout=int(args.minutes * 60000))
    check_run(bc, page, args, ws, summary)


def fill_form(page: Any, args: argparse.Namespace) -> None:
    expect = importlib.import_module("playwright.sync_api").expect
    page.goto(f"http://127.0.0.1:{PORT}/")
    page.wait_for_selector("#library-new-run", timeout=30000)
    page.click("#library-new-run")
    frame = page.frame_locator("#context-editor")
    frame.locator("#load").wait_for(state="attached", timeout=15000)
    frame.locator("#load").set_input_files(str(CONTEXT))
    expect(page.locator("#context-readiness")).to_contain_text(
        "Required fields complete", timeout=15000
    )
    page.click("#use-context")
    page.wait_for_selector("#source-step:not([hidden])")
    page.set_input_files("#run-sources", str(SOURCES))
    expect(page.locator("#upload-list")).to_contain_text(f"{len(list(SOURCES.iterdir()))} files")
    page.select_option("#run-model", args.config)
    page.fill("#run-budget", str(args.cap))
    page.locator("details.run-advanced summary").click()
    page.fill("#run-modules", args.modules)
    page.click("#review-run")
    page.wait_for_selector("#review-step:not([hidden])", timeout=120000)


def check_run(
    bc: Any, page: Any, args: argparse.Namespace, ws: Path, summary: dict[str, Any]
) -> None:
    note = bc.note
    status = page.inner_text("#run-progress")
    note(status.startswith("complete"), f"run finished: {status[:120]}")
    shown_spend = page.inner_text("#run-spend")
    page.click("#open-run")
    page.wait_for_selector(".report-built .report-row a", timeout=30000)
    page.click(".report-built .report-row a >> nth=0")
    report = page.frame_locator("#report-preview")
    report.locator("#view-root").wait_for(state="attached", timeout=30000)
    run = max((ws / "runs").glob("web-*"))
    summary["run_id"] = run.name
    state = json.loads(next((ws / "intake").glob("*/status.json")).read_text())
    summary["spent_usd"] = state.get("spent_usd")
    summary["report"] = str(next(run.glob("deliveries/*/report.html"), ""))
    note(
        shown_spend == f"Recorded spend: USD {state.get('spent_usd')}",
        f"app spend {shown_spend!r} equals status.json {state.get('spent_usd')!r}",
    )
    accepted = {p.stem for p in run.glob("CP-*.md")}
    built = page.locator(".built-from summary", has_text="Built from").first.inner_text()
    note(built_count(built) == len(accepted), f"{built!r} matches {len(accepted)} accepted modules")
    if args.rehearse:
        return
    shown = report.locator("#view-root").evaluate(
        "el => { const c = el.cloneNode(true); c.querySelectorAll('svg').forEach(n => n.remove());"
        " return c.textContent; }"
    )
    handoffs = [p.read_text() for p in sorted(run.glob("deliveries/*/CP-*.md"))]
    problems = flow_check.run_faults(run, SOURCES) + flow_check.report_faults(shown, handoffs)
    problems += live_evidence(run, args.cap, str(state.get("spent_usd")), accepted)
    problems += [f"report lacks filed value {n}" for n in LITERALS if n not in shown]
    wanted = set(args.modules.split()) - accepted
    problems += [f"requested module {m} not accepted" for m in sorted(wanted)]
    for problem in problems:
        note(False, f"live check: {problem}", kind="flow")
    note(not problems, "flow, evidence and filed-value checks")


def run_walk(bc: Any, args: argparse.Namespace, out: Path, summary: dict[str, Any]) -> None:
    sync_playwright = importlib.import_module("playwright.sync_api").sync_playwright
    ws = out / "ws"
    ws.mkdir()
    engine = HERE / "fake_engine" if args.rehearse else R / "apps/issuer-library/engine"
    servers: list[subprocess.Popen[bytes]] = []
    try:
        servers.append(
            bc.serve(
                ws,
                PORT,
                engine,
                key="not-a-real-key" if args.rehearse else None,
                keep_keys=not args.rehearse,
            )
        )
        with sync_playwright() as driver:
            browser = bc.SignedBrowser(driver.chromium.launch())
            try:
                page = browser.new_page(viewport={"width": 1366, "height": 768})
                bc.errors_of(page)
                bc.attempt("live", browser, lambda: walk(bc, page, args, ws, summary))
            finally:
                browser.close()
    finally:
        for server in servers:
            server.terminate()
        for server in servers:
            try:
                server.wait(timeout=15)
            except subprocess.TimeoutExpired:
                server.kill()
                server.wait()


def main(argv: list[str]) -> int:
    try:
        args = parse(argv)
    except Refusal as refusal:
        print(f"live_check: {refusal}", file=sys.stderr)
        return 2
    import browser_check as bc  # imports Playwright; after the refusals

    out = Path(args.out) if args.out else Path(tempfile.mkdtemp(prefix="issuer-library-live-"))
    out.mkdir(parents=True, exist_ok=True)
    bc.S, bc.PY, bc.APP = out, os.environ["FW_PYTHON"], os.environ["ISSUER_LIBRARY_BINARY"]
    mode = "REHEARSAL (fake engine, no provider)" if args.rehearse else "PAID RUN"
    print(
        f"{mode}: config={args.config}, modules={args.modules} (dependencies added by the "
        f"launcher), cap=USD {args.cap}, case={CASE}, workspace={out / 'ws'}",
        flush=True,
    )
    summary: dict[str, Any] = {"run_id": None, "spent_usd": None, "report": None}
    try:
        run_walk(bc, args, out, summary)
    except KeyboardInterrupt:
        bc.FAULTS.add("live", "interrupted", "interrupted by the operator; spend may be above zero")
    except (Exception, SystemExit) as error:  # noqa: BLE001 - recorded as a fault, never silent
        bc.FAULTS.add("live", "exception", f"{type(error).__name__}: {str(error)[:600]}")
    finally:
        bc.scan_server_logs()
        passed = sum(ok for ok, _ in bc.results)
        scope = (
            REHEARSAL
            if args.rehearse
            else f"live provider: {args.config}, {CASE}, modules {args.modules}, "
            f"spend USD {summary['spent_usd']}"
        )
        secrets = bc.secrets()
        bc.FAULTS.write(out / "faults.json", scope, passed, secrets)
        summary |= {"scope": scope, "failed": len(bc.FAULTS.items)}
        text = redact(json.dumps(summary, indent=2, default=str), secrets) + "\n"
        (out / "summary.json").write_text(text)
        print(f"{passed} passed, {len(bc.FAULTS.items)} faults: {out / 'faults.json'}")
    return int(bool(bc.FAULTS.items) or passed != len(bc.results))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
