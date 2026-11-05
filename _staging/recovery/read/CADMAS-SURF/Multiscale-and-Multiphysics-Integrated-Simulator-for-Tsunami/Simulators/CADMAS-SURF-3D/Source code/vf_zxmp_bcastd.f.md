---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_bcastd.f
lines: 36
sha256: 476d2122e98f14bb7a43ba2caa9dff57d30fb1a81553d22000718e9716d84cad
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_bcastd.f — 판독 구간 기록

구간은 1행부터 36행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | MPI 마스크(MPI mask) 루틴이다. IROOT에서 다른 프로세스로 배정밀도 실수 데이터를 배포한다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMP_BCASTD(BUF,N,IROOT,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMP_BCASTD:MPIマスク/irootからその他へ送信する/実数` (5) (MPI 마스크(MPI mask): IROOT에서 다른 프로세스로 배정밀도 실수 데이터를 배포한다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)。 `C     -- 大域変数 --` (12) (전역 변수)。 `      INCLUDE 'mpif.h'` (13)。 `      INCLUDE 'VF_A0PRM.h'` (14)。 `      INCLUDE 'VF_APARAI.h'` (15)。 `CD    -- 引数 --` (17) (인수)。 `CD    BUF(N)  : I/O : R*8 : 送信・受信するデータ` (18) (송수신 데이터)。 `CD    N       : IN  : I*4 : データの要素数` (19) (데이터 원소 수)。 `CD    IROOT   : IN  : I*4 : 送信元のランク` (20) (송신원 순위(rank))。 `CD    IERR    : OUT : I*4 : 完了コード` (21) (완료 코드)。 `      DIMENSION BUF(N)` (22)。 `C==== 実行 ===========================================================` (24) (실행)。 |
| 26–28 | 시작 시 1행 SUBROUTINE VF_ZXMP_BCASTD 루틴 안. MPI_BCAST는 BUF(N)의 N개 원소를 MPI_DOUBLE_PRECISION 형식으로 배포한다. 통신자(communicator)는 MGCOMM이며 송신원은 IROOT다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (26) (MPI 루틴)。 `      CALL MPI_BCAST(BUF,N,MPI_DOUBLE_PRECISION,IROOT,MGCOMM,IERR)` (27)。 |
| 29–36 | 시작 시 1행 SUBROUTINE VF_ZXMP_BCASTD 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (29) (실행문 종료)。 `      GOTO 9999` (30)。 `C==== 終了 ===========================================================` (32) (종료)。 ` 9999 CONTINUE` (34)。 `      RETURN` (35)。 `      END` (36)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
