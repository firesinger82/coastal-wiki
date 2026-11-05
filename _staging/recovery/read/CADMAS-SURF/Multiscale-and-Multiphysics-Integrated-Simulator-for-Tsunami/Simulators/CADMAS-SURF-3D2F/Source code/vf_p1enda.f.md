---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_p1enda.f
lines: 27
sha256: 89a875727b66305dde89f17c43e169184cb515a9a132c428484b477916294fa0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_p1enda.f — 판독 구간 기록

구간은 1행부터 27행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | 병렬 환경 비정상 종료 루틴 VF_P1ENDA다(5). 개요·선언·대역형·실행·종료 주석을 포함한다. 비정상 종료 주석 아래 VF_ZXMP_ABORT(IERR)을 호출한다(14–15). 그 다음 종료 주석 아래 VF_ZXMP_FINAL(IERR)을 호출한다(17–18). 실행문 종료·RETURN·END다(20–27). 원문: `      SUBROUTINE VF_P1ENDA()` (1) / `CD=== 概要 ===========================================================` (개요) (3) / `CDT   VF_P1ENDA:並列環境を異常終了する` (병렬 환경 비정상 종료) (5) / `C==== 宣言 ===========================================================` (선언) (7) / `C     -- 大域型 --` (대역형) (9) / `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10) / `C==== 実行 ===========================================================` (실행) (12) / `C     -- 異常終了する --` (비정상 종료함) (14) / `      CALL VF_ZXMP_ABORT(IERR)` (15) / `C     -- 終了する --` (종료함) (17) / `      CALL VF_ZXMP_FINAL(IERR)` (18) / `C     -- 実行文の終了 --` (실행문 종료) (20) / `      GOTO 9999` (21) / `C==== 終了 ===========================================================` (종료) (23) / ` 9999 CONTINUE` (25) / `      RETURN` (26) / `      END` (27) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–18: VF_ZXMP_ABORT 다음 실행문은 VF_ZXMP_FINAL 호출이다. 호출 대상 내부의 반환 여부는 이 파일 판독에서 확인하지 않았다.
