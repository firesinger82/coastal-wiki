---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/femap/femap_out.f
lines: 40
sha256: 94142cdef3da436db92ede95fd93ea2d202ae9574ecd3e0a0ca427e3362c9e8a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# femap_out.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | FEMAP_OUT의 인수 선언은 1–3행 연속문이다. MPI_PARAM을 사용한다. IMPLICIT·DIMENSION·DATA 선언을 아래에 그대로 인용한다. IOUT은 DATA로 0에서 시작한다. MYRANK=1이면 전역 통신부로 작업 번호 5를 M_MPI_SEND_I에 넘긴다. IOUT을 증가시키고 FMP_OUS를 호출한다. 블록 450의 개폐는 MYRANK=0 조건에 있다. 원문: `      SUBROUTINE FEMAP_OUT(KK,INDG,GRID,IELM,DT1,DT2,UG1,UG2,UG3,DZ,UG` (1); `     &                    ,VEL,ACC,RFCO,PPND,PG3,EPSG,SIGG,VELG,VELE` (2); `     &                    ,ISTEP,TIME,IDYN,ITO,IFMP)` (3); `      USE MPI_PARAM` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION KK(*),INDG(*),UG1(6,*),UG2(6,*),UG3(6,*),DZ(*),UG(6,*)` (7); `     &         ,VEL(3,*),ACC(3,*),RFCO(6,*),PG3(*),GRID(3,*),IELM(*)` (8); `     &         ,EPSG(*),SIGG(*),VELG(*),VELE(*),PPND(*)` (9); `      DATA IOUT / 0 /` (10); `      IF( MYRANK == 1 ) CALL M_MPI_SEND_I(5,1,0)  ! SEND IOP=5 TO GLB_COMM` (12); `      IOUT = IOUT + 1` (14); `      IF( MYRANK == 0 ) CALL BLK_S(450,IFMP)` (16); `      CALL FMP_OUS(IOUT,ISTEP,TIME,IFMP)` (18); `      IF( MYRANK == 0 ) CALL BLK_E(IFMP)` (20) |
| 21–40 | 블록 1051을 연 뒤 절점·솔리드(solid)·봉(rod)·보(bar) 결과 루틴을 차례로 호출한다. FMP_NODAL·FMP_SOL·FMP_BAR·FMP_SOIL 호출은 표시된 연속행 전체가 한 문장이다. KK(25)>0일 때만 FMP_SOIL을 호출한다. 마지막 블록 닫기도 MYRANK=0 조건이다. 원문: `      IF( MYRANK == 0 ) CALL BLK_S(1051,IFMP)` (22); `      CALL FMP_NODAL(IOUT,DT1,DT2,INDG,UG1,UG2,UG3,DZ,UG,VEL,ACC,RFCO` (24); `     &              ,PPND,PG3,KK(8),KK(26),KK(81),KK(25),IDYN,IFMP)` (25); `      CALL FMP_SOL(IOUT,KK,INDG,GRID,IELM,KK(37),EPSG,SIGG,KK(36),PG3` (27); `     &            ,ITO,IFMP)` (28); `      CALL FMP_ROD(IOUT,KK(10),KK(14),IELM,KK(37),SIGG,KK(36),IFMP)` (30); `      CALL FMP_BAR(IOUT,KK(10)+KK(14),KK(16),IELM,KK(37),SIGG,KK(36)` (32); `     &            ,IFMP)` (33); `      IF( KK(25) > 0 ) ` (35); `     &  CALL FMP_SOIL(IOUT,KK,INDG,IELM,KK(37),VELG,KK(36),VELE,IFMP)` (36); `      IF( MYRANK == 0 ) CALL BLK_E(IFMP)` (38); `      END` (40) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18·24–36: 결과 루틴 호출에는 MYRANK=0 조건이 없고 블록 개폐에만 해당 조건이 있다.
- 7–9·24–36: VELG·VELE는 가변 길이 배열로 선언하여 FMP_SOIL에 전달한다. 이 파일에는 배열 크기 검사문이 없다.
