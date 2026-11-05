---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_split.f
lines: 34
sha256: 22f59b9789bd5b040570a08cce69154bcc959c6b22c2cc6e9802b55be71c38e7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_split.f — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | MPI 마스크(MPI mask) 루틴이다. 통신자(communicator)를 분할한다. 개요 주석은 COMM_WORLD 분할이라고 적는다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_SPLIT(ICOL,IKEY,ICOMM,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_SPLIT:MPIマスク/COMM_WORLDを分割する` (5) (MPI 마스크(MPI mask): 통신자(communicator)를 분할한다. 개요 주석은 COMM_WORLD 분할이라고 적는다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      use mod_comm,only: comm_model` (10)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11)。 `C     -- 大域変数 --` (13) (전역 변수)。 `      INCLUDE 'mpif.h'` (14)。 `CD    -- 引数 --` (16) (인수)。 `CD    ICOL  : IN  : I*4 : カラー` (17) (색상(color))。 `CD    IKEY  : IN  : I*4 : キー` (18) (키)。 `CD    ICOMM : OUT : I*4 : コミュニケータ` (19) (통신자(communicator))。 `CD    IERR  : OUT : I*4 : 完了コード` (20) (완료 코드)。 `C==== 実行 ===========================================================` (22) (실행)。 |
| 24–26 | 시작 시 1행 SUBROUTINE VF_ZXMG_SPLIT 루틴 안. MPI_COMM_SPLIT의 입력 통신자 인수는 comm_model이다. 색상 인수는 ICOL이다. 키 인수는 IKEY다. 출력 통신자 인수는 ICOMM이다. 이 구간에는 색상과 키의 처리 구현이 없다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (24) (MPI 루틴)。 `      CALL MPI_COMM_SPLIT(comm_model,ICOL,IKEY,ICOMM,IERR)` (25)。 [11-04 전수 검증 정정] |
| 27–34 | 시작 시 1행 SUBROUTINE VF_ZXMG_SPLIT 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (27) (실행문 종료)。 `      GOTO 9999` (28)。 `C==== 終了 ===========================================================` (30) (종료)。 ` 9999 CONTINUE` (32)。 `      RETURN` (33)。 `      END` (34)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 5·25: 개요 주석은 COMM_WORLD를 분할한다고 적는다. 실제 MPI_COMM_SPLIT의 입력 통신자는 comm_model이다.
