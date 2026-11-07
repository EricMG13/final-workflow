package main

import (
	"context"
	"encoding/json"
	"errors"
	"io/fs"
	"log"
	"net"
	"net/http"
	"net/http/httptest"
	"os"
	"os/exec"
	"path/filepath"
	"regexp"
	"runtime"
	"strconv"
	"strings"
	"sync"
	"sync/atomic"
	"testing"
	"time"
)

// shortQuitTimes makes the running instance and a relaunch poll every 10 ms, and a relaunch wait
// at most wait.
func shortQuitTimes(t *testing.T, wait time.Duration) {
	savedPoll, savedWait := quitPoll, quitWait
	quitPoll, quitWait = 10*time.Millisecond, wait
	t.Cleanup(func() { quitPoll, quitWait = savedPoll, savedWait })
}

var loopback = &http.Client{Timeout: 10 * time.Second, Transport: &http.Transport{Proxy: nil}, CheckRedirect: func(*http.Request, []*http.Request) error { return http.ErrUseLastResponse }}

// waitOpened returns the next link a launch opens, failing if the launch ends first.
func waitOpened(t *testing.T, opened chan string, ended chan error) string {
	t.Helper()
	select {
	case link := <-opened:
		return link
	case err := <-ended:
		t.Fatalf("the launch ended before opening a link: %v", err)
	case <-time.After(20 * time.Second):
		t.Fatal("the launch opened no link")
	}
	return ""
}

// exchange opens a launch link as the browser does and returns the session cookie it receives.
func exchange(t *testing.T, link string) *http.Cookie {
	t.Helper()
	response, err := loopback.Get(link)
	if err != nil {
		t.Fatal(err)
	}
	response.Body.Close()
	if response.StatusCode != 303 || len(response.Cookies()) != 1 {
		t.Fatalf("exchange: %d %v", response.StatusCode, response.Cookies())
	}
	return response.Cookies()[0]
}

// send makes a request as the app's page does (a POST with the custom header, JSON and Origin),
// with cookie when it is not nil, and returns the status.
func send(t *testing.T, method, url string, cookie *http.Cookie) int {
	t.Helper()
	r, _ := http.NewRequest(method, url, strings.NewReader("{}"))
	if method == "POST" {
		r.Header.Set("X-Issuer-Library", "1")
		r.Header.Set("Content-Type", "application/json")
		r.Header.Set("Origin", url[:strings.Index(url[len("http://"):], "/")+len("http://")])
	}
	if cookie != nil {
		r.AddCookie(cookie)
	}
	response, err := loopback.Do(r)
	if err != nil {
		t.Fatal(err)
	}
	response.Body.Close()
	return response.StatusCode
}

// plantRequest writes a fresh quit request as a relaunch does.
func plantRequest(t *testing.T, state string) {
	t.Helper()
	if err := os.WriteFile(filepath.Join(state, quitRequestName), []byte("quit requested by process 1\n"), 0600); err != nil {
		t.Fatal(err)
	}
}

func absent(t *testing.T, name string) bool {
	t.Helper()
	_, err := os.Lstat(name)
	return errors.Is(err, fs.ErrNotExist)
}

