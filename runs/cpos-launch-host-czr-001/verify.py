"""Offline check of the Caesars host-session run of the `minimum` module set. Writes nothing.

Expected values come from cases/czr-2026q2-earnings-update/expected.json, keys authored from the
documents before this run existed, and from the source lines CP-1 cites, never from a handoff.
Run from the repository root:

    PYTHONPATH=src .venv/bin/python runs/cpos-launch-host-czr-001/verify.py
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
RUN = ROOT / "runs/cpos-launch-host-czr-001"
CASE = ROOT / "cases/czr-2026q2-earnings-update"
MODULES = ("CP-0", "CP-1", "CP-1A", "CP-2", "CP-5")
DOCS = {
    "K": "CZR_FY2025_10K.txt",
    "Q": "CZR_Q2_2026_10Q.txt",
    "R": "CZR_Q2_2026_Earnings_Release.txt",
}


def sha(raw: bytes) -> str:
    return hashlib.sha256(raw).hexdigest()


def rows(markdown: str) -> list[list[str]]:
    return [
        [c.strip() for c in line.strip().strip("|").split("|")]
        for line in markdown.splitlines()
        if line.startswith("|") and not set(line) <= set("|- ")
    ]


def printed(value: str) -> str:
    """An expected.json decimal string in the handoffs' printed form: 1,807 and (335)."""
    number = int(value)
    return f"({-number:,})" if number < 0 else f"{number:,}"


def check_answer_keys(handoffs: dict[str, str]) -> dict[str, object]:
    """Each keyed value must sit in a handoff table row that carries the key line's label."""
    keys = json.loads((CASE / "expected.json").read_text())
    table = [r for text in handoffs.values() for r in rows(text)]
    found, absent = 0, []
    for value in keys["values"]:
        label = value["key_line"].split("|")[0].strip()
        label = "Net revenues" if label == "Caesars" else label
        if any(r[0].startswith(label) and printed(value["value"]) in r[1:] for r in table):
            found += 1
        else:
            absent.append(f"{value['measure']} {value['period']} {value['value']}")
    return {"found": found, "total": len(keys["values"]), "absent": absent}


def numbers(lines: list[str], line: int, label: str) -> list[Fraction]:
    text = lines[line - 1]
    assert text.startswith(label), f"line {line} is not {label}: {text[:50]}"
    found = []
    for cell in text.split("|")[1:]:
        c = cell.strip().replace("$", "").replace(",", "")
        if re.fullmatch(r"\(?\d+\)?", c):
            found.append(-Fraction(c.strip("()")) if c.startswith("(") else Fraction(c))
    return found


def half_up(value: Fraction, places: int) -> str:
    scaled = value * 10**places
    whole = int(scaled) + (1 if scaled - int(scaled) >= Fraction(1, 2) else 0)
    return f"{Fraction(whole, 10**places):.{places}f}"


def check_metrics(cp1: str) -> int:
    """Recompute the CP-1 metric table from the source lines it cites, with exact fractions."""
    k, q, r = ((CASE / "documents" / name).read_text().splitlines() for name in DOCS.values())

    def ltm(year: Fraction, six: list[Fraction], first: int = 0) -> Fraction:
        return year + six[first] - six[first + 1]

    revenue = ltm(numbers(k, 1734, "Net revenues")[0], numbers(q, 113, "Net revenues"), 2)
    adjusted = ltm(numbers(k, 1329, "Adjusted EBITDA")[0], numbers(r, 64, "Caesars"))
    interest = -ltm(numbers(k, 1748, "Interest expense")[0], numbers(q, 126, "Interest expense"), 2)
    rent = ltm(numbers(k, 1868, "Cash interest paid for rent")[0], numbers(q, 250, "Cash interest"))
    cash_interest = ltm(numbers(k, 1867, "Cash interest paid for debt")[0], numbers(q, 249, "Cash"))
    debt = numbers(q, 507, "Total debt")[0]
    obligations = numbers(q, 89, "Long-term financing obligations")[0]
    net_debt = numbers(r, 78, "Net debt")[0]
    assert net_debt == debt - numbers(q, 69, "Cash and cash equivalents")[0]
    expected = {
        "Net revenues (USD m)": f"{int(revenue):,}",
        "Adjusted EBITDA, issuer-defined (USD m)": f"{int(adjusted):,}",
        "Total debt / Adjusted EBITDA (x)": half_up(debt / adjusted, 2),
        "Net debt / Adjusted EBITDA (x)": half_up(net_debt / adjusted, 2),
        "Debt plus financing obligations / Adjusted EBITDA (x)": half_up(
            (debt + obligations) / adjusted, 2
        ),
        "Total debt / Adjusted EBITDA after cash rent (x)": half_up(debt / (adjusted - rent), 2),
        "Adjusted EBITDA / interest expense, net (x)": half_up(adjusted / interest, 2),
        "Adjusted EBITDA after cash rent / cash interest paid for debt (x)": half_up(
            (adjusted - rent) / cash_interest, 2
        ),
        "Adjusted EBITDA margin (%)": half_up(100 * adjusted / revenue, 1),
    }
    selected = {r[0]: r[1] for r in rows(cp1.split("### Financials and credit metrics")[1])}
    for label, value in expected.items():
        assert selected[label] == value, f"{label}: {selected[label]} != {value}"
    return len(expected)


def check() -> dict[str, object]:
    completion = json.loads(next(RUN.glob("completed-*.json")).read_text())
    assert completion["execution"] == "host-session" and not (RUN / "live").exists()
    assert set(completion["module_execution"].values()) == {"host-session"}
    report = next((RUN / "deliveries").glob("*/report.html"))
    assert verify_delivery(next(RUN.glob("delivery-*.json")), report.parent) == report
    raw = {m: (report.parent / f"{m}.md").read_bytes() for m in MODULES}
    for i, module in enumerate(MODULES[1:], 1):
        for upstream in MODULES[:i]:
            assert sha(raw[upstream]).encode() in raw[module], f"{module} lacks {upstream}"
    view = json.loads((report.parent / "report-view.json").read_text())
    states = {b["block_id"]: b["state"] for b in view["blocks"]}
    assert set(states.values()) == {"populated"} and len(states) == 6, states
    handoffs = {m: data.decode() for m, data in raw.items()}
    keys = check_answer_keys(handoffs)
    metrics = check_metrics(handoffs["CP-1"])
    before = sorted(p for p in RUN.rglob("*") if "pending-deliveries" not in p.parts)
    argv = [
        *("--context", str(RUN / "context.json"), "--sources", str(CASE / "documents")),
        *("--config", "host", "--modules", "minimum", "--out", str(RUN)),
    ]
    with redirect_stdout(StringIO()) as out:
        assert main(argv) == 0
    assert str(report) in out.getvalue()
    assert sorted(p for p in RUN.rglob("*") if "pending-deliveries" not in p.parts) == before
    return {
        "report": str(report.relative_to(ROOT)),
        "report_sha256": sha(report.read_bytes()),
        "handoffs": {m: sha(data) for m, data in raw.items()},
        "sections_populated": len(states),
        "answer_key_values": keys,
        "recomputed_metric_cells": metrics,
    }


if __name__ == "__main__":
    json.dump(check(), sys.stdout, indent=2)
    print()
