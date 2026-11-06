"""Backfill ``runs/<id>/library.json`` for CP-OS host-session runs (schema ``issuer-library-run/1``).

    PYTHONPATH=src python -m deploy_workflow.cpos_library [--secdata DIR] [--check | --gate] RUN...
    PYTHONPATH=src python -m deploy_workflow.cpos_library --package OUT [--part-mb 40] RUN...

``--package`` keeps run folders out of the repository download: it writes the runs that pass the
gate, with their manifests, into ZIP parts of at most ``--part-mb`` compressed megabytes, plus
``SHA256SUMS.txt``. Each part holds whole run folders under ``runs/`` and is extracted into the
library's workspace folder. The same runs always give byte-identical parts. A failing run is
refused, and so is a run without its manifest.

``--gate`` decides which runs belong in the library and writes nothing. A run passes when its
instructions and report layout are byte-identical to what the current launcher writes for the same
run (the latest methodology), its delivery is published and hash-checked, every section of its
layout is populated, every chart figure of its layout is drawn with at least one plotted value in
every series, and its manifest carries every field the library shows: issuer name, sector with
its pinned source, as-of date, period, workflow, summary and primary handoff. Screening metrics
are optional in the schema and no screen shows them, so they do not decide inclusion.

Identity, sector, dates and currency come from the run's own retained context input: the SECData
context file kept byte for byte under ``inputs/``, or the pilot runs' ``context.json``. Every pinned
source therefore lies inside the run folder, and the manifest stays valid when only ``runs/`` is
copied into a library workspace. Screening metrics come from the delivered CP-1 handoff: leverage,
coverage and cash from its three chart tables, revenue, EBITDA and operating cash flow from its
financials table when the row label, the period column and the unit are explicit. Anything else is
null, never zero. ``checklist`` stays null and ``provenance`` is not set: the library shows these
runs as unassessed and not classified.

Issuer names are grouped in proper case. A context name that is not all capitals is kept. For an
all-capital EDGAR registrant name, the funds' spelling from SECData's ``corpus.json`` (``--secdata``
names the ``data/<date>`` folder holding ``corpus.json`` and ``contexts/``; a run's context is matched to
its CIK by hash) is used when it is the same name word for word apart from the corporate suffix;
otherwise the registrant name is
recased word by word (a leading or vowelless word of up to three letters stays as written, since it
is usually an acronym). The
registrant name is kept in the pinned context line and repeated in the summary.

Existing manifests are never overwritten. ``--check`` rebuilds every manifest, compares it with the
file on disk and exits 1 on any difference, so a changed run folder is noticed.
"""

from __future__ import annotations

import argparse
import hashlib
import io
import json
import os
import re
import sys
import tempfile
import zipfile
from dataclasses import dataclass
from pathlib import Path
from typing import Any

JSON = dict[str, Any]

