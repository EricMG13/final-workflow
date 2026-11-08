package main

import (
	"os"
	"path/filepath"
	"strings"
	"testing"
	"time"
)

func noticeFolder(t *testing.T, status, review string) string {
	t.Helper()
	folder := t.TempDir()
	if status != "" {
		if err := os.WriteFile(filepath.Join(folder, "status.json"), []byte(status), 0600); err != nil {
			t.Fatal(err)
		}
	}
	if review != "" {
		if err := os.WriteFile(filepath.Join(folder, "review.json"), []byte(review), 0600); err != nil {
			t.Fatal(err)
		}
	}
	return folder
}

func TestFinishNoticeTextUsesIssuerAndState(t *testing.T) {
	title, body, ok := finishNotice(noticeFolder(t, `{"state":"complete","message":"secret provider text"}`, `{"issuer":"Northbridge Group"}`))
	if !ok || title != "Issuer Library" || body != "Northbridge Group run complete" {
		t.Fatalf("got %q %q %v", title, body, ok)
	}
	if _, _, ok = finishNotice(noticeFolder(t, `{"state":"running"}`, `{"issuer":"Northbridge Group"}`)); ok {
		t.Fatal("a running job produced a notice")
	}
	if _, _, ok = finishNotice(noticeFolder(t, "", "")); ok {
		t.Fatal("an unreadable status produced a notice")
	}
	_, body, ok = finishNotice(noticeFolder(t, `{"state":"interrupted"}`, ""))
	if !ok || body != "Run interrupted" {
		t.Fatalf("got %q %v", body, ok)
	}
}

func TestToastScriptIsFixedAndReadsOnlyTheTwoVariables(t *testing.T) {
	if strings.Count(toastScript, "$env:") != 2 {
		t.Fatalf("expected exactly two environment reads")
	}
	for _, want := range []string{"$env:ISSUER_LIBRARY_TOAST_TITLE", "$env:ISSUER_LIBRARY_TOAST_BODY", "CreateTextNode", "ContentType = WindowsRuntime", "{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}"} {
		if !strings.Contains(toastScript, want) {
			t.Errorf("script lacks %q", want)
		}
	}
	for _, bad := range []string{"%s", "+ $env"} {
		if strings.Contains(toastScript, bad) {
			t.Errorf("script contains %q", bad)
		}
	}
}

func TestTabWatchingWindow(t *testing.T) {
	origin := time.Date(2026, 11, 8, 12, 0, 0, 0, time.UTC)
	now := origin
	old := clock
	clock = func() time.Time { return now }
	t.Cleanup(func() { clock = old })
	app := &Application{}
	if app.tabWatching() {
		t.Fatal("never watched counted as watching")
	}
	app.watched.Store(origin.UnixNano())
	now = origin.Add(15 * time.Second)
	if !app.tabWatching() {
		t.Fatal("exactly at the grace edge should still watch")
	}
	now = origin.Add(15*time.Second + time.Nanosecond)
	if app.tabWatching() {
		t.Fatal("past the grace should not watch")
	}
}
