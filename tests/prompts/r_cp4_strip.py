"""Undo the S09-cp4-cp5-A08 sentence in CP-4's composed message (`legal_covenants` only): rule e
(`CP4_METRIC_RULE`) gained one sentence naming the new refusal of `Same definition` when a quote
says the term is defined in a document that is not in the pack. Removing exactly that sentence and
the space before it gives the message the frozen digests pinned before the ruling."""

R_CP4_SENTENCE = (
    " `metric_basis` is also Not determinable, never Same definition, when a quote of the "
    "covenant says the term is defined in a named agreement, indenture or other instrument that "
    "is not a SOURCE block of this run: Python refuses Same definition there."
)


def undo_r_cp4(step_id: str, text: str) -> str:
    """Remove the A08 sentence from rule e of a composed CP-4 message."""
    if step_id != "legal_covenants":
        return text
    assert text.count(R_CP4_SENTENCE) == 1, step_id
    return text.replace(R_CP4_SENTENCE, "")
