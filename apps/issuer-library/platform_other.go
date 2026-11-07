//go:build !windows

package main

import (
	"errors"
	"fmt"
	"io/fs"
	"os"
	"os/exec"
	"path/filepath"
	"runtime"
	"syscall"
)

func platformLocations() (Locations, error) {
	config, err := os.UserConfigDir()
	if err != nil {
		return Locations{}, err
	}
	home, err := os.UserHomeDir()
	if err != nil {
		return Locations{}, err
	}
	return Locations{State: filepath.Join(config, "FinalWorkflow", "IssuerLibrary"), Documents: filepath.Join(home, "Documents")}, nil
}
func openBrowser(url string) error {
	program := "xdg-open"
	if runtime.GOOS == "darwin" {
		program = "open"
	}
	return exec.Command(program, url).Start()
}
func showError(message string) { fmt.Fprintln(os.Stderr, message) }

func configureWorkerCommand(command *exec.Cmd) {}

// holdWorkerLock creates the worker lock at name, locked, for command to inherit. A flock belongs
// to the open file, which the worker shares, so the lock lasts exactly as long as the worker
// process, past this app, and is released when the worker ends however it ends. The caller
// closes its own copy once the worker has started.
func holdWorkerLock(command *exec.Cmd, name string) (*os.File, error) {
	file, err := os.OpenFile(name, os.O_RDWR|os.O_CREATE, 0600)
	if err != nil {
		return nil, err
	}
	if err = syscall.Flock(int(file.Fd()), syscall.LOCK_EX|syscall.LOCK_NB); err != nil {
		file.Close()
		return nil, err
	}
	command.ExtraFiles = append(command.ExtraFiles, file)
	return file, nil
}

// workerAlive reports whether a worker still holds the lock at name. A missing lock means no
// worker ever held one.
func workerAlive(name string) (bool, error) {
	file, err := os.Open(name)
	if errors.Is(err, fs.ErrNotExist) {
		return false, nil
	}
	if err != nil {
		return false, err
	}
	defer file.Close() // Also releases this check's own lock.
	err = syscall.Flock(int(file.Fd()), syscall.LOCK_EX|syscall.LOCK_NB)
	if errors.Is(err, syscall.EWOULDBLOCK) {
		return true, nil
	}
	return false, err
}

// privateFolder returns an error unless name is a folder of this user's that no other user can
// write to (no group or world write bit).
func privateFolder(name string) error {
	info, err := os.Stat(name)
	if err != nil {
		return err
	}
	if stat, ok := info.Sys().(*syscall.Stat_t); !info.IsDir() || !ok || int(stat.Uid) != os.Getuid() {
		return fmt.Errorf("the state folder %s does not belong to this user", name)
	}
	if info.Mode().Perm()&0o022 != 0 {
		return fmt.Errorf("other users can write to the state folder %s", name)
	}
	return nil
}

// ownerOnly reports whether info describes a plain file of this user's that only they can read or
// write, as a relaunch creates its quit request.
func ownerOnly(info fs.FileInfo) bool {
	stat, ok := info.Sys().(*syscall.Stat_t)
	return info.Mode().IsRegular() && ok && int(stat.Uid) == os.Getuid() && info.Mode().Perm()&0o077 == 0
}
