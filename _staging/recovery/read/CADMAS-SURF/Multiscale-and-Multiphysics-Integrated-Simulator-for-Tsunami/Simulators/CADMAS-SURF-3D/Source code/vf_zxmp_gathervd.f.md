---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D/Source code/vf_zxmp_gathervd.f
lines: 44
sha256: c8a2d66084ac6650a4d846fd0e50029db6bb5a3dadd47c8798cbea72019d8cfc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vf_zxmp_gathervd.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | MPI 마스크(MPI mask) 루틴이다. 가변 길이 배정밀도 실수 데이터를 0번 처리 요소(processing element, PE)에 모은다. IMPLICIT 형식과 mpif.h, 인수의 형식·배열 범위를 아래 원문에 적는다. 원문: `      SUBROUTINE VF_ZXMP_GATHERVD(DSEND,ISIZE,DRECV,NDIM,` (1)<br>`     &                            NDATA,NDISP,NP,IERR)` (2)。 `CD=== 概要 ===========================================================` (4) (개요)。 `CDT   VF_ZXMP_GATHERVD: 可変長の実数型データを0番PEに集める` (6) (가변 길이 배정밀도 실수 데이터를 0번 처리 요소(processing element, PE)에 모은다.)。 `C==== 宣言 ===========================================================` (8) (선언)。 `C     -- 大域型 --` (10) (전역 형식)。 `      IMPLICIT INTEGER(I-N),DOUBLE PRECISION(A-H,O-Z)` (11)。 `C     -- 大域変数 --` (13) (전역 변수)。 `      INCLUDE 'mpif.h'` (14)。 `      INCLUDE 'VF_A0PRM.h'` (15)。 `      INCLUDE 'VF_APARAI.h'` (16)。 `CD    -- 引数 --` (18) (인수)。 `CD    ISEND : IN  : R*8 : 送信するデータ` (19) (송신 데이터)。 `CD    IRECV : OUT : R*8 : データの最小値` (20) (데이터의 최솟값)。 `CD    IERR  : OUT : I*4 : 完了コード` (21) (완료 코드)。 `      INTEGER ISIZE` (23)。 `      DOUBLE PRECISION DSEND(ISIZE)` (24)。 `      INTEGER NDIM,NP` (25)。 `      DOUBLE PRECISION DRECV(NDIM)` (26)。 `      INTEGER NDATA(NP)` (27)。 `      INTEGER NDISP(NP)` (28)。 `C==== 実行 ===========================================================` (30) (실행)。 [11-04 전수 검증 정정] |
| 32–36 | 시작 시 1행 SUBROUTINE VF_ZXMP_GATHERVD 루틴 안. DSEND(ISIZE)·DRECV(NDIM)은 DOUBLE PRECISION 배열이다. NDATA(NP)는 수신 개수 배열이고 NDISP(NP)는 배치 오프셋(displacement) 배열이다. MPI_GATHERV는 송신 개수 ISIZE, 두 배열, MPI_DOUBLE_PRECISION, 수집 순위(rank) 0과 통신자(communicator) MGCOMM을 사용한다. MPI 호출은 모든 인수와 고정형식 연속행을 원문대로 인용한다. 원문: `C     -- MPIルーチン --` (32) (MPI 루틴)。 `      CALL MPI_GATHERV(DSEND,ISIZE,MPI_DOUBLE_PRECISION,` (33)<br>`     &                 DRECV,NDATA,NDISP,MPI_DOUBLE_PRECISION,` (34)<br>`     &                 0,MGCOMM,IERR)` (35)。 |
| 37–44 | 시작 시 1행 SUBROUTINE VF_ZXMP_GATHERVD 루틴 안. 종료 표지 9999로 이동하고 RETURN으로 반환한다. 원문: `C     -- 実行文の終了 --` (37) (실행문 종료)。 `      GOTO 9999` (38)。 `C==== 終了 ===========================================================` (40) (종료)。 ` 9999 CONTINUE` (42)。 `      RETURN` (43)。 `      END` (44)。 |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 19–20·24–28: 주석의 인수 이름은 ISEND·IRECV이며 IRECV를 데이터 최솟값으로 설명한다. 실제 인수와 선언은 DSEND·DRECV이며 수집 배열로 사용한다.
- 33–35: 수집 순위는 0으로 고정되어 있다.