SCHEMA = "issuer-library-run/1"
# Go's numericToken in apps/issuer-library/discovery.go: a metric value must be one of these tokens
# of its quoted line, with the commas removed.
NUMBER = re.compile(r"-?[0-9][0-9,]*(?:\.[0-9]+)?")
EXCLUDED = re.compile(
    r"guidance|pro forma|indicative|forecast|projected|estimate|outlook|annualis|annualiz|illustrative",
    re.IGNORECASE,
)
PART_YEAR = re.compile(r"\bQ[1-4]\b|\bH[12]\b|months|quarter|weeks|\b[1-9]M\b", re.IGNORECASE)
MONTHS = {
    name[:3]: number
    for number, name in enumerate(
        [
            "january",
            "february",
            "march",
            "april",
            "may",
            "june",
            "july",
            "august",
            "september",
            "october",
            "november",
            "december",
        ],
        1,
    )
}
ISO_DATE = re.compile(r"(?<!\d)(20\d\d)-(\d\d)-\d\d(?!\d)")
MONTH_YEAR = re.compile(
    r"\b(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(?:\d{1,2},?\s+)?(20\d\d)\b",
    re.IGNORECASE,
)
DAY_MONTH_YEAR = re.compile(
    r"\b\d{1,2}\s+(jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\.?\s+(20\d\d)\b",
    re.IGNORECASE,
)
QUARTER_YEAR = re.compile(r"\bQ([1-4])\s*(?:FY)?\s*'?(20\d\d|\d\d)\b", re.IGNORECASE)
HALF_YEAR = re.compile(r"\bH([12])\s*(?:FY)?\s*(20\d\d)\b", re.IGNORECASE)
MONTHS_YEAR = re.compile(r"\b(three|six|nine|3|6|9)[ -]months?\b[^|]*?\b(20\d\d)\b", re.IGNORECASE)
FISCAL_YEAR = re.compile(r"\bFY\s?(20\d\d|\d\d)\b", re.IGNORECASE)
YEAR = re.compile(r"(?<![\dA-Za-z])(20\d\d)(?!\d)")
LTM = re.compile(r"\bLTM\b|last twelve|trailing twelve|\bTTM\b", re.IGNORECASE)
REVENUE = re.compile(
    r"^(total\s+)?(net\s+)?(operating\s+)?(revenues?|sales)(,\s*(net|reported|as reported))?$",
    re.IGNORECASE,
)
# EBITDA is the head noun: up to two qualifiers before it ("Adjusted", "Ongoing"), or "EBITDA
# excluding/before ..." after it. "Depreciation (EBITDA basis)" and "Segment EBITDA" are not it.
EBITDA = re.compile(
    r"^(?:[A-Za-z][\w-]*\s+){0,2}EBITDA(?:\s+(?:excluding|before|ex)\b[^(,:;]*)?(?:\s*[(,:;].*)?$",
    re.IGNORECASE,
)
CASHFLOW = re.compile(
    r"^(net\s+)?cash\s+(flows?\s+)?(\(used in\)\s+)?(provided\s+by|from|generated\s+(from|by)|"
    r"used\s+in)(\s+\(used\s+in\))?\s+operat(ing|ions)(\s+activities)?\b"
    r"|^operating\s+cash\s+flows?\b|^cash\s+from\s+operations\b",
    re.IGNORECASE,
)
# A label naming a ratio, margin or derived line built on the metric, not the metric itself.
NOT_THE_METRIC = re.compile(
    r"/|%|\bmargin\b|\(x\)|\btimes\b|\bcover|\bmultiple\b|\bleverage\b|\bgrowth\b|\bratio\b"
    r"|\bless\b|\bminus\b|\bafter\b|\bfree\b|\bconversion\b|\bper\b|\bto (net|cash|free)\b"
    r"|\bsegment\b|\bguidance\b",
    re.IGNORECASE,
)
# A currency with a scale, as a table states its unit: "US$m", "USD thousands", "Thousands of USD".
CURRENCY = r"(US\$|USD|U\.S\. dollars?|US dollars?|C\$|CAD|EUR|€|GBP|£|CHF|DKK|SEK|NOK)"
SCALE = r"(m|mm|mn|million|millions|bn|billion|billions|k|thousand|thousands)"
UNIT = re.compile(
    rf"(?<![A-Za-z]){CURRENCY}\s?{SCALE}\b|\b{SCALE}\s+of\s+{CURRENCY}",
    re.IGNORECASE,
)
CHART_METRICS = (
    # key, heading, value column, unit expected by the CP-1 instructions
    ("leverage", "Chart data: leverage", "Total debt / EBITDA"),
    ("coverage", "Chart data: interest cover", "EBITDA / cash interest"),
    ("cash", "Chart data: liquidity", "Cash"),
)
TABLE_METRICS = (("revenue", REVENUE), ("ebitda", EBITDA), ("cashflow", CASHFLOW))
SUFFIXES = {"INC", "CORP", "CO", "LTD", "LLC", "LP", "PLC", "SA", "SE", "NV", "AG", "AS"}
LONG_SUFFIX = {"CORPORATION": "CORP", "INCORPORATED": "INC", "COMPANY": "CO", "LIMITED": "LTD"}
KEEP_UPPER = {"LP", "LLC", "PLC", "NV", "SA", "AG", "SE", "ASA", "AB", "USA", "II", "III", "IV"}
RECASE = {
    "INC": "Inc",
    "CO": "Co",
    "LTD": "Ltd",
    "CORP": "Corp",
    "THE": "the",
    "AND": "and",
    "OF": "of",
}


class ManifestError(ValueError):
    pass


@dataclass(frozen=True)
class Line:
    number: int
    text: str


@dataclass(frozen=True)
class Table:
    header: list[str]
    rows: list[tuple[Line, list[str]]]


def _lines(raw: bytes) -> list[Line]:
    """Lines numbered as the library counts them: split on newline after CRLF normalisation."""
    text = raw.decode("utf-8").replace("\r\n", "\n")
    return [Line(i, t) for i, t in enumerate(text.split("\n"), 1)]