// S18 ruling 1, through run() as the executable runs it. Expected by hand: a request and an answer
// left from a crash are cleared when the first launch starts (it keeps running); that launch opens
// http://127.0.0.1:<port>/launch?ticket=<64 hex> and the browser then loses its cookie (403). A
// relaunch places the request, the idle instance removes it and stops (run returns nil), and the
// relaunch takes the port and opens a different link whose cookie works while the old one gets
// 403. Each launch prints only the address; no quit file is left, and neither launch's ticket or
// session is in any state file, library.log included.
func TestRelaunchAsksAnIdleLibraryToQuitAndOpensAFreshLink(t *testing.T) {
	shortQuitTimes(t, 10*time.Second)
	saved, savedLog := launchBrowser, log.Writer()
	t.Cleanup(func() { launchBrowser = saved; log.SetOutput(savedLog) })
	opened := make(chan string, 4)
	launchBrowser = func(url string) error { opened <- url; return nil }
	state, workspace, port := t.TempDir(), t.TempDir(), freePort(t)
	arguments := []string{"-state-dir", state, "-port", strconv.Itoa(port), "-workspace", workspace}
	base := "http://127.0.0.1:" + strconv.Itoa(port)
	plantRequest(t, state)
	if err := os.WriteFile(filepath.Join(state, quitAnswerName), []byte(`"busy: 9 runs, 9 reviews"`), 0600); err != nil {
		t.Fatal(err)
	}
	stdout := captureStdout(t)
	restored := false
	defer func() {
		if !restored {
			stdout()
		}
	}()
	first := make(chan error, 1)
	go func() { first <- runLauncher(t, arguments...) }()
	firstLink := waitOpened(t, opened, first)
	pattern := regexp.MustCompile(`^` + regexp.QuoteMeta(base) + `/launch\?ticket=[0-9a-f]{64}$`)
	if !pattern.MatchString(firstLink) {
		t.Fatalf("first link %q", firstLink)
	}
	if !absent(t, filepath.Join(state, quitRequestName)) || !absent(t, filepath.Join(state, quitAnswerName)) {
		t.Fatal("the files left from a crash were not cleared at start")
	}
	firstCookie := exchange(t, firstLink)
	time.Sleep(50 * time.Millisecond) // five polls: the cleared request did not stop the instance
	if code := send(t, "GET", base+"/api/catalogue", firstCookie); code != 200 {
		t.Fatalf("the first instance with its cookie: %d", code)
	}
	if code := send(t, "GET", base+"/api/catalogue", nil); code != 403 {
		t.Fatalf("the cookie is lost, but the library answered %d", code)
	}
	second := make(chan error, 1)
	go func() { second <- runLauncher(t, arguments...) }()
	select {
	case err := <-first:
		if err != nil {
			t.Fatalf("first instance: %v", err)
		}
	case err := <-second:
		t.Fatalf("the relaunch ended: %v", err)
	case <-time.After(10 * time.Second):
		t.Fatal("the idle library did not quit for the relaunch")
	}
	secondLink := waitOpened(t, opened, second)
	if !pattern.MatchString(secondLink) || secondLink == firstLink {
		t.Fatalf("second link %q (first %q)", secondLink, firstLink)
	}
	secondCookie := exchange(t, secondLink)
	if code := send(t, "GET", base+"/api/catalogue", secondCookie); code != 200 {
		t.Fatalf("the fresh session: %d", code)
	}
	if code := send(t, "GET", base+"/api/catalogue", firstCookie); code != 403 {
		t.Fatalf("the old session still opens the library: %d", code)
	}
	if !absent(t, filepath.Join(state, quitRequestName)) || !absent(t, filepath.Join(state, quitAnswerName)) {
		t.Error("a quit file was left behind")
	}
	if code := send(t, "POST", base+"/api/quit", secondCookie); code != 200 {
		t.Fatalf("quit: %d", code)
	}
	select {
	case err := <-second:
		if err != nil {
			t.Fatalf("second instance: %v", err)
		}
	case <-time.After(10 * time.Second):
		t.Fatal("the second instance did not stop")
	}
	printed := stdout()
	restored = true
	if want := "Issuer Library: " + base + "\n"; printed != want+want {
		t.Errorf("stdout %q", printed)
	}
	secrets := []string{strings.TrimPrefix(firstLink, base+"/launch?ticket="), firstCookie.Value, strings.TrimPrefix(secondLink, base+"/launch?ticket="), secondCookie.Value}
	_ = filepath.WalkDir(state, func(name string, entry fs.DirEntry, err error) error {
		if err == nil && !entry.IsDir() {
			raw, _ := os.ReadFile(name)
			for _, secret := range secrets {
				if strings.Contains(string(raw), secret) {
					t.Errorf("%s holds a secret", name)
				}
			}
		}
		return nil
	})
	logged, _ := os.ReadFile(filepath.Join(state, "library.log"))
	if !strings.Contains(string(logged), "A new launch asked the idle library to quit; stopping") {
		t.Errorf("library.log does not record the quit request: %q", logged)
	}
}

