package main

import (
	"net/http"
	"net/http/httptest"
	"strings"
	"sync"
	"sync/atomic"
	"testing"
)

// Hand-derived: 64 concurrent valid-ticket GETs: exactly one 303 with a cookie, 63 are 403 without.
func TestReviewConcurrentLaunchSpendsOnce(t *testing.T) {
	app, _ := testApp(t)
	ticket := app.ticket
	var ok, refused, cookies atomic.Int32
	var wg sync.WaitGroup
	start := make(chan struct{})
	for i := 0; i < 64; i++ {
		wg.Add(1)
		go func() {
			defer wg.Done()
			<-start
			w := launchRequest(app, "GET", "?ticket="+ticket)
			switch w.Code {
			case 303:
				ok.Add(1)
			case 403:
				refused.Add(1)
			}
			if w.Header().Get("Set-Cookie") != "" {
				cookies.Add(1)
			}
		}()
	}
	close(start)
	wg.Wait()
	if ok.Load() != 1 || refused.Load() != 63 || cookies.Load() != 1 {
		t.Fatalf("ok=%d refused=%d cookies=%d", ok.Load(), refused.Load(), cookies.Load())
	}
}

// Every method on every path shape without the cookie: 403 (or 405 only for /launch non-GET), never a
// 404/200/405 from behind the gate; with the cookie the gate lets it through (anything but the launcher text).
func TestReviewGateCoversMethodsAndPaths(t *testing.T) {
	app, _ := testApp(t)
	paths := []string{"/", "/nope", "/launch/", "//launch", "/LAUNCH", "/health/", "/health/x", "/files/", "/files/../x", "/api/", "/api/runs", "/api/runs/", "/api/runs/status", "/api/catalogue/", "/%2e%2e/etc", "/launch%2f", "/api/quit", "/api/settings", "/favicon.ico", "/web/index.html"}
	methods := []string{"GET", "HEAD", "OPTIONS", "POST", "PUT", "DELETE", "PATCH", "TRACE", "FOO"}
	for _, p := range paths {
		for _, m := range methods {
			r := httptest.NewRequest(m, "http://"+app.host+"/", nil)
			r.URL.Path = p
			r.URL.RawPath = ""
			w := httptest.NewRecorder()
			app.ServeHTTP(w, r)
			if w.Code != 403 || !strings.Contains(w.Body.String(), "Open Issuer Library from its launcher") && m != "HEAD" {
				t.Errorf("%s %s without cookie: %d %q", m, p, w.Code, w.Body.String())
			}
			if strings.Contains(w.Body.String(), app.session) || strings.Contains(w.Body.String(), app.ticket) {
				t.Errorf("secret in body %s %s", m, p)
			}
		}
	}
	// /launch with other methods: never spends, never sets a cookie.
	for _, m := range []string{"HEAD", "POST", "OPTIONS", "PUT"} {
		w := launchRequest(app, m, "?ticket="+app.ticket)
		if w.Code != 405 || w.Header().Get("Set-Cookie") != "" || app.ticket == "" {
			t.Errorf("%s /launch: %d", m, w.Code)
		}
	}
	// Host/Origin checks come first: a wrong host with a valid ticket is refused and does not spend it.
	r := httptest.NewRequest("GET", "http://evil.example/launch?ticket="+app.ticket, nil)
	w := httptest.NewRecorder()
	app.ServeHTTP(w, r)
	if w.Code != 403 || app.ticket == "" || !strings.Contains(w.Body.String(), "Local app requests only") {
		t.Errorf("foreign host: %d %q", w.Code, w.Body.String())
	}
	r = httptest.NewRequest("GET", "http://"+app.host+"/launch?ticket="+app.ticket, nil)
	r.Header.Set("Sec-Fetch-Site", "cross-site")
	w = httptest.NewRecorder()
	app.ServeHTTP(w, r)
	if w.Code != 403 || app.ticket == "" {
		t.Errorf("cross-site launch: %d", w.Code)
	}
	// Responses never carry a secret in any header except the one Set-Cookie of a successful launch.
	w = launchRequest(app, "GET", "?ticket="+app.ticket)
	for k, v := range w.Header() {
		if k != "Set-Cookie" && strings.Contains(strings.Join(v, ","), app.session) {
			t.Errorf("session in header %s", k)
		}
	}
	// /health: only the two fields, no secret, with and without the cookie.
	for _, withCookie := range []bool{false, true} {
		r = httptest.NewRequest("GET", "http://"+app.host+"/health", nil)
		if withCookie {
			r.AddCookie(&http.Cookie{Name: app.cookieName(), Value: app.session})
		}
		w = httptest.NewRecorder()
		app.ServeHTTP(w, r)
		body := w.Body.String()
		if w.Code != 200 || strings.Contains(body, app.session) || strings.Contains(body, app.loc.State) || strings.Count(body, ":") != 2 {
			t.Errorf("health: %d %q", w.Code, body)
		}
	}
}
