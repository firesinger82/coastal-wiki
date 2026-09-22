r"""설치 트리의 dirty 상태를 원인별로 가른다 (DESIGN failure mode 35, 2026-09-22).

migration apply 스크립트는 사전조건으로 `git status --porcelain` 이 비어 있기를 요구한다.
그런데 **체크아웃 필터 때문에 dirty 로 보이는 저장소**가 있다. 그 트리는 손상된 것도
사람이 수정한 것도 아니다 — 필터가 적용된 정상 상태다.

실측(`models/ADCIRC/raw/source_code/adcirc-testsuite`, 2026-09-22): 776 파일이 modified.

| 원인 | 판별 | 예 |
|---|---|---|
| LFS smudge | HEAD blob 이 `version https://git-lfs…` 포인터인데 작업파일은 실체 | `hrrr.222.nc` (포인터 131 B ↔ 실체 408 KB) |
| EOL 정규화 | CRLF↔LF 만 다르다 | `README.md`(HEAD LF ↔ 작업트리 CRLF) |
| 실제 수정 | 위 둘로 설명되지 않는다 | 사람·도구가 고친 것 |

**실제 수정이 하나라도 있으면 migration 을 막는다.** 나머지 둘은 통과시킨다.
`git status` 가 비어 있기만 요구하면 LFS 저장소는 영영 migration 할 수 없고,
반대로 dirty 를 무시하면 사람의 수정을 덮어쓴다.

사용:
    python3 tree_state.py <repo_path>          # 요약 + exit 0(통과) / 1(실제 수정 있음)
    python3 tree_state.py <repo_path> --list   # 실제 수정 목록도 출력
"""
import subprocess
import sys
from pathlib import Path

LFS_MAGIC = b"version https://git-lfs.github.com/spec/v1"


def _git(repo, *args, binary=True):
    r = subprocess.run(["git", "-c", "safe.directory=*", "-C", str(repo), *args],
                       capture_output=True)
    return r.stdout if binary else r.stdout.decode("utf-8", "replace")


def modified_paths(repo):
    """worktree 가 HEAD 와 다른 추적 파일 경로. rename/untracked 는 제외한다."""
    out = _git(repo, "status", "--porcelain", "-z")
    paths = []
    for entry in out.split(b"\0"):
        if len(entry) < 4:
            continue
        code, p = entry[:2], entry[3:].decode("utf-8", "replace")
        if b"?" in code or b"R" in code:
            continue
        paths.append(p)
    return paths


def classify(repo, path):
    """LFS_SMUDGED / EOL_NORMALIZED / REAL_MODIFICATION / MISSING"""
    head = _git(repo, "show", f"HEAD:{path}")
    f = Path(repo)/path
    if not f.is_file():
        return "MISSING"
    work = f.read_bytes()
    if head.startswith(LFS_MAGIC) and not work.startswith(LFS_MAGIC):
        return "LFS_SMUDGED"
    if head.replace(b"\r\n", b"\n") == work.replace(b"\r\n", b"\n"):
        return "EOL_NORMALIZED"
    return "REAL_MODIFICATION"


def check(repo, show_list=False):
    paths = modified_paths(repo)
    counts = {}
    real = []
    for p in paths:
        c = classify(repo, p)
        counts[c] = counts.get(c, 0) + 1
        if c in ("REAL_MODIFICATION", "MISSING"):
            real.append((c, p))
    print(f"[tree-state] {repo}")
    print(f"  modified {len(paths)} → " +
          " · ".join(f"{k} {v}" for k, v in sorted(counts.items())) if paths
          else "  clean")
    if real:
        print(f"  ✗ 실제 수정 {len(real)}건 — migration 사전조건 위반")
        if show_list:
            for c, p in real[:40]:
                print(f"    {c}  {p}")
        return 1
    print("  OK: 필터(LFS·EOL)로 설명되는 dirty 뿐 — migration 가능")
    return 0


def main(argv):
    if len(argv) < 2:
        print(__doc__)
        return 2
    return check(argv[1], "--list" in argv[2:])


if __name__ == "__main__":
    sys.exit(main(sys.argv))
