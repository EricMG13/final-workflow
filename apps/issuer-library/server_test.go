package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"net/http"
	"net/http/httptest"
	"os"
	"path/filepath"
	"strings"
	"sync"
	"testing"
	"time"
)

func testApp(t *testing.T) (*Application, string) {
	t.Helper()
	root, _ := fixture(t)
	addDelivery(t, root, "report", "case-a", "EX")
	app, err := newApplication(Locations{State: t.TempDir(), Documents: t.TempDir()}, root)
	if err != nil {
		t.Fatal(err)
	}
	app.host = "127.0.0.1:54321"
	app.stop = func() {}
	return app, root
}

// withSession adds this launch's session cookie, as the browser holds it after the launch.
func withSession(app *Application, r *http.Request) *http.Request {
	r.AddCookie(&http.Cookie{Name: app.cookieName(), Value: app.session})
	return r
}

// call sends a request as the app's own page does: with the session cookie and, for a POST, the
// custom header, JSON content type and the app's Origin.
func call(app *Application, method, endpoint, body string) *httptest.ResponseRecorder {
	r := withSession(app, httptest.NewRequest(method, "http://"+app.host+endpoint, strings.NewReader(body)))
	if method == "POST" {
		r.Header.Set("X-Issuer-Library", "1")
		r.Header.Set("Content-Type", "application/json")
		r.Header.Set("Origin", "http://"+app.host)
	}
	w := httptest.NewRecorder()
	app.ServeHTTP(w, r)
	return w
}

func TestLauncherDeliveryIsVerifiedAndPresentedLikeAnyDeliverable(t *testing.T) {
	app, root := testApp(t)
	folder := filepath.Join(root, "runs", "launched", "deliveries", "abc")
	if err := os.MkdirAll(folder, 0700); err != nil {
		t.Fatal(err)
	}
	// The launcher stamps deliveries with the run identity recorded in the run's workflow.json.
	if err := os.WriteFile(filepath.Join(root, "runs", "launched", "workflow.json"), []byte(`{"run":{"run_id":"nbg-2025-03-31-full-x","issuer_id":"nbg"}}`), 0600); err != nil {
		t.Fatal(err)
	}
	files := map[string]string{"report.html": "<html><body>Report</body></html>", "view.json": `{"run":{"run_id":"nbg-2025-03-31-full-x","issuer_id":"nbg","issuer_name":"Northbridge","as_of":"2025-03-31"}}`, "CP-1.md": "# CP-1\n"}
	hashes := map[string]string{}
	for name, text := range files {
		if err := os.WriteFile(filepath.Join(folder, name), []byte(text), 0600); err != nil {
			t.Fatal(err)
		}
		hashes[name] = digest([]byte(text))
	}
	if err := saveJSON(filepath.Join(folder, "delivery.json"), map[string]any{"files": hashes}); err != nil {
		t.Fatal(err)
	}
	if response := call(app, "POST", "/api/refresh", "{}"); response.Code != 200 {
		t.Fatal(response.Body.String())
	}
	found := false
	for _, run := range app.catalogue.Real {
		for _, artifact := range run.Artifacts {
			if run.ID == "launched" && artifact.Folder == "runs/launched/deliveries/abc" && artifact.Available {
				found = true
				shown := call(app, "GET", artifact.Href+"&embedded=1", "")
				if shown.Code != 200 || !strings.Contains(shown.Body.String(), "data-library-presentation") {
					t.Fatalf("report was not presented: %d", shown.Code)
				}
				saved := call(app, "GET", artifact.Href+"&download=1", "")
				if !strings.Contains(saved.Header().Get("Content-Disposition"), "abc.html") || strings.Contains(saved.Body.String(), "data-library-presentation") {
					t.Fatal("download must be the original report under its deliverable name")
				}
			}
		}
	}
	if !found {
		t.Fatal("launcher delivery missing from its run")
	}
	if err := os.WriteFile(filepath.Join(folder, "report.html"), []byte("changed"), 0600); err != nil {
		t.Fatal(err)
	}
	call(app, "POST", "/api/refresh", "{}")
	for _, issue := range app.catalogue.Issues {
		if strings.Contains(issue, "deliveries/abc") {
			return
		}
	}
	t.Fatal("a changed delivery must be reported")
}

