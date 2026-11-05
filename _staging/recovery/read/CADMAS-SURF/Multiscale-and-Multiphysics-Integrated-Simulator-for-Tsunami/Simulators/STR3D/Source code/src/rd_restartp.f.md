---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/rd_restartp.f
lines: 49
sha256: 7ad42a09742ef91a2198f5fc239550566d1a99d0f0ffcc793e3c7f748d3deec2
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rd_restartp.f — 판독 구간 기록

구간은 1행부터 49행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–20 | RD_RESTARTP 입구와 모듈·선언이다(1–7). rank 1은 작업 번호 31과 IRST를 전송한다(9–13). 읽을 절점·요소 범위를 N1·N3·N4·NELM으로 정한다(15–19). 원문: `      SUBROUTINE RD_RESTARTP(IFL,KK,ISTART,TIM3,DT1)` (1); `      USE M_VAL` (3); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION KK(*)` (7); `      IF( MYRANK == 1 ) CALL M_MPI_SEND_I(31,1,0)  ! SEND IOP=31 TO GLB_COMM` (9); `      IRST = KK(84)` (11); `      IF( MYRANK == 1 ) CALL M_MPI_SEND_I(IRST,1,0)` (13); `      N1 = KK(8)` (15); `      N3 = KK(8) + KK(28) + KK(94)` (16); `      N4 = KK(8) + KK(28) + KK(94) + KK(108)` (17); `      NELM = KK(12)` (19) |
| 21–49 | 시작 시 RD_RESTARTP 루틴(1) 안이다. 반복해서 시간과 배열의 지정 슬라이스(slice)를 읽는다(21–28). KK·ISTM 조건에 따라 추가 상태를 읽는다(30–37). ICPL별 종료 조건을 검사한 뒤 ISTART를 정한다(39–47). 원문: `      DO` (21); `        READ(IFL) ISTEP,TIM3,DT1,NNOW` (23); `        READ(IFL) UG1(:,1:N3),UG2(:,1:N3),UG3(:,1:N3),POS(:,1:N4)`<br>`     &           ,POSO(:,1:N4),FTID(:,1:N1),FCO(:,1:N1,:),FCK(:,1:N1,:)`<br>`     &           ,FCD(:,1:N1,:),FCM(:,1:N1,:),FCMD(:,1:N1,:)`<br>`     &           ,DMT(:,1:NELM),EPSG(:,1:NELM),SIGG(:,1:NELM)` (25–28); `        IF( KK(80) == 1 ) READ(IFL) IST(:,1:NELM),SIGY(:,1:NELM)` (30); `        IF( KK(92) > 0 ) READ(IFL) ISLV0,ISLVP,ISTICK` (32); `        IF( KK(25) > 0 )`<br>`     &    READ(IFL) PG1(1:N3),PG2(1:N3),PG3(1:N3),FCP(:,1:N1,:)` (34–35); `        IF( ISTM == 1 ) READ(IFL) GRID(:,1:N1),SUMZ(1:N1)` (37); `        IF( ICPL == 2 ) THEN` (39); `          IF( NNOW >= IRST ) EXIT` (40); `        ELSE` (41); `          IF( ISTEP == IRST ) EXIT` (42); `        ENDIF` (43); `      ENDDO` (45); `      ISTART = ISTEP + 1` (47); `      END` (49) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 23–42: READ에는 IOSTAT·END 지정이 없다. 종료 조건은 ICPL==2이면 NNOW>=IRST이고, 그 외에는 ISTEP==IRST이다.
