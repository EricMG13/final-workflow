"""The library's store: every retained handoff in a workspace, parsed for reading.

Reads files only. Nothing here runs analysis, calls a provider or changes a workspace.
Every page load runs this as its own process, so it imports only the standard library.
"""

import csv
import datetime
import decimal
import hashlib
import json
import os
import re
import stat
import sys
from collections import Counter
from collections.abc import Callable, Iterator
from pathlib import Path, PurePosixPath
from typing import Any, NamedTuple
from urllib.parse import quote

HERE = Path(__file__).resolve().parent
REPO = HERE if (HERE / "src").is_dir() else HERE.parents[2]
OUTPUT_SKIP = re.compile(r"instructions|prompt|calculations|verification")
INPUT_NAME = re.compile(r"selected-input|peer-inputs|delivery|-request\.md")
HANDOFF_NAME = re.compile(r"CP-[A-Z0-9]+")
OUTPUT_SEPARATORS = ("-", "_", ".", " ")
AEROSPACE = "Aerospace & defense"
# Reading labels written by hand. Route key: (folder under runs/, issuer, title, run label, sector, period).
CURATED_RUNS = {
    "tdg-002": (
        "tdg-002",
        "TransDigm Group",
        "TransDigm Group",
        "TDG-002",
        AEROSPACE,
        "FY2024 historical evidence · later events separately dated",
    ),
    "tdg-003": (
        "tdg-003",
        "TransDigm Group",
        "TransDigm Group",
        "TDG-003",
        AEROSPACE,
        "FY2024 and quarter ended 28 December 2024",
    ),
    "tdg-004": (
        "tdg-004",
        "TransDigm Group",
        "TransDigm Group",
        "TDG-004",
        AEROSPACE,
        "19 September 2024 indenture · 6% secured notes due 2033",
    ),
    "tdg-guidance": (
        "tdg-guidance-001",
        "TransDigm Group",
        "TransDigm Group",
        "TDG-GUIDANCE",
        AEROSPACE,
        "7 November 2024 guidance · FY2025 outlook",
    ),
    "tdg-peers-2024": (
        "tdg-peers-2024-001",
        "TransDigm Group",
        "TransDigm & peers",
        "TDG-PEERS-2024",
        AEROSPACE,
        "Each company’s own FY2024 · unmatched fiscal dates",
    ),
    "tdg-run-comparison": (
        "tdg-run-comparison-001",
        "TransDigm Group",
        "TransDigm Group",
        "TDG-RUN-COMPARISON",
        AEROSPACE,
        "Build 2 compared with build 6 · 30 September 2024 financial base",
    ),
    "ford-otosan-2024": (
        "ford-otosan-2024-001",
        "Ford Otosan",
        "Ford Otosan",
        "FORD-OTOSAN-2024",
        "Automotive",
        "11 April 2024 · historical case",
    ),
    "frontier-2020": (
        "frontier-2020-001",
        "Frontier",
        "Frontier",
        "FRONTIER-2020",
        "Telecommunications",
        "29 June 2020 disclosure · historical case",
    ),
}
# Build history recorded in README.md and VERIFICATION.md; builds 4-6 matched by diff.
CURATED_REPORTS = {
    "tdg-fy2024-snapshot": ("Initial snapshot · failed date presentation", "Superseded"),
    "tdg-fy2024-snapshot-2": ("Annual snapshot · reviewed", None),
    "tdg-fy2024-snapshot-3": ("Integrated · macro/ESG and conditional forecast", None),
    "tdg-fy2024-snapshot-4": ("Peer comparison · first delivery, gap rows dropped", None),
    "tdg-fy2024-snapshot-5": ("Peer comparison · gap boundary repaired", None),
    "tdg-fy2024-snapshot-6": ("Peer comparison · exact fiscal dates added", None),
    "tdg-fy2024-snapshot-7": ("Repairs from the deliverable comparison", "Latest build"),
}
SAFE_FOLDER = re.compile(r"[\w. -]+")
MONTHS = (
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
)
ISO_DATE = re.compile(r"\d{4}-\d{2}-\d{2}", re.ASCII)


def display_date(iso):
    """`31 December 2024` for a valid YYYY-MM-DD calendar date; any other text unchanged."""
    if not isinstance(iso, str) or not ISO_DATE.fullmatch(iso):
        return iso
    try:
        day = datetime.date.fromisoformat(iso)
    except ValueError:
        return iso
    return f"{day.day} {MONTHS[day.month - 1]} {day.year}"


WEB_RUN = re.compile(r"web-[a-f0-9]{32}")


READER_TABLES = [
    ["Bottom line", "Confidence", "Main limitation"],
    ["Finding", "Creditor impact", "Confidence"],
]
CHART_PREFIX = "Chart data: "
CHART_LAST_COLUMNS = ["Reporting unit", "Basis and limitation"]


def parse_source(text):
    """Keep every nonblank body line in one typed block with its source locator."""
    lines = text.splitlines()
    sections = []
    current = None
    i = 0
    while i < len(lines):
        line = lines[i]
        heading = re.match(r"^(#{1,4}) (.+)$", line)
        if heading:
            current = {"heading": heading[2], "level": len(heading[1]), "line": i + 1, "blocks": []}
            sections.append(current)
            i += 1
            continue
        if not line.strip():
            i += 1
            continue
        if re.fullmatch(r"<!-- table-id: [\w.-]+ -->", line):
            # A transport identifier, preserved in the downloadable original.
            i += 1
            continue
        if current is None:
            raise ValueError("Body before first heading")
        start = i + 1
        if line == "```text" and current["heading"].startswith("T4.4 —"):
            # The retained equity statement is a delimited transcription, not
            # prose. Its explicitly supplied column order governs this table.
            headers = [
                "Reported equity movement",
                "Common shares (individual)",
                "Common stock par",
                "APIC",
                "Accumulated deficit",
                "Accumulated other comprehensive loss",
                "Treasury shares (individual)",
                "Treasury stock value",
                "Noncontrolling interests",
                "Total",
            ]
            rows = []
            i += 1
            while i < len(lines) and lines[i] != "```":
                label, values = lines[i].split(":", 1)
                row = [label] + [c.strip() for c in values.split("|")]
                if len(row) != len(headers):
                    raise ValueError(f"Malformed equity transcription at {i + 1}")
                rows.append({"line": i + 1, "cells": row})
                i += 1
            if i == len(lines):
                raise ValueError("Unclosed equity transcription")
            current["blocks"].append(
                {
                    "type": "table",
                    "line": start,
                    "headers": headers,
                    "rows": rows,
                    "financial": True,
                }
            )
            i += 1
        elif (
            line.startswith("|")
            and i + 1 < len(lines)
            and re.fullmatch(r"\|[\s:|\-]+\|", lines[i + 1])
        ):

            def cells(value):
                return [c.strip() for c in re.split(r"(?<!\\)\|", value.strip().strip("|"))]

            headers = cells(line)
            i += 2
            rows = []
            while i < len(lines) and lines[i].startswith("|"):
                row = cells(lines[i])
                if len(row) != len(headers):
                    raise ValueError(f"Malformed table at line {i + 1}")
                rows.append({"line": i + 1, "cells": row})
                i += 1
            current["blocks"].append(
                {"type": "table", "line": start, "headers": headers, "rows": rows}
            )
        else:
            parts = [line]
            i += 1
            while (
                i < len(lines)
                and lines[i].strip()
                and not lines[i].startswith(("#", "|", "- ", "<!-- table-id:"))
                and not re.match(r"\d+\. ", lines[i])
            ):
                parts.append(lines[i])
                i += 1
            current["blocks"].append(
                {"type": "text", "line": start, "end": i, "text": "\n".join(parts)}
            )
    return sections


MODEL_FILE_LIMIT = 64 * 1024 * 1024  # The Go server's read cap for a delivered file.
CHUNK = 1024 * 1024


class UnreadableFile(OSError):
    """A path that is not a plain, bounded file: absent is OSError; this is everything else."""


def regular_chunks(
    path: str | Path, follow: bool = True, limit: int = MODEL_FILE_LIMIT
) -> Iterator[bytes]:
    """The bytes of a regular file of at most `limit` bytes, in chunks.

    The kind and size are read from the open descriptor, so a path swapped for a FIFO after a
    check is still refused; the open never blocks on a FIFO.
    """
    flags = os.O_RDONLY | getattr(os, "O_BINARY", 0) | getattr(os, "O_NONBLOCK", 0)
    if not follow:
        flags |= getattr(os, "O_NOFOLLOW", 0)
        if Path(path).is_symlink():
            raise UnreadableFile("a link")
    try:
        descriptor = os.open(path, flags)
    except ValueError as error:  # An embedded NUL.
        raise UnreadableFile("an invalid path") from error
    try:
        info = os.fstat(descriptor)
        if not stat.S_ISREG(info.st_mode):
            raise UnreadableFile("not a regular file")
        if info.st_size > limit:
            raise UnreadableFile("over the size limit")
        handle = os.fdopen(descriptor, "rb")
    except BaseException:
        os.close(descriptor)
        raise
    with handle:
        total = 0
        while chunk := handle.read(CHUNK):
            total += len(chunk)
            if total > limit:
                raise UnreadableFile("over the size limit")
            yield chunk


def sha256(path: Path) -> str:
    digest = hashlib.sha256()
    for chunk in regular_chunks(path):
        digest.update(chunk)
    return digest.hexdigest()


def listed_bytes(folder: Path, delivery: dict[str, Any], name: str) -> bytes | None:
    """The bytes of folder/name when it is a plain file, not a link, with the sha256 delivery.json lists; else None."""
    try:
        data = b"".join(regular_chunks(folder / name, follow=False))
    except (OSError, UnreadableFile):
        return None
    return data if hashlib.sha256(data).hexdigest() == delivery["files"][name] else None


