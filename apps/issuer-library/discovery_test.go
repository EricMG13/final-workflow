package main

import (
	"crypto/sha256"
	"encoding/hex"
	"encoding/json"
	"fmt"
	"os"
	"path/filepath"
	"slices"
	"strings"
	"testing"
)

func put(t *testing.T, root, name string, raw []byte) {
	t.Helper()
	file := filepath.Join(root, filepath.FromSlash(name))
	if err := os.MkdirAll(filepath.Dir(file), 0700); err != nil {
		t.Fatal(err)
	}
	if err := os.WriteFile(file, raw, 0600); err != nil {
		t.Fatal(err)
	}
}
func putJSON(t *testing.T, root, name string, value any) {
	t.Helper()
	raw, err := json.Marshal(value)
	if err != nil {
		t.Fatal(err)
	}
	put(t, root, name, raw)
}
func fixture(t *testing.T) (string, Manifest) {
	t.Helper()
	root := t.TempDir()
	raw := []byte("Issuer: Example Industries\nSector: Industrials\nRevenue: 0\nVerified scope\n")
	put(t, root, "runs/case-a/CP-0.md", raw)
	run := blankRun("case-a")
	run.Issuer = "EX"
	run.Name = "Example Industries"
	run.IdentitySource = "identity"
	run.Sector = "Industrials"
	run.SectorSource = "sector"
	run.Date = "2024-12-31"
	run.Period = "FY2024"
	run.Handoff = "runs/case-a/CP-0.md"
	run.Metrics["revenue"] = &Metric{Value: "0", Unit: "USD m", Period: "FY2024", Basis: "Reported revenue", Source: "revenue"}
	manifest := Manifest{Schema: "issuer-library-run/1", Run: run, Sources: map[string]Source{}}
	for key, number := range map[string]int{"identity": 1, "sector": 2, "revenue": 3, "check": 4} {
		manifest.Sources[key] = Source{Path: "runs/case-a/CP-0.md", SHA256: digest(raw), Line: number, Quote: strings.Split(string(raw), "\n")[number-1]}
	}
	putJSON(t, root, "runs/case-a/library.json", manifest)
	return root, manifest
}
func addDelivery(t *testing.T, root, folder, id, issuer string) {
	t.Helper()
	var view deliveryView
	view.Run.RunID = id
	view.Run.IssuerID = issuer
	view.Run.IssuerName = "Example Industries"
	view.Run.AsOf = "2024-12-31"
	view.Mode = "candidate"
	raw, _ := json.Marshal(view)
	report := []byte("<!doctype html><title>Report</title><p>Retained report</p>")
	put(t, root, "deliverables/"+folder+"/view.json", raw)
	put(t, root, "deliverables/"+folder+"/report.html", report)
	putJSON(t, root, "deliverables/"+folder+"/delivery.json", map[string]any{"files": map[string]string{"view.json": digest(raw), "report.html": digest(report)}})
}

func TestDiscoveryPreservesZeroAndFindsNewRun(t *testing.T) {
	root, _ := fixture(t)
	cat := discover(root, Catalogue{})
	if len(cat.Issues) != 0 || len(cat.Real) != 1 {
		t.Fatalf("%+v", cat)
	}
	run := cat.Real[0]
	if run.Metrics["revenue"].Value != "0" || run.Metrics["revenue"].Period != "FY2024" || run.Completion != nil {
		t.Fatalf("lost semantics: %+v", run)
	}
	put(t, root, "runs/new-case/CP-0.md", []byte("New evidence"))
	cat = discover(root, Catalogue{})
	if len(cat.Real) != 2 {
		t.Fatal("new run not discovered")
	}
	if cat.Real[1].Issuer != "Unclassified" {
		t.Fatal("filename became issuer identity")
	}
}

func TestChangedAndMalformedMetadataRemainVisible(t *testing.T) {
	root, _ := fixture(t)
	put(t, root, "runs/case-a/CP-0.md", []byte("changed"))
	cat := discover(root, Catalogue{})
	if len(cat.Real) != 1 || len(cat.Issues) == 0 || len(cat.Real[0].Metrics) != 0 || len(cat.Sources) != 0 {
		t.Fatal("bad summary leaked")
	}
	put(t, root, "runs/case-a/library.json", []byte("{"))
	cat = discover(root, Catalogue{})
	if len(cat.Real) != 1 || len(cat.Issues) == 0 {
		t.Fatal("partial manifest disappeared")
	}
}

func TestMetricCannotLoseBasisOrInventValue(t *testing.T) {
	for _, change := range []func(*Metric){func(m *Metric) { m.Value = "1" }, func(m *Metric) { m.Value = "NaN" }, func(m *Metric) { m.Basis = "" }, func(m *Metric) { m.Period = "" }, func(m *Metric) { m.Source = "missing" }} {
		root, m := fixture(t)
		change(m.Run.Metrics["revenue"])
		putJSON(t, root, "runs/case-a/library.json", m)
		cat := discover(root, Catalogue{})
		if len(cat.Issues) == 0 || len(cat.Real[0].Metrics) != 0 {
			t.Fatal("invalid metric admitted")
		}
	}
}

func TestMetricProvenanceIsOnlyProducerDeclared(t *testing.T) {
	for _, kind := range []string{"", "cited", "calculated", "synthetic", "user", "unknown", "C1"} {
		t.Run("classification_"+kind, func(t *testing.T) {
			root, manifest := fixture(t)
			manifest.Run.Metrics["revenue"].Provenance = kind
			putJSON(t, root, "runs/case-a/library.json", manifest)
			cat := discover(root, Catalogue{})
			if kind == "unknown" || kind == "C1" {
				if len(cat.Issues) == 0 || len(cat.Real[0].Metrics) != 0 {
					t.Fatal("unsupported provenance admitted")
				}
				return
			}
			metric := cat.Real[0].Metrics["revenue"]
			if len(cat.Issues) != 0 || metric == nil || metric.Provenance != kind || metric.Value != "0" {
				t.Fatalf("classification inferred or exact zero lost: %+v", cat)
			}
		})
	}
}

