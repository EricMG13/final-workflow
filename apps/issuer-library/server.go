package main

import (
	"bytes"
	"embed"
	"encoding/json"
	"fmt"
	"io/fs"
	"log"
	"mime"
	"net/http"
	"os"
	"path"
	"path/filepath"
	"strings"
	"sync"
	"sync/atomic"
	"time"
)

//go:embed web/*.html web/*.css web/*.js web/legacy-catalog.json web/fonts/* web/brand/* web/icons/*
var resources embed.FS

type Application struct {
	engine     Engine
	activeJobs map[string]bool
	reviews    int  // reviews in flight, each writing into the workspace it read; guarded by mu
	quitting   bool // set when the library agrees to quit for a relaunch; guarded by mu
	mu         sync.RWMutex
	refreshing sync.Mutex // serialises catalogue rebuilds and workspace switches; taken before mu
	loc        Locations
	config     Config
	locked     bool
	seed       Catalogue
	catalogue  Catalogue
	host       string
	stop       func()
	launch     sync.Mutex // guards ticket
	ticket     string     // one-time launch ticket, in memory only; empty once exchanged or expired
	expires    time.Time  // when the ticket stops working; fixed at start
	session    string     // this launch's session cookie value, in memory only; fixed at start
	storeCache storeCache
	watched    atomic.Int64 // app.now().UnixNano() of the last GET /api/runs/list; zero when never
	finished   atomic.Int64 // app.now().UnixNano() when the latest run finished; see tabWatching
	sawMu      sync.Mutex
	sawFinish  map[string]bool // run ids a notifying tab's poll served in a non-running state; see finishJob
	now        func() time.Time
	pause      func(time.Duration)            // how tabWatching waits between looks; tests move a fake clock
	notifier   func(title, body string) error // shows the native run notice; a no-op in tests
	onFinished func(id string)                // called when finishJob returns; nil outside tests
}

// storeCache holds the last workspace store output. mu is held while the store runs, so
// concurrent requests share one run; it is never taken with app.mu or app.refreshing held, and
// neither is taken while it is held, so the three cannot deadlock. state guards the entry and the
// generation and is held only for a field read or write, so clear never waits for a run: it bumps
// the generation, and a run that began before the bump does not store its body.
type storeCache struct {
	mu         sync.Mutex
	state      sync.Mutex
	generation uint64
	key        string
	body       []byte
}

func (cache *storeCache) clear() {
	cache.state.Lock()
	cache.generation++
	cache.key, cache.body = "", nil
	cache.state.Unlock()
}

// current is the generation now; a run records it before it reads anything.
func (cache *storeCache) current() uint64 {
	cache.state.Lock()
	defer cache.state.Unlock()
	return cache.generation
}

// lookup returns the cached body for key, or nil when there is none.
func (cache *storeCache) lookup(key string) []byte {
	cache.state.Lock()
	defer cache.state.Unlock()
	if key == cache.key {
		return cache.body
	}
	return nil
}

// store keeps body under key unless clear ran since generation was read.
func (cache *storeCache) store(key string, body []byte, generation uint64) {
	cache.state.Lock()
	defer cache.state.Unlock()
	if cache.generation == generation {
		cache.key, cache.body = key, body
	}
}

// discoverWorkspace is discover; swappable so tests can hold a discovery in progress. It is atomic
// because a run's worker goroutine may still read it when a test restores the original.
var discoverWorkspace = func() *atomic.Pointer[func(string, Catalogue) Catalogue] {
	var hook atomic.Pointer[func(string, Catalogue) Catalogue]
	original := discover
	hook.Store(&original)
	return &hook
}()

