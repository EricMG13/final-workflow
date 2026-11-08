package main

import (
	"encoding/json"
	"os"
	"path/filepath"
	"strings"
	"time"
)

// tabGrace is how long finishJob waits, after a run finishes, for a run-list request that proves a
// tab is open. The app-wide watcher polls /api/runs/list every 5 s while a run is running, but
// Chrome and Edge throttle a hidden tab to about one poll a minute, so the wait covers one such poll.
const tabGrace = 75 * time.Second

// tabPollStep is how long tabWatching sleeps between looks at the last run-list request.
const tabPollStep = time.Second

// tabWatching reports whether a run-list request arrived after the finish time recorded in
// app.finished, waiting up to tabGrace after that time for one. A request made before the finish
// does not count: a tab closed since then leaves only such a request. It holds no lock.
func (app *Application) tabWatching() bool {
	finished := app.finished.Load()
	for {
		if app.watched.Load() > finished {
			return true
		}
		if app.now().UnixNano()-finished >= int64(tabGrace) {
			return false
		}
		app.pause(tabPollStep)
	}
}

// toastEnvNames are the variables the PowerShell child inherits, matched case-insensitively: what
// PowerShell and WinRT need to start, and no credentials.
var toastEnvNames = []string{"SystemRoot", "windir", "SystemDrive", "USERPROFILE", "APPDATA", "LOCALAPPDATA", "TEMP", "TMP", "PATH", "PATHEXT", "ProgramData", "ProgramFiles", "COMPUTERNAME", "USERNAME", "PROCESSOR_ARCHITECTURE"}

// toastEnv builds the child environment from environ: the allowed names, then the two notice variables.
func toastEnv(environ []string, title, body string) []string {
	env := make([]string, 0, len(toastEnvNames)+2)
	for _, entry := range environ {
		name, _, _ := strings.Cut(entry, "=")
		for _, allowed := range toastEnvNames {
			if strings.EqualFold(name, allowed) {
				env = append(env, entry)
				break
			}
		}
	}
	return append(env, "ISSUER_LIBRARY_TOAST_TITLE="+title, "ISSUER_LIBRARY_TOAST_BODY="+body)
}

// stopReasonWords are the fixed words for a reason the worker records in status.json. Only these
// words are ever shown; a reason outside the table is dropped rather than echoed.
var stopReasonWords = map[string]string{
	"budget":      "spending cap reached",
	"checker":     "a handoff did not pass its check",
	"provider":    "provider error or unknown charge",
	"interrupted": "interrupted",
	"ruling":      "a provider ruling or pause is in force",
}

// finishNotice builds the native notice text for a finished run from its status word and, when
// known, its issuer and, for a run that did not complete, its recorded reason in short words. It never carries the status message, which may hold redacted provider text.
func finishNotice(folder string) (title, body string, ok bool) {
	var status struct {
		State  string `json:"state"`
		Reason any    `json:"reason"` // tolerant: a reason that is not a string is dropped, not a reason to lose the notice
	}
	raw, err := os.ReadFile(filepath.Join(folder, "status.json"))
	if err != nil || json.Unmarshal(raw, &status) != nil || status.State == "" || status.State == "running" {
		return "", "", false
	}
	var review struct {
		Issuer string `json:"issuer"`
	}
	if raw, err = os.ReadFile(filepath.Join(folder, "review.json")); err == nil {
		_ = json.Unmarshal(raw, &review) // an unreadable review only drops the issuer from the text
	}
	text := "Run " + status.State
	if review.Issuer != "" {
		text = review.Issuer + " run " + status.State
	}
	// A reason that only repeats the state word ("interrupted") adds nothing.
	reason, _ := status.Reason.(string)
	if words, known := stopReasonWords[reason]; known && status.State != "complete" && words != status.State {
		text += ": " + words
	}
	return "Issuer Library", text, true
}

// toastScript is the fixed PowerShell program for the Windows notice. The text arrives only
// through the two environment variables and is set as XML text nodes, never concatenated.
const toastScript = `$ErrorActionPreference = 'Stop'
$null = [Windows.UI.Notifications.ToastNotificationManager, Windows.UI.Notifications, ContentType = WindowsRuntime]
$null = [Windows.Data.Xml.Dom.XmlDocument, Windows.Data.Xml.Dom.XmlDocument, ContentType = WindowsRuntime]
$xml = New-Object Windows.Data.Xml.Dom.XmlDocument
$xml.LoadXml('<toast><visual><binding template="ToastGeneric"><text/><text/></binding></visual></toast>')
$texts = $xml.GetElementsByTagName('text')
$null = $texts.Item(0).AppendChild($xml.CreateTextNode($env:ISSUER_LIBRARY_TOAST_TITLE))
$null = $texts.Item(1).AppendChild($xml.CreateTextNode($env:ISSUER_LIBRARY_TOAST_BODY))
$toast = [Windows.UI.Notifications.ToastNotification]::new($xml)
[Windows.UI.Notifications.ToastNotificationManager]::CreateToastNotifier('{1AC14E77-02E7-4E5D-B744-2EB1AE5198B7}\WindowsPowerShell\v1.0\powershell.exe').Show($toast)
`
