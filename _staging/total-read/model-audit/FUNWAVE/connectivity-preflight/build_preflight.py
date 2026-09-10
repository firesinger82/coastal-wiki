#!/usr/bin/env python3
"""Build a read-only FUNWAVE raw-tree inventory and prior-evidence ledger."""

from __future__ import annotations

import csv
import hashlib
import json
import mimetypes
import os
import shutil
import subprocess
from collections import Counter, defaultdict
from pathlib import Path


REPO = Path(__file__).resolve().parents[5]
RAW = REPO / "models/FUNWAVE/raw"
TR = REPO / "_staging/total-read"
OUT = Path(__file__).resolve().parent
CODE_EXTS = {".f", ".f90", ".for", ".ftn", ".ftn90", ".c", ".cc", ".cpp", ".h", ".hpp", ".cu", ".cuh", ".m", ".js", ".wgsl", ".py"}
SCRIPT_EXTS = {".m", ".py", ".sh", ".pl", ".r", ".ipynb"}
DOC_EXTS = {".pdf", ".md", ".html", ".htm", ".rst", ".tex", ".doc", ".docx", ".odt", ".txt"}
MEDIA_EXTS = {".jpg", ".jpeg", ".png", ".gif", ".eps", ".tif", ".tiff", ".avi", ".mp4"}
ARCHIVE_EXTS = {".zip", ".gz", ".tgz", ".bz2", ".xz", ".7z", ".rar", ".tar"}
BUILD_EXTS = {".o", ".obj", ".mod", ".a", ".so", ".dll", ".exe"}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def norm(raw_path: str | None) -> str | None:
    if not raw_path:
        return None
    p = raw_path.replace("\\", "/")
    for prefix in ("models/FUNWAVE/", "FUNWAVE/"):
        if p.startswith(prefix):
            return "models/FUNWAVE/" + p[len(prefix):]
    marker = "/models/FUNWAVE/"
    if marker in p:
        return "models/FUNWAVE/" + p.split(marker, 1)[1]
    return p


def json_records(path: Path):
    try:
        if path.suffix == ".jsonl":
            with path.open(errors="replace") as f:
                for line in f:
                    try:
                        yield json.loads(line)
                    except json.JSONDecodeError:
                        continue
        else:
            yield json.loads(path.read_text(errors="replace"))
    except (OSError, json.JSONDecodeError):
        return


def add_evidence(index, obj, label, evidence_file):
    if not isinstance(obj, dict):
        return
    p = norm(obj.get("path") or obj.get("source_path") or obj.get("normalized_path"))
    s = obj.get("source_sha256") or obj.get("sha256") or obj.get("canonical_source_sha256")
    if p and s:
        index[(p, s)][label].add(str(evidence_file.relative_to(REPO)))


def material_class(rel: str, ext: str, mime: str) -> str:
    low = rel.lower()
    name = Path(rel).name.lower()
    if "/.git/" in low:
        return "vcs-metadata"
    if ext in ARCHIVE_EXTS or name.endswith(".tar.gz"):
        return "archive"
    if ext in BUILD_EXTS or name.startswith("funwave_") and "executable" in mime:
        return "generated-build"
    if ext in CODE_EXTS:
        if ext in SCRIPT_EXTS or "/postprocess" in low or "/tools/" in low or "/fft/" in low:
            return "script-source"
        if "/funwave-work/build/pre/" in low:
            return "generated-source-snapshot"
        return "solver-or-case-source"
    if ext == ".pdf":
        return "manual-or-paper-pdf"
    if ext in DOC_EXTS or name in {"readme", "license", "makefile"} or name.startswith("makefile"):
        return "documentation-or-build-text"
    if ext in MEDIA_EXTS:
        return "image-or-media"
    if ext in {".dat", ".out", ".sample", ".mat", ".qs"} or name.startswith(("input", "depth", "bathy", "eta_", "u_", "v_", "station", "gauge")):
        return "case-data-or-output"
    if mime.startswith("text/"):
        return "other-text"
    return "other-binary-or-data"