// S18 ruling 1 with a run in flight (a job an earlier instance left running, whose worker still
// holds its lock). Expected by hand: the relaunch returns exactly "Issuer Library is busy (1 run,
// 0 reviews); wait for it to finish, then start it again.", the instance keeps running with its
// session, and no quit file is left. Once the worker ends, a relaunch quits the idle instance and
// opens a fresh link.
func TestRelaunchIsToldARunKeepsTheLibraryBusy(t *testing.T) {
	shortQuitTimes(t, 10*time.Second)
	shortWorkerPoll(t)
	saved, savedLog := launchBrowser, log.Writer()
	t.Cleanup(func() { launchBrowser = saved; log.SetOutput(savedLog) })
	opened := make(chan string, 4)
	launchBrowser = func(url string) error { opened <- url; return nil }
	state, workspace, port := t.TempDir(), t.TempDir(), freePort(t)
	id := "web-" + strings.Repeat("b", 32)
	writeJob(t, workspace, id, "running", time.Now())
	worker := &exec.Cmd{}
	configureWorkerCommand(worker)
	lock, err := holdWorkerLock(worker, filepath.Join(workspace, "intake", id, "worker.lock"))
	if err != nil {
		t.Fatal(err)
	}
	released := false
	defer func() {
		if !released {
			lock.Close()
		}
	}()
	arguments := []string{"-state-dir", state, "-port", strconv.Itoa(port), "-workspace", workspace}
	base := "http://127.0.0.1:" + strconv.Itoa(port)
	first := make(chan error, 1)
	go func() { first <- runLauncher(t, arguments...) }()
	link := waitOpened(t, opened, first)
	cookie := exchange(t, link)
	err = runLauncher(t, arguments...)
	if want := "Issuer Library is busy (1 run, 0 reviews); wait for it to finish, then start it again."; err == nil || err.Error() != want {
		t.Fatalf("relaunch beside a run: %v", err)
	}
	select {
	case err := <-first:
		t.Fatalf("the busy library stopped: %v", err)
	default:
	}
	if code := send(t, "GET", base+"/api/catalogue", cookie); code != 200 {
		t.Fatalf("the busy library's session after the relaunch: %d", code)
	}
	if !absent(t, filepath.Join(state, quitRequestName)) || !absent(t, filepath.Join(state, quitAnswerName)) {
		t.Error("a quit file was left behind")
	}
	lock.Close()
	released = true
	// The instance notices the worker has ended within a few polls; until then a relaunch is told
	// it is busy, then one quits it.
	var relaunched chan error
	for attempt := 0; ; attempt++ {
		relaunched = make(chan error, 1)
		go func(done chan error) { done <- runLauncher(t, arguments...) }(relaunched)
		select {
		case err := <-first:
			if err != nil {
				t.Fatalf("first instance: %v", err)
			}
		case err := <-relaunched:
			if attempt > 100 || err == nil || !strings.HasPrefix(err.Error(), "Issuer Library is busy (") {
				t.Fatalf("relaunch after the run ended: %v", err)
			}
			time.Sleep(20 * time.Millisecond)
			continue
		}
		break
	}
	fresh := exchange(t, waitOpened(t, opened, relaunched))
	if code := send(t, "POST", base+"/api/quit", fresh); code != 200 {
		t.Fatalf("quit: %d", code)
	}
	if err := <-relaunched; err != nil {
		t.Fatalf("relaunched instance: %v", err)
	}
}

// answerOf returns the busy answer the instance left, or "" when there is none.
func answerOf(t *testing.T, state string) string {
	t.Helper()
	status, _ := readQuitAnswer(filepath.Join(state, quitAnswerName))
	return status
}

// S18 ruling 1, in process. Expected by hand: with one review in flight the answer is "busy: 0
// runs, 1 review"; with two runs as well "busy: 2 runs, 1 review"; with one "busy: 1 run, 1
// review". Each time the library keeps running (no stop) and the request is removed. Once nothing
// is in flight the next request stops it (one stop, request removed, no answer), and from then a
// review or Start is refused with 503 and the quitting message.
func TestQuitRequestIsAnsweredBusyWhileAReviewOrRunIsInFlight(t *testing.T) {
	app, root := testApp(t)
	app.engine = heldReviewEngine(t)
	var stops atomic.Int32
	app.stop = func() { stops.Add(1) }
	t.Cleanup(func() { releaseReviews(t, root, 0) })
	state, request := app.loc.State, filepath.Join(app.loc.State, quitRequestName)
	reviewed := make(chan *httptest.ResponseRecorder, 1)
	go func() { reviewed <- reviewRequest(t, app, `["annual.txt"]`) }()
	waitReviews(t, app, 1)
	for _, c := range []struct {
		jobs []string
		want string
	}{{nil, "busy: 0 runs, 1 review"}, {[]string{"web-a", "web-b"}, "busy: 2 runs, 1 review"}, {[]string{"web-a"}, "busy: 1 run, 1 review"}} {
		app.mu.Lock()
		app.activeJobs = map[string]bool{}
		for _, id := range c.jobs {
			app.activeJobs[id] = true
		}
		app.mu.Unlock()
		plantRequest(t, state)
		if app.answerQuitRequest() || stops.Load() != 0 {
			t.Fatalf("%v: the library stopped with work in flight", c.jobs)
		}
		if got := answerOf(t, state); got != c.want || !absent(t, request) {
			t.Fatalf("%v: answer %q, request removed %v", c.jobs, got, absent(t, request))
		}
	}
	app.mu.Lock()
	app.activeJobs = map[string]bool{}
	app.mu.Unlock()
	releaseReviews(t, root, 1)
	if w := <-reviewed; w.Code != 200 {
		t.Fatalf("held review: %d %s", w.Code, w.Body.String())
	}
	waitReviews(t, app, 0)
	_ = os.Remove(filepath.Join(state, quitAnswerName))
	plantRequest(t, state)
	if !app.answerQuitRequest() || stops.Load() != 1 || !absent(t, request) || answerOf(t, state) != "" {
		t.Fatalf("idle: stops %d, request removed %v, answer %q", stops.Load(), absent(t, request), answerOf(t, state))
	}
	if w := reviewRequest(t, app, `["annual.txt"]`); w.Code != 503 || w.Body.String() != libraryQuitting+"\n" {
		t.Errorf("review while quitting: %d %q", w.Code, w.Body.String())
	}
	if w := call(app, "POST", "/api/runs/start", `{"id":"web-`+strings.Repeat("c", 32)+`","review_id":"x","confirm":true}`); w.Code != 503 || w.Body.String() != libraryQuitting+"\n" {
		t.Errorf("Start while quitting: %d %q", w.Code, w.Body.String())
	}
}

