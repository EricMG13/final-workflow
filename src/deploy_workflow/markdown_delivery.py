"""Literal Markdown-to-report adapter, separate from native analytical contracts.

Existing report/index/table/prose components own presentation. This adapter
retains the actual handoffs, text and source lines; it performs no financial
calculation, journal promotion or analytical execution.
"""

from __future__ import annotations

import hashlib
import html
import json
import re
from collections.abc import Mapping
from dataclasses import dataclass, replace
from datetime import date
from decimal import Context, Decimal
from pathlib import Path

from deploy_vii.bindings import Binding, BindingMap, validate_bindings
from deploy_vii.contracts import (
    Citation,
    Fact,
    ModuleView,
    ReportTable,
    Run,
    Source,
    TableColumn,
    TableRow,
    View,
)
from deploy_vii.display import UnitClass
from deploy_vii.registry import modules
from deploy_vii.render import render
from deploy_vii.report_view import (
    Block,
    BlockTab,
    CallItem,
    FactCoord,
    ReportView,
    _call,
    _ChartPoint,
    _figure_of_points,
    _prose_lines,
    _refs_by_fact,
    _Slot,
    _slot,
    _spec_of,
    _unplaced,
    build_index,
    pathways,
)
from deploy_workflow.handoff_delivery import (
    FENCE,
    SOURCE_NUMBER,
    DeliveryRequest,
    MarkdownRoute,
    heading_of,
    hide_comments,
    is_gap,
    names_issuer,
    physical_lines,
    plain,
    section,
)

CHART_UNITS: dict[str, UnitClass] = {"x": "multiple", "US$m": "amount", "%": "percent"}

STRIP_FIGURES = {
    "model-chart-strip": ("S.1", "S.2", "S.3", "S.4"),
    "metric-strip": ("S.1", "S.2", "S.3"),
    "maturity-wall": ("S.4",),
    "yield-against-maturity": ("RV.1",),
}


LIST_ITEM = re.compile(r"[ \t]*(?:[-*+]|\d{1,3}[.)])[ \t]")


@dataclass(frozen=True)
class _Paragraph:
    """Consecutive physical lines that one fact quotes; a fenced block's text is kept as written."""

    lines: tuple[tuple[int, str], ...]
    code: bool = False

    @property
    def text(self) -> str:
        text = " ".join(line.strip() for _, line in self.lines)
        return text if self.code else plain(text)


@dataclass(frozen=True)
class _ProseGroup:
    """The paragraphs under one heading line; `path` is its parent headings and itself."""

    line: int
    heading: str
    path: str
    paragraphs: tuple[_Paragraph, ...]


def _opens_with(text: str | None, prefix: str) -> bool:
    """Whether a fact opens with `prefix`, as written or after its list marker (`- `, `2. `)."""
    shown = plain(text or "")
    return shown.startswith(prefix) or LIST_ITEM.sub("", shown, count=1).startswith(prefix)


def _table_lines(tables: list[ReportTable], facts: list[Fact]) -> set[int]:
    """Physical lines a recognised table consumed: header, separator and every row."""
    cited = {f.fact_id: int(f.citations[0].locator.split()[-1]) for f in facts if f.citations}
    spans = [[cited[fid] for row in t.rows for fid in row.fact_ids if fid in cited] for t in tables]
    return {n for rows in spans if rows for n in range(min(rows) - 2, max(rows) + 1)}


def _prose_groups(lines: list[str], in_table: set[int]) -> list[_ProseGroup]:
    """Every non-blank line outside a table lands in a paragraph under its nearest heading.

    Each list item (with its wrapped lines) and each pipe line that no table consumed is a
    paragraph of its own, and a fenced block is one paragraph including its fences, so none is
    dropped or folded into its neighbour; `#1 risk` is text, not a heading.
    """
    groups: dict[int, list[_Paragraph]] = {}
    titles: dict[int, tuple[str, str]] = {0: ("Document", "Document")}
    parents: list[tuple[int, str]] = []
    key, code = 0, False
    pending: list[tuple[int, str]] = []

    def close() -> None:
        nonlocal pending
        if pending:
            groups.setdefault(key, []).append(_Paragraph(tuple(pending), code))
            pending = []

    for number, line in enumerate(lines, 1):
        found = heading_of(line)
        if code and found and found[0] == 2:
            close()  # An unclosed fence ends at the next section.
            code = False
        if code:
            if line.strip():  # A blank line inside a fence has nothing to quote.
                pending.append((number, line))
            if FENCE.match(line):
                close()
                code = False
        elif FENCE.match(line):
            close()
            pending, code = [(number, line)], True
        elif found:
            close()
            level, text = found
            text = text or "Untitled"
            while parents and parents[-1][0] >= level:
                parents.pop()
            parents.append((level, text))
            key = number
            titles[key] = (text, " > ".join(t for lv, t in parents if lv > 1) or text)
        elif not line.strip() or line.startswith("<!--") or number in in_table:
            close()
        elif line.startswith("|"):
            close()
            pending = [(number, line)]
            close()
        else:
            if LIST_ITEM.match(line):
                close()
            pending.append((number, line))
    close()
    return [_ProseGroup(k, *titles[k], tuple(p)) for k, p in groups.items()]


