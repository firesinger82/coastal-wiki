r"""좌표 재앵커 — 주석화된 옛 코드에 정박하지 않는다 (DESIGN v2.0 §REANCHOR).

upstream 이 교체된 코드를 **주석으로 남기는** 경우가 많다. 그러면 옛 줄 내용과
똑같은 텍스트가 새 파일에 두 번 나타난다 — 주석 한 번, 실행 코드 한 번.
내용만 대조하면 주석 쪽에 정박한다.

Celeris 실측(2026-09-21): 재앵커 4건 전부 이 형태였다.
  Handler_BoundaryPass.js  138 `// export function create_BoundaryPass_BindGroup(...)`  ← 주석
                           140 `   export function create_BoundaryPass_BindGroup(...)`  ← 실행
  main.js                  2622 주석 / 2624 실행,  Time_Series.js 58 주석 / 60 실행

규칙: 후보가 여럿이면 **주석이 아닌 줄을 고른다.** 전부 주석이면 고르지 않고
`ALL_COMMENTED` 로 돌려보낸다(자동 치환 금지, 사람 판단).
"""
import re

# 줄 주석 접두. Fortran 은 열 1 의 `!`/`C`/`c` 와 자유형식 `!` 를 모두 본다.
LINE_COMMENT = {
    ".js": ("//",), ".ts": ("//",), ".wgsl": ("//",), ".c": ("//",), ".h": ("//",),
    ".cpp": ("//",), ".java": ("//",), ".go": ("//",),
    ".f": ("!",), ".f90": ("!",), ".F": ("!",), ".F90": ("!",),
    ".for": ("!",), ".ftn": ("!",), ".ftn90": ("!",), ".inc": ("!",),
    ".py": ("#",), ".sh": ("#",), ".pl": ("#",), ".cmake": ("#",), ".yml": ("#",),
}
DEFAULT_COMMENTS = ("//", "#", "!")


def comment_prefixes(path):
    for ext, pref in LINE_COMMENT.items():
        if path.endswith(ext):
            return pref
    return DEFAULT_COMMENTS


def is_commented(line, path=""):
    """그 줄이 통째로 주석인가. 코드 뒤에 붙은 꼬리 주석은 해당 없음."""
    s = line.strip()
    if not s:
        return False
    for p in comment_prefixes(path):
        if s.startswith(p):
            return True
    # 고정형식 Fortran: 1열의 C/c/*
    if path.endswith((".f", ".for", ".ftn", ".F")) and line[:1] in ("C", "c", "*"):
        return True
    return False


def _norm(s):
    return " ".join(s.split())


def _strip_comment(line, path=""):
    s = line.strip()
    for p in comment_prefixes(path):
        if s.startswith(p):
            return s[len(p):].strip()
    if path.endswith((".f", ".for", ".ftn", ".F")) and line[:1] in ("C", "c", "*"):
        return line[1:].strip()
    return s


_ASSIGN = re.compile(r"(?<![=!<>+\-*/])=(?!=)")


def _signature(s):
    """식이 바뀌어도 남는 식별 부분.

    호출·선언은 `(` 앞, 할당문은 `=` 왼쪽(대상 이름), 그 외는 앞 40자.
    인자 추가(`foo(a,b)` → `foo(a,b,c)`)나 우변 확장
    (`t = a*b` → `t = a*b + c`)에도 같은 signature 가 나온다.
    """
    if "(" in s:
        head = s.split("(")[0].strip()
        if len(head) >= 8:
            return head
    m = _ASSIGN.search(s)
    if m:
        lhs = s[:m.start()].strip()
        if len(lhs) >= 4:
            return lhs
    return s[:40].strip()


NEIGHBOR = 8


def find_anchor(old_line, new_lines, path="", hint=None):
    """옛 줄 내용에 해당하는 **실행 코드** 줄 번호를 찾는다.

    upstream 이 옛 코드를 주석으로 남기면 옛 텍스트와 정확히 같은 것은 **주석 쪽**이고
    실행 줄은 인자·식이 바뀌어 있다. 그래서 주석 일치를 찾았을 때는 주변에서
    같은 signature 의 실행 줄을 찾는다.

    status ∈ RESOLVED / RESOLVED_SKIPPED_COMMENT / RESOLVED_VIA_COMMENT_NEIGHBOR
             / ALL_COMMENTED / NOT_FOUND / AMBIGUOUS
    """
    key = _norm(old_line)
    if not key:
        return dict(line=None, status="NOT_FOUND", candidates=[])
    hits = [i + 1 for i, l in enumerate(new_lines)
            if _norm(l) == key or _norm(_strip_comment(l, path)) == key]
    if not hits:
        return dict(line=None, status="NOT_FOUND", candidates=[])

    # 옛 줄 자체가 주석이면(섹션 표제 등) 주석 일치가 정상이다.
    # 함정은 **옛 줄이 실행 코드**인데 그 사본이 주석으로만 남은 경우다.
    if is_commented(old_line, path):
        pick = min(hits, key=lambda h: abs(h - hint)) if hint else hits[0]
        st = "RESOLVED" if (hint or len(hits) == 1) else "AMBIGUOUS"
        return dict(line=pick, status=st, candidates=hits)

    live = [h for h in hits if not is_commented(new_lines[h - 1], path)]
    if live:
        pick = min(live, key=lambda h: abs(h - hint)) if hint else live[0]
        if len(live) > 1 and hint is None:
            return dict(line=pick, status="AMBIGUOUS", candidates=live)
        st = "RESOLVED_SKIPPED_COMMENT" if len(hits) > len(live) else "RESOLVED"
        return dict(line=pick, status=st, candidates=hits)

    # 일치가 전부 주석 → 주변에서 같은 signature 의 실행 줄을 찾는다
    sig = _signature(key)
    for h in sorted(hits, key=lambda x: abs(x - hint) if hint else x):
        for d in range(1, NEIGHBOR + 1):
            for cand in (h + d, h - d):
                if not (1 <= cand <= len(new_lines)):
                    continue
                l = new_lines[cand - 1]
                if is_commented(l, path) or not l.strip():
                    continue
                if _signature(_norm(l)) == sig:
                    return dict(line=cand, status="RESOLVED_VIA_COMMENT_NEIGHBOR",
                                candidates=hits)
    return dict(line=None, status="ALL_COMMENTED", candidates=hits)


def reanchor_range(old_lines, a, b, new_lines, path="", hint=None):
    """구간 [a,b] 의 시작·끝을 각각 재앵커한다. 반환: (start, end, status)"""
    def pick(idx, h):
        i = idx
        while 1 <= i <= len(old_lines) and not old_lines[i - 1].strip():
            i += 1 if idx == a else -1          # 빈 줄이면 안쪽으로 이동
        r = find_anchor(old_lines[i - 1], new_lines, path, h)
        return r, i - idx
    ra, da = pick(a, hint)
    rb, db = pick(b, (ra["line"] or 0) + (b - a) if ra["line"] else hint)
    if ra["line"] is None or rb["line"] is None:
        return None, None, (ra["status"] if ra["line"] is None else rb["status"])
    st = "RESOLVED"
    for r in (ra, rb):
        if r["status"] != "RESOLVED":
            st = r["status"]
    return ra["line"] - da, rb["line"] - db, st
