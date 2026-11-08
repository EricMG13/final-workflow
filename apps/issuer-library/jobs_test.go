package main

import (
	"bytes"
	"context"
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"io"
	"mime/multipart"
	"net/http"
	"net/http/httptest"
	"net/http/httptrace"
	"os"
	"os/exec"
	"path/filepath"
	"reflect"
	"runtime"
	"slices"
	"strconv"
	"strings"
	"sync"
	"testing"
	"time"
)

func fakeEngine(t *testing.T) Engine {
	t.Helper()
	python, err := exec.LookPath("python3")
	if err != nil {
		t.Skip("Python needed for the synthetic process-boundary test")
	}
	script := filepath.Join(t.TempDir(), "worker.py")
	raw := `import json,sys,pathlib,time
folder=pathlib.Path(sys.argv[2])
job=json.loads((folder/'job.json').read_text())
if sys.argv[1]=='review':
 print(json.dumps({'ok':True,'review_id':'review-fingerprint','id':job['id'],'provider_ready':True,'cap_usd':job['cap_usd']}))
else:
 with (folder/'synthetic-starts.txt').open('a') as stream: stream.write('one\n')
 while (folder/'hold').exists(): time.sleep(.02)
 time.sleep(.15)
 (folder/'status.json').write_text(json.dumps({'state':'stopped','message':'Synthetic worker seam only; no provider called.'}))
`
	if err = os.WriteFile(script, []byte(raw), 0600); err != nil {
		t.Fatal(err)
	}
	library := `import json,sys
print(json.dumps({'parsed':json.load(sys.stdin)['workspace'],'folder':sys.argv[1]}))
`
	if err = os.WriteFile(filepath.Join(filepath.Dir(script), "store.py"), []byte(library), 0600); err != nil {
		t.Fatal(err)
	}
	return Engine{Python: python, Script: script}
}
func reviewRequest(t *testing.T, app *Application, paths string) *httptest.ResponseRecorder {
	t.Helper()
	return reviewRequestTurns(t, app, paths, "7")
}
func reviewRequestTurns(t *testing.T, app *Application, paths, turns string) *httptest.ResponseRecorder {
	t.Helper()
	var body bytes.Buffer
	form := multipart.NewWriter(&body)
	for key, value := range map[string]string{"context": "{}", "config": "sol-medium", "cap_usd": "10.00", "source_paths": paths, "modules": "CP-4", "max_turns": turns} {
		if err := form.WriteField(key, value); err != nil {
			t.Fatal(err)
		}
	}
	file, err := form.CreateFormFile("sources", "../../original.txt")
	if err != nil {
		t.Fatal(err)
	}
	_, _ = file.Write([]byte("Synthetic source"))
	form.Close()
	request := withSession(app, httptest.NewRequest("POST", "http://"+app.host+"/api/runs/review", &body))
	request.Header.Set("Content-Type", form.FormDataContentType())
	request.Header.Set("X-Issuer-Library", "1")
	request.Header.Set("Origin", "http://"+app.host)
	response := httptest.NewRecorder()
	app.ServeHTTP(response, request)
	return response
}
func TestUploadReviewDoesNotStartAndRetainsTheFolderLayout(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	response := reviewRequest(t, app, `["filings/annual.txt"]`)
	if response.Code != 200 {
		t.Fatal(response.Body.String())
	}
	var value struct {
		ID string `json:"id"`
	}
	if err := json.Unmarshal(response.Body.Bytes(), &value); err != nil {
		t.Fatal(err)
	}
	folder := filepath.Join(root, "intake", value.ID)
	if raw, err := os.ReadFile(filepath.Join(folder, "sources", "filings", "annual.txt")); err != nil || string(raw) != "Synthetic source" {
		t.Fatal("source was not kept at its folder path", err)
	}
	var job NewJob
	raw, err := os.ReadFile(filepath.Join(folder, "job.json"))
	if err != nil || json.Unmarshal(raw, &job) != nil {
		t.Fatal(err)
	}
	if !slices.Equal(job.Modules, []string{"CP-4"}) || job.MaxTurns != 7 || job.Config != "sol-medium" || job.Sources[0].Path != "filings/annual.txt" {
		t.Fatalf("request was not retained: %+v", job)
	}
	if _, err := os.Stat(filepath.Join(folder, "synthetic-starts.txt")); !os.IsNotExist(err) {
		t.Fatal("review executed")
	}
	if _, err := os.Stat(filepath.Join(root, "original.txt")); !os.IsNotExist(err) {
		t.Fatal("upload filename escaped staging")
	}
}
func TestUploadRefusesPathsOutsideTheChosenFolder(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	for _, name := range []string{`["../../original.txt"]`, `["/etc/original.txt"]`, `["a/../../original.txt"]`, `["a/./b.txt"]`, `["a\\\\b.txt"]`, `["."]`, `[""]`, `["a","b"]`, `not json`} {
		if response := reviewRequest(t, app, name); response.Code != 400 {
			t.Fatalf("%s accepted: %d %s", name, response.Code, response.Body.String())
		}
	}
	if _, err := os.Stat(filepath.Join(root, "original.txt")); !os.IsNotExist(err) {
		t.Fatal("upload escaped staging")
	}
	if entries, _ := os.ReadDir(filepath.Join(root, "intake")); len(entries) != 0 {
		t.Fatalf("refused uploads left %d intake folders", len(entries))
	}
}
func TestWorkspaceStoreComesFromTheEngineWithTheCatalogue(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	response := call(app, "GET", "/api/workspace", "")
	var value map[string]string
	if response.Code != 200 || json.Unmarshal(response.Body.Bytes(), &value) != nil {
		t.Fatal(response.Code, response.Body.String())
	}
	if value["parsed"] != root || value["folder"] == "" {
		t.Fatalf("engine did not receive this workspace's catalogue: %v", value)
	}
	app.engine = Engine{Python: filepath.Join(root, "missing-python"), Script: "x"}
	response = call(app, "GET", "/api/workspace", "")
	if response.Code != 503 || !strings.Contains(response.Body.String(), "runtime is unavailable") {
		t.Fatalf("missing runtime hidden: %d %s", response.Code, response.Body.String())
	}
}
func TestExplicitStartIsOneShotUnderConcurrentRequests(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	response := reviewRequest(t, app, `["annual.txt"]`)
	var review map[string]any
	_ = json.Unmarshal(response.Body.Bytes(), &review)
	id := review["id"].(string)
	invalid := call(app, "POST", "/api/runs/start", `{"id":"`+id+`","review_id":"review-fingerprint","confirm":false}`)
	if invalid.Code != 400 {
		t.Fatal("implicit start accepted")
	}
	payload := `{"id":"` + id + `","review_id":"review-fingerprint","confirm":true}`
	var group sync.WaitGroup
	results := make(chan int, 2)
	for range 2 {
		group.Go(func() { results <- call(app, "POST", "/api/runs/start", payload).Code })
	}
	group.Wait()
	close(results)
	accepted := 0
	for code := range results {
		if code == 202 {
			accepted++
		} else if code != 409 {
			t.Fatalf("unexpected %d", code)
		}
	}
	if accepted != 1 {
		t.Fatalf("%d starts accepted", accepted)
	}
	deadline := time.Now().Add(5 * time.Second)
	for time.Now().Before(deadline) {
		app.mu.RLock()
		active := len(app.activeJobs)
		app.mu.RUnlock()
		if active == 0 {
			break
		}
		time.Sleep(20 * time.Millisecond)
	}
	raw, err := os.ReadFile(filepath.Join(root, "intake", id, "synthetic-starts.txt"))
	if err != nil {
		t.Fatal(err)
	}
	if string(raw) != "one\n" {
		t.Fatalf("duplicate execution: %q", raw)
	}
	status := call(app, "GET", "/api/runs/status?id="+id, "")
	if status.Code != 200 {
		t.Fatal(status.Code)
	}
}
func TestSourceUploadsRequireOriginAndCustomHeader(t *testing.T) {
	app, _ := testApp(t)
	request := withSession(app, httptest.NewRequest("POST", "http://"+app.host+"/api/runs/review", bytes.NewBufferString("anything")))
	request.Header.Set("Origin", "https://untrusted.invalid")
	response := httptest.NewRecorder()
	app.ServeHTTP(response, request)
	if response.Code != 403 {
		t.Fatal("cross-origin upload accepted")
	}
	request = withSession(app, httptest.NewRequest("POST", "http://"+app.host+"/api/runs/review", nil))
	response = httptest.NewRecorder()
	app.ServeHTTP(response, request)
	if response.Code != 403 {
		t.Fatal("implicit app request accepted")
	}
}

func TestStartRefusesUnconfiguredProviderBeforeCreatingClaim(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	response := reviewRequest(t, app, `["annual.txt"]`)
	var review map[string]any
	_ = json.Unmarshal(response.Body.Bytes(), &review)
	id := review["id"].(string)
	review["provider_ready"] = false
	folder := filepath.Join(root, "intake", id)
	if err := saveJSON(filepath.Join(folder, "review.json"), review); err != nil {
		t.Fatal(err)
	}
	response = call(app, "POST", "/api/runs/start", `{"id":"`+id+`","review_id":"review-fingerprint","confirm":true}`)
	if response.Code != 409 {
		t.Fatal("unconfigured execution accepted")
	}
	if _, err := os.Stat(filepath.Join(folder, "start.claim")); !os.IsNotExist(err) {
		t.Fatal("unconfigured run consumed its one-shot claim")
	}
}

func TestCorruptedReviewIsRefusedBeforeStarting(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	response := reviewRequest(t, app, `["annual.txt"]`)
	var value map[string]any
	_ = json.Unmarshal(response.Body.Bytes(), &value)
	id := value["id"].(string)
	file := filepath.Join(root, "intake", id, "review.json")
	raw, err := os.ReadFile(file)
	if err != nil {
		t.Fatal(err)
	}
	if err = os.WriteFile(file, append(raw, []byte("{}")...), 0600); err != nil {
		t.Fatal(err)
	}
	response = call(app, "POST", "/api/runs/start", `{"id":"`+id+`","review_id":"review-fingerprint","confirm":true}`)
	if response.Code != 409 {
		t.Fatal("corrupted review started a worker")
	}
}