func TestHTTPBoundaryAndChangedFile(t *testing.T) {
	app, root := testApp(t)
	for _, name := range []string{"/", "/screen.js", "/fonts/RedHatText-Regular.woff2", "/api/catalogue", "/files/deliverables/report/report.html"} {
		response := call(app, "GET", name, "")
		if response.Code != 200 {
			t.Fatalf("%s: %d %s", name, response.Code, response.Body.String())
		}
	}
	for _, name := range []string{"/files/AGENTS.md", "/files/../secret", "/legacy-catalog.json"} {
		if response := call(app, "GET", name, ""); response.Code != 404 {
			t.Fatalf("exposed %s", name)
		}
	}
	for _, header := range []struct{ key, value string }{{"Host", "attacker.invalid"}, {"Origin", "https://attacker.invalid"}, {"Sec-Fetch-Site", "cross-site"}} {
		r := withSession(app, httptest.NewRequest("GET", "http://"+app.host+"/api/catalogue", nil))
		if header.key == "Host" {
			r.Host = header.value
		} else {
			r.Header.Set(header.key, header.value)
		}
		w := httptest.NewRecorder()
		app.ServeHTTP(w, r)
		if w.Code != 403 {
			t.Fatal("cross-origin request admitted")
		}
	}
	r := withSession(app, httptest.NewRequest("POST", "http://"+app.host+"/api/quit", strings.NewReader("{}")))
	w := httptest.NewRecorder()
	app.ServeHTTP(w, r)
	if w.Code != 403 {
		t.Fatal("unprotected state change")
	}
	response := call(app, "GET", "/files/deliverables/report/report.html", "")
	if !strings.Contains(response.Header().Get("Content-Security-Policy"), "sandbox allow-scripts") || strings.Contains(response.Header().Get("Content-Security-Policy"), "allow-same-origin") {
		t.Fatal("report can reach application origin")
	}
	put(t, root, "deliverables/report/report.html", []byte("new unverified version"))
	if response = call(app, "GET", "/files/deliverables/report/report.html", ""); response.Code != 409 {
		t.Fatal("changed report served")
	}
}

func TestRefreshSettingsAndPolicy(t *testing.T) {
	app, root := testApp(t)
	put(t, root, "runs/added/CP-0.md", []byte("added"))
	response := call(app, "POST", "/api/refresh", "{}")
	var cat Catalogue
	if err := json.Unmarshal(response.Body.Bytes(), &cat); err != nil {
		t.Fatal(err)
	}
	if len(cat.Real) != 2 {
		t.Fatal("refresh missed new run")
	}
	other := t.TempDir()
	put(t, other, "runs/other/CP-0.md", []byte("other"))
	raw, _ := json.Marshal(Config{Workspace: other})
	if response = call(app, "POST", "/api/settings", string(raw)); response.Code != 200 {
		t.Fatal(response.Body.String())
	}
	if response = call(app, "GET", "/files/runs/case-a/CP-0.md", ""); response.Code != 404 {
		t.Fatal("old workspace file remains admitted")
	}
	reloaded, err := newApplication(app.loc, "")
	if err != nil || reloaded.config.Workspace != other {
		t.Fatal("settings did not persist")
	}
	app.locked = true
	if response = call(app, "POST", "/api/settings", string(raw)); response.Code != 403 {
		t.Fatal("policy did not lock settings")
	}
	if response = call(app, "POST", "/api/settings", `{"workspace":"relative"}`); response.Code == 200 {
		t.Fatal("relative path accepted")
	}
}

func TestPolicyPrecedenceAndNoSilentFallback(t *testing.T) {
	loc := Locations{State: t.TempDir(), Policy: filepath.Join(t.TempDir(), "settings.json"), Documents: t.TempDir()}
	if err := saveJSON(filepath.Join(loc.State, "settings.json"), Config{Workspace: t.TempDir()}); err != nil {
		t.Fatal(err)
	}
	managed := t.TempDir()
	if err := saveJSON(loc.Policy, Config{Workspace: managed}); err != nil {
		t.Fatal(err)
	}
	config, locked, err := loadConfig(loc)
	if err != nil || !locked || config.Workspace != managed {
		t.Fatal("policy lost precedence")
	}
	if _, err := newApplication(loc, t.TempDir()); err == nil {
		t.Fatal("CLI bypassed policy")
	}
	if err := os.WriteFile(loc.Policy, []byte("{"), 0600); err != nil {
		t.Fatal(err)
	}
	if _, _, err := loadConfig(loc); err == nil {
		t.Fatal("malformed IT config silently ignored")
	}
}

func TestConcurrentRefreshAndReaders(t *testing.T) {
	app, _ := testApp(t)
	var group sync.WaitGroup
	for i := 0; i < 20; i++ {
		group.Go(func() {
			response := call(app, "GET", "/api/catalogue", "")
			if response.Code != http.StatusOK {
				t.Errorf("reader: %d", response.Code)
			}
		})
		group.Go(func() {
			response := call(app, "POST", "/api/refresh", "{}")
			if response.Code != http.StatusOK {
				t.Errorf("refresh: %d", response.Code)
			}
		})
	}
	group.Wait()
}

func TestPinnedLinkCannotSilentlyOpenLaterVersion(t *testing.T) {
	app, root := testApp(t)
	old := app.catalogue.Real[0].Artifacts[0].Href
	// Replace and publish a new, internally valid bundle in the same directory.
	content := []byte("<!doctype html><p>Later revision</p>")
	put(t, root, "deliverables/report/report.html", content)
	raw, err := os.ReadFile(filepath.Join(root, "deliverables/report/delivery.json"))
	if err != nil {
		t.Fatal(err)
	}
	var record struct {
		Files map[string]string `json:"files"`
	}
	if err = json.Unmarshal(raw, &record); err != nil {
		t.Fatal(err)
	}
	record.Files["report.html"] = digest(content)
	putJSON(t, root, "deliverables/report/delivery.json", record)
	call(app, "POST", "/api/refresh", "{}")
	if response := call(app, "GET", old, ""); response.Code != 409 {
		t.Fatal("old screen opened new report bytes without noticing")
	}
}

