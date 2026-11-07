package main

import (
	"bufio"
	"encoding/json"
	"errors"
	"flag"
	"go/ast"
	"go/parser"
	"go/token"
	"io"
	"log"
	"net"
	"net/http"
	"net/http/httptest"
	"os"
	"path/filepath"
	"regexp"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
	"testing"
	"time"
)

// launchRequest asks for the launch path with the given raw query, as the browser does when the
// launcher opens it (no cookie, no Origin).
func launchRequest(app *Application, method, query string) *httptest.ResponseRecorder {
	r := httptest.NewRequest(method, "http://"+app.host+"/launch"+query, nil)
	w := httptest.NewRecorder()
	app.ServeHTTP(w, r)
	return w
}

// C03: the ticket is exchanged once for the session cookie, and the redirect drops it. Expected by
// hand: 303 to "/" with exactly `issuer-library-54321=<session>; Path=/; HttpOnly; SameSite=Strict`
// (no Secure on plain loopback HTTP, no expiry); the same ticket then gets the 403 page and no
// cookie, and the cookie opens /api/catalogue.
func TestLaunchTicketIsExchangedOnceAndTheRedirectDropsIt(t *testing.T) {
	app, _ := testApp(t)
	ticket, session := app.ticket, app.session
	if !regexp.MustCompile(`^[0-9a-f]{64}$`).MatchString(ticket) || !regexp.MustCompile(`^[0-9a-f]{64}$`).MatchString(session) || ticket == session {
		t.Fatalf("ticket %q and session %q must be distinct 32-byte random values", ticket, session)
	}
	if got, want := app.launchURL(), "http://127.0.0.1:54321/launch?ticket="+ticket; got != want {
		t.Fatalf("launch URL %q, want %q", got, want)
	}
	first := launchRequest(app, "GET", "?ticket="+ticket)
	if first.Code != http.StatusSeeOther || first.Header().Get("Location") != "/" {
		t.Fatalf("exchange: %d to %q", first.Code, first.Header().Get("Location"))
	}
	if cookies := first.Header().Values("Set-Cookie"); len(cookies) != 1 || cookies[0] != "issuer-library-54321="+session+"; Path=/; HttpOnly; SameSite=Strict" {
		t.Fatalf("Set-Cookie %q", cookies)
	}
	if body := first.Body.String(); strings.Contains(body, ticket) || strings.Contains(body, session) {
		t.Fatalf("redirect body carries a secret: %q", body)
	}
	again := launchRequest(app, "GET", "?ticket="+ticket)
	if again.Code != http.StatusForbidden || again.Header().Get("Set-Cookie") != "" || again.Body.String() != launcherOnly+"\n" {
		t.Fatalf("reused ticket: %d %q %q", again.Code, again.Header().Get("Set-Cookie"), again.Body.String())
	}
	r := httptest.NewRequest("GET", "http://"+app.host+"/api/catalogue", nil)
	for _, cookie := range first.Result().Cookies() {
		r.AddCookie(cookie)
	}
	w := httptest.NewRecorder()
	app.ServeHTTP(w, r)
	if w.Code != 200 {
		t.Fatalf("catalogue with the exchanged cookie: %d", w.Code)
	}
}

