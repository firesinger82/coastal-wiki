---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_csize.f
lines: 33
sha256: bedc1feebb6f93485627b40a0d5132959713bcdd5104642f2fd81d0dc5974881
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_csize.f — 판독 구간 기록

구간은 1행부터 33행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | MPI 마스크(MPI mask) 루틴이다. 통신자에 속한 프로세스 수를 얻는다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMP_CSIZE(IOPROC,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMP_CSIZE:MPIマスク/プロセス数を得る` (5) (MPI 마스크(MPI mask): 통신자에 속한 프로세스 수를 얻는다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)。 `C     -- 大域変数 --` (12) (전역 변수)。 `      INCLUDE 'mpif.h'` (13)。 `      INCLUDE 'VF_A0PRM.h'` (14)。 `      INCLUDE 'VF_APARAI.h'` (15)。 `CD    -- 引数 --` (17) (인수)。 `CD    IOPROC : OUT : I*4 : プロセス数` (18) (프로세스 수)。 `CD    IERR   : OUT : I*4 : 完了コード` (19) (완료 코드)。 `C==== 実行 ===========================================================` (21) (실행)。 |
| 23–25 | 시작 시 1행 SUBROUTINE VF_ZXMP_CSIZE 루틴 안. MPI_COMM_SIZE는 통신자(communicator) MGCOMM에서 IOPROC와 완료 코드 IERR를 반환한다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (23) (MPI 루틴)。 `      CALL MPI_COMM_SIZE(MGCOMM,IOPROC,IERR)` (24)。 |
| 26–33 | 시작 시 1행 SUBROUTINE VF_ZXMP_CSIZE 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (26) (실행문 종료)。 `      GOTO 9999` (27)。 `C==== 終了 ===========================================================` (29) (종료)。 ` 9999 CONTINUE` (31)。 `      RETURN` (32)。 `      END` (33)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