func TestChecklistRequiresAllStagesAndPins(t *testing.T) {
	root, m := fixture(t)
	raw := `{"scope":"Annual review","requirements":[{"id":"s","stage":"sources","done":true,"evidence":["check"]},{"id":"a","stage":"analysis","done":true,"evidence":["check"]},{"id":"v","stage":"verification","done":false},{"id":"c","stage":"downstream","done":false},{"id":"d","stage":"delivery","done":false}]}`
	if err := json.Unmarshal([]byte(raw), &m.Checklist); err != nil {
		t.Fatal(err)
	}
	putJSON(t, root, "runs/case-a/library.json", m)
	cat := discover(root, Catalogue{})
	if cat.Real[0].Completion == nil || *cat.Real[0].Completion != 40 {
		t.Fatalf("wrong independent 2/5 score: %+v", cat.Issues)
	}
	m.Checklist.Requirements[0].Evidence = nil
	putJSON(t, root, "runs/case-a/library.json", m)
	cat = discover(root, Catalogue{})
	if cat.Real[0].Completion != nil || len(cat.Issues) == 0 {
		t.Fatal("unsubstantiated completion admitted")
	}
	if _, err := assessChecklist(Checklist{Scope: "empty"}, map[string]Source{}); err == nil {
		t.Fatal("empty checklist admitted")
	}
}

func TestDeliveryRevisionIdentityAndCorruption(t *testing.T) {
	root, _ := fixture(t)
	addDelivery(t, root, "revision-1", "case-a", "EX")
	addDelivery(t, root, "revision-2", "different-run", "EX")
	cat := discover(root, Catalogue{})
	if len(cat.Real) != 2 {
		t.Fatalf("unrelated report must have its own row: %d", len(cat.Real))
	}
	var run Run
	for _, r := range cat.Real {
		if r.ID == "case-a" {
			run = r
		}
	}
	if len(run.Artifacts) != 1 || !run.Artifacts[0].Available {
		t.Fatal("explicit run link missing")
	}
	put(t, root, "deliverables/revision-1/report.html", []byte("changed"))
	cat = discover(root, Catalogue{})
	if _, ok := cat.Allowed["deliverables/revision-1/report.html"]; ok {
		t.Fatal("corrupt report still admitted")
	}
	if len(cat.Issues) == 0 {
		t.Fatal("missing corruption notice")
	}
}

func TestPathsAndSymlinksCannotEscape(t *testing.T) {
	root, _ := fixture(t)
	outside := t.TempDir()
	put(t, outside, "secret.txt", []byte("secret"))
	if err := os.Symlink(filepath.Join(outside, "secret.txt"), filepath.Join(root, "runs/case-a/escape.txt")); err != nil {
		t.Skip(err)
	}
	access, err := os.OpenRoot(root)
	if err != nil {
		t.Fatal(err)
	}
	defer access.Close()
	for _, name := range []string{"../secret.txt", "/secret.txt", "runs/case-a/escape.txt", "C:/secret.txt", "runs/a:stream", "runs\\a.txt"} {
		if _, err := readFile(access, name); err == nil {
			t.Fatalf("allowed %q", name)
		}
	}
	cat := discover(root, Catalogue{})
	if _, ok := cat.Allowed["runs/case-a/escape.txt"]; ok {
		t.Fatal("symlink enumerated")
	}
}

func TestCurrentRetainedWorkspace(t *testing.T) {
	root := filepath.Clean("../..")
	if _, err := os.Stat(filepath.Join(root, "runs/tdg-002")); err != nil {
		t.Skip("retained workspace not present")
	}
	var seeds Catalogue
	raw, _ := resources.ReadFile("web/legacy-catalog.json")
	if err := json.Unmarshal(raw, &seeds); err != nil {
		t.Fatal(err)
	}
	cat := discover(root, seeds)
	if len(cat.Issues) != 0 {
		t.Fatalf("retained data rejected: %v", cat.Issues)
	}
	var annual *Run
	reports := map[string]bool{}
	runFolders := 0
	for i := range cat.Real {
		run := &cat.Real[i]
		if !strings.HasPrefix(run.ID, "delivery:") {
			runFolders++
		}
		if run.ID == "tdg-002" {
			annual = run
		}
		for _, a := range run.Artifacts {
			if a.Available {
				reports[a.Folder] = true
			}
		}
	}
	if annual == nil || annual.Metrics["leverage"].Value != "5.96" || annual.Metrics["coverage"].Value != "3.60" || annual.Completion != nil {
		t.Fatal("retained financial semantics changed")
	}
	// Counted from the folders here, not through discovery.
	entries, err := os.ReadDir(filepath.Join(root, "runs"))
	if err != nil {
		t.Fatal(err)
	}
	wantRuns := 0
	for _, entry := range entries {
		if entry.IsDir() {
			wantRuns++
		}
	}
	delivered, _ := filepath.Glob(filepath.Join(root, "deliverables", "*", "report.html"))
	models, _ := filepath.Glob(filepath.Join(root, "deliverables", "*", "model.html"))
	delivered = append(delivered, models...)
	launched, _ := filepath.Glob(filepath.Join(root, "runs", "*", "deliveries", "*", "report.html"))
	if runFolders != wantRuns || len(reports) != len(delivered)+len(launched) {
		t.Fatalf("got %d run folders, %d reports; folders hold %d runs, %d reports", runFolders, len(reports), wantRuns, len(delivered)+len(launched))
	}
}

func TestManifestCannotSupplyDerivedLinksOrNullCollections(t *testing.T) {
	root, m := fixture(t)
	m.Run.Handoff = ""
	m.Run.HandoffHref = "javascript:alert(1)"
	m.Run.Artifacts = nil
	putJSON(t, root, "runs/case-a/library.json", m)
	cat := discover(root, Catalogue{})
	if cat.Real[0].HandoffHref != "" {
		t.Fatal("untrusted derived handoff URL survived admission")
	}
	if cat.Real[0].Artifacts == nil {
		t.Fatal("nil artifacts break browser rendering")
	}
}
func TestWrongIssuerMappingDoesNotHideDiscoveredDelivery(t *testing.T) {
	root, m := fixture(t)
	m.Run.Artifacts = []Artifact{{Folder: "deliverables/foreign", Label: "Bad mapping"}}
	putJSON(t, root, "runs/case-a/library.json", m)
	addDelivery(t, root, "foreign", "foreign-run", "OTHER")
	cat := discover(root, Catalogue{})
	if len(cat.Real) != 2 {
		t.Fatal("wrong-issuer mapping hid a valid delivery from discovery")
	}
}

