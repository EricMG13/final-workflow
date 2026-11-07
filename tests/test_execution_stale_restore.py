"""A stale head whose inputs return to an earlier settled set gets that settled result back.

Breaks caught: after replace_pack(B) and replace_pack(A) every head is stale, and `begin` refused
the module's own earlier settled input set, so no module could run or be restored.
"""

from pathlib import Path

import pytest
import test_connect_cp3c as tc

from deploy_vii.execution import Execution, Head

PLAN = ["CP-0", "CP-1", "CP-1A", "CP-2", "CP-2D"]  # the settled modules of tc.make_store, in order


def _heads(store: Execution) -> dict[str, Head]:
    return {h.module_id: h for h in store.read().heads}


def _swap_and_revert(store: Execution, pack: tc.PreparedPack) -> None:
    store.replace_pack(pack.model_copy(update={"sources": pack.sources[:1]}))  # pack B
    store.replace_pack(pack)  # back to pack A, byte for byte


def test_pack_swap_and_revert_restores_every_head_without_a_new_attempt(tmp_path: Path) -> None:
    store, pack = tc.make_store(tmp_path)
    before = _heads(store)
    attempts = store.read().attempts
    assert [a.status for a in attempts] == ["finished"] * len(attempts)
    _swap_and_revert(store, pack)
    assert {h.status for h in store.read().heads} == {"stale"}
    for module_id in PLAN:  # each begin needs its upstream restored first
        returned = store.begin(module_id)
        mine = [a for a in attempts if a.module_id == module_id]
        assert returned == mine[-1] and returned.status == "finished"
        assert _heads(store)[module_id] == before[module_id]
    # Expected: the journal is as it was before the swap. No attempt was added, and every head
    # (status, result hash, inputs, qualification, no staleness notes) is the pre-swap record.
    assert store.read().attempts == attempts
    assert _heads(store) == before
    with pytest.raises(ValueError, match="settled or its one repair"):
        store.begin("CP-0")  # idempotent: a current head still refuses its settled input set


def test_a_current_settled_head_still_refuses_begin(tmp_path: Path) -> None:
    store, _ = tc.make_store(tmp_path)
    attempts = store.read().attempts
    for module_id in PLAN:
        with pytest.raises(ValueError, match="settled or its one repair"):
            store.begin(module_id)
    assert store.read().attempts == attempts


def test_a_consumer_is_refused_until_its_upstream_is_restored(tmp_path: Path) -> None:
    store, pack = tc.make_store(tmp_path)
    _swap_and_revert(store, pack)
    with pytest.raises(ValueError, match="unrun, stale or blocked"):
        store.begin("CP-1")
    store.begin("CP-0")
    assert _heads(store)["CP-1"].status == "stale"  # restoring CP-0 keeps its consumers stale


def test_a_head_rerun_on_the_other_pack_is_replaced_by_the_earlier_result(tmp_path: Path) -> None:
    store, pack = tc.make_store(tmp_path)
    original = _heads(store)["CP-0"]
    store.replace_pack(pack.model_copy(update={"sources": pack.sources[:1]}))  # pack B
    tc._settle(store, "CP-0", None, True)  # a real second CP-0 attempt on pack B
    on_b = _heads(store)["CP-0"]
    assert on_b.result_sha256 != original.result_sha256 and on_b.status == "restricted"
    assert len([a for a in store.read().attempts if a.module_id == "CP-0"]) == 2
    store.replace_pack(pack)  # back to pack A: the CP-0 head (on B) is stale again
    assert _heads(store)["CP-0"].status == "stale"
    returned = store.begin("CP-0")
    assert returned.inputs == original.inputs and returned.status == "finished"
    # The qualification an earlier head earned is not kept on the attempt: it comes back unrun
    # (None), never invented; every other field is the original head's.
    assert original.qualification is not None
    restored = _heads(store)["CP-0"]
    assert restored == original.model_copy(update={"qualification": None})
    assert restored.notes == ()
    assert len([a for a in store.read().attempts if a.module_id == "CP-0"]) == 2  # none added