def load_evidence():
    ev = defaultdict(lambda: defaultdict(set))
    pending = TR / "pending/reread-20260728"
    for d in pending.glob("reread20260728-*-FUNWAVE-*"):
        run = d.name
        if "-code-" in run and "-fable5-" in run:
            label = "r1_code"
        elif "-code-" in run and "-codexaudit-" in run:
            label = "r2_code"
        elif "-doc-" in run:
            label = "document_read"
        elif "-note-" in run and "-fable5-" in run:
            label = "r1_note"
        elif "-note-" in run and "-codexaudit-" in run:
            label = "r2_note"
        else:
            continue
        for f in d.glob("*.json"):
            for obj in json_records(f):
                if obj.get("read_status") == "complete" and obj.get("comprehension_status", "complete") == "complete":
                    add_evidence(ev, obj, label, f)

    # Earlier single-reader records remain useful evidence but do not become R2.
    for f in (TR / "records").glob("all-FUNWAVE-*.jsonl"):
        for obj in json_records(f):
            if obj.get("read_status") == "complete":
                add_evidence(ev, obj, "legacy_complete_read", f)
            elif obj.get("read_status") == "partial":
                add_evidence(ev, obj, "legacy_partial_read", f)

    # Mechanical inspection is evidence of inventory/type/value sweep, not semantic reading.
    for pattern in ("numgrid-FUNWAVE-*.jsonl", "numbulk-FUNWAVE-*.jsonl", "binauto-*FUNWAVE.jsonl"):
        for f in (TR / "records").glob(pattern):
            for obj in json_records(f):
                add_evidence(ev, obj, "mechanical_inspection", f)

    cwroot = TR / "records-crosswalk/reread-20260728"
    for f in cwroot.glob("FUNWAVE-*/*.crosswalk.json"):
        for obj in json_records(f):
            add_evidence(ev, obj, "crosswalk", f)

    return ev


