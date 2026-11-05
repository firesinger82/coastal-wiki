---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_final.f
lines: 30
sha256: 2b414015ec9a25844e874eb4d9a9e712c72741aa93f72be4deda80410ea91ca0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_final.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | MPI 마스크(MPI mask) 루틴이다. MPI 실행을 종료한다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_FINAL(IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_FINAL:MPIマスク/終了する` (5) (MPI 마스크(MPI mask): MPI 실행을 종료한다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)。 `C     -- 大域変数 --` (12) (전역 변수)。 `      INCLUDE  'mpif.h'` (13)。 `CD    -- 引数 --` (15) (인수)。 `CD    IERR : OUT : I*4 : 完了コード` (16) (완료 코드)。 `C==== 実行 ===========================================================` (18) (실행)。 |
| 20–22 | 시작 시 1행 SUBROUTINE VF_ZXMG_FINAL 루틴 안. MPI_FINALIZE(IERR)를 호출하여 MPI 종료를 요청하고 완료 코드를 반환한다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (20) (MPI 루틴)。 `      CALL MPI_FINALIZE(IERR)` (21)。 |
| 23–30 | 시작 시 1행 SUBROUTINE VF_ZXMG_FINAL 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (23) (실행문 종료)。 `      GOTO 9999` (24)。 `C==== 終了 ===========================================================` (26) (종료)。 ` 9999 CONTINUE` (28)。 `      RETURN` (29)。 `      END` (30)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
