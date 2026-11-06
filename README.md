# SECData issuer runs for the Issuer Library (2026-11-05)

The 101 SECData credit snapshots (host session, `minimum` module set, as of 2026-11-05) that pass
the Issuer Library gate. They are kept on this branch, not in `main`, so a download of the
repository stays small. Each part is at most 40 MB.

To install, download the five `issuer-runs-part-*.zip` files and check them against
`SHA256SUMS.txt`. Extract each into the library's workspace folder, the one holding `runs/` and
`deliverables/`. Together they add the `runs/cpos-swarm-20261105-*` folders, each with its
`library.json`. Reload the library.

Each run passed the gate in `deploy_workflow.cpos_library`:

- Its instructions and layout match the current launcher's.
- Its report is published and hash-checked, and every section is populated.
- Every chart series has a plotted value.
- Its manifest has every field the library shows.

No run has had an independent review of its content, so treat each as a candidate.

The parts are built with `deploy_workflow.cpos_library --package` from the run folders at
`a7812217`, and a rebuild is byte-identical. See PR #16 and `VERIFICATION.md` on `main` once it
merges.