def _prose_labels(groups: list[_ProseGroup]) -> list[str]:
    """Distinct labels: the heading text, else its parent path, else the path with its line."""
    labels = []
    for group in groups:
        same = [g for g in groups if g.heading == group.heading]
        if len(same) == 1:
            labels.append(group.heading)
        elif len([g for g in same if g.path == group.path]) == 1:
            labels.append(group.path)
        else:
            labels.append(f"{group.path} (line {group.paragraphs[0].lines[0][0]})")
    return labels


def literal_module(
    module_id: str, raw: bytes
) -> tuple[ModuleView, Source, dict[str, tuple[str, str]]]:
    """Retain tables and wrapped prose with exact physical-line citations."""
    from deploy_workflow.model_handoff_delivery import _literal_tables

    digest = hashlib.sha256(raw).hexdigest()
    source, facts, tables, _ = _literal_tables(module_id, raw, digest)
    lines = hide_comments(physical_lines(raw.decode("utf-8")), module_id)
    headings = [(n, found[1]) for n, line in enumerate(lines, 1) if (found := heading_of(line))]
    metadata: dict[str, tuple[str, str]] = {}
    fact_map = {f.fact_id: f for f in facts}
    section_of: dict[str, int] = {}
    for i, table in enumerate(tables):
        first = fact_map[table.rows[0].fact_ids[0]].citations[0]
        number = int(first.locator.split()[-1])
        section_of[table.table_id], heading = next(
            (n, title) for n, title in reversed(headings) if n < number
        )
        tables[i] = table.model_copy(
            update={"title": heading + " — " + (table.row_header or "Table")}
        )
        metadata[table.table_id] = (heading, "table")
    groups = _prose_groups(lines, _table_lines(tables, facts))
    section_prose: dict[int, list[str]] = {}
    for group in groups:
        section_prose[group.line] = [p.text for p in group.paragraphs]
    for i, table in enumerate(tables):
        # The unit and limitation sentences of a table's own section travel with the table, so a
        # table route does not publish the numbers without them. The cited prose stays in Evidence.
        if sentences := section_prose.get(section_of[table.table_id]):
            tables[i] = table.model_copy(update={"limitation": " ".join(sentences)})
    for index, (group, heading) in enumerate(zip(groups, _prose_labels(groups), strict=True)):
        table_id = f"prose-{module_id}-{index}"
        rows = []
        for number, paragraph in enumerate(group.paragraphs):
            fact_id = f"{table_id}.r{number}.c0"
            facts.append(
                Fact(
                    fact_id=fact_id,
                    label=heading,
                    table_id=table_id,
                    row_id=f"r{number}",
                    field="c0",
                    text=paragraph.text,
                    value_class="source",
                    basis=(
                        "Literal wrapped paragraph from the model-authored handoff; "
                        "no new analysis."
                    ),
                    citations=tuple(
                        Citation(
                            source_id=module_id,
                            source_sha256=digest,
                            locator=f"line {n}",
                            quote=line,
                        )
                        for n, line in paragraph.lines
                    ),
                )
            )
            rows.append(
                TableRow(
                    row_id=f"r{number}",
                    label=f"{heading} — paragraph {number + 1}",
                    fact_ids=(fact_id,),
                )
            )
        tables.append(
            ReportTable(
                table_id=table_id,
                title=heading,
                row_header="Paragraph",
                columns=(TableColumn(field="c0", label="Text"),),
                rows=tuple(rows),
            )
        )
        metadata[table_id] = (heading, "prose")
    descriptor = next(m for m in modules() if m.module_id == module_id)
    return (
        ModuleView(
            module_id=module_id,
            title=descriptor.title,
            aliases=descriptor.aliases,
            status="candidate",
            artifact_sha256=digest,
            facts=tuple(facts),
            tables=tuple(tables),
            limitations=(
                (
                    "Literal checked analytical handoff, not native contract acceptance; "
                    "source qualifications and gaps remain."
                ),
            ),
        ),
        source,
        metadata,
    )


def _names_section(meta: tuple[str, str] | None, heading: str) -> bool:
    """Whether prose metadata is a `heading` section, under its bare label or, where the heading
    repeats, its path label (`Findings > heading`, `... (line 12)`), so no copy goes unseen."""
    return (
        meta is not None
        and meta[1] == "prose"
        and re.fullmatch(rf"(?:.+ > )?{re.escape(heading)}(?: \(line \d+\))?", meta[0]) is not None
    )


