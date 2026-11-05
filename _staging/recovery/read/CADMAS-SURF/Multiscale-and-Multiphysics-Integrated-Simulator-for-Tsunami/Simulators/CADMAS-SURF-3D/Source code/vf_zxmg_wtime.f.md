---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmg_wtime.f
lines: 30
sha256: 3736abe3a97be392f2167183cbdd2ba0b410d981be3943defba2365dba459c39
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmg_wtime.f — 판독 구간 기록

구간은 1행부터 30행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | MPI 마스크(MPI mask) 루틴이다. 경과시간(elapsed time)을 얻는다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMG_WTIME(PT)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMG_WTIME:MPIマスク/経過時間を得る` (5) (MPI 마스크(MPI mask): 경과시간(elapsed time)을 얻는다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)。 `C     -- 大域変数 --` (12) (전역 변수)。 `      INCLUDE  'mpif.h'` (13)。 `CD    -- 引数 --` (15) (인수)。 `CD    PT : OUT : R*8 : 経過時間` (16) (경과시간)。 `C==== 実行 ===========================================================` (18) (실행)。 |
| 20–22 | 시작 시 1행 SUBROUTINE VF_ZXMG_WTIME 루틴 안. PT=MPI_WTIME()로 시간을 출력 인수 PT에 저장한다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (20) (MPI 루틴)。 `      PT=MPI_WTIME()` (21)。 |
| 23–30 | 시작 시 1행 SUBROUTINE VF_ZXMG_WTIME 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (23) (실행문 종료)。 `      GOTO 9999` (24)。 `C==== 終了 ===========================================================` (26) (종료)。 ` 9999 CONTINUE` (28)。 `      RETURN` (29)。 `      END` (30)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