func TestWorkerUsesUTF8IndependentOfWindowsLocale(t *testing.T) {
	command := fakeEngine(t).command(context.Background(), "review", t.TempDir())
	if !slices.Contains(command.Args, "-X") || !slices.Contains(command.Args, "utf8") {
		t.Fatal("Windows workers must use UTF-8 for retained JSON and Markdown")
	}
}

func TestStatusOnlyOffersAnExistingRun(t *testing.T) {
	app, root := testApp(t)
	id := "web-aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
	folder := filepath.Join(root, "intake", id)
	if err := os.MkdirAll(folder, 0700); err != nil {
		t.Fatal(err)
	}
	if err := saveJSON(filepath.Join(folder, "status.json"), JobStatus{State: "failed"}); err != nil {
		t.Fatal(err)
	}
	status := func() bool {
		response := call(app, "GET", "/api/runs/status?id="+id, "")
		var result struct {
			Available bool `json:"run_available"`
		}
		if response.Code != 200 || json.Unmarshal(response.Body.Bytes(), &result) != nil {
			t.Fatal(response.Body.String())
		}
		return result.Available
	}
	if status() {
		t.Fatal("failed validation offered a nonexistent run")
	}
	if err := os.MkdirAll(filepath.Join(root, "runs", id), 0700); err != nil {
		t.Fatal(err)
	}
	if !status() {
		t.Fatal("retained run is unavailable")
	}
}

func TestReviewPreparesAnEmptyWorkspaceWithoutExecuting(t *testing.T) {
	root := t.TempDir()
	app, err := newApplication(Locations{State: t.TempDir(), Documents: t.TempDir()}, root)
	if err != nil {
		t.Fatal(err)
	}
	app.host = "127.0.0.1:54321"
	app.engine = fakeEngine(t)
	response := reviewRequest(t, app, `["annual.txt"]`)
	if response.Code != 200 {
		t.Fatal(response.Body.String())
	}
	for _, name := range []string{"runs", "deliverables"} {
		entries, err := os.ReadDir(filepath.Join(root, name))
		if err != nil || len(entries) != 0 {
			t.Fatalf("fresh workspace %s was not prepared without execution: %v", name, err)
		}
	}
}

func TestSaveJSONWaitsForAFileHeldOpen(t *testing.T) {
	name := filepath.Join(t.TempDir(), "status.json")
	// A folder in the way fails the rename until it goes, as a held file does on Windows.
	if err := os.Mkdir(name, 0700); err != nil {
		t.Fatal(err)
	}
	go func() {
		time.Sleep(150 * time.Millisecond)
		_ = os.Remove(name)
	}()
	if err := saveJSON(name, map[string]string{"state": "interrupted"}); err != nil {
		t.Fatal(err)
	}
	raw, err := os.ReadFile(name)
	if err != nil || !strings.Contains(string(raw), "interrupted") {
		t.Fatalf("%s %v", raw, err)
	}
}

// slowReviewEngine returns an Engine whose review sleeps for the given seconds.
func slowReviewEngine(t *testing.T, seconds string) Engine {
	t.Helper()
	python, err := exec.LookPath("python3")
	if err != nil {
		t.Skip("Python needed for the synthetic process-boundary test")
	}
	script := filepath.Join(t.TempDir(), "worker.py")
	raw := `import json,sys,pathlib,time
folder=pathlib.Path(sys.argv[2])
job=json.loads((folder/'job.json').read_text())
if sys.argv[1]=='review':
 time.sleep(` + seconds + `)
 print(json.dumps({'ok':True,'review_id':'rid','id':job['id'],'provider_ready':True}))
`
	if err = os.WriteFile(script, []byte(raw), 0600); err != nil {
		t.Fatal(err)
	}
	return Engine{Python: python, Script: script}
}

// slowServer serves the app with the production timeouts scaled down so that a review outlasts
// WriteTimeout and ReadTimeout but not the review bound.
func slowServer(t *testing.T, app *Application) *httptest.Server {
	t.Helper()
	server := httptest.NewUnstartedServer(app)
	server.Config.ReadTimeout = time.Second
	server.Config.WriteTimeout = time.Second
	server.Start()
	t.Cleanup(server.Close)
	app.host = strings.TrimPrefix(server.URL, "http://")
	return server
}

func postReview(t *testing.T, server *httptest.Server) (*http.Response, error) {
	t.Helper()
	return postReviewWith(t, server, context.Background(), http.DefaultClient)
}

func postReviewWith(t *testing.T, server *httptest.Server, ctx context.Context, client *http.Client) (*http.Response, error) {
	t.Helper()
	var body bytes.Buffer
	form := multipart.NewWriter(&body)
	for key, value := range map[string]string{"context": "{}", "config": "c", "cap_usd": "1", "source_paths": `["a.txt"]`, "modules": "CP-4"} {
		_ = form.WriteField(key, value)
	}
	file, _ := form.CreateFormFile("sources", "a.txt")
	_, _ = file.Write([]byte("x"))
	form.Close()
	request, _ := http.NewRequestWithContext(ctx, "POST", server.URL+"/api/runs/review", &body)
	withSession(server.Config.Handler.(*Application), request)
	request.Header.Set("Content-Type", form.FormDataContentType())
	request.Header.Set("X-Issuer-Library", "1")
	request.Header.Set("Origin", server.URL)
	return client.Do(request)
}

// A review that outlasts the server's write timeout must still deliver its review_id; two
// reviews at once each keep their own deadline.
func TestSlowReviewResponseOutlivesTheServerWriteTimeout(t *testing.T) {
	app, _ := testApp(t)
	app.engine = slowReviewEngine(t, "2.5")
	server := slowServer(t, app)
	type outcome struct {
		body string
		err  error
	}
	results := make(chan outcome, 2)
	for range 2 {
		go func() {
			response, err := postReview(t, server)
			if err != nil {
				results <- outcome{err: err}
				return
			}
			raw, _ := io.ReadAll(response.Body)
			response.Body.Close()
			results <- outcome{body: response.Status + " " + string(raw)}
		}()
	}
	ids := map[string]bool{}
	for range 2 {
		result := <-results
		if result.err != nil {
			t.Fatalf("response lost: %v", result.err)
		}
		var review struct {
			ID       string `json:"id"`
			ReviewID string `json:"review_id"`
		}
		_ = json.Unmarshal([]byte(strings.TrimPrefix(result.body, "200 OK ")), &review)
		if !strings.HasPrefix(result.body, "200 OK") || review.ID == "" || review.ReviewID != "rid" {
			t.Fatalf("unexpected response: %s", result.body)
		}
		ids[review.ID] = true
	}
	if len(ids) != 2 {
		t.Fatalf("reviews shared an id: %v", ids)
	}
}

// The review bound still applies: a review past it fails with an error the client receives, and
// leaves no intake folder behind.
func TestReviewPastTheBoundIsReportedNotDropped(t *testing.T) {
	shortReviewTimeout(t, time.Second)
	app, root := testApp(t)
	app.engine = slowReviewEngine(t, "30")
	server := slowServer(t, app)
	started := time.Now()
	response, err := postReview(t, server)
	if err != nil {
		t.Fatalf("error response lost: %v", err)
	}
	response.Body.Close()
	if response.StatusCode != 503 || time.Since(started) > 10*time.Second {
		t.Fatalf("status %d after %v", response.StatusCode, time.Since(started))
	}
	entries, _ := os.ReadDir(filepath.Join(root, "intake"))
	if len(entries) != 0 {
		t.Fatalf("intake folder left behind: %v", entries)
	}
}

// shortReviewTimeout sets the review bound for one test. It is restored by a cleanup registered
// before the test server's, so it runs after server.Close has waited for every handler.
func shortReviewTimeout(t *testing.T, bound time.Duration) {
	saved := reviewTimeout
	reviewTimeout = bound
	t.Cleanup(func() { reviewTimeout = saved })
}

// Adversarial: with the server's write deadline at 1 s and the review bound at 2 s, a review just
// under the bound (1.4 s) must answer 200 with its review_id, and one just over it (sleeping 4 s)
// must answer 503 at the bound, not at the sleep, and leave no intake folder or start claim.
func TestReviewJustUnderAndJustOverTheBound(t *testing.T) {
	shortReviewTimeout(t, 2*time.Second)
	for _, c := range []struct {
		sleep  string
		status int
	}{{"1.4", 200}, {"4", 503}} {
		app, root := testApp(t)
		app.engine = slowReviewEngine(t, c.sleep)
		server := slowServer(t, app)
		started := time.Now()
		response, err := postReview(t, server)
		if err != nil {
			t.Fatalf("sleep %s: response lost: %v", c.sleep, err)
		}
		raw, _ := io.ReadAll(response.Body)
		response.Body.Close()
		elapsed := time.Since(started)
		if response.StatusCode != c.status {
			t.Fatalf("sleep %s: status %d %s", c.sleep, response.StatusCode, raw)
		}
		server.Close()
		entries, _ := os.ReadDir(filepath.Join(root, "intake"))
		if c.status == 200 {
			var review struct {
				ReviewID string `json:"review_id"`
			}
			if json.Unmarshal(raw, &review) != nil || review.ReviewID != "rid" || len(entries) != 1 {
				t.Fatalf("sleep %s: body %s, intake %v", c.sleep, raw, entries)
			}
			continue
		}
		if elapsed > 3500*time.Millisecond || len(entries) != 0 {
			t.Fatalf("sleep %s: 503 after %v; intake %v", c.sleep, elapsed, entries)
		}
	}
}

