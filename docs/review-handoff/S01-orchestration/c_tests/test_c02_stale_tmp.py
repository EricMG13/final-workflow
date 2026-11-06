"""C02: a run.json.tmp left by an earlier failed write wedges every later run.json write."""
from tests.test_run_pathway import args, killed, no_network  # noqa: F401  (fixtures only)
from tests.test_run_pathway import calls_of, scripted_complete, pack_helpers, run_pathway, rp


def test_stale_run_json_tmp_blocks_resume(killed, monkeypatch):
    run_dir = killed["run_dir"]
    (run_dir / "run.json.tmp").write_bytes(b"{partial")   # left by ENOSPC / kill mid-write
    scripted_complete(monkeypatch, [pack_helpers.failed("sent_known", "ProviderRejected", 400)])
    try:
        outcome = run_pathway(**killed, resume=True)
        print("OUTCOME", outcome.outcome, outcome.stopped_reason)
    except Exception as e:  # noqa: BLE001
        print("RAISED", type(e).__name__, e)
        print("run.json exists:", (run_dir / "run.json").exists())
        raise
