"""The library's store over a hand-written workspace; expected values are written here."""

import fnmatch
import hashlib
import importlib.util
import json
import os
import subprocess
import sys
import threading
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location(
    "library_store", ROOT / "apps/issuer-library/engine/store.py"
)
store = importlib.util.module_from_spec(spec)
spec.loader.exec_module(store)

CP1 = "# CP-1\n\n## Findings\n\n| Item | Value |\n| --- | --- |\n| Revenue | 0 |\n| Debt | not stated |\n"
BETA = "# CP-0\n\n## Request\n\nBeta Group as of 2025-06-30.\n"


def put(root: Path, name: str, text: str) -> str:
    path = root / name
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8")
    return hashlib.sha256(text.encode()).hexdigest()


def delivery(root: Path, folder: str, issuer: str, handoffs: dict[str, str]) -> None:
    files = {name: put(root, f"{folder}/{name}", text) for name, text in handoffs.items()}
    files["report.html"] = put(root, f"{folder}/report.html", "<html>report</html>")
    view = {"run": {"issuer_name": issuer, "as_of": "2025-06-30", "pathway": "credit_snapshot"}}
    files["view.json"] = put(root, f"{folder}/view.json", json.dumps(view))
    put(root, f"{folder}/delivery.json", json.dumps({"files": files, "cp_model_published": False}))


def workspace(root: Path) -> dict:
    put(root, "runs/alpha-001/CP-1.md", CP1)
    put(root, "runs/alpha-001/CP-1-instructions.md", "# skipped\n")
    put(root, "runs/alpha-001/CP-1-selected-input.md", "# input\n")
    put(root, "runs/alpha-001/CP-2.md", "Body before any heading\n\n## Later\n\nText\n")
    put(root, "runs/alpha-001/CP-4A.md", "# CP-4A\n\nExtra module.\n")
    put(root, "runs/empty-001/notes.txt", "no handoff\n")
    put(
        root,
        "runs/launched/workflow.json",
        json.dumps(
            {
                "run": {
                    "issuer_name": "Beta Group",
                    "as_of": "2025-06-30",
                    "pathway": "credit_snapshot",
                }
            }
        ),
    )
    delivery(root, "runs/launched/deliveries/abc", "Beta Group", {"CP-0.md": BETA})
    delivery(
        root,
        "deliverables/alpha-report",
        "Alpha Holdings",
        {"CP-1.md": CP1, "CP-9.md": "# Not in any run\n"},
    )
    blank = {"sector": "Unclassified", "period": "", "artifacts": []}
    return {
        "issues": ["runs/x: earlier issue"],
        "real": [
            {
                "id": "alpha-001",
                "name": "Alpha Holdings",
                "sector": "Industrials",
                "period": "FY2024",
                "artifacts": [
                    {
                        "folder": "deliverables/alpha-report",
                        "label": "Alpha annual",
                        "state": "final",
                        "available": True,
                        "href": "/files/deliverables/alpha-report/report.html?sha256=r",
                    }
                ],
            },
            {"id": "empty-001", "name": "empty-001", **blank},
            {
                "id": "launched",
                "name": "launched",
                **blank,
                "artifacts": [
                    {
                        "folder": "runs/launched/deliveries/abc",
                        "label": "abc",
                        "state": "candidate",
                        "available": True,
                        "href": "/files/runs/launched/deliveries/abc/report.html?sha256=s",
                    }
                ],
            },
            {
                "id": "delivery:orphan",
                "name": "Gamma",
                "sector": "",
                "period": "",
                "artifacts": [
                    {
                        "folder": "deliverables/broken",
                        "label": "broken",
                        "state": "candidate",
                        "available": False,
                        "href": "",
                        "issue": "Missing",
                    }
                ],
            },
        ],
    }


def test_runs_take_labels_from_the_catalogue_and_launcher_manifest(tmp_path):
    result = store.workspace_store(tmp_path, workspace(tmp_path))
    assert list(result["runs"]) == ["alpha-001", "empty-001", "launched"]
    alpha, beta = result["runs"]["alpha-001"], result["runs"]["launched"]
    assert (alpha["issuer"], alpha["sector"], alpha["period"]) == (
        "Alpha Holdings",
        "Industrials",
        "FY2024",
    )
    assert (beta["issuer"], beta["title"], beta["period"]) == (
        "Beta Group",
        "Beta Group",
        "As of 30 June 2025",
    )
    assert result["runs"]["empty-001"]["first"] == "W-Overview"
    assert beta["first"] == "CP-0"


def test_outputs_keep_exact_values_identity_and_a_serving_link(tmp_path):
    result = store.workspace_store(tmp_path, workspace(tmp_path))
    output = result["outputs"]["alpha-001/CP-1.md"]
    rows = output["sections"][1]["blocks"][0]["rows"]
    assert [row["cells"] for row in rows] == [["Revenue", "0"], ["Debt", "not stated"]]
    assert output["sha256"] == hashlib.sha256(CP1.encode()).hexdigest()
    assert output["href"] == f"/files/runs/alpha-001/CP-1.md?sha256={output['sha256']}"
    assert "alpha-001/CP-1-instructions.md" not in result["outputs"]
    assert list(result["inputs"]) == ["alpha-001/CP-1-selected-input.md"]
    assert result["inputs"]["alpha-001/CP-1-selected-input.md"]["href"].startswith(
        "/files/runs/alpha-001/"
    )
    assert result["runs"]["alpha-001"]["modules"]["CP-4A"]["outputs"] == ["alpha-001/CP-4A.md"]


def test_delivered_handoffs_of_a_launcher_run_are_its_outputs(tmp_path):
    result = store.workspace_store(tmp_path, workspace(tmp_path))
    output = result["outputs"]["launched/deliveries/abc/CP-0.md"]
    assert output["source"] == "deliveries/abc/CP-0.md"
    assert output["run"] == "launched" and output["module"] == "CP-0"
    assert output["href"].startswith("/files/runs/launched/deliveries/abc/CP-0.md?sha256=")


def test_a_handoff_that_cannot_be_structured_stays_readable_and_is_flagged(tmp_path):
    result = store.workspace_store(tmp_path, workspace(tmp_path))
    output = result["outputs"]["alpha-001/CP-2.md"]
    assert "Body before" in output["parseError"]
    block = output["sections"][0]["blocks"][0]
    assert block["type"] == "text" and block["text"].startswith("Body before any heading")
    assert "## Later" in block["text"]
    assert any("alpha-001/CP-2.md" in issue for issue in result["issues"])