// C03: a tampered or misplaced ticket gets the 403 page and no cookie, and does not spend the real
// one, which still works afterwards. A HEAD or POST to the launch path neither exchanges nor spends.
func TestTamperedTicketsAreRefusedWithoutSpendingTheRealOne(t *testing.T) {
	app, _ := testApp(t)
	ticket := app.ticket
	flip := map[byte]byte{'0': '1'}[ticket[63]]
	if flip == 0 {
		flip = '0'
	}
	for _, query := range []string{
		"",
		"?ticket=",
		"?ticket=" + ticket[:63],
		"?ticket=" + ticket + "0",
		"?ticket=" + ticket[:63] + string(flip),
		"?ticket=" + strings.ToUpper(ticket),
		"?ticket=" + app.session,
		"?Ticket=" + ticket,
		"?t=" + ticket,
		"?ticket=x&ticket=" + ticket, // only the first value counts
	} {
		if w := launchRequest(app, "GET", query); w.Code != http.StatusForbidden || w.Header().Get("Set-Cookie") != "" {
			t.Errorf("%q: %d, cookie %q", query, w.Code, w.Header().Get("Set-Cookie"))
		}
	}
	for _, method := range []string{"HEAD", "POST", "PUT"} {
		if w := launchRequest(app, method, "?ticket="+ticket); w.Code != http.StatusMethodNotAllowed || w.Header().Get("Set-Cookie") != "" {
			t.Errorf("%s: %d, cookie %q", method, w.Code, w.Header().Get("Set-Cookie"))
		}
	}
	for _, path := range []string{"/launch/", "/launch/x", "/Launch", "/api/catalogue", "/"} {
		r := httptest.NewRequest("GET", "http://"+app.host+path+"?ticket="+ticket, nil)
		w := httptest.NewRecorder()
		app.ServeHTTP(w, r)
		if w.Code != http.StatusForbidden || w.Header().Get("Set-Cookie") != "" {
			t.Errorf("ticket on %s: %d, cookie %q", path, w.Code, w.Header().Get("Set-Cookie"))
		}
	}
	if w := launchRequest(app, "GET", "?ticket="+ticket); w.Code != http.StatusSeeOther {
		t.Fatalf("the real ticket after the refused ones: %d", w.Code)
	}
}

// C03: every request that reads the workspace, changes it, starts or spends needs the cookie.
// Expected by hand: without it 403 with the launcher text and no side effect (workspace, quit,
// intake unchanged); with it each endpoint answers as before (for the bodies used here: 200, the
// unknown run 404, the missing runtime 503, the malformed start and review 400). /health alone
// answers without it.
func TestEveryAppRequestNeedsTheSessionCookie(t *testing.T) {
	app, root := testApp(t)
	app.engine = Engine{Python: filepath.Join(t.TempDir(), "missing-python"), Script: "x"}
	var quits atomic.Int32 // app.stop runs on its own goroutine
	app.stop = func() { quits.Add(1) }
	workspace := func() string { app.mu.RLock(); defer app.mu.RUnlock(); return app.config.Workspace }
	other := t.TempDir()
	settings, _ := json.Marshal(Config{Workspace: other})
	for _, c := range []struct {
		method, endpoint, body string
		with                   int
	}{
		{"GET", "/", "", 200},
		{"GET", "/index.html", "", 200},
		{"GET", "/screen.js", "", 200},
		{"GET", "/context-form.html", "", 200},
		{"GET", "/fonts/RedHatText-Regular.woff2", "", 200},
		{"GET", "/api/catalogue", "", 200},
		{"HEAD", "/api/catalogue", "", 200},
		{"GET", "/api/workspace", "", 503},
		{"GET", "/api/runs/list", "", 200},
		{"GET", "/api/runs/status?id=web-" + strings.Repeat("a", 32), "", 404},
		{"GET", "/files/deliverables/report/report.html", "", 200},
		{"HEAD", "/files/deliverables/report/report.html", "", 200},
		{"GET", "/files/runs/case-a/CP-0.md?download=1", "", 200},
		{"POST", "/api/refresh", "{}", 200},
		{"POST", "/api/runs/start", `{"id":"x"}`, 400},
		{"POST", "/api/runs/review", "{}", 400},
		{"POST", "/api/quit", "{}", 200},
		{"POST", "/api/settings", string(settings), 200},
	} {
		r := httptest.NewRequest(c.method, "http://"+app.host+c.endpoint, strings.NewReader(c.body))
		r.Header.Set("X-Issuer-Library", "1")
		r.Header.Set("Content-Type", "application/json")
		r.Header.Set("Origin", "http://"+app.host)
		w := httptest.NewRecorder()
		app.ServeHTTP(w, r)
		if w.Code != http.StatusForbidden || w.Body.String() != launcherOnly+"\n" || !strings.HasPrefix(w.Header().Get("Content-Type"), "text/plain") {
			t.Errorf("%s %s without the cookie: %d %q", c.method, c.endpoint, w.Code, w.Body.String())
		}
		// A refused quit never reaches the handler (the body above is the 403 text); the one stop
		// counted below is the cookie-carrying quit, which calls stop on its own goroutine.
		if workspace() != root {
			t.Fatalf("%s %s without the cookie had an effect", c.method, c.endpoint)
		}
		if entries, _ := os.ReadDir(filepath.Join(root, "intake")); len(entries) != 0 {
			t.Fatalf("%s %s without the cookie created intake", c.method, c.endpoint)
		}
		if got := call(app, c.method, c.endpoint, c.body); got.Code != c.with {
			t.Errorf("%s %s with the cookie: %d, want %d: %s", c.method, c.endpoint, got.Code, c.with, got.Body.String())
		}
	}
	for deadline := time.Now().Add(5 * time.Second); quits.Load() == 0 && time.Now().Before(deadline); {
		time.Sleep(10 * time.Millisecond)
	}
	if quits.Load() != 1 || workspace() != other {
		t.Fatalf("with the cookie: quits %d, workspace %s", quits.Load(), workspace())
	}
	health := httptest.NewRecorder()
	app.ServeHTTP(health, httptest.NewRequest("GET", "http://"+app.host+"/health", nil))
	var value map[string]string
	if health.Code != 200 || json.Unmarshal(health.Body.Bytes(), &value) != nil || len(value) != 2 || value["application"] != "finalworkflow-issuer-library/1" || value["instance"] != digest([]byte(app.loc.State)) {
		t.Fatalf("health without the cookie: %d %s", health.Code, health.Body.String())
	}
}

