"""Independent data-flow check: sources -> module handoffs -> delivered copies -> report.

Stdlib only; nothing from src/ or engine/, so expected values stay independent of production code.
Usage: flow_check.py <run_dir> [--sources DIR]
"""

import hashlib
import json
import re
import sys
from collections.abc import Iterable
from decimal import ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal
from pathlib import Path
from typing import Any

ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}")
# A page reference (pp.3,105-109,131,146) lists pages, which are not figures.
PAGES = re.compile(r"\bpp?\.[\d,\u2013-]+", re.IGNORECASE)
# Arguments of a call, sum(980,161), are separate numbers, not one figure with a thousands comma.
CALL_ARGS = re.compile(r"(?<=\w\()[\d.,\s\u2212-]+(?=\))")
# A digest has letters; a run of digits alone is a long decimal result, not a digest.
# The same date written out for display: 31 March 2025, Mar 31, 2025.
MONTH = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]{0,6}\.?"
WRITTEN_DATE = re.compile(rf"\b\d{{1,2}} {MONTH},? \d{{4}}\b|\b{MONTH} \d{{1,2}},? \d{{4}}\b")
HEX_RUN = re.compile(r"(?=[0-9]*[a-fA-F])[0-9a-fA-F]{16,}")
# A standalone number: not inside a word, path or file name. A trailing x, bn, mm, m or k is a
# multiple or scale (4.2x, $12.6bn) and is stripped; the number never stops short of a decimal.
# Not after "slug-" in lowercase (run-20261105, tdg-20240930; Term Loan B-12 stays checked) and not
# after "digit," (a page list 38,54,106 is not the figure 54,106).
UNIT = r"(?i:x|bn|mm|m|k)"
NUMBER = re.compile(
    rf"(?<![\w/.])(?<![a-z]-)(?<!\d,)(?:\d{{1,3}}(?:,\d{{3}})+|\d+)(?:\.\d+)?{UNIT}?(?!\w|\.[A-Za-z\d])"
)
UNIT_END = re.compile(rf"{UNIT}$")
LEADING_ZERO = re.compile(r"0\d+")
MODULE = re.compile(r"CP-[A-Z0-9]+")


def numbers(text: str) -> set[str]:
    text = CALL_ARGS.sub(lambda m: m[0].replace(",", " "), text)
    text = PAGES.sub(" ", HEX_RUN.sub(" ", WRITTEN_DATE.sub(" ", ISO_DATE.sub(" ", text))))
    found = set()
    for match in NUMBER.findall(text):
        value = UNIT_END.sub("", match).replace(",", "")
        if "." in value:
            value = value.rstrip("0").rstrip(".")
        if len(value) > 1 and not LEADING_ZERO.fullmatch(value):  # 02, 057: labels, not quantities
            found.add(value)
    return found


def rounded(values: set[str]) -> set[str]:
    """The roundings a reader may print of a long calculation result (4.50682961... -> 4.51).

    Only values with 6 or more decimals are expanded: they are kernel results, not reported figures.
    """
    out = set(values)
    for value in values:
        if "." in value and len(value.split(".")[1]) >= 6:
            for places in range(7):
                for mode in (ROUND_HALF_UP, ROUND_HALF_EVEN):
                    out |= numbers(f"{Decimal(value).quantize(Decimal(1).scaleb(-places), mode):f}")
    return out


