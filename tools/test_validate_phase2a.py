#!/usr/bin/env python3
"""test_validate_phase2a.py — regression test suite for Phase 2a validator.

정책 출처: plan.md Sub-phase 2a (v8 — codex review 1~7차 반영, M1+M2+N1+N2+N3+O1+O2+O3)
범위:
  - Rule A 6 conditions + semantic validation (user/codex/self-cited-line)
  - Rule B dest frontmatter ↔ manifest cross-check
  - skip-readme pre/post-archive validation order
  - Inventory set equality
  - Post-archive set equality + sha256
  - Codex evidence durable archive (N2+O2) + deterministic naming (O1)
  - Self-cited-line marker raw_path resolution (N3+O3)

사용:
  python3 tools/test_validate_phase2a.py
  → exit 0 모두 통과 / exit 1 실패
"""
from __future__ import annotations

import csv
import hashlib
import io
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Callable

HERE = Path(__file__).resolve().parent
VALIDATOR = HERE / "validate-phase2a-manifest.py"

# Mirror EXPECTED_COLUMNS from the validator (must match)
COLUMNS = (
    "source_path",
    "dest_path",
    "sha256_before",
    "classification",
    "citation_status_target",
    "audit_status",
    "source_id",
    "raw_path",
    "raw_sha256",
    "captured_date",
    "claim_mapping_verified_by",
    "codex_evidence_sha256",
    "link_rewrite_needed",
    "validator_passed",
    "notes",
)

# Exit codes
EXIT_OK = 0
EXIT_RULE_A = 1
EXIT_RULE_B = 2
EXIT_RULE_AB = 3
EXIT_INVENTORY = 4
EXIT_POST_SET = 5
EXIT_POST_SHA = 6
EXIT_CODEX_EVIDENCE = 7
EXIT_CODEX_NAMING = 8
EXIT_MARKER_RESOLVE = 9


# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def write_file(path: Path, content: str | bytes) -> str:
    """Write file (creating parents), return sha256 of content."""
    path.parent.mkdir(parents=True, exist_ok=True)
    if isinstance(content, str):
        data = content.encode("utf-8")
    else:
        data = content
    path.write_bytes(data)
    return sha256_bytes(data)


