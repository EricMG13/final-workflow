package main

import (
	"bytes"
	"context"
	"crypto/rand"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"errors"
	"fmt"
	"io"
	"io/fs"
	"log"
	"net/http"
	"os"
	"os/exec"
	"path"
	"path/filepath"
	"regexp"
	"sort"
	"strconv"
	"strings"
	"time"
)

var jobID = regexp.MustCompile(`^web-[a-f0-9]{32}$`)
var moduleCode = regexp.MustCompile(`^CP-[A-Z0-9]+$`)

type Engine struct{ Python, Script string }

func localEngine() Engine {
	executable, _ := os.Executable()
	folder := filepath.Join(filepath.Dir(executable), "engine")
	if override := os.Getenv("ISSUER_LIBRARY_ENGINE_ROOT"); override != "" {
		folder = override
	}
	python := os.Getenv("ISSUER_LIBRARY_PYTHON")
	if python == "" {
		python = filepath.Join(folder, "runtime", "python.exe")
	}
	return Engine{Python: python, Script: filepath.Join(folder, "bridge.py")}
}
func (engine Engine) process(ctx context.Context, script string, arguments ...string) *exec.Cmd {
	command := exec.CommandContext(ctx, engine.Python, append([]string{"-I", "-B", "-X", "utf8", script}, arguments...)...)
	configureWorkerCommand(command)
	command.Stderr = io.Discard
	return command
}

func (engine Engine) command(ctx context.Context, operation, folder string) *exec.Cmd {
	return engine.process(ctx, engine.Script, operation, folder)
}

// library parses the workspace's handoffs for the app; the catalogue names what to show.
// store.py imports only the standard library, so a page load does not pay for the engine.
func (engine Engine) library(workspace string, catalogue []byte) ([]byte, error) {
	if _, err := os.Stat(engine.Python); err != nil {
		return nil, fmt.Errorf("CP-OS runtime is unavailable; use the complete application package")
	}
	ctx, cancel := context.WithTimeout(context.Background(), 120*time.Second)
	defer cancel()
	command := engine.process(ctx, filepath.Join(filepath.Dir(engine.Script), "store.py"), workspace)
	command.Stdin = bytes.NewReader(catalogue)
	output, err := command.Output()
	if err != nil || !json.Valid(output) {
		return nil, fmt.Errorf("the workspace could not be read; check the runtime installation and workspace folder")
	}
	return output, nil
}

// reviewTimeout bounds one launcher review; a variable so tests can shorten it.
var reviewTimeout = 10 * time.Minute

// reviewWriteGrace is the time left to write a review response after the review ends.
const reviewWriteGrace = 30 * time.Second

func (engine Engine) review(folder string) (json.RawMessage, error) {
	if _, err := os.Stat(engine.Python); err != nil {
		return nil, fmt.Errorf("CP-OS runtime is unavailable; use the complete application package")
	}
	// The launcher reads every file in the folder, so a large one takes minutes.
	ctx, cancel := context.WithTimeout(context.Background(), reviewTimeout)
	defer cancel()
	output, err := engine.command(ctx, "review", folder).Output()
	if len(output) > 1<<20 || !json.Valid(output) {
		return nil, fmt.Errorf("CP-OS validation could not complete; check the runtime installation")
	}
	if err != nil {
		var result struct {
			OK bool `json:"ok"`
		}
		if json.Unmarshal(output, &result) != nil || result.OK {
			return nil, fmt.Errorf("CP-OS validator failed")
		}
	}
	return output, nil
}

type UploadedSource struct {
	Path   string `json:"path"`
	SHA256 string `json:"sha256"`
}
type NewJob struct {
	ID        string           `json:"id"`
	Workspace string           `json:"workspace"`
	Config    string           `json:"config"`
	Cap       string           `json:"cap_usd"`
	Modules   []string         `json:"modules"`
	MaxTurns  int              `json:"max_turns"`
	Sources   []UploadedSource `json:"sources"`
}
type JobStatus struct {
	State   string `json:"state"`
	Message string `json:"message"`
	ID      string `json:"id,omitempty"`
}