// S18 ruling 1, adversarial requests. Expected by hand: each of these is removed unread, never
// followed, and does not stop the library or write an answer: an hour old, an hour in the future,
// readable or writable by others, a link to a file elsewhere (which keeps its content), a dangling
// link, a folder, and (as root) a file of another user.
func TestStaleOrInvalidQuitRequestsAreRemovedUnread(t *testing.T) {
	if runtime.GOOS == "windows" {
		t.Skip("permission bits and links are judged by Unix rules here")
	}
	app, _ := testApp(t)
	var stops atomic.Int32
	app.stop = func() { stops.Add(1) }
	state, request := app.loc.State, filepath.Join(app.loc.State, quitRequestName)
	outside := filepath.Join(t.TempDir(), "target")
	if err := os.WriteFile(outside, []byte("kept"), 0600); err != nil {
		t.Fatal(err)
	}
	must := func(err error) {
		if err != nil {
			t.Fatal(err)
		}
	}
	cases := map[string]func(){
		"an hour old": func() {
			plantRequest(t, state)
			must(os.Chtimes(request, time.Now().Add(-time.Hour), time.Now().Add(-time.Hour)))
		},
		"an hour ahead": func() {
			plantRequest(t, state)
			must(os.Chtimes(request, time.Now().Add(time.Hour), time.Now().Add(time.Hour)))
		},
		"readable by others": func() { plantRequest(t, state); must(os.Chmod(request, 0644)) },
		"writable by group":  func() { plantRequest(t, state); must(os.Chmod(request, 0620)) },
		"a link elsewhere":   func() { must(os.Symlink(outside, request)) },
		"a dangling link":    func() { must(os.Symlink(filepath.Join(state, "missing"), request)) },
		"a folder":           func() { must(os.Mkdir(request, 0700)) },
	}
	if os.Getuid() == 0 {
		cases["another user's file"] = func() { plantRequest(t, state); must(os.Chown(request, 12345, 12345)) }
	}
	for label, plant := range cases {
		plant()
		if app.answerQuitRequest() {
			t.Errorf("%s: the library stopped", label)
		}
		if !absent(t, request) || !absent(t, filepath.Join(state, quitAnswerName)) {
			t.Errorf("%s: request removed %v, answer absent %v", label, absent(t, request), absent(t, filepath.Join(state, quitAnswerName)))
		}
	}
	if raw, _ := os.ReadFile(outside); string(raw) != "kept" || stops.Load() != 0 {
		t.Fatalf("link target %q, stops %d", raw, stops.Load())
	}
	app.mu.RLock()
	defer app.mu.RUnlock()
	if app.quitting {
		t.Fatal("an invalid request set the library quitting")
	}
}

// S18 ruling 1: a state folder other users can write to, or that is not this user's, is refused
// by both sides. Expected by hand: for modes 0770, 0720, 0702 and 0777 privateFolder names the
// folder as writable by others; a fresh valid request there is left untouched (no stop, no
// answer); a relaunch returns the refusal before placing a request. Modes 0700, 0750 and 0755 are
// accepted, and back at 0700 the same request stops the library.
func TestAStateFolderOtherUsersCanWriteIsRefused(t *testing.T) {
	if runtime.GOOS == "windows" {
		t.Skip("permission bits do not describe access on Windows; see TestWindowsAccessListJudgement")
	}
	app, _ := testApp(t)
	var stops atomic.Int32
	app.stop = func() { stops.Add(1) }
	state, request := app.loc.State, filepath.Join(app.loc.State, quitRequestName)
	t.Cleanup(func() { _ = os.Chmod(state, 0700) })
	for _, mode := range []fs.FileMode{0770, 0720, 0702, 0777} {
		if err := os.Chmod(state, mode); err != nil {
			t.Fatal(err)
		}
		if err := privateFolder(state); err == nil || err.Error() != "other users can write to the state folder "+state {
			t.Errorf("%o: %v", mode, err)
		}
		plantRequest(t, state)
		if app.answerQuitRequest() || absent(t, request) || !absent(t, filepath.Join(state, quitAnswerName)) {
			t.Errorf("%o: the request was acted on", mode)
		}
		must(t, os.Remove(request))
		_, err := askToQuit(state, "127.0.0.1:1")
		if err == nil || !strings.Contains(err.Error(), "this launch does not ask it to quit: other users can write to the state folder "+state+". Quit the running library") || !absent(t, request) {
			t.Errorf("%o: relaunch %v, request placed %v", mode, err, !absent(t, request))
		}
	}
	for _, mode := range []fs.FileMode{0700, 0750, 0755} {
		must(t, os.Chmod(state, mode))
		if err := privateFolder(state); err != nil {
			t.Errorf("%o: %v", mode, err)
		}
	}
	must(t, os.Chmod(state, 0700))
	if os.Getuid() == 0 {
		must(t, os.Chown(state, 12345, 12345))
		if err := privateFolder(state); err == nil || err.Error() != "the state folder "+state+" does not belong to this user" {
			t.Errorf("another user's folder: %v", err)
		}
		must(t, os.Chown(state, 0, 0))
	}
	plantRequest(t, state)
	if !app.answerQuitRequest() || stops.Load() != 1 {
		t.Fatalf("private folder: stops %d", stops.Load())
	}
}

