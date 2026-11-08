package main

import (
	"errors"
	"io/fs"
	"os"
	"path/filepath"
	"sync"
	"testing"
)

// spawn runs f on a goroutine counted by group, as sync.WaitGroup.Go does from Go 1.25, so the
// tests build with Go 1.24.
func spawn(group *sync.WaitGroup, f func()) {
	group.Add(1)
	go func() {
		defer group.Done()
		f()
	}()
}

func TestMkdirAllInCreatesNestedAndAcceptsExisting(t *testing.T) {
	dir := t.TempDir()
	root, err := os.OpenRoot(dir)
	if err != nil {
		t.Fatal(err)
	}
	defer root.Close()
	if err := mkdirAllIn(root, "intake/job/sources/a", 0700); err != nil {
		t.Fatalf("create nested: %v", err)
	}
	if info, err := os.Stat(filepath.Join(dir, "intake", "job", "sources", "a")); err != nil || !info.IsDir() {
		t.Fatalf("nested directory missing: %v", err)
	}
	if err := mkdirAllIn(root, "intake/job", 0700); err != nil {
		t.Fatalf("existing directory refused: %v", err)
	}
	if err := mkdirAllIn(root, ".", 0700); err != nil {
		t.Fatalf("root itself refused: %v", err)
	}
}

func TestMkdirAllInRefusesFilesAndEscapes(t *testing.T) {
	dir := t.TempDir()
	root, err := os.OpenRoot(dir)
	if err != nil {
		t.Fatal(err)
	}
	defer root.Close()
	if err := os.WriteFile(filepath.Join(dir, "file"), []byte("x"), 0600); err != nil {
		t.Fatal(err)
	}
	if err := mkdirAllIn(root, "file/child", 0700); err == nil {
		t.Fatal("a file component was accepted as a directory")
	}
	for _, name := range []string{"../outside", "/abs", "a/../../b", ""} {
		if err := mkdirAllIn(root, name, 0700); !errors.Is(err, fs.ErrInvalid) {
			t.Fatalf("%q: want ErrInvalid, got %v", name, err)
		}
	}
	outside := t.TempDir()
	if err := os.Symlink(outside, filepath.Join(dir, "link")); err != nil {
		t.Skip("symlinks unavailable:", err)
	}
	if err := mkdirAllIn(root, "link/escaped", 0700); err == nil {
		t.Fatal("a symlink out of the root was followed")
	}
	if _, err := os.Stat(filepath.Join(outside, "escaped")); err == nil {
		t.Fatal("a directory was created outside the root")
	}
}
