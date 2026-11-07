"""Paid walk through the app: TDG, the real engine, a spend cap. Run explicitly; never by a gate.

    <playwright python> live_check.py --cap USD [--config sol-medium] [--modules "CP-1 CP-1A"]
        [--minutes 60] [--out DIR] [--rehearse]

Needs FW_PYTHON and ISSUER_LIBRARY_BINARY. --rehearse serves the fake engine (no provider, no
key) through the same walk and skips the flow and evidence checks, saying so in its scope.
Provider keys are popped from this process's environment at start and passed only to the server
process (which runs in its own process group, stopped on every exit path).
"""

import argparse
import hashlib
import importlib
import importlib.util
import json
import math
import os
import re
import runpy
import signal
import subprocess
import sys
import tempfile
import threading
import time
from contextlib import suppress
from decimal import Decimal, InvalidOperation
from pathlib import Path
from typing import Any

import flow_check
from faults import redact

HERE = Path(__file__).resolve().parent
R = HERE.parents[2]
PORT = 53920
KEYS = tuple(runpy.run_path(str(R / "src/deploy_workflow/model/redact.py"))["KEY_ENV_NAMES"])
# The adapter's KEY_VARIABLES values (a test pins it); GitHub tokens are not provider keys.
PROVIDER_KEYS = (
    "OPENAI_API_KEY",
    "ANTHROPIC_API_KEY",
    "OPENROUTER_API_KEY",
    "COPILOT_GITHUB_TOKEN",
)
SOURCES = R / "data/public-corpus/v1/TDG"
CONTEXT = R / "runs/cpos-launch-live-002/context.json"
CASE = "TDG as of 2024-09-30"
LITERALS = ("7,940", "6,261")  # filed net sales and cash, USD millions (10-K, 2024-09-30)
REHEARSAL = "rehearsal: fake engine, no provider called; flow and evidence checks skipped"
KEY_CONFIG, KEY_REQUESTED = "sol-medium", {"CP-1", "CP-1A"}  # the case the answer key checks
KEY_MODULES = {"CP-0", "CP-1", "CP-1A"}  # ... and what the launcher runs for it
# Run by `sh -c ... PGID` in its own session, with stdin a pipe only live_check holds: EOF means
# live_check is gone (any signal, a crash), so it stops the server's group. See arm_watchdog.
WATCHDOG = 'read _; kill -TERM -- "-$0"; sleep 15; kill -KILL -- "-$0"'
HALTING = (signal.SIGINT, signal.SIGTERM, signal.SIGHUP, signal.SIGQUIT)
INTERRUPTED = threading.Event()  # a signal asked live_check to stop
KEY_RUNNER = (
    "import importlib.util as u, sys\nfrom decimal import Decimal\nfrom pathlib import Path\n"
    "s = u.spec_from_file_location('answer_key', sys.argv[1]); m = u.module_from_spec(s)\n"
    "sys.modules['answer_key'] = m; s.loader.exec_module(m)\n"
    "m.assert_live_evidence(Path(sys.argv[2]), Decimal(sys.argv[3]))\n"
)


class Refusal(Exception):
    pass


def config_models() -> dict[str, str]:
    """The model each configuration runs (turn.py, a stdlib-only table, loaded by path)."""
    path = R / "src/deploy_workflow/model/turn.py"
    spec = importlib.util.spec_from_file_location("turn_models", path)
    assert spec and spec.loader
    module = importlib.util.module_from_spec(spec)
    sys.modules["turn_models"] = module
    spec.loader.exec_module(module)
    return dict(module.CONFIG_MODELS)