func must(t *testing.T, err error) {
	t.Helper()
	if err != nil {
		t.Fatal(err)
	}
}

// S18 ruling 1: the request is created owner-only and holds only the asking process. Expected by
// hand: mode 0600 and exactly the given text; a second launch while it is fresh joins it (false,
// text unchanged); a stale one is replaced; a link at the name is removed, not followed (its
// target keeps its content) and a plain file is placed.
func TestTheQuitRequestIsOwnerOnlyAndNamesOnlyTheProcess(t *testing.T) {
	state := t.TempDir()
	request := filepath.Join(state, quitRequestName)
	read := func() string { raw, _ := os.ReadFile(request); return string(raw) }
	if !placeQuitRequest(request, "quit requested by process 4242\n") || read() != "quit requested by process 4242\n" {
		t.Fatalf("placed %q", read())
	}
	if info, _ := os.Lstat(request); runtime.GOOS != "windows" && info.Mode().Perm() != 0600 {
		t.Errorf("mode %o", info.Mode().Perm())
	}
	if placeQuitRequest(request, "quit requested by process 4343\n") || read() != "quit requested by process 4242\n" {
		t.Errorf("a fresh request was replaced: %q", read())
	}
	must(t, os.Chtimes(request, time.Now().Add(-time.Hour), time.Now().Add(-time.Hour)))
	if !placeQuitRequest(request, "quit requested by process 4343\n") || read() != "quit requested by process 4343\n" {
		t.Errorf("a stale request was kept: %q", read())
	}
	if runtime.GOOS == "windows" {
		return
	}
	outside := filepath.Join(t.TempDir(), "target")
	must(t, os.WriteFile(outside, []byte("kept"), 0600))
	must(t, os.Remove(request))
	must(t, os.Symlink(outside, request))
	info, _ := os.Lstat(request)
	if !placeQuitRequest(request, "quit requested by process 4444\n") || read() != "quit requested by process 4444\n" {
		t.Errorf("through a link: %q", read())
	}
	if raw, _ := os.ReadFile(outside); string(raw) != "kept" || info.Mode()&fs.ModeSymlink == 0 {
		t.Errorf("link target %q", raw)
	}
	if info, _ := os.Lstat(request); !info.Mode().IsRegular() {
		t.Errorf("request is %v", info.Mode())
	}
}

// S18 ruling 1: the relaunch shows only a fresh, well-formed busy answer. Expected by hand: the
// three well-formed answers are read; text after the counts, a bare string, plain text, a stale
// answer, a link to a valid answer and an answer over 256 bytes are not.
func TestOnlyAFreshWellFormedBusyAnswerIsShown(t *testing.T) {
	state := t.TempDir()
	answer := filepath.Join(state, quitAnswerName)
	for _, text := range []string{`"busy: 1 run, 0 reviews"`, `"busy: 0 runs, 1 review"`, "\"busy: 12 runs, 3 reviews\"\n"} {
		must(t, os.WriteFile(answer, []byte(text), 0600))
		if got, ok := readQuitAnswer(answer); !ok || got != strings.Trim(strings.TrimSpace(text), `"`) {
			t.Errorf("%s: %q %v", text, got, ok)
		}
	}
	for _, text := range []string{`"busy: 1 run, 0 reviews; open http://x"`, `"Issuer Library is busy"`, "busy: 1 run, 0 reviews", `"busy: 1 run, 0 reviews` + strings.Repeat(" ", 300) + `"`} {
		must(t, os.WriteFile(answer, []byte(text), 0600))
		if got, ok := readQuitAnswer(answer); ok {
			t.Errorf("%q was shown as %q", text, got)
		}
	}
	must(t, os.WriteFile(answer, []byte(`"busy: 1 run, 0 reviews"`), 0600))
	must(t, os.Chtimes(answer, time.Now().Add(-time.Hour), time.Now().Add(-time.Hour)))
	if _, ok := readQuitAnswer(answer); ok {
		t.Error("a stale answer was shown")
	}
	if runtime.GOOS != "windows" {
		valid := filepath.Join(t.TempDir(), "valid")
		must(t, os.WriteFile(valid, []byte(`"busy: 1 run, 0 reviews"`), 0600))
		must(t, os.Remove(answer))
		must(t, os.Symlink(valid, answer))
		if _, ok := readQuitAnswer(answer); ok {
			t.Error("an answer behind a link was shown")
		}
	}
}

