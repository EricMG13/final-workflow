package main

import (
	"bytes"
	"context"
	"encoding/binary"
	"encoding/json"
	"errors"
	"fmt"
	"io/fs"
	"log"
	"net"
	"os"
	"path/filepath"
	"regexp"
	"slices"
	"strings"
	"time"
)

// Recovery when the browser has lost the session cookie. The running instance's secrets are in
// its memory only, so a relaunch cannot sign a browser in to it. Instead the relaunch asks it to
// quit through the per-user state folder: no network endpoint, and nothing secret on disk. The
// request names the asking process; the answer says what is in flight.
const (
	quitRequestName = "quit.request"
	quitAnswerName  = "quit.answer"
)

// quitPoll is how often the running instance looks for a request and a relaunch for the outcome;
// quitWait bounds a relaunch's wait; a request older than quitStale belongs to no waiting relaunch.
// Variables so tests can shorten them.
var (
	quitPoll  = 250 * time.Millisecond
	quitWait  = 10 * time.Second
	quitStale = 20 * time.Second
)

// busyAnswer is the only answer a relaunch shows, so nothing else written there reaches its dialog.
var busyAnswer = regexp.MustCompile(`^busy: [0-9]{1,6} runs?, [0-9]{1,6} reviews?$`)

// libraryQuitting refuses a review or Start once the library has agreed to quit for a relaunch.
const libraryQuitting = "Issuer Library is quitting for a new launch; use the window that launch opens."

func stale(modified time.Time) bool {
	age := time.Since(modified)
	return age > quitStale || age < -quitStale
}

func count(n int, noun string) string {
	if n == 1 {
		return "1 " + noun
	}
	return fmt.Sprintf("%d %ss", n, noun)
}

// clearQuitFiles removes a request or answer left by an instance or relaunch that has ended. A new
// instance calls it before it serves anything, so no relaunch is waiting on them.
func clearQuitFiles(state string) {
	for _, name := range []string{quitRequestName, quitAnswerName} {
		if err := os.Remove(filepath.Join(state, name)); err != nil && !errors.Is(err, fs.ErrNotExist) {
			log.Printf("Clear %s: %v", name, err)
		}
	}
}

// askToQuit asks this user's running instance to quit and waits, quitWait at most, for its port.
// It returns the port's listener once the instance has gone. Otherwise it returns the instance's
// busy answer, or errAlreadyRunning when the instance neither quits nor answers.
func askToQuit(state, host string) (net.Listener, error) {
	if err := privateFolder(state); err != nil {
		return nil, fmt.Errorf("Issuer Library is already running, and this launch does not ask it to quit: %v. Quit the running library (Settings > Quit library, or end Issuer Library in Task Manager), then start it again.", err)
	}
	request, answer := filepath.Join(state, quitRequestName), filepath.Join(state, quitAnswerName)
	_ = os.Remove(answer) // An answer to an earlier launch is not this launch's.
	mine := fmt.Sprintf("quit requested by process %d\n", os.Getpid())
	if placeQuitRequest(request, mine) {
		defer func() {
			// Withdrawn if the instance did not take it, unless another launch's replaced it.
			if raw, err := os.ReadFile(request); err == nil && string(raw) == mine {
				_ = os.Remove(request)
			}
		}()
	}
	for deadline := time.Now().Add(quitWait); ; time.Sleep(quitPoll) {
		if listener, err := net.Listen("tcp4", host); err == nil {
			return listener, nil
		}
		if status, ok := readQuitAnswer(answer); ok {
			_ = os.Remove(answer)
			return nil, fmt.Errorf("Issuer Library is busy (%s); wait for it to finish, then start it again.", strings.TrimPrefix(status, "busy: "))
		}
		if time.Now().After(deadline) {
			return nil, errAlreadyRunning
		}
	}
}

// placeQuitRequest creates the request, owner-only, and reports whether this launch created it. A
// stale request, or anything at that name that is not a plain file private to this user, is
// removed first (never followed); a fresh request of another launch is left for both to wait on.
func placeQuitRequest(request, content string) bool {
	if info, err := os.Lstat(request); err == nil && (!ownerOnly(info) || stale(info.ModTime())) {
		_ = os.Remove(request)
	}
	file, err := os.OpenFile(request, os.O_WRONLY|os.O_CREATE|os.O_EXCL, 0600)
	if err != nil {
		if !errors.Is(err, fs.ErrExist) {
			log.Printf("Quit request: %v", err)
		}
		return false
	}
	_, err = file.WriteString(content)
	if closeErr := file.Close(); err == nil {
		err = closeErr
	}
	if err != nil {
		log.Printf("Quit request: %v", err) // The file is the request; its text only names this launch.
	}
	return true
}

// readQuitAnswer returns the running instance's answer, if it has written a fresh, valid one.
func readQuitAnswer(answer string) (string, bool) {
	info, err := os.Lstat(answer)
	if err != nil || !info.Mode().IsRegular() || info.Size() > 256 || stale(info.ModTime()) {
		return "", false
	}
	raw, err := os.ReadFile(answer)
	var status string
	if err != nil || json.Unmarshal(raw, &status) != nil || !busyAnswer.MatchString(status) {
		return "", false
	}
	return status, true
}

