---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/wt_restartp.f
lines: 60
sha256: 34d8ce0726a79051487e8248ac6e5b9134b72ddf3580ed738a073805fed386db
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# wt_restartp.f — 판독 구간 기록

구간은 1행부터 60행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | WT_RESTARTP 입구와 모듈·선언이다(1–7). ISTEP==KK(7)이면 ISEND=1로 설정한다(9). 해석: KK(7)을 마지막 시각 단계로 보는 설명은 이 구간만으로 확인되지 않는다. rank 1은 작업 번호 30과 ISEND를 전송한다(11–14). ICPL==2이면 ISEND·브로드캐스트 N 조건으로, 그 외에는 IROUT로 쓰기 플래그 IRW를 정한다(16–28). rank 1만 IRW를 전송한다(30). IRW==0이면 랭크와 무관하게 반환한다(32). 원문: `      SUBROUTINE WT_RESTARTP(IFL,IFLT,KK,ISTEP,TIM3,DT1,ISEND)` (1); `      USE M_VAL` (3); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION KK(*)` (7); `      IF( ISTEP == KK(7) ) ISEND = 1` (9); `      IF( MYRANK == 1 ) THEN` (11); `        CALL M_MPI_SEND_I(30,1,0)  ! SEND IOP=30 TO GLB_COMM` (12); `        CALL M_MPI_SEND_I(ISEND,1,0)` (13); `      ENDIF` (14); `      IRW = 0` (16); `      IF( ICPL == 2 ) THEN` (18); `        IF( ISEND == 1 ) THEN` (19); `          CALL M_MPI_BCAST_I(N,1)` (20); `          IF( N > 0 ) THEN` (21); `            CALL M_MPI_BCAST_I(NNOW,1)` (22); `            IRW = 1` (23); `          ENDIF` (24); `        ENDIF` (25); `      ELSE` (26); `        IF( IROUT(ISTEP) > 0 ) IRW = 1` (27); `      ENDIF` (28); `      IF( MYRANK == 1 ) CALL M_MPI_SEND_I(IRW,1,0)` (30); `      IF( IRW == 0 ) RETURN` (32) [11-04 전수 검증 정정] |
| 34–60 | 시작 시 WT_RESTARTP 루틴(1) 안이다. N1·N3·N4·NELM으로 쓸 배열 범위를 정한다(34–38). ISTEP·TIM3·DT1·NNOW와 지정된 배열 슬라이스를 쓴다(40·44–47). KK·ISTM 조건에 따라 추가 배열을 쓴다(49–56). 해석: 배열을 변위·위치·힘·재료 상태로 분류하는 설명은 변수 이름에 따른 해석이다. rank 1은 ISTEP·TIM3를 전송한다(42·58). 원문: `      N1 = KK(8)` (34); `      N3 = KK(8) + KK(28) + KK(94)` (35); `      N4 = KK(8) + KK(28) + KK(94) + KK(108)` (36); `      NELM = KK(12)` (38); `      WRITE(IFL) ISTEP,TIM3,DT1,NNOW` (40); `      IF( MYRANK == 1 ) CALL M_MPI_SEND_I(ISTEP,1,0)` (42); `      WRITE(IFL) UG1(:,1:N3),UG2(:,1:N3),UG3(:,1:N3),POS(:,1:N4)`<br>`     &          ,POSO(:,1:N4),FTID(:,1:N1),FCO(:,1:N1,:),FCK(:,1:N1,:)`<br>`     &          ,FCD(:,1:N1,:),FCM(:,1:N1,:),FCMD(:,1:N1,:)`<br>`     &          ,DMT(:,1:NELM),EPSG(:,1:NELM),SIGG(:,1:NELM)` (44–47); `      IF( KK(80) == 1 ) WRITE(IFL) IST(:,1:NELM),SIGY(:,1:NELM)` (49); `      IF( KK(92) > 0 ) WRITE(IFL) ISLV0,ISLVP,ISTICK` (51); `      IF( KK(25) > 0 )`<br>`     &  WRITE(IFL) PG1(1:N3),PG2(1:N3),PG3(1:N3),FCP(:,1:N1,:)` (53–54); `      IF( ISTM == 1 ) WRITE(IFL) GRID(:,1:N1),SUMZ(1:N1)` (56); `      IF( MYRANK == 1 ) CALL M_MPI_SEND_D(TIM3,1,0)` (58); `      END` (60) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 1: 인수 IFLT는 이 파일에서 선언부 이후 참조되지 않는다.
- 18–28·40: NNOW의 브로드캐스트는 ICPL==2·ISEND==1·N>0일 때만 있다. 40행 WRITE는 IRW가 1이면 NNOW를 포함한다.