// C03: the secret checks use crypto/subtle. Expected by reading launch.go: authorized and
// serveLaunch each call subtle.ConstantTimeCompare on the secret, and no == or != compares
// anything naming a secret except against a literal ("" or the compare's 1).
func TestSecretComparisonsAreConstantTime(t *testing.T) {
	files := token.NewFileSet()
	parsed, err := parser.ParseFile(files, "launch.go", nil, 0)
	if err != nil {
		t.Fatal(err)
	}
	source, _ := os.ReadFile("launch.go")
	text := func(node ast.Node) string {
		return string(source[files.Position(node.Pos()).Offset:files.Position(node.End()).Offset])
	}
	secret := regexp.MustCompile(`session|ticket|Value|Query`)
	want := map[string]string{"authorized": "app.session", "serveLaunch": "app.ticket"}
	for _, declaration := range parsed.Decls {
		function, ok := declaration.(*ast.FuncDecl)
		if !ok || want[function.Name.Name] == "" {
			continue
		}
		compared := false
		ast.Inspect(function.Body, func(node ast.Node) bool {
			switch node := node.(type) {
			case *ast.CallExpr:
				if text(node.Fun) == "subtle.ConstantTimeCompare" && strings.Contains(text(node), want[function.Name.Name]) {
					compared = true
				}
			case *ast.BinaryExpr:
				if node.Op != token.EQL && node.Op != token.NEQ {
					break
				}
				_, xLiteral := node.X.(*ast.BasicLit)
				_, yLiteral := node.Y.(*ast.BasicLit)
				if secret.MatchString(text(node)) && !xLiteral && !yLiteral {
					t.Errorf("%s: %s compares a secret without crypto/subtle", function.Name.Name, text(node))
				}
			}
			return true
		})
		if !compared {
			t.Errorf("%s does not compare %s with subtle.ConstantTimeCompare", function.Name.Name, want[function.Name.Name])
		}
		delete(want, function.Name.Name)
	}
	if len(want) != 0 {
		t.Fatalf("functions not found: %v", want)
	}
}

