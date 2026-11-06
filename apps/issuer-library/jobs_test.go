package main

import (
	"bytes"
	"context"
	"encoding/json"
	"io"
	"mime/multipart"
	"net/http"
	"net/http/httptest"
	"net/http/httptrace"
	"os"
	"os/exec"
	"path/filepath"
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
