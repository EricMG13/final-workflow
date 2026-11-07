//go:build windows

package main

import (
	"errors"
	"fmt"
	"os"
	"os/exec"
	"path/filepath"
	"syscall"
	"unsafe"
)

type guid struct {
	A    uint32
	B, C uint16
	D    [8]byte
}

func knownFolder(id guid) (string, error) {
	var pointer *uint16
	result, _, _ := syscall.NewLazyDLL("shell32.dll").NewProc("SHGetKnownFolderPath").Call(uintptr(unsafe.Pointer(&id)), 0, 0, uintptr(unsafe.Pointer(&pointer)))
	if result != 0 {
		return "", fmt.Errorf("Windows known folder lookup failed: 0x%x", result)
	}
	defer syscall.NewLazyDLL("ole32.dll").NewProc("CoTaskMemFree").Call(uintptr(unsafe.Pointer(pointer)))
	// Windows paths cannot exceed the NT path limit.
	units := unsafe.Slice(pointer, 32768)
	length := 0
	for length < len(units) && units[length] != 0 {
		length++
	}
	return syscall.UTF16ToString(units[:length]), nil
}

func platformLocations() (Locations, error) {
	local, err := knownFolder(guid{0xF1B32785, 0x6FBA, 0x4FCF, [8]byte{0x9D, 0x55, 0x7B, 0x8E, 0x7F, 0x15, 0x70, 0x91}})
	if err != nil {
		return Locations{}, err
	}
	common, err := knownFolder(guid{0x62AB5D82, 0xFDC1, 0x4DC3, [8]byte{0xA9, 0xDD, 0x07, 0x0D, 0x1D, 0x49, 0x5D, 0x97}})
	if err != nil {
		return Locations{}, err
	}
	documents, err := knownFolder(guid{0xFDD39AD0, 0x238F, 0x46AF, [8]byte{0xAD, 0xB4, 0x6C, 0x85, 0x48, 0x03, 0x69, 0xC7}})
	if err != nil {
		return Locations{}, err
	}
	return Locations{State: filepath.Join(local, "FinalWorkflow", "IssuerLibrary"), Policy: filepath.Join(common, "FinalWorkflow", "IssuerLibrary", "settings.json"), Documents: documents}, nil
}

func openBrowser(url string) error {
	return exec.Command("rundll32.exe", "url.dll,FileProtocolHandler", url).Start()
}
func showError(message string) {
	text, _ := syscall.UTF16PtrFromString(message)
	title, _ := syscall.UTF16PtrFromString("Issuer Library")
	syscall.NewLazyDLL("user32.dll").NewProc("MessageBoxW").Call(0, uintptr(unsafe.Pointer(text)), uintptr(unsafe.Pointer(title)), 0x10)
}

func configureWorkerCommand(command *exec.Cmd) {
	command.SysProcAttr = &syscall.SysProcAttr{CreationFlags: 0x08000000}
}

const errorSharingViolation syscall.Errno = 32

// holdWorkerLock creates the worker lock at name, open without write sharing, as a handle for
// command to inherit. While the worker (or this app, until it closes its copy) has it open,
// nobody can open the file for writing; Windows closes the worker's handle when the worker ends,
// however it ends, so the lock lasts exactly as long as the worker process, past this app.
func holdWorkerLock(command *exec.Cmd, name string) (*os.File, error) {
	path, err := syscall.UTF16PtrFromString(name)
	if err != nil {
		return nil, err
	}
	inherit := syscall.SecurityAttributes{Length: uint32(unsafe.Sizeof(syscall.SecurityAttributes{})), InheritHandle: 1}
	handle, err := syscall.CreateFile(path, syscall.GENERIC_READ, syscall.FILE_SHARE_READ, &inherit, syscall.OPEN_ALWAYS, syscall.FILE_ATTRIBUTE_NORMAL, 0)
	if err != nil {
		return nil, err
	}
	command.SysProcAttr.AdditionalInheritedHandles = append(command.SysProcAttr.AdditionalInheritedHandles, handle)
	return os.NewFile(uintptr(handle), name), nil
}

// workerAlive reports whether a worker still holds the lock at name. A missing lock means no
// worker ever held one.
func workerAlive(name string) (bool, error) {
	path, err := syscall.UTF16PtrFromString(name)
	if err != nil {
		return false, err
	}
	handle, err := syscall.CreateFile(path, syscall.GENERIC_WRITE, syscall.FILE_SHARE_READ|syscall.FILE_SHARE_WRITE, nil, syscall.OPEN_EXISTING, syscall.FILE_ATTRIBUTE_NORMAL, 0)
	switch {
	case err == nil:
		syscall.CloseHandle(handle)
		return false, nil
	case errors.Is(err, syscall.ERROR_FILE_NOT_FOUND):
		return false, nil
	case errors.Is(err, errorSharingViolation):
		return true, nil
	}
	return false, err
}