def _portfolio_call(
    module: ModuleView | None,
    metadata: dict[str, tuple[str, str]],
    refs: dict[tuple[str, str], tuple[str, ...]],
    *,
    portfolio: bool = True,
) -> CallItem | None:
    """Copy CP-6's explicit terminal posture; never infer a decision or confidence."""
    if module is None or module.module_id != "CP-6":
        return None
    heading = "Final Sizing Posture" if portfolio else "Action Bias Determination"
    prefix = "Final Sizing Posture:" if portfolio else "Final Action Bias:"
    choices = (
        r"Include|Avoid|Resize-Reduce|Resize-Increase|Maintain-Hold|Requires More Work"
        if portfolio
        else r"Avoid|Watchlist|Starter Position|Core Hold|Add / Increase|Reduce / Trim|Exit"
        r"|Requires More Work"
    )
    records = [
        fact
        for fact in module.facts
        if _names_section(metadata.get(fact.table_id), heading)
        and (fact.text or "").startswith(prefix)
    ]
    if not records:
        return None
    match = re.match(
        re.escape(prefix) + " (" + choices + r")(?:\.(?:\s|$)|$)",
        records[0].text or "",
    )
    source_ref = next(
        (
            ref
            for ref in refs.get((module.module_id, records[0].fact_id), ())
            if ref.startswith("C")
        ),
        None,
    )
    if len(records) != 1 or match is None or source_ref is None:
        raise ValueError(
            "markdown_posture: one explicit terminal CP-6 posture with a citation required"
        )
    return CallItem(
        kind="fact",
        label="Portfolio posture" if portfolio else "Action bias",
        value_text=match[1],
        ref_id=source_ref,
    )


def _yield_observations(
    module: ModuleView, table: ReportTable, as_of: date
) -> tuple[ModuleView, tuple[str, ...], tuple[_ChartPoint, ...]]:
    """Type explicit yield cells for the existing figure; retain the literal table unchanged."""
    if (
        module.module_id not in {"CP-3", "CP-3D"}
        or table.row_header != "Instrument"
        or tuple(c.label for c in table.columns) != ("Maturity", "Price basis", "Yield, %")
    ):
        raise ValueError("markdown_yield: expected Instrument / Maturity / Price basis / Yield, %")
    facts = {f.fact_id: f for f in module.facts}
    tid = "chart-" + table.table_id
    values, rows, points = [], [], []
    seen = set()
    maturities: dict[str, str] = {}
    for index, row in enumerate(table.rows):
        maturity, basis, source = (facts[fid] for fid in row.fact_ids)
        if (
            maturity.status != "known"
            or maturity.text is None
            or date.fromisoformat(maturity.text).isoformat() != maturity.text
            or date.fromisoformat(maturity.text) <= as_of
            or basis.text not in {"Assume clean", "Assume dirty"}
        ):
            raise ValueError(
                "markdown_yield: future ISO maturity and explicit price assumption required"
            )
        if maturities.setdefault(row.label, maturity.text) != maturity.text:
            raise ValueError("markdown_yield: conflicting maturities for one instrument")
        key = (row.label, basis.text)
        if key in seen:
            raise ValueError(
                "markdown_yield: duplicate instrument/maturity/price-basis observation"
            )
        seen.add(key)
        amount = None
        decimals = None
        if source.status == "known":
            token = source.text or ""
            if len(token) > 64 or re.fullmatch(r"[+-]?[0-9]+(?:\.[0-9]+)?", token) is None:
                raise ValueError(
                    "markdown_yield: yield must be a finite plain percentage-point token"
                )
            value = Decimal(token)
            # Decimal construction is exact; this is unit representation, not a yield calculation.
            amount = value.scaleb(-2, context=Context(prec=max(28, len(value.as_tuple().digits))))
            decimals = min(6, len(token.partition(".")[2]))
        fact_id = f"{tid}.r{index}.value"
        values.append(
            Fact(
                fact_id=fact_id,
                table_id=tid,
                row_id=f"r{index}",
                field="value",
                label=row.label,
                amount=amount,
                status=source.status,
                unit="PERCENT",
                period=as_of.isoformat(),
                decimals=decimals,
                citations=source.citations,
                limitation=source.limitation,
                basis="Conditional model yield copied from Markdown; percentage points / 100 for display, no repricing.",
                value_class="source",
            )
        )
        category = f"{maturity.text} · {row.label}"
        rows.append(
            TableRow(row_id=f"r{index}", label=f"{category} · {basis.text}", fact_ids=(fact_id,))
        )
        points.append(_ChartPoint(series=basis.text, category=category, fact_id=fact_id))
    if len(seen) != 2 * len(maturities):
        raise ValueError(
            "markdown_yield: both price-basis rows required; retain missing yields as blanks"
        )
    if not any(f.amount is not None for f in values):
        raise ValueError(
            "markdown_yield: at least one numeric observation required; missing is not zero"
        )
    typed = ReportTable(
        table_id=tid,
        title="Conditional maturity yield numeric view",
        row_header="Observation",
        columns=(TableColumn(field="value", label="Yield, %"),),
        rows=tuple(rows),
    )
    updated = module.model_copy(
        update={"facts": (*module.facts, *values), "tables": (*module.tables, typed)}
    )
    points.sort(key=lambda p: (p.category, p.series))
    return updated, tuple(dict.fromkeys(p.series for p in points)), tuple(points)