func TestDeliveryCheckpointRequiresAvailableDirectBundle(t *testing.T) {
	root, m := fixture(t)
	raw := `{"scope":"Annual review","requirements":[{"id":"s","stage":"sources","done":true,"evidence":["check"]},{"id":"a","stage":"analysis","done":true,"evidence":["check"]},{"id":"v","stage":"verification","done":true,"evidence":["check"]},{"id":"c","stage":"downstream","done":true,"evidence":["check"]},{"id":"d","stage":"delivery","done":true,"evidence":["check"]}]}`
	if err := json.Unmarshal([]byte(raw), &m.Checklist); err != nil {
		t.Fatal(err)
	}
	putJSON(t, root, "runs/case-a/library.json", m)
	cat := discover(root, Catalogue{})
	if cat.Real[0].Completion != nil {
		t.Fatal("checklist claimed delivery without any verified deliverable")
	}
	addDelivery(t, root, "complete", "case-a", "EX")
	cat = discover(root, Catalogue{})
	if cat.Real[0].Completion == nil || *cat.Real[0].Completion != 100 {
		t.Fatal("verified synthetic delivery did not restore scoped producer assessment")
	}
	put(t, root, "deliverables/complete/report.html", []byte("corrupted"))
	cat = discover(root, Catalogue{})
	for _, run := range cat.Real {
		if run.ID == "case-a" && run.Completion != nil {
			t.Fatal("changed delivery retained completeness")
		}
	}
}

func addModelDelivery(t *testing.T, root, folder string, withReport bool) []byte {
	t.Helper()
	var view deliveryView
	view.Run.RunID = "model-run"
	view.Run.IssuerID = "TDG"
	view.Run.IssuerName = "Example Industries"
	view.Run.AsOf = "2024-12-31"
	raw, _ := json.Marshal(view)
	model := []byte("<!doctype html><title>Model</title><p>Published model</p>")
	files := map[string]string{"view.json": digest(raw), "model.html": digest(model)}
	put(t, root, "deliverables/"+folder+"/view.json", raw)
	put(t, root, "deliverables/"+folder+"/model.html", model)
	if withReport {
		put(t, root, "deliverables/"+folder+"/report.html", []byte("report"))
		files["report.html"] = digest([]byte("report"))
	}
	putJSON(t, root, "deliverables/"+folder+"/delivery.json", map[string]any{"files": files})
	return model
}

func findArtifact(cat Catalogue, folder string) *Artifact {
	for i := range cat.Real {
		for j := range cat.Real[i].Artifacts {
			if cat.Real[i].Artifacts[j].Folder == folder {
				return &cat.Real[i].Artifacts[j]
			}
		}
	}
	return nil
}

func TestModelDeliveryVerifiesAsAModelAndAReportKeepsItsKind(t *testing.T) {
	root, _ := fixture(t)
	model := addModelDelivery(t, root, "m-1", false)
	addDelivery(t, root, "r-1", "case-a", "other")
	cat := discover(root, Catalogue{})
	if len(cat.Issues) != 0 {
		t.Fatalf("issues: %v", cat.Issues)
	}
	artifact := findArtifact(cat, "deliverables/m-1")
	if artifact == nil || !artifact.Available || artifact.Kind != "model" || artifact.Href != pinnedURL("deliverables/m-1/model.html", digest(model)) {
		t.Fatalf("model delivery: %+v", artifact)
	}
	if report := findArtifact(cat, "deliverables/r-1"); report == nil || report.Kind != "report" || !strings.HasSuffix(strings.Split(report.Href, "?")[0], "/report.html") {
		t.Fatalf("report delivery: %+v", report)
	}
	if cat.Allowed["deliverables/m-1/model.html"] != digest(model) {
		t.Fatal("model file not admitted under its hash")
	}
}

func TestDeliveryWithNeitherPageKeepsItsIssue(t *testing.T) {
	root, _ := fixture(t)
	putJSON(t, root, "deliverables/empty/delivery.json", map[string]any{"files": map[string]string{"view.json": "x"}})
	cat := discover(root, Catalogue{})
	if !slices.Contains(cat.Issues, "deliverables/empty: Delivery manifest requires report.html and view.json") {
		t.Fatalf("issues: %v", cat.Issues)
	}
}

func TestChangedModelMakesItsDeliveryUnavailable(t *testing.T) {
	root, _ := fixture(t)
	addModelDelivery(t, root, "m-1", false)
	put(t, root, "deliverables/m-1/model.html", []byte("changed"))
	cat := discover(root, Catalogue{})
	if artifact := findArtifact(cat, "deliverables/m-1"); artifact != nil && artifact.Available {
		t.Fatalf("changed model stayed available: %+v", artifact)
	}
	if !slices.Contains(cat.Issues, "deliverables/m-1: Missing or changed delivery file: model.html") {
		t.Fatalf("issues: %v", cat.Issues)
	}
}

// moveDelivery places a verified delivery folder inside a run, as the launcher or a copy would.
func moveDelivery(t *testing.T, root, folder, run string) string {
	t.Helper()
	target := filepath.Join(root, "runs", run, "deliveries")
	if err := os.MkdirAll(target, 0700); err != nil {
		t.Fatal(err)
	}
	if err := os.Rename(filepath.Join(root, "deliverables", folder), filepath.Join(target, folder)); err != nil {
		t.Fatal(err)
	}
	return "runs/" + run + "/deliveries/" + folder
}

func attached(cat Catalogue, runID, folder string) (Artifact, bool) {
	for _, run := range cat.Real {
		if run.ID == runID {
			for _, artifact := range run.Artifacts {
				if artifact.Folder == folder && artifact.Available {
					return artifact, true
				}
			}
		}
	}
	return Artifact{}, false
}