def describe(error: BaseException) -> str:
    """An error as its type and a short reason; never the repr, which can hold file bytes."""
    if isinstance(error, UnicodeDecodeError):
        return f"UnicodeDecodeError: {error.reason}"
    return f"{type(error).__name__}: {str(error)[:80]}"


def locate_quote(sections, locator, owner):
    """Return a block's opening sentences verbatim, or fail the build."""
    for section in sections:
        if not section["heading"].startswith(locator["heading"]):
            continue
        for block in section["blocks"]:
            flat = re.sub(
                r"\s+", " ", block.get("text", "").replace("**", "").replace("`", "")
            ).strip()
            if flat.startswith(locator["startsWith"]):
                ends = [m.end() for m in re.finditer(r"[.!?](?:\*\*)?(?=\s|$)", block["text"])]
                text = block["text"][: ends[locator["sentences"] - 1]]
                if text.count("**") % 2:
                    raise ValueError(f"{owner}: quote {locator} cuts through bold text")
                return {"line": block["line"], "text": text}
    raise ValueError(f"{owner}: quote locator no longer matches {locator}")


def output_label(module: str, path: Path, siblings: list[Path]) -> tuple[str, int | None]:
    """Name a saved output from its file; a label never ranks it as accepted or primary."""
    rest = path.name.removeprefix(module).removesuffix(".md")
    # At most one separator follows the module code; a name with nothing else is its own label.
    stem = (rest[1:] if rest[:1] in OUTPUT_SEPARATORS else rest) or (path.name if rest else module)
    attempt = re.fullmatch(r"(?:(.+)-)?attempt-(\d+)", stem)
    if not attempt:
        repeated = sum(s.name == path.name for s in siblings) > 1
        delivered = repeated and path.parent.parent.name == "deliveries"
        return stem[0].upper() + stem[1:] + (
            f" · delivery {path.parent.name[:8]}" if delivered else ""
        ), None
    # Siblings in the same series share the file name up to "attempt-", taken literally.
    head = re.escape(path.name.removesuffix(f"attempt-{attempt[2]}.md"))
    total = sum(bool(re.fullmatch(rf"{head}attempt-\d+\.md", s.name)) for s in siblings)
    counted = f"attempt {attempt[2]} of {total}"
    return (f"{attempt[1].capitalize()} · {counted}" if attempt[1] else counted.capitalize()), int(
        attempt[2]
    )


def default_output(folder, sources, pinned, attempts):
    """Pinned file, else the only file, else the highest attempt; unnumbered variants pick none."""
    if pinned:
        return pinned
    if len(sources) == 1:
        return f"{folder}/{sources[0]}"
    numbered = [(attempts[s], s) for s in sources if attempts[s] is not None]
    return f"{folder}/{max(numbered)[1]}" if numbered else None


def locate_row(sections, locator, owner):
    """Return the retained table cell that states the output's unit, or fail the build."""
    for row in (row for s in sections for b in s["blocks"] for row in b.get("rows", [])):
        if row["cells"][0] == locator["row"]:
            if locator["unit"] not in row["cells"][1]:
                raise ValueError(
                    f"{owner}: basis row {locator['row']} does not state {locator['unit']}"
                )
            return {"line": row["line"], "text": row["cells"][1], "unit": locator["unit"]}
    raise ValueError(f"{owner}: basis locator no longer matches {locator}")


def pinned_fields(sections, config, module):
    """Curated fields of a pinned output; a locator that no longer matches fails the build."""
    fields = {
        "period": config["period"],
        "scope": config["scope"],
        "compare": config.get("compare"),
    }
    if "call" in config:
        fields["call"] = locate_quote(sections, config["call"], module)
    if "basis" in config:
        fields["basis"] = locate_row(sections, config["basis"], module)
    visual = config.get("visual")
    if visual:
        if not any(
            b["type"] == "table" and b["line"] == visual["table"]
            for s in sections
            for b in s["blocks"]
        ):
            raise ValueError(f"{module}: visual table locator no longer matches")
        quote = visual.get("noteQuote")
        fields["visual"] = (
            {**visual, "quote": locate_quote(sections, quote, module)} if quote else visual
        )
    return fields


def _reader_summary(section):
    """The section's values, or None when it does not hold its two tables."""
    tables = [b for b in section["blocks"] if b["type"] == "table"]
    if [t["headers"] for t in tables] != READER_TABLES:
        return None
    calls, findings = (t["rows"] for t in tables)
    if len(calls) != 1 or not findings or any(len(r["cells"]) != 3 for r in calls + findings):
        return None
    bottom_line, confidence, limitation = calls[0]["cells"]
    return {
        "bottomLine": bottom_line,
        "confidence": confidence,
        "limitation": limitation,
        "line": calls[0]["line"],
        "findings": [
            {
                "finding": r["cells"][0],
                "impact": r["cells"][1],
                "confidence": r["cells"][2],
                "line": r["line"],
            }
            for r in findings
        ],
    }


def _chart_table(section):
    """What the app needs to draw the section's table, or None when it is not the fixed shape."""
    tables = [b for b in section["blocks"] if b["type"] == "table"]
    if len(tables) != 1 or not tables[0]["rows"]:
        return None
    table = tables[0]
    headers = table["headers"]
    if len(headers) < 4 or headers[0] != "Period" or headers[-2:] != CHART_LAST_COLUMNS:
        return None
    return {
        "title": section["heading"].removeprefix(CHART_PREFIX).capitalize(),
        "unit": table["rows"][0]["cells"][-2],
        "table": table["line"],
        "columns": list(range(1, len(headers) - 2)),
    }


def reader_fields(sections):
    """A handoff's reader section and chart tables. A malformed one is named; the handoff still reads."""
    summary, charts, problems = None, [], []
    for section in sections:
        heading = section["heading"]
        if heading == "Reader summary":
            summary = _reader_summary(section)
            if summary is None:
                problems.append("Reader summary is not in its two tables")
        elif heading.startswith(CHART_PREFIX):
            chart = _chart_table(section)
            if chart:
                charts.append(chart)
            else:
                problems.append(f"{heading} is not in its fixed table")
    return {"summary": summary, "charts": charts, "issue": "; ".join(problems) or None}


def structured(raw: bytes, strict: bool) -> tuple[list[dict[str, Any]], str | None]:
    """Typed blocks. In the app a handoff the parser refuses stays readable as one flagged block.

    A UTF-8 byte-order mark, which Windows editors often write, is not part of the first heading.
    """
    try:
        return parse_source(raw.decode("utf-8-sig")), None  # type: ignore[no-untyped-call]  # legacy untyped parser
    except ValueError as error:
        if strict:
            raise
        text = raw.decode("utf-8-sig", "replace")
        block = {"type": "text", "line": 1, "end": text.count("\n") + 1, "text": text}
        return [{"heading": "Unstructured handoff", "level": 1, "line": 1, "blocks": [block]}], str(
            error
        )


def linked(folder: Path) -> bool:
    """A symbolic link or Windows junction: either can lead a folder out of its run."""
    return folder.is_symlink() or folder.is_junction()


class Handoff(NamedTuple):
    """One handoff file as read once: the parsed text and every hash shown come from these bytes."""

    module: str
    raw: bytes
    sha256: str


def handoff_files(run_dir: Path) -> dict[Path, Handoff]:
    """Handoffs at the run root, then those the launcher delivered; each distinct file once."""
    found: dict[Path, Handoff] = {}
    seen: set[str] = set()
    base = run_dir.resolve()
    for path in [*sorted(run_dir.glob("CP-*.md")), *sorted(run_dir.glob("deliveries/*/CP-*.md"))]:
        # The server serves regular files only, so a link out of the run is not a handoff either:
        # not a linked file, not a linked or junctioned delivery folder, nothing resolving outside.
        if (
            # Windows matches these patterns regardless of case; the names here do not.
            (match := HANDOFF_NAME.match(path.name))
            and path.name.endswith(".md")
            and not OUTPUT_SKIP.search(path.name)
            and path.is_file()
            and not path.is_symlink()
            and (path.parent == run_dir or not linked(path.parent))
            and path.resolve().is_relative_to(base)
        ):
            # Bounded: a handoff over the server's read cap raises, and the run is hidden and reported.
            raw = b"".join(regular_chunks(path))
            digest = hashlib.sha256(raw).hexdigest()
            if digest not in seen:
                seen.add(digest)
                found[path] = Handoff(match[0], raw, digest)
    return found


