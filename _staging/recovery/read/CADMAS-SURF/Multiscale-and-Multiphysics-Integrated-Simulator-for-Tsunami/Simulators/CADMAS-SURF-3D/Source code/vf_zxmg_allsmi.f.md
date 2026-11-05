---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_allsmi.f
lines: 34
sha256: 639b850043a22ca35a14bd6361ec03a483d75941abe008f9eef01eeb1a7a95ab
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_allsmi.f — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–22 | MPI 마스크(MPI mask) 루틴이다. 정수 데이터의 총합을 구한다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_ALLSMI(ISEND,IRECV,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_ALLSMI:MPIマスク/データの総和を求める/整数` (5) (MPI 마스크(MPI mask): 정수 데이터의 총합을 구한다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      use mod_comm,only: comm_model` (10)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11)。 `C     -- 大域変数 --` (13) (전역 변수)。 `      INCLUDE 'mpif.h'` (14)。 `CD    -- 引数 --` (16) (인수)。 `CD    ISEND : IN  : I*4 : 送信するデータ` (17) (송신 데이터)。 `CD    IRECV : OUT : I*4 : データの総和` (18) (데이터의 합계)。 `CD    IERR  : OUT : I*4 : 完了コード` (19) (완료 코드)。 `C==== 実行 ===========================================================` (21) (실행)。 |
| 23–26 | 시작 시 1행 SUBROUTINE VF_ZXMG_ALLSMI 루틴 안. mod_comm의 comm_model을 사용한다. MPI_ALLREDUCE는 ISEND에서 IRECV로 원소 1개, MPI_INTEGER 형식, MPI_SUM 연산을 수행한다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (23) (MPI 루틴)。 `      CALL MPI_ALLREDUCE(ISEND,IRECV,1,MPI_INTEGER,MPI_SUM,` (24)<br>`     &                   comm_model,IERR)` (25)。 |
| 27–34 | 시작 시 1행 SUBROUTINE VF_ZXMG_ALLSMI 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (27) (실행문 종료)。 `      GOTO 9999` (28)。 `C==== 終了 ===========================================================` (30) (종료)。 ` 9999 CONTINUE` (32)。 `      RETURN` (33)。 `      END` (34)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
