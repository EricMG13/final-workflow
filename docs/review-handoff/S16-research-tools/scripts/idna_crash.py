"""A03: a manifest url whose host the IDNA codec refuses (empty or >63-char label) passes
check_url, then system_resolver raises UnicodeError (a ValueError, not OSError), which escapes
fetch() instead of becoming a per-item refusal. Run under `unshare -n` (no network)."""
from deploy_workflow.research import webfetch as w
for url in ["https://www..example.com/a", "https://" + "a"*64 + ".example.com/"]:
    print("check_url:", w.check_url(url).host[:30])
    try:
        rec, body, media = w.fetch(url, manifest_hosts=frozenset({w.check_url(url).host}),
                                   resolver=w.system_resolver, connect=w.pinned_connection,
                                   cap=1000, clock=__import__("time").monotonic)
        print("record reason:", rec.reason)
    except Exception as e:
        print("ESCAPED:", type(e).__name__, str(e)[:80])