def collect_runs(
    root: Path,
    shown: dict[str, tuple[str, ...]],
    catalog: dict[str, Any],
    link: Callable[[str, str, str], str],
    strict: bool = True,
) -> tuple[
    dict[str, Any],
    dict[str, Any],
    dict[str, Any],
    dict[str, list[dict[str, Any]]],
    dict[str, str],
    list[str],
]:
    """Parse every saved output of every shown run; each file keeps its own identity."""
    runs: dict[str, Any] = {}
    outputs: dict[str, Any] = {}
    inputs: dict[str, Any] = {}
    sources: dict[str, list[dict[str, Any]]] = {}
    pins: dict[str, str] = {}
    issues: list[str] = []
    for key, (folder, issuer, title, label, sector, period) in shown.items():
        run_dir = root / "runs" / folder

        # The default binds this run's folder.
        def relative(path: Path, base: Path = run_dir) -> str:
            return path.relative_to(base).as_posix()

        grouped: dict[str, dict[str, list[Path]]] = {}
        read = handoff_files(run_dir)
        for path, handoff in read.items():
            kind = "inputs" if INPUT_NAME.search(path.name) else "outputs"
            grouped.setdefault(handoff.module, {"outputs": [], "inputs": []})[kind].append(path)
            sources.setdefault(handoff.sha256, []).append(
                {"run": key, "source": f"{folder}/{relative(path)}", "output": kind == "outputs"}
            )
        modules: dict[str, Any] = {}
        first: str | None = None
        for module, files in grouped.items():
            config = catalog.get(module, {})
            pinned: str | None = None
            labels = {
                relative(f): output_label(module, f, files["outputs"]) for f in files["outputs"]
            }
            for path in files["outputs"]:
                name = relative(path)
                output_id = f"{folder}/{name}"
                digest = read[path].sha256
                sections, problem = structured(read[path].raw, strict)
                record: dict[str, Any] = {
                    "id": output_id,
                    "run": key,
                    "module": module,
                    "source": name,
                    "file": f"{folder}--{name.replace('/', '--')}",
                    "href": link(folder, name, digest),
                    "label": labels[name][0],
                    "sha256": digest,
                    "case": f"{title} · {label}",
                    "period": period,
                    "scope": "Retained module output",
                    "firstHeading": config.get("firstHeading"),
                    "sections": sections,
                }
                record.update(reader_fields(sections))  # type: ignore[no-untyped-call]  # legacy untyped parser
                if record["issue"]:
                    issues.append(f"{output_id}: {record['issue']}")
                if problem:
                    record["parseError"] = problem
                    issues.append(f"{output_id}: shown unstructured ({problem})")
                if config.get("path") == output_id:
                    try:
                        record.update(pinned_fields(sections, config, module))  # type: ignore[no-untyped-call]  # legacy untyped parser
                        pins[module] = pinned = output_id
                        first = first or module
                    except (ValueError, KeyError, IndexError) as error:
                        if strict:
                            raise
                        issues.append(f"{module}: curated pin dropped: {error}")
                outputs[output_id] = record
            for path in files["inputs"]:
                name = relative(path)
                digest = read[path].sha256
                inputs[f"{folder}/{name}"] = {
                    "module": module,
                    "run": key,
                    "source": name,
                    "file": f"{folder}--{name.replace('/', '--')}",
                    "href": link(folder, name, digest),
                    "sha256": digest,
                }
            sources_here = [relative(f) for f in files["outputs"]]
            modules[module] = {
                "outputs": [f"{folder}/{s}" for s in sources_here],
                "inputs": [f"{folder}/{relative(f)}" for f in files["inputs"]],
                "default": default_output(  # type: ignore[no-untyped-call]  # legacy untyped helper
                    folder, sources_here, pinned, {s: labels[s][1] for s in sources_here}
                )
                if sources_here
                else None,
            }
        with_outputs = [module for module in modules if modules[module]["outputs"]]
        recorded = recorded_run(run_dir)
        runs[key] = {
            "folder": folder,
            "issuer": issuer,
            "title": title,
            "run": label,
            "sector": sector,
            "period": period,
            "pathway": recorded.get("pathway") or None,
            "asOf": recorded.get("as_of") or None,
            "first": first or (with_outputs[0] if with_outputs else "W-Overview"),
            "modules": modules,
        }
    return runs, outputs, inputs, sources, pins, issues


def built_from(
    files: dict[str, str], sources: dict[str, list[dict[str, Any]]]
) -> list[dict[str, Any]]:
    """Each handoff the verified delivery lists, traced to the run files holding the same bytes.

    The names and hashes are delivery.json's, which the server verified; a handoff-looking file
    beside the report that the delivery does not list was not verified and is not "built from".
    """
    rows = []
    for name, digest in sorted(files.items()):
        match = HANDOFF_NAME.match(name)
        if not match or not name.endswith(".md"):
            continue
        matches = sources.get(digest) or [{"run": None, "source": name, "output": False}]
        rows += [{"module": match[0], "sha256": digest, **found} for found in matches]
    return rows


def report_record(
    root: Path,
    folder: str,
    artifact: dict[str, Any],
    sources: dict[str, list[dict[str, Any]]],
    keys: dict[str, str],
) -> dict[str, Any]:
    """One verified deliverable as the app shows it; raises when its delivery cannot be read."""
    name = Path(folder).name
    delivery = json.loads((root / folder / "delivery.json").read_text(encoding="utf-8"))
    view = json.loads((root / folder / "view.json").read_text(encoding="utf-8"))
    identity = view["run"]
    issuer_name, as_of = identity["issuer_name"], identity["as_of"]
    issuer_key = report_issuer_key(keys, identity.get("issuer_id"))
    files = {str(n): str(h) for n, h in delivery["files"].items()}
    mode, qualification = view.get("mode"), view.get("analytical_qualification")
    # The hand-written labels describe the TransDigm builds under deliverables/; a folder of that
    # name elsewhere or for another issuer keeps the issuer its own view.json records.
    curated = (
        folder == f"deliverables/{name}"
        and name in CURATED_REPORTS
        and str(issuer_name).startswith("TransDigm Group")
    )
    issuer = "TransDigm Group" if curated else issuer_name
    if curated:
        label, status = CURATED_REPORTS[name]
    else:
        label = (
            artifact["label"]
            if artifact["label"] != name
            else f"{issuer} · as of {display_date(as_of)}"
        )
        status = "Superseded" if artifact.get("state") == "superseded" else None
    return {
        "id": name,
        "build": list(CURATED_REPORTS).index(name) + 1 if curated else None,
        "label": label,
        "status": status,
        "mode": mode if isinstance(mode, str) else None,
        "qualification": qualification if isinstance(qualification, str) else None,
        "issuer": issuer,
        "issuerKey": issuer_key,
        "sha256": files["report.html"],
        "scope": delivery.get("scope"),
        "modelPublished": delivery.get("cp_model_published", False),
        "href": artifact["href"] + "&embedded=1",
        "download": artifact["href"] + "&download=1",
        "files": [
            {"name": n, "href": f"/files/{quote(f'{folder}/{n}')}?sha256={h}&download=1"}
            for n, h in sorted(files.items())
        ],
        "builtFrom": built_from(files, sources),
    }


def catalogue_reports(
    root: Path,
    catalogue: dict[str, Any],
    sources: dict[str, list[dict[str, Any]]],
    keys: dict[str, str],
) -> tuple[list[dict[str, Any]], list[str]]:
    """Deliverables the server verified, each once, with what it was built from; keys maps issuer IDs to group keys."""
    reports, seen, issues = [], set(), []
    for run in catalogue["real"]:
        for artifact in run.get("artifacts") or []:
            folder = artifact["folder"]
            name = Path(folder).name
            if (
                not artifact.get("available")
                or artifact.get("kind", "report") != "report"
                or name in seen
            ):
                continue
            seen.add(name)
            # Documented fail-open: reported in Settings; the other deliverables stay readable.
            try:
                reports.append(report_record(root, folder, artifact, sources, keys))
            except (OSError, ValueError, KeyError, TypeError, AttributeError) as error:
                issues.append(f"{folder}: could not be read ({error!r})")
    return reports, issues


def register_of(sections):
    """The section whose heading names an assumption register: heading, intro text and table rows."""
    for section in sections:
        if "assumption register" not in section["heading"].casefold():
            continue
        text = next((b["text"] for b in section["blocks"] if b["type"] == "text"), None)
        table = next((b for b in section["blocks"] if b["type"] == "table"), None)
        return {
            "heading": section["heading"],
            "intro": text,
            "headers": table["headers"] if table else [],
            "rows": [row["cells"] for row in table["rows"]] if table else [],
        }
    return None


def text_or_none(value):
    return value if isinstance(value, str) else None


def source_location(root, path):
    """The file a model source names, only if it is runs/<folder>/<file> and resolves inside root."""
    if not isinstance(path, str) or "\\" in path or ":" in path:
        return None
    parts = PurePosixPath(path).parts
    if len(parts) < 3 or parts[0] != "runs" or PurePosixPath(path).is_absolute() or ".." in parts:
        return None
    try:
        resolved = (root / path).resolve()
    except (ValueError, OSError):  # An embedded NUL or an unresolvable path is an invalid source.
        return None
    return resolved if resolved.is_relative_to(root.resolve()) else None


def model_sources(root, delivery, outputs, folder=None, issues=None):
    """Each source a model declares, whether its file still has the declared bytes, and the run output holding them.

    A source whose path is not a confined runs/<folder>/<file> or whose hash is not 64 lowercase hex
    keeps its row with sha256 and changed null; its file is never opened. A source that is not a
    regular file of at most 64 MiB is likewise kept with nulls and named in the issues; an absent
    file stays "changed". The issues are appended to `issues`, prefixed with `folder`.
    """
    rows = []
    issues = [] if issues is None else issues
    declared_sources = delivery.get("sources")
    for role, source in (declared_sources if isinstance(declared_sources, dict) else {}).items():
        source = source if isinstance(source, dict) else {}
        path, declared = source.get("path"), source.get("sha256")
        location = source_location(root, path)
        valid = (
            location is not None
            and isinstance(declared, str)
            and re.fullmatch(r"[0-9a-f]{64}", declared) is not None
        )
        row = {
            "role": role,
            "path": path if isinstance(path, str) else None,
            "sha256": declared if valid else None,
            "changed": None,
            "run": None,
            "output": None,
        }
        if valid:
            try:
                row["changed"] = sha256(location) != declared
            except UnreadableFile:
                row["sha256"] = None
                issues.append(f"{folder}: source {role} is not a readable file")
            except OSError:
                row["changed"] = True
            held = outputs.get(path.removeprefix("runs/"))
            match = held if held and held["sha256"] == declared else None
            if match and row["sha256"] is not None:
                row["run"], row["output"] = match["run"], match["id"]
        else:
            issues.append(f"{folder}: source {role} has an invalid path or hash")
        rows.append(row)
    return rows


