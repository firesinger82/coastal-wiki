---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_wait.f
lines: 34
sha256: 58380fa8b4594a2ad9cd489dede71e437f96649c7f955827dd2de9fba73ddd66
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_wait.f — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | MPI 마스크(MPI mask) 루틴이다. 요청(request)이 끝날 때까지 기다린다. 주석은 MP와 같다고 적는다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_WAIT(IREQ,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_WAIT:MPIマスク/リクエストが終了するまで待つ(MPと同じ)` (5) (MPI 마스크(MPI mask): 요청(request)이 끝날 때까지 기다린다. 주석은 MP와 같다고 적는다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)。 `C     -- 大域変数 --` (12) (전역 변수)。 `      INCLUDE 'mpif.h'` (13)。 `CD    -- 引数 --` (15) (인수)。 `CD    IREQ    : I/O : I*4 : リクエスト` (16) (요청(request))。 `CD    IERR    : OUT : I*4 : 完了コード` (17) (완료 코드)。 `CD    -- 局所変数 --` (19) (지역 변수)。 `      DIMENSION ISTT(MPI_STATUS_SIZE)` (20)。 `C==== 実行 ===========================================================` (22) (실행)。 |
| 24–26 | 시작 시 1행 SUBROUTINE VF_ZXMG_WAIT 루틴 안. 지역 상태 배열 ISTT의 범위는 MPI_STATUS_SIZE다. MPI_WAIT는 IREQ의 완료를 기다리고 ISTT·IERR를 채운다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (24) (MPI 루틴)。 `      CALL MPI_WAIT(IREQ,ISTT,IERR)` (25)。 |
| 27–34 | 시작 시 1행 SUBROUTINE VF_ZXMG_WAIT 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (27) (실행문 종료)。 `      GOTO 9999` (28)。 `C==== 終了 ===========================================================` (30) (종료)。 ` 9999 CONTINUE` (32)。 `      RETURN` (33)。 `      END` (34)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
