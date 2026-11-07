package main

import (
	"crypto/rand"
	"crypto/subtle"
	"encoding/hex"
	"errors"
	"net"
	"net/http"
	"time"
)

// The per-launch secret. Host, Origin, Sec-Fetch-Site and the custom header stop browsers and
// DNS rebinding, but any local process (another user's, on a shared Windows host) can set them.
// So each launch makes two random values held in memory only: a one-time ticket, carried once in
// the URL the launcher opens, and a session secret the browser receives as a cookie in exchange.
// Neither is written to disk, the log, settings, the index or any response body.

// ticketLifetime is how long the launch ticket works after the library is ready: time for a
// browser to start on a slow machine, and a short window for a ticket other local users may read
// on the browser opener's command line (on a shared Linux or macOS host).
const ticketLifetime = 120 * time.Second

// clock is time.Now; a variable so tests can move it.
var clock = time.Now

// launcherOnly is the whole answer to a request without the session cookie.
const launcherOnly = "Open Issuer Library from its launcher. This page is not part of the library's current session. If the library is already running, start it again: a library with no run or review in progress quits and the new launch opens a fresh window."

// errAlreadyRunning is what a second launch reports when the running instance neither quits nor
// answers its quit request (quit.go): its secret is in its memory only, so this launch cannot sign
// a browser in to it and opens no window.
var errAlreadyRunning = errors.New("Issuer Library is already running and did not quit for this launch. Quit the running library (Settings > Quit library, or end Issuer Library in Task Manager), then start it again.")

// randomSecret returns 32 random bytes from crypto/rand, hex encoded.
func randomSecret() (string, error) {
	raw := make([]byte, 32)
	if _, err := rand.Read(raw); err != nil {
		return "", err
	}
	return hex.EncodeToString(raw), nil
}

// launchURL is the address the launcher opens: it carries the ticket, which works once.
func (app *Application) launchURL() string {
	app.launch.Lock()
	defer app.launch.Unlock()
	return "http://" + app.host + "/launch?ticket=" + app.ticket
}

// cookieName holds the port: cookies are not kept apart by port, so a second instance on another
// port must not replace this one's cookie.
func (app *Application) cookieName() string {
	_, port, _ := net.SplitHostPort(app.host)
	return "issuer-library-" + port
}

// authorized reports whether r carries this launch's session cookie, compared in constant time.
// Every cookie of that name is checked, so one set for a narrower path cannot shadow it.
func (app *Application) authorized(r *http.Request) bool {
	for _, cookie := range r.CookiesNamed(app.cookieName()) {
		if subtle.ConstantTimeCompare([]byte(cookie.Value), []byte(app.session)) == 1 {
			return true
		}
	}
	return false
}

// serveLaunch exchanges the one-time ticket for the session cookie and redirects to the app, so
// the ticket leaves the address bar. Only GET exchanges it: a HEAD or a prefetch does not spend it.
// A wrong ticket does not spend it either; a guess of 256 random bits cannot succeed. From
// ticketLifetime after start the ticket is gone: refused, and never accepted again.
func (app *Application) serveLaunch(w http.ResponseWriter, r *http.Request) {
	if r.Method != http.MethodGet {
		http.Error(w, "Method not allowed", http.StatusMethodNotAllowed)
		return
	}
	app.launch.Lock()
	if !clock().Before(app.expires) {
		app.ticket = ""
	}
	valid := app.ticket != "" && subtle.ConstantTimeCompare([]byte(r.URL.Query().Get("ticket")), []byte(app.ticket)) == 1
	if valid {
		app.ticket = ""
	}
	app.launch.Unlock()
	if !valid {
		http.Error(w, launcherOnly, http.StatusForbidden)
		return
	}
	// Plain loopback HTTP has no TLS, so the cookie is not marked Secure. It has no expiry: it
	// lasts for the browser session and the secret only for this launch.
	http.SetCookie(w, &http.Cookie{Name: app.cookieName(), Value: app.session, Path: "/", HttpOnly: true, SameSite: http.SameSiteStrictMode})
	http.Redirect(w, r, "/", http.StatusSeeOther)
}