// buildCatalogue discovers workspace and saves the disposable index. It takes no lock and reads
// only fields fixed at start, so the slow part of a refresh (hashing every pinned file) runs
// while requests are served from the previous catalogue. Callers hold app.refreshing.
func (app *Application) buildCatalogue(workspace string) Catalogue {
	catalogue := (*discoverWorkspace.Load())(workspace, app.seed)
	catalogue.PolicyLocked = app.locked
	// The persisted index is a disposable snapshot, never an authority on restart.
	if err := saveJSON(filepath.Join(app.loc.State, "index.json"), catalogue); err != nil {
		log.Printf("Index cache: %v", err)
		catalogue.Issues = append(catalogue.Issues, "Search index could not be saved; live browsing is still available.")
	}
	return catalogue
}

// refresh rediscovers the current workspace and swaps the result in under a short lock. The
// workspace only changes under app.refreshing, so the result always belongs to it.
func (app *Application) refresh() {
	app.refreshing.Lock()
	defer app.refreshing.Unlock()
	app.mu.RLock()
	workspace := app.config.Workspace
	app.mu.RUnlock()
	catalogue := app.buildCatalogue(workspace)
	app.mu.Lock()
	app.catalogue = catalogue
	app.mu.Unlock()
}

func jsonResponse(w http.ResponseWriter, value any) {
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	if err := json.NewEncoder(w).Encode(value); err != nil {
		log.Printf("Response: %v", err)
	}
}

