---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_crank.f
lines: 32
sha256: 585c22508739ae1a36bab1cbfb3b68b4a09dcc2933b557707a4c0614bbff9b46
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_crank.f — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | MPI 마스크(MPI mask) 루틴이다. 자신의 프로세스 순위(rank)를 얻는다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_CRANK(MGRANK,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_CRANK:MPIマスク/自分のランクを得る` (5) (MPI 마스크(MPI mask): 자신의 프로세스 순위(rank)를 얻는다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      use mod_comm,only: comm_model` (10)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11)。 `C     -- 大域変数 --` (13) (전역 변수)。 `      INCLUDE  'mpif.h'` (14)。 `CD    -- 引数 --` (16) (인수)。 `CD    MGRANK : OUT : I*4 : 自分のランク` (17) (자신의 순위)。 `CD    IERR   : OUT : I*4 : 完了コード` (18) (완료 코드)。 `C==== 実行 ===========================================================` (20) (실행)。 |
| 22–24 | 시작 시 1행 SUBROUTINE VF_ZXMG_CRANK 루틴 안. mod_comm의 comm_model을 사용한다. MPI_COMM_RANK가 MGRANK와 완료 코드 IERR를 반환한다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (22) (MPI 루틴)。 `      CALL MPI_COMM_RANK(comm_model,MGRANK,IERR)` (23)。 |
| 25–32 | 시작 시 1행 SUBROUTINE VF_ZXMG_CRANK 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (25) (실행문 종료)。 `      GOTO 9999` (26)。 `C==== 終了 ===========================================================` (28) (종료)。 ` 9999 CONTINUE` (30)。 `      RETURN` (31)。 `      END` (32)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