// A delivery under runs/<id>/deliveries is that run's only when its view.json says so.
func TestRunInternalDeliveryMustMatchItsRunAndIssuer(t *testing.T) {
	root, _ := fixture(t)
	addDelivery(t, root, "own", "case-a", "EX")
	addDelivery(t, root, "foreign-run", "other-run", "EX")
	addDelivery(t, root, "foreign-issuer", "case-a", "ZZZ")
	addDelivery(t, root, "foreign-both", "other-run", "ZZZ")
	own := moveDelivery(t, root, "own", "case-a")
	rejected := []string{moveDelivery(t, root, "foreign-run", "case-a"), moveDelivery(t, root, "foreign-issuer", "case-a"), moveDelivery(t, root, "foreign-both", "case-a")}
	cat := discover(root, Catalogue{})
	if _, ok := attached(cat, "case-a", own); !ok {
		t.Fatalf("the run's own delivery was refused: %+v", cat.Issues)
	}
	for _, folder := range rejected {
		if _, ok := attached(cat, "case-a", folder); ok {
			t.Errorf("%s was attached to case-a", folder)
		}
		if hash := cat.Allowed[folder+"/report.html"]; hash != "" {
			t.Errorf("%s is pinned as a verified report although it was refused", folder)
		}
		found := false
		for _, issue := range cat.Issues {
			found = found || strings.HasPrefix(issue, folder+": Delivery ")
		}
		if !found {
			t.Errorf("%s refusal not recorded: %v", folder, cat.Issues)
		}
	}
}

// The launcher's deliveries carry the run id recorded in workflow.json, not the web-<hex> folder.
func TestRunInternalDeliveryAcceptsTheLauncherRecordedIdentityOnly(t *testing.T) {
	root, _ := fixture(t)
	put(t, root, "runs/web-1/CP-0.md", []byte("x"))
	put(t, root, "runs/web-1/workflow.json", []byte(`{"run":{"run_id":"ex-2024-12-31-full-a","issuer_id":"EX"}}`))
	addDelivery(t, root, "mine", "ex-2024-12-31-full-a", "EX")
	addDelivery(t, root, "wrong-issuer", "ex-2024-12-31-full-a", "ZZZ")
	addDelivery(t, root, "other-launch", "zzz-2024-12-31-full-a", "EX")
	mine := moveDelivery(t, root, "mine", "web-1")
	wrongIssuer := moveDelivery(t, root, "wrong-issuer", "web-1")
	otherLaunch := moveDelivery(t, root, "other-launch", "web-1")
	cat := discover(root, Catalogue{})
	if _, ok := attached(cat, "web-1", mine); !ok {
		t.Fatalf("launcher delivery refused: %v", cat.Issues)
	}
	for _, folder := range []string{wrongIssuer, otherLaunch} {
		if _, ok := attached(cat, "web-1", folder); ok {
			t.Errorf("%s was attached", folder)
		}
	}
}

// A copied delivery must not satisfy the manifest's delivery checkpoint.
func TestForeignRunDeliveryDoesNotSatisfyTheDeliveryCheckpoint(t *testing.T) {
	root, m := fixture(t)
	raw := `{"scope":"Annual review","requirements":[{"id":"s","stage":"sources","done":true,"evidence":["check"]},{"id":"a","stage":"analysis","done":true,"evidence":["check"]},{"id":"v","stage":"verification","done":true,"evidence":["check"]},{"id":"c","stage":"downstream","done":true,"evidence":["check"]},{"id":"d","stage":"delivery","done":true,"evidence":["check"]}]}`
	if err := json.Unmarshal([]byte(raw), &m.Checklist); err != nil {
		t.Fatal(err)
	}
	putJSON(t, root, "runs/case-a/library.json", m)
	addDelivery(t, root, "foreign", "other-run", "ZZZ")
	moveDelivery(t, root, "foreign", "case-a")
	for _, run := range discover(root, Catalogue{}).Real {
		if run.ID == "case-a" && run.Completion != nil {
			t.Fatalf("a foreign delivery restored completeness: %+v", run.Completion)
		}
	}
	addDelivery(t, root, "mine", "case-a", "EX")
	moveDelivery(t, root, "mine", "case-a")
	for _, run := range discover(root, Catalogue{}).Real {
		if run.ID == "case-a" && (run.Completion == nil || *run.Completion != 100) {
			t.Fatal("the run's own delivery must still satisfy the checkpoint")
		}
	}
}