// jobView reads a job's own files: status, the app-written review and the
// module/step progress. None of them holds provider text.
func jobView(workspace, id string) (map[string]any, bool) {
	raw, err := os.ReadFile(filepath.Join(workspace, "intake", id, "status.json"))
	if err != nil {
		return nil, false
	}
	var status map[string]any
	if json.Unmarshal(raw, &status) != nil {
		return nil, false
	}
	if raw, err := os.ReadFile(filepath.Join(workspace, "intake", id, "review.json")); err == nil {
		var review map[string]any
		if json.Unmarshal(raw, &review) == nil {
			for _, key := range []string{"issuer", "pathway", "as_of", "modules", "module_details"} {
				if value, present := review[key]; present {
					status[key] = value
				}
			}
		}
	}
	if value, ok := runProgress(workspace, id); ok {
		status["progress"] = value
	}
	status["id"] = id
	info, statErr := os.Stat(filepath.Join(workspace, "runs", id))
	status["run_available"] = statErr == nil && info.IsDir()
	return status, true
}

// eventsLimit bounds how much of a run's event log is read.
const eventsLimit = 4 << 20

// runEvent is one line of runs/<id>/events.jsonl, written by the CP-OS loop. Amounts are the
// decimal strings it wrote.
type runEvent struct {
	Event    string `json:"event"`
	Module   string `json:"module"`
	Turn     int    `json:"turn"`
	MaxTurns int    `json:"max_turns"`
	SpentUSD string `json:"spent_usd"`
	HeldUSD  string `json:"held_usd"`
	CapUSD   string `json:"cap_usd"`
}

// runProgress folds a run's event log into the progress shown for it. A retained run has
// no log and falls back to its progress.json. An unparsable last line is a write in flight
// and is dropped. An unparsable earlier line skips the whole log and falls back to
// progress.json: a documented fail-open, because progress is advisory, logged once here.
// A log with no events yet has no progress either.
func runProgress(workspace, id string) (map[string]any, bool) {
	folder := filepath.Join(workspace, "runs", id)
	if file, err := os.Open(filepath.Join(folder, "events.jsonl")); err == nil {
		raw, readErr := io.ReadAll(io.LimitReader(file, eventsLimit))
		file.Close()
		if readErr == nil {
			if events, ok := parseEvents(raw); ok && len(events) > 0 {
				return foldEvents(events), true
			} else if !ok {
				log.Printf("run %s: events.jsonl has an unreadable line; falling back to progress.json", id)
			}
		}
	}
	raw, err := os.ReadFile(filepath.Join(folder, "progress.json"))
	if err != nil {
		return nil, false
	}
	var value map[string]any
	if json.Unmarshal(raw, &value) != nil {
		return nil, false
	}
	return value, true
}

func parseEvents(raw []byte) ([]runEvent, bool) {
	lines := bytes.Split(raw, []byte("\n"))
	if len(lines[len(lines)-1]) == 0 {
		lines = lines[:len(lines)-1]
	}
	var events []runEvent
	for number, line := range lines {
		var event runEvent
		if err := json.Unmarshal(line, &event); err != nil {
			if number == len(lines)-1 {
				break
			}
			return nil, false
		}
		events = append(events, event)
	}
	return events, true
}