CASHFLOW_FILES = ("forecast_exact.json", "calculation.json", "annual.md", "quarter.md")
# The CP-1 handoff table labels the cash flow reader matches, exactly as the handoffs print them
# (TDG wording). To read another issuer's handoffs, add or change its labels here; nothing else in
# the reader names a handoff label. Matching is exact and case-sensitive except the debt register,
# which is matched case-insensitively (see secured_debt).
CASHFLOW_LABELS = {
    "revenue": "NET SALES",
    "cogs": "COST OF SALES",
    "gross_profit": "GROSS PROFIT",
    "selling_admin": "SELLING AND ADMINISTRATIVE EXPENSES",
    "amortization": "AMORTIZATION OF INTANGIBLE ASSETS",
    "operating_income": "INCOME FROM OPERATIONS",
    "segment_revenue": "Net Sales",
    "total_prefix": "Total",
    "da": "Depreciation and amortization expense",
    "issuer_ebitda": "EBITDA",
    "adjusted_ebitda": "Total Company EBITDA As Defined",
    "interest_net": "Interest expense-net",
    "pretax_income": "Income from continuing operations before income taxes",
    "secured_securitization": "Trade receivable securitization",
    "secured_term_loans": "Term loans aggregate",
    "secured_notes": "secured notes",
    "unsecured_notes": "subordinated",
    "unsecured": "unsecured",
    "label_header": "Label",
    "period_header": "Period",
    "period_end_header": "End",
}
# Inputs beyond these are refused before any cell is built (see CashflowLimit).
QUARTER_COLUMN_LIMIT = 40
FORECAST_YEAR_LIMIT = 20
FISCAL_YEAR_LIMIT = 20
UNIT_ROW_LIMIT = 200
ADD_BACK_ROW_LIMIT = 200
TABLE_ROW_LIMIT = 2000
QUARTER_DAYS = 100
QUARTER_LENGTH_SLACK = 7
FORECAST_CASES = (("REFERENCE", "Base case (reference illustration)"), ("DOWNSIDE", "Downside"))
NOT_HELD = "\u2014"
PRIOR_MISSING = "prior-year period not in the handoffs"
COMPONENT_MISSING = "a component is not in the handoffs"
REASON_PHRASES = {
    "NOT_SOURCED": "not reported in the source",
    "COMPONENT_MISSING": COMPONENT_MISSING,
}
LTM_NEEDED = "needs last-twelve-months Adj EBITDA, which the handoffs do not construct"
MONTHS_SHORT = {name[:3]: number for number, name in enumerate(MONTHS, 1)}
Q1_NOTE = "Q1 is the first quarter of the fiscal year, so it is also the year to date."
CASHFLOW_NOTES = (
    Q1_NOTE,
    "Pro forma: no pro forma period is recorded in the handoffs.",
    (
        "Base case is the model's reference case: a conditional illustration, not an "
        "evidence-supported central issuer forecast. The upside case stays in the calculation "
        "record and the published model."
    ),
    "n.m. \u2014 not modelled: the calculation record does not project this line.",
    (
        "EBITDA (EBIT + D&A) differs from the issuer's reported EBITDA, which also deducts "
        "refinancing costs and includes other income or expense."
    ),
    (
        "Adj EBITDA is the issuer's EBITDA As Defined, a non-GAAP measure; in the forecast it is "
        "the model's earnings on that basis, not issuer guidance."
    ),
    (
        "Leverage uses carrying debt including securitization; senior secured debt is the term "
        "loans, secured notes and securitization at carrying value. Ratios are shown for fiscal "
        "years only."
    ),
)
QUARTER_HEADER = re.compile(r"(\d{4}-\d{2}-\d{2})[–-](\d{4}-\d{2}-\d{2})", re.ASCII)
FISCAL_HEADER = re.compile(r"FY\d{4}", re.ASCII)
TABLE_NUMBER = re.compile(r"(\()?((?:\d{1,3}(?:,\d{3})+|\d+)(?:\.\d+)?)(\))?", re.ASCII)
SEPARATOR_CELL = re.compile(r":?-+:?")
CARRYING = re.compile(r"carrying\s+(\d[\d,]*(?:\.\d+)?)", re.ASCII)
REGISTER_DATE = re.compile(r"\b([A-Z][a-z]{2}) (\d{1,2}), (\d{4})\b", re.ASCII)


def display_amount(exact, kind):
    """An exact decimal string as the reader sees it: half-up, money in brackets when negative."""
    with decimal.localcontext(decimal.Context(prec=200)) as context:
        value = decimal.Decimal(exact)
        if not value.is_finite():
            raise ValueError(f"not a finite decimal: {exact!r}")
        if kind in ("percent", "multiple"):
            scaled = value * 100 if kind == "percent" else value
            two = scaled.quantize(decimal.Decimal("0.01"), decimal.ROUND_HALF_UP, context)
            if two == 0:
                two = abs(two)  # a negative that rounds to zero is not shown as -0.00
            return f"{two:,.2f}{'%' if kind == 'percent' else 'x'}"
        rounded = value.quantize(decimal.Decimal(1), decimal.ROUND_HALF_UP, context)
        if rounded == 0:
            return "0"  # a negative that rounds to zero is not shown as -0 or in brackets
        return f"({-rounded:,})" if rounded < 0 else f"{rounded:,}"


def cashflow_units(handoff):
    """The first '<ISO currency> millions|billions|thousands' phrase of the handoff's Request section."""
    request = re.search(
        r"^## Request[ \t]*\r?\n(.*?)(?=^## |\Z)", handoff, re.MULTILINE | re.DOTALL
    )
    phrase = (
        re.search(r"\b[A-Z]{3}\s+(?:millions|billions|thousands)\b", request.group(1))
        if request
        else None
    )
    return re.sub(r"\s+", " ", phrase.group(0)) if phrase else None


class CashflowLimit(Exception):
    """A cash flow input larger than the reader accepts; names the file and what was too large."""

    def __init__(self, file, what, found, limit):
        super().__init__(f"{file} exceeds the cash flow model's limits ({what}, {found} > {limit})")


def grid_cell(exact, display, reason=None, status="value"):
    """A cell. `status` is value, gap (a dash), na (not available) or nm (not modelled)."""
    return {"exact": exact, "display": display, "reason": reason, "status": status}


def amount_cell(exact, kind):
    return grid_cell(exact, display_amount(exact, kind))


def absent_cell():
    return grid_cell(None, NOT_HELD, None, "gap")


def unavailable_cell(reason):
    return grid_cell(None, "n.a.", reason, "na")


def not_modelled_cell():
    return grid_cell(None, "n.m.", "not modelled in the calculation record", "nm")


def held_cell(held, kind, negate=False):
    """A calculation record's {amount, reason}; an amount of null is n.a. with the record's reason."""
    exact = held["amount"]
    if exact is None:
        reason = held.get("reason")
        return unavailable_cell(
            REASON_PHRASES.get(reason, reason) if isinstance(reason, str) else None
        )
    if negate:
        value = decimal.Decimal(exact).copy_negate()
        exact = "0" if value == 0 else str(value)
    return amount_cell(exact, kind)


def checked_entries(record, skip=()):
    """Every entry of a calculation record (but `skip`) must be {amount: text|null, reason: text|null}."""
    for key, held in record.items():
        if key in skip:
            continue
        if not isinstance(held, dict) or not {"amount", "reason"} <= held.keys():
            raise TypeError(f"{key} is not an amount and a reason")
        exact, reason = held["amount"], held["reason"]
        if not (reason is None or isinstance(reason, str)):
            raise TypeError(f"the reason of {key} is not text")
        if exact is None:
            continue
        if not isinstance(exact, str) or len(exact) > 200:
            raise ValueError("an amount is not a decimal string")
        display_amount(exact, "money")  # a non-finite or out-of-range amount raises here
        display_amount(exact, "percent")


def source_cell(text, kind):
    """A Markdown table cell as the handoff printed it."""
    if text == "":
        return absent_cell()
    if text == NOT_HELD:
        return grid_cell(None, NOT_HELD, "printed as — in the source", "gap")
    found = TABLE_NUMBER.fullmatch(text) if len(text) <= 40 else None
    if found is None or bool(found.group(1)) != bool(found.group(3)):
        return unavailable_cell("source cell is not a number")
    digits = found.group(2).replace(",", "")
    negative = found.group(1) and decimal.Decimal(digits) != 0
    return amount_cell(f"-{digits}" if negative else digits, kind)


def table_cells(line):
    return [cell.strip() for cell in line.strip().removeprefix("|").removesuffix("|").split("|")]


def period_key(header):
    quarter = QUARTER_HEADER.fullmatch(header)
    if quarter:
        try:
            for part in quarter.groups():
                datetime.date.fromisoformat(part)
        except ValueError:
            return None
        return ("q",) + quarter.groups()
    return ("fy", header) if FISCAL_HEADER.fullmatch(header) else None


def markdown_table(lines, file):
    """One run of '|' lines: header, optional separator, rows. Rows are found by their label."""
    header = table_cells(lines[0])
    separated = len(lines) > 1 and all(SEPARATOR_CELL.fullmatch(c) for c in table_cells(lines[1]))
    if len(lines) - 1 - separated > TABLE_ROW_LIMIT:
        raise CashflowLimit(file, "table rows", len(lines) - 1 - separated, TABLE_ROW_LIMIT)
    body = [table_cells(line) for line in lines[1 + separated :]]
    label_header = CASHFLOW_LABELS["label_header"]
    label_column = header.index(label_header) if label_header in header else 0
    rows, repeated = {}, None
    for row in body:
        if label_column < len(row):
            if row[label_column] in rows and repeated is None:
                repeated = row[label_column]
            rows.setdefault(row[label_column], row)
    periods = {}
    for index, name in enumerate(header):
        key = period_key(name)
        if key is not None:
            periods.setdefault(key, index)
    return {"header": header, "rows": rows, "periods": periods, "repeated": repeated}