// Review (S18 medium, A06/C04): adversarial identities for deliveries kept inside a run.
func TestReviewRunDeliveryIdentityAdversarial(t *testing.T) {
	root, _ := fixture(t)
	// web-2 has no manifest (issuer Unclassified) and a workflow.json whose issuer_id has the
	// wrong type. Expected: the file counts as unreadable, so only the folder id is accepted;
	// the recorded run id must not be honoured without its issuer (before review: attached).
	put(t, root, "runs/web-2/CP-0.md", []byte("x"))
	put(t, root, "runs/web-2/workflow.json", []byte(`{"run":{"run_id":"ex-run","issuer_id":7}}`))
	addDelivery(t, root, "typed", "ex-run", "ZZZ")
	addDelivery(t, root, "folder-id", "web-2", "EX")
	typed := moveDelivery(t, root, "typed", "web-2")
	folderID := moveDelivery(t, root, "folder-id", "web-2")
	// web-3: no workflow.json at all. Expected: only view run_id == "web-3" is accepted.
	put(t, root, "runs/web-3/CP-0.md", []byte("x"))
	addDelivery(t, root, "none-own", "web-3", "EX")
	addDelivery(t, root, "none-other", "ex-run", "EX")
	noneOwn := moveDelivery(t, root, "none-own", "web-3")
	noneOther := moveDelivery(t, root, "none-other", "web-3")
	// web-4: a CP-8 comparison plan recorded as workflow.json (ComparisonPlan also has "run").
	// Expected: its comparison delivery is accepted; an issuer differing only in case is not.
	put(t, root, "runs/web-4/CP-0.md", []byte("x"))
	put(t, root, "runs/web-4/workflow.json", []byte(`{"run":{"run_id":"tdg-cp8-comparison","issuer_id":"TDG"},"prior":{"path":"p","sha256":"x"}}`))
	addDelivery(t, root, "cp8", "tdg-cp8-comparison", "TDG")
	addDelivery(t, root, "cp8-case", "tdg-cp8-comparison", "tdg")
	cp8 := moveDelivery(t, root, "cp8", "web-4")
	cp8Case := moveDelivery(t, root, "cp8-case", "web-4")
	// case-a has an admitted manifest (issuer EX). A delivery naming case-a as its run but
	// another issuer, and one naming the other run web-3 with issuer EX. Expected: both refused.
	addDelivery(t, root, "case-other-issuer", "case-a", "ex")
	addDelivery(t, root, "case-other-run", "web-3", "EX")
	caseIssuer := moveDelivery(t, root, "case-other-issuer", "case-a")
	caseRun := moveDelivery(t, root, "case-other-run", "case-a")

	cat := discover(root, Catalogue{})
	for _, want := range []struct {
		run, folder string
		ok          bool
	}{
		{"web-2", typed, false}, {"web-2", folderID, true},
		{"web-3", noneOwn, true}, {"web-3", noneOther, false},
		{"web-4", cp8, true}, {"web-4", cp8Case, false},
		{"case-a", caseIssuer, false}, {"case-a", caseRun, false},
	} {
		if _, ok := attached(cat, want.run, want.folder); ok != want.ok {
			t.Errorf("%s attached=%v, want %v (issues %v)", want.folder, ok, want.ok, cat.Issues)
		}
		if pinned := cat.Allowed[want.folder+"/report.html"] != ""; pinned != want.ok {
			t.Errorf("%s pinned=%v, want %v", want.folder, pinned, want.ok)
		}
	}
	// A refused run delivery never appears as an available artifact under any run.
	for _, run := range cat.Real {
		for _, artifact := range run.Artifacts {
			if artifact.Available && (artifact.Folder == typed || artifact.Folder == caseIssuer || artifact.Folder == caseRun) {
				t.Errorf("%s available under %s", artifact.Folder, run.ID)
			}
		}
	}
}

// admitsMetric reports whether discovery admits value as the revenue metric quoted by quote.
func admitsMetric(t *testing.T, quote, value string) bool {
	t.Helper()
	root, manifest := fixture(t)
	manifest.Run.Metrics["revenue"].Value = value
	raw := []byte("Issuer: Example Industries\nSector: Industrials\n" + quote + "\nVerified scope\n")
	put(t, root, "runs/case-a/CP-0.md", raw)
	for key, source := range manifest.Sources {
		source.SHA256 = digest(raw)
		if key == "revenue" {
			source.Quote = quote
		}
		manifest.Sources[key] = source
	}
	putJSON(t, root, "runs/case-a/library.json", manifest)
	for _, run := range discover(root, Catalogue{}).Real {
		if run.ID == "case-a" {
			return run.Metrics["revenue"] != nil
		}
	}
	return false
}

// A03: a metric must equal a whole number the quote states, sign and scale included; a
// fragment of a date, range, list or other-convention figure is not evidence of it.
func TestMetricMustBeAWholeNumberOfTheQuoteWithItsSignAndScale(t *testing.T) {
	for _, c := range []struct {
		quote, value string
		admitted     bool
	}{
		// The reported fragments (all admitted before the fix).
		{"Net loss: (12.3)", "12.3", false},
		{"As of 2024-12-31 net debt was 450", "-12", false},
		{"Guidance: margin 3-5%", "-5", false},
		{"Yield: .5%", "5", false},
		{"Covenant tests 1,2,3 passed", "123", false},
		{"Revenue 1.234,5 (EUR format)", "1.234", false},
		// Whole numbers keep their sign, thousands grouping and decimals.
		{"Net loss: (12.3)", "-12.3", true},
		{"Net sales | 7,940 | 6,585", "7940", true},
		{"Closing cash | -1,676 | x", "-1676", true},
		{"Leverage 5.96x", "5.96", true},
		{"As Defined 4,685.", "4685", true},
		{"Revenue USD 1,234.5m, up 4%", "1234.5", true},
		{"Revenue 450, 500 and 600.", "500", true},
		{"As of 2024-12-31 net debt was 450", "450", true},
		// Dates, ranges and lists state none of their parts.
		{"As of 2024-12-31 net debt was 450", "2024", false},
		{"As of 2024-12-31 net debt was 450", "12", false},
		{"Guidance: margin 3-5%", "3", false},
		{"Guidance: margin 3–5%", "5", false},
		{"Covenant tests 1,2,3 passed", "1", false},
		{"COVID-19 costs", "-19", false},
		{"COVID-19 costs", "19", false},
		// A typographic minus or a sign inside parentheses is not dropped.
		{"Net loss −12.3", "12.3", false},
		{"Net loss: (-12.3)", "-12.3", false},
		{"Net loss: (-12.3)", "12.3", false},
		{"Net loss (USD 12.3m)", "12.3", false},
		{"Net loss (USD 12.3m)", "-12.3", false},
		{"Net loss (12.3m)", "12.3", false},
		{"Net change -(12.3)", "-12.3", false},
		{"Net change -(12.3)", "12.3", false},
		{"Net loss (12.3).", "-12.3", true},
		{"| Net loss | (1,676) |", "-1676", true},
		{"Net loss (12.3)5", "-12.3", false},
		{"Net loss –(12.3)", "-12.3", false},
		// Other separator conventions and malformed groups are refused, never truncated.
		{"Revenue 1.234,5", "1234.5", false},
		{"Revenue 1.234.567", "1.234", false},
		{"Revenue 1,2345", "1", false},
		{"Revenue 12,34", "12", false},
		{"Revenue 1 234,5", "1", false},
		{"Revenue 1 234 567", "234", false},
		{"Revenue 1 234 567", "1", false},
		{"Umsatz 1 234,5", "1", false},
		{"Revenue 1'234.5", "234.5", false},
		{"Yield: .5%", ".5", false},
		// Exponents and a parenthesis opened before the quote also hide scale or sign.
		{"Notional 1.2e3", "1.2", false},
		{"Notional 1.2E+3", "3", false},
		{"Notional 1.2e-3", "-3", false},
		{"USD 12.3)", "12.3", false},
		{"Revenue 450 (2023: 400)", "450", true},
		{"Revenue 450 (2023: 400)", "400", false},
	} {
		if got := admitsMetric(t, c.quote, c.value); got != c.admitted {
			t.Errorf("quote %q value %q: admitted=%v, want %v", c.quote, c.value, got, c.admitted)
		}
	}
}

