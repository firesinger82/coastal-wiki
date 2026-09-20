r"""coastal-wiki source reference resolver (DESIGN v2.0 §CROSS-MODEL RESOLUTION).

노트의 `file:line` 참조를 실제 소스 파일로 귀속한다. basename 단독 매칭은
동명 파일을 엉뚱한 모델로 귀속시키므로(예: Delft3D 가 SWAN 을 번들) 다음 순서를 강제한다.

  1. 소유 모델 안에서 경로 suffix 일치
  2. 소유 모델 안에서 basename 일치
  3. 소유 모델 안에서 **생성 파일 매핑** — SWAN/SWASH 는 switch.pl 이
     `.ftn90 → .f90`, `.ftn → .f` 로 전처리한다. 노트가 생성물 이름을 인용할 수 있다
  4. 다른 모델 트리 (cross-model). 소유자가 하나면 귀속 기록, 여럿이면 AMBIGUOUS
  5. 실패 → UNRESOLVED

**부분 이름(`Compdata.f90` ← `SwanCompdata.ftn90`)은 추측으로 해소하지 않는다.**
"""
import re
from pathlib import Path

# switch.pl 전처리 규칙: 생성 확장자 → 원본 확장자 후보
GENERATED = {"f90": ["ftn90"], "f": ["ftn"], "F90": ["ftn90"], "F": ["ftn"]}


# migration 롤백 자산(`<tree>.old-<sha>`)은 색인에서 제외한다.
# 포함하면 모든 파일이 동명 2중이 되어 AMBIGUOUS 로 오판정된다 (SWAN 파일럿 2026-09-20).
ROLLBACK_RE = re.compile(r"\.old-[0-9a-f]{7,40}$")


def _excluded(rel):
    return any(ROLLBACK_RE.search(part) for part in Path(rel).parts)


def build_index(wiki):
    """{model: {basename: [repo 상대 경로]}}"""
    idx = {}
    for m in sorted((Path(wiki)/"models").iterdir()):
        src = m/"raw/source_code"
        if not src.is_dir():
            continue
        d = {}
        for p in src.rglob("*"):
            if not p.is_file():
                continue
            rel = str(p.relative_to(wiki))
            if _excluded(rel):
                continue
            d.setdefault(p.name, []).append(rel)
        idx[m.name] = d
    return idx


def owning_model(note_path):
    """노트 경로에서 소유 모델을 얻는다. concepts/textbook 은 None."""
    parts = Path(note_path).parts
    return parts[1] if len(parts) > 2 and parts[0] == "models" else None


def _suffix_hit(cands, ref):
    """참조가 디렉터리 성분을 가지면 경로 끝 일치를 우선한다."""
    if "/" not in ref:
        return cands
    tail = ref.lstrip("./")
    hit = [c for c in cands if c.endswith("/" + tail)]
    return hit or cands


def _repo_of(rel):
    """models/<M>/raw/source_code/<repo>/… → <repo>"""
    parts = Path(rel).parts
    return parts[4] if len(parts) > 4 else ""


def _narrow(cands, wiki, model, max_line):
    """같은 모델 안 동명 후보 좁히기. 반환 (후보, 판정보조)"""
    note = ""
    # A. 줄 번호 배제 — 인용된 최대 줄보다 짧은 파일은 그 인용의 대상일 수 없다
    if max_line and len(cands) > 1:
        keep = []
        for c in cands:
            try:
                n = sum(1 for _ in open(Path(wiki)/c, errors="replace"))
            except OSError:
                n = 0
            if n >= max_line:
                keep.append(c)
        if keep and len(keep) < len(cands):
            cands, note = keep, f"줄 {max_line} 기준 후보 배제"
    # B. 주 저장소 우선 — 저장소 디렉터리명이 모델명과 일치하면 그쪽
    if len(cands) > 1 and model:
        pri = [c for c in cands if _repo_of(c).lower() == model.lower()]
        if pri and len(pri) < len(cands):
            return pri, (note + "; " if note else "") + f"주 저장소({model}) 우선"
        cands = pri or cands
    return cands, note


def declared_component(note_path, wiki):
    """노트 frontmatter 의 `component:` 선언. 이중 배치 소스의 귀속 근거."""
    try:
        lines = (Path(wiki)/note_path).read_text(errors="replace").splitlines()
    except OSError:
        return None
    if lines[:1] != ["---"]:
        return None
    for l in lines[1:40]:
        if l.strip() == "---":
            break
        m = re.match(r"\s*component\s*:\s*(.+?)\s*$", l)
        if m:
            return m.group(1).strip().strip('"\'')
    return None


def resolve(ref, note_path, index, max_line=None, wiki=None):
    """반환: dict(status, model, paths, detail)"""
    base = Path(ref).name
    stem, _, ext = base.rpartition(".")
    own = owning_model(note_path)

    def pack(status, model, paths, detail=""):
        return dict(status=status, model=model, paths=paths, detail=detail)

    def look(model):
        return index.get(model, {})

    # 1-2. 소유 모델 직접 일치
    if own:
        c = look(own).get(base)
        if c:
            c = _suffix_hit(c, ref)
            if len(c) > 1:
                c, why = _narrow(c, wiki, own, max_line)
                if len(c) > 1 and wiki:
                    # 이중 배치(배포본 vs 사용자 템플릿 등): 노트가 선언한 component 를 근거로 쓴다
                    comp = declared_component(note_path, wiki)
                    if comp:
                        pref = [x for x in c if f"/{comp.strip('/')}/" in "/" + x + "/"]
                        if pref and len(pref) < len(c):
                            return pack("RESOLVED_BY_COMPONENT", own, pref,
                                        (why + "; " if why else "") +
                                        f"노트 선언 component={comp}")
                if len(c) == 1:
                    return pack("RESOLVED_NARROWED", own, c, why)
            return pack("RESOLVED" if len(c) == 1 else "AMBIGUOUS_SAME_MODEL", own, c)
        # 3. 생성 파일 매핑
        for src_ext in GENERATED.get(ext, []):
            c = look(own).get(f"{stem}.{src_ext}")
            if c:
                return pack("RESOLVED_GENERATED", own, _suffix_hit(c, ref),
                            f"switch.pl 생성물 인용: {base} ← {stem}.{src_ext}")
        # 3b. 확장자 짝이 어긋난 생성물 (.f90 ↔ .ftn 등)
        for src_ext in ("ftn90", "ftn"):
            if src_ext in GENERATED.get(ext, []):
                continue
            c = look(own).get(f"{stem}.{src_ext}")
            if c and ext in GENERATED:
                return pack("RESOLVED_GENERATED_EXT_MISMATCH", own, _suffix_hit(c, ref),
                            f"생성 확장자 불일치: 인용 {base}, 실제 원본 {stem}.{src_ext}")

    # 4. cross-model
    owners = {m: d[base] for m, d in index.items() if base in d and m != own}
    if len(owners) == 1:
        m, c = next(iter(owners.items()))
        return pack("RESOLVED_CROSS_MODEL", m, _suffix_hit(c, ref),
                    f"소유 모델({own}) 밖에서 해소 — {m} 트리")
    if len(owners) > 1:
        return pack("AMBIGUOUS_CROSS_MODEL", None,
                    [p for c in owners.values() for p in c],
                    f"복수 모델 보유: {', '.join(sorted(owners))} — 번들 사본 가능성")

    return pack("UNRESOLVED", None, [], "어느 모델 트리에도 없음")