def call_faults(rows: list[dict[str, Any]], config: str) -> list[str]:
    found = [f"call {i}: no request_id" for i, r in enumerate(rows) if not r.get("request_id")]
    found += [
        f"call {i}: reported {r.get('reported_model')} != requested {r.get('requested_model')}"
        for i, r in enumerate(rows)
        if r.get("reported_model") != r.get("requested_model")
    ]
    configs = {r.get("config_id") for r in rows}
    if len(configs) != 1 or None in configs or (config and configs != {config}):
        return [
            *found,
            f"calls ran config(s) {sorted(map(str, configs))}, wanted {config or 'one'}",
        ]
    expected = config_models().get(str(next(iter(configs))))
    return found + [
        f"call {i}: model {r.get('requested_model')} != {expected} for config {r['config_id']}"
        for i, r in enumerate(rows)
        if r.get("requested_model") != expected
    ]


def spend_faults(rows: list[dict[str, Any]], cap: Decimal, status_spent: str) -> list[str]:
    charged = sum((Decimal(str(r["settled_usd"])) for r in rows), Decimal(0))
    found = [f"settled spend {charged} is not above zero"] if charged <= 0 else []
    if charged > cap:
        found.append(f"settled spend {charged} exceeds cap {cap}")
    try:
        if Decimal(status_spent) != charged:
            found.append(f"status spend {status_spent} != settled sum {charged}")
    except InvalidOperation:
        found.append(f"status spend {status_spent!r} is not a number")
    return found


def handoff_faults(run: Path, modules: set[str]) -> list[str]:
    """Live execution, and each handoff carrying the sha256 of its upstream (as the answer key)."""
    done = sorted(run.glob("completed-*.json"))
    if not done:
        return ["no completed-*.json: execution is not recorded"]
    record = json.loads(done[0].read_text())
    kinds = {record.get("execution"), *dict(record.get("module_execution", {})).values()}
    found = (
        [] if kinds == {"live-provider"} else [f"execution {sorted(map(str, kinds))} is not live"]
    )
    text = {m: (run / f"{m}.md").read_bytes() for m in modules if (run / f"{m}.md").exists()}
    found += [f"{m}: no accepted handoff file" for m in sorted(modules - set(text))]
    digest = {m: hashlib.sha256(raw).hexdigest().encode() for m, raw in text.items()}
    for later, upstream in (("CP-1", "CP-0"), ("CP-1A", "CP-0"), ("CP-1A", "CP-1")):
        if later in text and upstream in text and digest[upstream] not in text[later]:
            found.append(f"{later} handoff lacks the {upstream} digest: upstream not consumed")
    if "CP-1" in text:
        found += [
            f"CP-1 handoff lacks filed value {n}"
            for n in LITERALS
            if n.encode() not in text["CP-1"]
        ]
    return found


def live_evidence(
    run: Path, cap: Decimal, status_spent: str, modules: set[str], config: str = ""
) -> list[str]:
    """Faults in the retained provider calls and handoffs (rules of assert_live_evidence)."""
    rows = [json.loads(n) for n in (run / "live/calls.jsonl").read_text().splitlines() if n]
    found = call_faults(rows, config) + spend_faults(rows, cap, status_spent)
    seen = {r["module_id"] for r in rows}
    if seen != modules:
        found.append(f"modules called {sorted(seen)} != accepted {sorted(modules)}")
    return found + handoff_faults(run, modules)


def is_key_case(args: argparse.Namespace) -> bool:
    """The request is the one the answer key covers; decided from the arguments, not the run."""
    return args.config == KEY_CONFIG and set(args.modules.split()) == KEY_REQUESTED


def key_env() -> dict[str, str]:
    """The answer key's environment: pytest's pythonpath, and asserts never compiled away."""
    env = {k: v for k, v in os.environ.items() if k != "PYTHONOPTIMIZE"}
    return env | {"PYTHONPATH": f"{R / 'src'}{os.pathsep}{R}"}


