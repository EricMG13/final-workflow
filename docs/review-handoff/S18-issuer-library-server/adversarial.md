SECTION: S18-issuer-library-server   PASS: adversarial
COVERAGE: apps/issuer-library/{discovery.go, jobs.go, main.go, model.go, platform_other.go, platform_windows.go, server.go, settings.go, go.mod} read fully / existing *_test.go, engine/bridge.py, web/actions.js, src/deploy_workflow/cpos_handoffs.py (library.json + delivery writers), README.md skimmed for callers and contracts / none of the in-scope files left unread

All attack tests are in `S18-issuer-library-server/gocopy/attack_*_test.go`. Run them with `cd <section>/gocopy && GOTOOLCHAIN=auto go test -run TestAttack -v .`. The original suite still passes. Only the TestAttack* tests fail, and each failure reproduces a defect below. The live-binary repro is `scratch/run_timeout.sh`. It used loopback port 51888 only, and the server was stopped afterwards.

### S18-issuer-library-server-A01  [high] [CONFIRMED]  timeouts / lost review response
- Location: `apps/issuer-library/main.go:85` (run: `http.Server{... WriteTimeout: 180 * time.Second}`) versus `apps/issuer-library/jobs.go:73` (Engine.review: 10-minute timeout, commented "a large one takes minutes")
- Defect: the server's 180 s write deadline is shorter than the review it serves. Any review that takes more than about 3 minutes finishes on the server, but its response is dropped.
- Failure scenario: the user validates a large issuer folder and bridge.py's `review` (which re-reads every file) takes about 190 s. The server saves `review.json` and `status.json = "reviewed"` and keeps the intake folder (`valid = true`). The browser gets an empty reply, so it never receives `id`/`review_id`. `/api/runs/list` hides "reviewed" jobs, so the user cannot reach Start. Every retry stores a fresh copy of the upload (up to 512 MiB) and fails the same way. Large folders cannot be started from the UI at all.
- Evidence: `scratch/run_timeout.sh` runs the real binary with a fake bridge whose review sleeps 190 s. Result: `curl: (52) Empty reply from server`, `http=000 bytes=0`, `elapsed=190s`. Meanwhile `ws/intake/web-dd01…/status.json` = `{"state":"reviewed",…}` and review.json is present.
- Fix direction: keep the 10-minute bound but make it reachable. Either clear the per-request write deadline for `/api/runs/review` (`http.NewResponseController(w).SetWriteDeadline`), or make review asynchronous and have the client poll `/api/runs/status`, with "reviewed" jobs listable.

### S18-issuer-library-server-A02  [medium] [CONFIRMED]  HTML injection offset / handler panic
- Location: `apps/issuer-library/server.go:237` (reportPresentation)
- Defect: the insertion offset is computed in `bytes.ToLower(original)` and then applied to `original`. Unicode lower-casing changes byte lengths: U+0130 "İ" is 2 bytes and becomes 1, Kelvin and Ohm signs shrink, U+023A/U+023E grow, and each invalid UTF-8 byte becomes a 3-byte U+FFFD.
- Failure scenario: (a) A report for a Turkish issuer ("Türkiye İş Bankası" six times) gets the presentation `<style>/<script>` inserted 6 bytes early. Retained reports end with a font-licence `<!-- … -->` comment before `</body>`, so the adapter lands inside the comment and does nothing. If the shift reaches the report's own trailing `<script>`, it also corrupts that script. (b) 40 × "Ⱥ", or invalid UTF-8 bytes, push the offset past the end of the slice. The result is `slice bounds out of range`, the handler panics, net/http drops the connection, and the embedded report never loads.
- Evidence: `TestAttackPresentationOffset`: `turkish-I x6: inserted at 199, expected 205`; `U+023A x40: reportPresentation panicked: slice bounds out of range [:187] with capacity 161`. `TestAttackEmbeddedReportOverRealLoopback` (httptest loopback server, admitted deliveries): `presentation injected INSIDE the HTML comment (inert): "!-- licenc<style data-library-presentation>…"`, and for the glyph report `Get …?embedded=1: EOF` with `http: panic serving … slice bounds out of range [156:130]`.
- Fix direction: find `</body>` case-insensitively without changing lengths, for example with an ASCII-only fold or `bytes.EqualFold` on a 7-byte window scanned backwards. Clamp the offset to `len(original)`.

