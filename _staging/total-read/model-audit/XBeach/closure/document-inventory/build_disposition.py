#!/usr/bin/env python3
"""Add page provenance, duplicate candidates, and canonical routes to exact-207."""

from __future__ import annotations

import csv
import difflib
import hashlib
import json
import math
import re
from collections import Counter, defaultdict
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
BASE = ROOT / "_staging/total-read/model-audit/XBeach"

PDF_BY_WORK = {
    "xbeach-kingsday-technical-reference-2015-v1.22-r4567": "XBeach_manual_kingsday.md",
    "xbeach-master-manual-2015": "XBeach_manual_master.md",
    "xbeach-nonhydrostatic-model-draft-2010": "non-hydrostatic_report_draft.md",
}

PRINTED_PAGE_OFFSETS = {
    "xbeach-kingsday-technical-reference-2015-v1.22-r4567": (7, 2),
    "xbeach-master-manual-2015": (8, 4),
    "xbeach-nonhydrostatic-model-draft-2010": (11, 10),
}

ROUTES = {
    "modes-grid-coordinates": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_mode_dispatch.md",
        "models/XBeach/source-analysis/xbeach_single_dir.md",
        "models/XBeach/source-analysis/xbeach_params.md",
    ],
    "wave-action-breaking-roller-friction": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_wave_action_balance.md",
        "models/XBeach/source-analysis/xbeach_wave_breaking.md",
        "models/XBeach/source-analysis/xbeach_wave_functions.md",
    ],
    "flow-friction-viscosity": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_bed_friction.md",
        "models/XBeach/source-analysis/xbeach_flow_solver.md",
    ],
    "nonhydrostatic-physics-numerics": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_nonh.md",
        "models/XBeach/source-analysis/xbeach_solver.md",
        "models/XBeach/source-analysis/xbeach_flow_solver.md",
    ],
    "groundwater": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_groundwater.md",
    ],
    "sediment-transport": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_morphology.md",
        "models/XBeach/source-analysis/xbeach_intrawave_sediment_transport.md",
    ],
    "morphology-bed-composition-avalanching": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_morphology.md",
        "models/XBeach/source-analysis/xbeach_avalanching.md",
        "models/XBeach/source-analysis/xbeach-morphology-foundation.md",
    ],
    "wave-boundary-spectra": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_wave_boundary_generation.md",
        "models/XBeach/source-analysis/wave/xbeach_wave_boundary.md",
        "models/XBeach/source-analysis/wave/xbeach-boundary-and-wave-setup.md",
        "models/XBeach/source-analysis/xbeach_swan_handoff.md",
    ],
    "flow-tide-discharge-boundaries": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_flow_boundary_conditions.md",
        "models/XBeach/source-analysis/xbeach_tide_forcing.md",
    ],
    "vegetation-ships": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_vegetation.md",
        "models/XBeach/source-analysis/xbeach_ship_waves.md",
    ],
    "output": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_output.md",
    ],
    "validation-nonhydrostatic": [
        "models/XBeach/source-analysis/xbeach_nonh.md",
        "PROPOSED: models/XBeach/manual-notes/xbeach-nonhydrostatic-report.md",
    ],
    "build-mpi-version": [
        "models/XBeach/source-analysis/xbeach_infrastructure.md",
        "PROPOSED: models/XBeach/manual-notes/xbeach-document-version-drift.md",
    ],
    "manual-discrepancies": [
        "PROPOSED: models/XBeach/manual-notes/xbeach-manual-discrepancies.md",
    ],
    "parameter-defaults-mixed": [
        "models/XBeach/manual-notes/xbeach-master-manual.md",
        "models/XBeach/source-analysis/xbeach_params.md",
    ],
}