// Adversarial: the client gives up 300 ms into a 1.5 s review. Expected: the client sees its own
// cancellation; the handler is not stuck (server.Close returns, which waits for handlers); the
// server keeps serving the next review. The review is not tied to the request, so it completes and
// its draft stays in intake as "reviewed" (unchanged by the S18 fix; recorded, not endorsed).
func TestClientDisconnectMidReview(t *testing.T) {
	app, root := testApp(t)
	app.engine = slowReviewEngine(t, "1.5")
	server := slowServer(t, app)
	ctx, cancel := context.WithTimeout(context.Background(), 300*time.Millisecond)
	defer cancel()
	if response, err := postReviewWith(t, server, ctx, http.DefaultClient); err == nil {
		response.Body.Close()
		t.Fatalf("client received %s despite giving up", response.Status)
	}
	response, err := postReview(t, server)
	if err != nil || response.StatusCode != 200 {
		t.Fatalf("server stopped serving after a disconnect: %v", err)
	}
	response.Body.Close()
	closed := make(chan struct{})
	go func() { server.Close(); close(closed) }()
	select {
	case <-closed:
	case <-time.After(10 * time.Second):
		t.Fatal("a handler is still running after the review bound")
	}
	entries, _ := os.ReadDir(filepath.Join(root, "intake"))
	if len(entries) != 2 {
		t.Fatalf("expected the abandoned draft and the completed one, got %v", entries)
	}
}

// Adversarial: the extended deadline belongs to one response only. On one keep-alive connection, a
// slow review (1.5 s) answers past the 1 s WriteTimeout, then a slow /api/workspace (1.5 s) on the
// same connection must still be cut at WriteTimeout (client error, no 200). ReadTimeout is longer
// here only so the server keeps the connection open for reuse. The transport retries an idempotent
// GET that fails on a reused connection, on a fresh one, which is cut in the same way.
func TestOtherEndpointsKeepTheServerWriteTimeout(t *testing.T) {
	app, _ := testApp(t)
	app.engine = slowReviewEngine(t, "1.5")
	// The first call answers at once (control); later calls take 1.5 s.
	// Each run appends a byte under runs/, as a live run would, so the next read is a cache miss
	// and runs the store again (a retry after the cut would otherwise be served the cached output).
	store := `import sys,time,pathlib
sys.stdin.read()
mark=pathlib.Path(__file__).with_name('called')
if mark.exists(): time.sleep(1.5)
mark.write_text('1')
with (pathlib.Path(sys.argv[1])/'runs'/'case-a'/'timeout-probe.md').open('a') as stream: stream.write('x')
print('{}')
`
	if err := os.WriteFile(filepath.Join(filepath.Dir(app.engine.Script), "store.py"), []byte(store), 0600); err != nil {
		t.Fatal(err)
	}
	server := httptest.NewUnstartedServer(app)
	server.Config.ReadTimeout = 10 * time.Second
	server.Config.WriteTimeout = time.Second
	server.Start()
	t.Cleanup(server.Close)
	app.host = strings.TrimPrefix(server.URL, "http://")
	client := &http.Client{Transport: &http.Transport{MaxConnsPerHost: 1, Proxy: nil}}
	defer client.CloseIdleConnections()
	control, _ := http.NewRequest("GET", server.URL+"/api/workspace", nil)
	response, err := client.Do(withSession(app, control))
	if err != nil || response.StatusCode != 200 {
		t.Fatalf("control /api/workspace failed: %v", err)
	}
	response.Body.Close()
	response, err = postReviewWith(t, server, context.Background(), client)
	if err != nil || response.StatusCode != 200 {
		t.Fatalf("slow review lost: %v", err)
	}
	_, _ = io.Copy(io.Discard, response.Body)
	response.Body.Close()
	reused := false
	trace := &httptrace.ClientTrace{GotConn: func(info httptrace.GotConnInfo) { reused = reused || info.Reused }}
	request, _ := http.NewRequestWithContext(httptrace.WithClientTrace(context.Background(), trace), "GET", server.URL+"/api/workspace", nil)
	response, err = client.Do(withSession(app, request))
	if !reused {
		t.Fatal("the request was never tried on the review's connection")
	}
	if err == nil {
		raw, _ := io.ReadAll(response.Body)
		response.Body.Close()
		t.Fatalf("slow /api/workspace outlived WriteTimeout: %s %s", response.Status, raw)
	}
}

func writeJob(t *testing.T, root, id, state string, when time.Time) {
	t.Helper()
	folder := filepath.Join(root, "intake", id)
	if err := os.MkdirAll(folder, 0700); err != nil {
		t.Fatal(err)
	}
	file := filepath.Join(folder, "status.json")
	if err := os.WriteFile(file, []byte(`{"state":"`+state+`"}`), 0600); err != nil {
		t.Fatal(err)
	}
	if err := os.Chtimes(file, when, when); err != nil {
		t.Fatal(err)
	}
}

func listedJobs(t *testing.T, app *Application) []string {
	t.Helper()
	var rows []map[string]any
	response := call(app, "GET", "/api/runs/list", "")
	if err := json.Unmarshal(response.Body.Bytes(), &rows); err != nil {
		t.Fatal(err)
	}
	ids := []string{}
	for _, row := range rows {
		ids = append(ids, row["id"].(string))
	}
	return ids
}

// Job ids are random, so which jobs are "recent" must follow when they were written, and
// a running job must never be cut by the cap however old its status file is.
func TestRunListFollowsRecencyAndAlwaysKeepsActiveJobs(t *testing.T) {
	app, root := testApp(t)
	now := time.Now()
	// Ids sort opposite to age: the newest jobs have the smallest ids.
	for i := 0; i < 40; i++ {
		writeJob(t, root, fmt.Sprintf("web-%032x", 0x100+i), "complete", now.Add(-time.Duration(i+1)*time.Hour))
	}
	newest := "web-" + strings.Repeat("0", 31) + "1"
	writeJob(t, root, newest, "running", now)
	oldRunning := "web-" + strings.Repeat("f", 32)
	writeJob(t, root, oldRunning, "running", now.Add(-500*time.Hour))
	writeJob(t, root, "web-"+strings.Repeat("a", 32), "reviewed", now)
	ids := listedJobs(t, app)
	if len(ids) != 30 {
		t.Fatalf("%d rows, want the 30 cap: %v", len(ids), ids)
	}
	if ids[0] != newest {
		t.Fatalf("the just-started job must lead the list: %v", ids)
	}
	has := map[string]bool{}
	for _, id := range ids {
		has[id] = true
	}
	if !has[oldRunning] {
		t.Fatal("a running job must be listed even when its status file is old")
	}
	if has["web-"+strings.Repeat("a", 32)] {
		t.Fatal("a reviewed-only draft is not a run")
	}
	// 28 finished jobs fill the remaining places: the 28 newest by write time.
	for i := 0; i < 28; i++ {
		if want := fmt.Sprintf("web-%032x", 0x100+i); !has[want] {
			t.Fatalf("finished job %d (newer than the cut) missing: %v", i, ids)
		}
	}
	if has[fmt.Sprintf("web-%032x", 0x100+28)] {
		t.Fatal("an older finished job displaced a newer one")
	}
}

func waitIdle(t *testing.T, app *Application) {
	t.Helper()
	deadline := time.Now().Add(5 * time.Second)
	for time.Now().Before(deadline) {
		app.mu.RLock()
		active := len(app.activeJobs)
		app.mu.RUnlock()
		if active == 0 {
			return
		}
		time.Sleep(20 * time.Millisecond)
	}
	t.Fatal("worker did not finish")
}

// A spawn that never produced a process made no call, so the one-shot claim is released;
// once a worker did start the claim keeps refusing a second Start.
func TestFailedSpawnReleasesTheStartClaimButAStartedWorkerKeepsIt(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	response := reviewRequest(t, app, `["annual.txt"]`)
	var review map[string]any
	_ = json.Unmarshal(response.Body.Bytes(), &review)
	id := review["id"].(string)
	folder := filepath.Join(root, "intake", id)
	payload := `{"id":"` + id + `","review_id":"review-fingerprint","confirm":true}`
	good := app.engine
	app.engine = Engine{Python: filepath.Join(t.TempDir(), "no-such-python"), Script: good.Script}
	first := call(app, "POST", "/api/runs/start", payload)
	if first.Code != 503 || !strings.Contains(first.Body.String(), "no model call was made") {
		t.Fatalf("spawn failure: %d %q", first.Code, first.Body.String())
	}
	if _, err := os.Stat(filepath.Join(folder, "start.claim")); !os.IsNotExist(err) {
		t.Fatalf("claim survived a spawn that never ran: %v", err)
	}
	status := call(app, "GET", "/api/runs/status?id="+id, "")
	if !strings.Contains(status.Body.String(), `"state":"failed"`) || !strings.Contains(status.Body.String(), "can be tried again") {
		t.Fatalf("status: %s", status.Body.String())
	}
	app.engine = good
	second := call(app, "POST", "/api/runs/start", payload)
	if second.Code != 202 {
		t.Fatalf("retry after a failed spawn: %d %q", second.Code, second.Body.String())
	}
	third := call(app, "POST", "/api/runs/start", payload)
	if third.Code != 409 {
		t.Fatalf("a second Start while the worker runs: %d %q", third.Code, third.Body.String())
	}
	waitIdle(t, app)
	if raw, _ := os.ReadFile(filepath.Join(folder, "synthetic-starts.txt")); string(raw) != "one\n" {
		t.Fatalf("worker ran %q", raw)
	}
	if again := call(app, "POST", "/api/runs/start", payload); again.Code != 409 || !strings.Contains(again.Body.String(), "already been started") {
		t.Fatalf("a finished worker must keep the claim: %d %q", again.Code, again.Body.String())
	}
}