// C03 adversarial: cookies of another port or instance, a wrong or truncated value, the ticket in a
// Referer, cookie or header, a cross-site request carrying the valid cookie, path tricks on /files
// and on the two exempt paths, and a shadowing cookie. Expected by hand: 403 for each, except the
// last (the valid cookie is among those sent), and the ticket is still unspent at the end.
func TestRequestsWithoutThisLaunchsSessionAreRefused(t *testing.T) {
	app, _ := testApp(t)
	other, _ := testApp(t)
	other.host = "127.0.0.1:54322"
	ticket := app.ticket
	send := func(path string, change func(r *http.Request)) *httptest.ResponseRecorder {
		r := httptest.NewRequest("GET", "http://"+app.host+path, nil)
		change(r)
		w := httptest.NewRecorder()
		app.ServeHTTP(w, r)
		return w
	}
	cookie := func(name, value string) func(*http.Request) {
		return func(r *http.Request) { r.AddCookie(&http.Cookie{Name: name, Value: value}) }
	}
	name := app.cookieName()
	for label, change := range map[string]func(*http.Request){
		"other port's cookie":           cookie(other.cookieName(), other.session),
		"this value, other port's name": cookie(other.cookieName(), app.session),
		"other instance's value":        cookie(name, other.session),
		"name in another case":          cookie(strings.ToUpper(name), app.session),
		"one character changed":         cookie(name, app.session[:63]+map[bool]string{true: "1", false: "0"}[app.session[63] == '0']),
		"truncated value":               cookie(name, app.session[:32]),
		"value plus a byte":             cookie(name, app.session+"0"),
		"empty value":                   cookie(name, ""),
		"ticket as the cookie":          cookie(name, ticket),
		"ticket in a Referer":           func(r *http.Request) { r.Header.Set("Referer", "http://"+app.host+"/launch?ticket="+ticket) },
		"ticket in the custom header":   func(r *http.Request) { r.Header.Set("X-Issuer-Library", ticket) },
		"session in an Authorization":   func(r *http.Request) { r.Header.Set("Authorization", "Bearer "+app.session) },
	} {
		if w := send("/api/catalogue", change); w.Code != http.StatusForbidden {
			t.Errorf("%s: %d", label, w.Code)
		}
	}
	valid := cookie(name, app.session)
	for label, change := range map[string]func(*http.Request){
		"cross-site fetch":      func(r *http.Request) { valid(r); r.Header.Set("Sec-Fetch-Site", "cross-site") },
		"foreign Origin":        func(r *http.Request) { valid(r); r.Header.Set("Origin", "http://attacker.invalid") },
		"another port's Origin": func(r *http.Request) { valid(r); r.Header.Set("Origin", "http://127.0.0.1:54322") },
		"sandboxed Origin":      func(r *http.Request) { valid(r); r.Header.Set("Origin", "null") },
		"rebound Host":          func(r *http.Request) { valid(r); r.Host = "attacker.invalid:54321" },
		"localhost Host":        func(r *http.Request) { valid(r); r.Host = "localhost:54321" },
	} {
		if w := send("/api/catalogue", change); w.Code != http.StatusForbidden || w.Body.String() != "Local app requests only\n" {
			t.Errorf("%s with the valid cookie: %d %q", label, w.Code, w.Body.String())
		}
	}
	none := func(*http.Request) {}
	for _, path := range []string{
		"/files/../secret",
		"/files/%2e%2e/%2e%2e/etc/passwd",
		"/files//etc/passwd",
		"/files/deliverables/report/../../AGENTS.md",
		"/files/runs/case-a/CP-0.md?sha256=x&download=1",
		"/FILES/runs/case-a/CP-0.md",
		"/health/../api/catalogue",
		"/health/",
		"/launch/../api/catalogue",
		"/api/runs/list",
		"//api/catalogue",
	} {
		if w := send(path, none); w.Code != http.StatusForbidden || w.Body.String() != launcherOnly+"\n" {
			t.Errorf("%s without a cookie: %d %q", path, w.Code, w.Body.String())
		}
	}
	shadowed := func(r *http.Request) {
		r.Header.Set("Cookie", name+"=planted; "+other.cookieName()+"="+other.session+"; "+name+"="+app.session)
	}
	if w := send("/api/catalogue", shadowed); w.Code != 200 {
		t.Errorf("a planted cookie of the same name shadowed the valid one: %d", w.Code)
	}
	crossLaunch := httptest.NewRequest("GET", "http://"+app.host+"/launch?ticket="+ticket, nil)
	crossLaunch.Header.Set("Sec-Fetch-Site", "cross-site")
	w := httptest.NewRecorder()
	app.ServeHTTP(w, crossLaunch)
	if w.Code != http.StatusForbidden || w.Header().Get("Set-Cookie") != "" {
		t.Errorf("cross-site launch: %d %q", w.Code, w.Header().Get("Set-Cookie"))
	}
	if w := launchRequest(app, "GET", "?ticket="+ticket); w.Code != http.StatusSeeOther {
		t.Fatalf("the ticket was spent by a refused request: %d", w.Code)
	}
}