def answer_key(run: Path, cap: Decimal) -> list[str]:
    """Run the test suite's own assert_live_evidence on the run, in the project interpreter."""
    command = [os.environ["FW_PYTHON"], "-c", KEY_RUNNER, str(R / "tests/test_cpos_launch.py")]
    try:
        done = subprocess.run(
            [*command, str(run), str(cap)],
            cwd=R,
            env=key_env(),
            capture_output=True,
            text=True,
            timeout=300,
            check=False,
        )
    except subprocess.TimeoutExpired:
        return ["answer key assert_live_evidence timed out after 300 s"]
    if done.returncode == 0:
        return []
    return ["answer key assert_live_evidence: " + " | ".join(done.stderr.strip().splitlines()[-4:])]


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
    if not args.rehearse and not any(os.environ.get(k) for k in PROVIDER_KEYS):
        raise Refusal(f"no provider key in the environment (one of {', '.join(PROVIDER_KEYS)})")
    if not (math.isfinite(args.minutes) and args.minutes >= 1):
        raise Refusal("--minutes must be at least 1")
    if args.out and Path(args.out).exists() and any(Path(args.out).iterdir()):
        raise Refusal("--out exists and is not empty")
    for name in ("FW_PYTHON", "ISSUER_LIBRARY_BINARY"):
        if not os.environ.get(name):
            raise Refusal(f"{name} is not set")
    if not Path(os.environ["ISSUER_LIBRARY_BINARY"]).is_file():
        raise Refusal("ISSUER_LIBRARY_BINARY is not a file")
    args.cap = cap
    return args


def group_alive(server: subprocess.Popen[bytes]) -> bool:
    server.poll()  # reap the server itself, so a zombie does not count
    try:
        os.killpg(server.pid, 0)
    except ProcessLookupError:
        return False
    except PermissionError:
        # macOS refuses signal 0 to a group holding only zombies (reparented, not yet reaped).
        # The group is ours (same user), so no live foreign process explains the refusal.
        return False
    return True


def leads_group(server: subprocess.Popen[bytes]) -> bool:
    try:
        return os.getpgid(server.pid) == server.pid
    except ProcessLookupError:
        return True  # already gone; killpg on its id finds nothing either way


def stop_group(server: subprocess.Popen[bytes]) -> str | None:
    """SIGTERM, then SIGKILL, the server's process group; a message if anything may still live."""
    if not leads_group(server):
        for sig in (signal.SIGTERM, signal.SIGKILL):
            with suppress(ProcessLookupError):
                os.kill(server.pid, sig)
            with suppress(subprocess.TimeoutExpired):
                server.wait(timeout=10)
        return (
            f"server {server.pid} does not lead its own process group: only it was signalled, "
            "its workers may still be spending. Find them with: pgrep -fl 'bridge.py start'"
        )
    for sig, patience in ((signal.SIGTERM, 15), (signal.SIGKILL, 10)):
        if not group_alive(server):
            return None
        with suppress(ProcessLookupError):
            os.killpg(server.pid, sig)
        end = time.monotonic() + patience
        while group_alive(server) and time.monotonic() < end:
            time.sleep(0.2)
    if not group_alive(server):
        return None
    return (
        f"process group {server.pid} still alive after SIGKILL: an engine worker may still be "
        "spending. Find it with: pgrep -fl 'bridge.py start'; its status.json is under "
        "<workspace>/intake/<id>/"
    )


def arm_watchdog(server: subprocess.Popen[bytes]) -> subprocess.Popen[bytes]:
    """A helper in its own session that stops the server's group if live_check dies by any means.

    Its stdin is a pipe only this process holds (children start with close_fds), so the kernel's
    close of it on our death, SIGKILL included, is the signal. It cannot see a hung live_check."""
    return subprocess.Popen(
        ["sh", "-c", WATCHDOG, str(server.pid)],
        stdin=subprocess.PIPE,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        env={"PATH": os.environ.get("PATH", "/usr/bin:/bin")},
        start_new_session=True,
    )