// If the running status cannot be saved the worker is never spawned, so the claim is released too.
func TestUnsavableStartStatusReleasesTheStartClaim(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	response := reviewRequest(t, app, `["annual.txt"]`)
	var review map[string]any
	_ = json.Unmarshal(response.Body.Bytes(), &review)
	id := review["id"].(string)
	folder := filepath.Join(root, "intake", id)
	status := filepath.Join(folder, "status.json")
	if err := os.Remove(status); err != nil {
		t.Fatal(err)
	}
	if err := os.MkdirAll(filepath.Join(status, "blocker"), 0700); err != nil {
		t.Fatal(err)
	}
	payload := `{"id":"` + id + `","review_id":"review-fingerprint","confirm":true}`
	first := call(app, "POST", "/api/runs/start", payload)
	if first.Code != 500 {
		t.Fatalf("expected the status write to fail: %d %q", first.Code, first.Body.String())
	}
	if _, err := os.Stat(filepath.Join(folder, "synthetic-starts.txt")); err == nil {
		t.Fatal("a worker ran")
	}
	if _, err := os.Stat(filepath.Join(folder, "start.claim")); !os.IsNotExist(err) {
		t.Fatalf("claim survived: %v", err)
	}
	if err := os.RemoveAll(status); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(status, []byte(`{"state":"reviewed"}`), 0600); err != nil {
		t.Fatal(err)
	}
	if second := call(app, "POST", "/api/runs/start", payload); second.Code != 202 {
		t.Fatalf("retry: %d %q", second.Code, second.Body.String())
	}
	waitIdle(t, app)
}

// Review (S18 medium, A04/C05): after a crash, more stale "running" jobs than the
// cap. Expected: every active job is listed (40 rows, above the cap of 30), newest first,
// and no finished job takes a place because no room is left.
func TestReviewRunListManyStaleActiveJobsExceedTheCap(t *testing.T) {
	app, root := testApp(t)
	now := time.Now()
	for i := 0; i < 35; i++ {
		writeJob(t, root, fmt.Sprintf("web-%032x", 0x200+i), "running", now.Add(-time.Duration(100+i)*time.Hour))
	}
	for i := 0; i < 5; i++ {
		writeJob(t, root, fmt.Sprintf("web-%032x", 0x300+i), "running", now.Add(-time.Duration(200+i)*time.Hour))
	}
	for i := 0; i < 10; i++ {
		writeJob(t, root, fmt.Sprintf("web-%032x", 0x400+i), "complete", now.Add(-time.Duration(i)*time.Minute))
	}
	ids := listedJobs(t, app)
	if len(ids) != 40 {
		t.Fatalf("%d rows, want all 40 active jobs: %v", len(ids), ids)
	}
	for i, id := range ids {
		var want string
		if i < 35 {
			want = fmt.Sprintf("web-%032x", 0x200+i)
		} else {
			want = fmt.Sprintf("web-%032x", 0x300+i-35)
		}
		if id != want {
			t.Fatalf("row %d is %s, want %s (newest first)", i, id, want)
		}
	}
}

// Review (S18 medium, A04/C05): equal write times and unreadable status files. Expected:
// exactly 30 rows; with equal times the order falls back to the id, descending, and is the
// same on every request; a status.json that is a folder, invalid JSON or empty, a plain file
// named like a job, and a folder that is not a job id are all left out without failing.
func TestReviewRunListEqualTimesAndUnreadableStatus(t *testing.T) {
	app, root := testApp(t)
	when := time.Date(2026, 11, 6, 12, 0, 0, 0, time.UTC)
	for i := 0; i < 33; i++ {
		writeJob(t, root, fmt.Sprintf("web-%032x", 0x500+i), "complete", when)
	}
	bad := map[string]string{"web-" + strings.Repeat("e", 32): "{not json", "web-" + strings.Repeat("d", 32): ""}
	for id, raw := range bad {
		put(t, root, "intake/"+id+"/status.json", []byte(raw))
	}
	put(t, root, "intake/web-"+strings.Repeat("c", 32)+"/status.json/inner", []byte(`{"state":"running"}`))
	put(t, root, "intake/web-"+strings.Repeat("b", 32), []byte(`{"state":"running"}`))
	put(t, root, "intake/notes/status.json", []byte(`{"state":"running"}`))
	first, second := listedJobs(t, app), listedJobs(t, app)
	if len(first) != 30 || !slices.Equal(first, second) {
		t.Fatalf("%d rows, stable=%v: %v", len(first), slices.Equal(first, second), first)
	}
	for i, id := range first {
		if want := fmt.Sprintf("web-%032x", 0x500+32-i); id != want {
			t.Fatalf("row %d is %s, want %s", i, id, want)
		}
	}
}

// Review (S18 medium, A08/C02): concurrent Starts around a failed spawn. Expected: while the
// runtime is missing every request fails with 503 (each claims, fails and releases; none is
// accepted and no claim is left); after repair, of 8 concurrent Starts exactly one is accepted,
// the others get 409, and the worker runs exactly once.
func TestReviewConcurrentStartsAroundAFailedSpawn(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	response := reviewRequest(t, app, `["annual.txt"]`)
	var review map[string]any
	_ = json.Unmarshal(response.Body.Bytes(), &review)
	id := review["id"].(string)
	folder := filepath.Join(root, "intake", id)
	payload := `{"id":"` + id + `","review_id":"review-fingerprint","confirm":true}`
	good := app.engine
	app.engine = Engine{Python: filepath.Join(t.TempDir(), "no-such-python"), Script: good.Script}
	codes := func() map[int]int {
		var group sync.WaitGroup
		var lock sync.Mutex
		seen := map[int]int{}
		for range 8 {
			group.Go(func() {
				code := call(app, "POST", "/api/runs/start", payload).Code
				lock.Lock()
				seen[code]++
				lock.Unlock()
			})
		}
		group.Wait()
		return seen
	}
	if seen := codes(); seen[503] != 8 {
		t.Fatalf("missing runtime: %v", seen)
	}
	if _, err := os.Stat(filepath.Join(folder, "start.claim")); !os.IsNotExist(err) {
		t.Fatalf("claim left behind: %v", err)
	}
	app.mu.Lock()
	app.engine = good
	app.mu.Unlock()
	if seen := codes(); seen[202] != 1 || seen[409] != 7 {
		t.Fatalf("after repair: %v", seen)
	}
	waitIdle(t, app)
	if raw, _ := os.ReadFile(filepath.Join(folder, "synthetic-starts.txt")); string(raw) != "one\n" {
		t.Fatalf("worker ran %q", raw)
	}
}

// Review (S18 medium, A08/C02): a worker process that was created but exits at once with an
// error. Expected: Start is accepted (202) and the claim is kept, so a later Start is refused
// with 409 "already been started": once a process existed the one-shot guard holds.
func TestReviewWorkerThatStartedAndFailedKeepsTheClaim(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	response := reviewRequest(t, app, `["annual.txt"]`)
	var review map[string]any
	_ = json.Unmarshal(response.Body.Bytes(), &review)
	id := review["id"].(string)
	payload := `{"id":"` + id + `","review_id":"review-fingerprint","confirm":true}`
	crash := filepath.Join(t.TempDir(), "crash.py")
	if err := os.WriteFile(crash, []byte("import sys\nsys.exit(3)\n"), 0600); err != nil {
		t.Fatal(err)
	}
	app.engine = Engine{Python: app.engine.Python, Script: crash}
	if first := call(app, "POST", "/api/runs/start", payload); first.Code != 202 {
		t.Fatalf("first: %d %q", first.Code, first.Body.String())
	}
	waitIdle(t, app)
	if _, err := os.Stat(filepath.Join(root, "intake", id, "start.claim")); err != nil {
		t.Fatalf("claim released after a worker existed: %v", err)
	}
	again := call(app, "POST", "/api/runs/start", payload)
	if again.Code != 409 || !strings.Contains(again.Body.String(), "already been started") {
		t.Fatalf("second: %d %q", again.Code, again.Body.String())
	}
	if status := call(app, "GET", "/api/runs/status?id="+id, ""); !strings.Contains(status.Body.String(), `"state":"interrupted"`) {
		t.Fatalf("status: %s", status.Body.String())
	}
}

// C11: the workspace switch discovers the new folder without the lock, so a Start can begin
// meanwhile; the switch is then refused when it would commit, as for any active run.
func TestStartDuringAWorkspaceSwitchRefusesTheSwitch(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	response := reviewRequest(t, app, `["annual.txt"]`)
	var review map[string]any
	_ = json.Unmarshal(response.Body.Bytes(), &review)
	id := review["id"].(string)
	other := t.TempDir()
	entered, release := blockDiscovery(t, other)
	switched := make(chan *httptest.ResponseRecorder)
	raw, _ := json.Marshal(Config{Workspace: other})
	go func() { switched <- call(app, "POST", "/api/settings", string(raw)) }()
	<-entered
	if start := call(app, "POST", "/api/runs/start", `{"id":"`+id+`","review_id":"review-fingerprint","confirm":true}`); start.Code != 202 {
		t.Fatalf("start: %d %s", start.Code, start.Body.String())
	}
	close(release)
	if response := <-switched; response.Code != 409 || !strings.Contains(response.Body.String(), "Wait for the active run") {
		t.Fatalf("switch during a started run: %d %s", response.Code, response.Body.String())
	}
	waitIdle(t, app)
	app.mu.RLock()
	defer app.mu.RUnlock()
	if app.config.Workspace != root || app.catalogue.Workspace != root {
		t.Fatalf("workspace moved: config %s, catalogue %s", app.config.Workspace, app.catalogue.Workspace)
	}
}

