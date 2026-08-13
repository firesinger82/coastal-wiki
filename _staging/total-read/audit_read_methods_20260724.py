#!/usr/bin/env python3
"""Read-only provenance triage for total-read JSONL records.

This script never rewrites records.  It classifies evidence about *how a record
was produced*, not whether the record's factual fields are correct.  In
particular, ``vendor_llm_labeled`` means only that the existing ``reader`` field
names an LLM vendor; it is not proof that an LLM read and understood the file.

Confirmed-script patterns below are grounded in preserved emitters under
``helpers/`` or, for the three 2026-07-24 final files, their explicit
``read_method`` field.  Suspect patterns are kept separate because their
generators are not present even though the records have a uniform structural
index fingerprint.
"""

from __future__ import annotations

import argparse
import collections
import fnmatch
import json
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
RECORDS = Path(__file__).resolve().parent / "records"

FINAL_STRUCT_INDEX_FILES = {
    "rest-efdc-final-20260724.jsonl",
    "all-FUNWAVE-final-20260724.jsonl",
    "all-LISFLOOD-FP-final-20260724.jsonl",
}

# Preserved helper -> output evidence:
# - emit_all_cadmas_codex_20260722_39shards.py:533
# - emit_sfincs_codex_20260721_totalread_7d3c.py:697,705
# - emit_rest_xbeach_codex_20260721.py:822-828
# - rest_efdc_codex_totalread_20260721.py:694-701
# - emit_swash_codex_20260720_091500_7f3a.py:335-376; the doc-swash records
#   have its exact what_it_is/entity fingerprint and one run timestamp.
CONFIRMED_SCRIPT_GLOBS = (
    "all-cadmas-codex-*.jsonl",
    "sfincs-codex-*.jsonl",
    "rest-xbeach-codex-*.jsonl",
    "rest-efdc-codex-*.jsonl",
    "doc-swash-codex-*.jsonl",
)

# Strong structural-index fingerprints, but no preserved generator was found.
# These require quarantine and provenance reconstruction, not an assertion that
# a particular script generated them.
STRUCTURE_ONLY_SUSPECT_GLOBS = (
    "rest-celeris-codex-*.jsonl",
    "code-xbeach-codex-*.jsonl",
    "rest-shorelines-codex.jsonl",
    "note-swash-codex-*.jsonl",
)


def normalize_path(value: str) -> str:
    value = value.replace(str(ROOT) + "/", "")
    return value[7:] if value.startswith("models/") else value


def matches(name: str, patterns: tuple[str, ...]) -> bool:
    return any(fnmatch.fnmatch(name, pattern) for pattern in patterns)


def evidence_class(filename: str, record: dict[str, Any]) -> str:
    if filename in FINAL_STRUCT_INDEX_FILES:
        return "declared_struct_index"
    if matches(filename, CONFIRMED_SCRIPT_GLOBS):
        return "confirmed_script"
    if matches(filename, STRUCTURE_ONLY_SUSPECT_GLOBS):
        return "structure_only_suspect"
    if record.get("reader") == "mechanical-sweep":
        return "mechanical_binary"
    if record.get("reader") in {"claude", "grok"}:
        return "vendor_llm_labeled"
    return "method_unknown"


def load_records() -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    rows: list[dict[str, Any]] = []
    errors: list[dict[str, Any]] = []
    for source in sorted(RECORDS.glob("*.jsonl")):
        with source.open(encoding="utf-8") as stream:
            for line_number, line in enumerate(stream, 1):
                try:
                    record = json.loads(line)
                except Exception as exc:  # report and continue the read-only audit
                    errors.append(
                        {"record_file": source.name, "line": line_number, "error": str(exc)}
                    )
                    continue
                rows.append(
                    {
                        "record_file": source.name,
                        "line": line_number,
                        "path": normalize_path(str(record.get("path", ""))),
                        "record": record,
                        "evidence": evidence_class(source.name, record),
                    }
                )
    return rows, errors


def summarize(rows: list[dict[str, Any]], errors: list[dict[str, Any]]) -> dict[str, Any]:
    by_model_path: dict[str, dict[str, list[dict[str, Any]]]] = collections.defaultdict(
        lambda: collections.defaultdict(list)
    )
    evidence_records: collections.Counter[str] = collections.Counter()
    for row in rows:
        model = str(row["record"].get("model", "<missing>"))
        by_model_path[model][row["path"]].append(row)
        evidence_records[row["evidence"]] += 1

    models: dict[str, Any] = {}
    for model, paths in sorted(by_model_path.items()):
        evidence_paths: collections.Counter[str] = collections.Counter()
        exclusive_paths: collections.Counter[str] = collections.Counter()
        no_llm_evidence = 0
        for path_rows in paths.values():
            evidence = {row["evidence"] for row in path_rows}
            for item in evidence:
                evidence_paths[item] += 1
            if len(evidence) == 1:
                exclusive_paths[next(iter(evidence))] += 1
            if not evidence.intersection({"vendor_llm_labeled", "method_unknown"}):
                no_llm_evidence += 1
        models[model] = {
            "unique_normalized_paths": len(paths),
            "record_rows": sum(len(items) for items in paths.values()),
            "paths_with_evidence": dict(sorted(evidence_paths.items())),
            "paths_exclusive_to_evidence": dict(sorted(exclusive_paths.items())),
            "paths_without_vendor_llm_or_unknown_method_record": no_llm_evidence,
        }

    duplicate_rows = len(rows) - len(
        {(str(row["record"].get("model", "<missing>")), row["path"]) for row in rows}
    )
    return {
        "warning": (
            "vendor_llm_labeled is metadata evidence only; no JSONL field proves an LLM "
            "actually read and understood the source"
        ),
        "record_files": len(list(RECORDS.glob("*.jsonl"))),
        "record_rows": len(rows),
        "json_errors": errors,
        "unique_model_path_keys": len(rows) - duplicate_rows,
        "duplicate_rows_by_model_path_key": duplicate_rows,
        "records_by_evidence": dict(sorted(evidence_records.items())),
        "models": models,
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--list-files", action="store_true", help="include the complete sorted JSONL filename list"
    )
    args = parser.parse_args()
    rows, errors = load_records()
    report = summarize(rows, errors)
    if args.list_files:
        report["files"] = sorted(path.name for path in RECORDS.glob("*.jsonl"))
    print(json.dumps(report, ensure_ascii=False, indent=2, sort_keys=True))
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
