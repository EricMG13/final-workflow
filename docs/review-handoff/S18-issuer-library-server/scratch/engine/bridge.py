import json, sys, pathlib, time
folder = pathlib.Path(sys.argv[2])
job = json.loads((folder / "job.json").read_text())
if sys.argv[1] == "review":
    time.sleep(int(__import__("os").environ.get("FAKE_REVIEW_SECONDS", "190")))
    print(json.dumps({"ok": True, "review_id": "r1", "id": job["id"], "provider_ready": False}))