func TestReportRangeRequests(t *testing.T) {
	app, _ := testApp(t)
	request := withSession(app, httptest.NewRequest("GET", "http://"+app.host+"/files/deliverables/report/report.html", nil))
	request.Header.Set("Range", "bytes=0-14")
	response := httptest.NewRecorder()
	app.ServeHTTP(response, request)
	if response.Code != 206 || response.Body.String() != "<!doctype html>" {
		t.Fatalf("range contract failed: %d %s", response.Code, response.Body.String())
	}
}

type mutateOnServe struct {
	*httptest.ResponseRecorder
	once   sync.Once
	mutate func()
}

func (w *mutateOnServe) Header() http.Header {
	header := w.ResponseRecorder.Header()
	if header.Get("Content-Type") == "text/html; charset=utf-8" {
		w.once.Do(w.mutate)
	}
	return header
}
func TestResponseUsesTheBytesThatWereVerified(t *testing.T) {
	app, root := testApp(t)
	file := filepath.Join(root, "deliverables/report/report.html")
	original, err := os.ReadFile(file)
	if err != nil {
		t.Fatal(err)
	}
	changed := []byte(strings.Repeat("X", len(original)))
	response := &mutateOnServe{ResponseRecorder: httptest.NewRecorder(), mutate: func() {
		if err := os.WriteFile(file, changed, 0600); err != nil {
			t.Fatal(err)
		}
	}}
	request := withSession(app, httptest.NewRequest("GET", "http://"+app.host+"/files/deliverables/report/report.html", nil))
	app.ServeHTTP(response, request)
	if response.Code != 200 || response.Body.String() != string(original) {
		t.Fatal("served different bytes than the verified snapshot")
	}
}

func TestEmbeddedPresentationPreservesRetainedAndExportedReportBytes(t *testing.T) {
	app, root := testApp(t)
	name := "/files/deliverables/report/report.html"
	original, err := os.ReadFile(filepath.Join(root, "deliverables/report/report.html"))
	if err != nil {
		t.Fatal(err)
	}
	for _, query := range []string{"?embedded=1", "?download=1"} {
		response := call(app, "GET", name+query, "")
		if response.Code != 200 {
			t.Fatal(response.Body.String())
		}
		if query == "?embedded=1" {
			body := response.Body.Bytes()
			start := bytes.Index(body, []byte("<style data-library-presentation>"))
			end := bytes.LastIndex(body, []byte("</script>")) + len("</script>")
			if start < 0 || end < start {
				t.Fatal("embedded presentation is missing")
			}
			symbol, err := resources.ReadFile("web/brand/symbol.svg")
			if err != nil || !bytes.Contains(body, []byte("data:image/svg+xml;base64,"+base64.StdEncoding.EncodeToString(symbol))) {
				t.Fatal("embedded report does not carry the supplied offline symbol")
			}
			restored := append(append([]byte{}, body[:start]...), body[end:]...)
			if !bytes.Equal(restored, original) {
				t.Fatal("embedded view lost original content or its scoped presentation")
			}
		} else if response.Body.String() != string(original) {
			t.Fatal("HTML export changed original bytes")
		}
		policy := response.Header().Get("Content-Security-Policy")
		if strings.Contains(policy, "allow-same-origin") || !strings.Contains(policy, "connect-src 'none'") {
			t.Fatal("report lost isolation")
		}
		if query == "?embedded=1" && !strings.Contains(policy, "frame-ancestors http://"+app.host) {
			t.Fatal("trusted application cannot embed report")
		}
		if query == "?download=1" && !strings.HasPrefix(response.Header().Get("Content-Disposition"), "attachment;") {
			t.Fatal("HTML export is not a download")
		}
	}
	retained, err := os.ReadFile(filepath.Join(root, "deliverables/report/report.html"))
	if err != nil || !bytes.Equal(retained, original) {
		t.Fatal("presentation mutated the retained report")
	}
	combined := call(app, "GET", name+"?embedded=1&download=1", "")
	if !bytes.Equal(combined.Body.Bytes(), original) {
		t.Fatal("embedded export did not return original bytes")
	}
	response := call(app, "GET", name, "")
	if !strings.Contains(response.Header().Get("Content-Security-Policy"), "frame-ancestors 'none'") {
		t.Fatal("standalone report embedding policy changed")
	}
	response = call(app, "GET", "/", "")
	if !strings.Contains(response.Header().Get("Content-Security-Policy"), "frame-src 'self'") {
		t.Fatal("app cannot display local reports")
	}
	request := withSession(app, httptest.NewRequest("GET", "http://"+app.host+name+"?embedded=1", nil))
	request.Header.Set("Origin", "null")
	result := httptest.NewRecorder()
	app.ServeHTTP(result, request)
	if result.Code != 403 {
		t.Fatal("sandboxed child can access the application origin")
	}
}