def write_manifest(td: Path, rows: list[dict[str, str]], name: str = "manifest.csv") -> Path:
    p = td / name
    with p.open("w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=COLUMNS)
        writer.writeheader()
        for r in rows:
            writer.writerow({k: r.get(k, "") for k in COLUMNS})
    return p


def write_dest(td: Path, rel: str, citation_status: str, body: str = "body") -> None:
    p = td / rel
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(
        f"---\ncitation_status: {citation_status}\n---\n{body}\n",
        encoding="utf-8",
    )


def write_sources_yaml(td: Path, entries: list[dict[str, str]]) -> None:
    p = td / "textbook" / "sources.yml"
    p.parent.mkdir(parents=True, exist_ok=True)
    lines = ["sources:"]
    for e in entries:
        sid = e["source_id"]
        lines.append(f"  - source_id: {sid}")
        for k, v in e.items():
            if k == "source_id":
                continue
            lines.append(f"    {k}: {v}")
    lines.append("")
    p.write_text("\n".join(lines), encoding="utf-8")


def write_allowlist(td: Path, names: list[str] | None = None) -> None:
    if names is None:
        names = ["firesinger"]
    p = td / "tools" / "manifests" / "reviewer-allowlist.txt"
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text("\n".join(names) + "\n", encoding="utf-8")


def write_codex_archive(td: Path, session_id: str, content: bytes) -> str:
    """Write _archive/codex-reviews/<session_id>.output + update sums.txt.
    Returns sha256 of content."""
    archive_dir = td / "_archive" / "codex-reviews"
    archive_dir.mkdir(parents=True, exist_ok=True)
    out_path = archive_dir / f"{session_id}.output"
    out_path.write_bytes(content)
    sha = sha256_bytes(content)
    sums = archive_dir / "sha256sums.txt"
    existing: list[str] = []
    if sums.exists():
        existing = [
            line for line in sums.read_text(encoding="utf-8").splitlines()
            if line.strip() and f"{session_id}.output" not in line
        ]
    existing.append(f"{sha}  {session_id}.output")
    sums.write_text("\n".join(existing) + "\n", encoding="utf-8")
    return sha


def write_codex_archive_named(
    td: Path, filename: str, content: bytes
) -> None:
    """Write an arbitrarily-named file under _archive/codex-reviews/
    (without updating sums.txt) — for O1 non-deterministic naming fixture."""
    archive_dir = td / "_archive" / "codex-reviews"
    archive_dir.mkdir(parents=True, exist_ok=True)
    (archive_dir / filename).write_bytes(content)


def baseline_setup(td: Path) -> None:
    """Common setup: allowlist + minimal sources.yml (empty list)."""
    write_allowlist(td)
    # empty sources.yml
    (td / "textbook").mkdir(parents=True, exist_ok=True)
    (td / "textbook" / "sources.yml").write_text("sources:\n", encoding="utf-8")


def run_validator(
    td: Path,
    *,
    mode: str = "pre-archive",
    today: str = "2026-05-24",
    extra_args: list[str] | None = None,
) -> tuple[int, str]:
    cmd = [
        sys.executable,
        str(VALIDATOR),
        "--manifest", "manifest.csv",
        "--root", str(td),
        "--mode", mode,
        "--today", today,
    ]
    if extra_args:
        cmd.extend(extra_args)
    res = subprocess.run(cmd, capture_output=True, text=True, check=False)
    return res.returncode, res.stdout + res.stderr


# ------------------------------------------------------------------
# Fixture builders — each returns (description, setup, expected_exit, extra_args)
# ------------------------------------------------------------------


def fx_01_verified_pass(td: Path) -> tuple[int, dict]:
    """Fixture 1: verified row (codex form) — all conditions met → exit 0."""
    baseline_setup(td)
    session = "019e528e-0231-7573-b03d-eaf9506a6c1b"
    codex_sha = write_codex_archive(td, session, b"codex review output content\n")
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake pdf content")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src body\n")
    write_dest(td, "concepts/x/foo.md", "verified")
    write_sources_yaml(td, [
        {"source_id": "pugh-sea-level", "filename": "pugh.pdf",
         "raw_path": "textbook/raw/pugh.pdf"},
    ])
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "audit_status": "",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "captured_date": "",
        "claim_mapping_verified_by": f"codex-review-{session}",
        "codex_evidence_sha256": codex_sha,
        "link_rewrite_needed": "false",
        "validator_passed": "",
        "notes": "",
    }
    write_manifest(td, [row])
    return EXIT_OK, {}


def fx_02_empty_verified_by(td: Path) -> tuple[int, dict]:
    """Fixture 2: verified target but claim_mapping_verified_by empty → exit 1."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "",
    }
    write_manifest(td, [row])
    return EXIT_RULE_A, {}


def fx_03_user_date_out_of_range(td: Path) -> tuple[int, dict]:
    """Fixture 3: user-form regex OK but date < 2024-01-01 → exit 1 (M1 semantic)."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "user-firesinger-19990101",
    }
    write_manifest(td, [row])
    return EXIT_RULE_A, {}


def fx_04_codex_archive_missing(td: Path) -> tuple[int, dict]:
    """Fixture 4: codex-review form but archive file 부재 → exit 7 (N2)."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    # Don't create the codex archive file — only a dummy sha
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "codex-review-019eaaaa-0000-0000-0000-000000000001",
        "codex_evidence_sha256": "0" * 64,
    }
    write_manifest(td, [row])
    return EXIT_CODEX_EVIDENCE, {}


def fx_05_self_cite_file_missing(td: Path) -> tuple[int, dict]:
    """Fixture 5: self-cited-line points to a file that doesn't exist → exit 1."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "self-cited-line-models/NONE/missing.md:999",
    }
    write_manifest(td, [row])
    return EXIT_RULE_A, {}


def fx_06_self_cite_no_marker_on_line(td: Path) -> tuple[int, dict]:
    """Fixture 6: self-cited-line file·line exist but no marker on exact line → exit 1 (N3 strict)."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    # Sample file with no citation markers
    sample = (
        "line1\n"
        "line2\n"
        "line3 see (pugh-sea-level §6:3)\n"   # marker on line 3
        "line4\n"
        "line5 plain text no marker here\n"   # marker absent on line 5
    )
    write_file(td / "tests" / "sample.md", sample)
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "self-cited-line-tests/sample.md:5",
    }
    write_manifest(td, [row])
    return EXIT_RULE_A, {}


def fx_07_sha256_before_mismatch(td: Path) -> tuple[int, dict]:
    """Fixture 7: source_path 의 실제 sha256 != manifest sha256_before → exit 1."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "actual content")
    write_dest(td, "concepts/x/foo.md", "verified")
    write_sources_yaml(td, [{"source_id": "pugh-sea-level", "filename": "pugh.pdf"}])
    session = "019e528e-0231-7573-b03d-eaf9506a6c1b"
    codex_sha = write_codex_archive(td, session, b"x")
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": "0" * 64,  # bogus
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": f"codex-review-{session}",
        "codex_evidence_sha256": codex_sha,
    }
    write_manifest(td, [row])
    return EXIT_RULE_A, {}