// uploadOfSize builds a review request for one source of size bytes and returns it with the
// source's SHA-256, computed here as the bytes are generated.
func uploadOfSize(t *testing.T, app *Application, size int64) (*http.Request, string) {
	t.Helper()
	var body bytes.Buffer
	body.Grow(int(size) + 4096)
	form := multipart.NewWriter(&body)
	for key, value := range map[string]string{"context": "{}", "config": "sol-medium", "cap_usd": "10.00", "source_paths": `["big.pdf"]`} {
		if err := form.WriteField(key, value); err != nil {
			t.Fatal(err)
		}
	}
	file, err := form.CreateFormFile("sources", "big.pdf")
	if err != nil {
		t.Fatal(err)
	}
	hash := sha256.New()
	chunk := bytes.Repeat([]byte("0123456789abcdef"), 1<<16) // 1 MiB
	for written := int64(0); written < size; {
		part := chunk[:min(int64(len(chunk)), size-written)]
		_, _ = file.Write(part)
		hash.Write(part)
		written += int64(len(part))
	}
	form.Close()
	request := withSession(app, httptest.NewRequest("POST", "http://"+app.host+"/api/runs/review", &body))
	request.Header.Set("Content-Type", form.FormDataContentType())
	request.Header.Set("X-Issuer-Library", "1")
	return request, hex.EncodeToString(hash.Sum(nil))
}

// C12: an upload is streamed into its retained file and its hash together, never held whole in
// memory; the 64 MiB per-file limit stays exact.
func TestUploadStreamsEachSourceWithinTheExactLimit(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	request, want := uploadOfSize(t, app, 64<<20)
	response := httptest.NewRecorder()
	var before, after runtime.MemStats
	runtime.ReadMemStats(&before)
	app.ServeHTTP(response, request)
	runtime.ReadMemStats(&after)
	if response.Code != 200 {
		t.Fatalf("exactly 64 MiB: %d %s", response.Code, response.Body.String())
	}
	var review map[string]any
	_ = json.Unmarshal(response.Body.Bytes(), &review)
	folder := filepath.Join(root, "intake", review["id"].(string))
	var job NewJob
	raw, _ := os.ReadFile(filepath.Join(folder, "job.json"))
	if json.Unmarshal(raw, &job) != nil || len(job.Sources) != 1 || job.Sources[0].SHA256 != want {
		t.Fatalf("recorded sources %+v, want sha256 %s", job.Sources, want)
	}
	if info, err := os.Stat(filepath.Join(folder, "sources", "big.pdf")); err != nil || info.Size() != 64<<20 {
		t.Fatalf("retained source: %v %v", info, err)
	}
	// The request body (64 MiB) was built before the measurement; the handler itself must not
	// allocate the file again (io.ReadAll allocated more than 64 MiB here).
	allocated := after.TotalAlloc - before.TotalAlloc
	t.Logf("handling a 64 MiB upload allocated %.1f MiB", float64(allocated)/(1<<20))
	if allocated > 16<<20 {
		t.Errorf("handling a 64 MiB upload allocated %d MiB", allocated>>20)
	}
	entries, _ := os.ReadDir(filepath.Join(root, "intake"))
	request, _ = uploadOfSize(t, app, 64<<20+1)
	response = httptest.NewRecorder()
	app.ServeHTTP(response, request)
	if response.Code != 400 || !strings.Contains(response.Body.String(), "up to 64 MiB each") {
		t.Fatalf("64 MiB + 1: %d %s", response.Code, response.Body.String())
	}
	if again, _ := os.ReadDir(filepath.Join(root, "intake")); len(again) != len(entries) {
		t.Fatalf("a refused upload left a folder: %d -> %d", len(entries), len(again))
	}
}

// heldEngine's worker runs until <job>/release exists, then exits without a final status, as a
// worker killed mid-run would.
func heldEngine(t *testing.T) Engine {
	t.Helper()
	engine := fakeEngine(t)
	script := filepath.Join(t.TempDir(), "held.py")
	raw := `import json,sys,pathlib,time
folder=pathlib.Path(sys.argv[2])
job=json.loads((folder/'job.json').read_text())
if sys.argv[1]=='review':
 print(json.dumps({'ok':True,'review_id':'review-fingerprint','id':job['id'],'provider_ready':True}))
else:
 deadline=time.time()+60
 while not (folder/'release').exists() and time.time()<deadline: time.sleep(.01)
`
	if err := os.WriteFile(script, []byte(raw), 0600); err != nil {
		t.Fatal(err)
	}
	return Engine{Python: engine.Python, Script: script}
}

func jobState(t *testing.T, folder string) JobStatus {
	t.Helper()
	var status JobStatus
	raw, _ := os.ReadFile(filepath.Join(folder, "status.json"))
	_ = json.Unmarshal(raw, &status)
	return status
}

func restarted(t *testing.T, root string) *Application {
	t.Helper()
	app, err := newApplication(Locations{State: t.TempDir(), Documents: t.TempDir()}, root)
	if err != nil {
		t.Fatal(err)
	}
	app.host = "127.0.0.1:54321"
	app.stop = func() {}
	return app
}

// A07: a job an earlier instance left "running" is settled when the app starts: interrupted when
// no worker holds its lock (a dead worker, or one started before the lock existed); other
// states are left alone.
func TestRestartSettlesARunningJobWhoseWorkerIsGone(t *testing.T) {
	_, root := testApp(t)
	jobs := map[string]string{}
	for i, setup := range []string{"unlocked", "no-lock", "complete", "reviewed"} {
		id := fmt.Sprintf("web-%032x", i+1)
		jobs[setup] = filepath.Join(root, "intake", id)
		state := "running"
		if setup == "complete" || setup == "reviewed" {
			state = setup
		}
		writeJob(t, root, id, state, time.Now())
		if setup != "no-lock" {
			put(t, root, "intake/"+id+"/worker.lock", nil)
		}
	}
	app := restarted(t, root)
	for setup, folder := range jobs {
		want := map[string]string{"unlocked": "interrupted", "no-lock": "interrupted", "complete": "complete", "reviewed": "reviewed"}[setup]
		if got := jobState(t, folder); got.State != want {
			t.Errorf("%s: state %q, want %q", setup, got.State, want)
		} else if want == "interrupted" && !strings.Contains(got.Message, "no automatic paid retry was made") {
			t.Errorf("%s: message %q", setup, got.Message)
		}
	}
	app.mu.RLock()
	defer app.mu.RUnlock()
	if len(app.activeJobs) != 0 {
		t.Fatalf("dead jobs counted as active: %v", app.activeJobs)
	}
}

// A07: a worker that outlives the instance that started it still holds its lock, so a restarted
// app treats its job as active (no workspace change, no second Start) until the worker ends.
func TestRestartWithALiveWorkerKeepsItsJobActiveUntilItEnds(t *testing.T) {
	shortWorkerPoll(t)
	first, root := testApp(t)
	first.engine = heldEngine(t)
	review := reviewRequest(t, first, `["annual.txt"]`)
	var value map[string]any
	_ = json.Unmarshal(review.Body.Bytes(), &value)
	id := value["id"].(string)
	folder := filepath.Join(root, "intake", id)
	t.Cleanup(func() {
		started, _ := filepath.Glob(filepath.Join(root, "intake", "web-*"))
		for _, job := range started {
			_ = os.WriteFile(filepath.Join(job, "release"), nil, 0600)
		}
	})
	if start := call(first, "POST", "/api/runs/start", `{"id":"`+id+`","review_id":"review-fingerprint","confirm":true}`); start.Code != 202 {
		t.Fatalf("start: %d %s", start.Code, start.Body.String())
	}
	second := restarted(t, root)
	second.engine = first.engine
	if got := jobState(t, folder); got.State != "running" {
		t.Fatalf("a live worker's job was settled as %q", got.State)
	}
	other := reviewRequest(t, second, `["annual.txt"]`)
	_ = json.Unmarshal(other.Body.Bytes(), &value)
	if start := call(second, "POST", "/api/runs/start", `{"id":"`+value["id"].(string)+`","review_id":"review-fingerprint","confirm":true}`); start.Code != 409 {
		t.Fatalf("second Start beside a live worker: %d %s", start.Code, start.Body.String())
	}
	raw, _ := json.Marshal(Config{Workspace: t.TempDir()})
	if settings := call(second, "POST", "/api/settings", string(raw)); settings.Code != 409 {
		t.Fatalf("workspace change beside a live worker: %d %s", settings.Code, settings.Body.String())
	}
	if err := os.WriteFile(filepath.Join(folder, "release"), nil, 0600); err != nil {
		t.Fatal(err)
	}
	waitIdle(t, second)
	waitIdle(t, first)
	if got := jobState(t, folder); got.State != "interrupted" {
		t.Fatalf("after the worker ended: %q", got.State)
	}
}

func shortWorkerPoll(t *testing.T) {
	saved := workerPoll
	workerPoll = 10 * time.Millisecond
	t.Cleanup(func() { workerPoll = saved })
}

// A07: a worker lock that cannot be created fails the Start closed and retryably: no process, no
// "running" status, the start claim released; once the obstacle is gone the same run starts.
func TestStartWithAnUncreatableWorkerLockIsRetryable(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	review := reviewRequest(t, app, `["annual.txt"]`)
	var value map[string]any
	_ = json.Unmarshal(review.Body.Bytes(), &value)
	id := value["id"].(string)
	folder := filepath.Join(root, "intake", id)
	lock := filepath.Join(folder, "worker.lock")
	if err := os.Symlink(lock, lock); err != nil { // opening it fails with a loop, never a lock
		t.Skip(err)
	}
	payload := `{"id":"` + id + `","review_id":"review-fingerprint","confirm":true}`
	if start := call(app, "POST", "/api/runs/start", payload); start.Code != 500 || !strings.Contains(start.Body.String(), "Start can be tried again") {
		t.Fatalf("start with no lock: %d %s", start.Code, start.Body.String())
	}
	if _, err := os.Stat(filepath.Join(folder, "start.claim")); err == nil {
		t.Error("the start claim was kept though nothing started")
	}
	if _, err := os.Stat(filepath.Join(folder, "synthetic-starts.txt")); err == nil {
		t.Error("a worker started without its lock")
	}
	if got := jobState(t, folder); got.State == "running" {
		t.Error("status says running though no worker exists")
	}
	app.mu.RLock()
	active := len(app.activeJobs)
	app.mu.RUnlock()
	if active != 0 {
		t.Errorf("%d active jobs", active)
	}
	if err := os.Remove(lock); err != nil {
		t.Fatal(err)
	}
	if start := call(app, "POST", "/api/runs/start", payload); start.Code != 202 {
		t.Fatalf("retry: %d %s", start.Code, start.Body.String())
	}
	waitIdle(t, app)
}