func TestReportPresentationKeepsFragmentsAndOriginalStorage(t *testing.T) {
	for _, original := range []string{"<p>Original fragment</p>", "<HTML><BODY>Original report</BODY></HTML>"} {
		raw := []byte(original)
		result := reportPresentation(raw)
		if !bytes.Contains(result, []byte("data-library-presentation")) {
			t.Fatal("missing presentation")
		}
		if strings.Contains(original, "</BODY>") && !bytes.HasSuffix(result, []byte("</BODY></HTML>")) {
			t.Fatal("insertion lost the original document ending")
		}
		result[0] = 'X'
		if string(raw) != original {
			t.Fatal("presentation aliases original report storage")
		}
	}
}

func TestRunListAndStatusCarryReviewAndProgress(t *testing.T) {
	app, root := testApp(t)
	a, b := "web-"+strings.Repeat("a", 32), "web-"+strings.Repeat("b", 32)
	files := map[string]string{
		filepath.Join("intake", a, "status.json"): `{"state":"running","message":"Working"}`,
		filepath.Join("intake", a, "review.json"): `{"review_id":"x","issuer":"Northbridge Group","pathway":"covenant_refinancing","as_of":"2025-03-31","modules":["CP-0","CP-1"],"module_details":[{"id":"CP-0","title":"Source readiness","purpose":"p"}],"cap_usd":"10.00"}`,
		filepath.Join("runs", a, "progress.json"): `{"module":"CP-1","step":"started","spent_usd":"0.10"}`,
		filepath.Join("intake", b, "status.json"): `{"state":"stopped","message":"Halted"}`,
	}
	for name, text := range files {
		path := filepath.Join(root, name)
		if err := os.MkdirAll(filepath.Dir(path), 0700); err != nil {
			t.Fatal(err)
		}
		if err := os.WriteFile(path, []byte(text), 0600); err != nil {
			t.Fatal(err)
		}
	}
	checkA := func(row map[string]any) {
		t.Helper()
		if row["issuer"] != "Northbridge Group" || row["pathway"] != "covenant_refinancing" || row["as_of"] != "2025-03-31" {
			t.Fatalf("review fields: %v", row)
		}
		if len(row["modules"].([]any)) != 2 || len(row["module_details"].([]any)) != 1 {
			t.Fatalf("module fields: %v", row)
		}
		if row["progress"].(map[string]any)["module"] != "CP-1" || row["run_available"] != true {
			t.Fatalf("progress or run: %v", row)
		}
		for _, key := range []string{"cap_usd", "review_id"} {
			if _, present := row[key]; present {
				t.Fatalf("%s leaked: %v", key, row)
			}
		}
	}
	list := call(app, "GET", "/api/runs/list", "")
	var rows []map[string]any
	if list.Code != 200 || json.Unmarshal(list.Body.Bytes(), &rows) != nil || len(rows) != 2 {
		t.Fatalf("list: %d %s", list.Code, list.Body.String())
	}
	for _, row := range rows {
		switch row["id"] {
		case a:
			checkA(row)
		case b:
			if _, present := row["issuer"]; present || row["run_available"] != false {
				t.Fatalf("b row: %v", row)
			}
		default:
			t.Fatalf("unexpected row: %v", row)
		}
	}
	status := call(app, "GET", "/api/runs/status?id="+a, "")
	var row map[string]any
	if status.Code != 200 || json.Unmarshal(status.Body.Bytes(), &row) != nil {
		t.Fatalf("status: %d %s", status.Code, status.Body.String())
	}
	checkA(row)
}

func TestEmbeddedModelKeepsItsBytesAndSandbox(t *testing.T) {
	app, root := testApp(t)
	model := addModelDelivery(t, root, "m-1", false)
	if response := call(app, "POST", "/api/refresh", "{}"); response.Code != 200 {
		t.Fatal(response.Body.String())
	}
	artifact := findArtifact(app.catalogue, "deliverables/m-1")
	if artifact == nil || !artifact.Available {
		t.Fatalf("model not available: %+v", artifact)
	}
	response := call(app, "GET", artifact.Href+"&embedded=1", "")
	if response.Code != 200 || !bytes.Equal(response.Body.Bytes(), model) {
		t.Fatalf("model bytes changed: %d %q", response.Code, response.Body.String())
	}
	if bytes.Contains(response.Body.Bytes(), []byte("data-library-presentation")) {
		t.Fatal("report adapter was added to a model")
	}
	csp := response.Header().Get("Content-Security-Policy")
	if !strings.HasPrefix(csp, "sandbox allow-scripts allow-downloads;") || !strings.Contains(csp, "frame-ancestors http://"+app.host) {
		t.Fatalf("csp: %s", csp)
	}
}

