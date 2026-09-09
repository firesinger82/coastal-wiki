#!/usr/bin/env python3
"""Build the four source-scoped XBeach manual-note drafts and the 207 ledger."""

from __future__ import annotations

import hashlib
import json
import subprocess
import re
from collections import Counter, defaultdict
from difflib import SequenceMatcher
from pathlib import Path


ROOT = Path(__file__).resolve().parents[6]
HERE = Path(__file__).resolve().parent
OUT = HERE / "canonical/models/XBeach/manual-notes"
ROWS_PATH = HERE / "all-207-disposition.jsonl"
DOCX_EVIDENCE_PATH = HERE / "retrieval-docx-evidence.json"
CODE_ADJ_PATH = HERE.parent / "manual-code-adjudications.json"
MASTER_EXISTING = ROOT / "models/XBeach/manual-notes/xbeach-master-manual.md"

FILES = {
    "K": "xbeach-kingsday-technical-reference.md",
    "M": "xbeach-master-manual.md",
    "N": "xbeach-nonhydrostatic-report-2010.md",
    "D": "xbeach-document-discrepancies-and-version-drift.md",
}

TITLES = {
    "K": "XBeach Kingsday technical reference (2015 v1.22 r4567)",
    "M": "XBeach Master Manual (Deltares 2015)",
    "N": "XBeach non-hydrostatic model draft report (2010)",
    "D": "XBeach document discrepancies and version drift",
}

WORK_SHORT = {
    "xbeach-kingsday-technical-reference-2015-v1.22-r4567": "Kingsday technical reference 2015 v1.22 r4567",
    "xbeach-master-manual-2015": "Master Manual 2015",
    "xbeach-nonhydrostatic-model-draft-2010": "Non-hydrostatic draft report 2010",
}

WORK_ROUTE = {
    "xbeach-kingsday-technical-reference-2015-v1.22-r4567": "K",
    "xbeach-master-manual-2015": "M",
    "xbeach-nonhydrostatic-model-draft-2010": "N",
}

SPECIAL = {
    "document-both-source-statements-as-an-internal-conflict; do-not-select-a-value",
    "merge-document-conflict-with-frozen-source-snapshot-adjudication",
    "record-as-edition-or-parameter-drift; do-not-generalize-to-current-code",
    "record-as-source-scoped-unfinished-feature-or-document-limit",
    "exclude-converted-value-or-formula-from-canonical; retain-source-warning",
    "exclude-converted-formula; source-code-behavior-separately-adjudicated",
}

DISPOSITION_KO = {
    "merge-with-existing-canonical-as-edition-scoped-manual-fact": "판본 한정 사실로 채택",
    "add-source-and-version-scoped-manual-fact": "판본 한정 새 사실로 채택",
    "merge-as-draft-scoped-fact-or-limit-into-nonhydrostatic-report-note": "2010 초안의 사실·한계로 채택",
    "document-both-source-statements-as-an-internal-conflict; do-not-select-a-value": "같은 문서의 양립 불가 진술을 모두 보존; 단일 값 선택 안 함",
    "merge-document-conflict-with-frozen-source-snapshot-adjudication": "문서 모순 보존; 고정 소스 snapshot의 구현 판정 별도 적용",
    "record-as-edition-or-parameter-drift; do-not-generalize-to-current-code": "역사 판본·매개변수 드리프트로 종결; 현재 동작으로 일반화 금지",
    "record-as-source-scoped-unfinished-feature-or-document-limit": "해당 판본이 밝힌 미구현·적용 한계로 종결",
    "exclude-converted-value-or-formula-from-canonical; retain-source-warning": "변환 손상값을 사실 승격에서 제외; 경고만 보존",
    "exclude-converted-formula; source-code-behavior-separately-adjudicated": "깨진 변환식 제외; 구현은 소스 snapshot으로 별도 판정",
}