def _cells(text: str) -> list[str]:
    inner = text.strip()
    inner = inner.removeprefix("|")
    inner = inner.removesuffix("|")
    return [cell.strip() for cell in inner.split("|")]


def table_under(lines: list[Line], heading: str) -> Table | None:
    """The first Markdown table under ``### heading``, with each row's line number."""
    start = next((i for i, line in enumerate(lines) if line.text.strip() == f"### {heading}"), None)
    if start is None:
        return None
    i = start + 1
    while i < len(lines) and not lines[i].text.startswith("|"):
        if lines[i].text.startswith("#"):
            return None
        i += 1
    if i >= len(lines):
        return None
    header = _cells(lines[i].text)
    rows = []
    for line in lines[i + 1 :]:
        if not line.text.startswith("|"):
            break
        cells = _cells(line.text)
        if all(re.fullmatch(r":?-+:?", c) for c in cells if c) and any(cells):
            continue
        if len(cells) == len(header):
            rows.append((line, cells))
    return Table(header, rows)


def plain_number(cell: str) -> str | None:
    """The cell as the library will match it, or None for anything but one plain number."""
    text = cell.strip()
    if NUMBER.fullmatch(text) is None:
        return None
    return text.replace(",", "")


def _year(text: str) -> int:
    return int(text) + 2000 if len(text) == 2 else int(text)


def period_rank(label: str) -> tuple[int, int, int]:
    """(year, month, LTM) of the latest date a period label names.

    An explicit date wins. Without one, months come from the quarter, half or months named, and
    a bare fiscal year ranks as December: FY2026 ranks as December 2026.
    """
    keys: list[tuple[int, int]] = [(int(y), int(m)) for y, m in ISO_DATE.findall(label)]
    keys += [(int(y), MONTHS[m.lower()]) for m, y in MONTH_YEAR.findall(label)]
    keys += [(int(y), MONTHS[m.lower()]) for m, y in DAY_MONTH_YEAR.findall(label)]
    if keys:
        # An explicit date outranks what a fiscal-year or quarter name would imply.
        return (*max(keys), 1 if LTM.search(label) else 0)
    keys += [(_year(y), 3 * int(q)) for q, y in QUARTER_YEAR.findall(label)]
    keys += [(int(y), 6 * int(h)) for h, y in HALF_YEAR.findall(label)]
    keys += [
        (int(y), {"three": 3, "six": 6, "nine": 9}.get(n.lower(), int(n) if n.isdigit() else 0))
        for n, y in MONTHS_YEAR.findall(label)
    ]
    # A quarter or half named with its fiscal year, such as Q2 FY2027, ends with that quarter.
    rest = HALF_YEAR.sub("", QUARTER_YEAR.sub("", label))
    keys += [(_year(y), 12) for y in FISCAL_YEAR.findall(rest)]
    if not keys:
        keys = [(int(y), 0) for y in YEAR.findall(label)]
    year, month = max(keys, default=(0, 0))
    return (year, month, 1 if LTM.search(label) else 0)


def latest_row(
    table: Table, column: int, basis: int | None = None
) -> tuple[Line, list[str]] | None:
    """The reported row with the latest period whose value cell is a plain number.

    With ``basis`` (a ratio such as leverage), a row labelled as a quarter, half or year to date
    counts only when its label or basis says the figure is trailing twelve months.
    """
    best = None
    for position, (line, cells) in enumerate(table.rows):
        label = cells[0]
        if EXCLUDED.search(label) or plain_number(cells[column]) is None:
            continue
        if basis is not None and PART_YEAR.search(label) and not LTM.search(label + cells[basis]):
            continue
        key = (*period_rank(label), position)
        if best is None or key > best[0]:
            best = (key, (line, cells))
    return best[1] if best else None


def _column(header: list[str], name: str) -> int | None:
    return next((i for i, cell in enumerate(header) if cell == name), None)


def chart_metric(lines: list[Line], heading: str, value_column: str) -> tuple[JSON, Line] | None:
    table = table_under(lines, heading)
    if table is None:
        return None
    column, unit, basis = (
        _column(table.header, value_column),
        _column(table.header, "Reporting unit"),
        _column(table.header, "Basis and limitation"),
    )
    if column is None or unit is None or basis is None or table.header[0] != "Period":
        return None
    row = latest_row(table, column, None if value_column == "Cash" else basis)
    if row is None:
        return None
    line, cells = row
    if not cells[unit] or not cells[basis]:
        return None
    metric = {
        "value": plain_number(cells[column]),
        "unit": cells[unit],
        "period": cells[0],
        "basis": f"{value_column}. {cells[basis]}",
    }
    return metric, line


