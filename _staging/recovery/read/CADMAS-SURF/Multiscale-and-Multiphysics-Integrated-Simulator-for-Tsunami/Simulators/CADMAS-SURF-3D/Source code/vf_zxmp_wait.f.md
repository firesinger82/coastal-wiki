---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_wait.f
lines: 34
sha256: dee8b30fc6805140e81cfd13be082621bdcc6d0e5ae14ac172b9d29597d06db6
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_wait.f — 판독 구간 기록

구간은 1행부터 34행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | 요청 완료 대기 래퍼의 개요·암시적 자료형·mpif.h·인수를 선언한다. 지역 상태 배열(status array)의 범위는 MPI_STATUS_SIZE이다. 원문: `      SUBROUTINE VF_ZXMP_WAIT(IREQ,IERR)` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_ZXMP_WAIT:MPIマスク/リクエストが終了するまで待つ(MGと同じ)` (5) (VF_ZXMP_WAIT: MPI 마스크/요청 종료까지 대기(MG와 동일)); `C==== 宣言 ===========================================================` (7) (선언); `C     -- 大域型 --` (9) (전역 자료형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수); `      INCLUDE 'mpif.h'` (13); `CD    -- 引数 --` (15) (인수); `CD    IREQ    : I/O : I*4 : リクエスト` (16) (요청(request)); `CD    IERR    : OUT : I*4 : 完了コード` (17) (완료 코드); `CD    -- 局所変数 --` (19) (지역 변수); `      DIMENSION ISTT(MPI_STATUS_SIZE)` (20) |
| 22–34 | 시작 시 1행 VF_ZXMP_WAIT 루틴 안이다. MPI_WAIT(IREQ,ISTT,IERR)를 호출한다(25). 종료 표지로 이동하여 반환한다. 원문: `C==== 実行 ===========================================================` (22) (실행); `C     -- MPIルーチン --` (24) (MPI 루틴); `      CALL MPI_WAIT(IREQ,ISTT,IERR)` (25); `C     -- 実行文の終了 --` (27) (실행문 종료); `      GOTO 9999` (28); `C==== 終了 ===========================================================` (30) (종료); ` 9999 CONTINUE` (32); `      RETURN` (33); `      END` (34) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 20·25–34: MPI_WAIT의 상태 ISTT는 지역 배열이다. 이 루틴은 ISTT를 호출자 인수로 반환하지 않으며 IERR 검사문도 없다.
