# /code-review protocol (pass 2)

## Steps
1. Read `PROTOCOL-common.md` in the review root, then `AGENTS.md`, then your
   `files.txt`.
2. Invoke the `code-review` skill with the Skill tool at effort level `high` with your
   section's files as the target, for example:
   `Skill(skill="code-review", args="high <path1> <path2> ...")`.
   Paths are relative to `/workspace/final-workflow`. There is no diff (the tree is
   clean), so the target is the files themselves, reviewed whole.
   - If the skill accepts only one target, run it once per directory or file in your
     section, at `high` each time.
   - Do not pass `--fix` or `--comment`. This pass is read-only.
   - Follow the skill's own process (including any verification step it defines).
   - If the skill tells you to report through a UI tool such as ReportFindings, you
     may call it, but you MUST ALSO put every finding in your final message in the
     format of `PROTOCOL-common.md`. The parent agent cannot see that tool's output.
   - If the `code-review` skill is not available to you, say so in the first line of
     your report, then do the review yourself with the same scope: correctness bugs
     first, then security, then efficiency and simplification cleanups.
3. Verify each finding before you report it: reproduce it with a minimal script in your
   section folder where you can, and label each CONFIRMED or PLAUSIBLE as defined in
   `PROTOCOL-common.md`. Drop findings that you refute.
4. Return the report in the format of `PROTOCOL-common.md`, PASS: code-review, IDs
   `<SECTION>-Cnn`. Categories may include correctness, security, efficiency,
   simplification, test-coverage. Put correctness and security first.