// S18 ruling 1: a running instance that neither quits nor answers (an older build, or one that
// is hung). Expected by hand: after the wait (300 ms here) the relaunch returns errAlreadyRunning
// and withdraws its own request.
func TestARelaunchThatGetsNoAnswerWithdrawsItsRequest(t *testing.T) {
	shortQuitTimes(t, 300*time.Millisecond)
	state := t.TempDir()
	held, err := net.Listen("tcp4", "127.0.0.1:0")
	must(t, err)
	defer held.Close()
	began := time.Now()
	if _, err := askToQuit(state, held.Addr().String()); !errors.Is(err, errAlreadyRunning) {
		t.Fatalf("relaunch: %v", err)
	}
	if elapsed := time.Since(began); elapsed < 300*time.Millisecond || elapsed > 5*time.Second {
		t.Errorf("waited %v", elapsed)
	}
	if !absent(t, filepath.Join(state, quitRequestName)) {
		t.Error("the unanswered request was left behind")
	}
}

// S18 ruling 1: two relaunches at once against an idle instance (its port held, its watcher
// running). Expected by hand: the instance stops once; exactly one relaunch gets the port and the
// other returns errAlreadyRunning after its wait; no request is left.
func TestTwoRelaunchesAtOnce(t *testing.T) {
	shortQuitTimes(t, time.Second)
	app, _ := testApp(t)
	held, err := net.Listen("tcp4", "127.0.0.1:0")
	must(t, err)
	var stops atomic.Int32
	app.stop = func() { stops.Add(1); held.Close() }
	ctx, cancel := context.WithCancel(context.Background())
	defer cancel()
	go app.watchQuitRequests(ctx, quitPoll)
	type outcome struct {
		listener net.Listener
		err      error
	}
	outcomes := make(chan outcome, 2)
	for range 2 {
		go func() {
			listener, err := askToQuit(app.loc.State, held.Addr().String())
			outcomes <- outcome{listener, err}
		}()
	}
	ports, refused := 0, 0
	for range 2 {
		o := <-outcomes
		switch {
		case o.err == nil:
			ports++
			defer o.listener.Close() // The winner keeps the port, as the new instance does.
		case errors.Is(o.err, errAlreadyRunning):
			refused++
		default:
			t.Errorf("relaunch: %v", o.err)
		}
	}
	if ports != 1 || refused != 1 || stops.Load() != 1 || !absent(t, filepath.Join(app.loc.State, quitRequestName)) {
		t.Fatalf("ports %d, refused %d, stops %d, request removed %v", ports, refused, stops.Load(), absent(t, filepath.Join(app.loc.State, quitRequestName)))
	}
}

// S18 ruling 1: a request that arrives during a discovery (the periodic refresh) or a workspace
// switch waits for it. Expected by hand: while the discovery is held the request stays and the
// library keeps running; once it ends (the switch answering 200) the next poll stops the library.
func TestAQuitRequestWaitsForADiscoveryInProgress(t *testing.T) {
	for _, label := range []string{"refresh", "workspace switch"} {
		app, _ := testApp(t)
		var stops atomic.Int32
		app.stop = func() { stops.Add(1) }
		entered, release := make(chan struct{}), make(chan struct{})
		saved := discoverWorkspace
		discoverWorkspace = func(workspace string, seed Catalogue) Catalogue {
			close(entered)
			<-release
			return saved(workspace, seed)
		}
		done := make(chan int, 1)
		other := t.TempDir()
		go func() {
			if label == "refresh" {
				app.refresh()
				done <- 200
			} else {
				done <- switchTo(app, other).Code
			}
		}()
		<-entered
		plantRequest(t, app.loc.State)
		if app.answerQuitRequest() || stops.Load() != 0 || absent(t, filepath.Join(app.loc.State, quitRequestName)) {
			t.Errorf("%s: the request was acted on during the discovery", label)
		}
		close(release)
		if code := <-done; code != 200 {
			t.Errorf("%s: %d", label, code)
		}
		discoverWorkspace = saved
		if !app.answerQuitRequest() || stops.Load() != 1 {
			t.Errorf("%s: after the discovery, stops %d", label, stops.Load())
		}
	}
}

// sid builds a SID's stored form from its string form, by hand rather than with quit.go.
func sid(t *testing.T, text string) []byte {
	t.Helper()
	parts := strings.Split(text, "-")
	authority, _ := strconv.ParseUint(parts[2], 10, 48)
	raw := []byte{1, byte(len(parts) - 3), byte(authority >> 40), byte(authority >> 32), byte(authority >> 24), byte(authority >> 16), byte(authority >> 8), byte(authority)}
	for _, part := range parts[3:] {
		value, _ := strconv.ParseUint(part, 10, 32)
		raw = append(raw, byte(value), byte(value>>8), byte(value>>16), byte(value>>24))
	}
	return raw
}