def spend_of(ws: Path) -> tuple[str | None, Decimal, int]:
    """status.json's recorded spend, the ledger's settled sum, and rows of unknown cost.

    A row with no settled amount (cost unknown) or a torn line counts as unknown, never as zero."""
    status: str | None = None
    for path in sorted((ws / "intake").glob("*/status.json")):
        try:
            spent = json.loads(path.read_text()).get("spent_usd")
            status = None if spent is None else str(spent)
        except (OSError, ValueError):
            status = "unreadable"
    ledger, unknown = Decimal(0), 0
    for path in (ws / "runs").glob("*/live/calls.jsonl"):
        try:
            lines = [n for n in path.read_text().splitlines() if n]
        except OSError:
            unknown += 1
            continue
        for line in lines:
            try:
                ledger += Decimal(str(json.loads(line)["settled_usd"]))
            except (ValueError, KeyError, TypeError, InvalidOperation):
                unknown += 1
    return status, ledger, unknown


def check_review(page: Any, args: argparse.Namespace) -> list[str]:
    """What the review screen says it will run, against what was asked for."""
    shown = page.evaluate(
        """() => ({
          rows: Object.fromEntries([...document.querySelectorAll('#run-review dl dt')]
            .map(t => [t.textContent, t.nextElementSibling.textContent])),
          ids: [...document.querySelectorAll('#run-review .review-modules li')]
            .map(li => li.title.split(':')[0])})"""
    )
    print(f"review screen will run: {shown['ids']} ({shown['rows']})", flush=True)
    found = []
    model, effort = config_models().get(args.config), args.config.rsplit("-", 1)[-1]
    if (
        not model
        or model not in shown["rows"].get("Model", "")
        or effort not in shown["rows"]["Model"]
    ):
        found.append(f"review model {shown['rows'].get('Model')!r} is not config {args.config}")
    cap = shown["rows"].get("Maximum spend", "").removeprefix("USD ")
    try:
        if Decimal(cap) != args.cap:
            found.append(f"review cap USD {cap} != {args.cap}")
    except InvalidOperation:
        found.append(f"review cap {cap!r} is not a number")
    ids, wanted = set(shown["ids"]), set(args.modules.split())
    if is_key_case(args) and ids != KEY_MODULES:
        found.append(f"review modules {shown['ids']} are not exactly {sorted(KEY_MODULES)}")
    elif not wanted <= ids:
        found.append(f"review modules {shown['ids']} lack some of {args.modules}")
    return found


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
    # The app bounds the review at 10 minutes; a refusal shows its problems in #new-run-message.
    page.wait_for_function(
        "() => !document.getElementById('review-step').hidden"
        " || /\\S/.test(document.getElementById('new-run-message').textContent)"
        " && !/^Checking/.test(document.getElementById('new-run-message').textContent)",
        timeout=660000,
    )
    if page.locator("#review-step").is_hidden():
        raise RuntimeError("review refused: " + page.inner_text("#new-run-message")[:500])


def walk(
    bc: Any, browser: Any, args: argparse.Namespace, ws: Path, summary: dict[str, Any]
) -> None:
    page = browser.new_page(viewport={"width": 1366, "height": 768})  # inside attempt: captured
    bc.errors_of(page)
    fill_form(page, args)
    wrong = check_review(page, args)
    if wrong:  # raised, so the attempt keeps the page: screenshot, source and URL
        raise RuntimeError("review screen: " + "; ".join(wrong))
    page.check("#run-confirm")
    if page.is_disabled("#start-run"):
        raise RuntimeError("Start stays disabled after review (provider not configured?); no spend")
    page.click("#start-run")  # the one paid step; never retried
    page.wait_for_selector("#progress-step:not([hidden])")
    page.wait_for_selector(
        "#open-run:not([hidden]), #another-run:not([hidden])", timeout=int(args.minutes * 60000)
    )
    status = page.inner_text("#run-progress")
    if not status.startswith("complete"):
        raise RuntimeError(f"run did not complete: {status[:300]}")
    bc.note(True, f"run finished: {status[:120]}")
    check_run(bc, page, args, ws, summary)