// C09: a run manifest that declares its own runs/<id>/deliveries/<v> folder gets that delivery
// once: the verified entry replaces the declared one, keeping its label, relationship and a
// superseded state; a refused delivery stays one unavailable entry with the refusal.
func TestDeclaredRunDeliveryIsListedOnce(t *testing.T) {
	root, manifest := fixture(t)
	own, superseded, foreign := "runs/case-a/deliveries/v1", "runs/case-a/deliveries/v0", "runs/case-a/deliveries/vx"
	manifest.Run.Artifacts = []Artifact{
		{Folder: own, Label: "Annual report", State: "candidate", Relationship: "related"},
		{Folder: superseded, Label: "Earlier", State: "superseded", Relationship: "direct"},
		{Folder: foreign, Label: "Copied", State: "candidate", Relationship: "direct"},
	}
	putJSON(t, root, "runs/case-a/library.json", manifest)
	addDelivery(t, root, "v1", "case-a", "EX")
	addDelivery(t, root, "v0", "case-a", "EX")
	addDelivery(t, root, "vx", "other-run", "EX")
	for _, folder := range []string{"v1", "v0", "vx"} {
		moveDelivery(t, root, folder, "case-a")
	}
	cat := discover(root, Catalogue{})
	listed := map[string][]Artifact{}
	for _, run := range cat.Real {
		for _, artifact := range run.Artifacts {
			listed[artifact.Folder] = append(listed[artifact.Folder], artifact)
		}
	}
	for folder, want := range map[string]Artifact{
		own:        {Label: "Annual report", State: "candidate", Relationship: "related", Available: true},
		superseded: {Label: "Earlier", State: "superseded", Relationship: "direct", Available: true},
		foreign:    {Label: "Copied", State: "candidate", Relationship: "direct", Issue: "Delivery run identity does not match this run"},
	} {
		got := listed[folder]
		if len(got) != 1 {
			t.Errorf("%s listed %d times: %+v", folder, len(got), got)
			continue
		}
		a := got[0]
		if a.Label != want.Label || a.State != want.State || a.Relationship != want.Relationship || a.Available != want.Available || a.Issue != want.Issue || (a.Href != "") != want.Available {
			t.Errorf("%s: %+v, want %+v", folder, a, want)
		}
	}
	if cat.Allowed[own+"/report.html"] == "" || cat.Allowed[foreign+"/report.html"] != "" {
		t.Errorf("pins: own=%q foreign=%q", cat.Allowed[own+"/report.html"], cat.Allowed[foreign+"/report.html"])
	}
}

// A03 review: hand-derived readings of accounting, grouping, percentage, year and currency forms,
// and that every curated legacy metric is still stated by its own quote.
func TestStatedNumbersAdversarial(t *testing.T) {
	for _, c := range []struct {
		quote string
		want  []string
	}{
		{"Revenue $1,234.50 million", []string{"1234.50"}},
		{"Loss of $(1,234)", []string{"-1234"}},
		{"(1,234) and (567)", []string{"-1234", "-567"}},
		{"up 12.5% from 11.9%", []string{"12.5", "11.9"}},
		{"FY2023 revenue of 5,000 vs 4,500 in FY2022", []string{"2023", "5000", "4500", "2022"}},
		{"EUR 1.234,56", nil},
		{"CHF 1'234.50", nil},
		{"INR 1,23,456", nil},
		{"EUR -45.2m", []string{"-45.2"}},
		{"Loss -$5", nil},
		{"Loss −$5", nil},
		{"Loss $-5", []string{"-5"}},
		{"Loss -€1,200.", nil},
		{"Gain $5", []string{"5"}},
		{"1,000.5.", []string{"1000.5"}},
		{"10,000,000", []string{"10000000"}},
		{"1,000,00", nil},
		{"1,0000", nil},
		{"(12.5%)", nil},
		{"rose 3.5 points (from 2.1)", []string{"3.5"}},
		{"5 - 3", []string{"5", "3"}},
		{"Q2 2024 EBITDA 1,200", []string{"2", "2024", "1200"}},
		{"2023/24 sales 9", []string{"9"}},
		{"As of 12/31/2024 cash 450", []string{"450"}},
	} {
		if got := statedNumbers(c.quote); !slices.Equal(got, c.want) {
			t.Errorf("%q: %v want %v", c.quote, got, c.want)
		}
	}
}

func TestSeedMetricsAllStated(t *testing.T) {
	var seeds Catalogue
	raw, _ := resources.ReadFile("web/legacy-catalog.json")
	if err := json.Unmarshal(raw, &seeds); err != nil {
		t.Fatal(err)
	}
	n := 0
	for _, run := range seeds.Real {
		for k, m := range run.Metrics {
			if m == nil {
				continue
			}
			q := seeds.Sources[m.Source].Quote
			n++
			if !slices.Contains(statedNumbers(q), m.Value) {
				t.Errorf("%s/%s value %q quote %q", run.ID, k, m.Value, q)
			}
		}
	}
	t.Log(n)
}

