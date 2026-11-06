import sys, re, json
sys.path.insert(0, "/tmp/claude-0/-workspace-final-workflow/10d71552-cdca-5952-86dc-d4ef0b76ab9e/scratchpad/review/S04-delivery/t")
from harness import *

P = '</script><img src=x onerror=alert(1)><!--'
Q = "\"><svg onload=alert(2)>&amp;"
print("== B1 injection in cells, row labels, period labels, headings")
fin = f"| Metric | FY2023 | FY2024 |\n| --- | ---: | ---: |\n| Rev {P} | {Q} | 2 |\n"
text = handoff(fin_table=fin, leverage=[(f"FY2023 {P}", "4.1", "3.9"), ("FY2024", "3.8", "3.5")],
               extra_findings=f"### Notes {P}\n\nPara {P} {Q}\n\n")
files, rv, view = deliver(text)
html = files["report.html"].decode()
body_script = html.split('<script id="report-data" type="application/json">',1)[1].split("</script>",1)[0]
print("raw payload contains '<':", "<" in body_script, "| contains '</script':", "</script" in body_script.lower())
print("unescaped U+2028 in payload:", " " in body_script)
data = json.loads(body_script)
print("payload roundtrips value:", P in json.dumps(data, ensure_ascii=False))
# outside the data block
outside = html.replace(body_script, "")
print("payload text present outside data block:", "onerror=alert" in outside, "onload=alert" in outside)
# svg strings
svgs = [f["chart"]["svg"] for b in data["report"]["blocks"] for f in b.get("figures", [])]
import xml.etree.ElementTree as ET
for s in svgs:
    root = ET.fromstring(s)
    tags = {e.tag.split('}')[-1] for e in root.iter()}
    attrs = {a for e in root.iter() for a in e.attrib if a.lower().startswith("on")}
    assert tags <= {"svg","g","rect","path","line","circle","text","title","desc","defs","pattern"}, tags
    assert not attrs, attrs
print("svgs well-formed, allowed tags only, no on* attrs:", len(svgs))

print("== B2 pipe lines that are not a header+separator table vanish (neither table nor prose)")
text = handoff(extra_findings="### Peer notes\n\n| Peer A | leverage 4.0x | rated B2 |\n| Peer B | leverage 6.5x | rated Caa1 |\n\n")
files, rv, view = deliver(text)
mod = [m for m in view.modules if m.module_id=="CP-1"][0]
hits = [f.fact_id for f in mod.facts if "Peer B" in (f.text or "") or "Peer B" in f.label]
print("facts mentioning Peer B:", hits)
print("'6.5x' in report payload:", b"6.5x" in files["report.html"], "| in copied CP-1.md:", b"6.5x" in files["CP-1.md"])