def check_run(
    bc: Any, page: Any, args: argparse.Namespace, ws: Path, summary: dict[str, Any]
) -> None:
    note = bc.note
    shown_spend = page.inner_text("#run-spend")
    page.click("#open-run")
    page.wait_for_selector(".report-built .report-row a", timeout=30000)
    page.click(".report-built .report-row a >> nth=0")
    report = page.frame_locator("#report-preview")
    report.locator("#view-root").wait_for(state="attached", timeout=30000)
    run = max((ws / "runs").glob("web-*"))
    summary["run_id"] = run.name
    state = json.loads(next((ws / "intake").glob("*/status.json")).read_text())
    summary["report"] = str(next(run.glob("deliveries/*/report.html"), ""))
    note(
        shown_spend == f"Recorded spend: USD {state.get('spent_usd')}",
        f"app spend {shown_spend!r} equals status.json {state.get('spent_usd')!r}",
    )
    accepted = {p.stem for p in run.glob("CP-*.md")}
    built = page.locator(".built-from summary", has_text="Built from").first.inner_text()
    count = re.search(r"Built from (\d+) handoffs", built)
    note(
        count is not None and int(count[1]) == len(accepted),
        f"{built!r} vs {len(accepted)} accepted",
    )
    if args.rehearse:
        return
    shown = report.locator("#view-root").evaluate(
        "el => { const c = el.cloneNode(true); c.querySelectorAll('svg').forEach(n => n.remove());"
        " return c.textContent; }"
    )
    handoffs = [p.read_text() for p in sorted(run.glob("deliveries/*/CP-*.md"))]
    problems = flow_check.run_faults(run, SOURCES) + flow_check.report_faults(shown, handoffs)
    problems += live_evidence(run, args.cap, str(state.get("spent_usd")), accepted, args.config)
    problems += [f"report lacks filed value {n}" for n in LITERALS if n not in shown]
    problems += [
        f"requested module {m} not accepted" for m in sorted(set(args.modules.split()) - accepted)
    ]
    if is_key_case(args):  # any mismatch with the key's case (e.g. an extra module) is its fault
        problems += answer_key(run, args.cap)
        summary["answer_key"] = "applied"
    else:
        summary["answer_key"] = (
            f"not applicable: request is not {KEY_CONFIG} with {sorted(KEY_REQUESTED)}"
        )
    for problem in problems:
        note(False, f"live check: {problem}", kind="flow")
    note(not problems, "flow, evidence and filed-value checks")


def run_walk(
    bc: Any, args: argparse.Namespace, out: Path, summary: dict[str, Any], held: dict[str, str]
) -> None:
    sync_playwright = importlib.import_module("playwright.sync_api").sync_playwright
    ws = out / "ws"
    ws.mkdir()
    engine = HERE / "fake_engine" if args.rehearse else R / "apps/issuer-library/engine"
    server = dog = None
    try:
        server = bc.serve(
            ws,
            PORT,
            engine,
            key="not-a-real-key" if args.rehearse else None,
            extra=held,
        )
        dog = arm_watchdog(server)
        with sync_playwright() as driver:
            browser = bc.SignedBrowser(driver.chromium.launch())
            try:
                bc.attempt("live", browser, lambda: walk(bc, browser, args, ws, summary))
            finally:
                browser.close()
    finally:
        ignore_signals()  # teardown must finish
        try:
            if server is not None and (left := stop_group(server)):
                print(left, file=sys.stderr, flush=True)
                bc.FAULTS.add("live", "worker", left)
        finally:
            if dog is not None:
                dog.kill()  # disarmed: the group is gone, its id must not be signalled again
                dog.wait()
            report_spend(bc, ws, summary)


def report_spend(bc: Any, ws: Path, summary: dict[str, Any]) -> None:
    status, ledger, unknown = spend_of(ws)
    summary["spent_usd"], summary["ledger_usd"], summary["unknown_cost_calls"] = (
        status,
        str(ledger),
        unknown,
    )
    extra = f" + {unknown} calls of unknown cost" if unknown else ""
    print(f"spend: status.json USD {status}, ledger USD {ledger}{extra}", flush=True)
    if unknown:
        bc.FAULTS.add("live", "spend", f"{unknown} calls of unknown cost: spend is not known")