def test_reports_trace_handoffs_by_hash_and_name_what_has_no_match(tmp_path):
    result = store.workspace_store(tmp_path, workspace(tmp_path))
    reports = {report["id"]: report for report in result["reports"]}
    assert list(reports) == ["alpha-report", "abc"]
    alpha = reports["alpha-report"]
    assert alpha["label"] == "Alpha annual" and alpha["issuer"] == "Alpha Holdings"
    assert alpha["href"] == "/files/deliverables/alpha-report/report.html?sha256=r&embedded=1"
    assert alpha["download"] == "/files/deliverables/alpha-report/report.html?sha256=r&download=1"
    assert alpha["build"] is None and alpha["modelPublished"] is False
    traced = {row["module"]: row for row in alpha["builtFrom"]}
    assert traced["CP-1"]["run"] == "alpha-001" and traced["CP-1"]["source"] == "alpha-001/CP-1.md"
    assert traced["CP-1"]["output"] is True
    assert traced["CP-9"]["run"] is None
    assert {f["name"] for f in alpha["files"]} == {"CP-1.md", "CP-9.md", "report.html", "view.json"}
    beta = reports["abc"]
    assert beta["label"] == "Beta Group · as of 30 June 2025" and beta["issuer"] == "Beta Group"
    assert beta["builtFrom"][0]["run"] == "launched"


def _report_with_view(tmp_path, **declared):
    catalogue = workspace(tmp_path)
    view_path = tmp_path / "deliverables/alpha-report/view.json"
    view = json.loads(view_path.read_text(encoding="utf-8"))
    view.update(declared)
    view_path.write_text(json.dumps(view), encoding="utf-8")
    reports = {r["id"]: r for r in store.workspace_store(tmp_path, catalogue)["reports"]}
    return reports["alpha-report"]


@pytest.mark.parametrize(
    ("declared", "mode", "qualification"),
    [
        ({"mode": "accepted", "analytical_qualification": "qualified"}, "accepted", "qualified"),
        ({"mode": "candidate", "analytical_qualification": "partial"}, "candidate", "partial"),
        ({"analytical_qualification": "unrun"}, None, "unrun"),
        ({"mode": "candidate", "analytical_qualification": "mystery"}, "candidate", "mystery"),
        ({"mode": "candidate"}, "candidate", None),
        ({}, None, None),
    ],
)
def test_a_report_carries_the_mode_and_qualification_it_declares(
    tmp_path, declared, mode, qualification
):
    report = _report_with_view(tmp_path, **declared)
    assert report["mode"] == mode
    assert report["qualification"] == qualification


def test_the_latest_curated_build_is_labelled_latest_build():
    assert store.CURATED_REPORTS["tdg-fy2024-snapshot-7"][1] == "Latest build"
    assert store.CURATED_REPORTS["tdg-fy2024-snapshot"][1] == "Superseded"
    assert "Latest" not in {status for _, status in store.CURATED_REPORTS.values()}


def test_a_curated_pin_that_no_longer_matches_is_dropped_not_fatal(tmp_path):
    catalogue = {
        "issues": [],
        "real": [
            {"id": "tdg-002", "name": "TransDigm", "sector": "", "period": "", "artifacts": []}
        ],
    }
    put(tmp_path, "runs/tdg-002/CP-1-attempt-2.md", "# Changed\n\nNo curated heading here.\n")
    result = store.workspace_store(tmp_path, catalogue)
    assert "CP-1" not in result["pins"]
    assert "tdg-002/CP-1-attempt-2.md" in result["outputs"]
    assert any("CP-1" in issue and "pin" in issue for issue in result["issues"])
    run = result["runs"]["tdg-002"]
    assert (run["issuer"], run["run"]) == ("TransDigm Group", "TDG-002")  # Curated reading label.


def test_empty_workspace_and_unsafe_folder_names(tmp_path):
    empty = store.workspace_store(tmp_path, {"issues": [], "real": []})
    assert (empty["runs"], empty["outputs"], empty["reports"], empty["pins"]) == ({}, {}, [], {})
    assert isinstance(empty["visuals"], list)
    unsafe = store.workspace_store(
        tmp_path,
        {
            "issues": [],
            "real": [{"id": 'bad"name', "name": "x", "sector": "", "period": "", "artifacts": []}],
        },
    )
    assert unsafe["runs"] == {} and any('bad"name' in issue for issue in unsafe["issues"])


def test_a_web_run_gets_a_short_label_and_keeps_its_folder_key(tmp_path):
    folder = "web-" + "e8" * 16
    put(
        tmp_path,
        f"runs/{folder}/workflow.json",
        json.dumps({"run": {"issuer_name": "Beta Group", "as_of": "2025-06-30"}}),
    )
    catalogue = {
        "issues": [],
        "real": [
            {"id": folder, "name": folder, "sector": "Unclassified", "period": "", "artifacts": []}
        ],
    }
    run = store.workspace_store(tmp_path, catalogue)["runs"][folder]
    assert run["run"] == "WEB-E8E8E8E8" and run["folder"] == folder


def test_one_unreadable_run_or_report_does_not_take_the_library_down(tmp_path):
    catalogue = workspace(tmp_path)
    locked = tmp_path / "runs/alpha-001/CP-4A.md"
    locked.chmod(0)
    (tmp_path / "runs/launched/deliveries/abc/view.json").write_text("{}")
    try:
        result = store.workspace_store(tmp_path, catalogue)
    finally:
        locked.chmod(0o600)
    assert list(result["runs"]) == ["empty-001", "launched"]
    assert any(issue.startswith("alpha-001:") for issue in result["issues"])
    assert result["reports"][0]["id"] == "alpha-report" and [
        r["id"] for r in result["reports"]
    ] == ["alpha-report"]
    assert any("deliveries/abc" in issue for issue in result["issues"])


def plain_run(folder: str) -> dict:
    return {"issues": [], "real": [{"id": folder, "name": folder, "artifacts": []}]}


def test_files_that_are_not_handoffs_do_not_take_the_library_down(tmp_path):
    put(tmp_path, "runs/odd/CP-0.md", BETA)
    put(tmp_path, "runs/odd/CP-notes.md", "# Someone's notes\n")
    (tmp_path / "runs/odd/CP-7.md").mkdir()
    result = store.workspace_store(tmp_path, plain_run("odd"))
    assert list(result["outputs"]) == ["odd/CP-0.md"] and result["issues"] == []


def test_a_link_out_of_the_run_is_not_read(tmp_path):
    put(tmp_path, "private.md", "# Private\n\nNot part of any run.\n")
    put(tmp_path, "runs/linked/CP-0.md", BETA)
    (tmp_path / "runs/linked/CP-1.md").symlink_to(tmp_path / "private.md")
    result = store.workspace_store(tmp_path, plain_run("linked"))
    assert list(result["outputs"]) == ["linked/CP-0.md"]


def test_runs_carry_the_recorded_workflow_and_as_of_and_none_when_unrecorded(tmp_path):
    runs = store.workspace_store(tmp_path, workspace(tmp_path))["runs"]
    assert (runs["launched"]["pathway"], runs["launched"]["asOf"]) == (
        "credit_snapshot",
        "2025-06-30",
    )
    assert (runs["alpha-001"]["pathway"], runs["alpha-001"]["asOf"]) == (None, None)


def test_a_malformed_run_manifest_falls_back_to_the_catalogue(tmp_path):
    for number, manifest in enumerate(
        ('{"run": null}', '{"run": "x"}', "[]", '{"run": {"issuer_name": 7}}')
    ):
        folder = f"odd-{number}"
        put(tmp_path, f"runs/{folder}/workflow.json", manifest)
        run = store.workspace_store(tmp_path, plain_run(folder))["runs"][folder]
        assert run["issuer"] == folder and run["period"] == "Period not recorded"
        assert run["pathway"] is None and run["asOf"] is None