// watchQuitRequests answers quit requests, looking every interval, until ctx ends or the library
// stops for one.
func (app *Application) watchQuitRequests(ctx context.Context, every time.Duration) {
	ticker := time.NewTicker(every)
	defer ticker.Stop()
	for {
		select {
		case <-ctx.Done():
			return
		case <-ticker.C:
			if app.answerQuitRequest() {
				return
			}
		}
	}
}

// answerQuitRequest acts on a quit request in the state folder, if there is one, and reports
// whether the library is stopping for it. Nothing is done while other users can write to the
// folder. A request that is stale, or not a plain file private to this user, is removed unread
// (a link is removed, never followed). With a run or review in flight the library keeps running
// and answers "busy: …"; otherwise it stops. A discovery or workspace change in progress defers
// the request to the next poll, so the index and settings are never cut off mid-write.
func (app *Application) answerQuitRequest() bool {
	request := filepath.Join(app.loc.State, quitRequestName)
	info, err := os.Lstat(request)
	if err != nil || privateFolder(app.loc.State) != nil {
		return false
	}
	if !ownerOnly(info) || stale(info.ModTime()) {
		if os.Remove(request) == nil {
			log.Print("Removed a stale or invalid quit request unread")
		}
		return false
	}
	if !app.refreshing.TryLock() {
		return false
	}
	app.mu.Lock()
	runs, reviews := len(app.activeJobs), app.reviews
	quitting := runs == 0 && reviews == 0
	app.quitting = quitting // From here no review or Start begins.
	app.mu.Unlock()
	if !quitting {
		app.refreshing.Unlock()
		status := fmt.Sprintf("busy: %s, %s", count(runs, "run"), count(reviews, "review"))
		if err = saveJSON(filepath.Join(app.loc.State, quitAnswerName), status); err != nil {
			log.Printf("Quit request answer: %v", err)
		}
		_ = os.Remove(request)
		log.Printf("A new launch asked the library to quit; it keeps running (%s)", status)
		return false
	}
	_ = os.Remove(request)
	log.Print("A new launch asked the idle library to quit; stopping")
	app.stop()
	return true // app.refreshing stays held: no discovery starts while the library stops.
}

// Windows well-known SIDs, as stored: revision 1, the number of sub-authorities, the 6-byte
// identifier authority (big endian), then each sub-authority (little endian).
var (
	sidSystem         = []byte{1, 1, 0, 0, 0, 0, 0, 5, 18, 0, 0, 0}                   // S-1-5-18
	sidAdministrators = []byte{1, 2, 0, 0, 0, 0, 0, 5, 32, 0, 0, 0, 0x20, 0x02, 0, 0} // S-1-5-32-544
	sidCreatorOwner   = []byte{1, 1, 0, 0, 0, 0, 0, 3, 0, 0, 0, 0}                    // S-1-3-0
	sidOwnerRights    = []byte{1, 1, 0, 0, 0, 0, 0, 3, 4, 0, 0, 0}                    // S-1-3-4
)

// folderWriteRights let their holder put a file in a folder, replace or delete one, or take the
// folder over: add file, add subfolder, delete child, delete, write DAC, write owner, generic all
// and generic write.
const folderWriteRights = 0x2 | 0x4 | 0x40 | 0x10000 | 0x40000 | 0x80000 | 0x10000000 | 0x40000000

// othersMayWrite reports whether a Windows access-control list, as stored (an 8-byte header, then
// its entries), grants folderWriteRights to any SID not in trusted. A deny entry grants nothing.
// An allow entry of another kind (callback, object) is not judged here and a malformed list is not
// trusted, so both count as writable by others.
func othersMayWrite(acl []byte, trusted [][]byte) bool {
	if len(acl) < 8 {
		return true
	}
	entries := acl[8:]
	for remaining := binary.LittleEndian.Uint16(acl[4:]); remaining > 0; remaining-- {
		if len(entries) < 4 {
			return true
		}
		kind, size := entries[0], int(binary.LittleEndian.Uint16(entries[2:]))
		if size < 4 || size > len(entries) {
			return true
		}
		entry := entries[:size]
		entries = entries[size:]
		if kind == 1 { // ACCESS_DENIED_ACE_TYPE
			continue
		}
		// ACCESS_ALLOWED_ACE_TYPE: the 4-byte header, the access mask, then the SID.
		if kind != 0 || size < 16 || size < 16+4*int(entry[9]) {
			return true
		}
		sid := entry[8 : 16+4*int(entry[9])]
		if binary.LittleEndian.Uint32(entry[4:])&folderWriteRights != 0 && !slices.ContainsFunc(trusted, func(t []byte) bool { return bytes.Equal(t, sid) }) {
			return true
		}
	}
	return false
}
