#!/usr/bin/env python3
"""validate-phase2a-manifest.py — coastal-wiki Phase 2a validator.

정책 출처: plan.md "Sub-phase 2a" (v8 — codex review 1~7차 반영)
결정 근거: J1·J2·J4·K1·K2·L1·L2·M1·M2·N1·N2·N3·O1·O2·O3

검사 (manifest CSV row 단위):
  Rule A — citation_status_target = verified 강제 조건 (6 conditions):
    1. classification=manual-notes-catalog → audit_status=audited
    2. source_id non-empty
    3. raw_path non-empty
    4. raw_path 가 local 파일 → 존재 + sha256 == raw_sha256
    5. raw_path 가 외부 URL → captured_date non-empty
    6. claim_mapping_verified_by non-empty + semantic validation
       (user / codex-review / self-cited-line form 별 추가 검증)
  Rule B — dest_path 파일 frontmatter ↔ manifest citation_status_target 일치
    (skip-readme 는 pre-archive 시 면제, post-archive 시 archive 위치 + sha256 check)
  Post-archive (mode=post-archive):
    - expected (manifest 의 archive_path_for(source_path)) vs actual (filesystem)
      set equality (N1)
    - 각 archive 파일의 sha256 == sha256_before (M2)

도구 범위:
  validate-research-isolation.py 와 같은 conservative policy scanner. CSV·YAML·
  HTML 의 모든 spec 변형을 cover 하지 않음. 일반 manifest 작성 실수 + plan v8 의
  명시 위반 형태 catch 가 1차 목표. 의심 시 사용자 + ultrareview multi-defense.

  의도적 scope 제외 (codex review f497ad6 1차 + dbc8946 2차 명시):
    - archive 트리의 symlink: expected/actual set 둘 다 .resolve() 로 follow target.
      symlink 로 다른 파일 대체 시 catch 안 됨. 1회성 migration 후 archive 트리는
      외부 수정 게이트 (사용자 명시 OK) 로 관리.
    - Unicode NFC/NFD 경로 정규화: macOS NFD vs Linux NFC 경계 케이스 미커버.
      WSL2 ext4 단일 환경 가정. manifest 작성자가 NFC 만 사용 의무.
    - HTML cite marker 의 raw_path 매칭은 byte-exact 직접 equality (plan §693).
      canonical forward slash, no leading `./`, no Windows separators. 위
      형식 위반 시 reject (false-positive 처럼 보이지만 spec 강제).
    (F2-3 의 "null" literal 은 load_manifest 에서 empty 로 정규화하므로 scope 안)

사용:
  python3 tools/validate-phase2a-manifest.py --manifest <csv>
      [--mode pre-archive|post-archive] [--root <dir>] [--archive-root <dir>]
      [--codex-archive-dir <dir>] [--sources-yml <path>]
      [--reviewer-allowlist <path>] [--inventory-source <dir>]
      [--today <YYYY-MM-DD>]

Exit codes (우선순위: highest-specific 먼저):
  0 = OK
  1 = Rule A fail (verified row condition mismatch)
  2 = Rule B fail (dest frontmatter ↔ manifest mismatch)
  3 = Rule A + Rule B 모두
  4 = inventory set equality fail (manifest source_path vs filesystem)
  5 = post-archive set equality fail (N1)
  6 = post-archive sha256 mismatch (M2)
  7 = codex evidence archive 부재 / hash mismatch / sums.txt cross-check fail (N2+O2)
  8 = codex archive naming non-deterministic (O1)
  9 = marker raw_path resolution fail (O3)

우선순위: 8 > 7 > 9 > 4 > 5 > 6 > 3 > 1 > 2 > 0
"""
from __future__ import annotations

import argparse
import csv
import hashlib
import os
import re
import sys
from datetime import date, datetime
from pathlib import Path

# ------------------------------------------------------------------
# Exit codes
# ------------------------------------------------------------------

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

# Bucket order for picking the final exit code (most specific first)
PRIORITY = (
    EXIT_CODEX_NAMING,
    EXIT_CODEX_EVIDENCE,
    EXIT_MARKER_RESOLVE,
    EXIT_INVENTORY,
    EXIT_POST_SET,
    EXIT_POST_SHA,
)

# ------------------------------------------------------------------
# Manifest schema
# ------------------------------------------------------------------