def main():
    files = sorted(p for p in RAW.rglob("*") if p.is_file())
    evidence = load_evidence()
    tracked = set()
    for snap in ("FUNWAVE-TVD", "FUNWAVE-GPU"):
        root = RAW / "source_code" / snap
        cp = subprocess.run(["git", f"--git-dir={root / '.git'}", f"--work-tree={root}", "ls-files", "-z"], capture_output=True)
        for item in cp.stdout.split(b"\0"):
            if item:
                tracked.add((root / os.fsdecode(item)).relative_to(REPO).as_posix())
    preflight = set()
    pf = TR / "preflight/chunk-manifest-FUNWAVE-20260728.jsonl"
    for obj in json_records(pf):
        k = (norm(obj.get("path")), obj.get("source_sha256"))
        preflight.add(k)

    # One file(1) process per batch avoids thousands of subprocesses.
    mime_by_path = {}
    for i in range(0, len(files), 150):
        batch = files[i:i + 150]
        cp = subprocess.run(["file", "--mime-type", "-b", "--", *map(str, batch)], capture_output=True, text=True, check=True)
        vals = cp.stdout.splitlines()
        mime_by_path.update(zip(batch, vals))

    rows = []
    by_sha = defaultdict(list)
    for p in files:
        rel = p.relative_to(REPO).as_posix()
        ext = p.suffix.lower()
        s = sha256(p)
        by_sha[s].append(rel)
        mime = mime_by_path.get(p) or mimetypes.guess_type(p.name)[0] or "application/octet-stream"
        key = (rel, s)
        e = evidence.get(key, {})
        if "/FUNWAVE-TVD/" in rel:
            snapshot = "FUNWAVE-TVD"
        elif "/FUNWAVE-GPU/" in rel:
            snapshot = "FUNWAVE-GPU"
        else:
            snapshot = "raw-manuals"
        semantic = bool(e.get("r1_code") or e.get("r2_code") or e.get("document_read") or e.get("legacy_complete_read"))
        two_read = bool(e.get("r1_code") and e.get("r2_code"))
        rows.append({
            "path": rel,
            "sha256": s,
            "bytes": p.stat().st_size,
            "mime": mime,
            "extension": ext or "[none]",
            "material_class": material_class(rel, ext, mime),
            "distribution_snapshot": snapshot,
            "git_tracked": rel in tracked,
            "vendor_status": "no explicit vendor marker found; retained in denominator",
            "legacy_277_code_member": ext in CODE_EXTS,
            "legacy_preflight_member": key in preflight,
            "r1_code_exact": bool(e.get("r1_code")),
            "r2_code_exact": bool(e.get("r2_code")),
            "two_independent_code_reads_exact": two_read,
            "crosswalk_exact": bool(e.get("crosswalk")),
            "document_read_exact": bool(e.get("document_read")),
            "legacy_complete_read_exact": bool(e.get("legacy_complete_read")),
            "legacy_partial_read_exact": bool(e.get("legacy_partial_read")),
            "mechanical_inspection_exact": bool(e.get("mechanical_inspection")),
            "semantic_complete_exact": semantic,
            "evidence_files": " | ".join(sorted({q for vals in e.values() for q in vals})),
        })

    for row in rows:
        members = by_sha[row["sha256"]]
        row["duplicate_count"] = len(members)
        row["duplicate_representative"] = members[0]
        row["duplicate_members"] = " | ".join(members) if len(members) > 1 else ""

    with (OUT / "exact-duplicate-groups.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["sha256", "path_count", "paths"])
        for s, members in sorted(by_sha.items()):
            if len(members) > 1:
                w.writerow([s, len(members), " | ".join(members)])

    by_path = {r["path"]: r for r in rows}
    aliases = []
    pre_prefix = "models/FUNWAVE/raw/source_code/FUNWAVE-TVD/funwave-work/build/pre/"
    src_prefix = "models/FUNWAVE/raw/source_code/FUNWAVE-TVD/src/"
    for r in rows:
        if r["path"].startswith(pre_prefix) and r["extension"] == ".f90":
            peer = src_prefix + Path(r["path"]).stem + ".F"
            if peer in by_path:
                aliases.append(["generated-preprocessed-counterpart", r["path"], peer, r["sha256"] == by_path[peer]["sha256"], "build/pre path plus same stem; hashes retained separately"])
    gpu_prefix = "models/FUNWAVE/raw/source_code/FUNWAVE-GPU/src/"
    for r in rows:
        if r["path"].startswith(gpu_prefix) and r["extension"] == ".f":
            peer = src_prefix + Path(r["path"]).name
            if peer in by_path:
                aliases.append(["separate-repository-counterpart", r["path"], peer, r["sha256"] == by_path[peer]["sha256"], "same source filename in GPU and TVD commits; not collapsed"])
    with (OUT / "snapshot-alias-ledger.csv").open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["relationship", "path", "counterpart", "byte_identical", "basis"])
        w.writerows(aliases)

    fields = list(rows[0])
    with (OUT / "raw-inventory-read-coverage.csv").open("w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader(); w.writerows(rows)

    unread = [r for r in rows if not r["semantic_complete_exact"]]
    two_unread = [r for r in rows if r["legacy_277_code_member"] and not r["two_independent_code_reads_exact"]]
    exact_code_unread = [r for r in rows if r["legacy_277_code_member"] and not r["semantic_complete_exact"]]
    script_unread = [r for r in rows if r["material_class"] == "script-source" and not r["semantic_complete_exact"]]
    doc_unread = [r for r in rows if r["material_class"] in {"documentation-or-build-text", "manual-or-paper-pdf"} and not r["semantic_complete_exact"]]
    script_two_unread = [r for r in two_unread if r["material_class"] == "script-source"]
    solver_two_unread = [r for r in two_unread if r["material_class"] != "script-source"]
    for name, data in (
        ("remaining-all-semantic-unread.txt", unread),
        ("remaining-legacy277-without-two-independent-reads.txt", two_unread),
        ("remaining-solver-source-without-two-independent-reads.txt", solver_two_unread),
        ("remaining-script-source-without-two-independent-reads.txt", script_two_unread),
        ("remaining-code-source-unread.txt", exact_code_unread),
        ("remaining-script-source-unread.txt", script_unread),
        ("remaining-document-manual-unread.txt", doc_unread),
    ):
        (OUT / name).write_text("".join(r["path"] + "\n" for r in data))

    decisions = json.loads((TR / "supplement-decisions.json").read_text())
    receipts = decisions.get("decisions", [])
    funwave_receipts = [x for x in receipts if str(x.get("canonical_path", "")).startswith("FUNWAVE/")]
    raw_funwave_receipts = [x for x in funwave_receipts if str(x.get("canonical_path", "")).startswith("FUNWAVE/raw/")]
    receipt_summary = {
        "source": "_staging/total-read/supplement-decisions.json",
        "declared_count": decisions.get("decision_count"),
        "actual_count": len(receipts),
        "approved_count": sum(x.get("status") == "approved" for x in receipts),
        "funwave_entry_count": len(funwave_receipts),
        "funwave_raw_entry_count": len(raw_funwave_receipts),
        "non_funwave_entry_count": len(receipts) - len(funwave_receipts),
        "approvers": sorted({x.get("approver") for x in receipts}),
        "approved_at": sorted({x.get("approved_at") for x in receipts}),
        "unique_source_files_all_corpus": len({norm(x.get("canonical_path")) for x in receipts}),
        "funwave_source_files": sorted({norm(x.get("canonical_path")) for x in funwave_receipts}),
        "instruction": "Preserve byte-for-byte; this is finding-level human authority, not whole-file read coverage.",
    }
    (OUT / "human-receipts-preservation.json").write_text(json.dumps(receipt_summary, indent=2, ensure_ascii=False) + "\n")

    class_counts = Counter(r["material_class"] for r in rows)
    ext_counts = Counter(r["extension"] for r in rows)
    unique_sha = len(by_sha)
    dup_paths = sum(len(v) for v in by_sha.values() if len(v) > 1)
    dup_groups = sum(1 for v in by_sha.values() if len(v) > 1)
    snapshots = {}
    for name in ("FUNWAVE-TVD", "FUNWAVE-GPU"):
        root = RAW / "source_code" / name
        gitdir = root / ".git"
        head = subprocess.run(["git", f"--git-dir={gitdir}", "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
        origin = subprocess.run(["git", "config", "--file", str(gitdir / "config"), "--get", "remote.origin.url"], capture_output=True, text=True).stdout.strip()
        snapshots[name] = {"head": head, "origin": origin}
    tools = {name: shutil.which(name) for name in ("file", "strings", "sha256sum", "git", "tar", "gzip", "pdfinfo", "pdftotext", "mutool", "ffprobe", "identify", "exiftool", "jq", "python3", "jupyter")}

    summary = {
        "raw_root": "models/FUNWAVE/raw",
        "regular_files": len(rows),
        "bytes": sum(r["bytes"] for r in rows),
        "unique_sha256": unique_sha,
        "duplicate_sha_groups": dup_groups,
        "paths_in_duplicate_groups": dup_paths,
        "generated_preprocessed_counterparts": sum(a[0] == "generated-preprocessed-counterpart" for a in aliases),
        "gpu_tvd_named_counterparts": sum(a[0] == "separate-repository-counterpart" for a in aliases),
        "embedded_git_metadata_files": sum(r["material_class"] == "vcs-metadata" for r in rows),
        "legacy_277_code_members_actual": sum(r["legacy_277_code_member"] for r in rows),
        "legacy_preflight_members_current_exact": sum(r["legacy_preflight_member"] for r in rows),
        "r1_code_current_exact": sum(r["r1_code_exact"] for r in rows),
        "r2_code_current_exact": sum(r["r2_code_exact"] for r in rows),
        "two_independent_code_reads_current_exact": sum(r["two_independent_code_reads_exact"] for r in rows),
        "crosswalk_current_exact": sum(r["crosswalk_exact"] for r in rows),
        "document_reads_current_exact": sum(r["document_read_exact"] for r in rows),
        "legacy_complete_reads_current_exact": sum(r["legacy_complete_read_exact"] for r in rows),
        "mechanical_inspections_current_exact": sum(r["mechanical_inspection_exact"] for r in rows),
        "semantic_complete_current_exact_union": sum(r["semantic_complete_exact"] for r in rows),
        "semantic_unread_all_raw": len(unread),
        "legacy277_code_semantic_unread": len(exact_code_unread),
        "legacy277_without_two_independent_reads": len(two_unread),
        "solver_source_without_two_independent_reads": len(solver_two_unread),
        "script_source_without_two_independent_reads": len(script_two_unread),
        "script_source_semantic_unread": len(script_unread),
        "document_manual_semantic_unread": len(doc_unread),
        "class_counts": dict(sorted(class_counts.items())),
        "extension_counts": dict(sorted(ext_counts.items())),
        "snapshots": snapshots,
        "available_tools": tools,
        "human_receipts": receipt_summary,
    }
    (OUT / "coverage-summary.json").write_text(json.dumps(summary, indent=2, ensure_ascii=False) + "\n")


if __name__ == "__main__":
    main()