// C03 over real loopback: a HEAD is refused without the cookie and answers with no body with it;
// a HEAD to the launch path neither sets the cookie nor spends the ticket.
func TestHeadRequestsOverLoopback(t *testing.T) {
	app, _ := testApp(t)
	server := httptest.NewServer(app)
	t.Cleanup(server.Close)
	app.host = strings.TrimPrefix(server.URL, "http://")
	client := &http.Client{Transport: &http.Transport{Proxy: nil}, CheckRedirect: func(*http.Request, []*http.Request) error { return http.ErrUseLastResponse }}
	head := func(path string, signed bool) (*http.Response, string) {
		r, _ := http.NewRequest("HEAD", server.URL+path, nil)
		if signed {
			withSession(app, r)
		}
		response, err := client.Do(r)
		if err != nil {
			t.Fatal(err)
		}
		raw, _ := io.ReadAll(response.Body)
		response.Body.Close()
		return response, string(raw)
	}
	if response, _ := head("/api/catalogue", false); response.StatusCode != 403 {
		t.Errorf("HEAD without the cookie: %d", response.StatusCode)
	}
	if response, body := head("/api/catalogue", true); response.StatusCode != 200 || body != "" {
		t.Errorf("HEAD with the cookie: %d %q", response.StatusCode, body)
	}
	if response, _ := head("/files/runs/case-a/CP-0.md", false); response.StatusCode != 403 {
		t.Errorf("HEAD file without the cookie: %d", response.StatusCode)
	}
	ticket := app.ticket
	if response, _ := head("/launch?ticket="+ticket, false); response.StatusCode != 405 || response.Header.Get("Set-Cookie") != "" {
		t.Errorf("HEAD launch: %d %q", response.StatusCode, response.Header.Get("Set-Cookie"))
	}
	response, err := client.Get(server.URL + "/launch?ticket=" + ticket)
	if err != nil {
		t.Fatal(err)
	}
	response.Body.Close()
	if response.StatusCode != 303 || len(response.Cookies()) != 1 {
		t.Fatalf("GET launch after the HEAD: %d %v", response.StatusCode, response.Cookies())
	}
}