func foldEvents(events []runEvent) map[string]any {
	progress := map[string]any{"accepted": 0}
	steps := map[string]string{"module_started": "started", "turn": "running", "draft_rejected": "repairing",
		"module_accepted": "accepted", "delivery_started": "delivering", "delivered": "delivered", "stopped": "stopped"}
	for _, event := range events {
		if step, known := steps[event.Event]; known {
			progress["step"] = step
		}
		switch event.Event {
		case "module_started":
			progress["module"] = event.Module
		case "module_accepted":
			progress["accepted"] = progress["accepted"].(int) + 1
		case "turn":
			progress["turn"], progress["max_turns"] = event.Turn, event.MaxTurns
			progress["spent_usd"], progress["held_usd"], progress["cap_usd"] = event.SpentUSD, event.HeldUSD, event.CapUSD
		}
	}
	return progress
}

// recentJobs lists every running job plus the most recently written
// others, newest first, up to limit rows in all. Job ids are random, so recency is the
// modification time of status.json, never the folder name. Reviewed-only drafts are
// not runs and are left out.
func recentJobs(workspace string, limit int) []map[string]any {
	entries, _ := os.ReadDir(filepath.Join(workspace, "intake"))
	type candidate struct {
		id     string
		when   time.Time
		active bool
	}
	var candidates []candidate
	active := 0
	for _, entry := range entries {
		id := entry.Name()
		if !jobID.MatchString(id) {
			continue
		}
		file := filepath.Join(workspace, "intake", id, "status.json")
		info, err := os.Stat(file)
		raw, readErr := os.ReadFile(file)
		var status struct {
			State string `json:"state"`
		}
		if err != nil || readErr != nil || json.Unmarshal(raw, &status) != nil || status.State == "reviewed" {
			continue
		}
		running := status.State == "running"
		if running {
			active++
		}
		candidates = append(candidates, candidate{id, info.ModTime(), running})
	}
	sort.Slice(candidates, func(i, j int) bool {
		if !candidates[i].when.Equal(candidates[j].when) {
			return candidates[i].when.After(candidates[j].when)
		}
		return candidates[i].id > candidates[j].id
	})
	recent := []map[string]any{}
	room := limit - active // places left for finished jobs once every active job is kept
	for _, c := range candidates {
		if !c.active {
			if room <= 0 {
				continue
			}
			room--
		}
		if status, ok := jobView(workspace, c.id); ok {
			recent = append(recent, status)
		}
	}
	return recent
}

func (app *Application) serveRunAPI(w http.ResponseWriter, r *http.Request) {
	if r.Method == "GET" {
		app.mu.RLock()
		workspace := app.config.Workspace
		app.mu.RUnlock()
		if r.URL.Path == "/api/runs/list" {
			jsonResponse(w, recentJobs(workspace, 30))
			return
		}
		id := r.URL.Query().Get("id")
		if !jobID.MatchString(id) {
			http.NotFound(w, r)
			return
		}
		status, ok := jobView(workspace, id)
		if !ok {
			if _, err := os.Stat(filepath.Join(workspace, "intake", id, "status.json")); err != nil {
				http.NotFound(w, r)
			} else {
				http.Error(w, "Run status is unreadable", 500)
			}
			return
		}
		jsonResponse(w, status)
		return
	}
	if r.Method != "POST" {
		http.Error(w, "Method not allowed", 405)
		return
	}
	if r.Header.Get("X-Issuer-Library") != "1" {
		http.Error(w, "Invalid application request", 403)
		return
	}
	if r.URL.Path == "/api/runs/review" {
		app.reviewRun(w, r)
		return
	}
	if r.URL.Path == "/api/runs/start" {
		app.startRun(w, r)
		return
	}
	http.NotFound(w, r)
}

// A folder-relative path as the browser reports it, refused unless it stays inside sources/.
func validSourcePath(name string) bool {
	return filepath.IsLocal(name) && path.Clean(name) == name && name != "." && !strings.ContainsAny(name, "\\\x00")
}

