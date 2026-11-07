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
	"runtime"
	"slices"
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
	var body bytes.Buffer
	form := multipart.NewWriter(&body)
	for key, value := range map[string]string{"context": "{}", "config": "sol-medium", "cap_usd": "10.00", "source_paths": paths, "modules": "CP-4", "max_turns": "7"} {
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
	request := httptest.NewRequest("POST", "http://"+app.host+"/api/runs/review", &body)
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
	request := httptest.NewRequest("POST", "http://"+app.host+"/api/runs/review", bytes.NewBufferString("anything"))
	request.Header.Set("Origin", "https://untrusted.invalid")
	response := httptest.NewRecorder()
	app.ServeHTTP(response, request)
	if response.Code != 403 {
		t.Fatal("cross-origin upload accepted")
	}
	request = httptest.NewRequest("POST", "http://"+app.host+"/api/runs/review", nil)
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
	store := `import sys,time,pathlib
sys.stdin.read()
mark=pathlib.Path(__file__).with_name('called')
if mark.exists(): time.sleep(1.5)
mark.write_text('1')
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
	response, err := client.Get(server.URL + "/api/workspace")
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
	response, err = client.Do(request)
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

// Review (S18 medium, A04/C05): after a crash, more stale "running"/"starting" jobs than the
// cap. Expected: every active job is listed (40 rows, above the cap of 30), newest first,
// and no finished job takes a place because no room is left.
func TestReviewRunListManyStaleActiveJobsExceedTheCap(t *testing.T) {
	app, root := testApp(t)
	now := time.Now()
	for i := 0; i < 35; i++ {
		writeJob(t, root, fmt.Sprintf("web-%032x", 0x200+i), "running", now.Add(-time.Duration(100+i)*time.Hour))
	}
	for i := 0; i < 5; i++ {
		writeJob(t, root, fmt.Sprintf("web-%032x", 0x300+i), "starting", now.Add(-time.Duration(200+i)*time.Hour))
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
	request := httptest.NewRequest("POST", "http://"+app.host+"/api/runs/review", &body)
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