def markdown_tables(text, file):
    """The tables of a Markdown text, read line by line; `file` names it in a limit error."""
    tables, run = [], []
    for line in text.split("\n"):
        if line.lstrip().startswith("|"):
            run.append(line)
        elif run:
            tables.append(markdown_table(run, file))
            run = []
    if run:
        tables.append(markdown_table(run, file))
    return tables


def table_holding(tables, label):
    return next((table for table in tables if label in table["rows"]), None)


def table_cell(table, label, period, kind="money"):
    row = None if table is None else table["rows"].get(label)
    index = None if table is None else table["periods"].get(period)
    if row is None or index is None or index >= len(row):
        return absent_cell()
    return source_cell(row[index], kind)


def add_back_labels(table):
    """The rows between 'Interest expense-net' and the pre-tax income row of an As Defined bridge."""
    start = CASHFLOW_LABELS["interest_net"]
    if table is None or start not in table["rows"]:
        return []
    labels = list(table["rows"])
    labels = labels[labels.index(start) + 1 :]
    end = CASHFLOW_LABELS["pretax_income"]
    labels = labels[: labels.index(end)] if end in labels else labels
    return [label for label in labels if label]


def register_date(text):
    found = REGISTER_DATE.search(text)
    if found is None or found.group(1) not in MONTHS_SHORT:
        return None
    try:
        return datetime.date(int(found.group(3)), MONTHS_SHORT[found.group(1)], int(found.group(2)))
    except ValueError:
        return None


def secured_debt(tables):
    """(register date, secured carrying total, unclassified label) of the annual debt register, or None.

    Labels match case-insensitively. Secured: the securitization, the term loans aggregate, and
    secured notes. Unsecured: subordinated or unsecured notes. Total rows are subtotals. Any other row
    with a `carrying <n>` value cannot be classified: the total is then None and the label returned.
    None when the register date or a secured carrying value is missing.
    """
    names = CASHFLOW_LABELS
    anchor = names["secured_term_loans"].casefold()
    debt = next((t for t in tables if any(label.casefold() == anchor for label in t["rows"])), None)
    when = register_date(debt["header"][1]) if debt and len(debt["header"]) > 1 else None
    if when is None:
        return None
    required = {names["secured_securitization"].casefold(), names["secured_term_loans"].casefold()}
    secured_notes = re.compile(r"(?<![a-z])" + re.escape(names["secured_notes"]))
    total, named, incomplete, unclassified = decimal.Decimal(0), set(), False, None
    for label, row in debt["rows"].items():
        low = label.casefold()
        if low.startswith(names["total_prefix"].casefold()):
            continue
        unsecured = names["unsecured_notes"] in low or names["unsecured"] in low
        secured = low in required or (secured_notes.search(low) and not unsecured)
        carrying = CARRYING.search(row[1]) if len(row) > 1 and len(row[1]) <= 4000 else None
        if not secured:
            if carrying is not None and not unsecured and unclassified is None:
                unclassified = label[:200]
            continue
        if carrying is None:
            incomplete = True
            continue
        total += decimal.Decimal(carrying.group(1).replace(",", ""))
        named.add(low)
    if debt["repeated"] is not None:
        return (when, None, f"the debt register repeats a row label: {debt['repeated'][:200]}")
    if unclassified is not None:
        return (
            when,
            None,
            f"the debt register has a row that cannot be classified: {unclassified}",
        )
    return (when, total, None) if required <= named and not incomplete else None


def fiscal_year_ends(tables):
    """FY label -> ISO end date from the annual period register (headed Period ... End)."""
    names = CASHFLOW_LABELS
    period_name, end_name = names["period_header"], names["period_end_header"]
    register = next(
        (t for t in tables if period_name in t["header"] and end_name in t["header"]), None
    )
    if register is None:
        return {}
    period, end = register["header"].index(period_name), register["header"].index(end_name)
    return {
        row[period]: row[end]
        for row in register["rows"].values()
        if len(row) > max(period, end) and FISCAL_HEADER.fullmatch(row[period])
    }


def derive(kind, operands, compute):
    """A value computed from other cells under prec=28; n.m. or a gap in an operand carries through."""
    if any(operand["status"] == "nm" for operand in operands):
        return not_modelled_cell()
    if any(operand["exact"] is None for operand in operands):
        return unavailable_cell(COMPONENT_MISSING)
    try:
        with decimal.localcontext(decimal.Context(prec=28)):
            result = compute(*[decimal.Decimal(operand["exact"]) for operand in operands])
    except (decimal.DivisionByZero, decimal.InvalidOperation):
        return unavailable_cell("a divisor is zero")
    try:
        return amount_cell("0" if result == 0 else str(result), kind)
    except (ArithmeticError, ValueError):
        return unavailable_cell("the value cannot be displayed")


def forecast_inputs(exact):
    """(columns' source years by case, limits) of the forecast record; validated here."""
    cases = []
    for key, name in FORECAST_CASES:
        if key not in exact["outputs"]:
            continue
        years = exact["outputs"][key]["years"]
        if len(years) > FORECAST_YEAR_LIMIT:
            raise CashflowLimit(
                CASHFLOW_FILES[0], f"forecast years in {key}", len(years), FORECAST_YEAR_LIMIT
            )
        for year in years:
            if not isinstance(year["year"], int):
                raise TypeError("year is not a number")
            checked_entries(year, ("year", "planning_start", "planning_end"))
        cases.append((name, years))
    limits = exact["scope_limits"]
    if not isinstance(limits, list) or not all(isinstance(item, str) for item in limits):
        raise TypeError("scope_limits is not a list of text")
    return cases, limits


def fiscal_inputs(record):
    """[(fiscal year label, its values)] in the record's annual_periods order; validated here."""
    labels = record["annual_periods"]
    if not isinstance(labels, list) or not all(isinstance(label, str) for label in labels):
        raise TypeError("annual_periods is not a list of text")
    if len(labels) > FISCAL_YEAR_LIMIT:
        raise CashflowLimit(CASHFLOW_FILES[1], "fiscal years", len(labels), FISCAL_YEAR_LIMIT)
    years = []
    for label in labels:
        values = record["values"][label]
        checked_entries(values)
        years.append((label, values))
    return years


def span_days(start, end):
    return (datetime.date.fromisoformat(end) - datetime.date.fromisoformat(start)).days


def quarter_numbers(quarters, ends):
    """Per quarter, the fiscal year it opens (as Q1) or None.

    A quarter opens fiscal year N+1 when it spans at most QUARTER_DAYS days and starts the day after
    the end the period register records for FY N. Anything else is not Q1 and not year to date.
    """
    openings = {}
    for label, end in (ends or {}).items():
        try:
            day = datetime.date.fromisoformat(end) + datetime.timedelta(days=1)
            openings.setdefault(day, int(label.removeprefix("FY")) + 1)
        except (ValueError, OverflowError):
            continue  # a register row with an unreadable end opens no fiscal year
    numbers, longest = [], {}
    for index, (start, end) in enumerate(quarters):
        days = span_days(start, end)
        number = (
            openings.get(datetime.date.fromisoformat(start)) if 0 <= days <= QUARTER_DAYS else None
        )
        numbers.append(number)
        if number is not None and days > longest.get(number, (-1, 0))[0]:
            longest[number] = (days, index)
    # One Q1 per fiscal year: the longest span; the other candidates are plain date ranges.
    return [
        number if number is not None and longest[number][1] == index else None
        for index, number in enumerate(numbers)
    ]


def cashflow_columns(quarters, fiscal, cases, ends=None):
    """Quarter, fiscal-year and forecast columns, each with its prior-year column's index.

    The prior of Q1 FY<n> is Q1 FY<n-1>; other quarters have none. The prior of FY<n> is FY<n-1>, of the
    first forecast year the fiscal year before it, of a later forecast year the same case's year before
    it; a prior that is not the adjacent year is None.
    """
    columns = []

    def add(label, group, kind, record, start, end, period, prior, ytd=False):
        columns.append(
            {
                "label": label,
                "group": group,
                "kind": kind,
                "record": record,
                "start": start,
                "end": end,
                "period": period,
                "prior": prior,
                "ytd": ytd,
            }
        )

    numbers = quarter_numbers(quarters, ends)
    first_quarter = {}
    for index, number in enumerate(numbers):
        if number is not None:
            first_quarter.setdefault(number, index)
    for (start, end), number in zip(quarters, numbers, strict=True):
        label = f"{start}–{end}" if number is None else f"Q1 FY{number} (YTD)"
        prior = None if number is None else first_quarter.get(number - 1)
        add(label, "Quarter", "q", None, start, end, ("q", start, end), prior, number is not None)
        if prior is not None and abs(span_days(start, end) - span_days(*quarters[prior])) > (
            QUARTER_LENGTH_SLACK
        ):
            columns[-1]["length_differs"] = True
    fiscal_index = {}
    for label, values in fiscal:
        found = FISCAL_HEADER.fullmatch(label)
        prior = fiscal_index.get(f"FY{int(label[2:]) - 1}") if found else None
        add(label, "Fiscal year", "fy", values, None, None, ("fy", label), prior)
        fiscal_index.setdefault(label, len(columns) - 1)
    for name, years in cases:
        case_index = {}
        for year in years:
            prior = case_index.get(year["year"] - 1)
            if prior is None and not case_index:
                prior = fiscal_index.get(f"FY{year['year'] - 1}")
            add(
                f"FY{year['year']}E",
                name,
                "fc",
                year,
                text_or_none(year.get("planning_start")),
                text_or_none(year.get("planning_end")),
                None,
                prior,
            )
            case_index.setdefault(year["year"], len(columns) - 1)
    return columns


