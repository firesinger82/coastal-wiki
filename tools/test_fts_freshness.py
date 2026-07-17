#!/usr/bin/env python3
"""test_fts_freshness.py — FTS 인덱스 신선도 회귀 (Codex 22회차: indexed_git_sha).

검증: ① 훼손된 indexed_git_sha → ensure_index() 가 재빌드해 sha==HEAD 복귀
      ② meta 테이블 없는 구 스키마 DB → 자동 재빌드 (자가치유 경로 유지)
      ③ fresh 상태에서는 ensure_index() 가 재빌드하지 않음 (mtime 불변)
"""
import importlib.util
import os
import sqlite3
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
spec = importlib.util.spec_from_file_location(
    "fx", os.path.join(HERE, "llm-wiki-poc", "fts5_index.py"))
fx = importlib.util.module_from_spec(spec)
spec.loader.exec_module(fx)

failures = []


def check(name, cond, detail=""):
    if cond:
        print(f"  PASS  {name}")
    else:
        print(f"  FAIL  {name}  {detail}")
        failures.append(name)


def main():
    head = fx._git_head()
    check("git HEAD readable", bool(head), "git rev-parse HEAD 실패")

    # 기준 상태: 최신 빌드
    fx.build()
    check("build records HEAD sha", fx._indexed_sha() == head,
          f"indexed={fx._indexed_sha()!r} head={head!r}")

    # ① sha 훼손 → 재빌드
    con = sqlite3.connect(fx.DB)
    con.execute("UPDATE meta SET value='stale-sha' WHERE key='indexed_git_sha'")
    con.commit()
    con.close()
    check("tamper visible", fx._indexed_sha() == "stale-sha")
    fx.ensure_index()
    check("stale sha → rebuild to HEAD", fx._indexed_sha() == head,
          f"indexed={fx._indexed_sha()!r}")

    # ② 구 스키마 (meta 테이블 없음) → 자동 재빌드
    con = sqlite3.connect(fx.DB)
    con.execute("DROP TABLE meta")
    con.commit()
    con.close()
    check("old schema detected", not fx._schema_current())
    fx.ensure_index()
    check("old schema → rebuild", fx._schema_current() and fx._indexed_sha() == head)

    # ③ fresh → no rebuild (DB mtime 불변)
    mtime = fx.DB.stat().st_mtime_ns
    fx.ensure_index()
    check("fresh → no rebuild", fx.DB.stat().st_mtime_ns == mtime)

    # manifest_stats 가 sha 를 노출
    check("manifest_stats exposes indexed_git_sha",
          fx.manifest_stats().get("indexed_git_sha") == head)

    print()
    if failures:
        print(f"FAIL: {len(failures)} case(s): {', '.join(failures)}")
        return 1
    print("OK: fts freshness 회귀 전부 통과")
    return 0


if __name__ == "__main__":
    sys.exit(main())