func TestAPublishedModelAloneDoesNotRestoreARunsCompleteness(t *testing.T) {
	root, m := fixture(t)
	raw := `{"scope":"Annual review","requirements":[{"id":"s","stage":"sources","done":true,"evidence":["check"]},{"id":"a","stage":"analysis","done":true,"evidence":["check"]},{"id":"v","stage":"verification","done":true,"evidence":["check"]},{"id":"c","stage":"downstream","done":true,"evidence":["check"]},{"id":"d","stage":"delivery","done":true,"evidence":["check"]}]}`
	if err := json.Unmarshal([]byte(raw), &m.Checklist); err != nil {
		t.Fatal(err)
	}
	putJSON(t, root, "runs/case-a/library.json", m)
	var view deliveryView
	view.Run.RunID, view.Run.IssuerID, view.Run.IssuerName, view.Run.AsOf = "case-a", "EX", "Example Industries", "2024-12-31"
	rawView, _ := json.Marshal(view)
	model := []byte("<!doctype html><title>Model</title><p>Published model</p>")
	put(t, root, "deliverables/m-only/view.json", rawView)
	put(t, root, "deliverables/m-only/model.html", model)
	putJSON(t, root, "deliverables/m-only/delivery.json", map[string]any{"files": map[string]string{"view.json": digest(rawView), "model.html": digest(model)}})
	cat := discover(root, Catalogue{})
	found := false
	for _, run := range cat.Real {
		if run.ID != "case-a" {
			continue
		}
		found = true
		if run.Completion != nil {
			t.Fatalf("completeness %d%% restored by a model-only delivery; no report exists", *run.Completion)
		}
	}
	if !found {
		t.Fatal("run case-a not discovered")
	}
}

// Task 12: admission of classification, private side, facilities and user provenance, checked
// against the hand-written answer key in tests/fixtures/library-manifest (not edited here).
const manifestFixtures = "../../tests/fixtures/library-manifest"

func readFixtureJSON(t *testing.T, name string) any {
	t.Helper()
	raw, err := os.ReadFile(filepath.Join(manifestFixtures, filepath.FromSlash(name)))
	if err != nil {
		t.Fatal(err)
	}
	var value any
	if err := json.Unmarshal(raw, &value); err != nil {
		t.Fatal(err)
	}
	return value
}

func copyFile(t *testing.T, from, root, name string) []byte {
	t.Helper()
	raw, err := os.ReadFile(from)
	if err != nil {
		t.Fatal(err)
	}
	put(t, root, name, raw)
	return raw
}

const retainedRun = "runs/web-04cd5a5d02ea7d1dea714a8a6632cd21"

// fixtureWorkspace builds a temp workspace for the named fixture and returns it with the run id.
func fixtureWorkspace(t *testing.T, name string) (root, id string) {
	t.Helper()
	root = t.TempDir()
	switch name {
	case "synthetic":
		base := filepath.Join(manifestFixtures, "synthetic/workspace")
		err := filepath.WalkDir(base, func(p string, d os.DirEntry, err error) error {
			if err != nil || d.IsDir() {
				return err
			}
			rel, _ := filepath.Rel(base, p)
			copyFile(t, p, root, filepath.ToSlash(rel))
			return nil
		})
		if err != nil {
			t.Fatal(err)
		}
		return root, "synthetic-hy-001"
	case "retained-cp1":
		repo := filepath.Join("..", "..", filepath.FromSlash(retainedRun))
		if _, err := os.Stat(filepath.Join(repo, "CP-1.md")); err != nil {
			t.Skip("retained CP-1.md not present")
		}
		raw := copyFile(t, filepath.Join(repo, "CP-1.md"), root, retainedRun+"/CP-1.md")
		sum := sha256.Sum256(raw)
		if got := hex.EncodeToString(sum[:]); got != "7f0578c02be6bce6849863c7105d17f6d09674ed595b86626286e57d61268e3a" {
			t.Fatalf("retained CP-1.md changed: %s", got)
		}
		input := "inputs/ec0a711fe74781d81973060c2e34ae47b1129e9ff5aea9f5ef6218a082b4f984"
		copyFile(t, filepath.Join(repo, filepath.FromSlash(input)), root, retainedRun+"/"+input)
		return root, "web-04cd5a5d02ea7d1dea714a8a6632cd21"
	}
	t.Fatalf("unknown fixture %s", name)
	return "", ""
}

// setPointer sets an RFC 6901 location, replacing the member or adding it when the parent object
// lacks it. Array elements are replaced in place; only what the case files use is supported.
func setPointer(t *testing.T, doc any, pointer string, value any) any {
	t.Helper()
	parts := strings.Split(strings.TrimPrefix(pointer, "/"), "/")
	for i := range parts {
		parts[i] = strings.ReplaceAll(strings.ReplaceAll(parts[i], "~1", "/"), "~0", "~")
	}
	node := doc
	for _, part := range parts[:len(parts)-1] {
		switch n := node.(type) {
		case map[string]any:
			node = n[part]
		case []any:
			var index int
			if _, err := fmt.Sscanf(part, "%d", &index); err != nil || index >= len(n) {
				t.Fatalf("bad array index %q in %s", part, pointer)
			}
			node = n[index]
		default:
			t.Fatalf("pointer %s leaves the document at %q", pointer, part)
		}
	}
	last := parts[len(parts)-1]
	switch n := node.(type) {
	case map[string]any:
		n[last] = value
	case []any:
		var index int
		if _, err := fmt.Sscanf(last, "%d", &index); err != nil || index >= len(n) {
			t.Fatalf("bad array index %q in %s", last, pointer)
		}
		n[index] = value
	default:
		t.Fatalf("pointer %s has no container", pointer)
	}
	return doc
}

func discoverFixture(t *testing.T, name string, change func(doc any) any) (Catalogue, Run) {
	t.Helper()
	root, id := fixtureWorkspace(t, name)
	doc := readFixtureJSON(t, name+"/library.json")
	if change != nil {
		doc = change(doc)
	}
	putJSON(t, root, "runs/"+id+"/library.json", doc)
	cat := discover(root, Catalogue{})
	for _, run := range cat.Real {
		if run.ID == id {
			return cat, run
		}
	}
	t.Fatalf("run %s not served", id)
	return cat, Run{}
}

