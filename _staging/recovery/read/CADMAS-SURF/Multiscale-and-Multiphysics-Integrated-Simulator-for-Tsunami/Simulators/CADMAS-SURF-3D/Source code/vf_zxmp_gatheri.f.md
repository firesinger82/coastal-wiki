---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_gatheri.f
lines: 40
sha256: ce3fdf386ebb17598a97566359b8a4d9ac2be83b59b25b129ec61cfa5db06659
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_gatheri.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | MPI 마스크(MPI mask) 루틴이다. 고정 길이 정수 데이터를 0번 처리 요소(processing element, PE)에 모은다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMP_GATHERI(ISEND,ISIZE,IRECV,NDIM,IERR)` (1)。 `CD=== 概要 ===========================================================` (3) (개요)。 `CDT   VF_ZXMP_GATHERI: 固定長の整数型データを0番PEに集める` (5) (고정 길이 정수 데이터를 0번 처리 요소(processing element, PE)에 모은다.)。 `C==== 宣言 ===========================================================` (7) (선언)。 `C     -- 大域型 --` (9) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (10)。 `C     -- 大域変数 --` (12) (전역 변수)。 `      INCLUDE 'mpif.h'` (13)。 `      INCLUDE 'VF_A0PRM.h'` (14)。 `      INCLUDE 'VF_APARAI.h'` (15)。 `CD    -- 引数 --` (17) (인수)。 `CD    ISEND : IN  : R*8 : 送信するデータ` (18) (송신 데이터)。 `CD    IRECV : OUT : R*8 : データの最小値` (19) (데이터의 최솟값)。 `CD    IERR  : OUT : I*4 : 完了コード` (20) (완료 코드)。 `      INTEGER ISIZE` (22)。 `      INTEGER ISEND(ISIZE)` (23)。 `      INTEGER IRECV(NDIM)` (24)。 `C==== 実行 ===========================================================` (26) (실행)。 [11-04 전수 검증 정정] |
| 28–32 | 시작 시 1행 SUBROUTINE VF_ZXMP_GATHERI 루틴 안. ISEND(ISIZE)·IRECV(NDIM)은 INTEGER 배열이다. MPI_GATHER는 각 프로세스의 ISIZE개 정수를 수집한다. 송수신 형식은 MPI_INTEGER이고 수집 순위(rank)는 0, 통신자(communicator)는 MGCOMM이다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (28) (MPI 루틴)。 `      CALL MPI_GATHER(ISEND,ISIZE,MPI_INTEGER,` (29)<br>`     &                IRECV,ISIZE,MPI_INTEGER,` (30)<br>`     &                0,MGCOMM,IERR)` (31)。 |
| 33–40 | 시작 시 1행 SUBROUTINE VF_ZXMP_GATHERI 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (33) (실행문 종료)。 `      GOTO 9999` (34)。 `C==== 終了 ===========================================================` (36) (종료)。 ` 9999 CONTINUE` (38)。 `      RETURN` (39)。 `      END` (40)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–19·23–24·29–31: 인수 주석은 ISEND·IRECV를 R*8로 적고 IRECV를 최솟값이라고 설명한다. 실제 선언은 INTEGER 배열이며 호출은 MPI_GATHER와 MPI_INTEGER를 사용한다.
- 29–31: 수집 순위는 0으로 고정되어 있다.
