---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_scattervd.f
lines: 44
sha256: e0ce9fbab1908a573665cb2c54e54ac5bf3763f4a8d1b1e21458097f1b4d707c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_scattervd.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–29 | 가변 길이 분배(scatter) 래퍼의 입구는 1–2행 연속 문장이다. DSEND(NDIM)·NDATA(NP)·NDISP(NP)·DRECV(ISIZE)를 선언한다. 주석의 인수명도 아래에 그대로 인용한다. 원문: `      SUBROUTINE VF_ZXMP_SCATTERVD(DSEND,NDIM,NDATA,NDISP,NP,` (1); `     $                             DRECV,ISIZE,IERR)` (2); `CD=== 概要 ===========================================================` (4) (개요); `CDT   VF_ZXMP_SCATTERVD: 可変長の実数型データを0番PEから配る` (6) (VF_ZXMP_SCATTERVD: 가변 길이 실수형 데이터를 0번 처리 요소(processing element)에서 분배); `C==== 宣言 ===========================================================` (8) (선언); `C     -- 大域型 --` (10) (전역 자료형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11); `C     -- 大域変数 --` (13) (전역 변수); `      INCLUDE 'mpif.h'` (14); `      INCLUDE 'VF_A0PRM.h'` (15); `      INCLUDE 'VF_APARAI.h'` (16); `CD    -- 引数 --` (18) (인수); `CD    ISEND : IN  : R*8 : 送信するデータ` (19) (송신할 데이터); `CD    IRECV : OUT : R*8 : データの最小値` (20) (데이터 최솟값); `CD    IERR  : OUT : I*4 : 完了コード` (21) (완료 코드); `      INTEGER NDIM,NP` (23); `      DOUBLE PRECISION DSEND(NDIM)` (24); `      INTEGER NDATA(NP)` (25); `      INTEGER NDISP(NP)` (26); `      INTEGER ISIZE` (27); `      DOUBLE PRECISION DRECV(ISIZE)` (28) |
| 30–44 | 시작 시 1행 VF_ZXMP_SCATTERVD 루틴 안이다. MPI_SCATTERV의 33–35행은 하나의 연속 호출이다. 송신 개수 NDATA·변위 NDISP를 사용하여 MGCOMM의 루트(root) 0에서 배정밀도 자료를 분배한다. 수신 개수는 ISIZE이다. 반환 절차가 이어진다. 원문: `C==== 実行 ===========================================================` (30) (실행); `C     -- MPIルーチン --` (32) (MPI 루틴); `      CALL MPI_SCATTERV(DSEND,NDATA,NDISP,MPI_DOUBLE_PRECISION,` (33); `     &                 DRECV,ISIZE,MPI_DOUBLE_PRECISION,` (34); `     &                 0,MGCOMM,IERR)` (35); `C     -- 実行文の終了 --` (37) (실행문 종료); `      GOTO 9999` (38); `C==== 終了 ===========================================================` (40) (종료); ` 9999 CONTINUE` (42); `      RETURN` (43); `      END` (44) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–20 및 1–2·24–28: 인수 주석은 ISEND·IRECV를 쓰지만 실제 인수명은 DSEND·DRECV이다. IRECV 주석은 데이터 최솟값이라고 적는다.
- 33–35: MPI_SCATTERV의 루트는 상수 0이다. 이 루틴에는 IERR 검사문이 없다.