def test_two_different_deliveries_of_a_module_can_be_told_apart(tmp_path):
    put(tmp_path, "runs/twice/deliveries/aaaaaaaaaaaa/CP-0.md", BETA)
    put(tmp_path, "runs/twice/deliveries/bbbbbbbbbbbb/CP-0.md", BETA + "\nRepaired.\n")
    result = store.workspace_store(tmp_path, plain_run("twice"))
    labels = sorted(output["label"] for output in result["outputs"].values())
    assert labels == ["CP-0 · delivery aaaaaaaa", "CP-0 · delivery bbbbbbbb"]
    assert result["runs"]["twice"]["modules"]["CP-0"]["default"] is None


def test_the_library_reads_a_workspace_in_its_own_small_process(tmp_path):
    """Every page load runs this, so it must not import the engine; Windows pays for each import."""
    text = (
        "# CP-0\n\n## Findings\n\nNet debt ≥ 0 at Şişli − a Windows code page cannot print these.\n"
    )
    put(tmp_path, "runs/own/CP-0.md", text)
    script = ROOT / "apps/issuer-library/engine/store.py"
    probe = (
        "import runpy,sys;sys.argv=[sys.argv[1],sys.argv[2]];"
        "runpy.run_path(sys.argv[0],run_name='__main__');"
        "sys.stderr.write(' '.join(m for m in sys.modules if m.split('.')[0] in ('deploy_workflow','deploy_vii','pydantic')))"
    )
    done = subprocess.run(
        [sys.executable, "-I", "-B", "-X", "utf8", "-c", probe, str(script), str(tmp_path)],
        input=json.dumps(plain_run("own")).encode(),
        capture_output=True,
        check=True,
    )
    assert done.stderr == b""
    output = json.loads(done.stdout.decode("utf-8"))["outputs"]["own/CP-0.md"]
    assert output["sections"][1]["blocks"][0]["text"].startswith("Net debt ≥ 0 at Şişli −")


def test_one_run_that_breaks_the_parser_is_reported_and_the_rest_stay(tmp_path, monkeypatch):
    put(tmp_path, "runs/good/CP-0.md", BETA)
    put(tmp_path, "runs/bad/CP-0.md", BETA)
    real = store.output_label

    def label(module, path, siblings):
        if path.parent.name == "bad":
            raise IndexError("an unforeseen file name")
        return real(module, path, siblings)

    monkeypatch.setattr(store, "output_label", label)
    catalogue = {"issues": [], "real": [*plain_run("good")["real"], *plain_run("bad")["real"]]}
    result = store.workspace_store(tmp_path, catalogue)
    assert list(result["runs"]) == ["good"]
    assert any(issue.startswith("bad: could not be read") for issue in result["issues"])


def test_windows_case_blind_matching_adds_no_odd_handoffs(tmp_path, monkeypatch):
    put(tmp_path, "runs/case/CP-0.md", BETA)
    put(tmp_path, "runs/case/CP-1.MD", BETA + "Upper case suffix.\n")
    put(tmp_path, "runs/case/cp-2.md", BETA + "Lower case name.\n")

    def case_blind(self, pattern):
        if "/" in pattern:
            return iter(())
        return (p for p in self.iterdir() if fnmatch.fnmatchcase(p.name.lower(), pattern.lower()))

    monkeypatch.setattr(Path, "glob", case_blind)
    result = store.workspace_store(tmp_path, plain_run("case"))
    assert list(result["outputs"]) == ["case/CP-0.md"] and result["issues"] == []


READER_FIXTURE = ROOT / "apps/issuer-library/designs/reader-fixture/CP-1.md"


def reader_sections(text=None):
    return store.parse_source(READER_FIXTURE.read_text() if text is None else text)


def test_reader_fields_read_the_synthetic_handoff():
    fields = store.reader_fields(reader_sections())
    summary = fields["summary"]
    assert summary["bottomLine"] == (
        "Total debt / EBITDA fell from 4.20x to 3.60x while liquidity held above 275."
    )
    assert summary["confidence"] == "Medium"
    assert summary["limitation"] == "The maturity schedule has no FY2027 figure."
    assert summary["line"] == 17
    assert [(f["finding"], f["impact"], f["confidence"]) for f in summary["findings"]] == [
        (
            "Leverage fell over the two years.",
            "More debt capacity before a covenant test.",
            "Medium",
        ),
        (
            "Liquidity held. <img src=x onerror=alert(document.domain)>",
            "No near-term funding gap is shown.",
            "Low",
        ),
    ]
    assert [f["line"] for f in summary["findings"]] == [21, 22]
    assert fields["charts"] == [
        {"title": "Leverage", "unit": "x", "table": 26, "columns": [1, 2]},
        {"title": "Interest cover", "unit": "x", "table": 33, "columns": [1]},
        {"title": "Liquidity", "unit": "US$m", "table": 40, "columns": [1, 2]},
        {"title": "Debt maturities", "unit": "US$m", "table": 47, "columns": [1]},
    ]
    assert fields["issue"] is None


def test_the_fixture_passes_the_launcher_reader_check():
    sys.path.insert(0, str(ROOT / "src"))
    from deploy_workflow.reader_summary import reader_issues

    assert reader_issues(READER_FIXTURE.read_text()) == ()


def test_a_handoff_without_a_reader_section_has_no_issue():
    assert store.reader_fields(reader_sections(CP1)) == {
        "summary": None,
        "charts": [],
        "issue": None,
    }


@pytest.mark.parametrize(
    ("old", "new", "named"),
    [
        (
            "| Bottom line | Confidence | Main limitation |",
            "| Conclusion | Confidence | Limit |",
            "Reader summary",
        ),
        (
            "| Finding | Creditor impact | Confidence |",
            "| Item | Effect | Confidence |",
            "Reader summary",
        ),
        ("| Period | Debt maturing |", "| Year | Debt maturing |", "Chart data: debt maturities"),
    ],
)
def test_a_malformed_section_is_named_and_the_handoff_still_parses(old, new, named):
    fields = store.reader_fields(reader_sections(READER_FIXTURE.read_text().replace(old, new)))
    assert named in fields["issue"]
    if "Chart" in named:
        assert fields["summary"] is not None and len(fields["charts"]) == 3
    else:
        assert fields["summary"] is None and len(fields["charts"]) == 4


def test_a_malformed_reader_section_reaches_the_workspace_issues(tmp_path):
    folder = tmp_path / "runs/web-1"
    folder.mkdir(parents=True)
    broken = READER_FIXTURE.read_text().replace("| Bottom line |", "| Conclusion |")
    (folder / "CP-1.md").write_text(broken)
    catalogue = {
        "issues": [],
        "real": [{"id": "web-1", "name": "web-1", "sector": "", "period": "", "artifacts": []}],
    }
    result = store.workspace_store(tmp_path, catalogue)
    assert any("web-1/CP-1.md" in issue and "Reader summary" in issue for issue in result["issues"])
    output = result["outputs"]["web-1/CP-1.md"]
    assert output["summary"] is None
    assert any(s["heading"] == "Chart data: leverage" for s in output["sections"])