// C03: neither secret is in a log line, a response body, a header other than Set-Cookie, or a
// state or workspace file, across a launch exchange and every endpoint, refused or not.
func TestTheSecretsAppearOnlyInTheCookie(t *testing.T) {
	var logged strings.Builder
	var logMu sync.Mutex
	saved := log.Writer()
	log.SetOutput(writerFunc(func(p []byte) (int, error) { logMu.Lock(); defer logMu.Unlock(); return logged.Write(p) }))
	t.Cleanup(func() { log.SetOutput(saved) })
	app, root := testApp(t)
	ticket, session := app.ticket, app.session
	responses := []*httptest.ResponseRecorder{launchRequest(app, "GET", "?ticket="+ticket), launchRequest(app, "GET", "?ticket="+ticket), launchRequest(app, "HEAD", "?ticket=x")}
	for _, endpoint := range []string{"/", "/boot.js", "/health", "/api/catalogue", "/api/workspace", "/api/runs/list", "/files/deliverables/report/report.html?embedded=1", "/files/missing", "/nothing"} {
		responses = append(responses, call(app, "GET", endpoint, ""))
		r := httptest.NewRequest("GET", "http://"+app.host+endpoint, nil)
		w := httptest.NewRecorder()
		app.ServeHTTP(w, r)
		responses = append(responses, w)
	}
	for _, endpoint := range []string{"/api/refresh", "/api/runs/start", "/api/settings"} {
		responses = append(responses, call(app, "POST", endpoint, "{}"))
	}
	for i, w := range responses {
		if strings.Contains(w.Body.String(), ticket) || strings.Contains(w.Body.String(), session) {
			t.Errorf("response %d body carries a secret", i)
		}
		for key, values := range w.Header() {
			if key != "Set-Cookie" && (strings.Contains(strings.Join(values, " "), ticket) || strings.Contains(strings.Join(values, " "), session)) {
				t.Errorf("response %d header %s carries a secret", i, key)
			}
		}
	}
	if cookie := responses[0].Header().Get("Set-Cookie"); !strings.Contains(cookie, session) || strings.Contains(cookie, ticket) {
		t.Errorf("Set-Cookie %q", cookie)
	}
	logMu.Lock()
	text := logged.String()
	logMu.Unlock()
	if strings.Contains(text, ticket) || strings.Contains(text, session) {
		t.Errorf("a log line carries a secret: %q", text)
	}
	for _, folder := range []string{app.loc.State, root} {
		_ = filepath.WalkDir(folder, func(name string, entry os.DirEntry, err error) error {
			if err == nil && !entry.IsDir() {
				raw, _ := os.ReadFile(name)
				if strings.Contains(string(raw), ticket) || strings.Contains(string(raw), session) {
					t.Errorf("%s carries a secret", name)
				}
			}
			return nil
		})
	}
}

type writerFunc func([]byte) (int, error)

func (f writerFunc) Write(p []byte) (int, error) { return f(p) }

// freePort returns a loopback port that was free a moment ago.
func freePort(t *testing.T) int {
	t.Helper()
	listener, err := net.Listen("tcp4", "127.0.0.1:0")
	if err != nil {
		t.Fatal(err)
	}
	defer listener.Close()
	return listener.Addr().(*net.TCPAddr).Port
}

// runLauncher runs run() as a launch of the executable with arguments; flags and os.Args are
// restored afterwards.
func runLauncher(t *testing.T, arguments ...string) error {
	t.Helper()
	savedArgs, savedFlags := os.Args, flag.CommandLine
	defer func() { os.Args, flag.CommandLine = savedArgs, savedFlags }()
	flag.CommandLine = flag.NewFlagSet("issuer-library", flag.ContinueOnError)
	os.Args = append([]string{"issuer-library"}, arguments...)
	return run()
}

// captureStdout sends os.Stdout to a pipe until the returned function is called, which restores it
// and returns what was written.
func captureStdout(t *testing.T) func() string {
	t.Helper()
	reader, writer, err := os.Pipe()
	if err != nil {
		t.Fatal(err)
	}
	saved := os.Stdout
	os.Stdout = writer
	read := make(chan string)
	go func() { raw, _ := io.ReadAll(reader); read <- string(raw) }()
	return func() string {
		os.Stdout = saved
		writer.Close()
		return <-read
	}
}