def fx_08_rule_b_frontmatter_mismatch(td: Path) -> tuple[int, dict]:
    """Fixture 8: dest frontmatter=verified, manifest target=source-needed → exit 2 (Rule B)."""
    baseline_setup(td)
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "x")
    write_dest(td, "concepts/x/foo.md", "verified")  # dest verified
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "experience-mixed",
        "citation_status_target": "source-needed",   # mismatch
    }
    write_manifest(td, [row])
    return EXIT_RULE_B, {}


def fx_09_source_needed_pass(td: Path) -> tuple[int, dict]:
    """Fixture 9: target=source-needed minimal row + matching dest frontmatter → exit 0."""
    baseline_setup(td)
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "x")
    write_dest(td, "experience/foo.md", "source-needed")
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "experience/foo.md",
        "sha256_before": src_sha,
        "classification": "experience-only",
        "citation_status_target": "source-needed",
    }
    write_manifest(td, [row])
    return EXIT_OK, {}


def fx_10_skip_readme_prearchive(td: Path) -> tuple[int, dict]:
    """Fixture 10: skip-readme, pre-archive mode → Rule B 면제 → exit 0."""
    baseline_setup(td)
    src_sha = write_file(
        td / "_staging" / "from-modeling-wiki" / "knowledge" / "playbooks" / "README.md",
        "readme content",
    )
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/playbooks/README.md",
        "dest_path": "_archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/playbooks/README.md",
        "sha256_before": src_sha,
        "classification": "skip-readme",
        "citation_status_target": "n/a",
        "link_rewrite_needed": "false",
    }
    write_manifest(td, [row])
    return EXIT_OK, {}


def fx_11_skip_readme_postarchive(td: Path) -> tuple[int, dict]:
    """Fixture 11: skip-readme, post-archive mode, archive file exists + sha match → exit 0."""
    baseline_setup(td)
    content = b"readme content\n"
    src_sha = write_file(
        td / "_staging" / "from-modeling-wiki" / "knowledge" / "playbooks" / "README.md",
        content,
    )
    # Copy to archive location
    write_file(
        td / "_archive" / "from-modeling-wiki-knowledge-phase2a-2026-05-23" / "playbooks" / "README.md",
        content,
    )
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/playbooks/README.md",
        "dest_path": "_archive/from-modeling-wiki-knowledge-phase2a-2026-05-23/playbooks/README.md",
        "sha256_before": src_sha,
        "classification": "skip-readme",
        "citation_status_target": "n/a",
    }
    write_manifest(td, [row])
    return EXIT_OK, {"mode": "post-archive"}


def fx_12_postarchive_sha_mismatch(td: Path) -> tuple[int, dict]:
    """Fixture 12: post-archive 시 content row 의 archive sha != sha256_before → exit 6 (M2)."""
    baseline_setup(td)
    src_sha = write_file(
        td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "original"
    )
    write_dest(td, "experience/foo.md", "source-needed")
    # Archive copy with DIFFERENT content
    write_file(
        td / "_archive" / "from-modeling-wiki-knowledge-phase2a-2026-05-23" / "foo.md",
        "TAMPERED",
    )
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "experience/foo.md",
        "sha256_before": src_sha,
        "classification": "experience-only",
        "citation_status_target": "source-needed",
    }
    write_manifest(td, [row])
    return EXIT_POST_SHA, {"mode": "post-archive"}


def fx_13_postarchive_missing_in_archive(td: Path) -> tuple[int, dict]:
    """Fixture 13: post-archive, manifest expects file X but X not in archive → exit 5 (N1)."""
    baseline_setup(td)
    src_sha = write_file(
        td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "x"
    )
    write_dest(td, "experience/foo.md", "source-needed")
    # Create archive dir but don't put expected file
    (td / "_archive" / "from-modeling-wiki-knowledge-phase2a-2026-05-23").mkdir(
        parents=True, exist_ok=True
    )
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "experience/foo.md",
        "sha256_before": src_sha,
        "classification": "experience-only",
        "citation_status_target": "source-needed",
    }
    write_manifest(td, [row])
    return EXIT_POST_SET, {"mode": "post-archive"}