def unit_phrase(text: str) -> str | None:
    """The first currency-and-scale phrase in ``text``, exactly as written, or None."""
    found = UNIT.search(text)
    return found.group(0) if found else None


def _bare_label(label: str) -> tuple[str, str | None]:
    """The row label without a trailing unit in brackets, and that unit."""
    found = re.search(r"\s*\(([^()]*)\)\s*$", label)
    if found and (unit := unit_phrase(found.group(1))):
        return label[: found.start()].strip(), unit
    return label.strip(), None


def _table_unit(lines: list[Line], heading: str, header_first: str) -> str | None:
    """The unit a table states for all its rows: in its first header cell, else in the text
    between the heading and the table ("Amounts in USD thousands unless ...")."""
    found = re.search(r"\(([^()]*)\)", header_first)
    if found and (unit := unit_phrase(found.group(1))):
        return unit
    start = next((i for i, line in enumerate(lines) if line.text.strip() == f"### {heading}"), None)
    if start is None:
        return None
    for line in lines[start + 1 :]:
        if line.text.startswith(("|", "#")):
            break
        stated = re.search(r"\bamounts?\b|\bunless\b|\bfigures are\b", line.text, re.IGNORECASE)
        if stated and (unit := unit_phrase(line.text)):
            return unit
    return None


def _row_unit(
    header: list[str], cells: list[str], label_unit: str | None, table_unit: str | None
) -> str | None:
    """A row's unit: its Unit column, its label, a note column that opens with a unit, else the
    table's own. A note column is the last one, headed with unit, basis, note, source or locator."""
    unit_column = _column(header, "Unit")
    if unit_column is not None:
        return unit_phrase(cells[unit_column])
    if label_unit:
        return label_unit
    last = header[-1].lower()
    if len(header) > 2 and re.search(r"unit|basis|note|source|locator", last):
        found = UNIT.match(cells[-1].strip())
        if found:
            return found.group(0)
    return table_unit


def full_period(label: str) -> bool:
    """An LTM or whole fiscal-year period: not a quarter, half or year-to-date fragment."""
    if EXCLUDED.search(label):
        return False
    if LTM.search(label) or re.search(r"\b(twelve|12) months\b", label, re.IGNORECASE):
        return True
    whole_year = FISCAL_YEAR.search(label) or re.search(
        r"\byear ended\b|\bfiscal (year )?20\d\d\b|^\s*20\d\d\s*(\(|$)", label, re.IGNORECASE
    )
    return bool(whole_year and not PART_YEAR.search(label))


def _is_metric(label: str, pattern: re.Pattern[str]) -> bool:
    return bool(pattern.search(label)) and not NOT_THE_METRIC.search(label)


def table_metric(lines: list[Line], pattern: re.Pattern[str]) -> tuple[JSON, Line] | None:
    """The first row of the financials table that is this metric and reports a plain number for an
    LTM or whole fiscal-year period with an explicit unit, at the latest such period it reports."""
    heading = "Financials and credit metrics"
    table = table_under(lines, heading)
    if table is None:
        return None
    header = table.header
    table_unit = _table_unit(lines, heading, header[0])
    period_column = _column(header, "Period")
    value_column = next(
        (i for name in ("Value", "Amount") if (i := _column(header, name)) is not None), None
    )
    if period_column is not None and value_column is not None:
        # Long format: one row per metric and period; the first matching label decides the line.
        chosen = None
        for position, (line, cells) in enumerate(table.rows):
            bare, label_unit = _bare_label(cells[0])
            if not _is_metric(bare, pattern) or (chosen and bare != chosen[0]):
                continue
            unit = _row_unit(header, cells, label_unit, table_unit)
            label, value = cells[period_column], plain_number(cells[value_column])
            if unit is None or value is None or not full_period(label):
                continue
            key = (*period_rank(label), position)
            if chosen is None or key > chosen[1]:
                chosen = (bare, key, line, value, unit, label)
        if chosen is None:
            return None
        bare, _, line, value, unit, label = chosen
    else:
        columns = [i for i, cell in enumerate(header[1:], 1) if full_period(cell)]
        found = None
        for line, cells in table.rows:
            bare, label_unit = _bare_label(cells[0])
            if not _is_metric(bare, pattern):
                continue
            unit = _row_unit(header, cells, label_unit, table_unit)
            reported = [i for i in columns if plain_number(cells[i]) is not None]
            if unit is None or not reported:
                continue
            column = max(reported, key=lambda i: (*period_rank(header[i]), i))
            found = (line, bare, unit, header[column], plain_number(cells[column]))
            break
        if found is None:
            return None
        line, bare, unit, label, value = found
    metric = {
        "value": value,
        "unit": unit,
        "period": label,
        "basis": f"{bare}, as the CP-1 table prints it.",
    }
    return metric, line