### S18-issuer-library-server-A03  [medium] [CONFIRMED]  numbers: sign/scale lost in the "value present in source excerpt" guard
- Location: `apps/issuer-library/discovery.go:17` (numericToken) and `:90-96` (admitRun)
- Defect: the token regex `-?[0-9][0-9,]*(?:\.[0-9]+)?` plus comma stripping admits metric values that the pinned quote does not state. The metric is then published as source-verified, with a pinned href.
- Failure scenario: each line below is a quote paired with a value the guard admits. "Net loss: (12.3)" admits `12.3`, a parenthesised negative accepted as positive. "As of 2024-12-31 …" admits `-12`. "margin 3-5%" admits `-5`. "Yield: .5%" admits `5` (10x). "tests 1,2,3" admits `123`. The European-format "1.234,5" admits `1.234` (1000x). Each produces a catalogue metric with the wrong sign or scale, cited to a verified source. The CP-OS writer emits `metrics: {}`, so the path is reached by hand-authored or legacy manifests (run-manifest.example.json, legacy-catalog.json seeds).
- Evidence: `TestAttackMetricExcerptGuard` reports all six cases as `admitted value "…" (case-a.revenue)`.
- Fix direction: tokenise on number boundaries. A digit or `.` before the match, or a digit after `-`, must not start a token. Treat `(x)` as `-x`. Reject comma groups that are not exactly three digits. Require the token to be whole, not a fragment of a date or range.

### S18-issuer-library-server-A04  [medium] [CONFIRMED]  job listing hides the active run
- Location: `apps/issuer-library/jobs.go:148-160` (serveRunAPI `/api/runs/list`)
- Defect: the "30 most recent" jobs are the last 30 in filename order. Job IDs are random hex (`web-<rand>`), so this order has nothing to do with recency.
- Failure scenario: once 30 or more runs have finished, a newly started run's ID sorts outside the top 30 with probability (N-30)/(N+1). After a reload or after leaving New run, the UI (actions.js `recent()`) shows neither the running job nor its progress and does not poll it. The only way back to it is gone.
- Evidence: `TestAttackRunListHidesActiveRun` (31 complete jobs `web-f…`, newest job `web-0111…` running) gives `active (newest) run missing from /api/runs/list: 30 rows`.
- Fix direction: sort by `status.json` mtime (or a timestamp in the ID), always include active ("running"/"starting") jobs, and then apply the cap.

### S18-issuer-library-server-A05  [medium] [PLAUSIBLE]  Windows managed-policy trust (ProgramData squatting)
- Location: `apps/issuer-library/settings.go:316-338` (loadConfig) and `apps/issuer-library/platform_windows.go:456` (Policy path under FOLDERID_ProgramData)
- Defect: any file at `%ProgramData%\FinalWorkflow\IssuerLibrary\settings.json` is accepted as authoritative IT policy. There is no check on the file's owner or ACL. By default, BUILTIN\Users may create subfolders in ProgramData, and every user can read them.
- Failure scenario: IT has not provisioned the folder (README: "IT must provision"). On a shared or RDS host, user A creates the policy file with `{"workspace":"C:\\Users\\Public\\x"}`. User B's library then locks to A's folder. B's uploaded issuer sources and run outputs are written there (jobs.go:252-321), and A's planted `runs/` are shown to B as B's library.
- Evidence: code reading. Only `os.ReadFile` and `json.Unmarshal` run, with no owner verification. Not reproducible on this Linux host because there is no Windows ACL environment.
- Fix direction: accept the policy only if the file and its parent folders are owned by, and writable only by, Administrators/SYSTEM. Alternatively read the policy from HKLM.

### S18-issuer-library-server-A06  [low] [CONFIRMED]  identity: run-internal delivery not matched to its run
- Location: `apps/issuer-library/discovery.go:375-386` (discover, run `deliveries/` loop)
- Defect: deliveries under `runs/<id>/deliveries/*` are attached as available "direct" artifacts without comparing `view.json` run_id/issuer_id to the run. Top-level deliverables do get this check (`:406`, `:418`).
- Failure scenario: a delivery folder copied into the wrong run, or a stale one, is shown as that run's deliverable. It also satisfies the run's checklist delivery checkpoint (`:455-469`).
- Evidence: `TestAttackRunInternalDeliveryIdentity`: `run case-a (issuer EX) shows delivery for run_id other-run / issuer ZZZ as available direct artifact`.
- Fix direction: require `view.Run.RunID == id`, plus the issuer match when the run has admitted identity. Otherwise record an issue. Note that the existing fixture in server_test.go uses a mismatched run_id and would need updating.