def fx_14_postarchive_extra_in_archive(td: Path) -> tuple[int, dict]:
    """Fixture 14: post-archive, archive has file not in manifest → exit 5 (N1)."""
    baseline_setup(td)
    content = b"x"
    src_sha = write_file(
        td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", content
    )
    write_dest(td, "experience/foo.md", "source-needed")
    # Expected
    write_file(
        td / "_archive" / "from-modeling-wiki-knowledge-phase2a-2026-05-23" / "foo.md",
        content,
    )
    # EXTRA file not in manifest
    write_file(
        td / "_archive" / "from-modeling-wiki-knowledge-phase2a-2026-05-23" / "extra.md",
        "stray",
    )
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "experience/foo.md",
        "sha256_before": src_sha,
        "classification": "experience-only",
        "citation_status_target": "source-needed",
    }
    write_manifest(td, [row])
    return EXIT_POST_SET, {"mode": "post-archive"}


def fx_15_n2_ephemeral_only(td: Path) -> tuple[int, dict]:
    """Fixture 15: codex-review row but only ephemeral path (no durable archive) → exit 7."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    # No write_codex_archive — archive dir doesn't exist (or empty)
    # Simulate "user only has /tmp/claude-*/ output" — validator should reject
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "codex-review-019ebbbb-0000-0000-0000-000000000002",
        "codex_evidence_sha256": "a" * 64,
    }
    write_manifest(td, [row])
    return EXIT_CODEX_EVIDENCE, {}


def fx_16_n2_codex_hash_mismatch(td: Path) -> tuple[int, dict]:
    """Fixture 16: archive file 존재 but codex_evidence_sha256 mismatch → exit 7."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    session = "019e528e-0231-7573-b03d-eaf9506a6c1b"
    # Real codex archive
    actual_codex_sha = write_codex_archive(td, session, b"real content\n")
    # Manifest declares WRONG sha
    wrong_sha = "f" * 64
    assert actual_codex_sha != wrong_sha
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": f"codex-review-{session}",
        "codex_evidence_sha256": wrong_sha,
    }
    write_manifest(td, [row])
    return EXIT_CODEX_EVIDENCE, {}


def fx_17_self_cite_html_comment_pass(td: Path) -> tuple[int, dict]:
    """Fixture 17: self-cited-line + HTML cite marker at exact line → exit 0 (N3 explicit)."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    # Line 3 has HTML cite marker with raw_path
    sample = (
        "line1\n"
        "line2\n"
        "<!-- cite:source_id=pugh-sea-level,raw_path=textbook/raw/pugh.pdf,page=194 -->\n"
        "line4\n"
    )
    write_file(td / "concepts" / "x" / "sample.md", sample)
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "self-cited-line-concepts/x/sample.md:3",
    }
    write_manifest(td, [row])
    return EXIT_OK, {}


def fx_18_self_cite_proximity_no_exact(td: Path) -> tuple[int, dict]:
    """Fixture 18: marker exists at line 3 (within ±3 of line 5) but line 5 itself has no marker → exit 1 (N3 strict)."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    sample = (
        "line1\n"
        "line2\n"
        "<!-- cite:source_id=pugh-sea-level,raw_path=textbook/raw/pugh.pdf -->\n"  # line 3
        "line4\n"
        "line5 plain prose with NO marker\n"   # line 5 — pointed to but empty
        "line6\n"
    )
    write_file(td / "concepts" / "x" / "sample.md", sample)
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "self-cited-line-concepts/x/sample.md:5",  # line 5, no marker
    }
    write_manifest(td, [row])
    return EXIT_RULE_A, {}


