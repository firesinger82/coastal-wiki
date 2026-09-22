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


WIKI_ROOTS = {"models", "concepts", "textbook", "experience", "examples",
               "references", "research", "standards", "data", "tools",
               "_staging", "_archive"}


def check_note_path(note_path):
    """`note_path` 는 **위키 루트 기준 상대경로**여야 한다 (예: `models/ROMS/x.md`).

    이 계약을 강제하는 이유 — 어기면 예외가 아니라 **그럴듯한 오답**이 나오기 때문이다.
    절대경로를 넘기면 `parts[0]` 이 `"/"` 라서 `owning_model` 이 조용히 None 을 돌리고,
    모든 참조가 소유 모델 단계를 건너뛰어 cross-model 탐색으로 떨어진다. 결과는
    실패가 아니라 **다른 저장소로의 잘못된 귀속**이다.

    실측(2026-09-21): 남은 BEHIND 저장소 집계에서 절대경로를 넘긴 탓에
    `roms_test` 가 인용 0건이 아니라 **file-line 45 · file-only 36** 으로 나왔다.
    RESOLVED 9,120→0 · RESOLVED_CROSS_MODEL 46→9,044 · AMBIGUOUS 458→1,332.
    게이트는 통과한다 — 함수가 틀린 게 아니라 잘못 불린 것이라서. failure mode 34.
    """
    p = Path(note_path)
    if p.is_absolute():
        raise ValueError(
            f"note_path 는 위키 상대경로여야 한다(절대경로를 받음): {note_path}\n"
            f"  → wiki 루트 기준으로 바꿔 넘겨라: Path(p).relative_to(WIKI)")
    if p.parts and p.parts[0] not in WIKI_ROOTS:
        raise ValueError(
            f"note_path 의 첫 경로요소가 위키 최상위 디렉터리가 아니다: {note_path}\n"
            f"  → 허용: {sorted(WIKI_ROOTS)}")
    return p


def owning_model(note_path):
    """노트 경로에서 소유 모델을 얻는다. concepts/textbook 은 None."""
    parts = check_note_path(note_path).parts
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


def _frontmatter_field(note_path, wiki, field):
    try:
        lines = (Path(wiki)/note_path).read_text(errors="replace").splitlines()
    except OSError:
        return None
    if lines[:1] != ["---"]:
        return None
    for l in lines[1:40]:
        if l.strip() == "---":
            break
        m = re.match(rf"\s*{field}\s*:\s*(.+?)\s*$", l)
        if m:
            return m.group(1).strip().strip('"\'')
    return None


def declared_component(note_path, wiki):
    """노트 frontmatter 의 `component:` 선언. 이중 배치 소스의 귀속 근거."""
    return _frontmatter_field(note_path, wiki, "component")


def declared_scope(note_path, wiki):
    """`source_scope:` — 노트가 분석한 저장소 상대 디렉터리 선언 목록.

    변종 트리(배포본 vs 파생본, 3D vs 3D2F, CPU vs GPU 포팅)를 가르는 일반 선언이다.

    두 형태:
      `dir`   — 그 디렉터리 **아래 전부**(하위 디렉터리 포함)
      `dir/*` — 그 디렉터리 **직속 파일만**(하위 제외)

    `dir/*` 가 필요한 이유: 한 저장소 안에서 루트와 하위가 같은 파일명을 쓰면
    접두사로 갈리지 않는다. LISFLOOD-FP 는 `output.cpp` 와 `swe/output.cpp`,
    `swe/fields.cpp` 와 `swe/dg2/fields.cpp` 가 공존한다.
    """
    v = _frontmatter_field(note_path, wiki, "source_scope")
    if not v:
        return []
    return [s.strip().strip('"\'').rstrip("/") if s.strip().endswith("/*")
            else s.strip().strip('"\'').strip("/")
            for s in v.strip("[]").split(",") if s.strip()]


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
                    # 변종 트리: 노트가 선언한 source_scope 로 거른다.
                    #   `dir`   — 그 디렉터리 **아래 전부**(하위 포함)
                    #   `dir/*` — 그 디렉터리 **직속만**(하위 제외)
                    # 후자가 필요한 이유: 한 저장소 안에서 루트와 하위가 같은 파일명을
                    # 쓰는 경우(LISFLOOD-FP 의 `output.cpp` vs `swe/output.cpp`,
                    # `swe/fields.cpp` vs `swe/dg2/fields.cpp`)는 접두사로 갈리지 않는다.
                    root = f"models/{own}/raw/source_code/"
                    for sc in declared_scope(note_path, wiki):
                        if sc.endswith("/*"):
                            scope_dir = sc[:-2]          # ← ref basename 인 `base` 를 가리지 않는다
                            pref = [x for x in c
                                    if x[len(root):].rsplit("/", 1)[0] == scope_dir]
                        else:
                            pref = [x for x in c if x[len(root):].startswith(sc + "/")]
                        if pref and len(pref) < len(c):
                            c = pref
                            if len(c) == 1:
                                return pack("RESOLVED_BY_SCOPE", own, c,
                                            f"노트 선언 source_scope={sc}")
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

    # 5. 슬래시 축약 — `TriDiag_PCRx/y.wgsl` = `…x.wgsl` + `…y.wgsl` 두 파일의 압축 표기다.
    #    파일 참조가 아니므로 UNRESOLVED 로 세면 안 된다. 파서의 NUMERIC_STEM
    #    (`swancom1/5.ftn`)과 같은 현상인데 stem 이 알파벳이라 모양만으로는 갈리지 않는다.
    #    **모양이 아니라 트리를 보고 판정한다** — `/` 앞 마지막 성분이 그 모델의 실제
    #    디렉터리가 아니면 경로일 수 없다. 실디렉터리면(예: `src/main.c`) 건드리지 않는다.
    if "/" in ref and own and wiki:
        parent = ref.rsplit("/", 1)[0].rsplit("/", 1)[-1]
        src = Path(wiki)/f"models/{own}/raw/source_code"
        if src.is_dir() and not any(d.name == parent for d in src.rglob("*") if d.is_dir()):
            return pack("UNRESOLVED_SLASH_ABBREV", None, [],
                        f"`{parent}` 가 {own} 트리의 디렉터리가 아니다 — 슬래시 축약 표기")

    return pack("UNRESOLVED", None, [], "어느 모델 트리에도 없음")
