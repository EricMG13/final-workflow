package main

import (
	"context"
	"encoding/json"
	"flag"
	"fmt"
	"hash/crc32"
	"log"
	"net"
	"net/http"
	"os"
	"os/signal"
	"path/filepath"
	"sync"
	"time"
)

// launchBrowser opens a URL in the user's browser; a variable so tests can see what is opened.
var launchBrowser = openBrowser

// run starts the library with the command-line arguments (without the program name). Its flags
// are its own, so a test can run two launches at once.
func run(arguments []string) (err error) {
	flags := flag.NewFlagSet(os.Args[0], flag.ExitOnError)
	workspace := flags.String("workspace", "", "Workspace folder (disabled by IT policy)")
	state := flags.String("state-dir", "", "Override per-user state directory for testing")
	noBrowser := flags.Bool("no-browser", false, "Start without opening a browser")
	port := flags.Int("port", 0, "Loopback port; zero selects a stable per-user port")
	if err = flags.Parse(arguments); err != nil {
		return err
	}
	loc, err := platformLocations()
	if err != nil {
		return err
	}
	if *state != "" {
		loc.State, err = filepath.Abs(*state)
		if err != nil {
			return err
		}
	}
	if err = os.MkdirAll(loc.State, 0700); err != nil {
		return err
	}
	logPath := filepath.Join(loc.State, "library.log")
	if info, err := os.Stat(logPath); err == nil && info.Size() > 1<<20 {
		_ = os.Rename(logPath, logPath+".previous")
	}
	logFile, err := os.OpenFile(logPath, os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0600)
	if err != nil {
		return err
	}
	log.SetOutput(logFile)
	defer func() {
		// main reports the error once this file is closed, so record it here first.
		if err != nil {
			log.Print(err)
		}
		log.SetOutput(os.Stderr)
		logFile.Close()
	}()
	if *port == 0 {
		*port = 49000 + int(crc32.ChecksumIEEE([]byte(loc.State))%10000)
	}
	if *port < 1024 || *port > 65535 {
		return fmt.Errorf("port must be between 1024 and 65535")
	}
	host := fmt.Sprintf("127.0.0.1:%d", *port)
	address := "http://" + host
	listener, err := net.Listen("tcp4", host)
	if err != nil {
		if !instanceAnswers(address, loc.State) {
			return fmt.Errorf("local port is occupied by another application: %w", err)
		}
		// This user's instance answers. Its session secret is in its memory only, so this launch
		// cannot sign a browser in to it; it asks the instance to quit instead (quit.go).
		if listener, err = askToQuit(loc.State, host); err != nil {
			return err
		}
	}
	defer listener.Close()
	clearQuitFiles(loc.State)
	app, err := newApplication(loc, *workspace)
	if err != nil {
		return err
	}
	app.host = host
	server := &http.Server{Handler: app, ReadHeaderTimeout: 5 * time.Second, ReadTimeout: 150 * time.Second, WriteTimeout: 180 * time.Second, IdleTimeout: 30 * time.Second, MaxHeaderBytes: 16384}
	ctx, cancel := signal.NotifyContext(context.Background(), os.Interrupt)
	// run returns only once the periodic refresh and the quit watcher have ended, so neither
	// outlives the library: a discovery in progress finishes its index first. cancel comes first
	// and also restores the default interrupt, so a second Ctrl+C ends a wait that is too long.
	var background sync.WaitGroup
	defer func() { cancel(); background.Wait() }()
	app.stop = cancel
	stopped := make(chan struct{})
	go func() {
		<-ctx.Done()
		shutdownCtx, done := context.WithTimeout(context.Background(), 3*time.Second)
		defer done()
		_ = server.Shutdown(shutdownCtx)
		close(stopped)
	}()
	background.Go(func() { app.refreshPeriodically(ctx, refreshPoll) })
	background.Go(func() { app.watchQuitRequests(ctx, quitPoll) })
	// The one-time launch link goes to the browser, or with --no-browser to standard output for
	// whoever started the library; never to library.log.
	launch := app.launchURL()
	if *noBrowser {
		fmt.Println("Issuer Library:", launch)
	} else {
		fmt.Println("Issuer Library:", address)
		go func() {
			if err := launchBrowser(launch); err != nil {
				log.Printf("Open browser: %v", err)
				showError("Open this link in your browser within 2 minutes; it works once:\n" + launch + "\n" + err.Error())
			}
		}()
	}
	log.Printf("Listening at %s", address)
	err = server.Serve(listener)
	if err == http.ErrServerClosed {
		<-stopped // Requests in flight finish first, for 3 seconds at most.
		return nil
	}
	return err
}

func main() {
	if err := run(os.Args[1:]); err != nil {
		log.Print(err)
		showError(err.Error())
		os.Exit(1)
	}
}

// instanceAnswers reports whether this user's instance answers /health at address. A simultaneous
// launch may have bound the port but not started serving yet, so it asks up to five times.
func instanceAnswers(address, state string) bool {
	client := http.Client{Timeout: 2 * time.Second, Transport: &http.Transport{Proxy: nil}, CheckRedirect: func(*http.Request, []*http.Request) error { return http.ErrUseLastResponse }}
	for attempt := 0; attempt < 5; attempt++ {
		response, requestErr := client.Get(address + "/health")
		if requestErr == nil {
			var health map[string]string
			decodeErr := json.NewDecoder(http.MaxBytesReader(nil, response.Body, 4096)).Decode(&health)
			response.Body.Close()
			if decodeErr == nil && health["application"] == "finalworkflow-issuer-library/1" && health["instance"] == digest([]byte(state)) {
				return true
			}
		}
		time.Sleep(200 * time.Millisecond)
	}
	return false
}