def _sha(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def _decode(path: Path) -> str:
    # Binary sources (PDF, images) carry no checkable text; they are skipped, not guessed at. A
    # missing input is reported by _checked_inputs, so it adds no text here.
    if not path.is_file():
        return ""
    try:
        return path.read_bytes().decode("utf-8")
    except UnicodeDecodeError:
        return ""


def _accepted(run: Path) -> dict[str, Path]:
    records = sorted(run.glob("completed-*.json"), key=lambda p: p.stat().st_mtime)
    if records:
        modules = json.loads(records[-1].read_text())["modules"]
        return {module: run / relative for module, relative in modules.items()}
    return {p.stem: p for p in sorted(run.glob("CP-*.md")) if MODULE.fullmatch(p.stem)}


def _invocations(run: Path) -> tuple[dict[str, list[tuple[Path, dict[str, Any]]]], list[str]]:
    by_module: dict[str, list[tuple[Path, dict[str, Any]]]] = {}
    faults = []
    for folder in sorted(run.glob("live/modules/*/")):
        try:
            request = json.loads(
                json.loads((folder / "0.request.json").read_text())["messages"][1]["text"]
            )
            by_module.setdefault(request["module_id"], []).append((folder, request))
        except (OSError, ValueError, KeyError, IndexError, TypeError) as error:
            faults.append(f"{folder.name}: invocation record unreadable ({error!r})")
    return by_module, faults


def _read(folder: Path) -> str:
    parts = []
    for tools in sorted(folder.glob("*.tools.json")):
        parts += [c["text"] for c in json.loads(tools.read_text()) if c["name"] != "write_handoff"]
    return "\n".join(parts)


def _producing(
    invocations: list[tuple[Path, dict[str, Any]]], handoff: str
) -> list[tuple[Path, dict[str, Any]]]:
    """The invocations whose drafts hold the accepted text; earlier attempts of a re-run module
    received superseded upstreams and are not what produced it. Without a match, all are checked."""
    drafted = [
        (folder, request)
        for folder, request in invocations
        if any(d.read_text().strip() == handoff.strip() for d in folder.glob("*.draft.md"))
    ]
    return drafted or invocations


def _shared_numbers(run: Path, sources: Path | None) -> set[str]:
    texts = [_decode(p) for p in sorted(run.glob("source-text/*.jsonl"))]
    texts += [_decode(run / "context.json")] if (run / "context.json").exists() else []
    if sources is not None:
        texts += [_decode(p) for p in sorted(sources.rglob("*")) if p.is_file()]
    return set().union(*(numbers(t) for t in texts)) if texts else set()


def _checked_inputs(
    run: Path, request: dict[str, Any], sources: Path | None, module: str
) -> list[str]:
    faults = []
    for name, digest in request["sources"].items():
        local = sources / name if sources is not None else None
        in_sources = local is not None and local.is_file() and _sha(local.read_bytes()) == digest
        kept = run / "inputs" / digest
        in_inputs = kept.is_file() and _sha(kept.read_bytes()) == digest
        if not in_sources and not in_inputs:
            faults.append(f"{module}: source {name} sha256 {digest[:12]} matches no supplied file")
    return faults


def _received(run: Path, request: dict[str, Any]) -> set[str]:
    """Numbers in what the module was given: its upstream handoffs and its source files."""
    texts = [h["markdown"] for h in request["handoffs"].values()]
    texts += [_decode(run / "inputs" / digest) for digest in request["sources"].values()]
    return set().union(*(numbers(t) for t in texts)) if texts else set()


def run_faults(run: Path, sources: Path | None = None) -> list[str]:
    accepted = _accepted(run)
    handoffs = {module: path.read_bytes() for module, path in accepted.items()}
    by_module, faults = _invocations(run)
    shared = _shared_numbers(run, sources)
    for module, data in handoffs.items():
        invocations = _producing(by_module.get(module, []), data.decode("utf-8", "replace"))
        if not invocations:
            faults.append(f"{module}: no invocation record to check the handoff against")
        evidence = set(shared)
        for folder, request in invocations:
            for upstream, sent in request["handoffs"].items():
                want = handoffs.get(upstream)
                if (
                    want is None
                    or sent["sha256"] != _sha(want)
                    or sent["markdown"].encode() != want
                ):
                    faults.append(
                        f"{module}: upstream {upstream} received differs from its accepted handoff"
                    )
            faults += _checked_inputs(run, request, sources, module)
            evidence |= numbers(_read(folder)) | _received(run, request)
        evidence = rounded(evidence)
        if invocations:
            faults += [
                f"{module}: number {n} in the handoff is not in what the module read or received"
                for n in sorted(numbers(data.decode("utf-8", "replace")) - evidence)
            ]
    for folder in sorted(p for p in run.glob("deliveries/*") if p.is_dir()):
        faults += [
            f"{module}: no copy in delivery {folder.name}, the handoff was dropped"
            for module in handoffs
            if not (folder / f"{module}.md").is_file()
        ]
    for copy in sorted(run.glob("deliveries/*/CP-*.md")):
        if copy.read_bytes() != handoffs.get(copy.stem):
            faults.append(
                f"{copy.stem}: delivered copy {copy.parent.name}/{copy.name} differs "
                "from the accepted handoff"
            )
    return faults


def report_faults(report_text: str, handoffs: Iterable[str], context: str = "") -> list[str]:
    known = rounded(numbers(context).union(*(numbers(h) for h in handoffs)))
    return [
        f"report: number {n} is not in the handoffs or context"
        for n in sorted(numbers(report_text) - known)
    ]


def main(argv: list[str]) -> int:
    args = list(argv)
    sources = Path(args.pop(args.index("--sources") + 1)) if "--sources" in args else None
    if sources is not None:
        args.remove("--sources")
    if len(args) != 1:
        print("usage: flow_check.py <run_dir> [--sources DIR]", file=sys.stderr)
        return 2
    faults = run_faults(Path(args[0]), sources)
    print("\n".join(faults))
    print(f"flow: {len(faults)} fault(s)")
    return int(bool(faults))


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