func (app *Application) reviewRun(w http.ResponseWriter, r *http.Request) {
	r.Body = http.MaxBytesReader(w, r.Body, 512<<20)
	if err := r.ParseMultipartForm(1 << 20); err != nil {
		http.Error(w, "Upload is too large or malformed (512 MiB total maximum)", 400)
		return
	}
	defer r.MultipartForm.RemoveAll()
	var paths []string
	if json.Unmarshal([]byte(r.FormValue("source_paths")), &paths) != nil {
		http.Error(w, "Source paths are invalid", 400)
		return
	}
	files := r.MultipartForm.File["sources"]
	if len(files) == 0 || len(files) > 500 || len(paths) != len(files) || len(r.FormValue("context")) > 1<<20 {
		http.Error(w, "Choose a folder of 1–500 files and complete the context", 400)
		return
	}
	for _, name := range paths {
		if !validSourcePath(name) {
			http.Error(w, "Source path is not inside the chosen folder: "+name, 400)
			return
		}
	}
	modules := strings.Fields(r.FormValue("modules"))
	for _, module := range modules {
		if !moduleCode.MatchString(module) {
			http.Error(w, "Modules are CP codes separated by spaces: "+module, 400)
			return
		}
	}
	maxTurns := 32 // The launcher's default.
	if value := r.FormValue("max_turns"); value != "" {
		var err error
		if maxTurns, err = strconv.Atoi(value); err != nil || maxTurns < 1 || maxTurns > 64 {
			http.Error(w, "Max turns must be between 1 and 64", 400)
			return
		}
	}
	nonce := make([]byte, 16)
	if _, err := rand.Read(nonce); err != nil {
		http.Error(w, "Could not create run identity", 500)
		return
	}
	// The review writes into this workspace until it ends, however it ends (refusal, error, the
	// review bound, a client that went away), so a workspace switch is refused until then.
	app.mu.Lock()
	if app.quitting {
		app.mu.Unlock()
		http.Error(w, libraryQuitting, 503)
		return
	}
	app.reviews++
	workspace := app.config.Workspace
	app.mu.Unlock()
	defer func() {
		app.mu.Lock()
		app.reviews--
		app.mu.Unlock()
	}()
	job := NewJob{ID: "web-" + hex.EncodeToString(nonce), Workspace: workspace, Config: r.FormValue("config"), Cap: r.FormValue("cap_usd"), Modules: modules, MaxTurns: maxTurns, Sources: []UploadedSource{}}
	root, err := os.OpenRoot(workspace)
	if err != nil {
		http.Error(w, "Choose an available workspace folder first", 400)
		return
	}
	defer root.Close()
	for _, name := range []string{"intake", "runs", "deliverables"} {
		if err = root.MkdirAll(name, 0700); err != nil {
			http.Error(w, "The workspace is not writable", 400)
			return
		}
	}
	relative := "intake/" + job.ID
	if err = root.MkdirAll(relative, 0700); err != nil {
		http.Error(w, "The workspace is not writable", 400)
		return
	}
	folder := filepath.Join(workspace, "intake", job.ID)
	valid := false
	defer func() {
		if !valid {
			_ = os.RemoveAll(folder)
		}
	}()
	contextFile, err := root.OpenFile(relative+"/context.json", os.O_WRONLY|os.O_CREATE|os.O_EXCL, 0600)
	if err != nil {
		http.Error(w, "Could not retain context", 500)
		return
	}
	_, writeErr := io.Copy(contextFile, strings.NewReader(r.FormValue("context")))
	closeErr := contextFile.Close()
	if writeErr != nil || closeErr != nil {
		http.Error(w, "Could not retain context", 500)
		return
	}
	// Every chosen file is kept, so the launcher itself reports the ones no module can read.
	for i, file := range files {
		if file.Size > maxFileBytes {
			http.Error(w, "Files must be up to 64 MiB each: "+paths[i], 400)
			return
		}
		target := relative + "/sources/" + paths[i]
		if err = root.MkdirAll(path.Dir(target), 0700); err != nil {
			http.Error(w, "Could not retain source", 500)
			return
		}
		destination, err := root.OpenFile(target, os.O_WRONLY|os.O_CREATE|os.O_EXCL, 0600)
		if err != nil {
			http.Error(w, "Could not retain source: "+paths[i], 400)
			return
		}
		stream, err := file.Open()
		if err != nil {
			destination.Close()
			http.Error(w, "Source upload could not be read", 400)
			return
		}
		// Streamed into the retained file and its hash together, never held whole in memory; a
		// refusal below leaves the partial file to the folder's removal.
		hash := sha256.New()
		size, err := io.Copy(io.MultiWriter(destination, hash), io.LimitReader(stream, maxFileBytes+1))
		stream.Close()
		closeErr := destination.Close()
		if err != nil || closeErr != nil {
			http.Error(w, "Could not retain source", 500)
			return
		}
		if size > maxFileBytes {
			http.Error(w, "Source upload is too large or unreadable: "+paths[i], 400)
			return
		}
		job.Sources = append(job.Sources, UploadedSource{Path: paths[i], SHA256: hex.EncodeToString(hash.Sum(nil))})
	}
	if err = saveJSON(filepath.Join(folder, "job.json"), job); err != nil {
		http.Error(w, "Could not save run request", 500)
		return
	}
	// The server's write deadline (set when the request headers were read) is far shorter than a
	// review may take, and the browser needs this response for the review_id. Give this one
	// response the review bound plus the usual write time; each request starts afresh, so no other
	// endpoint is affected.
	_ = http.NewResponseController(w).SetWriteDeadline(time.Now().Add(reviewTimeout + reviewWriteGrace))
	result, err := app.engine.review(folder)
	if err != nil {
		http.Error(w, err.Error(), 503)
		return
	}
	var review struct {
		OK bool `json:"ok"`
	}
	if json.Unmarshal(result, &review) != nil {
		http.Error(w, "Invalid validation response", 500)
		return
	}
	if review.OK {
		if err = saveJSON(filepath.Join(folder, "review.json"), result); err != nil {
			http.Error(w, "Could not retain review", 500)
			return
		}
		if err = saveJSON(filepath.Join(folder, "status.json"), JobStatus{State: "reviewed", Message: "Reviewed; no model call has been made.", ID: job.ID}); err != nil {
			http.Error(w, "Could not retain run status", 500)
			return
		}
		valid = true
	}
	w.Header().Set("Content-Type", "application/json")
	_, _ = w.Write(result)
}