# Issuer identity: expected keys, headings and terms are written here, not computed by the store.
def view_delivery(
    root: Path, folder: str, run_id: str, issuer_id: str | None, name: str, available: bool = True
) -> dict:
    """A deliverable whose view.json says which run and issuer it belongs to; returns its catalogue artifact."""
    run = {"run_id": run_id, "issuer_name": name, "as_of": "2025-06-30"}
    if issuer_id is not None:
        run["issuer_id"] = issuer_id
    files = {
        "report.html": put(root, f"{folder}/report.html", "<html>r</html>"),
        "view.json": put(root, f"{folder}/view.json", json.dumps({"run": run})),
    }
    put(root, f"{folder}/delivery.json", json.dumps({"files": files}))
    href = f"/files/{folder}/report.html?sha256=x"
    return {
        "folder": folder,
        "label": folder,
        "state": "final",
        "available": available,
        "href": href,
    }


def identity_catalogue(root: Path, runs: dict, deliveries: list) -> dict:
    """runs: folder -> (catalogue name or None for the folder name, catalogue issuer or None, manifest or None)."""
    real = []
    for folder, (name, issuer, manifest) in runs.items():
        put(root, f"runs/{folder}/CP-0.md", "# CP-0\n\n## Request\n\nText.\n")
        if manifest is not None:
            put(root, f"runs/{folder}/workflow.json", json.dumps({"run": manifest}))
        real.append(
            {
                "id": folder,
                "name": name or folder,
                "issuer": issuer or "Unclassified",
                "sector": "",
                "period": "",
                "artifacts": [],
            }
        )
    for artifact in deliveries:
        pseudo = {"id": f"delivery:{Path(artifact['folder']).name}", "name": "x", "sector": ""}
        real.append({**pseudo, "period": "", "artifacts": [artifact]})
    return {"issues": [], "real": real}


def identities(tmp_path, runs, deliveries=()):
    result = store.workspace_store(tmp_path, identity_catalogue(tmp_path, runs, list(deliveries)))
    return result, result["runs"]


def test_agreeing_deliveries_name_an_otherwise_unrecorded_run(tmp_path):
    first = view_delivery(tmp_path, "deliverables/d1", "plain-001", "DLT", "Delta Corp")
    second = view_delivery(tmp_path, "deliverables/d2", "plain-001", "dlt", "Delta Corp")
    result, runs = identities(tmp_path, {"plain-001": (None, None, None)}, [first, second])
    run = runs["plain-001"]
    assert (run["issuer"], run["title"]) == ("Delta Corp", "Delta Corp")
    assert (run["issuerKey"], run["issuerHeading"]) == ("id:dlt", "Delta Corp")
    assert run["issuerTerms"] == ["DLT", "Delta Corp"]
    assert not any("different issuers" in issue for issue in result["issues"])


def test_disagreeing_deliveries_leave_the_run_unrecorded_and_say_so(tmp_path):
    one = view_delivery(tmp_path, "deliverables/d1", "plain-001", "AAA", "Alpha Corp")
    other = view_delivery(tmp_path, "deliverables/d2", "plain-001", "BBB", "Beta Corp")
    result, runs = identities(tmp_path, {"plain-001": (None, None, None)}, [one, other])
    run = runs["plain-001"]
    assert (run["issuer"], run["issuerKey"], run["issuerHeading"], run["issuerTerms"]) == (
        "plain-001",
        None,
        None,
        [],
    )
    assert (
        "runs/plain-001: deliverables name different issuers; issuer left unrecorded"
        in result["issues"]
    )


def test_deliveries_that_agree_on_the_id_but_not_the_name_disagree(tmp_path):
    one = view_delivery(tmp_path, "deliverables/d1", "plain-001", "AAA", "Alpha Corp")
    other = view_delivery(tmp_path, "deliverables/d2", "plain-001", "AAA", "Alpha Corporation")
    result, runs = identities(tmp_path, {"plain-001": (None, None, None)}, [one, other])
    assert runs["plain-001"]["issuerKey"] is None
    assert any("different issuers" in issue for issue in result["issues"])


def test_an_unavailable_delivery_names_nobody(tmp_path):
    gone = view_delivery(tmp_path, "deliverables/d1", "plain-001", "AAA", "Alpha", available=False)
    result, runs = identities(tmp_path, {"plain-001": (None, None, None)}, [gone])
    assert runs["plain-001"]["issuerKey"] is None and runs["plain-001"]["issuer"] == "plain-001"
    assert not any("different issuers" in issue for issue in result["issues"])


def test_a_delivery_for_another_run_names_nobody(tmp_path):
    other = view_delivery(tmp_path, "deliverables/d1", "someone-else", "AAA", "Alpha")
    _, runs = identities(tmp_path, {"plain-001": (None, None, None)}, [other])
    assert runs["plain-001"]["issuerKey"] is None


def test_a_recorded_name_outranks_a_delivery(tmp_path):
    delivered = view_delivery(tmp_path, "deliverables/d1", "named-001", "ZZZ", "Delivered Name")
    manifest = {"issuer_name": "Manifest Name", "issuer_id": "MAN"}
    _, runs = identities(tmp_path, {"named-001": (None, None, manifest)}, [delivered])
    assert (runs["named-001"]["issuer"], runs["named-001"]["issuerKey"]) == (
        "Manifest Name",
        "id:man",
    )


def test_the_catalogue_name_counts_only_when_it_differs_from_the_folder(tmp_path):
    seeded = {"seed-001": ("Seed Co", "SEED", None), "bare-001": (None, "BARE", None)}
    _, runs = identities(tmp_path, seeded)
    assert (runs["seed-001"]["issuer"], runs["seed-001"]["issuerKey"]) == ("Seed Co", "id:seed")
    assert (runs["bare-001"]["issuer"], runs["bare-001"]["issuerKey"]) == ("bare-001", None)


def test_ids_that_differ_only_in_case_join_runs_under_the_most_frequent_name(tmp_path):
    spec = {
        "a-001": (None, None, {"issuer_name": "Xyz Corporation", "issuer_id": "XYZ"}),
        "b-001": (None, None, {"issuer_name": "Xyz Corp", "issuer_id": "xyz"}),
        "c-001": (None, None, {"issuer_name": "Xyz Corp", "issuer_id": "Xyz"}),
    }
    _, runs = identities(tmp_path, spec)
    assert {run["issuerKey"] for run in runs.values()} == {"id:xyz"}
    assert {run["issuerHeading"] for run in runs.values()} == {"Xyz Corp"}
    assert runs["a-001"]["issuerTerms"] == ["XYZ", "Xyz", "Xyz Corp", "Xyz Corporation", "xyz"]
    assert runs["a-001"]["issuer"] == "Xyz Corporation"


