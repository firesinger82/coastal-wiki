#!/usr/bin/env python3
"""Deterministic integrity checks for the FUNWAVE connectivity preflight."""

import csv
import hashlib
import json
import subprocess
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[4]
RAW = REPO / "models/FUNWAVE/raw"


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


rows = list(csv.DictReader((HERE / "raw-inventory-read-coverage.csv").open()))
current = sorted(p.relative_to(REPO).as_posix() for p in RAW.rglob("*") if p.is_file())
listed = sorted(r["path"] for r in rows)
bad_hash = [r["path"] for r in rows if sha(REPO / r["path"]) != r["sha256"]]
summary = json.loads((HERE / "coverage-summary.json").read_text())
gate = subprocess.run([
    "python3", str(REPO / "_staging/total-read/verify_supplement.py"),
    str(REPO / "_staging/total-read/supplement-manifest.json"),
    str(REPO / "_staging/total-read/pending/reread-20260728"),
    str(REPO / "models"),
    str(REPO / "_staging/total-read/records-crosswalk/reread-20260728"),
    str(REPO / "_staging/total-read/supplement-decisions.json"),
], capture_output=True, text=True)
result = {
    "inventory_rows": len(rows),
    "current_regular_files": len(current),
    "unique_inventory_paths": len(set(listed)),
    "path_set_exact": current == listed,
    "sha256_rechecked_files": len(rows),
    "sha256_mismatches": bad_hash,
    "summary_count_matches": summary["regular_files"] == len(rows),
    "supplement_gate_exit": gate.returncode,
    "supplement_gate_last_line": gate.stdout.strip().splitlines()[-1] if gate.stdout.strip() else gate.stderr.strip(),
}
result["pass"] = all([
    result["path_set_exact"], not bad_hash, result["summary_count_matches"], gate.returncode == 0,
])
(HERE / "validation.json").write_text(json.dumps(result, indent=2, ensure_ascii=False) + "\n")
raise SystemExit(0 if result["pass"] else 1)