def reader_summary(lines: list[Line]) -> dict[str, str] | None:
    table = table_under(lines, "Reader summary")
    if (
        table is None
        or table.header != ["Bottom line", "Confidence", "Main limitation"]
        or not table.rows
    ):
        return None
    _, cells = table.rows[0]
    return dict(zip(table.header, cells, strict=True))


def normalised_words(name: str) -> list[str]:
    words = []
    for raw in name.upper().split():
        if re.fullmatch(r"/[A-Z]{2}/?", raw):
            continue
        word = re.sub(r"[^A-Z0-9&]", "", raw)
        if word:
            words.append(LONG_SUFFIX.get(word, word))
    while len(words) > 1 and words[-1] in SUFFIXES:
        words.pop()
    return words


def recased(name: str) -> str:
    out = []
    for i, raw in enumerate(name.split()):
        if re.fullmatch(r"/[A-Z]{2}/?", raw):
            continue
        found = re.fullmatch(r"([^A-Za-z0-9]*)([A-Za-z0-9&'./-]+?)([^A-Za-z0-9]*)", raw)
        if found is None:
            out.append(raw)
            continue
        pre, word, post = found.groups()
        acronym = len(word) <= 3 and word.isalpha() and (i == 0 or not re.search("[AEIOU]", word))
        if word in KEEP_UPPER or (acronym and word not in RECASE):
            text = word
        elif word in RECASE:
            text = RECASE[word] if i else RECASE[word].capitalize()
        else:
            parts = re.split(r"([-/])", word)
            text = "".join(part[:1] + part[1:].lower() for part in parts)
        out.append(pre + text + post)
    return " ".join(out)


def display_name(registrant: str, fund_names: list[str]) -> tuple[str, str]:
    """The grouping name and how it was chosen: context, funds or recased."""
    if registrant != registrant.upper():
        return registrant, "context"
    same = [
        n
        for n in fund_names
        if n != n.upper() and normalised_words(n) == normalised_words(registrant)
    ]
    if same:
        return max(same, key=len), "funds"
    return recased(registrant), "recased"


def load_fund_names(secdata: Path | None) -> dict[str, list[str]]:
    """Fund spellings by SHA-256 of the SECData context file, through the CIK in its file name."""
    if secdata is None:
        return {}
    corpus = json.loads((secdata / "corpus.json").read_text(encoding="utf-8"))
    by_cik = {entry["cik"]: list(entry.get("nport_names", ())) for entry in corpus["issuers"]}
    names = {}
    for path in sorted((secdata / "contexts").glob("*.json")):
        cik = path.name.split("-", 1)[0]
        if cik in by_cik:
            names[hashlib.sha256(path.read_bytes()).hexdigest()] = by_cik[cik]
    return names


def _context_file(run_dir: Path) -> Path:
    candidates = sorted(run_dir.glob("inputs/*")) + [run_dir / "context.json"]
    for path in candidates:
        if not path.is_file():
            continue
        with path.open("rb") as stream:
            head = stream.read(64)
        if b'"schema": "context/1"' in head:
            return path
    raise ManifestError(f"{run_dir.name}: no retained context input")


def _source(run_dir: Path, path: Path, line: Line) -> JSON:
    relative = path.relative_to(run_dir.parent.parent).as_posix()
    return {
        "path": relative,
        "sha256": hashlib.sha256(path.read_bytes()).hexdigest(),
        "line": line.number,
        "quote": line.text,
    }


def _first_line(lines: list[Line], marker: str, run_dir: Path) -> Line:
    found = next((line for line in lines if marker in line.text), None)
    if found is None:
        raise ManifestError(f"{run_dir.name}: context has no {marker} line")
    return found


def _delivery(run_dir: Path) -> Path | None:
    deliveries = run_dir / "deliveries"
    if not deliveries.is_dir():
        return None
    folders = sorted(p for p in deliveries.iterdir() if (p / "CP-1.md").is_file())
    if len(folders) > 1:
        raise ManifestError(f"{run_dir.name}: more than one delivery")
    return folders[0] if folders else None