func (app *Application) startRun(w http.ResponseWriter, r *http.Request) {
	var request struct {
		ID       string `json:"id"`
		ReviewID string `json:"review_id"`
		Confirm  bool   `json:"confirm"`
	}
	decoder := json.NewDecoder(http.MaxBytesReader(w, r.Body, 8192))
	decoder.DisallowUnknownFields()
	if err := decoder.Decode(&request); err != nil || !jobID.MatchString(request.ID) || !request.Confirm {
		http.Error(w, "Explicit confirmation of a reviewed run is required", 400)
		return
	}
	app.mu.Lock()
	defer app.mu.Unlock()
	if app.quitting {
		http.Error(w, libraryQuitting, 503)
		return
	}
	if len(app.activeJobs) > 0 {
		http.Error(w, "A CP-OS run is already active; wait for it to finish", 409)
		return
	}
	folder := filepath.Join(app.config.Workspace, "intake", request.ID)
	raw, err := os.ReadFile(filepath.Join(folder, "review.json"))
	if err != nil {
		http.Error(w, "Review this run before starting", 409)
		return
	}
	var review struct {
		ReviewID      string `json:"review_id"`
		ProviderReady bool   `json:"provider_ready"`
	}
	if json.Unmarshal(raw, &review) != nil || review.ReviewID != request.ReviewID || !review.ProviderReady {
		http.Error(w, "Review is invalid or the provider is not configured", 409)
		return
	}
	claim, err := os.OpenFile(filepath.Join(folder, "start.claim"), os.O_WRONLY|os.O_CREATE|os.O_EXCL, 0600)
	if err != nil {
		if !os.IsExist(err) {
			http.Error(w, "Could not retain the start authorisation", 500)
			return
		}
		http.Error(w, "This run has already been started; no additional call was made", 409)
		return
	}
	claim.Close()
	// The claim guards a worker that started. Until the process exists nothing was run or
	// paid for, so a failure before that releases it and the reviewed run can be started again.
	release := func() {
		if err := os.Remove(filepath.Join(folder, "start.claim")); err != nil && !os.IsNotExist(err) {
			log.Printf("Release start claim for %s: %v", request.ID, err)
		}
	}
	command := app.engine.command(context.Background(), "start", folder)
	// Discard command output; structured, redacted status is the only browser contract.
	command.Stdout = io.Discard
	// The worker inherits this lock and holds it while it runs, so a restarted app can tell a
	// live worker from a dead one; this copy is closed once the worker has started (or failed to).
	lock, err := holdWorkerLock(command, filepath.Join(folder, "worker.lock"))
	if err != nil {
		release()
		http.Error(w, "Could not prepare the run lock; no run was started and no model call was made. Start can be tried again.", 500)
		return
	}
	defer lock.Close()
	if err = saveJSON(filepath.Join(folder, "status.json"), JobStatus{State: "running", Message: "CP-OS is validating the reviewed inputs and starting the selected workflow.", ID: request.ID}); err != nil {
		release()
		http.Error(w, "Could not retain start state; no run was started and no model call was made. Start can be tried again.", 500)
		return
	}
	if err = command.Start(); err != nil {
		release()
		_ = saveJSON(filepath.Join(folder, "status.json"), JobStatus{State: "failed", Message: "CP-OS runtime could not start; no run was started and no model call was made. Start can be tried again.", ID: request.ID})
		http.Error(w, "CP-OS runtime could not start; no run was started and no model call was made. Start can be tried again.", 503)
		return
	}
	if app.activeJobs == nil {
		app.activeJobs = map[string]bool{}
	}
	app.activeJobs[request.ID] = true
	go func() {
		_ = command.Wait()
		app.finishJob(folder, request.ID)
	}()
	w.Header().Set("Content-Type", "application/json")
	w.WriteHeader(http.StatusAccepted)
	jsonResponse(w, JobStatus{State: "running", ID: request.ID, Message: "Run started."})
}