GROUP_TITLES = {
    "modes-grid-coordinates": "모드·격자·좌표",
    "wave-boundary-spectra": "파랑 경계·스펙트럼",
    "wave-action-breaking-roller-friction": "파동작용·쇄파·롤러·단파 마찰",
    "flow-friction-viscosity": "흐름 마찰·점성",
    "flow-tide-discharge-boundaries": "흐름·조석·유량 경계",
    "groundwater": "지하수",
    "sediment-transport": "표사이동",
    "morphology-bed-composition-avalanching": "지형변화·지층·avalanching",
    "nonhydrostatic-physics-numerics": "비정수압 물리·수치법",
    "validation-nonhydrostatic": "비정수압 검증 사례",
    "vegetation-ships": "식생·선박",
    "output": "출력",
    "build-mpi-version": "빌드·MPI·버전 범위",
    "parameter-defaults-mixed": "혼합 매개변수 기본값·입력 규약",
}


def sha256(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def compact_pages(values):
    values = list(values or [])
    return ", ".join(str(x) for x in values) if values else "none"


def locator(row, docx_evidence):
    span = reported_span_evidence(row)
    base = {
        "source_work": row["work_id"],
        "original_path": row["original_path"],
        "original_sha256": row["original_sha256"],
        "representation_path": row["representation_path"],
        "representation_sha256": row["representation_sha256"],
        "reported_lines": row["reported_lines"],
        "page_map_status": row["page_map"]["status"],
        "reported_span_sha256": span["sha256"],
        "reported_span_direct_quotes": span["direct_quotes"],
    }
    if row["finding_id"] in docx_evidence:
        ev = docx_evidence[row["finding_id"]]
        blocks = ev["evidence_blocks"]
        base.update({
            "citation_kind": "original-docx-block",
            "docx_blocks": [b["block_index"] for b in blocks],
            "docx_block_details": blocks,
            "pdf_pages": None,
            "pdf_page_claim": None,
        })
        return base
    if row["representation_kind"] == "doc-ole-text" and row["page_map"]["status"] == "cross-format-partial":
        extract = ROOT / "_staging/total-read/model-audit/XBeach/bindoc-converted" / row["representation_path"]
        source_lines = extract.read_text(encoding="utf-8", errors="replace").splitlines()
        candidates = []
        ftokens = set(re.findall(r"[a-z0-9_.=-]+", row["finding"].lower()))
        for lineno in parse_ranges(row["reported_lines"]):
            if 1 <= lineno <= len(source_lines):
                text = re.sub(r"\s+", " ", source_lines[lineno - 1]).strip()
                if len(text) < 8:
                    continue
                tokens = set(re.findall(r"[a-z0-9_.=-]+", text.lower()))
                score = len(ftokens & tokens)
                candidates.append((score, lineno, text))
        quotes = []
        for _, lineno, text in sorted(candidates, reverse=True):
            words = text.split()
            if len(words) > 24:
                text = " ".join(words[:24]) + " …"
            if text not in [x["quote"] for x in quotes]:
                quotes.append({"line": lineno, "quote": text})
            if len(quotes) == 3:
                break
        base.update({
            "citation_kind": "original-doc-text-extract",
            "text_extract_sha256": row["representation_sha256"],
            "text_extract_lines": row["reported_lines"],
            "direct_quotes": quotes,
            "printed_section_pages": row["page_map"].get("printed_pages_or_frontmatter", []),
            "physical_pdf_pages": None,
            "pdf_page_claim": None,
        })
        return base
    pm = row["page_map"]
    base.update({
        "citation_kind": "original-pdf-page" if row["representation_kind"] == "pdf-opendataloader-markdown" else "cross-format-pdf-page-alignment",
        "physical_pdf_pages": pm.get("physical_pdf_pages", []),
        "printed_pages_or_frontmatter": pm.get("printed_pages_or_frontmatter", []),
        "mapped_token_fraction": pm.get("mapped_token_fraction"),
        "page_aware_sha256": pm.get("page_aware_sha256"),
    })
    return base


def locator_text(row, loc):
    if loc["citation_kind"] == "original-docx-block":
        blocks = loc["docx_blocks"]
        btxt = ", ".join(f"B{x}" for x in blocks)
        # Direct excerpts are evidentiary, not a replacement for the source.
        quotes = []
        ftokens = set(re.findall(r"[a-z0-9_.=-]+", row["finding"].lower()))
        ranked = []
        for b in loc["docx_block_details"]:
            qt = b["quote"]
            qtokens = set(re.findall(r"[a-z0-9_.=-]+", qt.lower()))
            score = len(ftokens & qtokens)
            ranked.append((score, b["block_index"], qt))
        for _, _, q in sorted(ranked, reverse=True):
            if q not in quotes:
                quotes.append(q)
            if len(quotes) == 3:
                break
        qtxt = "; ".join(f'“{q}”' for q in quotes)
        partial = " 불완전한 PDF 정렬은 citation에서 폐기함." if loc["page_map_status"] == "cross-format-partial" else ""
        return f'{Path(loc["original_path"]).name}, 원본 DOCX 문서순 block {btxt} (SHA-256 `{loc["original_sha256"]}`; audit extract lines {loc["reported_lines"]}); 직접 인용: {qtxt}. PDF page는 주장하지 않음.{partial}'
    if loc["citation_kind"] == "original-doc-text-extract":
        qtxt = "; ".join(f'L{x["line"]} “{x["quote"]}”' for x in loc["direct_quotes"])
        printed = compact_pages(loc.get("printed_section_pages"))
        return f'{Path(loc["original_path"]).name} 원본 OLE DOC text extract lines {loc["text_extract_lines"]} (DOC SHA-256 `{loc["original_sha256"]}`; extract SHA-256 `{loc["text_extract_sha256"]}`); 직접 인용: {qtxt}; 대응 printed section {printed}. 불완전한 PDF 정렬은 citation에서 폐기하며 DOC 또는 PDF physical page를 주장하지 않음.'
    p = compact_pages(loc.get("physical_pdf_pages"))
    printed = compact_pages(loc.get("printed_pages_or_frontmatter"))
    kind = "직접 PDF" if loc["citation_kind"] == "original-pdf-page" else "DOC/DOCX→동일 work PDF 정렬"
    return f'{Path(loc["original_path"]).name}, {kind}, physical PDF p.{p}, printed page/frontmatter {printed}, audit extract lines {loc["reported_lines"]}; 원본 SHA-256 `{loc["original_sha256"]}`.'


def parse_ranges(spec: str):
    out = []
    for part in spec.split(","):
        if "-" in part:
            a, b = map(int, part.split("-"))
        else:
            a = b = int(part)
        out.extend(range(a, b + 1))
    return out


def reported_span_evidence(row):
    extract = ROOT / "_staging/total-read/model-audit/XBeach/bindoc-converted" / row["representation_path"]
    source_lines = extract.read_text(encoding="utf-8", errors="replace").splitlines()
    raw = []
    candidates = []
    ftokens = set(re.findall(r"[a-z0-9_.=-]+", row["finding"].lower()))
    for lineno in parse_ranges(row["reported_lines"]):
        if not 1 <= lineno <= len(source_lines):
            continue
        text = re.sub(r"\s+", " ", source_lines[lineno - 1]).strip()
        raw.append(f"{lineno}:{text}")
        if len(text) < 8:
            continue
        tokens = set(re.findall(r"[a-z0-9_.=-]+", text.lower()))
        candidates.append((len(ftokens & tokens), lineno, text))
    quotes = []
    for _, lineno, text in sorted(candidates, reverse=True):
        words = text.split()
        if len(words) > 24:
            text = " ".join(words[:24]) + " …"
        if text not in [x["quote"] for x in quotes]:
            quotes.append({"line": lineno, "quote": text})
        if len(quotes) == 3:
            break
    return {
        "sha256": hashlib.sha256("\n".join(raw).encode("utf-8")).hexdigest(),
        "direct_quotes": quotes,
    }


def make_clusters(rows):
    by_id = {r["finding_id"]: r for r in rows}
    parent = {x: x for x in by_id}

    def find(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x

    def union(a, b):
        a, b = find(a), find(b)
        if a != b:
            parent[max(a, b)] = min(a, b)

    for r in rows:
        other = r.get("cross_format_duplicate_candidate")
        if not other or other not in by_id:
            continue
        reciprocal = by_id[other].get("cross_format_duplicate_candidate") == r["finding_id"]
        same_work = by_id[other]["work_id"] == r["work_id"]
        if reciprocal and same_work:
            union(r["finding_id"], other)

    clusters = defaultdict(list)
    for r in rows:
        clusters[find(r["finding_id"])].append(r)
    return [sorted(v, key=lambda r: r["finding_id"]) for _, v in sorted(clusters.items())]


def target(cluster):
    if any(r["disposition"] in SPECIAL for r in cluster):
        return "D"
    return WORK_ROUTE[cluster[0]["work_id"]]


def distinct_findings(cluster):
    selected = []
    # Prefer the PDF rendering as canonical wording inside a same-work cluster.
    ordered = sorted(cluster, key=lambda r: (r["representation_kind"] != "pdf-opendataloader-markdown", r["finding_id"]))
    for row in ordered:
        text = row["finding"].strip()
        if any(SequenceMatcher(None, text.lower(), prior.lower()).ratio() >= 0.82 for prior in selected):
            continue
        selected.append(text)
    return selected


def evidence_code(adjudication):
    refs = []
    for e in adjudication["evidence"]:
        refs.append(f'{e["path"]}:{e["line_start"]}-{e["line_end"]} (SHA-256 `{e["sha256"]}`)')
    return "; ".join(refs)


def frontmatter(route):
    source = {
        "K": "XBeach Kingsday technical reference 2015 v1.22 r4567",
        "N": "XBeach non-hydrostatic model draft report 2010",
        "D": "three historical XBeach works plus frozen source snapshot",
    }[route]
    return f'''---
title: "{TITLES[route]}"
model: XBeach
layer: 2
depends_on: []
canonical_source: self
citation_status: verified
has_source_needed: false
verification_method: "Exhaustive locator/provenance cross-reference for XH001-XH207 using OpenDataLoader v2.4.7 page-aware PDF extraction, original DOCX document-order blocks, and original-bound OLE DOC text extracts; semantic dispositions inherited from immutable X00 with targeted independent spot checks"
verification_by: "Codex (cross-ref)"
verification_date: 2026-09-09
note_author: "Codex"
note_date: 2026-09-09
source_scope: "{source}"
---

# {TITLES[route]}

이 문서는 XBeach 문서 전수검수의 HIGH 207건 중 이 출처에 속하는 판본 한정 판정을 통합한다. 문서의 설명은 다른 판본이나 현재 코드의 기본값으로 자동 확장하지 않는다. PDF 인용은 physical page와 문서 자체의 printed page를 구분한다. DOCX locator는 원본 문서의 문단·표 행 순서와 직접 인용을 쓰며 PDF page를 부여하지 않는다. OLE DOC의 부분 정렬 항목은 원본에 결박된 text extract의 행·해시·직접 인용과 보고서 printed section만 기록하고 physical page를 주장하지 않는다. 같은 work의 reciprocal DOC/DOCX↔PDF 후보는 공동검토 묶음으로 배치했지만 두 finding은 독립 원장 항목이며 묶음이 의미 동일성을 주장하지 않는다.

## 검증 범위

XH001-XH207의 원본 정체·해시·표현 행·페이지 또는 문서 block locator는 전수 확인했다. `cross-format-partial` 15건은 불완전한 PDF 정렬을 citation으로 쓰지 않고, DOCX 9건은 원본 block, OLE DOC 6건은 원본에 결박된 text-extract 행과 직접 인용으로 대체했다. 의미 판정은 immutable X00 전수독해 결과를 보존하며, 별도의 독립 의미 재독해는 posdwn, 손상된 vardens, standing-wave, 1D solver, NetCDF와 DOCX retrieval 표본에 집중했다. 따라서 공동검토 묶음은 중복 제거를 위한 의미 동치 판정이 아니다.

'''


def section_entry(cluster, fact_id, route, locators, adjudications):
    ids = [r["finding_id"] for r in cluster]
    aliases = "\n".join(f'<a id="{x.lower()}"></a>' for x in ids)
    dispositions = list(dict.fromkeys(r["disposition"] for r in cluster))
    findings = distinct_findings(cluster)
    lines = [aliases, f'### {fact_id} — {", ".join(ids)}', ""]
    lines.append(f'**판정:** {"; ".join(DISPOSITION_KO[d] for d in dispositions)}.')
    lines.append("")

    code_items = []
    for topic, item in adjudications.items():
        if set(ids) & set(item["finding_ids"]):
            code_items.append(item)

    if any(d.startswith("exclude-converted") for d in dispositions):
        lines.append("깨진 식·수치 자체는 canonical 사실로 사용하지 않는다. 아래 문장에는 제외 이유와 문서가 보여 주는 손상 범위만 남긴다.")
        lines.append("")
    elif any("internal-conflict" in d for d in dispositions):
        lines.append("동일 판본 안의 진술이 양립하지 않으므로 양측을 함께 기록하며 어느 값을 실행 기본값으로 선택하지 않는다.")
        lines.append("")
    elif any("version-drift" in d for d in dispositions):
        lines.append("다음 내용은 이 판본을 재현하거나 해석할 때만 적용한다. 이후 인터페이스나 현재 소스 동작을 정하는 근거로 쓰지 않는다.")
        lines.append("")

    for f in findings:
        lines.append(f'- {f}')
    lines.append("")

    if code_items:
        lines.append("**고정 소스 snapshot 판정:**")
        lines.append("")
        for item in code_items:
            lines.append(f'- [[#source-adjudication-{item["topic"]}|`{item["topic"]}` 구현 판정]]을 적용한다.')
        lines.append("")

    lines.append("**출처 locator:**")
    lines.append("")
    for row in cluster:
        lines.append(f'- {row["finding_id"]}: {locator_text(row, locators[row["finding_id"]])}')
    lines.append("")
    return "\n".join(lines)


def main():
    rows = [json.loads(line) for line in ROWS_PATH.read_text(encoding="utf-8").splitlines()]
    assert len(rows) == 207 and len({r["finding_id"] for r in rows}) == 207
    assert [r["finding_id"] for r in rows] == [f"XH{i:03d}" for i in range(1, 208)]
    docx_obj = json.loads(DOCX_EVIDENCE_PATH.read_text(encoding="utf-8"))
    docx_evidence = {x["finding_id"]: x for x in docx_obj["items"]}
    assert len(docx_evidence) == 26 and all(x["status"] == "original-docx-block-verified" for x in docx_evidence.values())
    code_obj = json.loads(CODE_ADJ_PATH.read_text(encoding="utf-8"))
    adjudications = {x["topic"]: x for x in code_obj["items"]}
    code_sha = sha256(CODE_ADJ_PATH)

    clusters = make_clusters(rows)
    assert len(clusters) == 136
    locators = {r["finding_id"]: locator(r, docx_evidence) for r in rows}
    routed = defaultdict(list)
    for cluster in clusters:
        routed[target(cluster)].append(cluster)

    OUT.mkdir(parents=True, exist_ok=True)
    mapping = []
    fact_counters = Counter()
    documents = {}
    for route in ("K", "M", "N", "D"):
        if route == "M":
            # Use the frozen pre-closure note, so rebuilding after installation cannot append twice.
            baseline = json.loads((HERE.parent / "immutable-baseline.json").read_text())["baseline_commit"]
            base = subprocess.check_output(["git", "show", baseline + ":models/XBeach/manual-notes/xbeach-master-manual.md"], cwd=ROOT).decode("utf-8")
            if "has_source_needed:" not in base.split("---", 2)[1]:
                base = base.replace("citation_status: verified\n", "citation_status: verified\nhas_source_needed: false\n", 1)
            if "verification_by:" not in base.split("---", 2)[1]:
                base = base.replace("note_date: 2026-06-18\n", 'note_date: 2026-09-09\nverification_by: "Codex (closure cross-ref; original note attribution retained)"\nverification_date: 2026-09-09\n', 1)
            base = base.replace('note_author: "Claude Opus 4.8 (1M context)"', 'note_author: "Claude Opus 4.8 (original); Codex (207-finding closure supplement)"', 1)
            text = base.rstrip() + "\n\n## 17. 2026-09-09 document-audit closure supplement\n\n"
            text += "이 절의 2015 Master Manual 사실은 기존 본문과 함께 읽는다. 충돌·변환 손상·현재 소스 판정은 [[xbeach-document-discrepancies-and-version-drift]]가 canonical이며, 이 절에는 충돌하지 않는 판본 사실만 둔다. 신규 locator는 OpenDataLoader v2.4.7 page-aware PDF 결과를 사용했다. 같은 work의 reciprocal DOCX↔PDF 후보는 공동검토 묶음으로 배치했지만 두 finding은 독립 원장 항목이며 묶음이 의미 동일성을 주장하지 않는다.\n\n"
            text += "### 17.1 검증 범위\n\nXH001-XH207의 원본 정체·해시·표현 행·페이지 또는 문서 block locator는 전수 확인했다. `cross-format-partial` 15건은 불완전한 PDF 정렬을 citation으로 쓰지 않고 DOCX 원본 block 또는 원본에 결박된 OLE DOC text-extract로 대체했다. 의미 판정은 immutable X00 전수독해를 보존하며 별도 독립 의미 재독해는 posdwn, 손상된 vardens, standing-wave, 1D solver, NetCDF와 DOCX retrieval 표본에 집중했다.\n\n"
        else:
            text = frontmatter(route)
        text += "## 출처 고정\n\n"
        source_rows = [r for c in routed[route] for r in c]
        for path in sorted({r["original_path"] for r in source_rows}):
            r = next(r for r in source_rows if r["original_path"] == path)
            text += f'- `{path}` — SHA-256 `{r["original_sha256"]}`\n'
        if route == "D":
            text += f'- 고정 source-adjudication digest — SHA-256 `{code_sha}`. 아래 8개 판정의 repo-relative source line과 원문 SHA가 구현 근거다.\n'
        text += "\n"

        if route == "D":
            text += "## 고정 소스 snapshot 판정\n\n"
            text += "이 8개 판정은 문서 모순을 지우지 않는다. 보관 source snapshot에서 확인되는 구현 동작만 정하며, 각 역사 문서의 양측 진술은 해당 XH 항목에 그대로 남긴다.\n\n"
            for topic, item in adjudications.items():
                text += f'<a id="source-adjudication-{topic}"></a>\n'
                text += f'### `{topic}`\n\n{item["canonical_ready_ko"]}\n\n'
                text += f'소스 근거: {evidence_code(item)}.\n\n'

        by_group = defaultdict(list)
        for cluster in routed[route]:
            by_group[cluster[0]["canonical_group"]].append(cluster)
        for group in sorted(by_group, key=lambda x: GROUP_TITLES.get(x, x)):
            text += f'## {GROUP_TITLES.get(group, group)}\n\n'
            for cluster in by_group[group]:
                fact_counters[route] += 1
                fact_id = f'{route}-{fact_counters[route]:03d}'
                text += section_entry(cluster, fact_id, route, locators, adjudications)
                members = [r["finding_id"] for r in cluster]
                canonical_file = f'models/XBeach/manual-notes/{FILES[route]}'
                staged_file = str((OUT / FILES[route]).relative_to(ROOT))
                for row in cluster:
                    mapping.append({
                        "finding_id": row["finding_id"],
                        "canonical_anchor": f'{canonical_file}#{row["finding_id"].lower()}',
                        "canonical_file": canonical_file,
                        "staged_file": staged_file,
                        "review_group_id": fact_id,
                        "group_members": members,
                        "work_id": row["work_id"],
                        "canonical_group": row["canonical_group"],
                        "disposition": row["disposition"],
                        "source_locator": locators[row["finding_id"]],
                        "source_code_adjudication_topics": sorted(t for t, i in adjudications.items() if row["finding_id"] in i["finding_ids"]),
                    })
        documents[route] = text.rstrip() + "\n"

    # Correct two old Master-note sentences whose wording conflicts with the
    # frozen implementation adjudication; the full historical document dispute
    # remains in the discrepancy note.
    documents["M"] = documents["M"].replace(
        "- **dilatancy** (§2.7.5, p.36, `dilatancy = 1`): Van Rhee(2010) 임계 Shields 감소 (2.101), `pormax`($n_l$), `rheeA`(A, 단입자 0.75/연속체~1.7). permeability $k_l$ Den Adel(1987) (2.102).",
        "- **dilatancy** (§2.7.5, p.36, `dilatancy = 1`): 매뉴얼 본문은 임계 Shields 감소라고 서술하지만 식·문구와 보관 소스 snapshot이 충돌한다. 현재 snapshot은 양의 조건에서 임계 bed-load 속도를 증가시킨다. 문서 양측과 소스 판정은 [[xbeach-document-discrepancies-and-version-drift#xh103]] 참조. `pormax`($n_l$), `rheeA`(단입자 0.75/연속체~1.7), permeability $k_l$은 Den Adel(1987) 식 (2.102)에 따른다.",
    )
    documents["M"] = documents["M"].replace(
        "적응시간 $T_s=\\max(f_{Ts}\\,h/w_s,\\,T_{s,min})$ (2.77), `tsfac`($f_{Ts}$), `Tsmin`.",
        "매뉴얼 판본의 적응시간 식은 $T_s=\\max(f_{Ts}\\,h/w_s,\\,T_{s,min})$ (2.77)로 적혀 있다. 보관 소스 snapshot은 `oldTsmin` 분기에 따라 `Tsmin` 또는 `dtlimTs*dt` 하한을 선택하므로, 이 식을 현재 코드의 무조건 하한으로 일반화하지 않는다([[xbeach-document-discrepancies-and-version-drift#xh138]]).",
    )
    documents["M"] = documents["M"].replace(
        "- **tide** (§3.2.3, p.46): `tideloc` = 0(uniform `zs0`)/1/2/4 시계열, `zs0file`.",
        "- **tide** (§3.2.3, p.46): `tideloc` = 0(uniform `zs0`)/1/2/4 시계열, `zs0file`. 같은 판본은 `tideloc=1`의 landward 적용과 corner 순서, `tideloc=3` 허용 여부를 서로 다르게 적으므로 그 세부값은 [[xbeach-document-discrepancies-and-version-drift#xh110]]에서 양측 진술로만 보존한다.",
    )
    documents["M"] = documents["M"].replace(
        "1D params.txt 예시(p.49): `depfile`, `posdwn=0`, `nx=265`",
        "1D params.txt 예시(p.49)는 `depfile`, `posdwn=0`, `nx=265`",
    ).replace(
        "`nglobalvar`.",
        "`nglobalvar`를 싣는다. 이 예시의 `posdwn=0`은 표의 positive-up 값 `-1`과 충돌하며 보관 snapshot에서는 바닥고를 0으로 만들므로 재사용하지 않는다([[xbeach-document-discrepancies-and-version-drift#xh112]]).",
        1,
    )
    documents["M"] = documents["M"].replace(
        "`ts_nonh`(비정수압용 elev+velocity)",
        "`ts_nonh`(비정수압용 시계열; 열의 필수성·순서는 문서 내부가 충돌하므로 [[xbeach-document-discrepancies-and-version-drift#xh109]] 참조)",
    ).replace(
        "`Tm01switch`(0)",
        "`Tm01switch`(표 기본값 0; Kingsday 산문의 기본값 1 주장과 충돌하므로 [[xbeach-document-discrepancies-and-version-drift#xh147]] 참조)",
    )

    for route, text in documents.items():
        (OUT / FILES[route]).write_text(text, encoding="utf-8")

    mapping.sort(key=lambda x: x["finding_id"])
    assert [x["finding_id"] for x in mapping] == [f"XH{i:03d}" for i in range(1, 208)]
    obj = {
        "schema": "xbeach-document-canonical-mapping/v1",
        "date": "2026-09-09",
        "denominator": {
            "count": 207,
            "ids": "XH001-XH207",
            "exact_207_sha256": sha256(HERE / "exact-207.jsonl"),
            "x00_sha256": rows[0]["x00_sha256"],
        },
        "consolidation": {
            "consolidation_group_count": len(clusters),
            "same_work_cross_format_clusters": sum(len(c) > 1 for c in clusters),
            "rule": "Reciprocal DOC/DOCX↔PDF candidates within the same work are placed in a shared review group. Both findings remain independent; grouping is not a semantic-identity assertion. Editions remain separate and conflict groups preserve both statements.",
        },
        "document_counts": {
            FILES[r]: {
                "review_groups": len(routed[r]),
                "finding_ids": sum(len(c) for c in routed[r]),
            }
            for r in ("K", "M", "N", "D")
        },
        "retrieval_docx_evidence": {
            "retrieval_candidate_count": 17,
            "partial_docx_count": 9,
            "total_original_docx_block_records": 26,
            "sha256": sha256(DOCX_EVIDENCE_PATH),
            "pdf_page_claims": 0,
        },
        "manual_code_adjudications": {
            "topics": sorted(adjudications),
            "finding_ids": sorted({x for i in adjudications.values() for x in i["finding_ids"]}),
            "finding_topic_link_count": sum(len(i["finding_ids"]) for i in adjudications.values()),
            "sha256": code_sha,
        },
        "entries": mapping,
    }
    (HERE / "document-canonical-mapping.json").write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(obj["document_counts"], ensure_ascii=False, indent=2))
    print("review groups", len(clusters), "mapping entries", len(mapping))


if __name__ == "__main__":
    main()
