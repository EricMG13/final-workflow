"""Code-review repro (fakes only, no network): IDNA host crash; located date precedence."""
import socket
from datetime import date
from deploy_workflow.research import webfetch as w

for url in ("https://www..example.com/a", "https://" + "a" * 64 + ".example.com/a"):
    shape = w.check_url(url)
    print("check_url accepts:", shape.host[:30], "...")
    # what the system resolver would do: encoding fails locally before any lookup
    try:
        shape.host.encode("idna")
    except Exception as e:
        print("  host.encode('idna') ->", type(e).__name__, "isinstance OSError:", isinstance(e, OSError))
    def fake_resolver(host):  # mirrors socket.getaddrinfo's local IDNA failure
        return host.encode("idna")
    try:
        rec = w.fetch(url, manifest_hosts=frozenset({shape.host}), resolver=fake_resolver,
                      connect=lambda t: None, cap=100, clock=lambda: 0.0)
        print("  fetch returned record reason:", rec[0].reason)
    except Exception as e:
        print("  fetch RAISED", type(e).__name__, str(e)[:80])

# located date: header wins over body even when the body line is after the cutoff
hdr = {"Last-Modified": "Wed, 01 Jan 2025 00:00:00 GMT"}
body = b"Published: 2025-09-01\nText"
print("locate_published:", w.locate_published(hdr, body))
