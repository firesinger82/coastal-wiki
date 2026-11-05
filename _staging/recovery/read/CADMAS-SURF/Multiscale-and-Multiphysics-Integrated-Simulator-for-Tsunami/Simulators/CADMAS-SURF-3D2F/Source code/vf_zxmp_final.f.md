---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_zxmp_final.f
lines: 30
sha256: 490399d2411a8f84e36b4b9c21d4ee64d4fc28bb933891e08910216ef97d799c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_final.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | 루틴·IMPLICIT·INCLUDE 및 출력 인수 설명을 포함한다. mpif.h 내부는 판독하지 않았다. MPI_FINALIZE(IERR)를 호출한다(21). 나머지는 종료 레이블·RETURN·END이다. 원문(연속 표시는 같은 문장의 이어지는 행이다): `      SUBROUTINE VF_ZXMP_FINAL(IERR)` (1); `CD=== 概要 ===========================================================` (3) (개요 ); `CDT   VF_ZXMP_FINAL:MPIマスク/終了する` (5) (VF_ZXMP_FINAL:MPI 마스크/종료한다 ); `C==== 宣言 ===========================================================` (7) (선언 ); `C     -- 大域型 --` (9) (전역 자료형 ); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수 ); `      INCLUDE  'mpif.h'` (13); `CD    -- 引数 --` (15) (인수 ); `CD    IERR : OUT : I*4 : 完了コード` (16) (IERR : OUT : I*4 : 완료 코드 ); `C==== 実行 ===========================================================` (18) (실행 ); `C     -- MPIルーチン --` (20) (MPI 루틴 ); `      CALL MPI_FINALIZE(IERR)` (21); `C     -- 実行文の終了 --` (23) (실행문 종료 ); `      GOTO 9999` (24); `C==== 終了 ===========================================================` (26) (종료 ); ` 9999 CONTINUE` (28); `      RETURN` (29); `      END` (30). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
