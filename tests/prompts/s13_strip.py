"""Undo the S13 run-text sentences in a composed message: ``FIGURE_WORDS_RULE`` (S13 A04/C07,
appended to the source_readiness run-text rule and the narrative/readiness prose rule).
Removing exactly those sentences and the space before each gives the message the frozen digests
pinned before the fix."""

from deploy_vii.live.prompts import FIGURE_WORDS_RULE

S13_SENTENCES = (" " + FIGURE_WORDS_RULE,)


def undo_s13(step_id: str, text: str) -> str:
    """Remove every S13 sentence from a composed message (``step_id`` kept for symmetry with
    the other strips: the sentences are removed wherever they occur)."""
    del step_id
    for sentence in S13_SENTENCES:
        text = text.replace(sentence, "")
    return text