// C03 relaunch, through run() as the executable runs it. Expected by hand: the first launch opens
// the browser once, at http://127.0.0.1:<port>/launch?ticket=<64 hex>, and prints only the address;
// a second launch (with and without --no-browser) finds its port taken, asks /health, sees its own
// instance and returns errAlreadyRunning without opening anything; with --workspace it returns the
// workspace message. The first instance keeps working, and library.log never holds a secret.
func TestRelaunchReportsTheRunningLibraryAndOpensNoWindow(t *testing.T) {
	saved, savedLog := launchBrowser, log.Writer()
	t.Cleanup(func() { launchBrowser = saved; log.SetOutput(savedLog) })
	opened := make(chan string, 4)
	launchBrowser = func(url string) error { opened <- url; return nil }
	state, workspace, port := t.TempDir(), t.TempDir(), freePort(t)
	arguments := []string{"-state-dir", state, "-port", strconv.Itoa(port)}
	stdout := captureStdout(t)
	restored := false
	defer func() {
		if !restored {
			stdout()
		}
	}()
	first := make(chan error, 1)
	go func() { first <- runLauncher(t, append(arguments, "-workspace", workspace)...) }()
	var launch string
	select {
	case launch = <-opened:
	case err := <-first:
		t.Fatalf("first launch ended: %v", err)
	case <-time.After(20 * time.Second):
		t.Fatal("the first launch opened no browser")
	}
	base := "http://127.0.0.1:" + strconv.Itoa(port)
	if !regexp.MustCompile(`^` + regexp.QuoteMeta(base) + `/launch\?ticket=[0-9a-f]{64}$`).MatchString(launch) {
		t.Fatalf("launch URL %q", launch)
	}
	ticket := strings.TrimPrefix(launch, base+"/launch?ticket=")
	client := &http.Client{Transport: &http.Transport{Proxy: nil}, CheckRedirect: func(*http.Request, []*http.Request) error { return http.ErrUseLastResponse }}
	response, err := client.Get(launch)
	if err != nil {
		t.Fatal(err)
	}
	response.Body.Close()
	if response.StatusCode != 303 || len(response.Cookies()) != 1 {
		t.Fatalf("exchange: %d %v", response.StatusCode, response.Cookies())
	}
	session := response.Cookies()[0]
	get := func() int {
		r, _ := http.NewRequest("GET", base+"/api/catalogue", nil)
		r.AddCookie(session)
		response, err := client.Do(r)
		if err != nil {
			t.Fatal(err)
		}
		response.Body.Close()
		return response.StatusCode
	}
	if get() != 200 {
		t.Fatal("the first instance refused its own session")
	}
	for _, extra := range [][]string{nil, {"-no-browser"}} {
		if err := runLauncher(t, append(arguments, extra...)...); !errors.Is(err, errAlreadyRunning) {
			t.Errorf("second launch %v: %v", extra, err)
		}
	}
	if err := runLauncher(t, append(arguments, "-workspace", t.TempDir())...); err == nil || !strings.Contains(err.Error(), "already running; change its workspace in Settings or quit it first") {
		t.Errorf("second launch with a workspace: %v", err)
	}
	select {
	case url := <-opened:
		t.Errorf("a second launch opened %q", url)
	default:
	}
	if get() != 200 {
		t.Error("a second launch disturbed the first instance's session")
	}
	quit, _ := http.NewRequest("POST", base+"/api/quit", strings.NewReader("{}"))
	quit.AddCookie(session)
	quit.Header.Set("X-Issuer-Library", "1")
	quit.Header.Set("Content-Type", "application/json")
	quit.Header.Set("Origin", base)
	if response, err := client.Do(quit); err != nil || response.StatusCode != 200 {
		t.Fatalf("quit: %v %v", response, err)
	}
	select {
	case err := <-first:
		if err != nil {
			t.Fatalf("first launch: %v", err)
		}
	case <-time.After(10 * time.Second):
		t.Fatal("the first instance did not stop")
	}
	printed := stdout()
	restored = true
	if printed != "Issuer Library: "+base+"\n" {
		t.Errorf("stdout %q", printed)
	}
	logged, _ := os.ReadFile(filepath.Join(state, "library.log"))
	if strings.Contains(string(logged), ticket) || strings.Contains(string(logged), session.Value) {
		t.Errorf("library.log carries a secret: %q", logged)
	}
	if strings.Count(string(logged), errAlreadyRunning.Error()) != 2 {
		t.Errorf("library.log does not record both refused launches: %q", logged)
	}
}