def add_cells(cells, kind="money"):
    return derive(kind, cells, lambda a, b: a + b)


def op_table(ctx, column, index, grid, kind, name, label):
    return table_cell(ctx["tables"][name], label, column["period"], kind)


def op_table_sum(ctx, column, index, grid, kind, name, first, second):
    table = ctx["tables"][name]
    cells = [table_cell(table, label, column["period"], kind) for label in (first, second)]
    return add_cells(cells, kind)


def op_key(ctx, column, index, grid, kind, key, negate=False):
    forecast = column["kind"] == "fc"
    missing = not_modelled_cell if forecast else absent_cell
    record = column["record"]
    return held_cell(record[key], kind, negate) if key in record else missing()


def op_sum(ctx, column, index, grid, kind, *rows):
    return add_cells([grid[row][index] for row in rows], kind)


def op_growth(ctx, column, index, grid, kind, source):
    """YoY growth of an earlier row against the same row in the column's prior-year column."""
    current = grid[source][index]
    if current["status"] == "nm":
        return not_modelled_cell()
    if column["prior"] is None:
        return unavailable_cell(PRIOR_MISSING)
    if column.get("length_differs"):
        return unavailable_cell("the prior-year period has a different length")
    return derive("percent", [current, grid[source][column["prior"]]], lambda a, b: a / b - 1)


def op_margin(ctx, column, index, grid, kind, source):
    return derive("percent", [grid[source][index], grid["revenue"][index]], lambda a, b: a / b)


def op_needs_ltm(ctx, column, index, grid, kind):
    return unavailable_cell(LTM_NEEDED)


def op_senior(ctx, column, index, grid, kind):
    """Secured carrying values over Adj EBITDA, for the fiscal year ending on the register date only."""
    if ctx["secured"] is None:
        return unavailable_cell(COMPONENT_MISSING)
    when, total, problem = ctx["secured"]
    if ctx["ends"].get(column["label"]) != when.isoformat():
        return unavailable_cell(
            f"secured-debt carrying values are recorded only at {display_date(when.isoformat())}"
        )
    if problem is not None:
        return unavailable_cell(problem)
    return derive("multiple", [grid["adj"][index]], lambda a: total / a)


CELL_OPS = {
    "table": op_table,
    "table-sum": op_table_sum,
    "key": op_key,
    "sum": op_sum,
    "growth": op_growth,
    "margin": op_margin,
    "ltm": op_needs_ltm,
    "senior": op_senior,
}


def spec_cell(spec, ctx, column, index, grid, kind):
    """One cell from its row's spec for the column's kind (None: a dash for history, n.m. in forecast)."""
    if spec is None:
        return not_modelled_cell() if column["kind"] == "fc" else absent_cell()
    return CELL_OPS[spec[0]](ctx, column, index, grid, kind, *spec[1:])


def every(spec):
    return (spec, spec, spec)


# Rows as data: (id, band, label, kind, quarter spec, fiscal-year spec, forecast spec).
INCOME = "Profitability"
HEAD_ROWS = (
    (
        "revenue",
        "Revenue",
        "Revenue",
        "money",
        ("table", "income", CASHFLOW_LABELS["revenue"]),
        ("key", "revenue"),
        ("key", "revenue"),
    ),
    ("revenue-growth", "Revenue", "Revenue YoY growth", "percent", *every(("growth", "revenue"))),
    (
        "cogs",
        INCOME,
        "COGS (cost of sales)",
        "money",
        ("table", "income", CASHFLOW_LABELS["cogs"]),
        ("key", "cogs"),
        None,
    ),
    (
        "gp",
        INCOME,
        "Gross profit",
        "money",
        ("table", "income", CASHFLOW_LABELS["gross_profit"]),
        ("key", "gross_profit"),
        None,
    ),
    ("gp-margin", INCOME, "Gross profit margin", "percent", *every(("margin", "gp"))),
    (
        "opex",
        INCOME,
        "Opex (selling and administrative, amortization of intangibles)",
        "money",
        (
            "table-sum",
            "income",
            CASHFLOW_LABELS["selling_admin"],
            CASHFLOW_LABELS["amortization"],
        ),
        ("key", "opex_magnitude"),
        None,
    ),
    (
        "ebit",
        INCOME,
        "EBIT (income from operations)",
        "money",
        ("table", "income", CASHFLOW_LABELS["operating_income"]),
        ("key", "ebit_reported"),
        None,
    ),
    (
        "da",
        INCOME,
        "D&A (depreciation and amortization)",
        "money",
        ("table", "bridge", CASHFLOW_LABELS["da"]),
        ("key", "cash_flow_DA"),
        None,
    ),
    (
        "ebitda",
        INCOME,
        "EBITDA (EBIT + D&A)",
        "money",
        ("sum", "ebit", "da"),
        ("key", "operating_ebitda"),
        None,
    ),
    (
        "issuer",
        INCOME,
        "Issuer EBITDA (reported)",
        "money",
        ("table", "bridge", CASHFLOW_LABELS["issuer_ebitda"]),
        ("key", "issuer_ordinary_ebitda"),
        None,
    ),
)
ADJUSTED = "Adjusted EBITDA"
PROXY = "Earnings to cash proxy"
CASH = "Cash and liquidity"
DEBT = "Debt"
CREDIT = "Credit metrics"
TAIL_ROWS = (
    ("adj", ADJUSTED, "Adj EBITDA (EBITDA As Defined)", "money", ("table", "qdef", CASHFLOW_LABELS["adjusted_ebitda"]), ("key", "issuer_as_defined"), ("key", "ebitda")),
    ("adj-margin", ADJUSTED, "Adj EBITDA margin", "percent", *every(("margin", "adj"))),
    ("adj-growth", ADJUSTED, "Adj EBITDA YoY growth", "percent", *every(("growth", "adj"))),
    ("interest", PROXY, "Cash interest", "money", None, ("key", "interest_cash"), ("key", "interest")),
    ("tax", PROXY, "Cash taxes", "money", None, ("key", "tax_cash"), None),
    ("tax-wc", PROXY, "Cash taxes and working capital, combined", "money", None, None, ("key", "tax_wc")),
    ("cfo", PROXY, "Model cash from operations", "money", None, None, ("key", "cfo")),
    ("capex", PROXY, "Capital expenditure (outflow)", "money", None, ("key", "capex_signed", True), ("key", "capex")),
    ("fcf", PROXY, "Cash proxy (not issuer free cash flow)", "money", None, None, ("key", "fcf")),
    ("dividends", CASH, "Distributions", "money", None, None, ("key", "dividends")),
    ("repayment", CASH, "Debt repayment", "money", None, None, ("key", "repayment")),
    ("opening-cash", CASH, "Opening cash", "money", None, None, ("key", "opening_cash")),
    ("closing-cash", CASH, "Closing cash", "money", None, ("key", "cash"), ("key", "closing_cash")),
    ("undrawn", CASH, "Undrawn facility", "money", None, None, ("key", "undrawn")),
    ("liquidity", CASH, "Accessible liquidity", "money", None, None, ("key", "liquidity")),
    ("opening-debt", DEBT, "Opening debt", "money", None, None, ("key", "opening_debt")),
    ("closing-debt", DEBT, "Closing debt (carrying value)", "money", None, ("key", "carrying_debt"), ("key", "closing_debt")),
    ("net-debt", DEBT, "Net debt (all modelled cash deducted)", "money", None, ("key", "net_carrying_debt"), ("key", "net_debt")),
    ("senior", CREDIT, "Senior secured leverage (secured debt / Adj EBITDA)", "multiple", ("ltm",), ("senior",), None),
    ("total-leverage", CREDIT, "Total leverage (debt / Adj EBITDA)", "multiple", ("ltm",), ("key", "gross_carrying_multiple"), ("key", "total_leverage")),
    ("net-leverage", CREDIT, "Net leverage (net debt / Adj EBITDA)", "multiple", ("ltm",), ("key", "net_carrying_multiple"), ("key", "net_leverage")),
    ("coverage", CREDIT, "Interest coverage (Adj EBITDA / cash interest)", "multiple", None, ("key", "issuer_earnings_cash_interest"), ("key", "coverage")),
    ("cash-to-debt", CREDIT, "Cash proxy / closing debt", "percent", None, None, ("key", "fcf_to_debt")),
)  # fmt: skip


def capped(found, what, limit, file):
    if len(found) > limit:
        raise CashflowLimit(file, what, len(found), limit)


def listed_labels(tables):
    """Business units (rows `Total <unit>`) of the annual then the quarter segment table, in order."""
    units = {}
    prefix = CASHFLOW_LABELS["total_prefix"] + " "
    for name, file in (("aseg", CASHFLOW_FILES[2]), ("qseg", CASHFLOW_FILES[3])):
        table = tables[name]
        for label in () if table is None else table["rows"]:
            if label.startswith(prefix) and label.removeprefix(prefix):
                units.setdefault(label.removeprefix(prefix))
        capped(units, "business-unit rows", UNIT_ROW_LIMIT, file)
    return list(units)