def ignore_signals() -> None:
    for sig in HALTING:
        signal.signal(sig, signal.SIG_IGN)


def finish(bc: Any, args: argparse.Namespace, out: Path, summary: dict[str, Any]) -> int:
    passed = sum(ok for ok, _ in bc.results)
    mode = "rehearsal" if args.rehearse else "live"
    scope = (
        REHEARSAL
        if args.rehearse
        else f"live provider: {args.config}, {CASE}, modules {args.modules}, "
        f"spend USD {summary['spent_usd']}; answer key {summary.get('answer_key', 'not reached')}"
    )
    secrets = bc.secrets()
    bc.FAULTS.write(out / "faults.json", scope, passed, secrets)
    recorded = json.loads((out / "faults.json").read_text()) | {"mode": mode}
    (out / "faults.json").write_text(redact(json.dumps(recorded, indent=2), secrets) + "\n")
    summary |= {"mode": mode, "scope": scope, "failed": len(bc.FAULTS.items)}
    (out / "summary.json").write_text(
        redact(json.dumps(summary, indent=2, default=str), secrets) + "\n"
    )
    print(f"{passed} passed, {len(bc.FAULTS.items)} faults: {out / 'faults.json'}")
    return int(bool(bc.FAULTS.items) or passed != len(bc.results))


def terminate(_signal: int, _frame: Any) -> None:
    INTERRUPTED.set()
    raise KeyboardInterrupt


def main(argv: list[str]) -> int:
    try:
        args = parse(argv)
    except Refusal as refusal:
        print(f"live_check: {refusal}", file=sys.stderr)
        return 2
    # Keys leave this process's environment now; only the server gets the provider ones.
    popped = {k: os.environ.pop(k) for k in KEYS if k in os.environ}
    held = {k: v for k, v in popped.items() if k in PROVIDER_KEYS and not args.rehearse}
    import browser_check as bc  # imports Playwright; after the refusals

    known = bc.secrets
    bc.secrets = lambda: [*known(), *popped.values()]
    out = Path(args.out) if args.out else Path(tempfile.mkdtemp(prefix="issuer-library-live-"))
    out.mkdir(parents=True, exist_ok=True)
    bc.NEW_SESSION = True  # each server in its own process group
    bc.S, bc.PY, bc.APP = out, os.environ["FW_PYTHON"], os.environ["ISSUER_LIBRARY_BINARY"]
    mode = "REHEARSAL (fake engine, no provider)" if args.rehearse else "PAID RUN"
    print(
        f"{mode}: config={args.config}, modules={args.modules} (dependencies added by the "
        f"launcher), cap=USD {args.cap}, case={CASE}, workspace={out / 'ws'}",
        flush=True,
    )
    summary: dict[str, Any] = {"run_id": None, "spent_usd": None, "report": None}
    for sig in HALTING:  # also SIGINT: a shell's background job starts with it ignored
        signal.signal(sig, terminate)
    try:
        run_walk(bc, args, out, summary, held)
    except KeyboardInterrupt:
        ignore_signals()
        bc.FAULTS.add("live", "interrupted", "interrupted by a signal; spend may be above zero")
    except (Exception, SystemExit) as error:  # noqa: BLE001 - recorded as a fault, never silent
        bc.FAULTS.add("live", "exception", f"{type(error).__name__}: {str(error)[:600]}")
    finally:
        ignore_signals()
        for fault in bc.FAULTS.items:  # a Ctrl-C to the whole group also breaks the browser
            if INTERRUPTED.is_set() and fault.kind == "exception":
                fault.kind = "interrupted"
        bc.scan_server_logs()
        code = finish(bc, args, out, summary)
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