ADJUDICATION_MARKERS = (
    "contradiction",
    "drift",
    "verification",
    "unfinished",
    "invalid",
    "damage",
    "inconsistency",
    "ambiguity",
    "suspicious",
    "correction",
    "conflict",
)


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def tokens(text: str) -> list[str]:
    return re.findall(r"[a-z0-9_]+", text.lower())


def parse_ranges(spec: str) -> set[int]:
    result: set[int] = set()
    for part in spec.split(","):
        nums = [int(x) for x in re.findall(r"\d+", part)]
        if nums:
            result.update(range(nums[0], nums[-1] + 1))
    return result


def parse_page_aware(name: str) -> tuple[list[str], list[int], dict[int, str]]:
    lines = (HERE / "page-aware" / name).read_text(errors="replace").splitlines()
    page = 0
    page_text: dict[int, list[str]] = defaultdict(list)
    out_tokens: list[str] = []
    out_pages: list[int] = []
    for line in lines:
        marker = re.fullmatch(r"<!-- page (\d+) -->", line)
        if marker:
            page = int(marker.group(1))
            continue
        if line.strip():
            page_text[page].append(line.strip())
        for token in tokens(line):
            out_tokens.append(token)
            out_pages.append(page)
    return out_tokens, out_pages, {p: " ".join(v) for p, v in page_text.items()}


def align_representation(work_id: str, representation: str):
    pdf_name = PDF_BY_WORK[work_id]
    page_tokens, token_pages, page_text = parse_page_aware(pdf_name)
    old_lines = (BASE / "bindoc-converted" / representation).read_text(errors="replace").splitlines()
    old_tokens: list[str] = []
    old_token_lines: list[int] = []
    for line_number, line in enumerate(old_lines, 1):
        for token in tokens(line):
            old_tokens.append(token)
            old_token_lines.append(line_number)
    matcher = difflib.SequenceMatcher(None, old_tokens, page_tokens, autojunk=True)
    token_map = {
        old_start + offset: new_start + offset
        for old_start, new_start, length in matcher.get_matching_blocks()
        for offset in range(length)
    }
    return old_tokens, old_token_lines, token_map, token_pages, page_text, matcher.ratio()


def printed_pages(work_id: str, physical_pages: list[int]) -> list[str]:
    start, offset = PRINTED_PAGE_OFFSETS[work_id]
    return [str(page - offset) if page >= start else f"frontmatter-physical-{page}" for page in physical_pages]


def classify_group(item: dict) -> str:
    text = (item["finding"] + " " + item["class"]).lower()
    if any(x in text for x in ("validation", "shoal", "basin", "dam-break", "dambreak", "dispersion-limit", "tuning-limit")):
        return "validation-nonhydrostatic"
    if any(x in text for x in ("mpi", "compile", "build", "revision", "release", "version")):
        return "build-mpi-version"
    if any(x in text for x in ("output", "netcdf", "tintm", "tspoint")):
        return "output"
    if any(x in text for x in ("ship", "vegetation")):
        return "vegetation-ships"
    if any(x in text for x in ("groundwater", "aquifer", "infiltration", "forchheimer")):
        return "groundwater"
    if any(x in text for x in ("morfac", "morpholog", "avalan", "bed-layer", "breathing layer", "ne_layer", "setbathy", "dryslp", "wetslp")):
        return "morphology-bed-composition-avalanching"
    if any(x in text for x in ("sediment", "transport", "shields", "dilatancy", "cmax", "d50", "rheea", "facsl", "soulsby", "van thiel")):
        return "sediment-transport"
    if any(x in text for x in ("tide", "discharge", "cyclic", "paulrevere", "tideloc", "absorbing-generating", "radiation-boundary")):
        return "flow-tide-discharge-boundaries"
    if any(x in text for x in ("spectrum", "spectra", "jonswap", "wbctype", "dtheta", "swan", "ts_nonh", "boun_u", "wave forcing")):
        return "wave-boundary-spectra"
    if any(x in text for x in ("non-hydro", "pressure", "solver", "maccormack", "minmod", "sip", "keller", "hermitian", "dispersion", "wetting-drying", "secorder")):
        return "nonhydrostatic-physics-numerics"
    if any(x in text for x in ("friction", "chezy", "manning", "smagorinsky", "viscosity", "nuh")):
        return "flow-friction-viscosity"
    if any(x in text for x in ("wave", "breaking", "roller", "gamma", "wci", "fw", "stokes")):
        return "wave-action-breaking-roller-friction"
    if any(x in text for x in ("grid", " ny", "coordinate", "directional", "posdwn", "mode")):
        return "modes-grid-coordinates"
    return "parameter-defaults-mixed"


