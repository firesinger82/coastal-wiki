---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_csize.f
lines: 32
sha256: 5c4a54bb3fb946328798aa0bcfa2468bd6f2fdf73aba3a73bd6e0b4182b8feed
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_csize.f — 판독 구간 기록

구간은 1행부터 32행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | MPI 마스크(MPI mask) 루틴이다. 통신자에 속한 프로세스 수를 얻는다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_CSIZE(MGPROC,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_CSIZE:MPIマスク/プロセス数を得る` (5) (MPI 마스크(MPI mask): 통신자에 속한 프로세스 수를 얻는다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      use mod_comm,only: comm_model` (10)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11)。 `C     -- 大域変数 --` (13) (전역 변수)。 `      INCLUDE  'mpif.h'` (14)。 `CD    -- 引数 --` (16) (인수)。 `CD    MGPROC : OUT : I*4 : プロセス数` (17) (프로세스 수)。 `CD    IERR   : OUT : I*4 : 完了コード` (18) (완료 코드)。 `C==== 実行 ===========================================================` (20) (실행)。 |
| 22–24 | 시작 시 1행 SUBROUTINE VF_ZXMG_CSIZE 루틴 안. mod_comm의 comm_model을 사용한다. MPI_COMM_SIZE가 MGPROC와 완료 코드 IERR를 반환한다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (22) (MPI 루틴)。 `      CALL MPI_COMM_SIZE(comm_model,MGPROC,IERR)` (23)。 |
| 25–32 | 시작 시 1행 SUBROUTINE VF_ZXMG_CSIZE 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (25) (실행문 종료)。 `      GOTO 9999` (26)。 `C==== 終了 ===========================================================` (28) (종료)。 ` 9999 CONTINUE` (30)。 `      RETURN` (31)。 `      END` (32)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
