SECTION: S18-issuer-library-server   PASS: code-review
COVERAGE: apps/issuer-library/{discovery.go, jobs.go, main.go, model.go, platform_other.go, platform_windows.go, server.go, settings.go, go.mod} read in full / skimmed: existing *_test.go, README.md, engine/bridge.py (only lines that use review_id and cap_usd), src/deploy_workflow/cpos_handoffs.py library_metadata / not read: none in scope

Independence note: the code-review skill (high) ran as a fork with the reviewer constraint stated. Its output did not mention any adversarial finding. I did not read adversarial.md, scratch/, attack_*_test.go or docs/review-handoff/**.
Toolchain: fresh copy at <section>/cr-gocopy/. `GOTOOLCHAIN=auto go vet ./... && go test ./...` is clean (ok). All repros are in `cr-gocopy/cr_repro_test.go`. Each test PASSES when the defect is present. Run them with `cd <section>/cr-gocopy && GOTOOLCHAIN=auto go test -count=1 -run TestCR_ -v ./...` (all 10 pass, 8.3s).

### S18-issuer-library-server-C01  [high] [CONFIRMED]  correctness
- Location: `apps/issuer-library/main.go:85` (run, http.Server WriteTimeout 180s), together with `apps/issuer-library/jobs.go:73` (Engine.review, 10-minute timeout) and `jobs.go:338-350` (reviewRun)
- Defect: the server's WriteTimeout (180 s) is shorter than the time POST /api/runs/review may legitimately take (the engine gets up to 10 min; jobs.go:72 says "a large one takes minutes"), so a review that takes more than about 3 minutes can never return its response.
- Failure scenario: the user uploads a large folder and the launcher review takes 4 min. net/http's write deadline has already passed, so the browser gets EOF or a network error. The handler keeps running and writes review.json plus status.json `reviewed`. The review_id needed for Start is returned only in that lost response, and /api/runs/list hides `reviewed` jobs. The review is orphaned in intake/ and the user must upload and review again (and it fails again for the same reason).
- Evidence: `TestCR_WriteTimeoutLosesSlowReview`, scaled to WriteTimeout 1 s and a review that takes 2 s: `client error: Post ".../api/runs/review": EOF`; `orphaned job web-03e3... status={"state":"reviewed",...}`; `/api/runs/list = []`.
- Fix direction: make the review request outlive the engine timeout, either with http.ResponseController.SetWriteDeadline in reviewRun or by running the review asynchronously and having the client poll for it, and list `reviewed` jobs so a lost response can be recovered.

### S18-issuer-library-server-C02  [medium] [CONFIRMED]  correctness
- Location: `apps/issuer-library/jobs.go:385-406` (startRun)
- Defect: start.claim is created before the status write and the process spawn, and it is never removed when `saveJSON(running)` or `command.Start()` fails, although no worker (and so no provider call) ever ran.
- Failure scenario: the bundled python.exe is blocked by antivirus or ISSUER_LIBRARY_PYTHON is wrong. Start returns 503 "could not start". After the runtime is fixed, Start returns 409 "This run has already been started; no additional call was made", which is false. The reviewed run can never be started, and the user must upload and review everything again.
- Evidence: `TestCR_ClaimSurvivesSpawnFailure`: `first start: 503 CP-OS runtime could not start`, `second start after repair: 409 This run has already been started; no additional call was made`, and the worker never ran (no synthetic-starts.txt).
- Fix direction: remove start.claim only on those two pre-spawn failure paths, where the process never existed. This keeps the one-shot guard for every case where a worker actually started.

### S18-issuer-library-server-C03  [medium] [PLAUSIBLE]  security
- Location: `apps/issuer-library/server.go:58-62` (ServeHTTP), `main.go:47-55` (predictable per-user port)
- Defect: the API's only protection is the Host, Origin, Sec-Fetch-Site and X-Issuer-Library checks. These stop browser and DNS-rebinding attacks, but there is no per-launch secret, so any local process, including another user's on a shared machine (loopback is shared), can read the catalogue and /files/* and can POST /api/runs/review and /api/runs/start. Every one of those headers is client-settable.
- Failure scenario: on a Windows RDS or Citrix host (the packaging targets managed Windows with IT policy), user B finds user A's port (crc32 of A's state path, or by scanning 49000-58999), downloads A's confidential issuer files and reports, or uploads sources into A's workspace and starts a paid run with B's chosen cap_usd, executed with the provider keys in A's environment.
- Evidence: the existing tests drive every endpoint with only those headers (e.g. `call()` in server_test.go; TestExplicitStartIsOneShotUnderConcurrentRequests starts a run). A cross-user exploit could not be reproduced: this sandbox has a single OS user and no second session.
- Fix direction: generate a random per-launch token, pass it to the browser in the opened URL (exchange it for an HttpOnly SameSite=Strict cookie), and require it on every /api and /files request.

### S18-issuer-library-server-C04  [medium] [CONFIRMED]  correctness
- Location: `apps/issuer-library/discovery.go:374-386` (discover, runs/<id>/deliveries loop)
- Defect: a delivery under runs/<id>/deliveries/ is attached to run <id> as an available direct artifact without comparing view.json's run_id or issuer_id with the run. The deliverables/ path checks the issuer (line 406), and README "Every immediate subfolder of deliverables/ and of a run's deliveries/ is checked using ... view.json issuer/run identity" promises the same check here.
- Failure scenario: a delivery folder for another issuer or run is copied into runs/X/deliveries/. It passes its own hash checks and is shown as X's deliverable (wrong issuer report under X). For a manifest with a checklist delivery checkpoint it also satisfies the completeness gate at line 460, so X's completion is shown as verified.
- Evidence: `TestCR_RunDeliveryIdentityUnchecked`: a delivery with run_id `some-other-run` and issuer `OTHER-ISSUER` placed under runs/case-a/deliveries/ gives `case-a (issuer EX) artifact runs/case-a/deliveries/foreign available=true issue=""`.
- Fix direction: require view.Run.RunID == id (and IssuerID == run.Issuer when the run has a manifest identity) before attaching; otherwise list it with an issue as the deliverables/ path does.

### S18-issuer-library-server-C05  [medium] [CONFIRMED]  correctness
- Location: `apps/issuer-library/jobs.go:147-158` (serveRunAPI, /api/runs/list)
- Defect: the handler treats the end of os.ReadDir's name-sorted list as the most recent jobs and stops at 30, but job IDs are `web-` plus random hex, so the list is an arbitrary 30. README says "Recent runs lists every run in the workspace".
- Failure scenario: once a workspace has more than 30 non-`reviewed` jobs, a just-started run whose ID begins `web-0...` sorts first and is cut off. The user cannot see or open the active run from Recent runs.
- Evidence: `TestCR_RunListIsNotRecent`: 40 older stopped jobs plus one new `running` job `web-0aaa...` gives `30 rows returned; the just-started running job web-0aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa is absent`.
- Fix direction: sort candidates by a real timestamp (status.json or folder mtime, or a created_at in job.json) before truncating, or drop the cap as README describes.

### S18-issuer-library-server-C06  [medium] [CONFIRMED]  correctness
- Location: `apps/issuer-library/server.go:237` (reportPresentation)
- Defect: the `</body>` offset is found in `bytes.ToLower(original)` but used to slice `original`. bytes.ToLower changes byte length for some runes (U+0130 'İ' 2->1 byte, Kelvin sign 3->1) and for invalid UTF-8 (1->3 bytes), so the presentation <style>/<script> is spliced at the wrong place.
- Failure scenario: an embedded report for a Turkish issuer containing "İSTANBUL İZMİR" gets the adapter injected inside `</table>` ("</tab" + style/script + "le>"), which breaks the markup of the embedded report. Invalid UTF-8 moves the splice past `</body>` instead.
- Evidence: `TestCR_ReportPresentationOffset`: `turkish-dotted-I: injected before "</tr></tab", original tail after injection "le></body></html>"`; `invalid-utf8: ... tail "></html>"`.
- Fix direction: search case-insensitively on the original bytes (e.g. scan for "</" and compare the next 5 bytes with bytes.EqualFold), so the index refers to `original`.

### S18-issuer-library-server-C07  [low] [CONFIRMED]  correctness
- Location: `apps/issuer-library/server.go:169-170,230` (serveFile) together with `main.go:103-105` (refresh ticker)
- Defect: serveFile holds app.mu.RLock (deferred) across http.ServeContent, i.e. while writing up to 64 MiB to the client. If the client stops reading, the 30 s ticker's Lock() waits, and because RWMutex then blocks new readers, every request that needs the lock (catalogue, files, start, settings) hangs until that client resumes or WriteTimeout (180 s) fires.
- Failure scenario: a browser tab or download that stalls on a large PDF freezes the whole library UI for up to 3 minutes.
- Evidence: `TestCR_ServeFileHoldsLockDuringNetworkWrite`: a raw client requests a 48 MiB file and does not read; after a ticker-style Lock(), `/api/catalogue ... context deadline exceeded (Client.Timeout exceeded while awaiting headers)`.
- Fix direction: copy hash, allowed and workspace under the lock, release it, then read, verify and serve the file without the lock.

### S18-issuer-library-server-C08  [low] [CONFIRMED]  correctness
- Location: `apps/issuer-library/server.go:122-126` (post /api/settings) with `jobs.go:248-250` (reviewRun takes the workspace once)
- Defect: in-flight reviews are not tracked, so the workspace can be switched while a review (up to 10 min) is running. The review completes into the old workspace, while startRun and the status GETs look in the new one.
- Failure scenario: during a slow review the user changes Settings to workspace B (allowed: activeJobs is empty). The review returns OK with a review_id, but Start replies 409 "Review this run before starting".
- Evidence: `TestCR_SettingsSwitchDuringReview`: `settings during review: 200`, `review: 200 id=web-b715...`, `start: 409 Review this run before starting`.
- Fix direction: count in-flight reviews (e.g. a reviews counter checked by /api/settings), or record the workspace in the job and resolve it from there.

### S18-issuer-library-server-C09  [low] [CONFIRMED]  correctness
- Location: `apps/issuer-library/discovery.go:368-386` (discover)
- Defect: manifest-declared artifacts are all reset to "Delivery folder not found", and only deliverables/ folders are matched back to them. A declared artifact under runs/<id>/deliveries/ stays marked missing, and the runDeliveries loop appends a second, available entry for the same folder.
- Failure scenario: a library.json with `artifacts:[{folder:"runs/r1/deliveries/v1"}]` shows the same delivery twice, once as missing and once as available.
- Evidence: `TestCR_DeclaredRunDeliveryDuplicated`: `artifact available=false issue="Delivery folder not found"` and `artifact available=true issue=""` for the same folder.
- Fix direction: in the runDeliveries loop, update a declared entry with the same Folder (keeping its label and relationship, as the deliverables/ loop does) instead of appending.

### S18-issuer-library-server-C10  [low] [CONFIRMED]  correctness
- Location: `apps/issuer-library/main.go:45-46,128` (run/main)
- Defect: run() closes logFile with defer, but main() then calls log.Print(err) while log output still points at the closed file, so every fatal startup or serve error is silently dropped from library.log.
- Failure scenario: the port is taken, settings.json is invalid or Serve fails. library.log has no record; on Windows the only trace is a transient MessageBox.
- Evidence: `TestCR_MainLogsToClosedFile` (runs run() then log.Print like main): `run() error: local port is occupied by another application: ...; library.log = ""`.
- Fix direction: log the error inside run() before returning, or restore log.SetOutput(os.Stderr) in the deferred close.

### S18-issuer-library-server-C11  [low] [CONFIRMED]  efficiency
- Location: `apps/issuer-library/main.go:95-107` and `server.go:36-44` (refreshLocked)
- Defect: every 30 s the ticker runs a full discover(), which re-reads and SHA-256-hashes every pinned source and every delivery file (up to 64 MiB each) and rewrites index.json, all under the exclusive app.mu lock, even when nothing changed.
- Failure scenario: in a workspace with large delivery files, every tick blocks all lock-taking requests (catalogue, files, start, settings) for about a second or more and rewrites the index file.
- Evidence: `TestCR_RefreshHashesUnderWriteLock`: `one refreshLocked (ticker body) held the write lock for 897ms with 4x60 MiB delivery files`.
- Fix direction: run discover() without the lock and swap the result in under a short Lock; optionally skip unchanged files by size/mtime.

### S18-issuer-library-server-C12  [low] [CONFIRMED]  efficiency
- Location: `apps/issuer-library/jobs.go:297-319` (reviewRun upload loop)
- Defect: each uploaded part, which ParseMultipartForm has already spooled to disk, is read fully into memory with io.ReadAll (up to 64 MiB) before being written and hashed.
- Failure scenario: concurrent reviews of folders with near-limit files each hold 64 MiB slices on top of multipart buffers. This is avoidable memory pressure on user desktops.
- Evidence: code reading (jobs.go:298 `io.ReadAll(io.LimitReader(stream, (64<<20)+1))`, then `destination.Write(raw)` and `digest(raw)`).
- Fix direction: stream with io.Copy(destination, io.TeeReader(io.LimitReader(stream, max+1), sha256.New())) and check the copied size.

### Out of scope (one line each, optional)
- none

### Checked and sound (short bullets: what you attacked that held)
- Browser and DNS-rebinding boundary: Host must equal 127.0.0.1:port; foreign Origin and cross-site Sec-Fetch-Site are refused; POSTs need the custom X-Issuer-Library header (which forces a preflight, and OPTIONS is refused) and, outside /api/runs, an exact application/json Content-Type.
- Upload paths: validSourcePath with filepath.IsLocal, path.Clean equality and no backslash/NUL, plus os.Root and O_EXCL writes; duplicate or nested names fail closed and the folder is removed when valid=false.
- Served files: only names in Allowed; localPath rejects ':'/'\'; readFile rejects non-regular files and symlinks (Lstat plus fstat) and files over 64 MiB; the hash pin and the ?sha256 pin are both verified on the exact bytes served; HTML is sandboxed with an opaque origin and frame-ancestors 'none' unless the file is hash-verified and embedded.
- Start is one-shot under concurrency: app.mu plus the O_EXCL claim; review_id and provider_ready are re-read from review.json; the worker exit converts a stale `running` status to `interrupted` without a paid retry.
- Run metadata admission: metric values must appear verbatim in the pinned quote, with unit, period and basis required; "0" is preserved as a value, not treated as missing; failed manifests publish no Allowed entries or sources; checklist stages, duplicate IDs and evidence are validated; Total>0 guards the division.
- saveJSON is atomic (temp file, fsync, rename with retries); a policy file has precedence and is not silently overridden.