def build_manifest(run_dir: Path, fund_names: dict[str, list[str]]) -> JSON:
    run_dir = run_dir.resolve()
    if run_dir.parent.name != "runs":
        raise ManifestError(f"{run_dir}: not a runs/<id> folder")
    identity = json.loads((run_dir / "identity.json").read_text(encoding="utf-8"))
    context_path = _context_file(run_dir)
    context_raw = context_path.read_bytes()
    context = json.loads(context_raw)
    who, run = context["identity"], context["run"]
    if who["issuer_id"] != identity["run"]["issuer_id"]:
        raise ManifestError(f"{run_dir.name}: context and identity.json name different issuers")
    context_lines = _lines(context_raw)
    sources = {
        "context": _source(
            run_dir, context_path, _first_line(context_lines, '"issuer_name"', run_dir)
        )
    }
    name, chosen = display_name(
        who["issuer_name"], fund_names.get(sources["context"]["sha256"], [])
    )
    sector = who.get("sector") or "Unclassified"
    if sector != "Unclassified":
        sources["sector"] = _source(
            run_dir, context_path, _first_line(context_lines, '"sector"', run_dir)
        )

    metrics: dict[str, JSON | None] = {
        k: None for k in ("revenue", "ebitda", "leverage", "coverage", "cash", "cashflow")
    }
    gaps = []
    summary = None
    period = run.get("current_period") or ""
    handoff = None
    delivery = _delivery(run_dir)
    if delivery is None:
        gaps.append("Stopped before publication: no report was delivered from this run.")
    else:
        cp1_path = delivery / "CP-1.md"
        cp1 = _lines(cp1_path.read_bytes())
        for key, heading, column in CHART_METRICS:
            found = chart_metric(cp1, heading, column)
            if found is not None:
                metric, line = found
                sources[f"cp1-{key}"] = _source(run_dir, cp1_path, line)
                metrics[key] = {**metric, "source": f"cp1-{key}"}
                if key == "cash":
                    period = metric["period"]
        for key, pattern in TABLE_METRICS:
            found = table_metric(cp1, pattern)
            if found is not None:
                metric, line = found
                sources[f"cp1-{key}"] = _source(run_dir, cp1_path, line)
                metrics[key] = {**metric, "source": f"cp1-{key}"}
        cp2_path = delivery / "CP-2.md"
        if cp2_path.is_file():
            handoff = cp2_path.relative_to(run_dir.parent.parent).as_posix()
            cp2 = reader_summary(_lines(cp2_path.read_bytes()))
            if cp2:
                summary = cp2["Bottom line"]
                gaps.append(f"CP-2 main limitation: {cp2['Main limitation']}")
        cp1_summary = reader_summary(cp1)
        if cp1_summary:
            gaps.append(f"CP-1 main limitation: {cp1_summary['Main limitation']}")
            summary = summary or cp1_summary["Bottom line"]

    reviewed = (run_dir / "review.json").is_file()
    gaps.insert(
        0,
        "Host session: an agent answered every module from the pinned filings and CP-5 is its own review. "
        + (
            "One independent reviewer's findings are retained in review.json and are not repaired here."
            if reviewed
            else "No independent review has been made."
        )
        + " Treat the analysis as candidate.",
    )
    provenance = f"Launched through CP-OS as of {run['as_of']} on the retained context"
    if chosen != "context":
        provenance += f"; the EDGAR registrant name in that context is {who['issuer_name']}"
    ticker = who.get("ticker") or ""
    record = {
        "id": run_dir.name,
        "issuer": who["issuer_id"],
        "name": name,
        "identity_source": "context",
        "sector": sector,
        "sector_source": "sector" if "sector" in sources else None,
        "date": run["as_of"],
        "period": period,
        "currency": run.get("reporting_currency") or "",
        "workflow": run.get("pathway") or "",
        "title": f"CP-OS host session{f' ({ticker})' if ticker else ''}",
        "summary": f"{summary or 'No report was published.'} {provenance}.",
        "handoff": handoff,
        "metrics": metrics,
        "ratings": [],
        "gaps": gaps,
        "artifacts": [],
    }
    return {
        "schema": SCHEMA,
        "run": {key: value for key, value in record.items() if value is not None},
        "sources": sources,
        "checklist": None,
    }


NUMERIC_CELL = re.compile(r"^-?\(?[0-9][0-9,]*(\.[0-9]+)?\)?[x%]?$")
SHOWN_FIELDS = ("name", "issuer", "identity_source", "sector_source", "date", "period", "workflow")


