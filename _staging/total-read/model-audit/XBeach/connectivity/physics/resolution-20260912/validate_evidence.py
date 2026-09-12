"""Recheck source bytes, physical-LF quotes, frozen history, and installed candidates.

This is evidence binding, not an independent semantic or human approval gate.
Run from the repository root: python3 <this file>
"""
import hashlib
import json
import io
import zipfile
import olefile
from lxml import etree as ET
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[6]
CONNECTIVITY = HERE.parents[1]

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def inspect_spans(value, errors, totals):
    if isinstance(value, dict):
        if {"path", "sha256", "line_start", "line_end", "quote_exact_utf8"} <= value.keys():
            path = ROOT / value["path"]
            raw = path.read_bytes()
            quote = b"\n".join(raw.split(b"\n")[value["line_start"]-1:value["line_end"]]).decode()
            if digest(path) != value["sha256"] or quote != value["quote_exact_utf8"]:
                errors.append(f"source/quote mismatch: {value['path']}:{value['line_start']}")
            totals["exact_physics_spans"] += 1
        for child in value.values():
            inspect_spans(child, errors, totals)
    elif isinstance(value, list):
        for child in value:
            inspect_spans(child, errors, totals)

def inspect_lifecycle(value, source_root, errors, totals):
    if isinstance(value, dict):
        if {"path", "lines", "quote"} <= value.keys():
            path = source_root / value["path"]
            start, end = map(int, value["lines"].split("-"))
            quote = "\n".join(path.read_bytes().decode().replace("\r\n", "\n").split("\n")[start-1:end])
            if quote != value["quote"]:
                errors.append(f"lifecycle quote mismatch: {value['path']}:{start}")
            totals["lifecycle_spans"] += 1
        for child in value.values():
            inspect_lifecycle(child, source_root, errors, totals)
    elif isinstance(value, list):
        for child in value:
            inspect_lifecycle(child, source_root, errors, totals)

def main():
    errors = []
    totals = {"exact_physics_spans": 0, "lifecycle_spans": 0, "immutable_files": 0, "installed_candidates": 0}
    for path in [HERE / "adjudication.json", CONNECTIVITY / "physics/connectivity.json"]:
        inspect_spans(json.loads(path.read_text()), errors, totals)
    for name in ["edges.json", "state-contracts.json"]:
        data = json.loads((CONNECTIVITY / "lifecycle" / name).read_text())
        source_root = ROOT / data["source_root"]
        for name, sha in data["sources"].items():
            if digest(source_root / name) != sha:
                errors.append(f"lifecycle source changed: {name}")
        inspect_lifecycle(data, source_root, errors, totals)
    baseline = json.loads((CONNECTIVITY.parent / "closure/immutable-baseline.json").read_text())
    for name, sha in baseline["files"].items():
        if digest(ROOT / name) != sha:
            errors.append(f"immutable history changed: {name}")
        totals["immutable_files"] += 1
    adjudication = json.loads((HERE / "adjudication.json").read_text())
    binding = adjudication["original_findings"]
    if digest(ROOT / binding["path"]) != binding["sha256"]:
        errors.append("original findings changed")
    probe = json.loads((HERE / "grain-probe-result.json").read_text())
    if digest(HERE / "grain_assignment_probe.f90") != probe["source_sha256"]:
        errors.append("probe source changed")
    if probe["exit_code"] != 0:
        errors.append("probe failed")
    totals["document_symbols"] = 0
    ns = {"w": "http://schemas.openxmlformats.org/wordprocessingml/2006/main", "o": "urn:schemas-microsoft-com:office:office", "r": "http://schemas.openxmlformats.org/officeDocument/2006/relationships"}
    for name in ["stress-tensor-symbol", "solitary-wave-symbols"]:
        receipt = json.loads((CONNECTIVITY / "nonhydro-read" / name / "receipt.json").read_text())
        for binding in [receipt[k] for k in ["source_doc", "source_pdf", "converted_docx", "prior_survey"]] + receipt["artifacts"]:
            if digest(ROOT / binding["path"]) != binding["sha256"]:
                errors.append(f"document binding changed: {binding['path']}")
        with olefile.OleFileIO(ROOT / receipt["source_doc"]["path"]) as original, zipfile.ZipFile(ROOT / receipt["converted_docx"]["path"]) as converted:
            paragraphs = ET.fromstring(converted.read("word/document.xml")).findall(".//w:body/w:p", ns)
            relationships = {e.get("Id"): e.get("Target") for e in ET.fromstring(converted.read("word/_rels/document.xml.rels"))}
            for record in receipt["records"]:
                native = original.openstream(record["doc_stream"]).read()
                with olefile.OleFileIO(io.BytesIO(converted.read(record["converted_docx_member"]))) as embedded:
                    if embedded.openstream("Equation Native").read() != native:
                        errors.append("converted Native differs from original DOC")
                if hashlib.sha256(native).hexdigest() != record["native_sha256"]:
                    errors.append("document Native hash mismatch")
                paragraph = paragraphs[record["direct_body_paragraph_zero_based"]]
                if "".join(paragraph.xpath(".//w:t/text()", namespaces=ns)) != record["paragraph_text"]:
                    errors.append("document paragraph text changed")
                members = ["word/" + relationships[obj.get("{" + ns["r"] + "}id")] for obj in paragraph.findall(".//o:OLEObject", ns)]
                if record["converted_docx_member"] not in members:
                    errors.append("Native is not in cited paragraph")
                if ET.tostring(paragraph, encoding="utf-8") != (ROOT / record["paragraph_xml"]).read_bytes():
                    errors.append("saved paragraph XML differs")
                totals["document_symbols"] += 1
    manifest_path = HERE / "install-manifest.json"
    if manifest_path.exists():
        for entry in json.loads(manifest_path.read_text())["files"]:
            if digest(ROOT / entry["target"]) != entry["after_sha256"]:
                errors.append(f"installed candidate mismatch: {entry['target']}")
            totals["installed_candidates"] += 1
    result = {"scope": "source/citation/history binding only; not model completion or human approval", "status": "FAIL" if errors else "PASS", "counts": totals, "errors": errors}
    (HERE / "validation.json").write_text(json.dumps(result, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(result, ensure_ascii=False))
    raise SystemExit(bool(errors))

if __name__ == "__main__":
    main()
