import json, sys, collections
from pathlib import Path

R = Path("/tmp/claude-0/-home-user/ca174d89-4735-5f2e-9387-3daad8bafeb2/scratchpad/review")
sys.path.insert(0, str(R / "fable"))
from verdicts import V  # noqa: E402

findings = {f["id"]: f for f in json.load(open(R / "findings.json"))}
ids = [v[0] for v in V]
assert len(ids) == len(set(ids)) == 257, (len(ids), len(set(ids)))
assert set(ids) == set(findings), set(ids) ^ set(findings)
order = {f["id"]: i for i, f in enumerate(json.load(open(R / "findings.json")))}
V.sort(key=lambda v: order[v[0]])

rows = []
counts = collections.Counter()
ml = collections.Counter(v[4] for v in V if findings[v[0]]["severity"] in ("medium", "low"))
hi = collections.Counter(v[4] for v in V if findings[v[0]]["severity"] in ("critical", "high"))
assert hi == {"rerun": 47}, hi
changed = 0
for fid, verdict, sev_out, dup, basis, note in V:
    sev_in = findings[fid]["severity"]
    counts[verdict] += 1
    if sev_out is None:
        out = f"{sev_in} (KEEP)"
    else:
        level, reason = sev_out.split("|", 1)
        rank = {"low": 0, "medium": 1, "high": 2, "critical": 3}
        direction = "RAISE" if rank[level] > rank[sev_in] else "LOWER"
        out = f"{level} ({direction}: {reason})"
        changed += 1
    assert len(note.split()) <= 25, (fid, len(note.split()))
    rows.append(f"| {fid} | {verdict} | {sev_in} | {out.replace(chr(124), chr(92)+chr(124))} | {dup} | {basis} | {note.replace(chr(124), chr(92)+chr(124))} |")

summary = f"""## Summary

Verdicts over all 257 findings: **{counts['AGREE']} AGREE, {counts['DISAGREE']} DISAGREE, {counts['NEEDS-EVIDENCE']} NEEDS-EVIDENCE**. I re-ran every one of the 47 critical/high repros myself (45 Python scripts or Go tests, plus the live Go binary for S18-A01) and all 47 reproduced; of the 210 medium/low findings, {ml['rerun']} were re-run (patching four scripts whose paths pointed at the old `/workspace` checkout), {ml['code-read']} were settled by reading the cited code, and {ml['report-only']} timing-only efficiency items were taken from the report. I changed **{changed} severities**: 16 raised (2 to critical: S12-A02 signed-refund flip and S13-C01 quarter period label on trailing ratios; S13-A03 to high, S13-C06 and S16-C05 to medium on their own merits; 11 duplicates lifted to their group's level) and 6 lowered for reachability (S05-C02, S10-C01, S11-C07, S12-C02, S17-C03, S18-A03). I found **42 duplicate groups** (listed below), mostly adversarial/code-review pairs within a section, plus six that span sections (substring quote matching, `splitlines` locators, raw `{{ref}}` claim limitations, dead CP-OS transport, repeated validation per submit, copy-pasted owner helpers). Four findings cite line numbers that do not exist in the file (S17-A08, S17-C12, S18-A05, S18-A09: `runtime.py` has 74 lines, `settings.go` 79, `platform_windows.go` 62); their defects are real but the citations must be fixed before the report is handed on. S10-A05's root cause (the CP-8 registry entry) lives in `owner_workflow.py`, an S02 file. The three worst problems in the codebase: (1) **units, currency, scale and sign are stamped by Python from model text or a default and never checked against the cited source** — the same hole appears in the CP-1D bridge (S05-C01 critical, deterministic 1000x + wrong currency), CP-1D basis amounts (S05-A01), CP-2E rows (S06-A04 thousands as millions, S06-A03/C01 interest sign), CP-3D levels (S08-A03/A04 percent read as price, bp as %), the research peer sheet (S16-A01/A02/C01/C02) and the shared `quotes.quoted` substring matcher (S13-A03/C05) that lets "2.50:1.00" verify against "12.50:1.00"; (2) **period arithmetic and labelling in the deploy_vii engine is wrong for whole classes of inputs** — CFS balances summed as flows (S12-A01 critical: Q2 closing cash 20 instead of 520), a signed tax refund flipped to an outflow (S12-A02), trailing ratios labelled with the quarter's dates (S13-C01), leap-year and Q1->Q2 pairs refused by the earnings delta (S11-A04), annual columns verified as Q4 under dated headers (S11-A01), and structural BLOCKs hidden as WARN "absent input" (S13-A01/C02); (3) **validators that accept a model answer and then wedge or mislead** — CP-2D can never settle for an issuer without a facility schedule (S06-A01), CP-4C passes validation then raises after the paid response is retained (S09-A04/C02), CP-5 flags every verbatim copy table as a figure mismatch (S09-A01/C01), CP-2G accepts an unchecked break metric and unvalidated limitation text (S07-A01/A02), and the CP-8 run comparison has no code-level diff at all (S01-A03 and CLAIMS #2, which I confirm: `comparison_files` checks table shape and citations only).
"""

table = "\n".join(
    ["## Findings table", "", "| id | verdict | severity_in | severity_out | duplicate_of | basis | note |", "|---|---|---|---|---|---|---|"]
    + rows
)

repro = open(R / "fable" / "repro_log.md").read()
groups = open(R / "fable" / "dup_groups.md").read()
disagree = open(R / "fable" / "disagreements.md").read()

out = "# Fable review of all 257 findings (repo a313b50 + docs/review-handoff, read-only)\n\n" + summary + "\n" + table + "\n\n" + repro + "\n\n" + groups + "\n\n" + disagree
(R / "FABLE-REVIEW.md").write_text(out)
print(counts, "changed", changed, "rows", len(rows))
print(summary)