// entry builds an access-control entry: type, flags, size, mask, SID.
func entry(kind, flags byte, mask uint32, who []byte) []byte {
	size := 8 + len(who)
	return append([]byte{kind, flags, byte(size), byte(size >> 8), byte(mask), byte(mask >> 8), byte(mask >> 16), byte(mask >> 24)}, who...)
}

// acl builds a stored access-control list (revision 2) of entries; count overrides the entry count
// when it is not negative.
func acl(count int, entries ...[]byte) []byte {
	body := []byte{}
	for _, e := range entries {
		body = append(body, e...)
	}
	if count < 0 {
		count = len(entries)
	}
	size := 8 + len(body)
	return append([]byte{2, 0, byte(size), byte(size >> 8), byte(count), byte(count >> 8), 0, 0}, body...)
}

// S18 ruling 1 on Windows: the state folder's access-control list decides. Masks by hand: full
// control 0x1F01FF, modify 0x1301BF, read and execute 0x1200A9, add file 0x2, generic write
// 0x40000000. Expected: the default local application data list (SYSTEM, Administrators and the
// user with full control, inherited with OI|CI 0x13) is private, also with Users reading and an
// empty list; Users with modify, Everyone with generic write, Authenticated Users adding files,
// another user with full control, a callback allow entry, a short list, an entry count past the
// list and a SID past its entry are not. A deny entry grants nothing.
func TestWindowsAccessListJudgement(t *testing.T) {
	for text, want := range map[string][]byte{"S-1-5-18": sidSystem, "S-1-5-32-544": sidAdministrators, "S-1-3-0": sidCreatorOwner, "S-1-3-4": sidOwnerRights} {
		if got := sid(t, text); string(got) != string(want) {
			t.Errorf("%s: % x, want % x", text, want, got)
		}
	}
	user := sid(t, "S-1-5-21-1004336348-1177238915-682003330-1001")
	trusted := [][]byte{user, sidSystem, sidAdministrators, sidCreatorOwner, sidOwnerRights}
	system, administrators, users := sid(t, "S-1-5-18"), sid(t, "S-1-5-32-544"), sid(t, "S-1-5-32-545")
	standard := [][]byte{entry(0, 0x13, 0x1F01FF, system), entry(0, 0x13, 0x1F01FF, administrators), entry(0, 0x13, 0x1F01FF, user)}
	with := func(extra ...[]byte) []byte { return acl(-1, append(append([][]byte{}, standard...), extra...)...) }
	for label, c := range map[string]struct {
		list   []byte
		others bool
	}{
		"default":                     {with(), false},
		"users read and execute":      {with(entry(0, 0x13, 0x1200A9, users)), false},
		"empty list":                  {acl(-1), false},
		"creator owner inherit-only":  {with(entry(0, 0x1B, 0x10000000, sid(t, "S-1-3-0"))), false},
		"users denied, then allowed":  {with(entry(1, 0, 0x1301BF, users), entry(0, 0, 0x1200A9, users)), false},
		"users modify":                {with(entry(0, 0x13, 0x1301BF, users)), true},
		"everyone generic write":      {with(entry(0, 0, 0x40000000, sid(t, "S-1-1-0"))), true},
		"authenticated users add":     {with(entry(0, 0, 0x2, sid(t, "S-1-5-11"))), true},
		"another user full control":   {with(entry(0, 0, 0x1F01FF, sid(t, "S-1-5-21-1004336348-1177238915-682003330-1002"))), true},
		"callback allow entry":        {with(entry(9, 0, 0x1200A9, user)), true},
		"short header":                {[]byte{2, 0, 8, 0}, true},
		"count past the list":         {acl(4, standard...), true},
		"SID past its entry":          {acl(-1, entry(0, 0, 0x1200A9, []byte{1, 5, 0, 0, 0, 0, 0, 5, 18, 0, 0, 0})), true},
		"entry size below its header": {acl(1, []byte{0, 0, 2, 0}), true},
	} {
		if got := othersMayWrite(c.list, trusted); got != c.others {
			t.Errorf("%s: others may write %v, want %v", label, got, c.others)
		}
	}
}