def test_an_exact_recorded_name_joins_runs_without_ids_and_transitively(tmp_path):
    spec = {
        "a-001": (None, None, {"issuer_name": "Same Name"}),
        "b-001": (None, None, {"issuer_name": "Same Name", "issuer_id": "SN"}),
        "c-001": (None, None, {"issuer_name": "Other Name", "issuer_id": "sn"}),
        "d-001": (None, None, {"issuer_name": "same name"}),
    }
    _, runs = identities(tmp_path, spec)
    assert {runs[k]["issuerKey"] for k in ("a-001", "b-001", "c-001")} == {"id:sn"}
    assert runs["d-001"]["issuerKey"] == "name:same name"
    assert runs["d-001"]["issuerTerms"] == ["same name"]


def test_a_group_without_an_id_is_keyed_by_its_heading(tmp_path):
    spec = {"a-001": (None, None, {"issuer_name": "No Id Inc"})}
    _, runs = identities(tmp_path, spec)
    assert (runs["a-001"]["issuerKey"], runs["a-001"]["issuerHeading"]) == (
        "name:No Id Inc",
        "No Id Inc",
    )


def test_a_tied_heading_goes_to_the_alphabetically_first_name(tmp_path):
    spec = {
        "a-001": (None, None, {"issuer_name": "beta Co", "issuer_id": "K"}),
        "b-001": (None, None, {"issuer_name": "Alpha Co", "issuer_id": "K"}),
        "c-001": (None, None, {"issuer_name": "Alpha co", "issuer_id": "K"}),
    }
    _, runs = identities(tmp_path, spec)
    assert {run["issuerHeading"] for run in runs.values()} == {"Alpha Co"}


def test_a_curated_name_comes_first_and_an_unrecorded_run_shares_no_group(tmp_path):
    spec = {
        "tdg-002": (None, "TDG", {"issuer_name": "Manifest Loses", "issuer_id": "TDG"}),
        "blank-001": (None, None, None),
        "blank-002": (None, None, None),
    }
    _, runs = identities(tmp_path, spec)
    assert (runs["tdg-002"]["issuer"], runs["tdg-002"]["issuerKey"]) == (
        "TransDigm Group",
        "id:tdg",
    )
    for folder in ("blank-001", "blank-002"):
        assert [runs[folder][f] for f in ("issuerKey", "issuerHeading", "issuerTerms")] == [
            None,
            None,
            [],
        ]


def test_a_report_takes_the_key_of_the_group_holding_its_issuer_id(tmp_path):
    spec = {"a-001": (None, None, {"issuer_name": "Alpha Co", "issuer_id": "ALP"})}
    held = view_delivery(tmp_path, "deliverables/held", "elsewhere", "alp", "Alpha Co")
    loose = view_delivery(tmp_path, "deliverables/loose", "elsewhere", "NEW", "New Co")
    anonymous = view_delivery(tmp_path, "deliverables/anon", "elsewhere", None, "Nameless")
    result, _ = identities(tmp_path, spec, [held, loose, anonymous])
    keys = {report["id"]: report["issuerKey"] for report in result["reports"]}
    assert keys == {"held": "id:alp", "loose": "id:new", "anon": None}


# Published models: expected values are written here, not computed by the store.
FORECAST = (
    "# CP-2G\n\n## Findings\n\n### T2H.3 — Assumption Register\n\n"
    "Every row applies to the group;\nrates are decimals.\n\n"
    "| ID | Driver | Rationale |\n|---|---|---|\n| G | Growth 0.05 | Analyst judgment |\n"
    "| M | Margin 0.5 | Held |\n"
)


def model_delivery(
    root, folder, scope="Scope.", forecast=FORECAST, sources=None, previous=None, exact=None
):
    """A model deliverable (model.html, no report.html); returns its catalogue artifact."""
    files = {
        "model.html": put(root, f"{folder}/model.html", "<html>model</html>"),
        "view.json": put(
            root,
            f"{folder}/view.json",
            json.dumps(
                {
                    "run": {
                        "run_id": "alpha-001",
                        "issuer_id": "ALP",
                        "issuer_name": "Alpha Holdings",
                        "as_of": "2025-06-30",
                    },
                    "mode": "candidate",
                    "analytical_qualification": "partial",
                }
            ),
        ),
    }
    if forecast is not None:
        files["forecast.md"] = put(root, f"{folder}/forecast.md", forecast)
    if exact is not None:
        files["forecast_exact.json"] = put(
            root,
            f"{folder}/forecast_exact.json",
            exact if isinstance(exact, str) else json.dumps(exact),
        )
    record = {
        "scope": scope,
        "files": files,
        "sources": sources or {},
        "input_contract": "Six headings.",
        "presentation_repair": None,
        "previous_directory": previous,
    }
    put(root, f"{folder}/delivery.json", json.dumps(record))
    return {
        "folder": folder,
        "kind": "model",
        "label": folder,
        "state": "candidate",
        "available": True,
        "href": f"/files/{folder}/model.html?sha256=m",
    }


def models_of(root, *artifacts, edit=None):
    catalogue = workspace(root)
    if edit:
        edit()  # After the workspace is written, before the store reads it.
    catalogue["real"].append(
        {"id": "delivery:m", "name": "x", "sector": "", "period": "", "artifacts": list(artifacts)}
    )
    return store.workspace_store(root, catalogue)


def test_a_model_is_listed_with_its_register_sources_and_not_as_a_report(tmp_path):
    cp1 = hashlib.sha256(CP1.encode()).hexdigest()
    artifact = model_delivery(
        tmp_path,
        "deliverables/m-2",
        sources={
            "annual": {"path": "runs/alpha-001/CP-1.md", "sha256": cp1},
            "other": {"path": "runs/alpha-001/CP-4A.md", "sha256": "0" * 64},
            "gone": {"path": "runs/alpha-001/missing.md", "sha256": "1" * 64},
        },
        previous="deliverables/m-1",
    )
    result = models_of(tmp_path, artifact)
    assert [r["id"] for r in result["reports"]] == ["alpha-report", "abc"]
    (model,) = result["models"]
    assert model["id"] == "m-2" and model["previous"] == "m-1"
    assert (model["mode"], model["qualification"]) == ("candidate", "partial")
    assert model["runId"] == "alpha-001" and model["issuerKey"] == "id:alp"
    assert model["scope"] == "Scope." and model["inputContract"] == "Six headings."
    assert model["revisionNote"] is None
    assert model["href"] == "/files/deliverables/m-2/model.html?sha256=m&embedded=1"
    assert model["download"] == "/files/deliverables/m-2/model.html?sha256=m&download=1"
    assert {f["name"] for f in model["files"]} == {"model.html", "view.json", "forecast.md"}
    assert model["register"] == {
        "heading": "T2H.3 — Assumption Register",
        "intro": "Every row applies to the group;\nrates are decimals.",
        "headers": ["ID", "Driver", "Rationale"],
        "rows": [["G", "Growth 0.05", "Analyst judgment"], ["M", "Margin 0.5", "Held"]],
    }
    by_role = {row["role"]: row for row in model["sources"]}
    assert [row["role"] for row in model["sources"]] == ["annual", "other", "gone"]
    assert by_role["annual"] == {
        "role": "annual",
        "path": "runs/alpha-001/CP-1.md",
        "sha256": cp1,
        "changed": False,
        "run": "alpha-001",
        "output": "alpha-001/CP-1.md",
    }
    assert (by_role["other"]["changed"], by_role["other"]["run"]) == (True, None)
    assert by_role["other"]["output"] is None
    assert (by_role["gone"]["changed"], by_role["gone"]["output"]) == (True, None)


