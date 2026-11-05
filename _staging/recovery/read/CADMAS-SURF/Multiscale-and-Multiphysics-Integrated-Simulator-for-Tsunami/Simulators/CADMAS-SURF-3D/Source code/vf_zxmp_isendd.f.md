---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_isendd.f
lines: 38
sha256: d1b7bde22d17944a9ecd8ca6ff37d3935cb2c7313045e06b49b398ec44ca9a57
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_isendd.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 배정밀도(double precision) 비차단 송신 래퍼의 선언부이다. DBUF(N)와 송신 대상 IDEST·요청 IREQ·완료 코드 IERR를 사용한다. 원문: `      SUBROUTINE VF_ZXMP_ISENDD(DBUF,N,IDEST,IREQ,IERR)` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_ZXMP_ISENDD:MPIマスク/1対1非ブロッキング送信/実数` (5) (VF_ZXMP_ISENDD: MPI 마스크/일대일 비차단(nonblocking) 실수 송신); `C==== 宣言 ===========================================================` (7) (선언); `C     -- 大域型 --` (9) (전역 자료형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수); `      INCLUDE 'mpif.h'` (13); `      INCLUDE 'VF_A0PRM.h'` (14); `      INCLUDE 'VF_APARAI.h'` (15); `CD    -- 引数 --` (17) (인수); `CD    DBUF(N) : IN  : R*8 : 送信するデータ` (18) (송신할 데이터); `CD    N       : IN  : I*4 : データの要素数` (19) (데이터 원소 수); `CD    IDEST   : IN  : I*4 : 送信先のランク` (20) (송신 대상 순위(rank)); `CD    IREQ    : OUT : I*4 : リクエスト` (21) (요청(request)); `CD    IERR    : OUT : I*4 : 完了コード` (22) (완료 코드); `      DIMENSION DBUF(N)` (23) |
| 25–38 | 시작 시 1행 VF_ZXMP_ISENDD 루틴 안이다. MPI_ISEND 호출은 28–29행이 하나의 고정형식 연속 문장이다. MGCOMM에서 DBUF의 N개 배정밀도 값을 IDEST로 태그 0으로 송신 등록한다. 이후 반환한다. 원문: `C==== 実行 ===========================================================` (25) (실행); `C     -- MPIルーチン --` (27) (MPI 루틴); `      CALL MPI_ISEND(DBUF,N,MPI_DOUBLE_PRECISION,IDEST,0,` (28); `     &               MGCOMM,IREQ,IERR)` (29); `C     -- 実行文の終了 --` (31) (실행문 종료); `      GOTO 9999` (32); `C==== 終了 ===========================================================` (34) (종료); ` 9999 CONTINUE` (36); `      RETURN` (37); `      END` (38) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28–29: 송신 태그는 상수 0이다. 이 루틴은 MPI_ISEND의 IERR를 검사하지 않고 반환한다.