// A07: a lock that cannot be checked leaves its job exactly as it was, and not active.
func TestRestartLeavesAJobWhoseLockCannotBeCheckedAsItIs(t *testing.T) {
	_, root := testApp(t)
	id := fmt.Sprintf("web-%032x", 9)
	writeJob(t, root, id, "running", time.Now())
	lock := filepath.Join(root, "intake", id, "worker.lock")
	if err := os.Symlink(lock, lock); err != nil {
		t.Skip(err)
	}
	app := restarted(t, root)
	if got := jobState(t, filepath.Join(root, "intake", id)); got.State != "running" {
		t.Errorf("state %q, want running left as it is", got.State)
	}
	app.mu.RLock()
	defer app.mu.RUnlock()
	if len(app.activeJobs) != 0 {
		t.Errorf("an unchecked job counted as active: %v", app.activeJobs)
	}
}

// heldReviewEngine's review waits until <job>/release exists (60 s at most), then reports a
// provider-ready review; its start records the start and exits, as fakeEngine's does.
func heldReviewEngine(t *testing.T) Engine {
	t.Helper()
	engine := fakeEngine(t)
	script := filepath.Join(t.TempDir(), "held-review.py")
	raw := `import json,sys,pathlib,time
folder=pathlib.Path(sys.argv[2])
job=json.loads((folder/'job.json').read_text())
if sys.argv[1]=='review':
 deadline=time.time()+60
 while not (folder/'release').exists() and time.time()<deadline: time.sleep(.01)
 print(json.dumps({'ok':True,'review_id':'review-fingerprint','id':job['id'],'provider_ready':True}))
else:
 (folder/'synthetic-starts.txt').write_text('one\n')
 (folder/'status.json').write_text(json.dumps({'state':'stopped','message':'Synthetic worker seam only; no provider called.'}))
`
	if err := os.WriteFile(script, []byte(raw), 0600); err != nil {
		t.Fatal(err)
	}
	return Engine{Python: engine.Python, Script: script}
}

func inFlightReviews(app *Application) int {
	app.mu.RLock()
	defer app.mu.RUnlock()
	return app.reviews
}

// waitReviews waits (5 s at most) until exactly want reviews are in flight.
func waitReviews(t *testing.T, app *Application, want int) {
	t.Helper()
	for deadline := time.Now().Add(5 * time.Second); inFlightReviews(app) != want; time.Sleep(5 * time.Millisecond) {
		if time.Now().After(deadline) {
			t.Fatalf("%d reviews in flight, want %d", inFlightReviews(app), want)
		}
	}
}

// heldJobs waits (5 s at most) until at least want reviews in workspace have saved job.json, which
// the handler writes after counting the review and before the held review starts, and returns
// their folders.
func heldJobs(t *testing.T, workspace string, want int) []string {
	t.Helper()
	for deadline := time.Now().Add(5 * time.Second); ; time.Sleep(5 * time.Millisecond) {
		jobs, _ := filepath.Glob(filepath.Join(workspace, "intake", "web-*", "job.json"))
		if len(jobs) >= want {
			folders := []string{}
			for _, job := range jobs {
				folders = append(folders, filepath.Dir(job))
			}
			return folders
		}
		if time.Now().After(deadline) {
			t.Fatalf("%d held reviews, want %d", len(jobs), want)
		}
	}
}

// releaseReviews waits for want held reviews in workspace, then lets every held review finish.
func releaseReviews(t *testing.T, workspace string, want int) {
	t.Helper()
	for _, folder := range heldJobs(t, workspace, want) {
		if err := os.WriteFile(filepath.Join(folder, "release"), nil, 0600); err != nil {
			t.Fatal(err)
		}
	}
}

func switchTo(app *Application, workspace string) *httptest.ResponseRecorder {
	raw, _ := json.Marshal(Config{Workspace: workspace})
	return call(app, "POST", "/api/settings", string(raw))
}

func currentWorkspace(app *Application) string {
	app.mu.RLock()
	defer app.mu.RUnlock()
	return app.config.Workspace
}

// C08: while a review is in flight a workspace switch is refused with 409 and the message, and
// saving the same workspace (also spelled with a trailing separator or ".") keeps today's 200.
// Once the review ends the reviewed run starts in the workspace it was reviewed in (202, where the
// reproduction got 409 "Review this run before starting"), and the switch is accepted.
func TestWorkspaceSwitchIsRefusedWhileAReviewIsInFlight(t *testing.T) {
	app, root := testApp(t)
	app.engine = heldReviewEngine(t)
	t.Cleanup(func() { releaseReviews(t, root, 0) })
	other := t.TempDir()
	discovered := 0 // discoveries of other; only this test goroutine switches to it
	saved := discoverWorkspace.Load()
	count := func(folder string, seeds Catalogue) Catalogue {
		if folder == other {
			discovered++
		}
		return (*saved)(folder, seeds)
	}
	discoverWorkspace.Store(&count)
	t.Cleanup(func() { discoverWorkspace.Store(saved) })
	done := make(chan *httptest.ResponseRecorder)
	go func() { done <- reviewRequest(t, app, `["annual.txt"]`) }()
	waitReviews(t, app, 1)
	if response := switchTo(app, other); response.Code != 409 || response.Body.String() != reviewInFlight+"\n" {
		t.Fatalf("switch during a review: %d %q", response.Code, response.Body.String())
	}
	if discovered != 0 {
		t.Fatal("a switch refused for the review still discovered the new workspace")
	}
	for _, same := range []string{root, root + string(filepath.Separator), filepath.Join(root, ".")} {
		if response := switchTo(app, same); response.Code != 200 {
			t.Fatalf("saving the same workspace %q during a review: %d %s", same, response.Code, response.Body.String())
		}
	}
	if currentWorkspace(app) != root {
		t.Fatalf("workspace moved to %s", currentWorkspace(app))
	}
	releaseReviews(t, root, 1)
	review := <-done
	var value map[string]any
	if review.Code != 200 || json.Unmarshal(review.Body.Bytes(), &value) != nil || value["ok"] != true {
		t.Fatalf("review: %d %s", review.Code, review.Body.String())
	}
	waitReviews(t, app, 0)
	if start := call(app, "POST", "/api/runs/start", `{"id":"`+value["id"].(string)+`","review_id":"review-fingerprint","confirm":true}`); start.Code != 202 {
		t.Fatalf("start after the refused switch: %d %s", start.Code, start.Body.String())
	}
	waitIdle(t, app)
	if response := switchTo(app, other); response.Code != 200 || currentWorkspace(app) != other {
		t.Fatalf("switch after the review: %d %s", response.Code, response.Body.String())
	}
}

// C08: a review cut at the review bound (1 s here; the held review would wait 60 s) answers 503
// and leaves no review in flight, so the switch refused during it is accepted after it.
func TestAReviewPastTheBoundReleasesTheWorkspace(t *testing.T) {
	shortReviewTimeout(t, time.Second)
	app, root := testApp(t)
	app.engine = heldReviewEngine(t)
	t.Cleanup(func() { releaseReviews(t, root, 0) })
	other := t.TempDir()
	done := make(chan *httptest.ResponseRecorder)
	go func() { done <- reviewRequest(t, app, `["annual.txt"]`) }()
	waitReviews(t, app, 1)
	if response := switchTo(app, other); response.Code != 409 {
		t.Fatalf("switch during the review: %d", response.Code)
	}
	if review := <-done; review.Code != 503 {
		t.Fatalf("review past the bound: %d %s", review.Code, review.Body.String())
	}
	if n := inFlightReviews(app); n != 0 {
		t.Fatalf("%d reviews in flight after the bound", n)
	}
	if response := switchTo(app, other); response.Code != 200 {
		t.Fatalf("switch after the bound: %d %s", response.Code, response.Body.String())
	}
}

// C08: the browser gives up on a review over real loopback. The review still runs (it is not tied
// to the request) and still writes into the workspace, so the switch stays refused until the
// review ends; then the handler returns and the switch is accepted.
func TestAReviewWhoseClientWentAwayHoldsTheWorkspaceUntilItEnds(t *testing.T) {
	app, root := testApp(t)
	app.engine = heldReviewEngine(t)
	server := slowServer(t, app)
	t.Cleanup(func() { releaseReviews(t, root, 0) }) // runs before server.Close waits for the handler
	other := t.TempDir()
	ctx, cancel := context.WithCancel(context.Background())
	gone := make(chan error, 1)
	go func() {
		response, err := postReviewWith(t, server, ctx, &http.Client{Transport: &http.Transport{Proxy: nil}})
		if err == nil {
			response.Body.Close()
		}
		gone <- err
	}()
	waitReviews(t, app, 1)
	cancel()
	if err := <-gone; err == nil {
		t.Fatal("the client received a response after giving up")
	}
	if response := switchTo(app, other); response.Code != 409 {
		t.Fatalf("switch while the abandoned review runs: %d", response.Code)
	}
	releaseReviews(t, root, 1)
	waitReviews(t, app, 0)
	if response := switchTo(app, other); response.Code != 200 {
		t.Fatalf("switch after the abandoned review: %d %s", response.Code, response.Body.String())
	}
}

