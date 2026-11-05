---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_irecvi.f
lines: 37
sha256: e6a2f2837bc9aa10585b23841784a386cad1976ef38f04b59dcb29b0959d7d12
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_irecvi.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | MPI 마스크(MPI mask) 루틴이다. 일대일 비차단 수신(nonblocking receive)으로 정수 데이터를 받는다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_IRECVI(IBUF,N,ISRC,IREQ,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_IRECVI:MPIマスク/1対1非ブロッキング受信/整数` (5) (MPI 마스크(MPI mask): 일대일 비차단 수신(nonblocking receive)으로 정수 데이터를 받는다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      use mod_comm,only: comm_model` (10)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11)。 `C     -- 大域変数 --` (13) (전역 변수)。 `      INCLUDE 'mpif.h'` (14)。 `CD    -- 引数 --` (16) (인수)。 `CD    IBUF(N) : OUT : I*4 : 受信するデータ` (17) (수신 데이터)。 `CD    N       : IN  : I*4 : データの要素数` (18) (데이터 원소 수)。 `CD    ISRC    : IN  : I*4 : 送信元のランク` (19) (송신원 순위(rank))。 `CD    IREQ    : OUT : I*4 : リクエスト` (20) (요청(request))。 `CD    IERR    : OUT : I*4 : 完了コード` (21) (완료 코드)。 `      DIMENSION IBUF(N)` (22)。 `C==== 実行 ===========================================================` (24) (실행)。 |
| 26–29 | 시작 시 1행 SUBROUTINE VF_ZXMG_IRECVI 루틴 안. mod_comm의 comm_model을 사용한다. MPI_IRECV의 수신 버퍼 인수는 IBUF다. 원소 수 인수는 N이다. 자료형 인수는 MPI_INTEGER이다. 송신원 인수는 ISRC다. 이 호출문만으로 실제 수신 원소 수를 확정하지 않는다. 태그(tag)는 0이며 IREQ와 IERR를 반환한다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (26) (MPI 루틴)。 `      CALL MPI_IRECV(IBUF,N,MPI_INTEGER,ISRC,0,` (27)<br>`     &               comm_model,IREQ,IERR)` (28)。 [11-04 전수 검증 정정] |
| 30–37 | 시작 시 1행 SUBROUTINE VF_ZXMG_IRECVI 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (30) (실행문 종료)。 `      GOTO 9999` (31)。 `C==== 終了 ===========================================================` (33) (종료)。 ` 9999 CONTINUE` (35)。 `      RETURN` (36)。 `      END` (37)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–28: MPI_IRECV의 메시지 태그는 0으로 고정되어 있다.