def _current_method(run_dir: Path) -> list[str]:
    """How the run's instructions and layout differ from what the current launcher writes."""
    from deploy_vii.registry import plan
    from deploy_workflow.owners.cpos import HandoffPlan
    from deploy_workflow.owners.cpos_launch import HOST, _instructions, _layout

    recorded = HandoffPlan.model_validate_json((run_dir / "workflow.json").read_bytes())
    context = json.loads(_context_file(run_dir).read_bytes())
    aliases = tuple(a for a in context["identity"].get("aliases", ()) if a.strip())
    ordered = plan(recorded.run.requested_modules)
    host = recorded.execution == "host-session"
    layout, _ = _layout(recorded.run, ordered, aliases, HOST if host else "")
    problems = []
    for module in ordered:
        text = _instructions(recorded.run, module, layout.routes, host)
        held = recorded.instructions.get(module)
        if held is None or held.sha256 != hashlib.sha256(text).hexdigest():
            problems.append(f"{module} instructions are not the current launcher's")
    if layout != recorded.layout:
        problems.append("report layout is not the current launcher's")
    return problems


def _published(run_dir: Path) -> list[str]:
    from deploy_workflow.handoff_delivery import verify_delivery

    manifests = sorted(run_dir.glob("delivery-*.json"))
    delivery = _delivery(run_dir)
    if not list(run_dir.glob("completed-*.json")) or len(manifests) != 1 or delivery is None:
        return ["no published report"]
    try:
        verify_delivery(manifests[0], delivery)
    except (OSError, ValueError) as error:
        return [f"published report fails its hash check: {error}"]
    return []


def _sections_and_charts(run_dir: Path) -> list[str]:
    delivery = _delivery(run_dir)
    if delivery is None:
        return []
    layout = json.loads((run_dir / "workflow.json").read_text(encoding="utf-8"))["layout"]
    view = json.loads((delivery / "report-view.json").read_text(encoding="utf-8"))
    blocks = {block["block_id"]: block for block in view["blocks"]}
    problems = [
        f"section {block_id} is not populated"
        for block_id in layout["blocks"]
        if blocks.get(block_id, {}).get("state") != "populated"
    ]
    figures = {f["fig_id"]: f for b in view["blocks"] for f in (b.get("figures") or ())}
    for route in layout["routes"]:
        if route["kind"] != "chart":
            continue
        figure = figures.get(route["figure_id"])
        if figure is None:
            problems.append(f"chart {route['figure_id']} is not drawn")
            continue
        rows = figure["chart"]["table_twin"]["rows"]
        for series in route["value_columns"]:
            plotted = any(
                cell["state"] == "known" and NUMERIC_CELL.match(cell["text"].replace("\u2212", "-"))
                for row in rows
                if row["label"].startswith(f"{series} · ")
                for cell in row["cells"]
            )
            if not plotted:
                problems.append(f"chart {route['figure_id']} has no value for {series}")
    return problems


def gate(run_dir: Path, fund_names: dict[str, list[str]]) -> list[str]:
    """Why a run does not belong in the library; empty when it does."""
    problems = _current_method(run_dir) + _published(run_dir) + _sections_and_charts(run_dir)
    record = build_manifest(run_dir, fund_names)["run"]
    missing = [field for field in SHOWN_FIELDS if not record.get(field)]
    if record.get("sector") in (None, "", "Unclassified"):
        missing.append("sector")
    if not record.get("handoff"):
        missing.append("handoff")
    if missing:
        problems.append(f"library fields missing: {', '.join(missing)}")
    return problems


ZIP_TIME = (1980, 1, 1, 0, 0, 0)


def _run_entries(run_dir: Path) -> list[tuple[str, Path]]:
    """Every file of a run folder, as ``runs/<id>/...`` archive names, in a fixed order."""
    files = sorted(p for p in run_dir.rglob("*") if p.is_file() and not p.is_symlink())
    return [(f"runs/{run_dir.name}/{p.relative_to(run_dir).as_posix()}", p) for p in files]


def _zip_run(archive: zipfile.ZipFile, run_dir: Path) -> None:
    for name, path in _run_entries(run_dir):
        info = zipfile.ZipInfo(name, ZIP_TIME)
        info.compress_type = zipfile.ZIP_DEFLATED
        info.external_attr = 0o644 << 16
        archive.writestr(info, path.read_bytes(), compresslevel=9)