// C08: the error exits. A missing runtime (503), a validator refusal (200, ok false) and an
// upload refused before the workspace is read (400) each leave no review in flight.
func TestReviewErrorsLeaveNoReviewInFlight(t *testing.T) {
	app, _ := testApp(t)
	good := fakeEngine(t)
	refusing := filepath.Join(t.TempDir(), "refuse.py")
	if err := os.WriteFile(refusing, []byte("import json\nprint(json.dumps({'ok':False,'problems':['synthetic refusal']}))\n"), 0600); err != nil {
		t.Fatal(err)
	}
	for _, c := range []struct {
		label  string
		engine Engine
		paths  string
		status int
	}{
		{"missing runtime", Engine{Python: filepath.Join(t.TempDir(), "no-python"), Script: good.Script}, `["annual.txt"]`, 503},
		{"validator refusal", Engine{Python: good.Python, Script: refusing}, `["annual.txt"]`, 200},
		{"refused upload", good, `["../outside.txt"]`, 400},
	} {
		app.engine = c.engine
		if response := reviewRequest(t, app, c.paths); response.Code != c.status {
			t.Fatalf("%s: %d %s", c.label, response.Code, response.Body.String())
		}
		if n := inFlightReviews(app); n != 0 {
			t.Fatalf("%s: %d reviews in flight", c.label, n)
		}
	}
	if response := switchTo(app, t.TempDir()); response.Code != 200 {
		t.Fatalf("switch after the failed reviews: %d %s", response.Code, response.Body.String())
	}
}

// C08 adversarial: two reviews in flight. Expected: the switch is refused while either runs (2,
// then 1 in flight) and accepted once both have ended.
func TestTwoReviewsInFlightRefuseTheSwitchUntilBothEnd(t *testing.T) {
	app, root := testApp(t)
	app.engine = heldReviewEngine(t)
	t.Cleanup(func() { releaseReviews(t, root, 0) })
	other := t.TempDir()
	done := make(chan *httptest.ResponseRecorder, 2)
	for range 2 {
		go func() { done <- reviewRequest(t, app, `["annual.txt"]`) }()
	}
	waitReviews(t, app, 2)
	if response := switchTo(app, other); response.Code != 409 {
		t.Fatalf("switch with two reviews: %d", response.Code)
	}
	jobs := heldJobs(t, root, 2)
	if err := os.WriteFile(filepath.Join(jobs[0], "release"), nil, 0600); err != nil {
		t.Fatal(err)
	}
	if review := <-done; review.Code != 200 {
		t.Fatalf("first review: %d", review.Code)
	}
	waitReviews(t, app, 1)
	if response := switchTo(app, other); response.Code != 409 {
		t.Fatalf("switch with one review left: %d", response.Code)
	}
	releaseReviews(t, root, 1)
	if review := <-done; review.Code != 200 {
		t.Fatalf("second review: %d", review.Code)
	}
	waitReviews(t, app, 0)
	if response := switchTo(app, other); response.Code != 200 {
		t.Fatalf("switch after both: %d %s", response.Code, response.Body.String())
	}
}

// C08: a review that starts while a switch is discovering the new workspace (unlocked) refuses the
// switch when it would commit, as a Start does; the workspace and catalogue stay, and the review
// completes into the workspace it read.
func TestAReviewStartedDuringASwitchRefusesItAtCommit(t *testing.T) {
	app, root := testApp(t)
	app.engine = heldReviewEngine(t)
	t.Cleanup(func() { releaseReviews(t, root, 0) })
	other := t.TempDir()
	entered, release := blockDiscovery(t, other)
	switched := make(chan *httptest.ResponseRecorder)
	go func() { switched <- switchTo(app, other) }()
	<-entered
	done := make(chan *httptest.ResponseRecorder)
	go func() { done <- reviewRequest(t, app, `["annual.txt"]`) }()
	waitReviews(t, app, 1)
	close(release)
	if response := <-switched; response.Code != 409 || response.Body.String() != reviewInFlight+"\n" {
		t.Fatalf("switch committed during a review: %d %q", response.Code, response.Body.String())
	}
	app.mu.RLock()
	workspace, catalogue := app.config.Workspace, app.catalogue.Workspace
	app.mu.RUnlock()
	if workspace != root || catalogue != root {
		t.Fatalf("config %s, catalogue %s; want %s", workspace, catalogue, root)
	}
	releaseReviews(t, root, 1)
	review := <-done
	var value map[string]any
	if review.Code != 200 || json.Unmarshal(review.Body.Bytes(), &value) != nil {
		t.Fatalf("review: %d %s", review.Code, review.Body.String())
	}
	if _, err := os.Stat(filepath.Join(root, "intake", value["id"].(string), "review.json")); err != nil {
		t.Fatalf("review not retained in the workspace it read: %v", err)
	}
}

func writeEvents(t *testing.T, root, id, text string) {
	t.Helper()
	folder := filepath.Join(root, "runs", id)
	if err := os.MkdirAll(folder, 0700); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(filepath.Join(folder, "events.jsonl"), []byte(text), 0600); err != nil {
		t.Fatal(err)
	}
}

const eventsID = "web-" + "c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0c0"

// Hand-written log: CP-0 accepted after one turn; CP-1 on its second turn, then a rejected draft.
const eventLines = `{"at":"2026-11-07T10:00:00Z","event":"module_started","module":"CP-0"}
{"at":"2026-11-07T10:00:01Z","event":"turn","module":"CP-0","turn":1,"max_turns":32,"spent_usd":"0","held_usd":"1.50","cap_usd":"10"}
{"at":"2026-11-07T10:00:02Z","event":"module_accepted","module":"CP-0"}
{"at":"2026-11-07T10:00:03Z","event":"module_started","module":"CP-1"}
{"at":"2026-11-07T10:00:04Z","event":"turn","module":"CP-1","turn":1,"max_turns":32,"spent_usd":"0.40","held_usd":"1.50","cap_usd":"10"}
{"at":"2026-11-07T10:00:05Z","event":"turn","module":"CP-1","turn":2,"max_turns":32,"spent_usd":"0.85","held_usd":"1.60","cap_usd":"10"}
`

func TestRunProgressFoldsEvents(t *testing.T) {
	root := t.TempDir()
	writeEvents(t, root, eventsID, eventLines+`{"at":"2026-11-07T10:00:06Z","event":"draft_rejected","module":"CP-1","writes_left":2}`+"\n")
	got, ok := runProgress(root, eventsID)
	if !ok {
		t.Fatal("no progress from a readable log")
	}
	want := map[string]any{"module": "CP-1", "step": "repairing", "turn": 2, "max_turns": 32, "spent_usd": "0.85", "held_usd": "1.60", "cap_usd": "10", "accepted": 1}
	if !reflect.DeepEqual(got, want) {
		t.Fatalf("got %v, want %v", got, want)
	}
	writeEvents(t, root, eventsID, eventLines+`{"at":"x","event":"module_accepted","module":"CP-1"}`+"\n"+`{"at":"x","event":"delivery_started"}`+"\n")
	if got, _ := runProgress(root, eventsID); got["step"] != "delivering" || got["accepted"] != 2 {
		t.Fatalf("after delivery start: %v", got)
	}
	writeEvents(t, root, eventsID, eventLines+`{"at":"x","event":"stopped","reason":"budget"}`+"\n")
	if got, _ := runProgress(root, eventsID); got["step"] != "stopped" || got["turn"] != 2 || got["stopped_during"] != "running" {
		t.Fatalf("after stop: %v", got)
	}
	writeEvents(t, root, eventsID, eventLines+`{"at":"x","event":"module_accepted","module":"CP-1"}`+"\n"+`{"at":"x","event":"delivery_started"}`+"\n"+`{"at":"x","event":"stopped","reason":"other"}`+"\n")
	if got, _ := runProgress(root, eventsID); got["step"] != "stopped" || got["stopped_during"] != "delivering" || got["accepted"] != 2 {
		t.Fatalf("stop in delivery: %v", got)
	}
	writeEvents(t, root, eventsID, `{"at":"x","event":"module_started","module":"CP-0"}`+"\n")
	if got, _ := runProgress(root, eventsID); got["step"] != "started" || got["accepted"] != 0 {
		t.Fatalf("first module only: %v", got)
	}
}

func TestRunProgressIgnoresATruncatedLastLine(t *testing.T) {
	root := t.TempDir()
	writeEvents(t, root, eventsID, eventLines+`{"at":"2026-11-07T10:00:06Z","event":"tur`)
	got, ok := runProgress(root, eventsID)
	if !ok || got["turn"] != 2 || got["step"] != "running" || got["accepted"] != 1 {
		t.Fatalf("truncated tail changed the fold: %v %v", got, ok)
	}
}

func TestRunProgressFallsBackToProgressJSON(t *testing.T) {
	root := t.TempDir()
	if _, ok := runProgress(root, eventsID); ok {
		t.Fatal("progress from nothing")
	}
	folder := filepath.Join(root, "runs", eventsID)
	if err := os.MkdirAll(folder, 0700); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(filepath.Join(folder, "progress.json"), []byte(`{"module":"CP-1","step":"started","spent_usd":"0.10"}`), 0600); err != nil {
		t.Fatal(err)
	}
	want := map[string]any{"module": "CP-1", "step": "started", "spent_usd": "0.10"}
	if got, ok := runProgress(root, eventsID); !ok || !reflect.DeepEqual(got, want) {
		t.Fatalf("retained fallback: %v %v", got, ok)
	}
	// An empty log (run started, no module dispatched yet) has no progress; progress.json still serves.
	writeEvents(t, root, eventsID, "")
	if got, ok := runProgress(root, eventsID); !ok || !reflect.DeepEqual(got, want) {
		t.Fatalf("empty log: %v %v", got, ok)
	}
	// A corrupt earlier line skips the whole log (documented fail-open, logged once).
	writeEvents(t, root, eventsID, "not json\n"+eventLines)
	if got, ok := runProgress(root, eventsID); !ok || !reflect.DeepEqual(got, want) {
		t.Fatalf("corrupt earlier line: %v %v", got, ok)
	}
}

func TestRunProgressIsAbsentWithNeitherFile(t *testing.T) {
	app, root := testApp(t)
	writeJob(t, root, eventsID, "running", time.Now())
	row := call(app, "GET", "/api/runs/status?id="+eventsID, "")
	var value map[string]any
	if row.Code != 200 || json.Unmarshal(row.Body.Bytes(), &value) != nil {
		t.Fatalf("%d %s", row.Code, row.Body.String())
	}
	if _, present := value["progress"]; present {
		t.Fatalf("progress invented: %v", value)
	}
}

