"""Code-review repro (fake connector, no network): Last-Modified hides a body 'Published:' line."""
from datetime import date
from pathlib import Path
from deploy_workflow.research import webfetch as w
from deploy_workflow.research.intake import parse_rows, intake

class Resp:
    status = 200
    def __init__(self, headers, body): self.h, self.b = headers, body
    def getheader(self, n): return self.h.get(n)
    def read(self, amt):
        out, self.b = self.b[:amt], self.b[amt:]; return out
class Conn:
    def __init__(self, resp): self.resp = resp
    def request(self, m, u, *, headers): pass
    def getresponse(self): return self.resp
    def close(self): pass

def run(last_modified, body):
    hdr = {"Content-Type": "text/plain; charset=utf-8", "Last-Modified": last_modified}
    def fetcher(url, hosts):
        b = body.encode()
        return w.fetch(url, manifest_hosts=hosts, resolver=lambda h: ["93.184.216.34"],
                       connect=lambda t: Conn(Resp({**hdr, "Content-Length": str(len(b))}, b)), cap=10000, clock=lambda: 0.0)
    rows = parse_rows([{"url": "https://example.com/a", "family": "Wire", "locator": "L1", "tag": "research", "published": "2025-03-01"}])
    res = intake(rows, base_dir=Path("."), dest_dir=None, as_of=date(2025, 6, 30), cutoff=date(2025, 6, 30), today=date(2026, 11, 6), fetch=fetcher)
    f = res.fetches[0]
    print(f"Last-Modified={last_modified!r} body={body.splitlines()[0]!r}: located={f.published_located} via {f.published_source}; "
          f"accepted={[a.item_id for a in res.accepted]} refused={[r.reason for r in res.refused]}")

run("Wed, 01 Jan 2025 00:00:00 GMT", "Published: 2025-09-01\nPost-cutoff article text.")
run("Fri, 06 Nov 2026 00:00:00 GMT", "Published: 2025-03-01\nPre-cutoff article text.")