EXPECTED_COLUMNS = (
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

VALID_CLASSIFICATIONS = {
    "source-analysis",
    "experience-mixed",
    "experience-only",
    "manual-notes-catalog",
    "skip-readme",
}

VALID_TARGETS = {"verified", "source-needed", "n/a"}

# H1 (codex review f497ad6 1차) + F2-2 (codex review dbc8946 2차):
# sources.yml 미등록 source_id 의 허용 prefix.
# - `internal:` = explicit escape hatch (existence check 면제)
# - 나머지 prefix = wiki layer 의 path-like source_id, 실제 `root/<sid>` 존재 강제
#
# 의도적 제외:
#   `research/` — workbench 영역. promote 후만 canonical, source_id 로 직접 인용 금지
#   `textbook/` — 모든 textbook 인용은 sources.yml 의 source_id 기반 (canonical)
INTERNAL_SOURCE_ID_PREFIXES = (
    "internal:",
    "models/",
    "concepts/",
    "experience/",
    "data/",
    "tools/",
)
INTERNAL_PREFIX_EXEMPT_EXISTENCE = ("internal:",)

# ------------------------------------------------------------------
# Regexes
# ------------------------------------------------------------------

USER_FORM_RE = re.compile(r"^user-(?P<name>\S+?)-(?P<date>\d{8})$")
CODEX_FORM_RE = re.compile(r"^codex-review-(?P<session_id>019e[0-9a-f-]+)$")
SELF_LINE_RE = re.compile(r"^self-cited-line-(?P<file>.+):(?P<line>\d+)$")

HTML_CITE_MARKER_RE = re.compile(
    r"<!--\s*cite:source_id=(?P<sid>[^,\s>]+)"
    r"(?:,raw_path=(?P<raw>[^,\s>]+))?"
    r"(?:,page=\d+)?"
    r"(?:,line=\d+)?\s*-->"
)
SOURCE_CODE_REF_RE = re.compile(
    r"(?P<path>(?:[\w./\-]+/)?(?P<base>[\w.\-]+\.[A-Za-z][\w]*)):(?P<line>\d+)"
)

FRONTMATTER_RE = re.compile(r"\A---\n(.*?)\n---", re.DOTALL)
CITATION_STATUS_RE = re.compile(r"(?m)^citation_status:\s*(\S+)\s*$")

URL_SCHEME_RE = re.compile(r"^[a-zA-Z][a-zA-Z0-9+.\-]*://")

# ------------------------------------------------------------------
# Helpers
# ------------------------------------------------------------------


def sha256_of(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def parse_sha256sums(path: Path) -> dict[str, str]:
    """`sha256sum *.output` 출력 형식 파싱 → {filename: hash}."""
    entries: dict[str, str] = {}
    if not path.exists():
        return entries
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        # "<hash>  <filename>" or "<hash> *<filename>"
        m = re.match(r"^([0-9a-f]{64})\s+\*?(.+)$", line)
        if m:
            entries[m.group(2)] = m.group(1)
    return entries


def parse_sources_yaml(path: Path) -> dict[str, dict[str, str]]:
    """textbook/sources.yml 의 source_id → {filename, raw_path, ...} 매핑.

    PyYAML 없이 plan v8 의 schema 만 cover. multi-line `notes: |` block 은 무시.
    """
    if not path.exists():
        return {}
    text = path.read_text(encoding="utf-8", errors="replace")
    entries: dict[str, dict[str, str]] = {}
    current_id: str | None = None
    current: dict[str, str] = {}
    entry_re = re.compile(r"^\s*-\s*source_id:\s*(\S+)\s*$")
    field_re = re.compile(r"^\s+(\w+):\s*(.+?)\s*$")
    for raw in text.splitlines():
        m = entry_re.match(raw)
        if m:
            if current_id:
                entries[current_id] = current
            current_id = m.group(1)
            current = {}
            continue
        m = field_re.match(raw)
        if m and current_id:
            key = m.group(1)
            val = m.group(2)
            if val == "|":
                continue  # multi-line block, skip
            if val.lower() == "null":
                continue
            current[key] = val
    if current_id:
        entries[current_id] = current
    return entries


def load_reviewer_allowlist(path: Path) -> set[str]:
    if not path.exists():
        return set()
    names: set[str] = set()
    for line in path.read_text(encoding="utf-8", errors="replace").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        names.add(line)
    return names


_NULL_LITERALS = {"null", "none"}


def _normalise_cell(val: str | None) -> str:
    """F2-3 (codex review dbc8946 2차): literal 'null'/'none' (case-insensitive)
    을 empty 로 정규화. CSV 작성 시 빈 값을 'null' 로 잘못 쓴 경우의 우회 차단."""
    if val is None:
        return ""
    s = val.strip()
    if s.lower() in _NULL_LITERALS:
        return ""
    return s


def load_manifest(path: Path) -> list[dict[str, str]]:
    with path.open("r", encoding="utf-8", newline="") as f:
        reader = csv.DictReader(f)
        if reader.fieldnames is None:
            raise SystemExit(f"manifest 비어있음: {path}")
        missing_cols = set(EXPECTED_COLUMNS) - set(reader.fieldnames)
        if missing_cols:
            raise SystemExit(
                f"manifest 컬럼 누락: {sorted(missing_cols)} (have {reader.fieldnames})"
            )
        rows: list[dict[str, str]] = []
        for row in reader:
            # Normalise: strip + treat missing as empty + null/none literal → empty
            normalised = {
                col: _normalise_cell(row.get(col)) for col in EXPECTED_COLUMNS
            }
            rows.append(normalised)
        return rows


# ------------------------------------------------------------------
# Rule A — form validators
# ------------------------------------------------------------------


def verify_user_form(
    verified_by: str, today: date, allowlist: set[str]
) -> tuple[int, str]:
    m = USER_FORM_RE.match(verified_by)
    if not m:
        return EXIT_RULE_A, f"user-form regex 불일치: {verified_by}"
    name = m.group("name")
    date_str = m.group("date")
    try:
        d = datetime.strptime(date_str, "%Y%m%d").date()
    except ValueError as e:
        return EXIT_RULE_A, f"date parse 실패: {e}"
    if d < date(2024, 1, 1):
        return EXIT_RULE_A, f"date {d} earlier than 2024-01-01"
    if d > today:
        return EXIT_RULE_A, f"date {d} later than today {today}"
    if name not in allowlist:
        return EXIT_RULE_A, f"name '{name}' 가 reviewer-allowlist.txt 에 없음"
    return EXIT_OK, ""


def verify_codex_form(
    verified_by: str,
    codex_evidence_sha256: str,
    archive_dir: Path,
    sums_txt: Path,
) -> tuple[int, str]:
    m = CODEX_FORM_RE.match(verified_by)
    if not m:
        return EXIT_RULE_A, f"codex-review form regex 불일치: {verified_by}"
    session_id = m.group("session_id")

    # O2: codex_evidence_sha256 mandatory
    if not codex_evidence_sha256:
        return (
            EXIT_CODEX_EVIDENCE,
            f"codex_evidence_sha256 empty for {verified_by} (O2)",
        )

    archive_path = archive_dir / f"{session_id}.output"

    # 1. archive 파일 존재
    if not archive_path.exists():
        # O1: 같은 session_id 가 다른 이름으로 존재하는지 확인
        if archive_dir.is_dir():
            candidates = [
                p for p in archive_dir.iterdir() if session_id in p.name and p != archive_path
            ]
            if candidates:
                names = ", ".join(p.name for p in candidates)
                return (
                    EXIT_CODEX_NAMING,
                    f"non-deterministic naming: expected {archive_path.name} but "
                    f"found {names} (O1)",
                )
        return EXIT_CODEX_EVIDENCE, f"archive 파일 부재: {archive_path} (N2)"

    # 2. archive 파일 실제 sha256 == manifest sha256
    actual_sha = sha256_of(archive_path)
    if actual_sha != codex_evidence_sha256:
        return (
            EXIT_CODEX_EVIDENCE,
            f"{archive_path.name} sha256 {actual_sha[:16]}… != "
            f"manifest {codex_evidence_sha256[:16]}… (N2)",
        )

    # 3. sha256sums.txt cross-check
    if not sums_txt.exists():
        return EXIT_CODEX_EVIDENCE, f"sha256sums.txt 부재: {sums_txt} (N2)"
    sums = parse_sha256sums(sums_txt)
    target_name = f"{session_id}.output"
    if target_name not in sums:
        return EXIT_CODEX_EVIDENCE, f"sums.txt 에 {target_name} 엔트리 없음 (N2)"
    if sums[target_name] != codex_evidence_sha256:
        return (
            EXIT_CODEX_EVIDENCE,
            f"sums.txt {target_name} hash {sums[target_name][:16]}… != "
            f"manifest {codex_evidence_sha256[:16]}… (N2)",
        )

    return EXIT_OK, ""


def is_registered_source_id(
    sid: str,
    sources: dict[str, dict[str, str]],
    root: Path,
) -> bool:
    """H1+F2-2+R3-1: source_id 가 sources.yml 에 등록 OR internal-ref prefix 인지.

    internal: prefix 는 existence check 면제 (escape hatch). 다른 prefix
    (models/, concepts/, …) 는 root/<sid> 가 실제 존재 + repo 안 (containment).

    R3-1 (codex review 8e70e38 3차): existence check 만으론 `models/../research/foo`
    traversal 이나 `models/link-outside` repo escape symlink 우회 가능. resolve()
    후 root 안인지 강제.
    """
    if not sid:
        return False
    if sid in sources:
        return True
    for p in INTERNAL_SOURCE_ID_PREFIXES:
        if not sid.startswith(p):
            continue
        if p in INTERNAL_PREFIX_EXEMPT_EXISTENCE:
            return True
        # path-like prefix: traversal/abs/symlink-escape 모두 차단 후 existence
        if not _is_repo_relative_path(sid, root):
            return False
        return (root / sid).exists()
    return False


def _is_repo_relative_path(file_rel: str, wiki_root: Path) -> bool:
    """H3: file_rel 이 wiki_root 안 (no traversal) repo-relative 경로인지.

    거부: 절대 경로, '..' 세그먼트 포함, resolve 결과가 wiki_root 밖.
    """
    if not file_rel:
        return False
    if file_rel.startswith("/") or file_rel.startswith("\\"):
        return False
    parts = file_rel.replace("\\", "/").split("/")
    if any(seg == ".." for seg in parts):
        return False
    try:
        abs_root = wiki_root.resolve()
        abs_target = (wiki_root / file_rel).resolve()
    except (OSError, RuntimeError):
        return False
    try:
        abs_target.relative_to(abs_root)
    except ValueError:
        return False
    return True


def _matches_raw_path(yaml_value: str, manifest_raw_path: str) -> bool:
    """sources.yml 의 filename/raw_path 값과 manifest 의 raw_path 의 호환성 판정.

    equality / suffix-match / prefix-match — plan §694 의 'prefix-match 또는 equality'
    """
    if not yaml_value or not manifest_raw_path:
        return False
    if yaml_value == manifest_raw_path:
        return True
    if manifest_raw_path.endswith(yaml_value):
        return True
    if yaml_value.endswith(manifest_raw_path):
        return True
    if manifest_raw_path.startswith(yaml_value):
        return True
    if yaml_value.startswith(manifest_raw_path):
        return True
    # basename match (가장 약함, 마지막 fallback)
    if os.path.basename(yaml_value) == os.path.basename(manifest_raw_path):
        return True
    return False


def verify_self_cited_line(
    verified_by: str,
    manifest_raw_path: str,
    wiki_root: Path,
    sources: dict[str, dict[str, str]],
) -> tuple[int, str]:
    m = SELF_LINE_RE.match(verified_by)
    if not m:
        return EXIT_RULE_A, f"self-cited-line regex 불일치: {verified_by}"
    file_rel = m.group("file")
    line_no = int(m.group("line"))

    # H3 (codex review f497ad6 1차): repo-relative 강제 (no abs / no traversal)
    if not _is_repo_relative_path(file_rel, wiki_root):
        return (
            EXIT_RULE_A,
            f"self-cited-line 경로가 repo-relative 아님 (abs/'..'/escape): {file_rel}",
        )

    file_path = wiki_root / file_rel
    if not file_path.is_file():
        return EXIT_RULE_A, f"self-cited-line 파일 부재: {file_rel}"

    try:
        lines = file_path.read_text(encoding="utf-8", errors="replace").splitlines()
    except OSError as e:
        return EXIT_RULE_A, f"read 실패: {e}"

    if not (1 <= line_no <= len(lines)):
        return EXIT_RULE_A, (
            f"line {line_no} out of range [1, {len(lines)}] for {file_rel}"
        )
    cited = lines[line_no - 1]

    # 1. HTML comment marker (가장 명시적)
    # 정책 출처: plan.md §688-§695. raw_path 필수 + 직접 equality.
    html_hits = list(HTML_CITE_MARKER_RE.finditer(cited))
    if html_hits:
        for mh in html_hits:
            sid = mh.group("sid")
            raw = mh.group("raw")
            # codex review f497ad6 1차: HTML marker 의 raw_path 필수 (spec)
            if not raw:
                return (
                    EXIT_MARKER_RESOLVE,
                    f"HTML marker sid={sid} 에 raw_path 누락 — "
                    f"plan §690 의 HTML form 은 source_id+raw_path 모두 명시 필수 (O3)",
                )
            # codex review f497ad6 1차: HTML marker 는 직접 equality 만 (suffix/basename 금지)
            if raw == manifest_raw_path:
                return EXIT_OK, ""
            return (
                EXIT_MARKER_RESOLVE,
                f"HTML marker raw_path={raw} != manifest raw_path={manifest_raw_path} "
                f"(plan §693 의 HTML form 은 직접 equality; O3)",
            )

    # 2. Inline citation: (source_id [§/p./,/space/)] ...)
    #    O3: sid 로 sources.yml lookup → manifest raw_path 와 일치 확인
    inline_match_sid: str | None = None
    for sid in sorted(sources.keys(), key=len, reverse=True):
        pattern = re.compile(r"\(" + re.escape(sid) + r"(?![\w-])")
        if pattern.search(cited):
            inline_match_sid = sid
            break
    if inline_match_sid:
        entry = sources[inline_match_sid]
        yaml_path = entry.get("raw_path") or entry.get("filename") or ""
        if _matches_raw_path(yaml_path, manifest_raw_path):
            return EXIT_OK, ""
        return (
            EXIT_MARKER_RESOLVE,
            f"inline citation sid={inline_match_sid} → sources.yml '{yaml_path}' "
            f"가 manifest raw_path={manifest_raw_path} 와 불일치 (O3)",
        )

    # 3. Source-code reference: <basename>:<LN> or <path>:<LN>
    if manifest_raw_path:
        manifest_base = os.path.basename(manifest_raw_path)
        for ms in SOURCE_CODE_REF_RE.finditer(cited):
            ref_base = ms.group("base")
            ref_path = ms.group("path")
            if ref_base == manifest_base:
                return EXIT_OK, ""
            if ref_path and (
                manifest_raw_path == ref_path
                or manifest_raw_path.endswith(ref_path)
                or ref_path.endswith(manifest_raw_path)
            ):
                return EXIT_OK, ""

    # No marker found
    return (
        EXIT_RULE_A,
        f"line {line_no} 에 explicit citation marker 없음 "
        f"(HTML cite / inline (source_id …) / file:LN 모두 fail; N3 strict)",
    )


# ------------------------------------------------------------------
# Rule A — row-level
# ------------------------------------------------------------------


def check_rule_a(
    row: dict[str, str],
    ctx: dict,
) -> list[tuple[int, str]]:
    """Returns list of (exit_code, message). Empty = pass."""
    fails: list[tuple[int, str]] = []

    target = row["citation_status_target"]
    if target != "verified":
        return fails  # Rule A only for verified rows

    classification = row["classification"]

    # Condition 1: catalog audit
    if classification == "manual-notes-catalog":
        if row["audit_status"] != "audited":
            fails.append(
                (
                    EXIT_RULE_A,
                    f"manual-notes-catalog 인데 audit_status='{row['audit_status']}' "
                    f"(audited 필요)",
                )
            )

    # Condition 2: source_id non-empty + sources.yml 등록 또는 internal-ref prefix
    # H1 (codex review f497ad6 1차): non-empty 만으론 typo (`pugh-sealevel`) 통과
    if not row["source_id"]:
        fails.append((EXIT_RULE_A, "source_id empty"))
    elif not is_registered_source_id(
        row["source_id"], ctx["sources"], ctx["root"]
    ):
        fails.append(
            (
                EXIT_RULE_A,
                f"source_id '{row['source_id']}' 가 textbook/sources.yml 미등록 + "
                f"허용된 internal-ref prefix ({', '.join(INTERNAL_SOURCE_ID_PREFIXES)}) "
                f"가 아니거나 path-like prefix 일 때 root/<sid> 미존재",
            )
        )

    # Condition 3: raw_path non-empty
    if not row["raw_path"]:
        fails.append((EXIT_RULE_A, "raw_path empty"))
    else:
        raw_path_val = row["raw_path"]
        is_url = bool(URL_SCHEME_RE.match(raw_path_val))
        if is_url:
            # Condition 5: external URL → captured_date
            if not row["captured_date"]:
                fails.append(
                    (
                        EXIT_RULE_A,
                        f"external URL raw_path 인데 captured_date empty",
                    )
                )
        else:
            # Condition 4: local file 존재 + sha256
            local = ctx["root"] / raw_path_val
            if not local.exists():
                fails.append(
                    (EXIT_RULE_A, f"raw_path local 파일 부재: {raw_path_val}")
                )
            else:
                # H2 (codex review f497ad6 1차): local raw_path 는 raw_sha256 필수
                if not row["raw_sha256"]:
                    fails.append(
                        (
                            EXIT_RULE_A,
                            f"local raw_path '{raw_path_val}' 인데 raw_sha256 empty "
                            f"(verified row 의 raw artifact hash 미기재)",
                        )
                    )
                else:
                    actual = sha256_of(local)
                    if actual != row["raw_sha256"]:
                        fails.append(
                            (
                                EXIT_RULE_A,
                                f"raw_sha256 mismatch for {raw_path_val}: "
                                f"actual {actual[:16]}… != manifest {row['raw_sha256'][:16]}…",
                            )
                        )

    # source_path 의 sha256_before sanity check (pre-archive 한정)
    if (
        ctx["mode"] == "pre-archive"
        and row["sha256_before"]
        and row["source_path"]
    ):
        src = ctx["root"] / row["source_path"]
        if src.exists():
            actual = sha256_of(src)
            if actual != row["sha256_before"]:
                fails.append(
                    (
                        EXIT_RULE_A,
                        f"source_path {row['source_path']} sha256 {actual[:16]}… "
                        f"!= sha256_before {row['sha256_before'][:16]}…",
                    )
                )

    # Condition 6: claim_mapping_verified_by + semantic validation
    verified_by = row["claim_mapping_verified_by"]
    if not verified_by:
        fails.append((EXIT_RULE_A, "claim_mapping_verified_by empty"))
    else:
        if verified_by.startswith("user-"):
            ec, msg = verify_user_form(verified_by, ctx["today"], ctx["allowlist"])
        elif verified_by.startswith("codex-review-"):
            ec, msg = verify_codex_form(
                verified_by,
                row["codex_evidence_sha256"],
                ctx["codex_archive_dir"],
                ctx["codex_sums_txt"],
            )
        elif verified_by.startswith("self-cited-line-"):
            ec, msg = verify_self_cited_line(
                verified_by, row["raw_path"], ctx["root"], ctx["sources"]
            )
        else:
            ec, msg = (
                EXIT_RULE_A,
                f"claim_mapping_verified_by '{verified_by}' 가 인정된 form 아님",
            )
        if ec != EXIT_OK:
            fails.append((ec, msg))

    return fails


# ------------------------------------------------------------------
# Rule B — dest frontmatter cross-check
# ------------------------------------------------------------------


def extract_citation_status(content: str) -> str | None:
    m = FRONTMATTER_RE.match(content)
    if not m:
        return None
    sm = CITATION_STATUS_RE.search(m.group(1))
    return sm.group(1) if sm else None


def check_rule_b(
    row: dict[str, str],
    ctx: dict,
) -> list[tuple[int, str]]:
    fails: list[tuple[int, str]] = []
    classification = row["classification"]

    if classification == "skip-readme":
        # Pre-archive: validation skip (Rule B 1-4 적용 안 함)
        # Post-archive: archive_path 존재 + sha256 check → post_archive 단계에서 처리
        return fails

    dest = row["dest_path"]
    if not dest:
        fails.append((EXIT_RULE_B, "content row 인데 dest_path empty"))
        return fails

    dest_path = ctx["root"] / dest
    if not dest_path.is_file():
        fails.append((EXIT_RULE_B, f"dest_path 파일 부재: {dest}"))
        return fails

    try:
        content = dest_path.read_text(encoding="utf-8", errors="replace")
    except OSError as e:
        fails.append((EXIT_RULE_B, f"dest_path 읽기 실패: {dest}: {e}"))
        return fails

    fm_status = extract_citation_status(content)
    if fm_status is None:
        fails.append(
            (EXIT_RULE_B, f"dest {dest} frontmatter 의 citation_status 없음")
        )
        return fails

    if fm_status != row["citation_status_target"]:
        fails.append(
            (
                EXIT_RULE_B,
                f"dest {dest} frontmatter citation_status='{fm_status}' "
                f"!= manifest citation_status_target='{row['citation_status_target']}'",
            )
        )

    return fails


# ------------------------------------------------------------------
# Inventory check (J4) — manifest source_path vs filesystem
# ------------------------------------------------------------------


def check_inventory(
    rows: list[dict[str, str]],
    inventory_source: Path,
    root: Path,
) -> list[tuple[int, str]]:
    fails: list[tuple[int, str]] = []
    if not inventory_source.is_dir():
        fails.append(
            (EXIT_INVENTORY, f"inventory source dir 부재: {inventory_source}")
        )
        return fails

    actual: set[str] = set()
    for p in inventory_source.rglob("*"):
        if p.is_file():
            try:
                rel = p.relative_to(root)
            except ValueError:
                rel = p
            actual.add(str(rel))

    expected = {row["source_path"] for row in rows if row["source_path"]}

    missing = sorted(expected - actual)
    extra = sorted(actual - expected)

    if missing:
        fails.append(
            (
                EXIT_INVENTORY,
                f"manifest 가 기대했지만 filesystem 에 없음 ({len(missing)}): "
                + ", ".join(missing[:5])
                + (" …" if len(missing) > 5 else ""),
            )
        )
    if extra:
        fails.append(
            (
                EXIT_INVENTORY,
                f"filesystem 에 있지만 manifest 가 모름 ({len(extra)}): "
                + ", ".join(extra[:5])
                + (" …" if len(extra) > 5 else ""),
            )
        )
    return fails


# ------------------------------------------------------------------
# Post-archive integrity (M2 + N1)
# ------------------------------------------------------------------

STAGING_PREFIX = "_staging/from-modeling-wiki/knowledge"


def archive_path_for(source_path: str, archive_root: Path) -> Path | None:
    """source_path 가 _staging/from-modeling-wiki/knowledge/... 안이면 archive_root
    아래로 매핑. 그 외에는 None — F2-1 (codex review dbc8946 2차): plan §757
    의 `relative_to(...)` 는 staging prefix 밖이면 ValueError 발생, 즉 spec 은
    non-staging source_path 를 reject.
    """
    if source_path.startswith(STAGING_PREFIX + "/"):
        rel = source_path[len(STAGING_PREFIX) + 1 :]
        return archive_root / rel
    return None


def check_post_archive(
    rows: list[dict[str, str]],
    archive_root: Path,
    root: Path,
) -> tuple[list[tuple[int, str]], list[tuple[int, str]]]:
    """Returns (set_eq_fails, sha_fails)."""
    set_fails: list[tuple[int, str]] = []
    sha_fails: list[tuple[int, str]] = []

    abs_archive = archive_root if archive_root.is_absolute() else root / archive_root
    if not abs_archive.is_dir():
        set_fails.append(
            (EXIT_POST_SET, f"archive root 부재: {archive_root}")
        )
        return set_fails, sha_fails

    expected: set[Path] = set()
    for row in rows:
        if not row["source_path"]:
            continue
        ap = archive_path_for(row["source_path"], abs_archive)
        if ap is None:
            # F2-1: staging prefix 밖 source_path 는 spec 위반
            set_fails.append(
                (
                    EXIT_POST_SET,
                    f"source_path '{row['source_path']}' 가 staging prefix "
                    f"({STAGING_PREFIX}) 밖 — plan §757 의 relative_to 위반",
                )
            )
            continue
        expected.add(ap.resolve())

    actual: set[Path] = {p.resolve() for p in abs_archive.rglob("*") if p.is_file()}

    missing = sorted(expected - actual)
    extra = sorted(actual - expected)

    if missing:
        rel_missing = [str(p.relative_to(root) if p.is_relative_to(root) else p) for p in missing[:5]]
        set_fails.append(
            (
                EXIT_POST_SET,
                f"archive 에 누락된 파일 ({len(missing)}): "
                + ", ".join(rel_missing)
                + (" …" if len(missing) > 5 else ""),
            )
        )
    if extra:
        rel_extra = [str(p.relative_to(root) if p.is_relative_to(root) else p) for p in extra[:5]]
        set_fails.append(
            (
                EXIT_POST_SET,
                f"archive 에 잉여 파일 ({len(extra)}): "
                + ", ".join(rel_extra)
                + (" …" if len(extra) > 5 else ""),
            )
        )

    # Per-file sha256
    # codex review f497ad6 1차: plan §780 "모든 50 rows" 강제 — empty sha256_before 도 fail
    for row in rows:
        if not row["source_path"]:
            continue
        if not row["sha256_before"]:
            sha_fails.append(
                (
                    EXIT_POST_SHA,
                    f"row {row['source_path']}: post-archive mode 인데 "
                    f"sha256_before empty (plan §780 의 'all 50 rows' 강제)",
                )
            )
            continue
        ap = archive_path_for(row["source_path"], abs_archive)
        if ap is None or not ap.is_file():
            continue  # already in missing/set_fails
        actual_sha = sha256_of(ap)
        if actual_sha != row["sha256_before"]:
            sha_fails.append(
                (
                    EXIT_POST_SHA,
                    f"archive {ap.name} sha256 {actual_sha[:16]}… != "
                    f"sha256_before {row['sha256_before'][:16]}… "
                    f"(source_path: {row['source_path']})",
                )
            )

    return set_fails, sha_fails


# ------------------------------------------------------------------
# Sanity checks on manifest row shape
# ------------------------------------------------------------------


def check_row_shape(row: dict[str, str], row_num: int) -> list[tuple[int, str]]:
    fails: list[tuple[int, str]] = []
    cls = row["classification"]
    # codex review f497ad6 1차: empty classification 도 fail (schema 강제)
    if not cls and row.get("source_path"):
        fails.append(
            (
                EXIT_RULE_A,
                f"row {row_num}: classification empty (one of "
                f"{sorted(VALID_CLASSIFICATIONS)} 필요)",
            )
        )
    elif cls and cls not in VALID_CLASSIFICATIONS:
        fails.append(
            (
                EXIT_RULE_A,
                f"row {row_num}: classification '{cls}' 가 인정된 값 아님 "
                f"({sorted(VALID_CLASSIFICATIONS)})",
            )
        )
    target = row["citation_status_target"]
    if target and target not in VALID_TARGETS:
        fails.append(
            (
                EXIT_RULE_A,
                f"row {row_num}: citation_status_target '{target}' 가 인정된 값 아님 "
                f"({sorted(VALID_TARGETS)})",
            )
        )
    if cls == "skip-readme" and target != "n/a":
        fails.append(
            (
                EXIT_RULE_A,
                f"row {row_num}: skip-readme 는 citation_status_target='n/a' 이어야 함 "
                f"(현재: '{target}')",
            )
        )
    return fails


# ------------------------------------------------------------------
# main
# ------------------------------------------------------------------


def build_arg_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description="Phase 2a manifest validator (plan.md v8)"
    )
    p.add_argument("--manifest", required=True, help="phase2a manifest CSV 경로")
    p.add_argument(
        "--mode",
        choices=["pre-archive", "post-archive"],
        default="pre-archive",
        help="validation mode (default pre-archive)",
    )
    p.add_argument(
        "--root",
        default=None,
        help="wiki root (default: 스크립트 위치 기준 부모 디렉토리)",
    )
    p.add_argument(
        "--archive-root",
        default="_archive/from-modeling-wiki-knowledge-phase2a-2026-05-23",
        help="post-archive 모드의 archive root (default plan v8 의 명시 경로)",
    )
    p.add_argument(
        "--codex-archive-dir",
        default="_archive/codex-reviews",
        help="codex evidence durable archive dir",
    )
    p.add_argument(
        "--sources-yml",
        default="textbook/sources.yml",
        help="textbook sources manifest",
    )
    p.add_argument(
        "--reviewer-allowlist",
        default="tools/manifests/reviewer-allowlist.txt",
        help="user-form 허용 reviewer 이름 목록",
    )
    p.add_argument(
        "--inventory-source",
        default=None,
        help="manifest source_path 와 set equality 확인할 디렉토리",
    )
    p.add_argument(
        "--today",
        default=None,
        help="ISO YYYY-MM-DD (default today; user-form date range 검증용)",
    )
    return p


def run(args: argparse.Namespace) -> int:
    root = Path(args.root).resolve() if args.root else Path(__file__).resolve().parent.parent
    if not root.is_dir():
        print(f"ERROR: --root {root} 가 디렉토리 아님", file=sys.stderr)
        return EXIT_RULE_A

    manifest_path = Path(args.manifest)
    if not manifest_path.is_absolute():
        manifest_path = (root / manifest_path).resolve()
    if not manifest_path.is_file():
        print(f"ERROR: manifest 부재: {manifest_path}", file=sys.stderr)
        return EXIT_INVENTORY

    rows = load_manifest(manifest_path)

    today = (
        date.fromisoformat(args.today) if args.today else date.today()
    )
    allowlist = load_reviewer_allowlist(root / args.reviewer_allowlist)
    sources = parse_sources_yaml(root / args.sources_yml)
    codex_archive_dir = root / args.codex_archive_dir
    codex_sums_txt = codex_archive_dir / "sha256sums.txt"

    ctx = {
        "root": root,
        "today": today,
        "allowlist": allowlist,
        "sources": sources,
        "codex_archive_dir": codex_archive_dir,
        "codex_sums_txt": codex_sums_txt,
        "mode": args.mode,
    }

    # Per-exit-code buckets
    buckets: dict[int, list[str]] = {
        ec: []
        for ec in (
            EXIT_RULE_A,
            EXIT_RULE_B,
            EXIT_INVENTORY,
            EXIT_POST_SET,
            EXIT_POST_SHA,
            EXIT_CODEX_EVIDENCE,
            EXIT_CODEX_NAMING,
            EXIT_MARKER_RESOLVE,
        )
    }

    def add_fail(ec_msg: tuple[int, str], context: str = "") -> None:
        ec, msg = ec_msg
        prefix = f"{context}: " if context else ""
        buckets[ec].append(f"{prefix}{msg}")

    # Per-row checks
    for i, row in enumerate(rows, start=2):  # CSV header is row 1
        ctx_label = f"row {i} [{row.get('source_path') or '?'}]"
        for f in check_row_shape(row, i):
            add_fail(f, ctx_label)
        for f in check_rule_a(row, ctx):
            add_fail(f, ctx_label)
        for f in check_rule_b(row, ctx):
            add_fail(f, ctx_label)

    # Inventory check (optional)
    if args.inventory_source:
        inv = Path(args.inventory_source)
        if not inv.is_absolute():
            inv = root / inv
        for f in check_inventory(rows, inv, root):
            add_fail(f)

    # Post-archive checks
    if args.mode == "post-archive":
        archive_root = Path(args.archive_root)
        set_fails, sha_fails = check_post_archive(rows, archive_root, root)
        for f in set_fails:
            add_fail(f)
        for f in sha_fails:
            add_fail(f)

    # Report
    print(f"[validate-phase2a-manifest] mode={args.mode} root={root}")
    print(f"  rows: {len(rows)}, sources.yml entries: {len(sources)}, "
          f"reviewer-allowlist: {len(allowlist)}")
    total_fail = 0
    for ec, msgs in buckets.items():
        if not msgs:
            continue
        total_fail += len(msgs)
        label = {
            EXIT_RULE_A: "Rule A",
            EXIT_RULE_B: "Rule B",
            EXIT_INVENTORY: "Inventory (4)",
            EXIT_POST_SET: "Post-archive set equality (5)",
            EXIT_POST_SHA: "Post-archive sha256 (6)",
            EXIT_CODEX_EVIDENCE: "Codex evidence (7)",
            EXIT_CODEX_NAMING: "Codex naming (8)",
            EXIT_MARKER_RESOLVE: "Marker raw_path (9)",
        }[ec]
        print(f"  FAIL [{label}] ({len(msgs)}):")
        for m in msgs[:20]:
            print(f"    - {m}")
        if len(msgs) > 20:
            print(f"    … (+{len(msgs) - 20} more)")

    # Determine exit code (specific first)
    for ec in PRIORITY:
        if buckets[ec]:
            print(f"RESULT: FAIL exit={ec}")
            return ec
    a_fail = bool(buckets[EXIT_RULE_A])
    b_fail = bool(buckets[EXIT_RULE_B])
    if a_fail and b_fail:
        print(f"RESULT: FAIL exit={EXIT_RULE_AB}")
        return EXIT_RULE_AB
    if a_fail:
        print(f"RESULT: FAIL exit={EXIT_RULE_A}")
        return EXIT_RULE_A
    if b_fail:
        print(f"RESULT: FAIL exit={EXIT_RULE_B}")
        return EXIT_RULE_B
    print("RESULT: OK")
    return EXIT_OK


def main(argv: list[str] | None = None) -> int:
    args = build_arg_parser().parse_args(argv)
    return run(args)


if __name__ == "__main__":
    sys.exit(main())