def test_a_model_without_a_register_section_has_none(tmp_path):
    artifact = model_delivery(
        tmp_path, "deliverables/m-1", forecast="# CP-2G\n\n## Findings\n\nx\n"
    )
    assert models_of(tmp_path, artifact)["models"][0]["register"] is None
    bare = model_delivery(tmp_path, "deliverables/m-0", forecast=None)
    assert {m["id"]: m for m in models_of(tmp_path, artifact, bare)["models"]}["m-0"][
        "register"
    ] is None


def test_a_changed_source_is_flagged_and_the_model_stays_listed(tmp_path):
    cp1 = hashlib.sha256(CP1.encode()).hexdigest()
    artifact = model_delivery(
        tmp_path,
        "deliverables/m-1",
        sources={"annual": {"path": "runs/alpha-001/CP-1.md", "sha256": cp1}},
    )
    (model,) = models_of(
        tmp_path,
        artifact,
        edit=lambda: (tmp_path / "runs/alpha-001/CP-1.md").write_text(CP1 + "x", encoding="utf-8"),
    )["models"]
    (source,) = model["sources"]
    assert source["changed"] is True and source["run"] is None and source["output"] is None


def test_hostile_text_in_a_model_stays_a_string(tmp_path):
    hostile = "<img src=x onerror=alert(1)>"
    artifact = model_delivery(tmp_path, "deliverables/m-1", scope=hostile)
    (model,) = models_of(tmp_path, artifact)["models"]
    assert model["scope"] == hostile


def test_an_unreadable_model_is_reported_and_the_others_stay(tmp_path):
    good = model_delivery(tmp_path, "deliverables/m-1")
    bad = model_delivery(tmp_path, "deliverables/m-2")
    (tmp_path / "deliverables/m-2/view.json").write_text("{", encoding="utf-8")
    result = models_of(tmp_path, good, bad)
    assert [m["id"] for m in result["models"]] == ["m-1"]
    assert any(i.startswith("deliverables/m-2: could not be read") for i in result["issues"])


@pytest.mark.parametrize(
    ("iso", "shown"),
    [
        ("2024-12-31", "31 December 2024"),
        ("2025-05-01", "1 May 2025"),
        ("2024-02-29", "29 February 2024"),
        ("2023-02-29", "2023-02-29"),
        ("2024-02-30", "2024-02-30"),
        ("0000-01-01", "0000-01-01"),
        ("2024-13-01", "2024-13-01"),
        ("2024-1-05", "2024-1-05"),
        (" 2024-12-31", " 2024-12-31"),
        ("2024-12-31x", "2024-12-31x"),
        ("05/08/2023", "05/08/2023"),
        ("2024-12-31T00:00", "2024-12-31T00:00"),
        ("", ""),
    ],
)
def test_display_date_reads_only_a_valid_calendar_date(iso, shown):
    assert store.display_date(iso) == shown


def test_a_model_with_untyped_fields_keeps_only_strings(tmp_path):
    artifact = model_delivery(tmp_path, "deliverables/m-1")
    record = json.loads((tmp_path / "deliverables/m-1/delivery.json").read_text(encoding="utf-8"))
    record.update(scope=5, input_contract=["x"], presentation_repair={"a": 1})
    record["sources"] = {
        "num": {"path": "runs/alpha-001/CP-1.md", "sha256": 5},
        "badhex": {"path": "runs/alpha-001/CP-1.md", "sha256": "A" * 64},
        "short": {"path": "runs/alpha-001/CP-1.md", "sha256": "a" * 63},
        "path": {"path": 7, "sha256": "a" * 64},
        "whole": "not an object",
    }
    (tmp_path / "deliverables/m-1/delivery.json").write_text(json.dumps(record), encoding="utf-8")
    result = models_of(tmp_path, artifact)
    (model,) = result["models"]
    assert (model["scope"], model["inputContract"], model["revisionNote"]) == (None, None, None)
    for row in model["sources"]:
        assert (row["sha256"], row["changed"]) == (None, None), row
        assert row["path"] is None or isinstance(row["path"], str)
    for role in ("num", "badhex", "short", "path", "whole"):
        assert f"deliverables/m-1: source {role} has an invalid path or hash" in result["issues"]


def test_source_paths_outside_the_workspace_are_never_opened(tmp_path, monkeypatch):
    root = tmp_path / "ws"
    outside = tmp_path / "outside"
    outside.mkdir()
    secret = outside / "secret.txt"
    secret.write_text("secret", encoding="utf-8")
    digest = hashlib.sha256(b"secret").hexdigest()
    (root / "runs/alpha-001").mkdir(parents=True)
    (root / "runs/alpha-001/link.md").symlink_to(secret)
    (root / "runs/escape").symlink_to(outside, target_is_directory=True)
    artifact = model_delivery(root, "deliverables/m-1")
    record = json.loads((root / "deliverables/m-1/delivery.json").read_text(encoding="utf-8"))
    record["sources"] = {
        "absolute": {"path": str(secret), "sha256": digest},
        "dotdot": {"path": "runs/alpha-001/../../../outside/secret.txt", "sha256": digest},
        "link": {"path": "runs/alpha-001/link.md", "sha256": digest},
        "dirlink": {"path": "runs/escape/secret.txt", "sha256": digest},
        "outside_runs": {"path": "deliverables/m-1/view.json", "sha256": digest},
        "backslash": {"path": "runs\\alpha-001\\x.md", "sha256": digest},
    }
    (root / "deliverables/m-1/delivery.json").write_text(json.dumps(record), encoding="utf-8")
    opened = []
    real = store.sha256
    monkeypatch.setattr(store, "sha256", lambda p: opened.append(p) or real(p))
    result = models_of(root, artifact)
    (model,) = result["models"]
    assert [(r["sha256"], r["changed"]) for r in model["sources"]] == [(None, None)] * 6
    assert not [p for p in opened if "secret" in str(p) or p.name in {"link.md", "x.md"}]
    assert len([i for i in result["issues"] if "has an invalid path or hash" in i]) == 6


# The cash flow model: expected strings are written here, not computed by the store.
REQUEST = "# CP-2G\n\n## Request\n\nTest paths. Amounts in EUR\nbillions; consolidated.\n\n## Findings\n\nUSD millions.\n"


def amount(value, reason=None):
    return {"amount": value, "reason": reason}