def listed_add_backs(tables):
    """The annual add-back labels in order, then any quarter-only label."""
    labels = dict.fromkeys(add_back_labels(tables["adef"]))
    capped(labels, "add-back rows", ADD_BACK_ROW_LIMIT, CASHFLOW_FILES[2])
    labels.update(dict.fromkeys(add_back_labels(tables["qdef"])))
    capped(labels, "add-back rows", ADD_BACK_ROW_LIMIT, CASHFLOW_FILES[3])
    return list(labels)


def cashflow_rows(tables):
    """The grid's rows in presentation order: units, the fixed head, add-backs, the fixed tail."""
    rows = []
    for unit in listed_labels(tables):
        total = f"{CASHFLOW_LABELS['total_prefix']} {unit}"
        rows.append(
            (
                ("unit", unit),
                "Revenue",
                unit,
                "money",
                ("table", "qseg", total),
                ("table", "aseg", total),
                None,
            )
        )
        rows.append(
            (
                ("growth", unit),
                "Revenue",
                f"{unit} YoY growth",
                "percent",
                *every(("growth", ("unit", unit))),
            )
        )
    rows.extend(HEAD_ROWS)
    for label in listed_add_backs(tables):
        rows.append(
            (
                ("add-back", label),
                "Add-backs to issuer EBITDA",
                label,
                "money",
                ("table", "qdef", label),
                ("table", "adef", label),
                None,
            )
        )
    return rows + list(TAIL_ROWS)


def cashflow_of(forecast, fiscal, annual, quarter, handoff):
    """History from the parsed annual and quarter tables and the forecast record, laid out as a grid."""
    cases, limits = forecast
    names = CASHFLOW_LABELS
    tables = {
        "income": table_holding(quarter, names["cogs"]),
        "qseg": table_holding(quarter, names["segment_revenue"]),
        "aseg": table_holding(annual, names["segment_revenue"]),
        "bridge": table_holding(quarter, names["issuer_ebitda"]),
        "qdef": table_holding(quarter, names["adjusted_ebitda"]),
        "adef": table_holding(annual, names["adjusted_ebitda"]),
    }
    ends = fiscal_year_ends(annual)
    ctx = {"tables": tables, "secured": secured_debt(annual), "ends": ends}
    income = tables["income"]
    periods = sorted({key[1:] for key in income["periods"] if key[0] == "q"}) if income else []
    capped(periods, "quarter columns", QUARTER_COLUMN_LIMIT, CASHFLOW_FILES[3])
    layout = cashflow_rows(tables)
    columns = cashflow_columns(periods, fiscal, cases, ends)
    grid, rows = {}, []
    for key, band, label, kind, *specs in layout:
        pick = {"q": specs[0], "fy": specs[1], "fc": specs[2]}
        grid[key] = [
            spec_cell(pick[column["kind"]], ctx, column, index, grid, kind)
            for index, column in enumerate(columns)
        ]
        rows.append({"band": band, "label": label, "cells": grid[key]})
    year_to_date = any(column["ytd"] for column in columns)
    return {
        "units": cashflow_units(handoff) if handoff is not None else None,
        "columns": [
            {key: column[key] for key in ("label", "group", "start", "end", "ytd")}
            for column in columns
        ],
        "rows": rows,
        "notes": [note for note in CASHFLOW_NOTES if year_to_date or note != Q1_NOTE],
        "limits": limits,
    }


# Errors a malformed input file or layout can raise; each is reported, never allowed to end the store.
CASHFLOW_ERRORS = (
    OSError,
    ValueError,
    KeyError,
    TypeError,
    AttributeError,
    IndexError,
    ArithmeticError,
    RecursionError,
    MemoryError,
)


def read_cashflow(files, handoff):
    """(grid, None), or (None, (kind, text)): kind "file" (text: the input that cannot be read), "limit"
    (text: the limit message) or "layout" (text: describe(error) of the failure while laying out).

    Documented fail-open: an input the reader cannot read or lay out leaves the model listed with no
    grid and a Workspace issue naming the file or the cause. A model too large to parse (MemoryError) or
    nested too deep (RecursionError) is reported the same way, not allowed to end the store.
    """
    stage = CASHFLOW_FILES[0]
    try:
        forecast = forecast_inputs(json.loads(files[stage].decode("utf-8")))
        stage = CASHFLOW_FILES[1]
        fiscal = fiscal_inputs(json.loads(files[stage].decode("utf-8")))
        stage = CASHFLOW_FILES[2]
        annual = markdown_tables(files[stage].decode("utf-8"), stage)
        stage = CASHFLOW_FILES[3]
        quarter = markdown_tables(files[stage].decode("utf-8"), stage)
    except CashflowLimit as error:
        return None, ("limit", str(error))
    except CASHFLOW_ERRORS:
        return None, ("file", stage)
    try:
        return cashflow_of(forecast, fiscal, annual, quarter, handoff), None
    except CashflowLimit as error:
        return None, ("limit", str(error))
    except CASHFLOW_ERRORS as error:
        return None, ("layout", describe(error))


def cashflow_or_issues(folder, files, inputs, handoff, issues):
    """The model's cash flow grid, or None with one issue for each of the four files that is not usable."""
    for name in CASHFLOW_FILES:
        if inputs[name] is not None:
            continue
        what = "does not match its delivery record" if name in files else "is missing or unreadable"
        issues.append(f"{folder}: {name} {what}")
    if any(inputs[name] is None for name in CASHFLOW_FILES):
        return None
    cashflow, problem = read_cashflow(inputs, handoff)
    if problem is not None:
        kind, text = problem
        issues.append(
            {
                "file": f"{folder}: {text} is missing or unreadable",
                "limit": f"{folder}: {text}",
                "layout": f"{folder}: the cash flow model could not be laid out ({text})",
            }[kind]
        )
    return cashflow


def shown_models(root, catalogue):
    """The one available model folder shown per name (the route id), and the issues naming the others.

    A folder is listed once however many runs list it. When folders share a name, the run's own delivery
    (runs/<run_id>/deliveries/<name>, its view.json recording that run) is kept, else the first by path; each
    dropped folder is named in an issue that says which one is shown. Only the kept folder is read in full.
    """
    by_name: dict[str, list[str]] = {}
    for run in catalogue["real"]:
        for artifact in run.get("artifacts") or []:
            folder = artifact["folder"]
            if artifact.get("available") and artifact.get("kind") == "model":
                names = by_name.setdefault(Path(folder).name, [])
                if folder not in names:
                    names.append(folder)

    def own(folder):
        parts = PurePosixPath(folder).parts
        if len(parts) != 4 or parts[0] != "runs" or parts[2] != "deliveries":
            return False
        # Documented fail-open: an unreadable view.json means "not known to be the run's own"; the model
        # read in catalogue_models reports the same failure as a Workspace issue.
        try:
            recorded = json.loads((root / folder / "view.json").read_text(encoding="utf-8"))["run"][
                "run_id"
            ]
        except (
            OSError,
            ValueError,
            KeyError,
            TypeError,
            AttributeError,
            RecursionError,
            MemoryError,
        ):
            return False
        return recorded == parts[1]

    shown: set[str] = set()
    issues: list[str] = []
    for name, folders in by_name.items():
        kept = next((f for f in folders if own(f)), None) or min(folders)
        shown.add(kept)
        issues.extend(
            f"{f}: another published model has the same name {name}; {kept} is shown"
            for f in sorted(folders)
            if f != kept
        )
    return shown, issues


def catalogue_models(root, catalogue, outputs, keys):
    """Published models the server verified, each once, with why it was built and what it was built from."""
    models, done = [], set()
    shown, issues = shown_models(root, catalogue)
    for run in catalogue["real"]:
        for artifact in run.get("artifacts") or []:
            folder = artifact["folder"]
            name = Path(folder).name
            if not artifact.get("available") or artifact.get("kind") != "model":
                continue
            if folder not in shown or folder in done:
                continue
            done.add(folder)
            # Documented fail-open: reported in Settings; the other models stay readable. A model too
            # large to parse (MemoryError) is reported the same way, not allowed to end the store.
            try:
                delivery = json.loads((root / folder / "delivery.json").read_text(encoding="utf-8"))
                view = json.loads((root / folder / "view.json").read_text(encoding="utf-8"))
                identity = view["run"]
                run_id = identity["run_id"]
                issuer_key = report_issuer_key(keys, identity.get("issuer_id"))
                sources = model_sources(root, delivery, outputs, folder, issues)
                register = handoff_text = None
                files = delivery["files"]
                if not isinstance(files, dict):
                    raise TypeError("files is not an object")
                if "forecast.md" in files:
                    handoff = listed_bytes(root / folder, delivery, "forecast.md")
                    if handoff is None:
                        issues.append(f"{folder}: forecast.md does not match its delivery record")
                    else:
                        handoff_text = handoff.decode("utf-8")
                        register = register_of(parse_source(handoff_text))
                inputs = {
                    name: listed_bytes(root / folder, delivery, name) if name in files else None
                    for name in CASHFLOW_FILES
                }
                previous = delivery.get("previous_directory")
            except (
                OSError,
                ValueError,
                KeyError,
                TypeError,
                AttributeError,
                RecursionError,
                MemoryError,
            ) as error:
                issues.append(f"{folder}: could not be read ({describe(error)})")
                continue
            cashflow = cashflow_or_issues(folder, files, inputs, handoff_text, issues)
            mode, qualification = view.get("mode"), view.get("analytical_qualification")
            models.append(
                {
                    "id": name,
                    "issuerKey": issuer_key,
                    "mode": mode if isinstance(mode, str) else None,
                    "qualification": qualification if isinstance(qualification, str) else None,
                    "runId": run_id if isinstance(run_id, str) else None,
                    "scope": text_or_none(delivery.get("scope")),
                    "inputContract": text_or_none(delivery.get("input_contract")),
                    "revisionNote": text_or_none(delivery.get("presentation_repair")),
                    "previous": Path(previous).name if isinstance(previous, str) else None,
                    "href": artifact["href"] + "&embedded=1",
                    "download": artifact["href"] + "&download=1",
                    "files": [
                        {
                            "name": n,
                            "href": f"/files/{quote(f'{folder}/{n}')}?sha256={h}&download=1",
                        }
                        for n, h in sorted(files.items())
                    ],
                    "sources": sources,
                    "register": register,
                    "cashflow": cashflow,
                }
            )
    return models, issues


