---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_irecvd.f
lines: 38
sha256: ca4cad7e1c784be941bdda4957c9f8952fdd43e1f583b76908d886924264f5a3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_irecvd.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | MPI 마스크(MPI mask) 루틴이다. 일대일 비차단 수신(nonblocking receive)으로 배정밀도 실수 데이터를 받는다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMP_IRECVD(DBUF,N,ISRC,IREQ,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMP_IRECVD:MPIマスク/1対1非ブロッキング受信/実数` (5) (MPI 마스크(MPI mask): 일대일 비차단 수신(nonblocking receive)으로 배정밀도 실수 데이터를 받는다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)。 `C     -- 大域変数 --` (12) (전역 변수)。 `      INCLUDE 'mpif.h'` (13)。 `      INCLUDE 'VF_A0PRM.h'` (14)。 `      INCLUDE 'VF_APARAI.h'` (15)。 `CD    -- 引数 --` (17) (인수)。 `CD    DBUF(N) : OUT : R*8 : 受信するデータ` (18) (수신 데이터)。 `CD    N       : IN  : I*4 : データの要素数` (19) (데이터 원소 수)。 `CD    ISRC    : IN  : I*4 : 送信元のランク` (20) (송신원 순위(rank))。 `CD    IREQ    : OUT : I*4 : リクエスト` (21) (요청(request))。 `CD    IERR    : OUT : I*4 : 完了コード` (22) (완료 코드)。 `      DIMENSION DBUF(N)` (23)。 `C==== 実行 ===========================================================` (25) (실행)。 |
| 27–30 | 시작 시 1행 SUBROUTINE VF_ZXMP_IRECVD 루틴 안. MPI_IRECV의 수신 버퍼 인수는 DBUF다. 원소 수 인수는 N이다. 자료형 인수는 MPI_DOUBLE_PRECISION이다. 송신원 인수는 ISRC다. 이 호출문만으로 실제 수신 원소 수를 확정하지 않는다. 메시지 태그(tag)는 0이고 통신자(communicator)는 MGCOMM이다. IREQ·IERR를 반환한다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (27) (MPI 루틴)。 `      CALL MPI_IRECV(DBUF,N,MPI_DOUBLE_PRECISION,ISRC,0,` (28)<br>`     &               MGCOMM,IREQ,IERR)` (29)。 [11-04 전수 검증 정정] |
| 31–38 | 시작 시 1행 SUBROUTINE VF_ZXMP_IRECVD 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (31) (실행문 종료)。 `      GOTO 9999` (32)。 `C==== 終了 ===========================================================` (34) (종료)。 ` 9999 CONTINUE` (36)。 `      RETURN` (37)。 `      END` (38)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–29: MPI_IRECV의 메시지 태그는 0으로 고정되어 있다.
