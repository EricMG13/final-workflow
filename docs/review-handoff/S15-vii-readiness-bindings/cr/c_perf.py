import time
from deploy_vii.contracts import Source, Span, Citation
from deploy_vii.readiness import citation_issues
H = "a"*64
n = 50000
src = Source(source_id="wb", name="wb.xlsx", status="ready", sha256=H,
             spans=tuple(Span(locator=f"sheet:S!A{i}", text=f"v{i}") for i in range(n)))
cites = tuple(Citation(source_id="wb", source_sha256=H, locator=f"sheet:S!A{n-1-i}", quote=f"v{n-1-i}") for i in range(300))
t = time.perf_counter(); issues = citation_issues(cites, (src,)); dt = time.perf_counter() - t
print(f"{len(cites)} citations over {n} spans: {dt:.2f}s, issues={len(issues)}")
