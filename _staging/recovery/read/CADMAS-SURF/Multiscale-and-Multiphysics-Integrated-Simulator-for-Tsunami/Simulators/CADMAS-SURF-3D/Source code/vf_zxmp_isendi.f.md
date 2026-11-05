---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_isendi.f
lines: 37
sha256: e304adfdc0ff7f5d42f912c69452b99adbfc09f165150249205c18fe4e547da2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_isendi.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 정수 비차단 송신 래퍼의 개요·암시적 자료형·포함 파일·IBUF(N) 인수를 선언한다. 원문: `      SUBROUTINE VF_ZXMP_ISENDI(IBUF,N,IDEST,IREQ,IERR)` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_ZXMP_ISENDI:MPIマスク/1対1非ブロッキング送信/整数` (5) (VF_ZXMP_ISENDI: MPI 마스크/일대일 비차단(nonblocking) 정수 송신); `C==== 宣言 ===========================================================` (7) (선언); `C     -- 大域型 --` (9) (전역 자료형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수); `      INCLUDE 'mpif.h'` (13); `      INCLUDE 'VF_A0PRM.h'` (14); `      INCLUDE 'VF_APARAI.h'` (15); `CD    -- 引数 --` (17) (인수); `CD    IBUF(N) : IN  : I*4 : 送信するデータ` (18) (송신할 데이터); `CD    N       : IN  : I*4 : データの要素数` (19) (데이터 원소 수); `CD    IDEST   : IN  : I*4 : 送信先のランク` (20) (송신 대상 순위(rank)); `CD    IREQ    : OUT : I*4 : リクエスト` (21) (요청(request)); `CD    IERR    : OUT : I*4 : 完了コード` (22) (완료 코드); `      DIMENSION IBUF(N)` (23) |
| 25–37 | 시작 시 1행 VF_ZXMP_ISENDI 루틴 안이다. MPI_ISEND로 정수 N개를 MGCOMM의 IDEST에 태그 0으로 송신 등록하고 반환한다(28). 원문: `C==== 実行 ===========================================================` (25) (실행); `C     -- MPIルーチン --` (27) (MPI 루틴); `      CALL MPI_ISEND(IBUF,N,MPI_INTEGER,IDEST,0,MGCOMM,IREQ,IERR)` (28); `C     -- 実行文の終了 --` (30) (실행문 종료); `      GOTO 9999` (31); `C==== 終了 ===========================================================` (33) (종료); ` 9999 CONTINUE` (35); `      RETURN` (36); `      END` (37) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28: 송신 태그는 상수 0이다. 이 루틴은 MPI_ISEND의 IERR를 검사하지 않고 반환한다.