def exact_record(**more):
    year = {
        "year": 2026,
        "planning_start": "2025-10-01",
        "planning_end": "2026-09-30",
        "revenue": amount("-1234.5"),
        "ebitda": amount("2.5"),
        "interest": amount("0.4"),
        "cfo": amount("-0.4"),
        "capex": amount(None, "<img src=x onerror=alert(1)>"),
        "fcf": amount("1234567.5"),
        "total_leverage": amount("0.125"),
        "net_leverage": amount("0.135"),
        "coverage": amount("2"),
        "fcf_to_debt": amount("0.12345"),
    }
    record = {
        "base": {"revenue": amount("100"), "wc": amount(None, "No operand")},
        "outputs": {
            "REFERENCE": {"years": [year]},
            "STRESS_CASE": {"years": [{**year, "year": 2026}]},
        },
        "scope_limits": ["First <b>limit</b>", "Second limit"],
    }
    record.update(more)
    return record


def cashflow_of(tmp_path, forecast=REQUEST, **kwargs):
    artifact = model_delivery(tmp_path, "deliverables/m-1", forecast=forecast, **kwargs)
    result = models_of(tmp_path, artifact)
    return result["models"][0]["cashflow"], [i for i in result["issues"] if "forecast_exact" in i]


def row(cashflow, label):
    return next(r for r in cashflow["rows"] if r["label"] == label)


# Security review L1-L3: model files are read only as bounded regular files; nothing hangs or drops a model.
def within(seconds, call):
    """Run call on a thread; a read that blocks forever (a FIFO) fails the test instead of hanging it."""
    box = {}
    thread = threading.Thread(target=lambda: box.update(value=call()), daemon=True)
    thread.start()
    thread.join(seconds)
    assert not thread.is_alive(), "the store blocked"
    return box["value"]


def source_model(tmp_path, role, path, prepare):
    root = tmp_path / "ws"
    prepare(root)
    artifact = model_delivery(root, "deliverables/m-1")
    record = json.loads((root / "deliverables/m-1/delivery.json").read_text(encoding="utf-8"))
    record["sources"] = {role: {"path": path, "sha256": "a" * 64}}
    (root / "deliverables/m-1/delivery.json").write_text(json.dumps(record), encoding="utf-8")
    result = within(20, lambda: models_of(root, artifact))
    return result, [m for m in result["models"] if m["id"] == "m-1"]


def test_a_fifo_source_keeps_the_row_without_a_hash_and_is_reported(tmp_path):
    result, (model,) = source_model(
        tmp_path,
        "fifo",
        "runs/alpha-001/pipe",
        lambda root: (
            (root / "runs/alpha-001").mkdir(parents=True) or os.mkfifo(root / "runs/alpha-001/pipe")
        ),
    )
    (row,) = model["sources"]
    assert (row["role"], row["sha256"], row["changed"]) == ("fifo", None, None)
    assert "deliverables/m-1: source fifo is not a readable file" in result["issues"]


def test_a_source_over_64_mib_is_not_read_and_is_reported(tmp_path):
    def big(root):
        (root / "runs/alpha-001").mkdir(parents=True)
        with open(root / "runs/alpha-001/big.bin", "wb") as f:
            f.truncate(64 * 1024 * 1024 + 1)

    result, (model,) = source_model(tmp_path, "big", "runs/alpha-001/big.bin", big)
    (row,) = model["sources"]
    assert (row["sha256"], row["changed"]) == (None, None)
    assert "deliverables/m-1: source big is not a readable file" in result["issues"]


def test_a_source_path_with_a_nul_byte_is_an_invalid_source_not_a_dropped_model(tmp_path):
    result, (model,) = source_model(tmp_path, "nul", "runs/alpha-001/a\x00b.md", lambda root: None)
    (row,) = model["sources"]
    assert (row["sha256"], row["changed"]) == (None, None)
    assert "deliverables/m-1: source nul has an invalid path or hash" in result["issues"]


def test_forecast_md_through_a_symlink_is_not_read_even_when_its_bytes_match(tmp_path):
    root = tmp_path / "ws"
    artifact = model_delivery(root, "deliverables/m-1")
    outside = tmp_path / "outside.md"
    outside.write_text(FORECAST, encoding="utf-8")
    (root / "deliverables/m-1/forecast.md").unlink()
    (root / "deliverables/m-1/forecast.md").symlink_to(outside)
    result = models_of(root, artifact)
    (model,) = result["models"]
    assert (model["register"], model["cashflow"]) == (None, None)
    assert "deliverables/m-1: forecast.md does not match its delivery record" in result["issues"]


def test_a_forecast_md_whose_hash_changed_is_not_read_and_the_model_stays(tmp_path):
    artifact = model_delivery(tmp_path, "deliverables/m-1")
    (model,) = models_of(
        tmp_path,
        artifact,
        edit=lambda: (tmp_path / "deliverables/m-1/forecast.md").write_text(
            FORECAST + "\nEdited.\n", encoding="utf-8"
        ),
    )["models"]
    assert model["register"] is None and model["cashflow"] is None
    result = models_of(
        tmp_path,
        artifact,
        edit=lambda: (tmp_path / "deliverables/m-1/forecast.md").write_text("x", encoding="utf-8"),
    )
    assert "deliverables/m-1: forecast.md does not match its delivery record" in result["issues"]


def test_forecast_exact_json_must_match_its_listed_hash_and_not_be_a_symlink(tmp_path):
    artifact = model_delivery(tmp_path, "deliverables/m-1", forecast=REQUEST, exact=exact_record())
    path = tmp_path / "deliverables/m-1/forecast_exact.json"
    result = models_of(tmp_path, artifact, edit=lambda: path.write_text("{}", encoding="utf-8"))
    assert result["models"][0]["cashflow"] is None
    assert (
        "deliverables/m-1: forecast_exact.json does not match its delivery record"
        in result["issues"]
    )
    outside = tmp_path / "outside.json"
    outside.write_text(json.dumps(exact_record()), encoding="utf-8")
    result = models_of(tmp_path, artifact, edit=lambda: (path.unlink(), path.symlink_to(outside)))
    assert result["models"][0]["cashflow"] is None
    assert (
        "deliverables/m-1: forecast_exact.json does not match its delivery record"
        in result["issues"]
    )


def test_a_model_read_error_names_its_type_and_reason_and_never_the_bytes(tmp_path):
    good = model_delivery(tmp_path, "deliverables/m-1")
    bad = model_delivery(tmp_path, "deliverables/m-2")
    (tmp_path / "deliverables/m-2/view.json").write_bytes(b"\xff\xfe TOPSECRET")
    issues = models_of(tmp_path, good, bad)["issues"]
    (issue,) = [i for i in issues if i.startswith("deliverables/m-2: could not be read")]
    assert "UnicodeDecodeError" in issue and "invalid start byte" in issue
    assert "TOPSECRET" not in issue and "\\x" not in issue and "b'" not in issue