// The splice point must be an offset into the original bytes: Unicode lower-casing
// changes lengths (U+0130, Kelvin sign, U+023A, invalid UTF-8), so it must not be used.
func TestReportPresentationSplicesBeforeTheFinalBodyTagInTheOriginalBytes(t *testing.T) {
	tail := "<script>render()</script>\n<!-- font licence -->\n</BODY></html>"
	invalid := append(append([]byte("<html><body><p>"), bytes.Repeat([]byte{0xff}, 40)...), []byte("</p>"+tail)...)
	cases := map[string][]byte{
		"ascii":        []byte("<html><body><p>Issuer</p>" + tail),
		"turkish I":    []byte("<html><body><p>" + strings.Repeat("T\u00fcrkiye \u0130\u015f Bankas\u0131 ", 6) + "</p>" + tail),
		"kelvin":       []byte("<html><body><p>300 \u212a</p>" + tail),
		"U+023A":       []byte("<html><body><p>" + strings.Repeat("\u023a", 40) + "</p>" + tail),
		"invalid utf8": invalid,
		"mixed case":   []byte("<html><body><p>x</p></BoDy></html>"),
		"early body":   []byte("</body><p>İİİİİ</p>"),
		"no body":      []byte("<p>\u0130\u0130 \xff\xff plain fragment</p>"),
	}
	for label, original := range cases {
		out := reportPresentation(original)
		start := bytes.Index(out, []byte("<style data-library-presentation>"))
		end := bytes.LastIndex(out, []byte("</script>")) + len("</script>")
		want := len(original)
		for i := len(original) - 7; i >= 0; i-- {
			if strings.EqualFold(string(original[i:i+7]), "</body>") && original[i] == '<' {
				want = i
				break
			}
		}
		if start != want || !bytes.Equal(out[:start], original[:want]) || !bytes.Equal(out[end:], original[want:]) {
			t.Errorf("%s: block at %d, want %d; after block %q", label, start, want, out[end:min(end+20, len(out))])
		}
	}
}

// Review (S18 medium, A02/C06): boundary inputs for the splice offset. Expected values are
// written out by hand; "end" means len(input), i.e. the adapter is appended.
func TestReviewLastBodyCloseBoundaries(t *testing.T) {
	for _, c := range []struct {
		html string
		want int // -1 means len(html)
	}{
		{"", -1},                       // empty: no tag, no panic
		{"</body", -1},                 // 6 bytes, shorter than the tag
		{"</body>", 0},                 // tag is the whole input
		{"x</BODY>", 1},                // upper case at the very end
		{"<p>İ</bOdY></html>", 5},      // U+0130 is 2 bytes and stays 2 bytes in the offset
		{"</body ></html>", -1},        // whitespace inside the tag is not matched: appended
		{"</body\n></html>", -1},       // likewise for a newline
		{"<</body>>", 1},               // the scan starts at a '<' preceded by another '<'
		{"</body></body>", 7},          // the final tag wins
		{"\xff\xff\xff</body>\xff", 3}, // invalid UTF-8 does not move the offset
		{"</bödy></html>", -1},         // a non-ASCII lookalike never matches
		{"</Kody></html>", -1},         // Kelvin sign is not 'b' (nor 'k') here
		{"<body>x</bodyx></html>", -1}, // a longer name is not the tag
		{"<body>x</bod></html>", -1},   // nor a shorter one
	} {
		want := c.want
		if want < 0 {
			want = len(c.html)
		}
		if got := lastBodyClose([]byte(c.html)); got != want {
			t.Errorf("%q: %d, want %d", c.html, got, want)
		}
		// Splicing never drops or reorders an original byte.
		out := reportPresentation([]byte(c.html))
		start := bytes.Index(out, []byte("<style data-library-presentation>"))
		block := len(out) - len(c.html)
		if start != want || string(out[:start])+string(out[start+block:]) != c.html {
			t.Errorf("%q: spliced at %d (want %d) or bytes changed", c.html, start, want)
		}
	}
}

// Differential check against an oracle built differently from production: a same-length
// ASCII-lowered copy searched with bytes.LastIndex. Expected: identical offsets on 50,000
// random strings over an alphabet of tag fragments, length-changing runes and invalid bytes.
func TestReviewLastBodyCloseMatchesAnASCIILoweredOracle(t *testing.T) {
	oracle := func(html []byte) int {
		low := make([]byte, len(html))
		for i, c := range html {
			if 'A' <= c && c <= 'Z' {
				c += 'a' - 'A'
			}
			low[i] = c
		}
		if i := bytes.LastIndex(low, []byte("</body>")); i >= 0 {
			return i
		}
		return len(html)
	}
	alphabet := []string{"<", "/", "b", "B", "o", "O", "d", "D", "y", "Y", ">", " ", "</body>", "</BODY>", "</bOdY", "İ", "K", "Ⱥ", "\xff", "\xc4"}
	state := uint64(1)
	next := func(n int) int { // xorshift: deterministic, no shared RNG state
		state ^= state << 13
		state ^= state >> 7
		state ^= state << 17
		return int(state % uint64(n))
	}
	for n := 0; n < 50000; n++ {
		var s []byte
		for k := next(12); k > 0; k-- {
			s = append(s, alphabet[next(len(alphabet))]...)
		}
		if got, want := lastBodyClose(s), oracle(s); got != want {
			t.Fatalf("%q: %d, oracle %d", s, got, want)
		}
	}
}

