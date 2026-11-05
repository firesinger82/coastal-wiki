---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_irecvi.f
lines: 37
sha256: b9b71470f8fb0ac97c210e6c1b4b575bf9a50dae653e659f0b35372cb1c6856f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_irecvi.f — 판독 구간 기록

구간은 1행부터 37행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | 정수 비차단 수신 래퍼(wrapper)의 입구·개요·암시적 자료형(implicit typing)·포함 파일·인수 배열을 선언한다. IBUF의 범위는 N이다. 원문: `      SUBROUTINE VF_ZXMP_IRECVI(IBUF,N,ISRC,IREQ,IERR)` (1); `CD=== 概要 ===========================================================` (3) (개요); `CDT   VF_ZXMP_IRECVI:MPIマスク/1対1非ブロッキング受信/整数` (5) (VF_ZXMP_IRECVI: MPI 마스크/일대일 비차단(nonblocking) 정수 수신); `C==== 宣言 ===========================================================` (7) (선언); `C     -- 大域型 --` (9) (전역 자료형); `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10); `C     -- 大域変数 --` (12) (전역 변수); `      INCLUDE 'mpif.h'` (13); `      INCLUDE 'VF_A0PRM.h'` (14); `      INCLUDE 'VF_APARAI.h'` (15); `CD    -- 引数 --` (17) (인수); `CD    IBUF(N) : OUT : I*4 : 受信するデータ` (18) (수신할 데이터); `CD    N       : IN  : I*4 : データの要素数` (19) (데이터 원소 수); `CD    ISRC    : IN  : I*4 : 送信元のランク` (20) (송신 출처 순위(rank)); `CD    IREQ    : OUT : I*4 : リクエスト` (21) (요청(request)); `CD    IERR    : OUT : I*4 : 完了コード` (22) (완료 코드); `      DIMENSION IBUF(N)` (23) |
| 25–37 | 시작 시 1행 VF_ZXMP_IRECVI 루틴 안이다. MPI_IRECV는 MGCOMM에서 ISRC의 태그(tag) 0 메시지를 받을 정수 버퍼 IBUF를 최대 N개 원소 용량으로 등록한다(28). IREQ·IERR를 반환한다. 종료 표지로 이동한 뒤 반환한다. 원문: `C==== 実行 ===========================================================` (25) (실행); `C     -- MPIルーチン --` (27) (MPI 루틴); `      CALL MPI_IRECV(IBUF,N,MPI_INTEGER,ISRC,0,MGCOMM,IREQ,IERR)` (28); `C     -- 実行文の終了 --` (30) (실행문 종료); `      GOTO 9999` (31); `C==== 終了 ===========================================================` (33) (종료); ` 9999 CONTINUE` (35); `      RETURN` (36); `      END` (37) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 28: 수신 태그는 상수 0이다. 이 루틴은 MPI_IRECV의 IERR를 검사하지 않고 반환한다.
