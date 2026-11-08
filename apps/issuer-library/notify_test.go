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

func TestFinishNoticeNamesTheStopReason(t *testing.T) {
	cases := []struct{ name, status, review, want string }{
		{"budget", `{"state":"stopped","reason":"budget"}`, `{"issuer":"TransDigm Group Incorporated"}`, "TransDigm Group Incorporated run stopped: spending cap reached"},
		{"checker", `{"state":"stopped","reason":"checker"}`, `{"issuer":"Northbridge Group"}`, "Northbridge Group run stopped: a handoff did not pass its check"},
		{"provider", `{"state":"failed","reason":"provider"}`, `{"issuer":"Northbridge Group"}`, "Northbridge Group run failed: provider error or unknown charge"},
		{"ruling", `{"state":"failed","reason":"ruling"}`, `{"issuer":"Northbridge Group"}`, "Northbridge Group run failed: a provider ruling or pause is in force"},
		{"interrupted repeats the state word once", `{"state":"interrupted","reason":"interrupted"}`, `{"issuer":"Northbridge Group"}`, "Northbridge Group run interrupted"},
		{"no reason", `{"state":"stopped"}`, `{"issuer":"Northbridge Group"}`, "Northbridge Group run stopped"},
		{"unknown reason is not echoed", `{"state":"failed","reason":"sk-secret"}`, `{"issuer":"Northbridge Group"}`, "Northbridge Group run failed"},
		{"no issuer", `{"state":"stopped","reason":"budget"}`, "", "Run stopped: spending cap reached"},
		{"non-string reason keeps the notice", `{"state":"stopped","reason":5}`, `{"issuer":"Northbridge Group"}`, "Northbridge Group run stopped"},
		{"object reason keeps the notice", `{"state":"failed","reason":{"a":1}}`, `{"issuer":"Northbridge Group"}`, "Northbridge Group run failed"},
		{"complete carries no reason", `{"state":"complete","reason":"budget"}`, `{"issuer":"Northbridge Group"}`, "Northbridge Group run complete"},
	}
	for _, c := range cases {
		title, body, ok := finishNotice(noticeFolder(t, c.status, c.review))
		if !ok || title != "Issuer Library" || body != c.want {
			t.Errorf("%s: got %q %q %v, want %q", c.name, title, body, ok, c.want)
		}
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

func TestTabWatchingWaitsForAPollAfterTheFinish(t *testing.T) {
	origin := time.Date(2026, 11, 8, 12, 0, 0, 0, time.UTC)
	now := origin
	app := &Application{now: func() time.Time { return now }}
	app.pause = func(d time.Duration) { now = now.Add(d) }
	app.finished.Store(origin.UnixNano())

	// Never polled: waits the whole 75 s, then false.
	if app.tabWatching() {
		t.Fatal("never watched counted as watching")
	}
	if now != origin.Add(75*time.Second) {
		t.Fatalf("waited until %v, want 75 s after the finish", now)
	}
	// A poll before the finish does not count.
	now = origin
	app.watched.Store(origin.Add(-time.Second).UnixNano())
	if app.tabWatching() {
		t.Fatal("a poll before the finish counted")
	}
	// A poll at the finish instant does not count either; only a later one does.
	now = origin
	app.watched.Store(origin.UnixNano())
	if app.tabWatching() {
		t.Fatal("a poll at the finish instant counted")
	}
	// A poll arriving during the wait (60 s in) counts and ends the wait there.
	now = origin
	app.pause = func(d time.Duration) {
		now = now.Add(d)
		if now == origin.Add(60*time.Second) {
			app.watched.Store(now.UnixNano())
		}
	}
	if !app.tabWatching() || now != origin.Add(60*time.Second) {
		t.Fatalf("late poll not seen; clock %v", now)
	}
}

func TestToastEnvKeepsOnlyTheAllowedNames(t *testing.T) {
	got := toastEnv([]string{"OPENAI_API_KEY=k1", "Path=C:\\bin", "systemroot=C:\\Windows", "GH_TOKEN=k2", "USERNAME=eg", "BAD"}, "T", "B")
	want := []string{"Path=C:\\bin", "systemroot=C:\\Windows", "USERNAME=eg", "ISSUER_LIBRARY_TOAST_TITLE=T", "ISSUER_LIBRARY_TOAST_BODY=B"}
	if strings.Join(got, "|") != strings.Join(want, "|") {
		t.Fatalf("got %q", got)
	}
}