def fx_19_o1_non_deterministic_naming(td: Path) -> tuple[int, dict]:
    """Fixture 19 (O1): archive has <id>.log instead of <id>.output → exit 8."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    session = "019ecccc-0000-0000-0000-000000000003"
    # Wrong extension — .log instead of .output
    write_codex_archive_named(td, f"{session}.log", b"content")
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": f"codex-review-{session}",
        "codex_evidence_sha256": sha256_bytes(b"content"),
    }
    write_manifest(td, [row])
    return EXIT_CODEX_NAMING, {}


def fx_20_o2_codex_sha_empty(td: Path) -> tuple[int, dict]:
    """Fixture 20 (O2): codex-review row 의 codex_evidence_sha256 empty → exit 7."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    session = "019e528e-0231-7573-b03d-eaf9506a6c1b"
    write_codex_archive(td, session, b"x")
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": f"codex-review-{session}",
        "codex_evidence_sha256": "",   # empty → O2 violation
    }
    write_manifest(td, [row])
    return EXIT_CODEX_EVIDENCE, {}


def fx_21_o3_inline_resolve_pass(td: Path) -> tuple[int, dict]:
    """Fixture 21 (O3): inline citation `(pugh-sea-level …)` resolves to manifest raw_path via sources.yml → exit 0."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    write_sources_yaml(td, [
        {"source_id": "pugh-sea-level", "filename": "pugh.pdf",
         "raw_path": "textbook/raw/pugh.pdf"},
    ])
    sample = (
        "line1\n"
        "line2 see (pugh-sea-level §6:3 p.194) for details\n"   # line 2 — inline citation
        "line3\n"
    )
    write_file(td / "concepts" / "x" / "sample.md", sample)
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "self-cited-line-concepts/x/sample.md:2",
    }
    write_manifest(td, [row])
    return EXIT_OK, {}


def fx_22_o3_inline_resolve_fail(td: Path) -> tuple[int, dict]:
    """Fixture 22 (O3): inline citation `(pugh-sea-level …)` BUT sources.yml filename != manifest raw_path → exit 9."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "right.pdf", "real")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    # sources.yml entry points to WRONG raw_path
    write_sources_yaml(td, [
        {"source_id": "pugh-sea-level",
         "filename": "OTHER-DOCUMENT.pdf",
         "raw_path": "textbook/raw/wrong.pdf"},
    ])
    sample = (
        "line1\n"
        "line2 (pugh-sea-level §6:3 p.194) inline cite\n"
        "line3\n"
    )
    write_file(td / "concepts" / "x" / "sample.md", sample)
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/right.pdf",   # manifest claims `right.pdf`
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "self-cited-line-concepts/x/sample.md:2",
    }
    write_manifest(td, [row])
    return EXIT_MARKER_RESOLVE, {}


# Extras (not required but useful)


def fx_23_self_cite_src_code_ref(td: Path) -> tuple[int, dict]:
    """Bonus: self-cited-line + source-code reference `file.F:5798` matches manifest raw_path basename → exit 0."""
    baseline_setup(td)
    raw_sha = write_file(
        td / "models" / "ADCIRC" / "raw" / "source_code" / "wind.F",
        "fortran wind module\n" * 1000,
    )
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    sample = (
        "line1 (wind.F:5798) implements NWS=13\n"
    )
    write_file(td / "concepts" / "x" / "sample.md", sample)
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "adcirc-source",
        "raw_path": "models/ADCIRC/raw/source_code/wind.F",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "self-cited-line-concepts/x/sample.md:1",
    }
    write_manifest(td, [row])
    return EXIT_OK, {}


def fx_24_user_form_pass(td: Path) -> tuple[int, dict]:
    """Bonus: user-firesinger-20260524 with date in range and name in allowlist → exit 0."""
    baseline_setup(td)
    raw_sha = write_file(td / "textbook" / "raw" / "pugh.pdf", "fake")
    src_sha = write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "foo.md", "src")
    write_dest(td, "concepts/x/foo.md", "verified")
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "concepts/x/foo.md",
        "sha256_before": src_sha,
        "classification": "source-analysis",
        "citation_status_target": "verified",
        "source_id": "pugh-sea-level",
        "raw_path": "textbook/raw/pugh.pdf",
        "raw_sha256": raw_sha,
        "claim_mapping_verified_by": "user-firesinger-20260524",
    }
    write_manifest(td, [row])
    return EXIT_OK, {}


