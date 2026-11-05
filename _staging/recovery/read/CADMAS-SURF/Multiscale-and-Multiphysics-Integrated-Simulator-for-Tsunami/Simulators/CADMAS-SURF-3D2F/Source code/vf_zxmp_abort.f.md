---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/vf_zxmp_abort.f
lines: 31
sha256: d2382e4b687d851eaf7a3911a16ccc00d217e17d13d80b8dc4e51d5dc91a331c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_abort.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | 루틴·IMPLICIT·INCLUDE 및 출력 인수 설명을 포함한다. mpif.h 내부는 판독하지 않았다. MPI_ABORT를 MPI_COMM_WORLD·고정 오류 코드 77·반환 IERR로 호출한다(21–22). 나머지는 종료 레이블·RETURN·END이다. 원문(연속 표시는 같은 문장의 이어지는 행이다): `      SUBROUTINE VF_ZXMP_ABORT(IERR)` (1); `CD=== 概要 ===========================================================` (3) (개요 ); `CDT   VF_ZXMP_ABORT:MPIマスク/異常終了する` (5) (VF_ZXMP_ABORT:MPI 마스크/비정상 종료한다 ); `C==== 宣言 ===========================================================` (7) (선언 ); `C     -- 大域型 --` (9) (전역 자료형 ); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수 ); `      INCLUDE  'mpif.h'` (13); `CD    -- 引数 --` (15) (인수 ); `CD    IERR : OUT : I*4 : 完了コード` (16) (IERR : OUT : I*4 : 완료 코드 ); `C==== 実行 ===========================================================` (18) (실행 ); `C     -- MPIルーチン --` (20) (MPI 루틴 ); `      IERR2=77` (21); `      CALL MPI_ABORT(MPI_COMM_WORLD,IERR2,IERR)` (22); `C     -- 実行文の終了 --` (24) (실행문 종료 ); `      GOTO 9999` (25); `C==== 終了 ===========================================================` (27) (종료 ); ` 9999 CONTINUE` (29); `      RETURN` (30); `      END` (31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 21–22: 비정상 종료 오류 코드는 상수 77이다. 통신자(communicator)는 MPI_COMM_WORLD이다.
