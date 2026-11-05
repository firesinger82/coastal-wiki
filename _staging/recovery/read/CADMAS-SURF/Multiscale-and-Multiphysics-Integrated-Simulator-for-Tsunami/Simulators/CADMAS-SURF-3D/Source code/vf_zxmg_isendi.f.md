---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_isendi.f
lines: 37
sha256: ad0fbb9e352dfe8f99f451861af99a4670f29cf99142eb0a6dc122c3b0daf642
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_isendi.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | MPI 마스크(MPI mask) 루틴이다. 일대일 비차단 송신(nonblocking send)으로 정수 데이터를 보낸다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_ISENDI(IBUF,N,IDEST,IREQ,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_ISENDI:MPIマスク/1対1非ブロッキング送信/整数` (5) (MPI 마스크(MPI mask): 일대일 비차단 송신(nonblocking send)으로 정수 데이터를 보낸다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      use mod_comm,only: comm_model` (10)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11)。 `C     -- 大域変数 --` (13) (전역 변수)。 `      INCLUDE 'mpif.h'` (14)。 `CD    -- 引数 --` (16) (인수)。 `CD    IBUF(N) : IN  : I*4 : 送信するデータ` (17) (송신 데이터)。 `CD    N       : IN  : I*4 : データの要素数` (18) (데이터 원소 수)。 `CD    IDEST   : IN  : I*4 : 送信先のランク` (19) (수신처 순위)。 `CD    IREQ    : OUT : I*4 : リクエスト` (20) (요청(request))。 `CD    IERR    : OUT : I*4 : 完了コード` (21) (완료 코드)。 `      DIMENSION IBUF(N)` (22)。 `C==== 実行 ===========================================================` (24) (실행)。 |
| 26–29 | 시작 시 1행 SUBROUTINE VF_ZXMG_ISENDI 루틴 안. mod_comm의 comm_model을 사용한다. MPI_ISEND는 IBUF(N)의 N개 MPI_INTEGER 원소를 IDEST로 보내도록 요청한다. 태그(tag)는 0이며 IREQ와 IERR를 반환한다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (26) (MPI 루틴)。 `      CALL MPI_ISEND(IBUF,N,MPI_INTEGER,IDEST,0,` (27)<br>`     &               comm_model,IREQ,IERR)` (28)。 |
| 30–37 | 시작 시 1행 SUBROUTINE VF_ZXMG_ISENDI 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (30) (실행문 종료)。 `      GOTO 9999` (31)。 `C==== 終了 ===========================================================` (33) (종료)。 ` 9999 CONTINUE` (35)。 `      RETURN` (36)。 `      END` (37)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 27–28: MPI_ISEND의 메시지 태그는 0으로 고정되어 있다.
