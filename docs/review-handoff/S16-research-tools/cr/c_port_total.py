"""Code-review repro: redirect to another port on a manifest host is followed; peer_id 'total' -> total row."""
import copy, sys, json
sys.path.insert(0, "tests/research")
from deploy_workflow.research import webfetch as w

class Resp:
    def __init__(self, status, headers, body=b""): self.status, self.h, self.b = status, headers, body
    def getheader(self, n): return self.h.get(n)
    def read(self, amt): out, self.b = self.b[:amt], self.b[amt:]; return out
class Conn:
    def __init__(self, t): self.t = t
    def request(self, m, u, *, headers): self.u = u
    def close(self): pass
    def getresponse(self):
        if self.t.port == 443:
            return Resp(302, {"Location": "https://example.com:8443/admin"})
        return Resp(200, {"Content-Type": "text/plain"}, b"internal admin page")
targets = []
def connect(t): targets.append((t.host, t.port)); return Conn(t)
rec, body, media = w.fetch("https://example.com/a", manifest_hosts=frozenset({"example.com"}),
                           resolver=lambda h: ["93.184.216.34"], connect=connect, cap=1000, clock=lambda: 0.0)
print("connections:", targets, "reason:", rec.reason, "body:", body)

from cpdr_peers_support import peers_case
case = peers_case()
body = json.loads(json.dumps(case.body).replace('"p01"', '"total"'))
print("peer_id total issues:", case.issues(body))
comp = case.composed(body)
for t in comp.tables:
    for r in t.rows:
        if r.row_kind == "total":
            print("  total-styled row:", t.table_id, r.row_id)
