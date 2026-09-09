#!/usr/bin/env python3
"""Read-only integrity gate for the frozen XBeach closure packet.

This program checks identity, hashes, quoted spans, denominator sets, and
canonical anchor reachability.  It deliberately does not re-adjudicate any
technical conclusion.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable


ROOT = Path(__file__).resolve().parents[5]
HERE = Path(__file__).resolve().parent
XBEACH_AUDIT = HERE.parent
RAW_SOURCE = ROOT / "models/XBeach/raw/source_code"

BASELINE = HERE / "immutable-baseline.json"
ATTRIBUTION = HERE / "attribution.json"
DEFERRED = HERE / "deferred-inputs.json"
HARD = HERE / "hard-resolutions/hard-resolutions.json"
LOCAL = HERE / "local-refutations/resolution-ledger.json"
MANUAL = HERE / "manual-code-adjudications.json"
DEFERRED_MAPPING = HERE / "deferred-canonical-mapping.json"
BUILD_MAPPING = HERE / "build-canonical-mapping.json"
SOURCE_EVIDENCE = HERE / "source-canonical/evidence-ledger.json"
SOURCE_MAPPING = HERE / "source-canonical/mapping-ledger.json"
SUPPLEMENT_MANIFEST = XBEACH_AUDIT / "XBeach-supplement-manifest.json"
SUPPLEMENT_DECISIONS = XBEACH_AUDIT / "XBeach-supplement-decisions.json"
INVENTORY = XBEACH_AUDIT / "xb-inventory.json"
DOC_DIR = HERE / "document-inventory"
DOC_EXACT = DOC_DIR / "exact-207.jsonl"
DOC_EXACT_MANIFEST = DOC_DIR / "exact-207-manifest.json"
DOC_DISPOSITIONS = DOC_DIR / "all-207-disposition.jsonl"
DOC_SUMMARY = DOC_DIR / "disposition-summary.json"
DOC_MAPPING = DOC_DIR / "document-canonical-mapping.json"
INSTALL_MANIFEST = HERE / "canonical-install.json"

SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
EXPLICIT_ANCHOR_PATTERNS = (
    '<a id="{anchor}"',
    "<a id='{anchor}'",
    '<a name="{anchor}"',
    "<a name='{anchor}'",
    "{{#{anchor}}}",
)


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def file_sha(path: Path) -> str:
    require(path.is_file(), f"missing file: {path.relative_to(ROOT)}")
    return sha256_bytes(path.read_bytes())


def load_json(path: Path) -> Any:
    require(path.is_file(), f"missing JSON: {path.relative_to(ROOT)}")
    return json.loads(path.read_bytes())


def load_jsonl(path: Path) -> list[dict[str, Any]]:
    require(path.is_file(), f"missing JSONL: {path.relative_to(ROOT)}")
    rows: list[dict[str, Any]] = []
    for number, raw in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if raw.strip():
            value = json.loads(raw)
            require(isinstance(value, dict), f"{path.name}:{number}: row is not an object")
            rows.append(value)
    return rows


def repo_path(value: str) -> Path:
    path = Path(value)
    require(not path.is_absolute() and ".." not in path.parts, f"unsafe repo path: {value}")
    resolved = (ROOT / path).resolve()
    require(resolved.is_relative_to(ROOT.resolve()), f"path escapes repository: {value}")
    return resolved


def assert_hash(path: Path, expected: str, label: str) -> bytes:
    require(isinstance(expected, str) and SHA256_RE.fullmatch(expected) is not None,
            f"{label}: invalid SHA-256: {expected!r}")
    require(path.is_file(), f"{label}: missing file: {path.relative_to(ROOT)}")
    data = path.read_bytes()
    actual = sha256_bytes(data)
    require(actual == expected, f"{label}: SHA drift: expected {expected}, got {actual}")
    return data


def unique_values(values: Iterable[str], label: str) -> set[str]:
    items = list(values)
    require(all(isinstance(item, str) and item for item in items), f"{label}: empty/non-string key")
    duplicates = [item for item, count in Counter(items).items() if count != 1]
    require(not duplicates, f"{label}: duplicate keys: {duplicates[:5]}")
    return set(items)


def physical_span(data: bytes, start: int, end: int, label: str) -> bytes:
    require(isinstance(start, int) and isinstance(end, int) and 1 <= start <= end,
            f"{label}: invalid span {start}-{end}")
    lines = data.split(b"\n")
    require(end <= len(lines), f"{label}: span ends after physical line count {len(lines)}")
    return b"\n".join(lines[start - 1:end])


def normalized_lf_span(data: bytes, start: int, end: int, label: str) -> bytes:
    raw = physical_span(data, start, end, label)
    return b"\n".join(line[:-1] if line.endswith(b"\r") else line for line in raw.split(b"\n"))


def parse_line_range(value: str, label: str) -> tuple[int, int]:
    match = re.fullmatch(r"(\d+)(?:-(\d+))?", value)
    require(match is not None, f"{label}: invalid line range: {value!r}")
    start = int(match.group(1))
    end = int(match.group(2) or start)
    require(1 <= start <= end, f"{label}: invalid line range: {value!r}")
    return start, end


def check_raw_quote(entry: dict[str, Any], label: str) -> None:
    path = repo_path(entry["path"])
    data = assert_hash(path, entry["sha256"], label)
    span = physical_span(data, entry["line_start"], entry["line_end"], label)
    try:
        actual = span.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise AssertionError(f"{label}: selected span is not UTF-8") from exc
    require(actual == entry["quote_exact_utf8"], f"{label}: raw LF span quote mismatch")


def check_normalized_quote(entry: dict[str, Any], label: str) -> None:
    path = repo_path(entry["path"])
    data = assert_hash(path, entry["sha256"], label)
    start, end = parse_line_range(entry["lines"], label)
    try:
        actual = normalized_lf_span(data, start, end, label).decode("utf-8")
    except UnicodeDecodeError as exc:
        raise AssertionError(f"{label}: selected span is not UTF-8") from exc
    require(actual == entry["quote"], f"{label}: normalized-LF quote mismatch")


def github_slug(heading: str) -> str:
    text = re.sub(r"<[^>]+>", "", heading.strip().lower())
    text = re.sub(r"[^\w\- ]", "", text, flags=re.UNICODE)
    return re.sub(r"[ -]+", "-", text).strip("-")


def anchor_exists(path: Path, anchor: str) -> bool:
    text = path.read_text(encoding="utf-8")
    if any(pattern.format(anchor=anchor) in text for pattern in EXPLICIT_ANCHOR_PATTERNS):
        return True
    seen: Counter[str] = Counter()
    for line in text.splitlines():
        match = re.match(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", line)
        if not match:
            continue
        base = github_slug(match.group(1))
        number = seen[base]
        seen[base] += 1
        slug = base if number == 0 else f"{base}-{number}"
        if slug == anchor:
            return True
    return False


def check_anchor(value: str, canonical_root: Path, label: str) -> None:
    require(isinstance(value, str) and value.count("#") == 1, f"{label}: malformed anchor: {value!r}")
    relative, anchor = value.split("#", 1)
    require(relative and anchor, f"{label}: incomplete anchor: {value!r}")
    rel = Path(relative)
    require(not rel.is_absolute() and ".." not in rel.parts, f"{label}: unsafe canonical path")
    path = (canonical_root / rel).resolve()
    require(path.is_relative_to(canonical_root.resolve()), f"{label}: canonical path escapes root")
    require(path.is_file(), f"{label}: missing canonical file: {relative}")
    require(anchor_exists(path, anchor), f"{label}: missing anchor #{anchor} in {relative}")


def validate_baseline() -> int:
    data = load_json(BASELINE)
    files = data.get("files")
    require(isinstance(files, dict) and len(files) == 292, "immutable baseline must contain exactly 292 files")
    for rel, expected in files.items():
        assert_hash(repo_path(rel), expected, f"baseline:{rel}")
    print("PASS baseline files=292")
    return len(files)


def validate_attribution() -> tuple[int, int]:
    data = load_json(ATTRIBUTION)
    files = data.get("files")
    dispositions = data.get("dispositions")
    require(data.get("file_count") == 456 and isinstance(files, list) and len(files) == 456,
            "attribution file denominator must be 456")
    require(data.get("disposition_count") == 1472 and isinstance(dispositions, list) and len(dispositions) == 1472,
            "attribution disposition denominator must be 1472")

    file_paths = unique_values((row["path"] for row in files), "attribution files")
    file_by_path = {row["path"]: row for row in files}
    for rel, row in file_by_path.items():
        require(row.get("class_evidence", {}).get("path") == rel,
                f"attribution:{rel}: class-evidence path mismatch")
        require(row.get("class_evidence", {}).get("source_sha256") == row["source_sha256"],
                f"attribution:{rel}: class-evidence hash mismatch")
        assert_hash(RAW_SOURCE / rel, row["source_sha256"], f"attribution source:{rel}")

    inventory = load_json(INVENTORY)
    require(isinstance(inventory, list) and len(inventory) == 456, "inventory denominator must be 456")
    require(file_sha(INVENTORY) == data.get("inventory_sha256"), "attribution inventory SHA mismatch")
    inventory_paths = unique_values((row["path"] for row in inventory), "inventory files")
    require(inventory_paths == file_paths, "attribution and inventory path sets differ")
    for row in inventory:
        require(file_by_path[row["path"]]["source_sha256"] == row["sha256"],
                f"inventory/attribution hash mismatch: {row['path']}")

    disposition_ids = unique_values((row["id"] for row in dispositions), "attribution dispositions")
    crosswalk_cache: dict[str, dict[str, Any]] = {}
    rebuilt_ids: set[str] = set()
    for row in dispositions:
        rel = row["crosswalk_path"]
        path = repo_path(rel)
        if rel not in crosswalk_cache:
            assert_hash(path, row["crosswalk_sha256"], f"crosswalk:{rel}")
            crosswalk_cache[rel] = load_json(path)
        cw = crosswalk_cache[rel]
        require(file_sha(path) == row["crosswalk_sha256"], f"crosswalk hash link mismatch: {rel}")
        index = row["disposition_index"]
        require(isinstance(index, int) and 0 <= index < len(cw["dispositions"]),
                f"{row['id']}: disposition index out of range")
        expected_id = f"{cw['shard']}:{cw['source_path']}:{index}"
        require(row["id"] == expected_id, f"attribution ID mismatch: {row['id']} != {expected_id}")
        require(row["source_path"] == cw["source_path"], f"{row['id']}: source path link mismatch")
        require(row["source_sha256"] == cw["source_sha256"], f"{row['id']}: source hash link mismatch")
        require(row["source_sha256"] == file_by_path[row["source_path"]]["source_sha256"],
                f"{row['id']}: attribution file hash link mismatch")
        disposition = cw["dispositions"][index]
        require(row["base_ids"] == disposition["base_ids"], f"{row['id']}: base_ids mismatch")
        require(row["audit_ids"] == disposition["audit_ids"], f"{row['id']}: audit_ids mismatch")
        require(row["historical_disposition"] == disposition["disposition"],
                f"{row['id']}: historical disposition mismatch")
        adversarial = disposition.get("adversarial")
        expected_verdict = adversarial.get("verdict") if isinstance(adversarial, dict) else None
        require(row["historical_adversarial_verdict"] == expected_verdict,
                f"{row['id']}: adversarial verdict mismatch")

    for rel, cw in crosswalk_cache.items():
        for index in range(len(cw["dispositions"])):
            rebuilt_ids.add(f"{cw['shard']}:{cw['source_path']}:{index}")
    require(rebuilt_ids == disposition_ids,
            f"attribution/crosswalk disposition sets differ: attribution={len(disposition_ids)}, rebuilt={len(rebuilt_ids)}")
    print("PASS attribution files=456 dispositions=1472 source-hash-links=1472")
    return len(files), len(dispositions)


def validate_deferred(canonical_root: Path) -> int:
    deferred = load_json(DEFERRED)
    require(deferred.get("count") == 13 and len(deferred.get("items", [])) == 13,
            "deferred denominator must be 13")
    deferred_items = deferred["items"]
    deferred_ids = unique_values((row["id"] for row in deferred_items), "deferred inputs")
    deferred_by_id = {row["id"]: row for row in deferred_items}

    hard = load_json(HARD)
    hard_items = hard.get("items", [])
    require(len(hard_items) == 5, "hard resolution denominator must be 5")
    hard_ids = unique_values((row["deferred_input_id"] for row in hard_items), "hard resolutions")
    for item in hard_items:
        did = item["deferred_input_id"]
        require(did in deferred_by_id, f"hard resolution has unknown deferred ID: {did}")
        original = deferred_by_id[did]
        require(item["original_crosswalk_path"] == original["crosswalk_path"], f"{did}: hard crosswalk path mismatch")
        require(item["original_crosswalk_sha256"] == original["crosswalk_sha256"], f"{did}: hard crosswalk hash mismatch")
        require(item["disposition_index_zero_based"] == original["index"], f"{did}: hard disposition index mismatch")
        require(item["source_sha256"] == original["source_sha256"], f"{did}: hard source hash mismatch")
        require(file_sha(repo_path(item["deferred_input_path"])) == item["deferred_input_sha256"],
                f"{did}: hard deferred-input hash mismatch")
        for number, evidence in enumerate(item.get("evidence", []), 1):
            check_raw_quote(evidence, f"hard:{item['id']}:evidence-{number}")
        for artifact in item.get("experiment_artifacts", []):
            assert_hash(repo_path(artifact["path"]), artifact["sha256"], f"hard:{item['id']}:artifact")

    local = load_json(LOCAL)
    local_items = local.get("items", [])
    require(len(local_items) == 8, "local resolution denominator must be 8")
    local_ids = unique_values((row["id"] for row in local_items), "local resolutions")
    for item in local_items:
        did = item["id"]
        require(did in deferred_by_id, f"local resolution has unknown deferred ID: {did}")
        original = deferred_by_id[did]
        require(item["crosswalk"]["path"] == original["crosswalk_path"], f"{did}: local crosswalk path mismatch")
        require(item["crosswalk"]["sha256"] == original["crosswalk_sha256"], f"{did}: local crosswalk hash mismatch")
        require(item["crosswalk"]["disposition_index"] == original["index"], f"{did}: local disposition index mismatch")
        require(item["source"]["sha256"] == original["source_sha256"], f"{did}: local source hash mismatch")
        require(file_sha(repo_path(item["crosswalk"]["path"])) == item["crosswalk"]["sha256"],
                f"{did}: local crosswalk file hash mismatch")
        require(file_sha(repo_path(item["source"]["path"])) == item["source"]["sha256"],
                f"{did}: local source file hash mismatch")
        for number, evidence in enumerate(item.get("evidence", []), 1):
            check_normalized_quote(evidence, f"local:{did}:evidence-{number}")

    require(hard_ids.isdisjoint(local_ids), "hard and local deferred ID sets overlap")
    require(hard_ids | local_ids == deferred_ids,
            f"hard/local sets do not close frozen deferred set: hard={len(hard_ids)} local={len(local_ids)} frozen={len(deferred_ids)}")

    mapping = load_json(DEFERRED_MAPPING)
    mappings = mapping.get("mappings")
    require(mapping.get("count") == 13 and isinstance(mappings, list) and len(mappings) == 13,
            "deferred canonical mapping denominator must be 13")
    mapped_ids = unique_values((row["id"] for row in mappings), "deferred canonical mappings")
    require(mapped_ids == deferred_ids, "deferred canonical mapping ID set differs from frozen 13")
    for row in mappings:
        check_anchor(row["canonical_anchor"], canonical_root, f"deferred mapping:{row['id']}")
    print("PASS deferred frozen=13 hard=5 local=8 mapped=13")
    return len(deferred_ids)


def validate_manual_quotes() -> int:
    data = load_json(MANUAL)
    items = data.get("items", [])
    require(len(items) == 8, "manual-code adjudication topic denominator must be 8")
    exact = {r["finding_id"]: r["finding"] for r in load_jsonl(DOC_EXACT)}
    topic_patterns = {"wci": r"wci", "nuh": r"nuh", "bedfriction": r"chezy|friction",
                      "dilatancy": r"dilatancy", "adaptation-time": r"adaptation-time",
                      "posdwn": r"posdwn", "dthetaS_XB": r"dthetaS_XB|angular reference axis",
                      "secorder": r"sec_?order"}
    quote_count = 0
    for item in items:
        require(item.get("finding_ids"), f"manual-code:{item.get('topic')}: missing finding IDs")
        bindings = item.get("finding_bindings", [])
        require({r["finding_id"] for r in bindings} == set(item["finding_ids"]), "manual binding ID set")
        for binding in bindings:
            finding = exact[binding["finding_id"]]
            require(binding["finding_exact"] == finding, "manual binding frozen finding text")
            require(binding["finding_sha256"] == hashlib.sha256(finding.encode()).hexdigest(), "manual finding hash")
            require(re.search(topic_patterns[item["topic"]], finding, re.I), "unrelated manual topic/ID")
        for number, evidence in enumerate(item.get("evidence", []), 1):
            check_raw_quote(evidence, f"manual-code:{item['topic']}:evidence-{number}")
            quote_count += 1
    print(f"PASS manual-code topics=8 raw-quotes={quote_count}")
    return quote_count


def supplement_manifest_keys() -> set[str]:
    data = load_json(SUPPLEMENT_MANIFEST)
    require(data.get("entry_count") == 43 and len(data.get("entries", [])) == 43,
            "supplement manifest entry denominator must be 43")
    keys: list[str] = []
    supplements = 0
    for entry in data["entries"]:
        source_sha = entry["canonical_key"]["source_sha256"]
        for supplement in entry.get("supplements", []):
            supplements += 1
            member_ids = supplement.get("member_input_ids")
            require(isinstance(member_ids, list) and member_ids,
                    f"manifest:{source_sha}: supplement has no member_input_ids")
            keys.extend(f"{source_sha}:{audit_id}" for audit_id in member_ids)
    require(supplements == data.get("supplement_count") == 103,
            f"supplement manifest denominator must be 103, got {supplements}")
    return unique_values(keys, "supplement manifest stable keys")


def manifest_supplement_by_key() -> dict[str, dict[str, Any]]:
    data = load_json(SUPPLEMENT_MANIFEST)
    result: dict[str, dict[str, Any]] = {}
    for entry in data["entries"]:
        source_sha = entry["canonical_key"]["source_sha256"]
        for supplement in entry["supplements"]:
            for audit_id in supplement["member_input_ids"]:
                key = f"{source_sha}:{audit_id}"
                require(key not in result, f"duplicate manifest stable key: {key}")
                result[key] = supplement
    return result


def validate_source_evidence() -> tuple[int, set[str]]:
    ledger = load_json(SOURCE_EVIDENCE)
    entries = ledger.get("entries", [])
    require(ledger.get("entry_count") == 60 and len(entries) == 60,
            "source evidence denominator must be 60")
    keys = unique_values((row["stable_key"] for row in entries), "source evidence stable keys")
    manifest_by_key = manifest_supplement_by_key()
    require(keys <= set(manifest_by_key), "source evidence contains a stable key absent from manifest")

    immutable = ledger.get("immutable_input_sha256", {})
    manifest_rel = str(SUPPLEMENT_MANIFEST.relative_to(ROOT))
    decisions_rel = str(SUPPLEMENT_DECISIONS.relative_to(ROOT))
    require(immutable.get(manifest_rel) == file_sha(SUPPLEMENT_MANIFEST),
            "source evidence manifest SHA link mismatch")
    require(immutable.get(decisions_rel) == file_sha(SUPPLEMENT_DECISIONS),
            "source evidence decision SHA link mismatch")

    neutralizer_count = 0
    for row in entries:
        key = row["stable_key"]
        require(key == f"{row['source_sha256']}:{row['audit_id']}", f"source evidence malformed stable key: {key}")
        require(row["human_decision"].get("status") == "approved", f"source evidence decision is not approved: {key}")
        source = row["source"]
        path = repo_path(source["repo_relative_path"])
        data = assert_hash(path, source["byte_sha256"], f"source evidence:{key}")
        require(source["byte_sha256"] == row["source_sha256"], f"source evidence source hash link mismatch: {key}")
        evidence = row["physical_lf_evidence"]
        raw_span = physical_span(data, evidence["line_start"], evidence["line_end"], f"source evidence:{key}")
        require(sha256_bytes(raw_span) == evidence["raw_span_sha256"], f"source evidence raw-span SHA mismatch: {key}")
        normalized = normalized_lf_span(data, evidence["line_start"], evidence["line_end"], f"source evidence:{key}")
        require(sha256_bytes(normalized) == evidence["lf_normalized_quote_sha256"],
                f"source evidence normalized quote SHA mismatch: {key}")
        require(normalized.decode("utf-8") == evidence["lf_normalized_quote"],
                f"source evidence normalized quote mismatch: {key}")

        manifest = manifest_by_key[key]
        require(evidence["lf_normalized_quote"] == manifest["authoritative_quote"],
                f"source evidence/manifest quote mismatch: {key}")
        require(evidence["lf_normalized_quote_sha256"] == manifest["source_span_hash"],
                f"source evidence/manifest span hash mismatch: {key}")
        expected_lines = parse_line_range(manifest["source_span"]["lines"], f"manifest:{key}")
        require(expected_lines == (evidence["line_start"], evidence["line_end"]),
                f"source evidence/manifest line span mismatch: {key}")

        crosswalk = row["crosswalk"]
        assert_hash(repo_path(crosswalk["path"]), crosswalk["byte_sha256"], f"source crosswalk:{key}")
        scope = crosswalk.get("neutralizer_or_scope_evidence")
        if scope:
            neutralizer_count += 1
            scope_path = repo_path(scope["where"].split(":L", 1)[0].split(":", 1)[0])
            scope_data = assert_hash(scope_path, scope["source_byte_sha256"], f"source scope:{key}")
            scope_raw = physical_span(scope_data, scope["line_start"], scope["line_end"], f"source scope:{key}")
            require(sha256_bytes(scope_raw) == scope["raw_span_sha256"], f"source scope raw-span SHA mismatch: {key}")
            scope_normalized = normalized_lf_span(scope_data, scope["line_start"], scope["line_end"], f"source scope:{key}")
            require(scope_normalized.decode("utf-8") == scope["lf_normalized_quote"],
                    f"source scope quote mismatch: {key}")
            require(sha256_bytes(scope_normalized) == scope["lf_normalized_quote_sha256"],
                    f"source scope quote SHA mismatch: {key}")
    print(f"PASS source evidence=60 exact-quotes=60 scope-quotes={neutralizer_count}")
    return len(entries), keys


def validate_supplement_mappings(canonical_root: Path, source_evidence_keys: set[str]) -> int:
    manifest_keys = supplement_manifest_keys()
    build = load_json(BUILD_MAPPING)
    source = load_json(SOURCE_MAPPING)
    build_rows = build.get("mappings", [])
    source_rows = source.get("mappings", [])
    require(build.get("count") == 43 and len(build_rows) == 43, "build canonical mapping denominator must be 43")
    require(source.get("entry_count") == 60 and len(source_rows) == 60,
            "source canonical mapping denominator must be 60")
    build_keys = unique_values((row["stable_key"] for row in build_rows), "build mapping stable keys")
    source_keys = unique_values((row["stable_key"] for row in source_rows), "source mapping stable keys")
    require(source_keys == source_evidence_keys, "source mapping and evidence stable-key sets differ")
    require(build_keys.isdisjoint(source_keys), "build/source mapping stable-key sets overlap")
    require(build_keys | source_keys == manifest_keys,
            f"combined canonical mapping set differs from 103 manifest keys: combined={len(build_keys | source_keys)} manifest={len(manifest_keys)}")
    for kind, rows in (("build", build_rows), ("source", source_rows)):
        for row in rows:
            require(row["stable_key"] == f"{row['source_sha256']}:{row['audit_id']}",
                    f"{kind} mapping malformed stable key: {row['stable_key']}")
            check_anchor(row["canonical_anchor"], canonical_root, f"{kind} mapping:{row['stable_key']}")
    print("PASS supplements manifest=103 build-mapped=43 source-mapped=60 anchors=103")
    return len(manifest_keys)


FROZEN_DOC_FIELDS = (
    "finding_id", "class", "finding", "original_path", "original_sha256",
    "reported_lines", "representation_kind", "representation_lines_read",
    "representation_path", "representation_sha256", "severity", "work_id",
    "x00_artifact", "x00_record_index0", "x00_record_index1", "x00_sha256",
    "x00_unresolved_index0", "x00_unresolved_index1",
)


def validate_documents(canonical_root: Path) -> int:
    manifest = load_json(DOC_EXACT_MANIFEST)
    require(manifest.get("frozen_high_count") == 207, "document frozen denominator must be 207")
    require(file_sha(repo_path(manifest["exact_207_path"])) == manifest["exact_207_sha256"],
            "exact-207 manifest file SHA mismatch")
    require(file_sha(repo_path(manifest["x00_path"])) == manifest["x00_sha256"],
            "exact-207 manifest X00 SHA mismatch")

    exact = load_jsonl(DOC_EXACT)
    dispositions = load_jsonl(DOC_DISPOSITIONS)
    require(len(exact) == len(dispositions) == 207, "document exact/disposition denominators must both be 207")
    expected_ids = {f"XH{number:03d}" for number in range(1, 208)}
    exact_ids = unique_values((row["finding_id"] for row in exact), "exact-207 finding IDs")
    disposition_ids = unique_values((row["finding_id"] for row in dispositions), "document disposition IDs")
    require(exact_ids == expected_ids, "exact-207 finding ID set is not XH001..XH207")
    require(disposition_ids == exact_ids, "document disposition ID set differs from exact-207")
    exact_by_id = {row["finding_id"]: row for row in exact}
    expected_topics = {}
    for item in load_json(MANUAL)["items"]:
        for fid in item["finding_ids"]:
            expected_topics.setdefault(fid, set()).add(item["topic"])
    for row in dispositions:
        actual_topics = [a["topic"] for a in row.get("source_code_adjudications", [])]
        require(len(actual_topics) == len(set(actual_topics)), "duplicate document topic")
        require(set(actual_topics) == expected_topics.get(row["finding_id"], set()), "lost/unrelated compound adjudication")
        frozen = exact_by_id[row["finding_id"]]
        for field in FROZEN_DOC_FIELDS:
            require(row.get(field) == frozen.get(field),
                    f"document disposition changed frozen field {field}: {row['finding_id']}")

    with (DOC_DIR / "all-207-disposition.csv").open(newline="") as handle:
        csv_rows = {r["finding_id"]: r for r in csv.DictReader(handle)}
    require(set(csv_rows) == exact_ids, "CSV document ID set")
    for row in dispositions:
        encoded = csv_rows[row["finding_id"]]["source_code_adjudications_json"]
        require(json.loads(encoded or "[]") == row.get("source_code_adjudications", []), "CSV lost compound evidence")

    summary = load_json(DOC_SUMMARY)
    require(summary.get("count") == 207, "document disposition summary count must be 207")
    require(summary.get("input_exact_207_sha256") == file_sha(DOC_EXACT),
            "document summary exact-207 SHA mismatch")
    require(summary.get("output_jsonl_sha256") == file_sha(DOC_DISPOSITIONS),
            "document summary disposition SHA mismatch")

    require(DOC_MAPPING.is_file(),
            f"missing document canonical mapping ledger: {DOC_MAPPING.relative_to(ROOT)}")
    mapping = load_json(DOC_MAPPING)
    require(mapping.get("schema") == "xbeach-document-canonical-mapping/v1",
            "document canonical mapping schema mismatch")
    entries = mapping.get("entries")
    require(isinstance(entries, list) and len(entries) == 207,
            "document canonical mapping denominator must be 207")
    mapping_ids = unique_values((row["finding_id"] for row in entries), "document canonical mapping IDs")
    require(mapping_ids == exact_ids, "document canonical mapping ID set differs from exact-207")
    for row in entries:
        anchor = row.get("canonical_anchor")
        require(row.get("canonical_file") == anchor.split("#", 1)[0] if isinstance(anchor, str) else False,
                f"document mapping canonical_file/anchor mismatch: {row['finding_id']}")
        require(row.get("review_group_id"), f"document mapping missing review_group_id: {row['finding_id']}")
        require(row.get("disposition"), f"document mapping missing disposition: {row['finding_id']}")
        require(row.get("source_locator"), f"document mapping missing source_locator: {row['finding_id']}")
        check_anchor(anchor, canonical_root, f"document mapping:{row['finding_id']}")
        locator = row["source_locator"]
        assert_hash(repo_path(locator["original_path"]), locator["original_sha256"], "document original")
        extract = XBEACH_AUDIT / "bindoc-converted" / locator["representation_path"]
        assert_hash(extract, locator["representation_sha256"], "document extract")
        body = extract.read_text(encoding="utf-8", errors="replace").splitlines()
        selected = []
        for part in locator["reported_lines"].split(","):
            nums = [int(x) for x in part.split("-")]
            a, b = nums[0], nums[-1]
            require(1 <= a <= b <= len(body), "document span bounds")
            selected.extend(f"{n}:" + re.sub(r"\s+", " ", body[n-1]).strip() for n in range(a,b+1))
        actual = hashlib.sha256("\n".join(selected).encode()).hexdigest()
        require(actual == locator["reported_span_sha256"], "document reported span hash")
        for quote in locator["reported_span_direct_quotes"]:
            original = re.sub(r"\s+", " ", body[quote["line"]-1]).strip()
            require(quote["quote"].removesuffix(" …") in original, "document direct quotation")
        if locator["page_map_status"] in {"cross-format-partial", "cross-format-retrieval-candidate"}:
            require(not locator.get("physical_pdf_pages"), "weak alignment falsely promoted to PDF page")

    print("PASS documents frozen=207 dispositions=207 mapped=207 anchors=207")
    return len(exact_ids)


def validate_install_manifest() -> int:
    require(INSTALL_MANIFEST.is_file(), f"--installed requires {INSTALL_MANIFEST.relative_to(ROOT)}")
    data = load_json(INSTALL_MANIFEST)
    files = data.get("files")
    require(isinstance(files, list) and files, "canonical install manifest has no files")
    targets = unique_values((row["target"] for row in files), "install targets")
    staged = unique_values((row["staged"] for row in files), "install staged paths")
    staged_files = {
        str(path.relative_to(ROOT))
        for path in (HERE / "canonical").rglob("*")
        if path.is_file()
    }
    require(staged == staged_files,
            f"install manifest staged-file set differs from closure/canonical: manifest={len(staged)} staged={len(staged_files)}")
    for row in files:
        staged_path = repo_path(row["staged"])
        target_path = repo_path(row["target"])
        after = row["after_sha256"]
        assert_hash(staged_path, after, f"install staged:{row['target']}")
        assert_hash(target_path, after, f"install target:{row['target']}")
        require(str(staged_path.relative_to(HERE / "canonical")) == row["target"],
                f"install target/staged relative path mismatch: {row['target']}")
    immutable = data.get("immutable_baseline")
    require(isinstance(immutable, dict), "install manifest missing immutable_baseline")
    baseline_files = load_json(BASELINE)["files"]
    require(immutable == baseline_files, "install manifest immutable baseline differs from frozen baseline")
    for rel, expected in immutable.items():
        assert_hash(repo_path(rel), expected, f"install immutable:{rel}")
    print(f"PASS installed targets={len(targets)} staged-after-sha={len(files)} installed-after-sha={len(files)}")
    return len(files)


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--installed",
        action="store_true",
        help="validate anchors in installed canonical files and verify canonical-install.json after_sha256 values",
    )
    args = parser.parse_args()

    canonical_root = ROOT if args.installed else HERE / "canonical"
    validate_baseline()
    validate_attribution()
    validate_deferred(canonical_root)
    validate_manual_quotes()
    source_count, source_keys = validate_source_evidence()
    supplement_count = validate_supplement_mappings(canonical_root, source_keys)
    document_count = validate_documents(canonical_root)
    installed_count = validate_install_manifest() if args.installed else 0
    print(
        "PASS closure integrity "
        f"source-evidence={source_count} supplements={supplement_count} "
        f"documents={document_count} installed-files={installed_count}"
    )


if __name__ == "__main__":
    main()