def _token_decimals(token: str, chart_unit: str | None) -> int:
    """Places to show a copied source token: as many as it was written to, at most six.

    A `%` chart reads the token as a fraction (0.0725 is 7.25%), so two of its places are the
    percent scaling. A gap has no digits to show and keeps the class default.
    """
    written = len(found[1]) if (found := re.search(r"\.(\d+)", token)) else 0
    return min(6, max(0, written - 2) if chart_unit == "%" else written)


YEAR = re.compile(r"(?<![0-9])([0-9]{4})(?:-([0-9]{2})-[0-9]{2})?(?![0-9])")
PART = re.compile(r"(?<![A-Za-z])([QH])([1-4])(?![0-9])")


def _period_key(label: str) -> tuple[str, int, int] | None:
    """(granularity, year, part) of a period label: `FY2024` ("year", 2024, 0), `Q3 2024`
    ("Q", 2024, 3), `H1 2024` ("H", 2024, 1), `2024-09-30` ("date", 2024, 9); None without a
    year."""
    year = YEAR.search(label)
    if year is None:
        return None
    if year[2]:
        return ("date", int(year[1]), int(year[2]))
    part = PART.search(label)
    return (part[1], int(year[1]), int(part[2])) if part else ("year", int(year[1]), 0)


def _chronological(points: tuple[_ChartPoint, ...]) -> tuple[_ChartPoint, ...]:
    """Oldest period first, so time reads left to right whatever order the table was written in.

    Only the order of the points changes, never a value or label. The authored order stays unless
    every category has a key, all of one granularity, and no two categories share one: a label
    without a year, `Jun 2024` beside `Dec 2024`, or `FY2024` beside `Q1 2024` cannot be placed.
    """
    keys = {p.category: _period_key(p.category) for p in points}
    known = {category: key for category, key in keys.items() if key is not None}
    granularities = {key[0] for key in known.values()}
    if len(known) < len(keys) or len(set(known.values())) < len(known) or len(granularities) > 1:
        return points
    return tuple(sorted(points, key=lambda p: known[p.category]))


def _require_reporting_unit(
    facts: dict[str, Fact], row: TableRow, columns: list[str], column: str, route: MarkdownRoute
) -> None:
    """Refuse a number its own `Reporting unit` cell places in another unit than the chart's;
    a table without that column makes no claim. Nothing is converted or relabelled."""
    if "Reporting unit" not in columns:
        return
    own = (facts[row.fact_ids[columns.index("Reporting unit")]].text or "").strip()
    if own != route.chart_unit:
        raise ValueError(
            f"markdown_chart: {row.label} {column} is reported in {own or 'no unit'}, "
            f"not {route.chart_unit}; write `Not supplied: reported in <unit>`"
        )