def visual_catalogue() -> list[dict[str, str]]:
    with (REPO / "docs/visualisations/catalogue.csv").open(encoding="utf-8-sig") as source:
        return list(csv.DictReader(source))


def recorded_run(run_dir: Path) -> dict[str, str]:
    """The text fields of the launcher's own manifest; a run without a readable one records none."""
    try:
        manifest = json.loads((run_dir / "workflow.json").read_text(encoding="utf-8"))
        return {key: value for key, value in manifest["run"].items() if isinstance(value, str)}
    except (OSError, ValueError, KeyError, TypeError, AttributeError):
        return {}


def delivery_identities(root, catalogue):
    """What each available (hash-verified) deliverable says about its own run and issuer.

    A deliverable whose view.json cannot be read is skipped here; catalogue_reports names it in
    Workspace issues, so the failure is reported once and no run takes an identity from it.
    """
    found, seen = [], set()
    for run in catalogue["real"]:
        for artifact in run.get("artifacts") or []:
            folder = artifact["folder"]
            if not artifact.get("available") or folder in seen:
                continue
            seen.add(folder)
            try:
                identity = json.loads((root / folder / "view.json").read_text(encoding="utf-8"))[
                    "run"
                ]
                run_id, name = identity["run_id"], identity["issuer_name"]
                issuer_id = identity.get("issuer_id") or None
            except (
                OSError,
                ValueError,
                KeyError,
                TypeError,
                AttributeError,
                RecursionError,
                MemoryError,
            ):
                continue
            if isinstance(run_id, str) and isinstance(name, str) and name:
                valid_id = issuer_id if isinstance(issuer_id, str) else None
                found.append(
                    {"folder": folder, "run_id": run_id, "issuer_id": valid_id, "issuer_name": name}
                )
    return sorted(found, key=lambda item: item["folder"])


def recorded_identity(run_dir, run, curated_name, delivered):
    """A run's recorded issuer (name, ID) and, if its deliverables disagree, the issue to report.

    Name: curated, else the launcher manifest, else a catalogue name unlike the folder, else what
    its deliverables agree on. ID: manifest, else the catalogue's issuer, else the deliverables'.
    """
    manifest = recorded_run(run_dir)
    name = (
        curated_name
        or manifest.get("issuer_name")
        or (run["name"] if run["name"] != run["id"] else None)
    )
    seeded = run.get("issuer")
    issuer_id = manifest.get("issuer_id") or (seeded if seeded != "Unclassified" else None)
    if name:
        return name, issuer_id, None
    said = {}
    # In folder order, so the first deliverable's spelling of the ID is kept.
    for item in delivered:
        said.setdefault(((item["issuer_id"] or "").casefold(), item["issuer_name"]), item)
    if len(said) > 1:
        return None, issuer_id, "deliverables name different issuers; issuer left unrecorded"
    if said:
        (agreed,) = said.values()
        return agreed["issuer_name"], issuer_id or agreed["issuer_id"], None
    return None, issuer_id, None


def issuer_groups(recorded):
    """Group runs by issuer. recorded maps run key to (name or None, ID or None).

    Runs with a name join when they share a case-folded ID or an exact name, transitively. Returns
    the identity fields of every run and a map from each case-folded ID to its group's key.
    """
    named = {key: pair for key, pair in recorded.items() if pair[0]}
    parent = {key: key for key in named}

    def root_of(key):
        while parent[key] != key:
            parent[key] = parent[parent[key]]
            key = parent[key]
        return key

    first = {}
    for key, (name, issuer_id) in named.items():
        for token in [("name", name), *([("id", issuer_id.casefold())] if issuer_id else [])]:
            parent[root_of(key)] = root_of(first.setdefault(token, key))
    members = {}
    for key in named:
        members.setdefault(root_of(key), []).append(key)
    fields = {
        key: {"issuerKey": None, "issuerHeading": None, "issuerTerms": []} for key in recorded
    }
    keys = {}
    for group in members.values():
        names = Counter(named[key][0] for key in group)
        heading = min(names, key=lambda name: (-names[name], name.casefold(), name))
        ids = {named[key][1] for key in group if named[key][1]}
        folded = {issuer_id.casefold() for issuer_id in ids}
        group_key = f"id:{min(folded)}" if folded else f"name:{heading}"
        keys |= dict.fromkeys(folded, group_key)
        for key in group:
            fields[key] = {
                "issuerKey": group_key,
                "issuerHeading": heading,
                "issuerTerms": sorted({*names, *ids}),
            }
    return fields, keys


def report_issuer_key(keys, issuer_id):
    """The key of the group holding a report's issuer ID, or one built from that ID alone."""
    if not isinstance(issuer_id, str) or not issuer_id:
        return None
    return keys.get(issuer_id.casefold(), f"id:{issuer_id.casefold()}")


def run_row(root: Path, run: dict[str, Any], name: str | None = None) -> tuple[str, ...]:
    """Labels for a run with no curated ones: the launcher's own manifest, else the catalogue."""
    folder = run["id"]
    identity = recorded_run(root / "runs" / folder)
    issuer = name or identity.get("issuer_name") or run["name"]
    period = (
        f"As of {display_date(identity['as_of'])}"
        if identity.get("as_of")
        else run.get("period") or "Period not recorded"
    )
    # A web run's folder is 32 hex characters; eight are enough to tell runs apart on screen.
    label = folder.upper()[:12] if WEB_RUN.fullmatch(folder) else folder.upper()
    return (folder, issuer, issuer, label, run.get("sector") or "Unclassified", period)


def workspace_store(root: str | Path, catalogue: dict[str, Any]) -> dict[str, Any]:
    """Everything the app reads. A curated pin that stopped matching is dropped, not fatal."""
    root = Path(root)
    catalog = json.loads((HERE / "catalog.json").read_text(encoding="utf-8"))
    curated = {row[0]: (key, row) for key, row in CURATED_RUNS.items()}
    shown: dict[str, tuple[str, ...]] = {}
    issues = list(catalogue.get("issues") or [])
    recorded: dict[str, tuple[str | None, str | None]] = {}
    delivered: dict[str, list[dict[str, Any]]] = {}
    for item in delivery_identities(root, catalogue):
        delivered.setdefault(item["run_id"], []).append(item)
    route_keys = {curated[run["id"]][0] for run in catalogue["real"] if run["id"] in curated}
    for run in catalogue["real"]:
        folder = run["id"]
        if folder.startswith("delivery:"):
            continue
        if not SAFE_FOLDER.fullmatch(folder):
            issues.append(f"{folder}: folder name cannot be linked; rename it to show this run")
            continue
        if folder in route_keys and folder not in curated:
            # The route key names the retained case in links and pins: never replace it.
            issues.append(f"{folder}: name is a retained case's route key; rename it to show it")
            continue
        key, row = curated.get(folder) or (folder, None)
        name, issuer_id, problem = recorded_identity(
            root / "runs" / folder, run, row and row[1], delivered.get(folder, [])
        )
        if problem:
            issues.append(f"runs/{folder}: {problem}")
        shown[key] = row or run_row(root, run, name)
        recorded[key] = (name, issuer_id)

    def link(folder: str, relative: str, digest: str) -> str:
        return f"/files/{quote(f'runs/{folder}/{relative}')}?sha256={digest}"

    runs: dict[str, Any] = {}
    outputs: dict[str, Any] = {}
    inputs: dict[str, Any] = {}
    sources: dict[str, list[dict[str, Any]]] = {}
    pins: dict[str, Any] = {}
    found: list[str] = []
    for key, row in shown.items():
        # Documented fail-open: one run that cannot be read is hidden and reported in Settings.
        try:
            part = collect_runs(root, {key: row}, catalog, link, strict=False)
        except Exception as error:  # noqa: BLE001
            found.append(f"{row[0]}: could not be read ({error!r})")
            continue
        runs |= part[0]
        outputs |= part[1]
        inputs |= part[2]
        for digest, matches in part[3].items():
            sources.setdefault(digest, []).extend(matches)
        pins |= part[4]
        found += part[5]
    fields, keys = issuer_groups({key: recorded[key] for key in runs})
    for key, identity in fields.items():
        runs[key].update(identity)
    reports, unread = catalogue_reports(root, catalogue, sources, keys)
    found += unread
    models, unread = catalogue_models(root, catalogue, outputs, keys)
    found += unread
    # A compared deliverable is a curated build, not a folder that merely has its name.
    for module, config in catalog.items():
        compare = config.get("compare")
        if (
            module in pins
            and compare
            and not (
                compare["recheck"] in outputs
                and {compare["prior"], compare["current"], compare["repaired"]}
                <= {r["id"] for r in reports if r["build"]}
            )
        ):
            del pins[module]
            found.append(
                f"{module}: curated pin dropped: a compared deliverable or recheck is missing"
            )
    return {
        "runs": runs,
        "outputs": outputs,
        "inputs": inputs,
        "pins": pins,
        "reports": reports,
        "models": models,
        "visuals": visual_catalogue(),
        "issues": issues + found,
    }


if __name__ == "__main__":
    print(json.dumps(workspace_store(Path(sys.argv[1]), json.load(sys.stdin)), ensure_ascii=False))
