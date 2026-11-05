---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_bcasti.f
lines: 35
sha256: ce143788c944f1da559d6c1bfe9ed5c81f4d60aa473b1502cfcdde526be5219b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_bcasti.f — 판독 구간 기록

구간은 1행부터 35행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | MPI 마스크(MPI mask) 루틴이다. IROOT에서 다른 프로세스로 정수 데이터를 배포한다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_BCASTI(IBUF,N,IROOT,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_BCASTI:MPIマスク/irootからその他へ送信する/整数` (5) (MPI 마스크(MPI mask): IROOT에서 다른 프로세스로 정수 데이터를 배포한다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      use mod_comm,only: comm_model` (10)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11)。 `C     -- 大域変数 --` (13) (전역 변수)。 `      INCLUDE 'mpif.h'` (14)。 `CD    -- 引数 --` (16) (인수)。 `CD    IBUF(N) : I/O : I*4 : 送信・受信するデータ` (17) (송수신 데이터)。 `CD    N       : IN  : I*4 : データの要素数` (18) (데이터 원소 수)。 `CD    IROOT   : IN  : I*4 : 送信元のランク` (19) (송신원 순위(rank))。 `CD    IERR    : OUT : I*4 : 完了コード` (20) (완료 코드)。 `      DIMENSION IBUF(N)` (21)。 `C==== 実行 ===========================================================` (23) (실행)。 |
| 25–27 | 시작 시 1행 SUBROUTINE VF_ZXMG_BCASTI 루틴 안. mod_comm의 comm_model을 사용한다. MPI_BCAST는 IBUF(N)의 N개 원소를 MPI_INTEGER 형식으로 배포한다. 송신원은 IROOT다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (25) (MPI 루틴)。 `      CALL MPI_BCAST(IBUF,N,MPI_INTEGER,IROOT,comm_model,IERR)` (26)。 |
| 28–35 | 시작 시 1행 SUBROUTINE VF_ZXMG_BCASTI 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (28) (실행문 종료)。 `      GOTO 9999` (29)。 `C==== 終了 ===========================================================` (31) (종료)。 ` 9999 CONTINUE` (33)。 `      RETURN` (34)。 `      END` (35)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
