"""Stub-only attacks on webfetch.fetch (no sockets)."""
from deploy_workflow.research import webfetch as w

class Resp:
    def __init__(self, status, headers, body, per_read_cost=0.0, clock=None):
        self.status, self._h, self._b, self.cost, self.clock = status, headers, body, per_read_cost, clock
    def getheader(self, n):
        for k, v in self._h.items():
            if k.lower() == n.lower(): return v
        return None
    def read(self, amt):
        chunk, self._b = self._b[:min(amt, 3)], self._b[min(amt, 3):]
        if self.clock: self.clock.t += self.cost
        return chunk

class Clock:
    t = 0.0
    def __call__(self): return self.t

def run(name, url, script, resolver, cap=100, hosts=None):
    clock = Clock()
    calls = []
    def connect(target):
        calls.append((target.host, target.ip, target.port))
        resp = script.pop(0)
        resp.clock = clock if resp.cost else None
        class C:
            def request(self, m, u, headers): calls.append(("GET", u, headers["Host"]))
            def getresponse(self): return resp
            def close(self): pass
        return C()
    hosts = hosts or frozenset({w.check_url(url).host})
    rec, body, media = w.fetch(url, manifest_hosts=hosts, resolver=resolver, connect=connect, cap=cap, clock=clock)
    print(f"{name:28} reason={rec.reason!r} body={body!r} hops={rec.hops} calls={calls}")

pub = lambda h: ["93.184.216.34"]
run("redirect-to-other-host", "https://a.example/x", [Resp(302, {"Location": "https://169.254.169.254/latest"}, b"")], pub)
run("redirect-proto-rel", "https://a.example/x", [Resp(302, {"Location": "//evil.example/"}, b"")], pub)
run("redirect-http", "https://a.example/x", [Resp(301, {"Location": "http://a.example/"}, b"")], pub)
run("redirect-userinfo", "https://a.example/x", [Resp(301, {"Location": "https://a.example@evil.example/"}, b"")], pub)
seq = iter([["93.184.216.34"], ["10.0.0.5"]])
run("dns-rebind-2nd-hop", "https://a.example/x", [Resp(302, {"Location": "/y"}, b""), Resp(200, {}, b"hi")], lambda h: next(seq))
run("mixed-records", "https://a.example/x", [], lambda h: ["93.184.216.34", "127.0.0.1"])
run("v4mapped", "https://a.example/x", [], lambda h: ["::ffff:10.1.2.3"])
run("over-cap", "https://a.example/x", [Resp(200, {"Content-Type": "text/plain"}, b"x"*101)], pub)
run("at-cap", "https://a.example/x", [Resp(200, {"Content-Type": "text/plain"}, b"x"*100)], pub)
run("short-body", "https://a.example/x", [Resp(200, {"Content-Length": "50"}, b"x"*10)], pub)
run("slow-drip", "https://a.example/x", [Resp(200, {}, b"x"*90, per_read_cost=1.0)], pub)
run("4-redirects", "https://a.example/x", [Resp(302, {"Location": "/1"}, b""), Resp(302, {"Location": "/2"}, b""), Resp(302, {"Location": "/3"}, b""), Resp(302, {"Location": "/4"}, b"")], pub)
run("location-with-pipe", "https://a.example/x", [Resp(302, {"Location": "https://a.example/|<<<x"}, b"")], pub)
run("scheme-file", "file:///etc/passwd", [], pub)
run("decimal-ip", "https://2130706433/", [], lambda h: ["127.0.0.1"])