// C03 --no-browser: the launch link goes to standard output only, for whoever started the
// library; nothing is opened and library.log does not hold it.
func TestNoBrowserLaunchPrintsTheLinkOnStandardOutputOnly(t *testing.T) {
	saved, savedLog := launchBrowser, log.Writer()
	t.Cleanup(func() { launchBrowser = saved; log.SetOutput(savedLog) })
	launchBrowser = func(url string) error { t.Errorf("opened %q", url); return nil }
	state, port := t.TempDir(), freePort(t)
	reader, writer, err := os.Pipe()
	if err != nil {
		t.Fatal(err)
	}
	savedStdout := os.Stdout
	os.Stdout = writer
	first := make(chan error, 1)
	go func() {
		first <- runLauncher(t, "-state-dir", state, "-port", strconv.Itoa(port), "-no-browser", "-workspace", t.TempDir())
	}()
	line, readErr := bufio.NewReader(reader).ReadString('\n')
	os.Stdout = savedStdout
	writer.Close()
	base := "http://127.0.0.1:" + strconv.Itoa(port)
	if readErr != nil || !regexp.MustCompile(`^Issuer Library: `+regexp.QuoteMeta(base)+`/launch\?ticket=[0-9a-f]{64}\n$`).MatchString(line) {
		t.Fatalf("stdout %q (%v)", line, readErr)
	}
	launch := strings.TrimSpace(strings.TrimPrefix(line, "Issuer Library: "))
	client := &http.Client{Transport: &http.Transport{Proxy: nil}, CheckRedirect: func(*http.Request, []*http.Request) error { return http.ErrUseLastResponse }}
	response, err := client.Get(launch)
	if err != nil {
		t.Fatal(err)
	}
	response.Body.Close()
	if response.StatusCode != 303 || len(response.Cookies()) != 1 {
		t.Fatalf("exchange of the printed link: %d %v", response.StatusCode, response.Cookies())
	}
	if again, err := client.Get(launch); err != nil || again.StatusCode != 403 {
		t.Fatalf("the printed link worked twice: %v %v", again, err)
	}
	quit := func(signed bool) int {
		r, _ := http.NewRequest("POST", base+"/api/quit", strings.NewReader("{}"))
		r.Header.Set("X-Issuer-Library", "1")
		r.Header.Set("Content-Type", "application/json")
		r.Header.Set("Origin", base)
		if signed {
			r.AddCookie(response.Cookies()[0])
		}
		answer, err := client.Do(r)
		if err != nil {
			t.Fatal(err)
		}
		answer.Body.Close()
		return answer.StatusCode
	}
	if code := quit(false); code != 403 {
		t.Fatalf("quit without the session: %d", code)
	}
	if code := quit(true); code != 200 {
		t.Fatalf("quit with the session: %d", code)
	}
	select {
	case err := <-first:
		if err != nil {
			t.Fatalf("launch: %v", err)
		}
	case <-time.After(10 * time.Second):
		t.Fatal("the instance did not stop")
	}
	logged, _ := os.ReadFile(filepath.Join(state, "library.log"))
	if strings.Contains(string(logged), strings.TrimPrefix(launch, base+"/launch?ticket=")) {
		t.Errorf("library.log carries the ticket: %q", logged)
	}
}
