package main

import (
	"encoding/json"
	"os"
	"path/filepath"
	"time"
)

// tabGrace is how long after the last run-list request a browser tab still counts as watching.
// The app-wide watcher polls /api/runs/list every 5 s while a run is running.
const tabGrace = 15 * time.Second

// tabWatching reports whether a run-list request was served within tabGrace. Never watched is false.
func (app *Application) tabWatching() bool {
	return clock().Sub(time.Unix(0, app.watched.Load())) <= tabGrace
}

// finishNotice builds the native notice text for a finished run from its status word and, when
// known, its issuer. It never carries the status message, which may hold redacted provider text.
func finishNotice(folder string) (title, body string, ok bool) {
	var status struct {
		State string `json:"state"`
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
	if review.Issuer != "" {
		return "Issuer Library", review.Issuer + " run " + status.State, true
	}
	return "Issuer Library", "Run " + status.State, true
}

// notifyNatively shows the notice; swappable in tests.
var notifyNatively = platformNotify

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