def _numeric_observations(
    module: ModuleView, table: ReportTable, route: MarkdownRoute
) -> tuple[ModuleView, tuple[str, ...], tuple[_ChartPoint, ...]]:
    """Copy explicitly selected cells into the existing charts without calculating finance."""
    columns = [column.label for column in table.columns]
    labels = [row.label for row in table.rows]
    if (
        len(set(columns)) != len(columns)
        or len(set(labels)) != len(labels)
        or len(set(route.value_columns)) != len(route.value_columns)
        or len(set(route.row_labels)) != len(route.row_labels)
        or not set(route.value_columns) <= set(columns)
        or not set(route.row_labels) <= set(labels)
    ):
        raise ValueError("markdown_chart: unique source rows and columns must match selectors")
    selected = [row for row in table.rows if not route.row_labels or row.label in route.row_labels]
    facts = {fact.fact_id: fact for fact in module.facts}
    tid = "chart-" + route.block_id + "-" + str(route.figure_id)
    values: list[Fact] = []
    rows: list[TableRow] = []
    points: list[_ChartPoint] = []
    for row in selected:
        for column in route.value_columns:
            source = facts[row.fact_ids[columns.index(column)]]
            if re.search(r"per\s+share|USD\s*/\s*share|million.*shares", row.label, re.IGNORECASE):
                raise ValueError(
                    "markdown_chart: share/per-share quantities are not monetary totals"
                )
            amount = source.amount
            missing = source.status != "known"
            if amount is not None or module.module_id == "CP-MODEL":
                expected = {"x": "MULTIPLE", "US$m": "MILLIONS", "%": "PERCENT"}[
                    route.chart_unit or ""
                ]
                if (
                    source.unit != expected
                    or source.scale != (Decimal(1000000) if expected == "MILLIONS" else Decimal(1))
                    or (expected == "MILLIONS" and source.currency != "USD")
                    or (amount is not None and not amount.is_finite())
                ):
                    raise ValueError("markdown_chart: typed source unit/currency differs")
            else:
                token = source.text or ""
                missing = missing or is_gap(token)
                if not missing:
                    _require_reporting_unit(facts, row, columns, column, route)
                    if len(token) > 64 or not SOURCE_NUMBER.fullmatch(token):
                        raise ValueError(
                            "markdown_chart: selected value must be an exact finite number "
                            "or explicit gap"
                        )
                    amount = Decimal(token.replace(",", "").replace("(", "-").replace(")", ""))
            series, category = (
                (row.label, column)
                if route.orientation == "period-columns"
                else (column, row.label)
            )
            if module.module_id == "CP-MODEL":
                points.append(_ChartPoint(series=series, category=category, fact_id=source.fact_id))
                continue
            fid = f"{tid}.r{len(values)}.value"
            values.append(
                Fact(
                    fact_id=fid,
                    table_id=tid,
                    row_id=f"r{len(values)}",
                    field="value",
                    label=source.label,
                    amount=amount,
                    status="missing" if missing else "known",
                    unit={"x": "MULTIPLE", "US$m": "MILLIONS", "%": "PERCENT"}[
                        route.chart_unit or ""
                    ],
                    scale=Decimal(1000000) if route.chart_unit == "US$m" else Decimal(1),
                    currency="USD" if route.chart_unit == "US$m" else None,
                    period=category,
                    decimals=source.decimals
                    if source.amount is not None
                    else _token_decimals(source.text or "", route.chart_unit),
                    citations=source.citations,
                    limitation=(source.limitation or source.text or "Missing source observation")
                    if missing
                    else source.limitation,
                    basis=source.basis
                    or "Exact selected handoff value; no new financial calculation.",
                    value_class=source.value_class,
                    calculation_id=source.calculation_id,
                    calculation_status=source.calculation_status,
                    formula=source.formula,
                    denominator=source.denominator,
                )
            )
            rows.append(
                TableRow(row_id=f"r{len(rows)}", label=f"{series} · {category}", fact_ids=(fid,))
            )
            points.append(_ChartPoint(series=series, category=category, fact_id=fid))
    if not points:
        raise ValueError("markdown_chart: no selected observations")
    all_series = tuple(dict.fromkeys(p.series for p in points))
    chronological = _chronological(tuple(points))
    if module.module_id == "CP-MODEL":
        return module, all_series, chronological
    typed = ReportTable(
        table_id=tid,
        title=route.label or table.title,
        row_header="Observation",
        columns=(TableColumn(field="value", label=route.chart_unit or "Value"),),
        rows=tuple(rows),
    )
    return (
        module.model_copy(
            update={"facts": (*module.facts, *values), "tables": (*module.tables, typed)}
        ),
        all_series,
        chronological,
    )


def require_issuer(run: Run, aliases: tuple[str, ...], module_id: str, lines: list[str]) -> None:
    """The handoff's title or Request section must name the run's issuer."""
    declaration = lines[0] + "\n" + "\n".join(line for _, line in section(lines, "Request"))
    if not names_issuer(declaration, (run.issuer_name, *aliases, run.issuer_id)):
        raise ValueError(
            "markdown_issuer: handoff title or Request must identify the selected issuer: "
            + module_id
        )


def _section_sentences(bound: tuple[Binding, ...], modules: list[ModuleView]) -> tuple[str, ...]:
    """Unit and limitation sentences written beside the bound tables in their handoff sections."""
    tables = {(m.module_id, t.table_id): t for m in modules for t in m.tables}
    found = (tables.get((e.fact_coord.module_id, str(e.fact_coord.table_id))) for e in bound)
    return tuple(dict.fromkeys(t.limitation for t in found if t is not None and t.limitation))


def _registers(
    bound: tuple[Binding, ...],
    modules: list[ModuleView],
    refs: Mapping[tuple[str, str], tuple[str, ...]],
) -> list[_Slot]:
    """One register per whole table, and one per route for the rows a route selected.

    A partial selection binds each selected row separately; rows of one table that share a
    label are one register, so a route's rows are one tab and tab labels stay distinct.
    """
    by_module = {m.module_id: m for m in modules}
    slots: list[_Slot] = []
    merged: dict[tuple[str, str | None, str], int] = {}
    for entry in bound:
        coord = entry.fact_coord
        slot = _slot(entry, by_module[coord.module_id], refs)
        key = (coord.module_id, coord.table_id, slot.label)
        if coord.row_id is None or key not in merged:
            merged[key] = len(slots)
            slots.append(slot)
        else:
            held = slots[merged[key]]
            slots[merged[key]] = replace(held, rows=held.rows + slot.rows)
    return slots