// subsetDiff returns the first place served differs from want: every key and element the answer
// key holds must be present and equal; arrays must have the same length.
func subsetDiff(want, got any, where string) string {
	switch w := want.(type) {
	case map[string]any:
		g, ok := got.(map[string]any)
		if !ok {
			return where + ": not an object"
		}
		for key, value := range w {
			have, present := g[key]
			if !present {
				return where + "/" + key + ": missing"
			}
			if diff := subsetDiff(value, have, where+"/"+key); diff != "" {
				return diff
			}
		}
	case []any:
		g, ok := got.([]any)
		if !ok || len(g) != len(w) {
			return fmt.Sprintf("%s: array length differs (%v)", where, got)
		}
		for i := range w {
			if diff := subsetDiff(w[i], g[i], fmt.Sprintf("%s/%d", where, i)); diff != "" {
				return diff
			}
		}
	default:
		if want != got {
			return fmt.Sprintf("%s: want %v got %v", where, want, got)
		}
	}
	return ""
}

func servedJSON(t *testing.T, run Run) map[string]any {
	t.Helper()
	raw, err := json.Marshal(run)
	if err != nil {
		t.Fatal(err)
	}
	var served map[string]any
	if err := json.Unmarshal(raw, &served); err != nil {
		t.Fatal(err)
	}
	return served
}

func TestManifestAdmitsAnswerKey(t *testing.T) {
	for _, name := range []string{"synthetic", "retained-cp1"} {
		t.Run(name, func(t *testing.T) {
			cat, run := discoverFixture(t, name, nil)
			if len(cat.Issues) != 0 {
				t.Fatalf("answer-key manifest rejected: %v", cat.Issues)
			}
			served := servedJSON(t, run)
			want := readFixtureJSON(t, name+"/expected-served.json").(map[string]any)
			if diff := subsetDiff(want, served, ""); diff != "" {
				t.Fatal(diff)
			}
			// A key the answer key does not hold must be absent or empty when served.
			for _, key := range []string{"classification", "classification_source", "private_side", "private_side_source", "facilities"} {
				if _, held := want[key]; held {
					continue
				}
				v := served[key]
				if list, isList := v.([]any); (isList && len(list) != 0) || (!isList && v != nil && v != false && v != "") {
					t.Fatalf("%s served but not in the answer key: %v", key, v)
				}
			}
			facilities, ok := served["facilities"].([]any)
			wantFacilities, wantOK := want["facilities"].([]any)
			if !ok || !wantOK || (len(wantFacilities) == 0 && len(facilities) != 0) {
				t.Fatalf("facilities must be served as an array: %v (answer key %v)", served["facilities"], want["facilities"])
			}
		})
	}
}

func caseChange(t *testing.T, c map[string]any) func(any) any {
	return func(doc any) any { return setPointer(t, doc, c["pointer"].(string), c["value"]) }
}

func TestManifestRejectCases(t *testing.T) {
	for _, item := range readFixtureJSON(t, "reject-cases.json").([]any) {
		c := item.(map[string]any)
		t.Run(c["name"].(string), func(t *testing.T) {
			cat, run := discoverFixture(t, c["fixture"].(string), caseChange(t, c))
			t.Logf("rejected: %v", run.Gaps)
			if len(run.Gaps) == 0 || !strings.HasPrefix(run.Gaps[len(run.Gaps)-1], "Run metadata rejected:") || len(cat.Issues) == 0 {
				t.Fatalf("not rejected (%s): gaps %v issues %v", c["why"], run.Gaps, cat.Issues)
			}
			if run.Classification != "" || run.ClassificationSource != "" || run.PrivateSide || run.PrivateSideSource != "" || run.Facilities == nil || len(run.Facilities) != 0 || len(run.Metrics) != 0 {
				t.Fatalf("rejected run still serves new fields: %+v", run)
			}
			for key := range cat.Sources {
				if strings.HasPrefix(key, run.ID+".") {
					t.Fatalf("rejected manifest published source %s", key)
				}
			}
		})
	}
}

func TestManifestAcceptCases(t *testing.T) {
	for _, item := range readFixtureJSON(t, "accept-cases.json").([]any) {
		c := item.(map[string]any)
		t.Run(c["name"].(string), func(t *testing.T) {
			cat, run := discoverFixture(t, c["fixture"].(string), caseChange(t, c))
			if len(cat.Issues) != 0 {
				t.Fatalf("rejected (%s): %v", c["why"], cat.Issues)
			}
			if len(run.Metrics) == 0 || run.Facilities == nil {
				t.Fatalf("admitted run lost metrics or served null facilities: %+v", run)
			}
		})
	}
}

// A facility written without quotes or terms is still served with [] and {}, never null.
func TestManifestOmittedFacilityCollectionsServedEmpty(t *testing.T) {
	_, run := discoverFixture(t, "synthetic", func(doc any) any {
		facilities := doc.(map[string]any)["run"].(map[string]any)["facilities"].([]any)
		delete(facilities[0].(map[string]any), "quotes")
		delete(facilities[1].(map[string]any), "terms")
		return doc
	})
	if len(run.Facilities) != 2 {
		t.Fatalf("facilities not admitted: %+v", run.Gaps)
	}
	raw, err := json.Marshal(run.Facilities)
	if err != nil {
		t.Fatal(err)
	}
	if strings.Contains(string(raw), "null") {
		t.Fatalf("facility served with null collection: %s", raw)
	}
}

// Two bad terms must always be reported by the same key (the sorted-first one).
func TestManifestTermErrorNamesSortedFirstKey(t *testing.T) {
	for i := 0; i < 20; i++ {
		_, run := discoverFixture(t, "synthetic", func(doc any) any {
			terms := doc.(map[string]any)["run"].(map[string]any)["facilities"].([]any)[0].(map[string]any)["terms"].(map[string]any)
			for _, key := range []string{"zz_bad", "aa_bad", "mm_bad"} {
				terms[key] = terms["size_m"]
			}
			return doc
		})
		if len(run.Gaps) == 0 || !strings.Contains(run.Gaps[len(run.Gaps)-1], `"aa_bad"`) {
			t.Fatalf("run %d: error does not name the sorted-first bad key: %v", i, run.Gaps)
		}
	}
}
