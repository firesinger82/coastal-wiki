---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_p0end.f
lines: 24
sha256: c9fd07c79e3b0d3b8eb669d363cee49f1ee3f5408571a15daccce85ac427320e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_p0end.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | 병렬 환경 정상 종료 루틴의 암시적 형식을 선언한다. 원문: `      SUBROUTINE VF_P0END()` (1). `CD=== 概要 ===========================================================` (3) (개요). `CDT   VF_P0END:並列環境を正常終了する` (5) (병렬 환경을 정상 종료한다). `C==== 宣言 ===========================================================` (7) (선언). `C     -- 大域型 --` (9) (전역 형식). `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10). `C==== 実行 ===========================================================` (12) (실행). |
| 14–24 | 시작 시 1행 루틴 `SUBROUTINE VF_P0END` 안. VF_ZXMG_FINAL(IERR)을 호출하고 반환한다. 원문: `C     -- 終了する --` (14) (종료한다). `      CALL VF_ZXMG_FINAL(IERR)` (15). `C     -- 実行文の終了 --` (17) (실행문 종료). `      GOTO 9999` (18). `C==== 終了 ===========================================================` (20) (종료). ` 9999 CONTINUE` (22). `      RETURN` (23). `      END` (24). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
