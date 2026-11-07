package main

import (
	"log"
	"os"
	"path/filepath"
	"strings"
	"testing"
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