// Review (S18 medium, A02/C06): the reported crash through the HTTP path. A delivered report
// with 40 x U+023A, invalid UTF-8 and a trailing licence comment. Expected: 200, adapter
// directly before the final </body> (outside the comment), every guard header unchanged,
// and the download still the exact original bytes.
func TestReviewEmbeddedGlyphReportOverHTTP(t *testing.T) {
	app, root := testApp(t)
	report := []byte("<!doctype html><html><body><p>" + strings.Repeat("Ⱥ", 40) + "\xff\xfe İstanbul</p><script>render()</script>\n<!-- font licence -->\n</body></html>")
	view := []byte(`{"run":{"run_id":"case-a","issuer_id":"EX","issuer_name":"Example Industries","as_of":"2024-12-31"}}`)
	put(t, root, "deliverables/glyph/report.html", report)
	put(t, root, "deliverables/glyph/view.json", view)
	putJSON(t, root, "deliverables/glyph/delivery.json", map[string]any{"files": map[string]string{"report.html": digest(report), "view.json": digest(view)}})
	if response := call(app, "POST", "/api/refresh", "{}"); response.Code != 200 {
		t.Fatal(response.Body.String())
	}
	href := ""
	for _, run := range app.catalogue.Real {
		for _, artifact := range run.Artifacts {
			if artifact.Folder == "deliverables/glyph" && artifact.Available {
				href = artifact.Href
			}
		}
	}
	if href == "" {
		t.Fatalf("glyph delivery not available: %v", app.catalogue.Issues)
	}
	shown := call(app, "GET", href+"&embedded=1", "")
	body := shown.Body.Bytes()
	at := bytes.Index(body, []byte("<style data-library-presentation>"))
	if shown.Code != 200 || at < 0 || !bytes.HasSuffix(body, []byte("</script></body></html>")) || !bytes.HasPrefix(body, report[:bytes.LastIndex(report, []byte("</body>"))]) {
		t.Fatalf("embedded: %d, adapter at %d, tail %q", shown.Code, at, body[max(0, len(body)-40):])
	}
	csp := shown.Header().Get("Content-Security-Policy")
	if !strings.HasPrefix(csp, "sandbox allow-scripts allow-downloads;") || !strings.Contains(csp, "connect-src 'none'") || !strings.HasSuffix(csp, "frame-ancestors http://"+app.host) {
		t.Fatalf("CSP changed: %q", csp)
	}
	saved := call(app, "GET", href+"&download=1", "")
	if !bytes.Equal(saved.Body.Bytes(), report) || !strings.HasSuffix(saved.Header().Get("Content-Security-Policy"), "frame-ancestors 'none'") {
		t.Fatal("download must be the exact original with frame-ancestors 'none'")
	}
}

// A09: Windows PowerShell 5.1 writes "UTF8" files with a byte order mark. One leading BOM is
// accepted in the managed and the per-user settings; anything else invalid still fails closed.
func TestSettingsAcceptOneLeadingByteOrderMark(t *testing.T) {
	bom := "\xef\xbb\xbf"
	workspace := t.TempDir()
	valid := `{"workspace": ` + jsonQuote(workspace) + `}`
	for _, c := range []struct {
		name, content string
		ok            bool
	}{
		{"bom", bom + valid, true},
		{"plain", valid, true},
		{"bom-only", bom, false},
		{"double-bom", bom + bom + valid, false},
		{"bom-then-garbage", bom + "{", false},
		{"bom-relative", bom + `{"workspace": "relative"}`, false},
		{"utf16-bom", "\xff\xfe" + valid, false},
	} {
		for _, managed := range []bool{true, false} {
			loc := Locations{State: t.TempDir(), Policy: filepath.Join(t.TempDir(), "settings.json"), Documents: t.TempDir()}
			file := filepath.Join(loc.State, "settings.json")
			if managed {
				file = loc.Policy
			}
			if err := os.WriteFile(file, []byte(c.content), 0600); err != nil {
				t.Fatal(err)
			}
			config, locked, err := loadConfig(loc)
			if (err == nil) != c.ok {
				t.Errorf("%s (managed=%v): err=%v, want ok=%v", c.name, managed, err, c.ok)
				continue
			}
			if c.ok && (config.Workspace != workspace || locked != managed) {
				t.Errorf("%s (managed=%v): config=%+v locked=%v", c.name, managed, config, locked)
			}
		}
	}
}

func jsonQuote(value string) string {
	raw, _ := json.Marshal(value)
	return string(raw)
}

// stalledWriter is a client that never reads: Write blocks until release is closed.
type stalledWriter struct {
	header  http.Header
	writing chan struct{}
	release chan struct{}
	once    sync.Once
}

func (w *stalledWriter) Header() http.Header { return w.header }
func (w *stalledWriter) WriteHeader(int)     {}
func (w *stalledWriter) Write(p []byte) (int, error) {
	w.once.Do(func() { close(w.writing) })
	<-w.release
	return len(p), nil
}

