//go:build windows

package main

import (
	"bytes"
	"context"
	"encoding/binary"
	"errors"
	"fmt"
	"io/fs"
	"log"
	"os"
	"os/exec"
	"path/filepath"
	"syscall"
	"time"
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

// privateFolder returns an error unless only this user, SYSTEM and Administrators may write to the
// folder name, according to its access-control list. The per-user local application data folder
// is private this way by default. Permission bits do not describe access on Windows.
func privateFolder(name string) error {
	path, err := syscall.UTF16PtrFromString(name)
	if err != nil {
		return err
	}
	var acl unsafe.Pointer
	var descriptor syscall.Handle
	// GetNamedSecurityInfoW(name, SE_FILE_OBJECT, DACL_SECURITY_INFORMATION, ...)
	result, _, _ := syscall.NewLazyDLL("advapi32.dll").NewProc("GetNamedSecurityInfoW").Call(uintptr(unsafe.Pointer(path)), 1, 4, 0, 0, uintptr(unsafe.Pointer(&acl)), 0, uintptr(unsafe.Pointer(&descriptor)))
	if result != 0 {
		return fmt.Errorf("the state folder's permissions cannot be read: %w", syscall.Errno(result))
	}
	defer syscall.LocalFree(descriptor)
	if acl == nil { // A null DACL gives everyone full access.
		return fmt.Errorf("everyone can write to the state folder %s", name)
	}
	size := binary.LittleEndian.Uint16(unsafe.Slice((*byte)(acl), 4)[2:])
	list := bytes.Clone(unsafe.Slice((*byte)(acl), size))
	token, err := syscall.OpenCurrentProcessToken()
	if err != nil {
		return err
	}
	defer token.Close()
	user, err := token.GetTokenUser()
	if err != nil {
		return err
	}
	sid := bytes.Clone(unsafe.Slice((*byte)(unsafe.Pointer(user.User.Sid)), syscall.GetLengthSid(user.User.Sid)))
	if othersMayWrite(list, [][]byte{sid, sidSystem, sidAdministrators, sidCreatorOwner, sidOwnerRights}) {
		return fmt.Errorf("other users can write to the state folder %s", name)
	}
	return nil
}

// ownerOnly reports whether info describes a plain file (not a link or other reparse point). Its
// access comes from the state folder, which privateFolder has checked.
func ownerOnly(info fs.FileInfo) bool { return info.Mode().IsRegular() }

// systemDirectory is the Windows system folder from GetSystemDirectoryW, not from the environment.
func systemDirectory() (string, error) {
	buffer := make([]uint16, syscall.MAX_PATH)
	length, _, err := syscall.NewLazyDLL("kernel32.dll").NewProc("GetSystemDirectoryW").Call(uintptr(unsafe.Pointer(&buffer[0])), uintptr(len(buffer)))
	if length == 0 || int(length) >= len(buffer) {
		return "", fmt.Errorf("Windows system folder lookup failed: %v", err)
	}
	return syscall.UTF16ToString(buffer[:length]), nil
}

// powershellPath is the system PowerShell by absolute path. There is no PATH fallback: if it is
// missing the notice fails, and the caller logs that.
func powershellPath() (string, error) {
	directory, err := systemDirectory()
	if err != nil {
		return "", err
	}
	path := filepath.Join(directory, "WindowsPowerShell", "v1.0", "powershell.exe")
	if _, err = os.Stat(path); err != nil {
		return "", err
	}
	return path, nil
}

// platformNotify shows a toast through PowerShell running the fixed toastScript; the text goes
// in environment variables only. A failure is returned for the caller to log, never to act on.
func platformNotify(title, body string) error {
	program, err := powershellPath()
	if err != nil {
		return err
	}
	ctx, cancel := context.WithTimeout(context.Background(), 20*time.Second)
	defer cancel()
	cmd := exec.CommandContext(ctx, program, "-NoProfile", "-NonInteractive", "-ExecutionPolicy", "Bypass", "-Command", toastScript)
	cmd.Env = toastEnv(os.Environ(), title, body)
	configureWorkerCommand(cmd)
	if output, err := cmd.CombinedOutput(); err != nil {
		log.Printf("PowerShell toast output: %s", output)
		return err
	}
	return nil
}