def _compressed_size(run_dir: Path) -> int:
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, "w") as archive:
        _zip_run(archive, run_dir)
    return buffer.tell()


def package(
    runs: list[Path], out: Path, part_bytes: int, fund_names: dict[str, list[str]]
) -> list[Path]:
    """Write the runs into ZIP parts of at most ``part_bytes``, in run-id order, and SHA256SUMS."""
    runs = sorted(runs, key=lambda r: r.name)
    for run_dir in runs:
        if problems := gate(run_dir, fund_names):
            raise ManifestError(f"{run_dir.name} does not pass the gate: {'; '.join(problems)}")
        if not (run_dir / "library.json").is_file():
            raise ManifestError(f"{run_dir.name} has no library.json")
        if (run_dir / "library.json").read_bytes() != encode(build_manifest(run_dir, fund_names)):
            raise ManifestError(f"{run_dir.name}: library.json differs from a fresh build")
    groups: list[list[Path]] = []
    size = 0
    for run_dir in runs:
        weight = _compressed_size(run_dir)
        if weight > part_bytes:
            raise ManifestError(f"{run_dir.name} alone is larger than one part")
        if not groups or size + weight > part_bytes:
            groups.append([])
            size = 0
        groups[-1].append(run_dir)
        size += weight
    out.mkdir(parents=True, exist_ok=False)
    parts, sums = [], []
    for number, group in enumerate(groups, 1):
        path = out / f"issuer-runs-part-{number}-of-{len(groups)}.zip"
        with zipfile.ZipFile(path, "w") as archive:
            for run_dir in group:
                _zip_run(archive, run_dir)
        parts.append(path)
        sums.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {path.name}\n")
    (out / "SHA256SUMS.txt").write_text("".join(sums), encoding="utf-8")
    return parts


def encode(manifest: JSON) -> bytes:
    return (json.dumps(manifest, indent=2, ensure_ascii=False) + "\n").encode("utf-8")


def write_new(target: Path, raw: bytes) -> None:
    """Write atomically, never over an existing file."""
    fd, name = tempfile.mkstemp(dir=target.parent, suffix=".tmp")
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
        os.link(name, target)
    finally:
        Path(name).unlink(missing_ok=True)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("runs", nargs="+", type=Path, help="runs/<id> folders")
    parser.add_argument(
        "--secdata", type=Path, help="SECData data/<date> folder: corpus.json and contexts/"
    )
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--check", action="store_true", help="compare with the existing manifests")
    mode.add_argument("--gate", action="store_true", help="say which runs belong in the library")
    mode.add_argument(
        "--package", type=Path, help="write passing runs into ZIP parts in this folder"
    )
    parser.add_argument("--part-mb", type=int, default=40, help="largest part, compressed MB")
    args = parser.parse_args(argv)
    fund_names = load_fund_names(args.secdata)
    failures = 0
    if args.package:
        try:
            parts = package(list(args.runs), args.package, args.part_mb * 1_000_000, fund_names)
        except (ManifestError, OSError) as error:
            print(f"FAIL {error}", flush=True)
            return 1
        for path in parts:
            print(f"wrote {path.name} {path.stat().st_size / 1e6:.1f} MB", flush=True)
        return 0
    if args.gate:
        for run_dir in args.runs:
            try:
                problems = gate(run_dir, fund_names)
            except (ManifestError, OSError, ValueError, KeyError) as error:
                problems = [f"cannot be read: {error}"]
            print(
                f"fail {run_dir.name}: {'; '.join(problems)}"
                if problems
                else f"pass {run_dir.name}"
            )
            failures += bool(problems)
        return 1 if failures else 0
    for run_dir in args.runs:
        target = run_dir / "library.json"
        try:
            manifest = build_manifest(run_dir, fund_names)
        except (ManifestError, OSError, ValueError, KeyError) as error:
            print(f"FAIL {run_dir.name}: {error}", flush=True)
            failures += 1
            continue
        raw = encode(manifest)
        run = manifest["run"]
        filled = ",".join(k for k, v in run["metrics"].items() if v)
        line = f"{run_dir.name}: {run['name']} | {run['sector']} | metrics {filled or 'none'}"
        if args.check:
            same = target.is_file() and target.read_bytes() == raw
            print(("same " if same else "DIFF ") + line, flush=True)
            failures += not same
        elif target.exists():
            print("exists " + line, flush=True)
        else:
            write_new(target, raw)
            print("wrote " + line, flush=True)
    return 1 if failures else 0


if __name__ == "__main__":
    sys.exit(main())