def test_a_cash_flow_model_shows_exact_values_rounded_half_up_with_brackets(tmp_path):
    cashflow, issues = cashflow_of(tmp_path, exact=exact_record())
    assert issues == []
    assert cashflow["units"] == "EUR billions"
    assert [(c["group"], c["label"]) for c in cashflow["columns"]] == [
        ("Base", "FY2025"),
        ("Reference", "FY2026E"),
        ("Stress_Case", "FY2026E"),
    ]
    assert (
        cashflow["columns"][1]["start"] == "2025-10-01"
        and cashflow["columns"][1]["end"] == "2026-09-30"
    )
    assert [c["display"] for c in row(cashflow, "Revenue")["cells"]] == [
        "100",
        "(1,235)",
        "(1,235)",
    ]
    assert row(cashflow, "Revenue")["cells"][1]["exact"] == "-1234.5"
    assert row(cashflow, "Model earnings (operating-based EBITDA)")["cells"][1]["display"] == "3"
    assert row(cashflow, "Cash interest")["cells"][1]["display"] == "0"
    assert row(cashflow, "Model cash from operations")["cells"][1]["display"] == "0"
    assert (
        row(cashflow, "Cash proxy (not issuer free cash flow)")["cells"][1]["display"]
        == "1,234,568"
    )
    assert row(cashflow, "Debt / model earnings")["cells"][1]["display"] == "0.13x"
    assert row(cashflow, "Net debt / model earnings")["cells"][1]["display"] == "0.14x"
    assert row(cashflow, "Model earnings / cash interest")["cells"][1]["display"] == "2.00x"
    assert row(cashflow, "Cash proxy / closing debt")["cells"][1]["display"] == "12.35%"


def test_a_cash_flow_cell_is_n_a_with_its_reason_or_a_dash_when_the_key_is_not_held(tmp_path):
    cashflow, _ = cashflow_of(tmp_path, exact=exact_record())
    hostile = row(cashflow, "Capital expenditure")["cells"][1]
    assert hostile == {"exact": None, "display": "n.a.", "reason": "<img src=x onerror=alert(1)>"}
    assert row(cashflow, "Working capital")["cells"][0] == {
        "exact": None,
        "display": "n.a.",
        "reason": "No operand",
    }
    assert row(cashflow, "Cash taxes")["cells"][1] == {
        "exact": None,
        "display": "\u2014",
        "reason": None,
    }
    assert row(cashflow, "Opening cash")["cells"][0]["display"] == "\u2014"
    assert cashflow["limits"] == ["First <b>limit</b>", "Second limit"]
    assert [r["band"] for r in cashflow["rows"]][:2] == ["Operating", "Operating"]


def test_units_are_none_when_the_request_names_none(tmp_path):
    cashflow, _ = cashflow_of(tmp_path, exact=exact_record(), forecast="## Request\n\nNo units.\n")
    assert cashflow["units"] is None


@pytest.mark.parametrize(
    "exact", [None, "{", '{"base": 1}', '{"base": {}, "outputs": {}, "scope_limits": []}']
)
def test_a_missing_or_invalid_calculation_record_gives_no_cash_flow_model_and_an_issue(
    tmp_path, exact
):
    cashflow, issues = cashflow_of(tmp_path, exact=exact)
    assert cashflow is None
    assert "deliverables/m-1: forecast_exact.json is missing or unreadable" in issues


def test_a_non_numeric_amount_is_unreadable_not_shown(tmp_path):
    record = exact_record()
    record["base"]["revenue"] = amount("NaN")
    cashflow, issues = cashflow_of(tmp_path, exact=record)
    assert cashflow is None and issues == [
        "deliverables/m-1: forecast_exact.json is missing or unreadable"
    ]


@pytest.mark.parametrize(
    ("exact", "kind", "shown"),
    [("-0.004", "multiple", "0.00x"), ("-0.00004", "percent", "0.00%")],
)
def test_a_multiple_or_percent_that_rounds_to_zero_has_no_sign(exact, kind, shown):
    assert store.display_amount(exact, kind) == shown


def test_units_are_read_from_a_request_with_windows_line_endings():
    handoff = "# CP\r\n\r\n## Request\r\n\r\nAmounts in USD\r\nmillions.\r\n\r\n## Findings\r\n\r\nEUR billions.\r\n"
    assert store.cashflow_units(handoff) == "USD millions"


# Fix round: a stray or hostile file in one delivery never ends the store.
def test_a_stray_oversize_handoff_beside_a_report_is_named_and_the_library_stays(tmp_path):
    report = view_delivery(tmp_path, "deliverables/r-1", "alpha-001", "ALP", "Alpha Holdings")
    with open(tmp_path / "deliverables/r-1/CP-0-attempt-1.md", "wb") as f:
        f.truncate(64 * 1024 * 1024 + 1)
    catalogue = identity_catalogue(tmp_path, {"alpha-001": (None, None, None)}, [report])
    result = store.workspace_store(tmp_path, catalogue)
    assert [r["id"] for r in result["reports"]] == ["r-1"]
    assert result["reports"][0]["builtFrom"] == []
    (issue,) = [i for i in result["issues"] if "CP-0-attempt-1.md" in i]
    assert issue.startswith("deliverables/r-1: CP-0-attempt-1.md could not be read (UnreadableFile")


def test_deeply_nested_json_in_a_model_is_an_issue_not_a_crash(tmp_path):
    artifact = model_delivery(tmp_path, "deliverables/m-1", forecast=REQUEST, exact="[" * 20000)
    result = models_of(tmp_path, artifact)
    assert result["models"][0]["cashflow"] is None
    assert "deliverables/m-1: forecast_exact.json is missing or unreadable" in result["issues"]
    artifact = model_delivery(tmp_path, "deliverables/m-2")
    (tmp_path / "deliverables/m-2/view.json").write_text("[" * 20000, encoding="utf-8")
    result = models_of(tmp_path, artifact)
    assert [m["id"] for m in result["models"]] == []
    assert any(i.startswith("deliverables/m-2: could not be read (") for i in result["issues"])


def test_a_directory_source_is_not_a_readable_file_and_leaks_no_descriptor(tmp_path):
    def prepare(root):
        (root / "runs/alpha-001/adir").mkdir(parents=True)

    before = len(os.listdir("/dev/fd")) if os.path.isdir("/dev/fd") else None
    result, (model,) = source_model(tmp_path, "dir", "runs/alpha-001/adir", prepare)
    assert (model["sources"][0]["sha256"], model["sources"][0]["changed"]) == (None, None)
    assert "deliverables/m-1: source dir is not a readable file" in result["issues"]
    if before is not None:
        assert len(os.listdir("/dev/fd")) <= before + 1


def test_a_files_list_in_a_delivery_is_an_issue_not_a_crash(tmp_path):
    artifact = model_delivery(tmp_path, "deliverables/m-1")
    record = json.loads((tmp_path / "deliverables/m-1/delivery.json").read_text(encoding="utf-8"))
    record["files"] = ["model.html"]
    (tmp_path / "deliverables/m-1/delivery.json").write_text(json.dumps(record), encoding="utf-8")
    result = models_of(tmp_path, artifact)
    assert result["models"] == []
    assert (
        "deliverables/m-1: could not be read (TypeError: files is not an object)"
        in result["issues"]
    )
