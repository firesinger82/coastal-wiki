---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/rd_restart.f
lines: 38
sha256: f4f23083d048d5a0f275241df3017f1dd96a3d470938b6481e7f0a6591a34a91
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rd_restart.f — 판독 구간 기록

구간은 1행부터 38행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–10 | RD_RESTART 입구와 M_VAL·MPI_PARAM 모듈·IMPLICIT·배열 선언이다(1–7). 목표 재시작(restart) 식별자 IRST를 KK(84)에서 가져온다(9). 원문: `      SUBROUTINE RD_RESTART(IFL,KK,ISTART,TIM3,DT1)` (1); `      USE M_VAL` (3); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION KK(*)` (7); `      IRST = KK(84)` (9) |
| 11–38 | 시작 시 RD_RESTART 루틴(1) 안이다. 반복해서 ISTEP·TIM3·DT1·NNOW와 인용한 배열을 읽는다(11–16). 해석: 이 배열을 변위·위치·힘·재료 상태로 분류하는 것은 변수 이름에 따른 해석이다. KK·ISTM 조건에 따라 추가 상태를 읽는다(18–26). ICPL==2이면 NNOW로, 그 외에는 ISTEP으로 종료를 판단하고 ISTART를 정한다(28–36). 원문: `      DO` (11); `        READ(IFL) ISTEP,TIM3,DT1,NNOW` (13); `        READ(IFL) UG1,UG2,UG3,POS,POSO,FTID,FCO,FCK,FCD,FCM,FCMD`<br>`     &           ,DMT,EPSG,SIGG` (15–16); `        IF( KK(16) > 0 ) READ(IFL) VG` (18); `        IF( KK(80) == 1 ) READ(IFL) IST,SIGY` (20); `        IF( KK(92) > 0 ) READ(IFL) ISLV,RSLV,U0,RL0,IFRIC,ISTK,FRIC` (22); `        IF( KK(25) > 0 ) READ(IFL) PG1,PG2,PG3,FCP` (24); `        IF( ISTM == 1 ) READ(IFL) GRID,SUMZ` (26); `        IF( ICPL == 2 ) THEN` (28); `          IF( NNOW >= IRST ) EXIT` (29); `        ELSE` (30); `          IF( ISTEP == IRST ) EXIT` (31); `        ENDIF` (32); `      ENDDO` (34); `      ISTART = ISTEP + 1` (36); `      END` (38) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 13–31: READ에는 IOSTAT·END 지정이 없다. 종료 조건은 ICPL==2이면 NNOW>=IRST이고, 그 외에는 ISTEP==IRST이다.
