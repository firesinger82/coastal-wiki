---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_allsmi.f
lines: 35
sha256: 823b9e19275b203cd2830e0086e72ad1b9a63074bfabda1fdc0d8c11eec20857
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_allsmi.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | MPI 마스크(MPI mask) 루틴이다. 정수 데이터의 총합을 구한다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMP_ALLSMI(ISEND,IRECV,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMP_ALLSMI:MPIマスク/データの総和を求める/整数` (5) (MPI 마스크(MPI mask): 정수 데이터의 총합을 구한다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)。 `C     -- 大域変数 --` (12) (전역 변수)。 `      INCLUDE 'mpif.h'` (13)。 `      INCLUDE 'VF_A0PRM.h'` (14)。 `      INCLUDE 'VF_APARAI.h'` (15)。 `CD    -- 引数 --` (17) (인수)。 `CD    ISEND : IN  : I*4 : 送信するデータ` (18) (송신 데이터)。 `CD    IRECV : OUT : I*4 : データの総和` (19) (데이터의 합계)。 `CD    IERR  : OUT : I*4 : 完了コード` (20) (완료 코드)。 `C==== 実行 ===========================================================` (22) (실행)。 |
| 24–27 | 시작 시 1행 SUBROUTINE VF_ZXMP_ALLSMI 루틴 안. MPI_ALLREDUCE는 ISEND에서 IRECV로 원소 1개, MPI_INTEGER, MPI_SUM을 사용한다. 통신자(communicator)는 MGCOMM이다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (24) (MPI 루틴)。 `      CALL MPI_ALLREDUCE(ISEND,IRECV,1,MPI_INTEGER,MPI_SUM,` (25)<br>`     &                   MGCOMM,IERR)` (26)。 |
| 28–35 | 시작 시 1행 SUBROUTINE VF_ZXMP_ALLSMI 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (28) (실행문 종료)。 `      GOTO 9999` (29)。 `C==== 終了 ===========================================================` (31) (종료)。 ` 9999 CONTINUE` (33)。 `      RETURN` (34)。 `      END` (35)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