// Review of S18 ruling 1: Start racing the quit watcher. Expected by hand, whichever runs first:
// either Start gets 202 and the watcher then sees one run (it keeps running, answers "busy: 1
// run, 0 reviews", and has not asked the app to stop), or the watcher wins (it stops) and Start
// gets 503 with no claim and no worker, so nothing is orphaned. Any other pair is a defect.
func TestStartRacingAQuitRequestNeverOrphansAWorker(t *testing.T) {
	app, root := testApp(t)
	app.engine = fakeEngine(t)
	var stops atomic.Int32
	app.stop = func() { stops.Add(1) }
	state := app.loc.State
	started, quit := 0, 0
	for round := range 40 {
		var review map[string]any
		w := reviewRequest(t, app, `["annual.txt"]`)
		if w.Code != 200 {
			t.Fatalf("round %d: review %d %s", round, w.Code, w.Body.String())
		}
		must(t, json.Unmarshal(w.Body.Bytes(), &review))
		id := review["id"].(string)
		plantRequest(t, state)
		before := stops.Load()
		var code int
		var stopped bool
		gate := make(chan struct{})
		var group sync.WaitGroup
		group.Go(func() {
			<-gate
			code = call(app, "POST", "/api/runs/start", `{"id":"`+id+`","review_id":"review-fingerprint","confirm":true}`).Code
		})
		group.Go(func() {
			<-gate
			time.Sleep(time.Duration(round%8) * 100 * time.Microsecond)
			stopped = app.answerQuitRequest()
		})
		close(gate)
		group.Wait()
		claim := !absent(t, filepath.Join(root, "intake", id, "start.claim"))
		switch {
		case code == 202 && !stopped:
			started++
			if got := answerOf(t, state); got != "busy: 1 run, 0 reviews" || stops.Load() != before {
				t.Fatalf("round %d: Start won; answer %q, stops %d", round, got, stops.Load()-before)
			}
			waitIdle(t, app)
		case code == 503 && stopped:
			quit++
			if claim || !absent(t, filepath.Join(root, "intake", id, "synthetic-starts.txt")) || stops.Load() != before+1 {
				t.Fatalf("round %d: quit won; claim %v, stops %d", round, claim, stops.Load()-before)
			}
			app.refreshing.Unlock() // The test's stand-in for the process ending.
		default:
			t.Fatalf("round %d: Start %d, library stopped %v", round, code, stopped)
		}
		_ = os.Remove(filepath.Join(state, quitAnswerName))
		app.mu.Lock()
		app.quitting = false
		app.mu.Unlock()
	}
	t.Logf("Start won %d rounds, quit won %d", started, quit)
}

// Review of S18 ruling 1: planted answers and links on the relaunch side. Expected by hand: a
// fresh, well-formed busy answer left in the folder before the relaunch (nobody is running to
// write it) is deleted at the start, so the relaunch waits its 300 ms and reports
// errAlreadyRunning rather than busy; a link at quit.answer is deleted, never followed; a link at
// quit.request is replaced by a plain file of this launch (the link's target keeps its content);
// a hard link to an old file is judged stale, removed, and its other name is untouched.
func TestRelaunchSidePlantedAnswersAndLinks(t *testing.T) {
	if runtime.GOOS == "windows" {
		t.Skip("links are judged by Unix rules here")
	}
	shortQuitTimes(t, 300*time.Millisecond)
	state := t.TempDir()
	held, err := net.Listen("tcp4", "127.0.0.1:0")
	must(t, err)
	defer held.Close()
	answer, request := filepath.Join(state, quitAnswerName), filepath.Join(state, quitRequestName)
	outside := filepath.Join(t.TempDir(), "outside")
	must(t, os.WriteFile(outside, []byte("kept"), 0600))

	must(t, os.WriteFile(answer, []byte(`"busy: 9 runs, 9 reviews"`), 0600))
	if _, err := askToQuit(state, held.Addr().String()); !errors.Is(err, errAlreadyRunning) {
		t.Errorf("a pre-planted answer: %v", err)
	}
	must(t, os.Symlink(outside, answer))
	if _, err := askToQuit(state, held.Addr().String()); !errors.Is(err, errAlreadyRunning) || !absent(t, answer) {
		t.Errorf("a linked answer: %v, removed %v", err, absent(t, answer))
	}
	must(t, os.Symlink(outside, request))
	if !placeQuitRequest(request, "quit requested by process 1\n") {
		t.Error("the request behind a link was not replaced")
	}
	if info, err := os.Lstat(request); err != nil || !info.Mode().IsRegular() {
		t.Errorf("request after a link: %v %v", info, err)
	}
	must(t, os.Remove(request))
	old := filepath.Join(t.TempDir(), "old")
	must(t, os.WriteFile(old, []byte("kept"), 0600))
	must(t, os.Chtimes(old, time.Now().Add(-time.Hour), time.Now().Add(-time.Hour)))
	must(t, os.Link(old, request))
	if !placeQuitRequest(request, "quit requested by process 1\n") {
		t.Error("a stale hard link was not replaced")
	}
	if raw, _ := os.ReadFile(old); string(raw) != "kept" {
		t.Errorf("the hard link's other name changed: %q", raw)
	}
	if raw, _ := os.ReadFile(outside); string(raw) != "kept" {
		t.Errorf("the link target changed: %q", raw)
	}
}