def markdown_files(  # noqa: C901, PLR0912, PLR0915 - pre-existing complexity (C901 40 at base)
    request: DeliveryRequest, base: Path
) -> dict[str, bytes]:
    """Select literal source sections into the existing requested pathway design."""
    layout = request.layout
    if layout is None:
        raise ValueError("markdown_layout: select explicit presentation routes")
    preset = next(p for p in pathways() if p.id == request.run.pathway)
    if len(set(layout.blocks)) != len(layout.blocks) or not set(layout.blocks) <= set(
        preset.blocks
    ):
        raise ValueError("markdown_layout: unique blocks must belong to the selected pathway")
    if {route.block_id for route in layout.routes} != set(layout.blocks):
        raise ValueError("markdown_layout: every requested block needs explicit handoff routes")
    if any(
        (
            r.module_id not in request.handoffs
            and not (r.module_id == "CP-MODEL" and request.model is not None)
        )
        or r.block_id not in layout.blocks
        for r in layout.routes
    ):
        raise ValueError("markdown_layout: routes must name supplied modules and selected blocks")
    if any(
        _spec_of(block_id).kind not in {"dense", "prose", "keyvalue", "period_grid"}
        and block_id not in {"yield-against-maturity", *STRIP_FIGURES}
        for block_id in layout.blocks
    ):
        raise ValueError("markdown_layout: literal presentation supports table and prose blocks")
    if any(
        route.kind in {"table", "chart"}
        and (route.prefix is not None or _spec_of(route.block_id).kind == "prose")
        for route in layout.routes
    ):
        raise ValueError("markdown_layout: preserve complete table columns in a table block")
    if any(
        route.kind != "chart"
        and route.block_id in STRIP_FIGURES
        and route.block_id != "yield-against-maturity"
        for route in layout.routes
    ):
        raise ValueError("markdown_layout: a chart strip block takes only chart routes")
    module_views = []
    sources = []
    metadata = {}
    files = {}
    for module_id, spec in request.handoffs.items():
        raw = (base / spec.path).read_bytes()
        if hashlib.sha256(raw).hexdigest() != spec.sha256:
            raise ValueError(f"Changed handoff: {module_id}")
        require_issuer(request.run, layout.issuer_aliases, module_id, physical_lines(raw.decode()))
        module, source, meta = literal_module(module_id, raw)
        module_views.append(module)
        sources.append(source)
        metadata[module_id] = meta
        files[module_id + ".md"] = raw
    if request.model is not None:
        from deploy_workflow.model_handoff_delivery import build_model

        if not {"CP-1", "CP-2"} <= set(request.handoffs) or "CP-MODEL" in request.handoffs:
            raise ValueError("markdown_model: annual CP-1 and current CP-2 handoffs required")
        if set(request.model.extra_handoffs) - {"quarter", "forecast"}:
            raise ValueError("model_inputs: unknown extra handoff role")
        inputs = {
            "annual": request.handoffs["CP-1"],
            "current_synthesis": request.handoffs["CP-2"],
            **request.model.extra_handoffs,
        }
        if request.model.forecast_exact is not None:
            inputs["forecast_exact"] = request.model.forecast_exact
        publication = build_model(
            request.run,
            inputs,
            {k: (base / v.path).read_bytes() for k, v in inputs.items()},
            request.model,
        )
        module_views.append(publication.module)
        sources.extend(publication.sources)
        files.update(publication.files)
        metadata["CP-MODEL"] = {t.table_id: (t.title, "table") for t in publication.module.tables}
    entries: dict[str, list[Binding]] = {m.module_id: [] for m in module_views}
    used: set[tuple[str, str]] = set()
    yield_charts: dict[str, tuple[str, tuple[str, ...], tuple[_ChartPoint, ...]]] = {}
    strip_charts: dict[
        str, dict[str, tuple[str, str, str, tuple[str, ...], tuple[_ChartPoint, ...]]]
    ] = {}
    for route in layout.routes:
        module = next(m for m in module_views if m.module_id == route.module_id)
        tables = [
            t
            for t in module.tables
            if metadata[module.module_id][t.table_id]
            == (route.heading, "table" if route.kind == "chart" else route.kind)
            and (route.table_header is None or t.row_header == route.table_header)
            and (route.kind != "chart" or set(route.value_columns) <= {c.label for c in t.columns})
        ]
        if len(tables) != 1:
            raise ValueError(
                f"markdown_selector: expected one "
                f"{route.module_id}/{route.heading}/{route.table_header}"
            )
        table = tables[0]
        facts = {f.fact_id: f for f in module.facts}
        selected = [
            r
            for r in table.rows
            if all((module.module_id, fid) not in used for fid in r.fact_ids)
            and (route.prefix is None or _opens_with(facts[r.fact_ids[0]].text, route.prefix))
        ]
        if not selected and route.kind != "chart":
            raise ValueError(f"markdown_selector: no unused content for {route.heading}")
        if route.kind == "chart":
            if route.figure_id not in STRIP_FIGURES.get(route.block_id, ()):
                raise ValueError("markdown_chart: figure does not belong to this pathway block")
            figure_specs = strip_charts.setdefault(route.block_id, {})
            if route.figure_id in figure_specs:
                raise ValueError("markdown_chart: exactly one selector per figure")
            updated, series, points = _numeric_observations(module, table, route)
            if module.module_id != "CP-MODEL":
                module_views[module_views.index(module)] = updated
                typed = updated.tables[-1]
                metadata[module.module_id][typed.table_id] = (route.heading, "chart")
                entries[module.module_id].append(
                    Binding(
                        fact_coord=FactCoord(module_id=module.module_id, table_id=typed.table_id),
                        block_id=route.block_id,
                        cell_slot=route.figure_id,
                        unit_class=CHART_UNITS[route.chart_unit or ""],
                    )
                )
                used.update((module.module_id, point.fact_id) for point in points)
            figure_specs[route.figure_id] = (
                module.module_id,
                route.label or table.title,
                route.chart_unit or "",
                series,
                points,
            )
            continue
        if route.block_id == "yield-against-maturity":
            if route.kind != "table" or route.block_id in yield_charts:
                raise ValueError("markdown_yield: exactly one complete source table required")
            updated, series, points = _yield_observations(module, table, request.run.as_of)
            module_views[module_views.index(module)] = updated
            typed = updated.tables[-1]
            metadata[module.module_id][typed.table_id] = (route.heading, "chart")
            entries[module.module_id].append(
                Binding(
                    fact_coord=FactCoord(module_id=module.module_id, table_id=typed.table_id),
                    block_id=route.block_id,
                    cell_slot="conditional-yield",
                    unit_class="percent",
                )
            )
            used.update((module.module_id, p.fact_id) for p in points)
            yield_charts[route.block_id] = (module.module_id, series, points)
            continue
        groups = [None] if len(selected) == len(table.rows) else [r.row_id for r in selected]
        for row_id in groups:
            entries[module.module_id].append(
                Binding(
                    fact_coord=FactCoord(
                        module_id=module.module_id, table_id=table.table_id, row_id=row_id
                    ),
                    block_id=route.block_id,
                    cell_slot=f"{module.module_id}-{len(entries[module.module_id])}",
                    unit_class=("amount" if table.table_id == "history" else "multiple")
                    if module.module_id == "CP-MODEL" and table.table_id in {"history", "ratios"}
                    else "text",
                    label=route.label or table.title,
                )
            )
        used.update((module.module_id, fid) for r in selected for fid in r.fact_ids)
    for module in module_views:
        for table in module.tables:
            remaining = [
                r
                for r in table.rows
                if all((module.module_id, fid) not in used for fid in r.fact_ids)
            ]
            groups = [None] if len(remaining) == len(table.rows) else [r.row_id for r in remaining]
            for row_id in groups:
                entries[module.module_id].append(
                    Binding(
                        fact_coord=FactCoord(
                            module_id=module.module_id, table_id=table.table_id, row_id=row_id
                        ),
                        block_id="evidence",
                        cell_slot=f"{module.module_id}-{len(entries[module.module_id])}",
                        unit_class="text",
                    )
                )
    view = View(
        run=request.run,
        mode="candidate",
        modules=tuple(module_views),
        sources=tuple(sources),
        analytical_qualification="partial",
        native_host_qualification="unrun",
    )
    maps = tuple(
        BindingMap(module_id=module_id, entries=tuple(items))
        for module_id, items in entries.items()
    )
    if issues := validate_bindings(view, maps):
        raise ValueError("markdown_bindings: " + "; ".join(issues))
    pathway = preset.model_copy(
        update={
            "blocks": layout.blocks,
            "requested_modules": request.run.requested_modules,
            "title": layout.title or preset.title,
            "question": layout.question or preset.question,
        }
    )
    passports, index = build_index(view)
    refs = _refs_by_fact(index)
    blocks = []
    for block_id in layout.blocks:
        bound = tuple(e for items in entries.values() for e in items if e.block_id == block_id)
        if not bound and block_id not in strip_charts:
            raise ValueError(f"markdown_content: selected block has no handoff content: {block_id}")
        block_spec = _spec_of(block_id)
        labels = tuple(
            dict.fromkeys(r.label for r in layout.routes if r.block_id == block_id and r.label)
        )
        presentation_note = " · ".join(labels) or None
        owner = " · ".join(dict.fromkeys(e.fact_coord.module_id for e in bound))
        if block_spec.kind == "chart":
            if block_id in strip_charts:
                specs = strip_charts.get(block_id, {})
                if set(specs) != set(STRIP_FIGURES[block_id]):
                    raise ValueError(
                        "markdown_chart: supply every requested strip figure, "
                        "preserving explicit gaps"
                    )
                figures = []
                for fig_id in STRIP_FIGURES[block_id]:
                    module_id, title, unit, series, points = specs[fig_id]
                    figures.append(
                        _figure_of_points(
                            block_id,
                            next(m for m in module_views if m.module_id == module_id),
                            refs,
                            fig_id=fig_id,
                            title=title,
                            kind="grouped" if fig_id in {"S.4", "RV.1"} else "line",
                            unit_class=CHART_UNITS[unit],
                            unit=unit,
                            series=series,
                            points=points,
                            placement="above",
                            summary=(
                                "Exact selected handoff/Model observations. Dates, definitions and "
                                "limitations remain in the source evidence; gaps are not zero."
                            ),
                        )
                    )
                blocks.append(
                    Block(
                        block_id=block_id,
                        title=block_spec.title,
                        kind="chart",
                        owner=" · ".join(dict.fromkeys(spec[0] for spec in specs.values())),
                        state="populated",
                        full_analysis_route=next(iter(specs.values()))[0],
                        width="full",
                        figures=tuple(figures),
                    )
                )
                continue
            if block_id not in yield_charts:
                raise ValueError(
                    "markdown_chart: explicit numeric selectors required for each figure"
                )
            module_id, series, points = yield_charts[block_id]
            figure = _figure_of_points(
                block_id,
                next(m for m in module_views if m.module_id == module_id),
                refs,
                fig_id="RV.1",
                title="Conditional maturity yield by note maturity",
                kind="line",
                unit_class="percent",
                unit="%",
                series=series,
                points=points,
                placement="above",
                summary=(
                    "Separate clean/dirty assumptions; categorical note maturities, not an "
                    "observed or fitted curve. Raw values remain in the source table; labels use "
                    "at most six decimal places."
                ),
            )
            blocks.append(
                Block(
                    block_id=block_id,
                    title=block_spec.title,
                    kind="chart",
                    owner=owner,
                    state="populated",
                    full_analysis_route=module_id,
                    width="full",
                    figures=(figure,),
                )
            )
        elif block_spec.kind == "prose":
            blocks.append(
                Block(
                    block_id=block_id,
                    title=block_spec.title,
                    kind="prose",
                    owner=owner,
                    state="populated",
                    full_analysis_route=bound[0].fact_coord.module_id,
                    width="full",
                    lines=_prose_lines(bound, view, refs),
                    note=presentation_note,
                )
            )
        else:
            slots = _registers(bound, module_views, refs)
            primary, *further = slots
            tabs = tuple(
                BlockTab(label=s.label, row_header=s.row_header, columns=s.columns, rows=s.rows)
                for s in further
            )
            blocks.append(
                Block(
                    block_id=block_id,
                    title=block_spec.title,
                    kind=block_spec.kind,
                    owner=owner,
                    state="populated",
                    full_analysis_route=bound[0].fact_coord.module_id,
                    width="full",
                    row_header=primary.row_header,
                    columns=primary.columns,
                    rows=primary.rows,
                    note=" · ".join(
                        dict.fromkeys([*labels, *_section_sentences(bound, module_views)])
                    )
                    or None,
                    tab_label=primary.label if tabs else None,
                    tabs=tabs,
                )
            )
    call, withheld = _call({m.module_id: m for m in module_views}, pathway)
    posture = _portfolio_call(
        next((m for m in module_views if m.module_id == "CP-6"), None),
        metadata.get("CP-6", {}),
        refs,
        portfolio=pathway.id == "portfolio_decision",
    )
    if posture is not None:
        call, withheld = (posture,), None
    if "CP-6" not in request.handoffs:
        withheld = "not_requested"
    report = ReportView(
        pathway=pathway,
        call=call,
        call_withheld=withheld,
        blocks=tuple(blocks),
        passports=passports,
        index=index,
        unplaced=_unplaced(view, pathway, maps),
    )
    rendered = render(view, report)
    if request.model is not None:
        nav = '["model", "Model", "#CP-1"]'
        if rendered.count(nav) != 1:
            raise ValueError("model_shell: main report Model destination changed")
        rendered = rendered.replace(nav, '["model", "Model", "model.html"]')
    anchor = '<div id="call-root"></div>'
    if rendered.count(anchor) != 1:
        raise ValueError("Existing renderer scope-banner location changed")
    files.update(
        {
            "view.json": view.model_dump_json(indent=2).encode(),
            "report-view.json": report.model_dump_json(indent=2).encode(),
            "report.html": rendered.replace(
                anchor,
                '<section id="delivery-scope-banner" class="banner" role="note">'
                + html.escape(layout.scope)
                + "</section>"
                + (
                    '<nav aria-label="Published deliverables">'
                    '<a href="model.html">HTML Model and charts</a> · '
                    '<a href="calculation.json">Calculation JSON</a></nav>'
                    if request.model is not None
                    else ""
                )
                + anchor,
            ).encode(),
        }
    )
    record = {
        "kind": "literal_handoff_delivery",
        "scope": layout.scope,
        "analytical_runtime_executed": False,
        "cp_model_published": request.model is not None,
        "excel_output": False,
        "files": {name: hashlib.sha256(raw).hexdigest() for name, raw in files.items()},
    }
    files["delivery.json"] = (json.dumps(record, indent=2) + "\n").encode()
    return files
