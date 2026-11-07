package main

import (
	"context"
	"log"
	"os"
	"path/filepath"
	"strconv"
	"strings"
	"sync/atomic"
	"testing"
	"time"
)

// C10: an error run() returns after opening library.log is recorded there, and the log output
// no longer points at the file run() closed (main logs the error again after run returns).
func TestRunRecordsItsErrorInTheLogBeforeClosingIt(t *testing.T) {
	state := t.TempDir()
	savedOutput := log.Writer()
	defer log.SetOutput(savedOutput)
	err := run([]string{"-state-dir", state, "-no-browser", "-port", "80"})
	if err == nil || !strings.Contains(err.Error(), "port must be between") {
		t.Fatalf("run: %v", err)
	}
	raw, readErr := os.ReadFile(filepath.Join(state, "library.log"))
	if readErr != nil || !strings.Contains(string(raw), "port must be between 1024 and 65535") {
		t.Fatalf("library.log = %q (%v)", raw, readErr)
	}
	if log.Writer() != os.Stderr {
		t.Fatalf("log output still points at the closed library.log: %v", log.Writer())
	}
}

// The periodic refresh ends with the library: run waits for a discovery in progress, so none
// outlives it reading discoverWorkspace and writing the index into the state folder. Expected:
// with the first periodic discovery held (the second in all; newApplication's is the first), run
// has not returned 500 ms after the quit is answered, and returns nil once the discovery ends.
// The ticks that fell due meanwhile start no further discovery: two in all.
func TestRunReturnsOnlyAfterItsPeriodicRefreshEnds(t *testing.T) {
	savedPoll, savedBrowser, savedLog, savedDiscover := refreshPoll, launchBrowser, log.Writer(), discoverWorkspace
	t.Cleanup(func() {
		refreshPoll, launchBrowser, discoverWorkspace = savedPoll, savedBrowser, savedDiscover
		log.SetOutput(savedLog)
	})
	refreshPoll = 20 * time.Millisecond
	opened := make(chan string, 1)
	launchBrowser = func(url string) error { opened <- url; return nil }
	entered, release := make(chan struct{}), make(chan struct{})
	var discoveries atomic.Int32
	discoverWorkspace = func(folder string, seeds Catalogue) Catalogue {
		if discoveries.Add(1) == 2 {
			close(entered)
			<-release
		}
		return savedDiscover(folder, seeds)
	}
	defer captureStdout(t)()
	port := strconv.Itoa(freePort(t))
	ended := make(chan error, 1)
	go func() { ended <- runLauncher(t, "-state-dir", t.TempDir(), "-port", port, "-workspace", t.TempDir()) }()
	cookie := exchange(t, waitOpened(t, opened, ended))
	select {
	case <-entered:
	case <-time.After(10 * time.Second):
		t.Fatal("no periodic refresh began")
	}
	if code := send(t, "POST", "http://127.0.0.1:"+port+"/api/quit", cookie); code != 200 {
		t.Fatalf("quit: %d", code)
	}
	select {
	case err := <-ended:
		close(release)
		t.Fatalf("run returned (%v) while its periodic refresh was discovering", err)
	case <-time.After(500 * time.Millisecond):
		close(release)
	}
	select {
	case err := <-ended:
		if err != nil {
			t.Fatalf("run: %v", err)
		}
	case <-time.After(10 * time.Second):
		t.Fatal("run did not return after the discovery ended")
	}
	if n := discoveries.Load(); n != 2 {
		t.Errorf("%d discoveries, want 2: a tick left waiting started one after the quit", n)
	}
}

// A library quitting for a relaunch keeps app.refreshing until the process ends, so the periodic
// refresh skips its ticks instead of waiting for the lock, which would keep run from returning.
// Expected: with the lock held throughout, refreshPeriodically returns once its context ends.
func TestPeriodicRefreshDoesNotWaitOnAHeldRefreshLock(t *testing.T) {
	app, _ := testApp(t)
	app.refreshing.Lock() // as answerQuitRequest keeps it
	ctx, cancel := context.WithCancel(context.Background())
	ended := make(chan struct{})
	go func() { app.refreshPeriodically(ctx, time.Millisecond); close(ended) }()
	time.Sleep(20 * time.Millisecond) // ticks while the lock is held
	cancel()
	select {
	case <-ended:
	case <-time.After(5 * time.Second):
		t.Fatal("the periodic refresh waited on the held lock")
	}
}
