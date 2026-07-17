#!/usr/bin/env python3
"""scan-runs-feedback.py — coastal-runs 의 미처리 wiki_feedback 스캐너 (§3.3).

coastal-runs/observations/<host>/*.md frontmatter 의 wiki_feedback id 를 모아
위키 원장(_staging/runs-feedback/ledger.yml)의 feedback_id 와 대조, **원장에
없는 id 만** 출력한다. 무상태 report-only(항상 exit 0; 사용 오류만 exit 2) —
처리 기록은 원장에만 남기고 원 observation 은 수정하지 않는다(RUNS-CHANNEL §3.3).

순수 stdlib(pyyaml 불사용 — llm-wiki-poc 와 동일 원칙): frontmatter 의
wiki_feedback 블록에서 `- id:` 줄만 regex 로 뽑는 얕은 파서. id 는 스키마상
`<host_id>-<YYYYMMDD>-<slug>-NNN` 한 줄 스칼라라 이 수준으로 충분.

사용: python3 tools/scan-runs-feedback.py [--runs-root ~/coastal-runs]
"""
import argparse
import re
import sys
from pathlib import Path

WIKI = Path(__file__).resolve().parents[1]
LEDGER = WIKI / "_staging" / "runs-feedback" / "ledger.yml"

FM = re.compile(r"^---\n(.*?)\n---\n", re.S)
# wiki_feedback: 블록(다음 최상위 키 또는 frontmatter 끝까지) 안의 "- id: <값>"
FEEDBACK_BLOCK = re.compile(r"^wiki_feedback:[^\n]*\n((?:[ \t]+\S.*\n?|[ \t]*\n)*)", re.M)  # 콜론 뒤 주석 허용(§2.2 예시와 일치 — Phase L L4 버그 수정)
ITEM_ID = re.compile(r"^[ \t]*-[ \t]+id:[ \t]*(\S+)", re.M)
LEDGER_ID = re.compile(r"^[ \t]*-[ \t]+feedback_id:[ \t]*(\S+)", re.M)


def observation_ids(runs_root: Path):
    """[(id, 파일 상대경로)] — observations/<host>/*.md 의 wiki_feedback id."""
    out = []
    obs = runs_root / "observations"
    if not obs.is_dir():
        return out
    for md in sorted(obs.glob("*/*.md")):
        m = FM.match(md.read_text(encoding="utf-8", errors="ignore"))
        if not m:
            continue
        blk = FEEDBACK_BLOCK.search(m.group(1) + "\n")
        if not blk:
            continue
        for fid in ITEM_ID.findall(blk.group(1)):
            out.append((fid.strip().strip('"').strip("'"),
                        str(md.relative_to(runs_root))))
    return out


def ledger_ids():
    if not LEDGER.is_file():
        return set()
    return {i.strip().strip('"').strip("'")
            for i in LEDGER_ID.findall(LEDGER.read_text(encoding="utf-8"))}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--runs-root", default=str(Path.home() / "coastal-runs"),
                    help="coastal-runs clone 경로 (기본 ~/coastal-runs)")
    args = ap.parse_args(argv)

    runs_root = Path(args.runs_root).expanduser()
    if not runs_root.is_dir():
        print(f"scan-runs-feedback: coastal-runs 경로 없음: {runs_root}\n"
              f"  → --runs-root <경로> 로 지정하세요 (RUNS-CHANNEL §3.3).")
        return 2

    acked = ledger_ids()
    pending = [(fid, path) for fid, path in observation_ids(runs_root)
               if fid not in acked]

    if not pending:
        print(f"scan-runs-feedback: 미처리 wiki_feedback 없음 "
              f"(원장 ack {len(acked)}건, root={runs_root})")
        return 0
    print(f"scan-runs-feedback: 미처리 wiki_feedback {len(pending)}건 "
          f"(원장 ack {len(acked)}건) — 원장({LEDGER.relative_to(WIKI)})에 기록하세요:")
    for fid, path in pending:
        print(f"  {fid}\t{path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