func TestReviewRefusesMoreTurnsThanTheLoopAllows(t *testing.T) {
	app, _ := testApp(t)
	app.engine = fakeEngine(t)
	if response := reviewRequestTurns(t, app, `["a.txt"]`, "65"); response.Code != 400 {
		t.Fatalf("65 turns: %d %s", response.Code, response.Body.String())
	}
	if response := reviewRequestTurns(t, app, `["a.txt"]`, "64"); response.Code != 200 {
		t.Fatalf("64 turns: %d %s", response.Code, response.Body.String())
	}
}

// A Refresh must not wait behind a store run that is still going, and the body that run
// produces (read before the refresh) must not be cached for later reads.
func TestRefreshDoesNotWaitForARunningStoreAndItsBodyIsNotCached(t *testing.T) {
	app, _ := testApp(t)
	engine := fakeEngine(t)
	folder := filepath.Dir(engine.Script)
	release, starts := filepath.Join(folder, "release"), filepath.Join(folder, "starts")
	script := `import json,sys,os,time
with open(` + strconv.Quote(starts) + `,'a') as s: s.write('x')
n=os.path.getsize(` + strconv.Quote(starts) + `)
while not os.path.exists(` + strconv.Quote(release) + `): time.sleep(.02)
print(json.dumps({'run':n}))
`
	if err := os.WriteFile(filepath.Join(folder, "store.py"), []byte(script), 0600); err != nil {
		t.Fatal(err)
	}
	app.engine = engine
	first := make(chan *httptest.ResponseRecorder, 1)
	go func() { first <- call(app, "GET", "/api/workspace", "") }()
	for deadline := time.Now().Add(5 * time.Second); ; time.Sleep(10 * time.Millisecond) {
		if info, err := os.Stat(starts); err == nil && info.Size() == 1 {
			break
		}
		if time.Now().After(deadline) {
			t.Fatal("the store run never started")
		}
	}
	refreshed := make(chan *httptest.ResponseRecorder, 1)
	go func() { refreshed <- call(app, "POST", "/api/refresh", "{}") }()
	select {
	case response := <-refreshed:
		if response.Code != 200 {
			t.Fatalf("refresh: %d %s", response.Code, response.Body.String())
		}
	case <-time.After(3 * time.Second):
		t.Fatal("refresh waited for the running store")
	}
	if err := os.WriteFile(release, nil, 0600); err != nil {
		t.Fatal(err)
	}
	if response := <-first; response.Code != 200 || strings.TrimSpace(response.Body.String()) != `{"run": 1}` {
		t.Fatalf("first read: %d %s", response.Code, response.Body.String())
	}
	next := call(app, "GET", "/api/workspace", "")
	if next.Code != 200 || strings.TrimSpace(next.Body.String()) != `{"run": 2}` {
		t.Fatalf("the pre-refresh body was cached: %d %s", next.Code, next.Body.String())
	}
}

// fakeClock is a settable clock for one app, safe for the goroutines that read it.
type fakeClock struct {
	mu  sync.Mutex
	now time.Time
}

func (c *fakeClock) read() time.Time { c.mu.Lock(); defer c.mu.Unlock(); return c.now }
func (c *fakeClock) add(d time.Duration) {
	c.mu.Lock()
	c.now = c.now.Add(d)
	c.mu.Unlock()
}

func TestAFinishedRunNotifiesNativelyOnlyWhenNoTabWatches(t *testing.T) {
	origin := time.Date(2026, 11, 8, 12, 0, 0, 0, time.UTC)
	cases := []struct {
		name      string
		pollFirst bool // a list request before the finish (a tab that was open and then closed)
		pollAfter bool // a list request while finishJob waits (a throttled hidden tab)
		want      int
	}{
		{"A poll after the finish gives no native notice", true, true, 0},
		{"No poll at all gives one native notice", false, false, 1},
		{"A poll only before the finish gives one native notice", true, false, 1},
	}
	for _, c := range cases {
		t.Run(c.name, func(t *testing.T) {
			app, root := testApp(t)
			app.engine = fakeEngine(t)
			clock := &fakeClock{now: origin}
			app.now = clock.read
			var mu sync.Mutex
			var calls [][2]string
			app.notifier = func(title, body string) error {
				mu.Lock()
				defer mu.Unlock()
				calls = append(calls, [2]string{title, body})
				return nil
			}
			pauses := 0
			app.pause = func(d time.Duration) {
				pauses++ // only the finishJob goroutine calls pause
				if c.pollAfter && pauses == 3 {
					clock.add(d)
					call(app, "GET", "/api/runs/list", "")
					return
				}
				clock.add(d)
			}
			done := make(chan struct{})
			app.onFinished = func(string) { close(done) }
			var review map[string]any
			_ = json.Unmarshal(reviewRequest(t, app, `["annual.txt"]`).Body.Bytes(), &review)
			id := review["id"].(string)
			hold := filepath.Join(root, "intake", id, "hold")
			if err := os.WriteFile(hold, nil, 0600); err != nil {
				t.Fatal(err)
			}
			if start := call(app, "POST", "/api/runs/start", `{"id":"`+id+`","review_id":"review-fingerprint","confirm":true}`); start.Code != 202 {
				t.Fatal(start.Code)
			}
			if c.pollFirst {
				if list := call(app, "GET", "/api/runs/list", ""); list.Code != 200 {
					t.Fatal(list.Code)
				}
			}
			clock.add(time.Second) // time passes between that poll and the finish
			if err := os.Remove(hold); err != nil {
				t.Fatal(err)
			}
			select {
			case <-done:
			case <-time.After(10 * time.Second):
				t.Fatal("finishJob did not return")
			}
			mu.Lock()
			defer mu.Unlock()
			if len(calls) != c.want {
				t.Fatalf("%d native notices, want %d: %v", len(calls), c.want, calls)
			}
			if c.want == 1 && calls[0] != [2]string{"Issuer Library", "Run stopped"} {
				t.Fatalf("notice %v", calls[0])
			}
		})
	}
}

const activityLines = `{"at":"2026-11-08T09:00:00Z","event":"module_started","module":"CP-0"}
{"at":"2026-11-08T09:00:01Z","event":"turn","module":"CP-0","turn":1,"max_turns":24,"spent_usd":"0.00","held_usd":"5.73","cap_usd":"10"}
{"at":"2026-11-08T09:00:02Z","event":"draft_rejected","module":"CP-0","writes_left":2}
{"at":"2026-11-08T09:00:03Z","event":"module_accepted","module":"CP-0"}
{"at":"2026-11-08T09:00:04Z","event":"delivery_started"}
{"at":"2026-11-08T09:00:05Z","event":"delivered"}
`

type eventsBody struct {
	Events   []map[string]any `json:"events"`
	Complete bool             `json:"complete"`
}

func getEvents(t *testing.T, app *Application) (int, eventsBody, string) {
	t.Helper()
	response := call(app, "GET", "/api/runs/events?id="+eventsID, "")
	var body eventsBody
	if response.Code == 200 {
		if err := json.Unmarshal(response.Body.Bytes(), &body); err != nil {
			t.Fatal(err)
		}
	}
	return response.Code, body, response.Body.String()
}

func TestRunEventsEndpointListsEveryEventWithItsFields(t *testing.T) {
	app, root := testApp(t)
	writeJob(t, root, eventsID, "running", time.Now())
	writeEvents(t, root, eventsID, activityLines)
	code, body, raw := getEvents(t, app)
	if code != 200 || len(body.Events) != 6 || !body.Complete {
		t.Fatalf("%d %s", code, raw)
	}
	if body.Events[0]["at"] != "2026-11-08T09:00:00Z" || body.Events[0]["event"] != "module_started" {
		t.Fatalf("first event: %v", body.Events[0])
	}
	if body.Events[1]["held_usd"] != "5.73" || body.Events[1]["turn"] != float64(1) || body.Events[1]["max_turns"] != float64(24) {
		t.Fatalf("turn event: %v", body.Events[1])
	}
	if body.Events[2]["writes_left"] != float64(2) {
		t.Fatalf("rejected event: %v", body.Events[2])
	}
	if body.Events[5]["event"] != "delivered" {
		t.Fatalf("last event: %v", body.Events[5])
	}
}

func TestRunEventsEndpointDropsATruncatedLastLine(t *testing.T) {
	app, root := testApp(t)
	writeJob(t, root, eventsID, "running", time.Now())
	writeEvents(t, root, eventsID, activityLines[:strings.LastIndex(strings.TrimSuffix(activityLines, "\n"), "\n")+1]+`{"event":"tur`)
	code, body, raw := getEvents(t, app)
	if code != 200 || len(body.Events) != 5 || body.Complete {
		t.Fatalf("%d %s", code, raw)
	}
}

func TestRunEventsEndpointWithoutALogIsAnEmptyList(t *testing.T) {
	app, root := testApp(t)
	if code, _, _ := getEvents(t, app); code != 404 {
		t.Fatalf("neither file: %d", code)
	}
	writeJob(t, root, eventsID, "running", time.Now())
	code, _, raw := getEvents(t, app)
	if code != 200 || strings.TrimSpace(raw) != `{"events":[],"complete":true}` {
		t.Fatalf("%d %s", code, raw)
	}
}

func TestRunEventsStopsAtTheReadLimit(t *testing.T) {
	saved := eventsLimit
	eventsLimit = 300
	t.Cleanup(func() { eventsLimit = saved })
	app, root := testApp(t)
	writeJob(t, root, eventsID, "running", time.Now())
	writeEvents(t, root, eventsID, activityLines)
	code, body, raw := getEvents(t, app)
	if code != 200 || body.Complete || len(body.Events) == 0 || len(body.Events) >= 6 {
		t.Fatalf("%d %s", code, raw)
	}
}