func (app *Application) ServeHTTP(w http.ResponseWriter, r *http.Request) {
	w.Header().Set("Cache-Control", "no-store")
	w.Header().Set("X-Content-Type-Options", "nosniff")
	w.Header().Set("Referrer-Policy", "no-referrer")
	w.Header().Set("Cross-Origin-Resource-Policy", "same-origin")
	origin := "http://" + app.host
	if r.Host != app.host || (r.Header.Get("Origin") != "" && r.Header.Get("Origin") != origin) || foreignSite(r) {
		http.Error(w, "Local app requests only", http.StatusForbidden)
		return
	}
	if r.URL.Path == "/launch" {
		app.serveLaunch(w, r)
		return
	}
	// Only the instance check needs no session: it names the application and a digest of its
	// state folder, and reads no workspace data.
	if r.URL.Path != "/health" && !app.authorized(r) {
		http.Error(w, launcherOnly, http.StatusForbidden)
		return
	}
	if strings.HasPrefix(r.URL.Path, "/api/runs/") {
		app.serveRunAPI(w, r)
		return
	}
	if r.Method == http.MethodPost {
		if r.Header.Get("X-Issuer-Library") != "1" || r.Header.Get("Content-Type") != "application/json" {
			http.Error(w, "Invalid application request", http.StatusForbidden)
			return
		}
		app.post(w, r)
		return
	}
	if r.Method != http.MethodGet && r.Method != http.MethodHead {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	switch r.URL.Path {
	case "/health":
		jsonResponse(w, map[string]string{"application": "finalworkflow-issuer-library/1", "instance": digest([]byte(app.loc.State))})
	case "/api/catalogue":
		app.writeCatalogue(w)
	case "/api/workspace":
		app.serveWorkspace(w)
	default:
		if strings.HasPrefix(r.URL.Path, "/files/") {
			app.serveFile(w, r)
			return
		}
		app.serveAsset(w, r)
	}
}

// foreignSite reports whether the browser says r comes from another origin. Sec-Fetch-Site is
// accepted only as same-origin (the app's own page and frames), none (an address the user or the
// launcher opened) or absent. same-site is refused too: a page on another 127.0.0.1 port is the
// same site, and the SameSite=Strict cookie goes with its requests.
func foreignSite(r *http.Request) bool {
	for _, site := range r.Header.Values("Sec-Fetch-Site") {
		if site != "same-origin" && site != "none" {
			return true
		}
	}
	return false
}

// writeCatalogue sends the current catalogue. It is encoded under the read lock and written
// after it: a client that stops reading must not hold the lock the refresh ticker waits for.
func (app *Application) writeCatalogue(w http.ResponseWriter) {
	app.mu.RLock()
	raw, err := json.Marshal(app.catalogue)
	app.mu.RUnlock()
	if err != nil {
		http.Error(w, "Could not read the library", http.StatusInternalServerError)
		return
	}
	w.Header().Set("Content-Type", "application/json; charset=utf-8")
	_, _ = w.Write(append(raw, '\n'))
}

func (app *Application) serveWorkspace(w http.ResponseWriter) {
	app.mu.RLock()
	catalogue, err := json.Marshal(app.catalogue)
	snapshot := app.catalogue
	workspace := app.config.Workspace
	app.mu.RUnlock()
	if err != nil {
		http.Error(w, "Could not read the library", http.StatusInternalServerError)
		return
	}
	store, err := app.workspaceStore(workspace, snapshot, catalogue)
	if err != nil {
		http.Error(w, err.Error(), http.StatusServiceUnavailable)
		return
	}
	w.Header().Set("Content-Type", "application/json")
	_, _ = w.Write(store) // written with storeCache.mu released: a stalled client holds nothing
}

// workspaceStore returns the store output, rerunning the store only when its fingerprint changed.
// The returned slice is never modified. A failed fingerprint or store is not cached.
func (app *Application) workspaceStore(workspace string, snapshot Catalogue, catalogue []byte) ([]byte, error) {
	app.storeCache.mu.Lock()
	defer app.storeCache.mu.Unlock()
	generation := app.storeCache.current()
	key, keyErr := workspaceFingerprint(workspace, snapshot, filepath.Dir(app.engine.Script))
	if keyErr != nil {
		log.Printf("Workspace fingerprint: %v; running the store uncached", keyErr)
	} else if cached := app.storeCache.lookup(key); cached != nil {
		return cached, nil
	}
	body, err := app.engine.library(workspace, catalogue)
	if err != nil {
		return nil, err
	}
	if keyErr == nil {
		app.storeCache.store(key, body, generation)
	}
	return body, nil
}

// post handles the state-changing requests. Responses are written after app.mu is released.
func (app *Application) post(w http.ResponseWriter, r *http.Request) {
	switch r.URL.Path {
	case "/api/refresh":
		app.refresh()
		app.storeCache.clear()
		app.writeCatalogue(w)
	case "/api/settings":
		status, message := app.changeSettings(w, r)
		app.storeCache.clear() // after the locks are released; the key also names the workspace
		if status != http.StatusOK {
			http.Error(w, message, status)
			return
		}
		app.writeCatalogue(w)
	case "/api/quit":
		app.mu.RLock()
		active := len(app.activeJobs) > 0
		app.mu.RUnlock()
		if active {
			http.Error(w, "A run is active. Keep the application open until it finishes or stops.", 409)
			return
		}
		jsonResponse(w, map[string]bool{"stopped": true})
		go app.stop()
	default:
		http.NotFound(w, r)
	}
}

// reviewInFlight refuses a workspace switch while a review writes into the current workspace.
const reviewInFlight = "A run review is in progress; wait for it to finish before changing the workspace"

// switchesDuringReviewLocked reports whether moving to workspace would switch it while a review
// is in flight. Saving the same workspace is not a switch. The caller holds app.mu.
func (app *Application) switchesDuringReviewLocked(workspace string) bool {
	return app.reviews > 0 && workspace != filepath.Clean(app.config.Workspace)
}

// changeSettings switches to the requested workspace, refusing with an HTTP status and message
// while a run is active, while a review is in flight (for a switch), under IT policy or for an
// unusable folder. The new workspace is discovered without app.mu; the settings, configuration
// and catalogue then change together.
func (app *Application) changeSettings(w http.ResponseWriter, r *http.Request) (int, string) {
	app.refreshing.Lock()
	defer app.refreshing.Unlock()
	app.mu.RLock()
	active := len(app.activeJobs) > 0
	app.mu.RUnlock()
	if active {
		return 409, "Wait for the active run before changing its workspace"
	}
	if app.locked {
		return http.StatusForbidden, "Workspace is managed by IT"
	}
	var config Config
	decoder := json.NewDecoder(http.MaxBytesReader(w, r.Body, 8192))
	decoder.DisallowUnknownFields()
	if err := decoder.Decode(&config); err != nil {
		return http.StatusBadRequest, "Invalid settings"
	}
	if !filepath.IsAbs(config.Workspace) {
		return http.StatusBadRequest, "Enter an absolute workspace folder"
	}
	config.Workspace = filepath.Clean(config.Workspace)
	app.mu.RLock()
	reviewing := app.switchesDuringReviewLocked(config.Workspace)
	app.mu.RUnlock()
	if reviewing {
		return 409, reviewInFlight
	}
	info, err := os.Stat(config.Workspace)
	if err != nil || !info.IsDir() {
		return http.StatusBadRequest, "The workspace folder is unavailable"
	}
	catalogue := app.buildCatalogue(config.Workspace)
	app.mu.Lock()
	defer app.mu.Unlock()
	if len(app.activeJobs) > 0 { // A run started while the new workspace was being read.
		return 409, "Wait for the active run before changing its workspace"
	}
	if app.switchesDuringReviewLocked(config.Workspace) { // Likewise a review.
		return 409, reviewInFlight
	}
	if err = saveJSON(filepath.Join(app.loc.State, "settings.json"), config); err != nil {
		return http.StatusInternalServerError, "Could not save settings"
	}
	app.config = config
	app.catalogue = catalogue
	app.adoptJobsLocked(config.Workspace)
	return http.StatusOK, ""
}

func (app *Application) serveFile(w http.ResponseWriter, r *http.Request) {
	name := strings.TrimPrefix(r.URL.Path, "/files/")
	// Only the lookup holds the lock; reading, verifying and above all writing the file to a
	// client that may stop reading happen after it is released.
	app.mu.RLock()
	hash, allowed := app.catalogue.Allowed[name]
	workspace := app.config.Workspace
	app.mu.RUnlock()
	if !allowed || !localPath(name) {
		http.NotFound(w, r)
		return
	}
	root, err := os.OpenRoot(workspace)
	if err != nil {
		http.Error(w, "Workspace unavailable", http.StatusGone)
		return
	}
	defer root.Close()
	raw, err := readFile(root, name)
	if err != nil {
		http.Error(w, "File unavailable; refresh the library", http.StatusGone)
		return
	}
	pinned := r.URL.Query().Get("sha256")
	actual := ""
	if hash != "" || pinned != "" {
		actual = digest(raw)
	}
	if hash != "" && actual != hash {
		http.Error(w, "File changed since verification; refresh the library", http.StatusConflict)
		return
	}
	if pinned != "" && actual != pinned {
		http.Error(w, "This link refers to a different evidence version; refresh the library", http.StatusConflict)
		return
	}
	ext := strings.ToLower(path.Ext(name))
	contentType := "text/plain; charset=utf-8"
	if ext == ".html" || ext == ".htm" {
		contentType = "text/html; charset=utf-8"
	}
	if ext == ".pdf" {
		contentType = "application/pdf"
	}
	if ext == ".xlsx" {
		contentType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
		w.Header().Set("Content-Disposition", mime.FormatMediaType("attachment", map[string]string{"filename": path.Base(name)}))
	}
	if r.URL.Query().Get("download") == "1" {
		filename := path.Base(name)
		if hash != "" && (filename == "report.html" || filename == "model.html") {
			filename = path.Base(path.Dir(name)) + ".html"
		}
		w.Header().Set("Content-Disposition", mime.FormatMediaType("attachment", map[string]string{"filename": filename}))
	}
	// Reports retain their local scripts but receive an opaque sandboxed origin:
	// a report cannot read the library API, modify settings or access the network.
	ancestors := "'none'"
	if (ext == ".html" || ext == ".htm") && hash != "" && r.URL.Query().Get("embedded") == "1" {
		ancestors = "http://" + app.host
		// Only a report receives the presentation adapter; a published model is served as it was verified.
		if r.URL.Query().Get("download") != "1" && path.Base(name) == "report.html" {
			raw = reportPresentation(raw)
		}
	}
	w.Header().Set("Content-Security-Policy", "sandbox allow-scripts allow-downloads; default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; img-src data:; font-src data:; connect-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors "+ancestors)
	w.Header().Set("Content-Type", contentType)
	http.ServeContent(w, r, path.Base(name), time.Time{}, bytes.NewReader(raw))
}

// lastBodyClose returns the offset in html of its final "</body>", matched with an
// ASCII-only fold so the offset always indexes the original bytes (Unicode lower-casing
// changes lengths); len(html) when there is none.
func lastBodyClose(html []byte) int {
	const tag = "</body>"
	for i := len(html) - len(tag); i >= 0; i-- {
		if html[i] != '<' {
			continue
		}
		match := true
		for j := 1; j < len(tag); j++ {
			c := html[i+j]
			if 'A' <= c && c <= 'Z' {
				c += 'a' - 'A'
			}
			if c != tag[j] {
				match = false
				break
			}
		}
		if match {
			return i
		}
	}
	return len(html)
}

func reportPresentation(original []byte) []byte {
	style, _ := resources.ReadFile("web/report-adapter.css")
	brand, _ := resources.ReadFile("web/brand.css")
	script, _ := resources.ReadFile("web/report-adapter.js")
	position := lastBodyClose(original)
	return bytes.Join([][]byte{original[:position], []byte("<style data-library-presentation>"), style, brand,
		[]byte("</style><script data-library-presentation>"), script, []byte("</script>"), original[position:]}, nil)
}

func (app *Application) serveAsset(w http.ResponseWriter, r *http.Request) {
	name := strings.TrimPrefix(r.URL.Path, "/")
	if name == "" {
		name = "index.html"
	}
	if !localPath(name) || name == "legacy-catalog.json" {
		http.NotFound(w, r)
		return
	}
	raw, err := fs.ReadFile(resources, "web/"+name)
	if err != nil {
		http.NotFound(w, r)
		return
	}
	w.Header().Set("Content-Security-Policy", "default-src 'none'; script-src 'self'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; font-src 'self'; connect-src 'self'; frame-src 'self'; base-uri 'none'; form-action 'none'; frame-ancestors 'none'")
	if name == "context-form.html" {
		w.Header().Set("Content-Security-Policy", "sandbox allow-scripts allow-downloads; default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; font-src data:; img-src data:; connect-src 'none'; base-uri 'none'; form-action 'none'; frame-ancestors http://"+app.host)
	}
	contentType := mime.TypeByExtension(path.Ext(name))
	if contentType == "" {
		contentType = "application/octet-stream"
	}
	w.Header().Set("Content-Type", contentType)
	http.ServeContent(w, r, name, time.Time{}, bytes.NewReader(raw))
}

func newApplication(loc Locations, override string) (*Application, error) {
	config, locked, err := loadConfig(loc)
	if err != nil {
		return nil, err
	}
	if override != "" {
		if locked {
			return nil, fmt.Errorf("workspace override is disabled by IT configuration")
		}
		config.Workspace, err = filepath.Abs(override)
		if err != nil {
			return nil, err
		}
	}
	var seed Catalogue
	raw, err := resources.ReadFile("web/legacy-catalog.json")
	if err != nil {
		return nil, err
	}
	if err = json.Unmarshal(raw, &seed); err != nil {
		return nil, err
	}
	app := &Application{engine: localEngine(), loc: loc, config: config, locked: locked, seed: seed, now: time.Now, pause: time.Sleep, notifier: platformNotify}
	// Without the secret nothing can be served safely, so the app does not start.
	if app.ticket, err = randomSecret(); err != nil {
		return nil, fmt.Errorf("could not create the launch secret: %w", err)
	}
	if app.session, err = randomSecret(); err != nil {
		return nil, fmt.Errorf("could not create the launch secret: %w", err)
	}
	app.catalogue = app.buildCatalogue(config.Workspace)
	app.adoptJobsLocked(config.Workspace)
	// Counted from here, once the library is ready, so a slow first discovery does not use it up.
	app.expires = clock().Add(ticketLifetime)
	return app, nil
}