// C07: no response is written while the catalogue lock is held, so a stalled client cannot
// stop the refresh ticker (a writer) and with it every request that reads the catalogue.
func TestStalledClientDoesNotHoldTheCatalogueLock(t *testing.T) {
	app, root := testApp(t)
	put(t, root, "runs/case-a/big.txt", bytes.Repeat([]byte("a"), 1<<20))
	call(app, "POST", "/api/refresh", "{}")
	pinned := app.catalogue.Real[0].Artifacts[0].Href
	for _, c := range []struct{ method, endpoint string }{
		{"GET", "/files/runs/case-a/big.txt"},
		{"GET", pinned + "&embedded=1"},
		{"GET", "/api/catalogue"},
		{"POST", "/api/refresh"},
	} {
		request := withSession(app, httptest.NewRequest(c.method, "http://"+app.host+c.endpoint, strings.NewReader("{}")))
		request.Header.Set("X-Issuer-Library", "1")
		request.Header.Set("Content-Type", "application/json")
		w := &stalledWriter{header: http.Header{}, writing: make(chan struct{}), release: make(chan struct{})}
		served := make(chan struct{})
		go func() { app.ServeHTTP(w, request); close(served) }()
		select {
		case <-w.writing:
		case <-served:
			t.Fatalf("%s %s finished without writing", c.method, c.endpoint)
		}
		locked := make(chan struct{})
		go func() { app.mu.Lock(); close(locked); app.mu.Unlock() }()
		select {
		case <-locked:
		case <-time.After(2 * time.Second):
			t.Errorf("%s %s: the catalogue lock is held while the response is written", c.method, c.endpoint)
		}
		close(w.release)
		<-served
		<-locked
	}
}

// blockDiscovery makes discovery of workspace wait until release is closed; entered is closed
// when it starts. Other workspaces are discovered as usual.
func blockDiscovery(t *testing.T, workspace string) (entered, release chan struct{}) {
	t.Helper()
	entered, release = make(chan struct{}), make(chan struct{})
	saved := discoverWorkspace.Load()
	var once sync.Once
	hold := func(folder string, seeds Catalogue) Catalogue {
		if folder == workspace {
			once.Do(func() { close(entered) })
			<-release
		}
		return (*saved)(folder, seeds)
	}
	discoverWorkspace.Store(&hold)
	t.Cleanup(func() { discoverWorkspace.Store(saved) })
	return entered, release
}

func lockWithin(t *testing.T, app *Application, what string) {
	t.Helper()
	locked := make(chan struct{})
	go func() { app.mu.Lock(); close(locked); app.mu.Unlock() }()
	select {
	case <-locked:
	case <-time.After(2 * time.Second):
		t.Fatalf("%s holds the catalogue lock", what)
	}
}

// C11: discovery hashes every pinned file, so it runs without the catalogue lock; requests are
// served from the previous catalogue meanwhile and only the swap is locked.
func TestRefreshDiscoversWithoutHoldingTheCatalogueLock(t *testing.T) {
	app, root := testApp(t)
	put(t, root, "runs/added/CP-0.md", []byte("added"))
	entered, release := blockDiscovery(t, root)
	done := make(chan *httptest.ResponseRecorder)
	go func() { done <- call(app, "POST", "/api/refresh", "{}") }()
	<-entered
	lockWithin(t, app, "a refresh in discovery")
	var during Catalogue
	if response := call(app, "GET", "/api/catalogue", ""); response.Code != 200 || json.Unmarshal(response.Body.Bytes(), &during) != nil || len(during.Real) != 1 {
		t.Fatalf("catalogue during discovery: %d %s", response.Code, response.Body.String())
	}
	if response := call(app, "GET", "/files/runs/case-a/CP-0.md", ""); response.Code != 200 {
		t.Fatalf("file during discovery: %d", response.Code)
	}
	close(release)
	var after Catalogue
	if response := <-done; json.Unmarshal(response.Body.Bytes(), &after) != nil || len(after.Real) != 2 {
		t.Fatalf("refresh result: %s", response.Body.String())
	}
}

// C11: a workspace switch waits for a refresh already discovering the old workspace, and the
// old workspace's catalogue never replaces the new one; the switch itself discovers unlocked.
func TestWorkspaceSwitchDuringARefreshKeepsTheNewWorkspace(t *testing.T) {
	app, root := testApp(t)
	other := t.TempDir()
	put(t, other, "runs/other/CP-0.md", []byte("other"))
	oldEntered, oldRelease := blockDiscovery(t, root)
	refreshed := make(chan struct{})
	go func() { call(app, "POST", "/api/refresh", "{}"); close(refreshed) }()
	<-oldEntered
	newEntered, newRelease := blockDiscovery(t, other)
	switched := make(chan *httptest.ResponseRecorder)
	raw, _ := json.Marshal(Config{Workspace: other})
	go func() { switched <- call(app, "POST", "/api/settings", string(raw)) }()
	close(oldRelease)
	<-refreshed
	<-newEntered
	lockWithin(t, app, "a workspace switch in discovery")
	close(newRelease)
	if response := <-switched; response.Code != 200 {
		t.Fatalf("switch: %d %s", response.Code, response.Body.String())
	}
	app.mu.RLock()
	workspace, catalogueWorkspace := app.config.Workspace, app.catalogue.Workspace
	app.mu.RUnlock()
	if workspace != other || catalogueWorkspace != other {
		t.Fatalf("config %s, catalogue %s; want %s", workspace, catalogueWorkspace, other)
	}
	if response := call(app, "GET", "/files/runs/case-a/CP-0.md", ""); response.Code != 404 {
		t.Fatalf("old workspace file still admitted: %d", response.Code)
	}
}

