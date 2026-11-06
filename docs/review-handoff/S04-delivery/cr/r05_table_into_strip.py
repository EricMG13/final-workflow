import sys, os, json; sys.path.insert(0, os.path.dirname(__file__))
from common import deliver
MD = """# CP-1B TransDigm Group Incorporated
## Request
Earnings view.
## Sources
None.
## Findings
### Ratios
| Metric | FY2023 | FY2024 |
|---|---|---|
| Leverage | 5.10 | 4.90 |
| Coverage | 2.50 | 2.75 |
### Cash
| Metric | FY2023 | FY2024 |
|---|---|---|
| Cash | 3001 | 0.0725 |
### Covenant notes
| Item | Text |
|---|---|
| UNIQUE-COVENANT-ROW | Springing leverage test 7.25x |
## Calculations
None.
## Gaps
None.
## Next module
Delivery.
"""
def chart(fid, heading, rows, unit):
    return {"module_id": "CP-1B", "heading": heading, "kind": "chart", "block_id": "metric-strip", "figure_id": fid,
            "value_columns": ["FY2023", "FY2024"], "row_labels": rows, "chart_unit": unit}
routes = [chart("S.1", "Ratios", ["Leverage"], "x"), chart("S.2", "Ratios", ["Coverage"], "x"), chart("S.3", "Cash", ["Cash"], "US$m"),
          {"module_id": "CP-1B", "heading": "Covenant notes", "kind": "table", "block_id": "metric-strip"}]
files = deliver(MD, ["metric-strip"], routes)
html = files["report.html"].decode()
rv = files["report-view.json"].decode()
print("UNIQUE-COVENANT-ROW in report.html:", "UNIQUE-COVENANT-ROW" in html, "| in report-view.json:", "UNIQUE-COVENANT-ROW" in rv)
view = json.loads(files["view.json"])
print("in view.json facts:", any("UNIQUE-COVENANT-ROW" in json.dumps(m) for m in view["modules"]))
r = json.loads(rv)
print("blocks:", [(b["block_id"], b["kind"]) for b in r["blocks"]])
evid = json.dumps([b for b in r["blocks"] if b["block_id"]=="evidence"])
print("unplaced:", r.get("unplaced"))
def find(o, path=""):
    if isinstance(o, dict):
        for k, v in o.items(): yield from find(v, path + "/" + k)
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from find(v, path + f"[{i}]")
    elif isinstance(o, str) and "UNIQUE-COVENANT-ROW" in o:
        yield path
print(list(find(r))[:10])