// workerPoll is how often a restarted app checks a worker it did not start; a variable so tests
// can shorten it.
var workerPoll = 5 * time.Second

// settleJob marks a job interrupted when its worker has ended while its status still says running.
func settleJob(folder string) {
	raw, _ := os.ReadFile(filepath.Join(folder, "status.json"))
	var status JobStatus
	if json.Unmarshal(raw, &status) == nil && status.State == "running" {
		_ = saveJSON(filepath.Join(folder, "status.json"), JobStatus{State: "interrupted", Message: "The worker exited without a final result. Retained evidence remains available; no automatic paid retry was made."})
	}
}

// finishJob settles a job whose worker has ended, ends its activity and refreshes the library.
func (app *Application) finishJob(folder, id string) {
	settleJob(folder)
	app.mu.Lock()
	delete(app.activeJobs, id)
	app.mu.Unlock()
	app.refresh()
}

// adoptJobsLocked settles the jobs an earlier instance of the app left running in workspace. A
// job whose worker still holds its lock is active again, so no second Start or workspace change
// is allowed, and is watched until the worker ends; a job whose lock is free, or absent because
// it was started before the lock existed, is interrupted. A lock that cannot be checked leaves
// its job as it is. The caller holds app.mu or owns app alone.
func (app *Application) adoptJobsLocked(workspace string) {
	entries, _ := os.ReadDir(filepath.Join(workspace, "intake"))
	for _, entry := range entries {
		id := entry.Name()
		folder := filepath.Join(workspace, "intake", id)
		if !jobID.MatchString(id) || app.activeJobs[id] {
			continue
		}
		var status JobStatus
		if raw, err := os.ReadFile(filepath.Join(folder, "status.json")); err != nil || json.Unmarshal(raw, &status) != nil || status.State != "running" {
			continue
		}
		alive, err := workerAlive(filepath.Join(folder, "worker.lock"))
		switch {
		case err != nil:
			log.Printf("Run %s: its worker lock cannot be checked; its state is left as it is: %v", id, err)
		case alive:
			if app.activeJobs == nil {
				app.activeJobs = map[string]bool{}
			}
			app.activeJobs[id] = true
			go app.watchWorker(folder, id)
		default:
			settleJob(folder)
		}
	}
}