def technical_anchors(text: str) -> set[str]:
    raw = set(tokens(text))
    return {
        token
        for token in raw
        if "_" in token
        or any(char.isdigit() for char in token)
        or token
        in {
            "wci", "nuh", "smag", "morfac", "morfacopt", "tideloc", "paulrevere",
            "posdwn", "tspoint", "tspoints", "tintm", "tintg", "secorder", "solver",
            "instat", "nonh", "swave", "waveform", "swan", "dtheta", "snells",
            "setbathy", "ne_layer", "compute_motion", "wbctype", "jonswap", "cfl",
        }
    }


def text_similarity(a: str, b: str) -> float:
    at, bt = set(tokens(a)), set(tokens(b))
    jaccard = len(at & bt) / max(1, len(at | bt))
    sequence = difflib.SequenceMatcher(None, a.lower(), b.lower()).ratio()
    aa, ba = technical_anchors(a), technical_anchors(b)
    anchor = len(aa & ba) / max(1, len(aa | ba))
    return 0.35 * jaccard + 0.35 * sequence + 0.30 * anchor


def main() -> None:
    items = [json.loads(line) for line in (HERE / "exact-207.jsonl").read_text().splitlines()]
    adjudication_path = BASE / "closure/manual-code-adjudications.json"
    adjudication_doc = json.loads(adjudication_path.read_text())
    adjudication_by_id = defaultdict(list)
    for adjudication in adjudication_doc["items"]:
        for finding_id in adjudication["finding_ids"]:
            adjudication_by_id[finding_id].append(adjudication)
    canonical_text = {
        str(path.relative_to(ROOT)): path.read_text(errors="replace").lower()
        for path in sorted((ROOT / "models/XBeach").rglob("*.md"))
        if "/raw/" not in str(path)
    }
    alignments = {}
    page_aware_meta = {}
    for work_id, pdf_name in PDF_BY_WORK.items():
        page_path = HERE / "page-aware" / pdf_name
        page_aware_meta[work_id] = {
            "path": str(page_path.relative_to(ROOT)),
            "sha256": sha256(page_path),
            "page_count": sum(1 for line in page_path.read_text().splitlines() if line.startswith("<!-- page ")),
        }
    for item in items:
        key = (item["work_id"], item["representation_path"])
        if key not in alignments:
            alignments[key] = align_representation(*key)
        old_tokens, old_lines, token_map, token_pages, page_text, alignment_ratio = alignments[key]
        line_set = parse_ranges(item["reported_lines"])
        source_indices = [index for index, line in enumerate(old_lines) if line in line_set]
        mapped = [token_map[index] for index in source_indices if index in token_map]
        page_hits = Counter(token_pages[index] for index in mapped if token_pages[index] > 0)
        query = set(tokens(item["finding"]))
        ranked_pages = sorted(
            page_hits,
            key=lambda page: (
                len(query & set(tokens(page_text.get(page, "")))) * math.log2(page_hits[page] + 2),
                page_hits[page],
            ),
            reverse=True,
        )
        retrieval_fallback = False
        if not ranked_pages:
            retrieval_fallback = True
            query_core = {
                token for token in query
                if len(token) > 3 or "_" in token or any(char.isdigit() for char in token)
            }
            page_token_sets = {page: set(tokens(text)) for page, text in page_text.items()}
            document_frequency = Counter(
                token for token_set in page_token_sets.values() for token in token_set
            )
            ranked_pages = sorted(
                page_token_sets,
                key=lambda page: sum(
                    math.log((len(page_token_sets) + 1) / (document_frequency[token] + 1)) + 1
                    for token in query_core & page_token_sets[page]
                ),
                reverse=True,
            )[:3]
        selected_pages = sorted(ranked_pages[:6])
        item["page_map"] = {
            "method": "OpenDataLoader v2.4.7 page-separator regeneration followed by ordered token-sequence alignment; no alternate PDF parser",
            "page_aware_path": page_aware_meta[item["work_id"]]["path"],
            "page_aware_sha256": page_aware_meta[item["work_id"]]["sha256"],
            "alignment_ratio_whole_representation": round(alignment_ratio, 6),
            "reported_span_token_count": len(source_indices),
            "mapped_token_count": len(mapped),
            "mapped_token_fraction": round(len(mapped) / max(1, len(source_indices)), 6),
            "physical_pdf_pages": selected_pages,
            "printed_pages_or_frontmatter": printed_pages(item["work_id"], selected_pages),
            "all_mapped_physical_page_hits": dict(sorted(page_hits.items())),
            "status": (
                "direct-pdf-representation"
                if item["representation_kind"] == "pdf-opendataloader-markdown"
                else "cross-format-retrieval-candidate"
                if retrieval_fallback
                else "cross-format-mapped"
                if len(mapped) / max(1, len(source_indices)) >= 0.7
                else "cross-format-partial"
            ),
        }
        group = classify_group(item)
        item["canonical_group"] = group
        item["candidate_canonical_routes"] = list(ROUTES[group])
        named_anchors = sorted(
            anchor for anchor in technical_anchors(item["finding"])
            if not anchor.isdigit() and len(anchor) >= 2
        )
        anchor_hits = {
            path: [anchor for anchor in named_anchors if anchor in body]
            for path, body in canonical_text.items()
        }
        anchor_hits = {path: hits for path, hits in anchor_hits.items() if hits}
        matched_anchors = set(anchor for hits in anchor_hits.values() for anchor in hits)
        item["existing_canonical_anchor_check"] = {
            "anchors": named_anchors,
            "matched_anchors": sorted(matched_anchors),
            "matched_fraction": round(len(matched_anchors) / max(1, len(named_anchors)), 4),
            "files": anchor_hits,
            "scope_note": "Lexical locator only; this is not semantic verification or proof that the compound finding is covered.",
        }
        class_lower = item["class"].lower()
        if any(marker in class_lower for marker in ("conversion", "equation_verification", "damage", "invalid")):
            item["disposition"] = "exclude-converted-value-or-formula-from-canonical; retain-source-warning"
            item["current_canonical_coverage"] = "conversion-risk-disposition-complete"
            item["candidate_canonical_routes"].append(ROUTES["manual-discrepancies"][0])
        elif any(marker in class_lower for marker in ("contradiction", "inconsistency", "conflict", "ambiguity", "suspicious")):
            item["disposition"] = "document-both-source-statements-as-an-internal-conflict; do-not-select-a-value"
            item["current_canonical_coverage"] = "conflict-register-addition-required"
            item["candidate_canonical_routes"].append(ROUTES["manual-discrepancies"][0])
        elif any(marker in class_lower for marker in ("drift", "correction")):
            item["disposition"] = "record-as-edition-or-parameter-drift; do-not-generalize-to-current-code"
            item["current_canonical_coverage"] = "version-crosswalk-addition-required"
            item["candidate_canonical_routes"].append(ROUTES["manual-discrepancies"][0])
        elif "unfinished" in class_lower:
            item["disposition"] = "record-as-source-scoped-unfinished-feature-or-document-limit"
            item["current_canonical_coverage"] = "historical-limit-addition-required"
            item["candidate_canonical_routes"].append(ROUTES["manual-discrepancies"][0])
        elif item["work_id"] == "xbeach-nonhydrostatic-model-draft-2010":
            item["disposition"] = "merge-as-draft-scoped-fact-or-limit-into-nonhydrostatic-report-note"
            item["current_canonical_coverage"] = "partial-mechanism-coverage; validation/applicability detail absent"
        elif group in {"validation-nonhydrostatic", "build-mpi-version"}:
            item["disposition"] = "add-source-and-version-scoped-manual-fact"
            item["current_canonical_coverage"] = "gap"
        else:
            item["disposition"] = "merge-with-existing-canonical-as-edition-scoped-manual-fact"
            item["current_canonical_coverage"] = "existing-merge-target; retain compound finding as one denominator row"
        if item["finding_id"] in adjudication_by_id:
            conversion_exclusion = item["disposition"].startswith("exclude-converted")
            item["source_code_adjudications"] = [
                {
                    "topic": adjudication["topic"],
                    "finding_ids": adjudication["finding_ids"],
                    "finding_binding": next(
                        binding
                        for binding in adjudication["finding_bindings"]
                        if binding["finding_id"] == item["finding_id"]
                    ),
                    "finding_bindings": adjudication["finding_bindings"],
                    "scope": adjudication["scope"],
                    "canonical_ready_ko": adjudication["canonical_ready_ko"],
                    "evidence": [
                        {
                            "path": evidence["path"],
                            "sha256": evidence["sha256"],
                            "line_start": evidence["line_start"],
                            "line_end": evidence["line_end"],
                        }
                        for evidence in adjudication["evidence"]
                    ],
                    "source_artifact": str(adjudication_path.relative_to(ROOT)),
                    "source_artifact_sha256": sha256(adjudication_path),
                }
                for adjudication in adjudication_by_id[item["finding_id"]]
            ]
            item["disposition"] = (
                "exclude-converted-formula; source-code-behavior-separately-adjudicated"
                if conversion_exclusion
                else "merge-document-conflict-with-frozen-source-snapshot-adjudication"
            )
            item["current_canonical_coverage"] = (
                "conversion-exclusion-complete; separate-source-code-adjudication-complete"
                if conversion_exclusion
                else "source-code-adjudication-complete; retain-document-version-scope"
            )

    # Cross-format duplicate candidates stay explicitly probabilistic. A fact can be split or
    # combined differently by the two readers, so this intentionally permits many-to-one links.
    by_work_kind = defaultdict(lambda: defaultdict(list))
    for item in items:
        by_work_kind[item["work_id"]][item["representation_kind"]].append(item)
    for item in items:
        other_kind = (
            "pdf-opendataloader-markdown"
            if item["representation_kind"] != "pdf-opendataloader-markdown"
            else "docx-text"
            if item["work_id"] != "xbeach-nonhydrostatic-model-draft-2010"
            else "doc-ole-text"
        )
        candidates = by_work_kind[item["work_id"]].get(other_kind, [])
        scored = []
        pages = set(item["page_map"]["physical_pdf_pages"])
        for candidate in candidates:
            candidate_pages = set(candidate["page_map"]["physical_pdf_pages"])
            page_overlap = len(pages & candidate_pages) / max(1, len(pages | candidate_pages))
            group_bonus = 0.15 if item["canonical_group"] == candidate["canonical_group"] else 0.0
            score = 0.70 * text_similarity(item["finding"], candidate["finding"]) + 0.15 * page_overlap + group_bonus
            scored.append((score, candidate["finding_id"]))
        score, candidate_id = max(scored, default=(0.0, None))
        item["cross_format_duplicate_candidate"] = candidate_id if score >= 0.30 else None
        item["cross_format_duplicate_score"] = round(score, 4)
        item["duplicate_confidence"] = "high" if score >= 0.55 else "probable" if score >= 0.30 else "unresolved"

    output = HERE / "all-207-disposition.jsonl"
    output.write_text("".join(json.dumps(item, ensure_ascii=False, sort_keys=True) + "\n" for item in items))
    fields = [
        "finding_id", "work_id", "representation_path", "reported_lines", "class", "finding",
        "canonical_group", "disposition", "current_canonical_coverage",
        "cross_format_duplicate_candidate", "duplicate_confidence", "cross_format_duplicate_score",
        "physical_pdf_pages", "printed_pages_or_frontmatter", "page_map_status", "mapped_token_fraction",
        "candidate_canonical_routes",
        "source_code_adjudication_topics", "source_code_adjudications_json",
    ]
    with (HERE / "all-207-disposition.csv").open("w", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields)
        writer.writeheader()
        for item in items:
            writer.writerow({
                **{key: item.get(key) for key in fields},
                "physical_pdf_pages": ";".join(map(str, item["page_map"]["physical_pdf_pages"])),
                "printed_pages_or_frontmatter": ";".join(item["page_map"]["printed_pages_or_frontmatter"]),
                "page_map_status": item["page_map"]["status"],
                "mapped_token_fraction": item["page_map"]["mapped_token_fraction"],
                "candidate_canonical_routes": ";".join(item["candidate_canonical_routes"]),
                "source_code_adjudication_topics": ";".join(
                    x["topic"] for x in item.get("source_code_adjudications", [])
                ),
                "source_code_adjudications_json": json.dumps(
                    item.get("source_code_adjudications", []), ensure_ascii=False, sort_keys=True
                ),
            })
    by_id = {item["finding_id"]: item for item in items}
    mutual_pairs = set()
    for item in items:
        candidate_id = item["cross_format_duplicate_candidate"]
        if candidate_id and by_id[candidate_id]["cross_format_duplicate_candidate"] == item["finding_id"]:
            mutual_pairs.add(tuple(sorted((item["finding_id"], candidate_id))))
    summary = {
        "schema": "xbeach-document-findings-disposition/v1",
        "count": len(items),
        "input_exact_207_sha256": sha256(HERE / "exact-207.jsonl"),
        "output_jsonl_sha256": sha256(output),
        "group_counts": dict(sorted(Counter(x["canonical_group"] for x in items).items())),
        "disposition_counts": dict(sorted(Counter(x["disposition"] for x in items).items())),
        "coverage_counts": dict(sorted(Counter(x["current_canonical_coverage"] for x in items).items())),
        "duplicate_confidence_counts": dict(sorted(Counter(x["duplicate_confidence"] for x in items).items())),
        "mutual_cross_format_duplicate_pair_count": len(mutual_pairs),
        "mutual_cross_format_duplicate_pairs": [list(pair) for pair in sorted(mutual_pairs)],
        "page_map_status_counts": dict(sorted(Counter(x["page_map"]["status"] for x in items).items())),
        "page_aware_sources": page_aware_meta,
        "source_code_adjudications": {
            "path": str(adjudication_path.relative_to(ROOT)),
            "sha256": sha256(adjudication_path),
            "topic_count": len(adjudication_doc["items"]),
            "finding_count": len(adjudication_by_id),
            "finding_topic_link_count": sum(len(values) for values in adjudication_by_id.values()),
        },
        "opendataloader": {
            "executable": ".venv/bin/opendataloader-pdf",
            "package_version": "2.4.7",
            "command": ".venv/bin/opendataloader-pdf -o <page-aware-dir> -f markdown --markdown-page-separator '<!-- page %page-number% -->' --image-output off <pdfs>",
        },
    }
    (HERE / "disposition-summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True) + "\n")
    print(json.dumps(summary, ensure_ascii=False, indent=2, sort_keys=True))


if __name__ == "__main__":
    main()