### S18-issuer-library-server-A07  [low] [CONFIRMED]  job lifecycle: a dead "running" job is never reconciled
- Location: `apps/issuer-library/jobs.go:395,411-423` (startRun worker on `context.Background()`, reconciliation only in the in-process goroutine) and `apps/issuer-library/server.go:271-296` (newApplication)
- Defect: a job is marked "interrupted" only by the goroutine of the process that started it. After the app exits (SIGTERM, logoff, crash, or SIGINT with the orphaned worker killed), `status.json` stays "running" forever and `activeJobs` starts empty.
- Failure scenario: after a restart, the UI shows the job as running and polls it indefinitely. Settings changes and a second paid Start are allowed, even though the old worker's fate is unknown.
- Evidence: `TestAttackStaleRunningAfterRestart` logs `status after restart: state=running, activeJobs=0`.
- Fix direction: at startup, mark "running" jobs that have no live worker (for example a PID/lock file held by the worker) as "interrupted", using the existing no-automatic-retry message.

### S18-issuer-library-server-A08  [low] [CONFIRMED]  false refusal message after a failed spawn
- Location: `apps/issuer-library/jobs.go:385-406` (startRun)
- Defect: `start.claim` is created before `command.Start()`. If the spawn fails, or the "running" status cannot be saved, no worker ran, but the claim stays.
- Failure scenario: retrying Start returns 409 "This run has already been started; no additional call was made". That is false (no run was started), and the reviewed run can never start without re-uploading.
- Evidence: `TestAttackClaimSurvivesFailedSpawn`: `first=503 "CP-OS runtime could not start" second=409 "This run has already been started; no additional call was made"`.
- Fix direction: keep the one-shot claim, but on a definite spawn failure write a distinct claim/status ("not started; review again") and return a message that says so.

### S18-issuer-library-server-A09  [low] [CONFIRMED]  settings parsing: BOM-prefixed managed policy blocks startup
- Location: `apps/issuer-library/settings.go:332` (loadConfig)
- Defect: a UTF-8 BOM, which Windows PowerShell 5.1 writes with `Set-Content/Out-File -Encoding UTF8`, makes `json.Unmarshal` fail.
- Failure scenario: IT provisions the documented `{"workspace": "D:\\…"}` with PowerShell. Every user's app then exits at launch with "invalid configuration …: invalid character 'ï'".
- Evidence: `TestAttackPolicyWithBOM`: `BOM-prefixed managed configuration refused: … invalid character 'ï' looking for beginning of value`.
- Fix direction: strip a leading `EF BB BF` before unmarshalling. Keep failing closed on any other invalid content.

### Out of scope (one line each, optional)
- None found that warrants a line. bridge.py validates cap_usd and config, and Go passes them through only as raw strings.

### Checked and sound (short bullets: what you attacked that held)
- Host/Origin/Sec-Fetch-Site gate: DNS-rebinding hosts, Origin "null" from sandboxed reports, and cross-site POSTs are all rejected. POSTs need the custom header (forces a preflight, and OPTIONS returns 405), and `/api/settings` also requires `application/json`.
- serveFile: only files in the Allowed map are served. Traversal (`..`, backslash, `:`, NUL, escaped segments) and alternative spellings miss the map or fail localPath. os.Root plus the Lstat regular-file check block symlink and device escapes. The verified-hash and `?sha256=` pins are compared against the bytes actually served.
- CSP: reports get `sandbox allow-scripts allow-downloads` with `connect-src 'none'` and no allow-same-origin. Only verified, hash-pinned HTML with `embedded=1` may be framed by the app origin. The download path returns the original bytes.
- Upload path handling: validSourcePath (filepath.IsLocal rejects `:`/reserved names on Windows, plus path.Clean equality), O_EXCL writes and os.Root confinement. Duplicate or case-colliding paths are refused and the intake folder is cleaned up. Limits hold: 500 files, 64 MiB per file, 512 MiB total.
- Start is one-shot under concurrency (claim file O_EXCL under app.mu, review_id binding, provider_ready). Settings and quit are refused while a job is active.
- Discovery: symlinked run/delivery folders are skipped. Files under hidden folders are not indexed. Manifest source keys are namespaced. Failed admissions publish no sources or Allowed entries. The checklist requires all five stages and verified evidence, so the completion divide has Total > 0. Delivery hashes are re-checked on every refresh.
- saveJSON: temp file in the same directory, fsync, then rename with a bounded retry. Policy precedence over user settings fails closed on invalid or relative paths.
- Windows helpers: knownFolder reads only up to the NUL terminator, the DLLs are KnownDLLs, and the browser launch URL is fixed.
