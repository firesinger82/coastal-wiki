---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_abort.f
lines: 31
sha256: aca726d77c9d44e13d6e4e779693b29ae74d1772be65190bc41f795004587adb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_abort.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | MPI 마스크(MPI mask) 루틴이다. 22행의 `CALL MPI_ABORT(MPI_COMM_WORLD,IERR2,IERR)`는 MPI_COMM_WORLD를 통신자 인수로 넘긴다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_ABORT(IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_ABORT:MPIマスク/異常終了する` (5) (MPI 마스크: 비정상 종료한다)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)。 `C     -- 大域変数 --` (12) (전역 변수)。 `      INCLUDE  'mpif.h'` (13)。 `CD    -- 引数 --` (15) (인수)。 `CD    IERR : OUT : I*4 : 完了コード` (16) (완료 코드)。 `C==== 実行 ===========================================================` (18) (실행)。 [11-04 전수 검증 정정] |
| 20–23 | 시작 시 1행 SUBROUTINE VF_ZXMG_ABORT 루틴 안. IERR2=77로 오류 번호를 설정한다. MPI_ABORT는 MPI_COMM_WORLD와 IERR2, 완료 코드 IERR를 인수로 받는다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (20) (MPI 루틴)。 `      IERR2=77` (21)。 `      CALL MPI_ABORT(MPI_COMM_WORLD,IERR2,IERR)` (22)。 |
| 24–31 | 시작 시 1행 SUBROUTINE VF_ZXMG_ABORT 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (24) (실행문 종료)。 `      GOTO 9999` (25)。 `C==== 終了 ===========================================================` (27) (종료)。 ` 9999 CONTINUE` (29)。 `      RETURN` (30)。 `      END` (31)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21–22: 비정상 종료 오류 번호는 77로 고정되어 있다. 종료 통신자는 MPI_COMM_WORLD다.