def fx_25_inventory_diff(td: Path) -> tuple[int, dict]:
    """Bonus: manifest source_path vs filesystem 의 set equality 실패 → exit 4 (J4)."""
    baseline_setup(td)
    # manifest references foo.md, but actually bar.md exists on disk
    write_file(td / "_staging" / "from-modeling-wiki" / "knowledge" / "bar.md", "bar")
    write_dest(td, "experience/foo.md", "source-needed")
    row = {
        "source_path": "_staging/from-modeling-wiki/knowledge/foo.md",
        "dest_path": "experience/foo.md",
        "sha256_before": "",
        "classification": "experience-only",
        "citation_status_target": "source-needed",
    }
    write_manifest(td, [row])
    return EXIT_INVENTORY, {
        "extra_args": ["--inventory-source", "_staging/from-modeling-wiki/knowledge"],
    }


# ------------------------------------------------------------------
# Runner
# ------------------------------------------------------------------


FIXTURES: list[tuple[str, Callable[[Path], tuple[int, dict]]]] = [
    ("01 verified codex-form pass", fx_01_verified_pass),
    ("02 verified fail — claim_mapping_verified_by empty", fx_02_empty_verified_by),
    ("03 verified fail — user-form date out of range (M1)", fx_03_user_date_out_of_range),
    ("04 verified fail — codex archive missing (N2)", fx_04_codex_archive_missing),
    ("05 verified fail — self-cited-line file 부재", fx_05_self_cite_file_missing),
    ("06 verified fail — self-cited-line no marker on exact line (N3)", fx_06_self_cite_no_marker_on_line),
    ("07 verified fail — sha256_before mismatch", fx_07_sha256_before_mismatch),
    ("08 verified fail — dest frontmatter ↔ manifest target (Rule B)", fx_08_rule_b_frontmatter_mismatch),
    ("09 source-needed pass", fx_09_source_needed_pass),
    ("10 skip-readme pre-archive (Rule B 면제)", fx_10_skip_readme_prearchive),
    ("11 skip-readme post-archive (sha match)", fx_11_skip_readme_postarchive),
    ("12 post-archive content sha256 mismatch (M2)", fx_12_postarchive_sha_mismatch),
    ("13 post-archive set equality — missing in archive (N1)", fx_13_postarchive_missing_in_archive),
    ("14 post-archive set equality — extra in archive (N1)", fx_14_postarchive_extra_in_archive),
    ("15 N2 ephemeral-only evidence rejection", fx_15_n2_ephemeral_only),
    ("16 N2 archived codex output hash mismatch", fx_16_n2_codex_hash_mismatch),
    ("17 N3 self-cited-line HTML comment marker pass", fx_17_self_cite_html_comment_pass),
    ("18 N3 false-positive proximity but no marker on cited line", fx_18_self_cite_proximity_no_exact),
    ("19 O1 codex archive non-deterministic naming rejected", fx_19_o1_non_deterministic_naming),
    ("20 O2 codex_evidence_sha256 missing", fx_20_o2_codex_sha_empty),
    ("21 O3 inline citation marker raw_path resolution pass", fx_21_o3_inline_resolve_pass),
    ("22 O3 inline citation raw_path resolution fail", fx_22_o3_inline_resolve_fail),
    # Bonus
    ("23 self-cited-line + source-code ref (extra)", fx_23_self_cite_src_code_ref),
    ("24 user-firesinger-20260524 pass (extra)", fx_24_user_form_pass),
    ("25 inventory set equality diff (extra)", fx_25_inventory_diff),
]


def run_one(name: str, setup: Callable[[Path], tuple[int, dict]]) -> tuple[bool, str]:
    with tempfile.TemporaryDirectory() as raw:
        td = Path(raw).resolve()
        expected, opts = setup(td)
        mode = opts.get("mode", "pre-archive")
        extra_args = opts.get("extra_args")
        code, output = run_validator(td, mode=mode, extra_args=extra_args)
        if code == expected:
            return True, ""
        return False, (
            f"  expected exit {expected}, got {code}\n"
            + "  --- validator output ---\n"
            + "\n".join("  " + l for l in output.splitlines())
        )


def main() -> int:
    print(f"[test_validate_phase2a] validator: {VALIDATOR}")
    passed = failed = 0
    failures: list[tuple[str, str]] = []
    for name, setup in FIXTURES:
        ok, msg = run_one(name, setup)
        if ok:
            print(f"  PASS  {name}")
            passed += 1
        else:
            print(f"  FAIL  {name}")
            failures.append((name, msg))
            failed += 1
    print()
    if failures:
        print("=" * 60)
        for name, msg in failures:
            print(f"FAIL: {name}")
            print(msg)
            print()
    print(f"RESULT: {passed} passed, {failed} failed (of {len(FIXTURES)})")
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