// watchWorker waits for a worker this instance did not start to release its lock, then settles
// its job as for a worker it started.
func (app *Application) watchWorker(folder, id string) {
	for {
		time.Sleep(workerPoll)
		if alive, err := workerAlive(filepath.Join(folder, "worker.lock")); err == nil && !alive {
			break
		}
	}
	app.finishJob(folder, id)
}

// workspaceFingerprint names the inputs of one store run: the catalogue without its build time,
// and size and mtime (never contents) of every regular file under workspace/runs and
// workspace/deliverables, the only workspace trees store.py reads, plus store.py, catalog.json
// and the visualisation catalogue. A missing file is recorded as missing, not as an error.
// ponytail: one entry keyed on size and mtime; an edit that keeps both is missed until Refresh. Hash the files if that happens.
func workspaceFingerprint(workspace string, catalogue Catalogue, engineDir string) (string, error) {
	catalogue.BuiltAt = ""
	raw, err := json.Marshal(catalogue)
	if err != nil {
		return "", err
	}
	var lines []string
	describe := func(label, name string) error {
		info, err := os.Lstat(name)
		if errors.Is(err, fs.ErrNotExist) {
			lines = append(lines, label+"\tmissing")
			return nil
		}
		if err != nil {
			return err
		}
		lines = append(lines, fmt.Sprintf("%s\t%d\t%d", label, info.Size(), info.ModTime().UnixNano()))
		return nil
	}
	for _, tree := range []string{"runs", "deliverables"} {
		err = filepath.WalkDir(filepath.Join(workspace, tree), func(name string, entry fs.DirEntry, walkErr error) error {
			if walkErr != nil {
				if name == filepath.Join(workspace, tree) && errors.Is(walkErr, fs.ErrNotExist) {
					return nil
				}
				return walkErr
			}
			if !entry.Type().IsRegular() {
				return nil
			}
			relative, err := filepath.Rel(workspace, name)
			if err != nil {
				return err
			}
			return describe(filepath.ToSlash(relative), name)
		})
		if err != nil {
			return "", err
		}
	}
	engineFiles := map[string]string{
		"engine/store.py":     filepath.Join(engineDir, "store.py"),
		"engine/catalog.json": filepath.Join(engineDir, "catalog.json"),
	}
	// store.py's REPO: the engine folder itself when packaged (it has src), else the checkout root.
	repo := filepath.Join(engineDir, "..", "..", "..")
	if info, statErr := os.Stat(filepath.Join(engineDir, "src")); statErr == nil && info.IsDir() {
		repo = engineDir
	}
	engineFiles["docs/visualisations/catalogue.csv"] = filepath.Join(repo, "docs", "visualisations", "catalogue.csv")
	for label, name := range engineFiles {
		if err = describe(label, name); err != nil {
			return "", err
		}
	}
	sort.Strings(lines)
	hash := sha256.New()
	hash.Write(raw)
	hash.Write([]byte("\n" + strings.Join(lines, "\n")))
	return hex.EncodeToString(hash.Sum(nil)), nil
}
