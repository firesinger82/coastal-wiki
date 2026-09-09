#!/usr/bin/env python3
"""Freeze the XBeach X00 HIGH-finding denominator with stable provenance."""

from __future__ import annotations

import hashlib
import json
from collections import Counter
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
X00 = ROOT / "_staging/total-read/model-audit/XBeach/XBeach-X00.jsonl"

REPRESENTATIONS = {
    "XBeach_manual_kingsday.docx.txt": {
        "work_id": "xbeach-kingsday-technical-reference-2015-v1.22-r4567",
        "representation": "docx-text",
        "original_path": "models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_kingsday.docx",
    },
    "XBeach_manual_kingsday.md": {
        "work_id": "xbeach-kingsday-technical-reference-2015-v1.22-r4567",
        "representation": "pdf-opendataloader-markdown",
        "original_path": "models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_kingsday.pdf",
    },
    "XBeach_manual_master.docx.txt": {
        "work_id": "xbeach-master-manual-2015",
        "representation": "docx-text",
        "original_path": "models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_master.docx",
    },
    "XBeach_manual_master.md": {
        "work_id": "xbeach-master-manual-2015",
        "representation": "pdf-opendataloader-markdown",
        "original_path": "models/XBeach/raw/source_code/trunk/doc/manual/XBeach_manual_master.pdf",
    },
    "non-hydrostatic_report_draft.doc.txt": {
        "work_id": "xbeach-nonhydrostatic-model-draft-2010",
        "representation": "doc-ole-text",
        "original_path": "models/XBeach/raw/source_code/trunk/doc/reports/non-hydrostatic_report_draft.doc",
    },
    "non-hydrostatic_report_draft.md": {
        "work_id": "xbeach-nonhydrostatic-model-draft-2010",
        "representation": "pdf-opendataloader-markdown",
        "original_path": "models/XBeach/raw/source_code/trunk/doc/reports/non-hydrostatic_report_draft.pdf",
    },
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def main() -> None:
    records = [json.loads(line) for line in X00.read_text().splitlines() if line.strip()]
    artifact_sha = sha256(X00)
    frozen = []
    high_index = 0
    for record_index0, record in enumerate(records):
        path = record["path"]
        for unresolved_index0, finding in enumerate(record["unresolved"]):
            if finding["severity"] != "HIGH":
                continue
            high_index += 1
            source = REPRESENTATIONS[path]
            representation_path = (
                ROOT / "_staging/total-read/model-audit/XBeach/bindoc-converted" / path
            )
            original_path = ROOT / source["original_path"]
            frozen.append(
                {
                    "finding_id": f"XH{high_index:03d}",
                    "x00_artifact": "_staging/total-read/model-audit/XBeach/XBeach-X00.jsonl",
                    "x00_sha256": artifact_sha,
                    "x00_record_index0": record_index0,
                    "x00_record_index1": record_index0 + 1,
                    "x00_unresolved_index0": unresolved_index0,
                    "x00_unresolved_index1": unresolved_index0 + 1,
                    "work_id": source["work_id"],
                    "representation_path": path,
                    "representation_kind": source["representation"],
                    "representation_sha256": sha256(representation_path),
                    "representation_lines_read": record["lines_read"],
                    "reported_lines": finding["lines"],
                    "severity": finding["severity"],
                    "class": finding["class"],
                    "finding": finding["finding"],
                    "original_path": source["original_path"],
                    "original_sha256": sha256(original_path),
                }
            )

    assert high_index == 207, high_index
    assert all(item["severity"] == "HIGH" for item in frozen)

    out = HERE / "exact-207.jsonl"
    out.write_text(
        "".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in frozen)
    )
    manifest = {
        "schema": "xbeach-document-findings-denominator/v1",
        "population_rule": "Every unresolved item with severity HIGH in the immutable XBeach-X00.jsonl artifact, in artifact order.",
        "x00_path": str(X00.relative_to(ROOT)),
        "x00_sha256": artifact_sha,
        "x00_record_count": len(records),
        "x00_all_unresolved_count": sum(len(r["unresolved"]) for r in records),
        "severity_counts": dict(
            sorted(Counter(x["severity"] for r in records for x in r["unresolved"]).items())
        ),
        "frozen_high_count": len(frozen),
        "work_counts": dict(sorted(Counter(x["work_id"] for x in frozen).items())),
        "representation_counts": dict(
            sorted(Counter(x["representation_path"] for x in frozen).items())
        ),
        "exact_207_path": str(out.relative_to(ROOT)),
        "exact_207_sha256": sha256(out),
    }
    (HERE / "exact-207-manifest.json").write_text(
        json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True) + "\n"
    )
    print(json.dumps(manifest, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