// countingEngine is fakeEngine whose store script appends one line to the returned counter file
// per run, and fails while failFile exists.
func countingEngine(t *testing.T) (Engine, string, string) {
	t.Helper()
	engine := fakeEngine(t)
	counter := filepath.Join(t.TempDir(), "store-runs.txt")
	failFile := filepath.Join(t.TempDir(), "fail")
	script := fmt.Sprintf(`import json,sys,os,time
with open(%q,'a') as s: s.write('run\n')
time.sleep(.2)
if os.path.exists(%q): sys.exit(3)
print(json.dumps({'ok':True}))
`, counter, failFile)
	if err := os.WriteFile(filepath.Join(filepath.Dir(engine.Script), "store.py"), []byte(script), 0600); err != nil {
		t.Fatal(err)
	}
	return engine, counter, failFile
}

func storeRuns(t *testing.T, counter string) int {
	t.Helper()
	raw, err := os.ReadFile(counter)
	if os.IsNotExist(err) {
		return 0
	}
	if err != nil {
		t.Fatal(err)
	}
	return strings.Count(string(raw), "run\n")
}

func TestWorkspaceStoreRunsOnceUntilAFileChanges(t *testing.T) {
	app, root := testApp(t)
	var counter string
	app.engine, counter, _ = countingEngine(t)
	for range 2 {
		if r := call(app, "GET", "/api/workspace", ""); r.Code != 200 {
			t.Fatalf("workspace: %d", r.Code)
		}
	}
	if n := storeRuns(t, counter); n != 1 {
		t.Fatalf("two reads ran the store %d times, want 1", n)
	}
	put(t, root, "runs/case-a/extra-note.md", []byte("a longer file than before"))
	call(app, "GET", "/api/workspace", "")
	if n := storeRuns(t, counter); n != 2 {
		t.Fatalf("after a file change the store ran %d times, want 2", n)
	}
}

func TestCatalogueRebuildAloneDoesNotRerunTheStore(t *testing.T) {
	app, _ := testApp(t)
	var counter string
	app.engine, counter, _ = countingEngine(t)
	call(app, "GET", "/api/workspace", "")
	app.mu.Lock()
	app.catalogue.BuiltAt = "2001-01-01T00:00:00Z"
	app.mu.Unlock()
	call(app, "GET", "/api/workspace", "")
	app.refresh()
	call(app, "GET", "/api/workspace", "")
	if n := storeRuns(t, counter); n != 1 {
		t.Fatalf("a rebuild that changed only BuiltAt ran the store %d times, want 1", n)
	}
}

func TestConcurrentWorkspaceReadsShareOneStore(t *testing.T) {
	app, _ := testApp(t)
	var counter string
	app.engine, counter, _ = countingEngine(t)
	var group sync.WaitGroup
	for range 8 {
		group.Go(func() {
			if r := call(app, "GET", "/api/workspace", ""); r.Code != 200 {
				t.Errorf("workspace: %d", r.Code)
			}
		})
	}
	group.Wait()
	if n := storeRuns(t, counter); n != 1 {
		t.Fatalf("8 parallel reads ran the store %d times, want 1", n)
	}
}

func TestRefreshClearsTheWorkspaceCache(t *testing.T) {
	app, _ := testApp(t)
	var counter string
	app.engine, counter, _ = countingEngine(t)
	call(app, "GET", "/api/workspace", "")
	call(app, "POST", "/api/refresh", "{}")
	call(app, "GET", "/api/workspace", "")
	if n := storeRuns(t, counter); n != 2 {
		t.Fatalf("a read after /api/refresh ran the store %d times in total, want 2", n)
	}
}

func TestAFailedStoreIsNotCached(t *testing.T) {
	app, _ := testApp(t)
	var counter, failFile string
	app.engine, counter, failFile = countingEngine(t)
	if err := os.WriteFile(failFile, nil, 0600); err != nil {
		t.Fatal(err)
	}
	if r := call(app, "GET", "/api/workspace", ""); r.Code != http.StatusServiceUnavailable {
		t.Fatalf("failing store: %d", r.Code)
	}
	if err := os.Remove(failFile); err != nil {
		t.Fatal(err)
	}
	if r := call(app, "GET", "/api/workspace", ""); r.Code != 200 {
		t.Fatalf("after the store recovered: %d", r.Code)
	}
	call(app, "GET", "/api/workspace", "")
	if n := storeRuns(t, counter); n != 2 {
		t.Fatalf("store ran %d times, want 2 (failure, then one success, then a hit)", n)
	}
}
