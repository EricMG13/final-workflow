"""Offline check of the two host-session pilot runs. No provider call; writes nothing.

Expected values come from the pinned 10-K text, never from a handoff or production calculation:
every reported row in CP-1 must appear with the same figures on its cited page, and each CP-1
ratio is recomputed with Fraction from those source rows. Run from the repository root:

    PYTHONPATH=src .venv/bin/python runs/cpos-launch-host-002/verify.py
"""

import hashlib
import json
import re
import sys
from contextlib import redirect_stdout
from fractions import Fraction
from io import StringIO
from pathlib import Path

from deploy_workflow.handoff_delivery import verify_delivery
from deploy_workflow.owners.cpos_launch import main

ROOT = Path(__file__).resolve().parents[2]
RUNS = ("cpos-launch-host-001", "cpos-launch-host-002")
TDG = ROOT / "data/public-corpus/v1/TDG"
TEN_K = "source-text/TDG_2024-09-30_10-K_0001260221-24-000083_tdg-20240930.htm.jsonl"
# Reported CP-1 tables and the 10-K pages that print them.
TABLES = {
    "Reported income statement": (121,),
    "Reported balance sheet": (120,),
    "Reported cash flows (selected lines)": (122, 123),
    "Debt register at September 30, 2024": (144, 145),
    "Issuer non-GAAP measures and definition review": (71,),
}
# Labels this handoff rewrote for the reader; their figures are checked under the printed label.
RELABELLED = {
    "Earnings per share (USD per share)": "Earnings per share",
    "Cash dividends declared per common share (USD per share)": "Cash dividends declared per common share",
    "Printed subtotal, excluding the securitization row": "Finance lease obligations 262 — — 262",
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def flat(text: str) -> str:
    return " ".join(text.replace("$", " ").split())


def pages(run: Path) -> dict[int, str]:
    rows = (json.loads(line) for line in (run / TEN_K).read_text().splitlines())
    return {r["page"]: flat(r["text"]) for r in rows}


def tables(markdown: str) -> dict[str, list[list[str]]]:
    """Each `###` section's first table, as rows of cells without the header."""
    found: dict[str, list[list[str]]] = {}
    heading = None
    for line in markdown.splitlines():
        if line.startswith("### "):
            heading = line[4:].strip()
        elif heading and line.startswith("|") and not set(line) <= set("|- "):
            found.setdefault(heading, []).append([c.strip() for c in line.strip("|").split("|")])
    return {h: rows[1:] for h, rows in found.items()}


def check_reported_rows(cp1: str, text: dict[int, str]) -> tuple[dict[str, list[str]], int]:
    """Every figure of every reported row follows its printed label on a cited page, with at most
    a footnote marker or note alias in between."""
    source: dict[str, list[str]] = {}
    cells = 0
    for heading, numbers in TABLES.items():
        joined = " ".join(text[n] for n in numbers)
        for label, *values in tables(cp1)[heading]:
            printed = flat(RELABELLED.get(label, label))
            sequence = flat(" ".join(values))
            starts = [m.end() for m in re.finditer(re.escape(printed), joined)]
            assert starts, f"{heading}: label not on its page: {label}"
            assert any(sequence in joined[s : s + 60 + len(sequence)] for s in starts), (
                f"{heading}: {label}: {values} do not follow the label"
            )
            source[label] = values
            cells += len(values)
    return source, cells


def number(cell: str) -> Fraction:
    cell = cell.replace(",", "")
    return -Fraction(cell[1:-1]) if cell.startswith("(") else Fraction(cell)


def half_up(value: Fraction, places: int) -> str:
    scaled = value * 10**places
    whole = int(scaled) + (1 if scaled - int(scaled) >= Fraction(1, 2) else 0)
    return f"{Fraction(whole, 10**places):.{places}f}" if places else str(whole)


def check_ratios(cp1: str, rows: dict[str, list[str]], text: dict[int, str]) -> int:
    """Recompute the calculated metrics from source rows; compare with the selected table."""
    total_debt = re.search(r"Total debt \(1\) ([\d,]+) ([\d,]+)", text[52])
    assert total_debt, "10-K page 52 total debt row"
    debt = [number(total_debt.group(1)), number(total_debt.group(2))]
    cash = [number(v) for v in rows["Cash and cash equivalents"]]
    ad = [number(v) for v in rows["EBITDA As Defined"]]
    ebitda = [number(v) for v in rows["EBITDA"]]
    interest = [number(v) for v in rows["INTEREST EXPENSE—NET"][:2]]
    sales = [number(v) for v in rows["NET SALES"][:2]]
    cfo = [number(v) for v in rows["Net cash provided by operating activities"][:2]]
    capex = [number(v) for v in rows["Capital expenditures"][:2]]
    payment = re.search(r"([\d,]+) million payment in special dividends and dividend", text[56])
    assert payment, "10-K page 56 pro forma footnote"
    paid = number(payment.group(1))
    expected = {
        "Free cash flow, CFO less capex (USD m)": [f"{int(cfo[i] + capex[i]):,}" for i in range(2)],
        "Net debt, carrying (USD m)": [f"{int(debt[i] - cash[i]):,}" for i in range(2)],
        "Total debt / EBITDA As Defined (x)": [half_up(debt[i] / ad[i], 2) for i in range(2)],
        "Total debt / EBITDA (x)": [half_up(debt[i] / ebitda[i], 2) for i in range(2)],
        "Net debt / EBITDA As Defined (x)": [
            half_up((debt[i] - cash[i]) / ad[i], 2) for i in range(2)
        ],
        "EBITDA As Defined / interest expense—net (x)": [
            half_up(ad[i] / interest[i], 2) for i in range(2)
        ],
        "EBITDA / interest expense—net (x)": [
            half_up(ebitda[i] / interest[i], 2) for i in range(2)
        ],
        "EBITDA As Defined margin (%)": [half_up(100 * ad[i] / sales[i], 1) for i in range(2)],
    }
    selected = {r[0]: r[1:3] for r in tables(cp1)["Financials and credit metrics"]}
    for label, values in expected.items():
        assert selected[label] == values, f"{label}: {selected[label]} != {values}"
    pro_forma = debt[0] - (cash[0] - paid)
    assert f"{int(pro_forma):,}" in cp1 and half_up(pro_forma / ad[0], 2) + "x" in cp1
    return len(expected) * 2 + 2


def check_run(name: str) -> dict[str, object]:
    run = ROOT / "runs" / name
    completion = json.loads(next(run.glob("completed-*.json")).read_text())
    assert completion["execution"] == "host-session"
    assert set(completion["module_execution"].values()) == {"host-session"}
    assert completion["provider_cap_usd"] == 0 and not (run / "live").exists()
    report = next((run / "deliveries").glob("*/report.html"))
    assert verify_delivery(next(run.glob("delivery-*.json")), report.parent) == report
    handoffs = {m: (report.parent / f"{m}.md").read_bytes() for m in ("CP-0", "CP-1", "CP-1A")}
    digest = {m: sha(raw) for m, raw in handoffs.items()}
    assert digest["CP-0"].encode() in handoffs["CP-1"]
    assert digest["CP-0"].encode() in handoffs["CP-1A"]
    assert digest["CP-1"].encode() in handoffs["CP-1A"]
    view = json.loads((report.parent / "report-view.json").read_text())
    states = {b["block_id"]: b["state"] for b in view["blocks"]}
    assert set(states.values()) == {"populated"} and len(states) == 4
    page = report.read_text()
    for figure in ("7,940", "6,261", "24,880", "4,173", "5.96"):
        assert figure in page, figure
    text = pages(run)
    cp1 = handoffs["CP-1"].decode()
    rows, cells = check_reported_rows(cp1, text)
    ratios = check_ratios(cp1, rows, text)
    # A relaunch publishes the same report, sends nothing and writes nothing.
    before = sorted(p for p in run.rglob("*") if "pending-deliveries" not in p.parts)
    argv = [
        *("--context", str(run / "context.json"), "--sources", str(TDG), "--config", "host"),
        *("--modules", "CP-1", "CP-1A", "--out", str(run)),
    ]
    with redirect_stdout(StringIO()) as out:
        assert main(argv) == 0
    assert str(report) in out.getvalue()
    assert sorted(p for p in run.rglob("*") if "pending-deliveries" not in p.parts) == before
    return {
        "report": str(report.relative_to(ROOT)),
        "report_sha256": sha(report.read_bytes()),
        "handoffs": digest,
        "reported_rows": len(rows),
        "reported_cells": cells,
        "recomputed_metric_cells": ratios,
    }


if __name__ == "__main__":
    results = {name: check_run(name) for name in RUNS}
    json.dump(results, sys.stdout, indent=2)
    print()
