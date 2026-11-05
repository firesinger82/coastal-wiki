---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_pos_init.f
lines: 85
sha256: b87ecd3b3f871757ea6f18f8b54495e0caa5cbf2d5c881331f6454ead1d3d7ce
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_pos_init.f — 판독 구간 기록

구간은 1행부터 85행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | SF_POS_INIT의 선언부다. MYRANK=0에서 SF_GIPND를 호출하고 모든 프로세스가 SF_GPRES를 호출한다(22–24). ISTM=1이면 DZ를 0으로 초기화한다(26). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_POS_INIT(POS,POS2,DVEL,DVEL2,POS0,POS20,DVEL20` (1); `     &                      ,IPND0,PRES0,IPFACE0,AFC,IPGRID,IPGRID0` (2); `     &                      ,IRFACE,IRGRID0,IGNO,IENO,ZZ,NF,PP,DZ)` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      INCLUDE 'VF_A0PRM.h'` (7); `      INCLUDE 'VF_ANUMBI.h'` (8); `      INCLUDE 'VF_APARAI.h'` (9); `      INCLUDE 'VF_APHYSR.h'` (10); `      INCLUDE 'SF_STRUCT.h'` (11); `      DIMENSION POS(3,NNOD),POS2(3,NNOD),POS0(3,NNOD0),POS20(3,NNOD0)` (13); `     &         ,DVEL(3,NELM),DVEL2(3,NELM),DVEL20(3,NELM0),IGNO(NNOD)` (14); `     &         ,IENO(NELM),IPND0(NNOD0),IPGRID(2,NNOD),IPGRID0(2,NNOD0)` (15); `     &         ,PRES0(NNOD0),PP(NUMI,NUMJ,NUMK),ZZ(MAXG1,NUMK)` (16); `     &         ,NF(NUMI,NUMJ,NUMK),IPFACE0(12,NPFC0),AFC(NPFC0)` (17); `     &         ,IRFACE(NPFC0),IRGRID0(NNOD0),DZ(NUMI,NUMJ)` (18); `      INTEGER, POINTER :: IPF(:,:)` (20); `      IF( MYRANK == 0 ) CALL SF_GIPND(IPND0,IPGRID0,NNOD0)` (22); `      CALL SF_GPRES(PRES0,PP,IPGRID,IGNO,POS,ZZ,NF)` (24); `      IF( ISTM == 1 ) DZ(:,:) = 0.D0` (26). |
| 28–60 | 시작 시 1행 SF_POS_INIT 루틴 안. SF_POS_INIT 안. MYRANK=0이면 WVLVL·ZZ(1,NUMK)·NPFC0·IPFACE0(3:12,:)에서 복사한 IPF·AFC·IPND0를 이 순서로 IROOTS에 보낸다(28–44). ISTM=1이면 IRFACE·IRGRID0도 보낸다(46–49). PRES0와 TNEXT=0을 보낸 후 POS20을 받는다(51–56). IGEO=1일 때 DVEL20을 받는다(57). 원문(연속 표시는 앞 문장에 이어짐): `      IF( MYRANK == 0 ) THEN` (28); `        CALL SF_C_MPI_SEND_D(WVLVL,1,IROOTS)` (30); `        CALL SF_C_MPI_SEND_D(ZZ(1,NUMK),1,IROOTS)` (31); `        ALLOCATE( IPF(10,NPFC0) )` (33); `        IPF(:,:) = 0` (35); `        IPF(:,:) = IPFACE0(3:12,:)` (36); `        CALL SF_C_MPI_SEND_I(NPFC0,1,IROOTS)` (38); `        CALL SF_C_MPI_SEND_I(IPF,NPFC0*10,IROOTS)` (39); `        DEALLOCATE( IPF )` (41); `        CALL SF_C_MPI_SEND_D(AFC,NPFC0,IROOTS)` (43); `        CALL SF_C_MPI_SEND_I(IPND0,NNOD0,IROOTS)` (44); `        IF( ISTM == 1 ) THEN` (46); `          CALL SF_C_MPI_SEND_I(IRFACE,NPFC0,IROOTS)` (47); `          CALL SF_C_MPI_SEND_I(IRGRID0,NNOD0,IROOTS)` (48); `        ENDIF` (49); `        CALL SF_C_MPI_SEND_D(PRES0,NNOD0,IROOTS)` (51); `        TNEXT = 0.D0` (53); `        CALL SF_C_MPI_SEND_D(TNEXT,1,IROOTS)` (54); `        CALL SF_C_MPI_RECV_D(POS20,NNOD0*3,IROOTS)` (56); `        IF( IGEO == 1 ) CALL SF_C_MPI_RECV_D(DVEL20,NELM0*3,IROOTS)` (57); `      ENDIF` (59). 해석: WVLVL은 수위로 읽힌다. 해석: ZZ(1,NUMK)는 상단 Z 좌표로 읽힌다. [11-04 전수 검증 정정] |
| 61–85 | 시작 시 1행 SF_POS_INIT 루틴 안. SF_POS_INIT 안이며 28행 분기 밖. IPART=0이면 루트(root)에서 POS2·DVEL2를 복사한 후 VF_P1BCSD로 배포한다(61–69). IPART=1이면 SF_BCAST_D로 배포한다(71–75). TSTR2=0을 설정하고 POS0·POS·DVEL을 갱신한다(78–83). 원문(연속 표시는 앞 문장에 이어짐): `      IF( IPART == 0 ) THEN` (61); `        IF( MYRANK == 0 ) THEN` (63); `          POS2 = POS20` (64); `          DVEL2 = DVEL20` (65); `        ENDIF` (66); `        CALL VF_P1BCSD(POS2,NNOD*3,0)` (68); `        CALL VF_P1BCSD(DVEL2,NELM*3,0)` (69); `      ELSEIF( IPART == 1 ) THEN` (71); `        CALL SF_BCAST_D(POS2,IGNO,NNOD,POS20,NNOD0,3)` (73); `        CALL SF_BCAST_D(DVEL2,IENO,NELM,DVEL20,NELM0,3)` (74); `      ENDIF` (76); `      TSTR2 = 0.D0` (78); `      IF( MYRANK == 0 ) POS0 = POS20` (80); `      POS = POS2` (82); `      DVEL = DVEL2` (83); `      END` (85). 61–76행의 IF/ELSEIF에는 ELSE가 없다. 80행의 POS0 대입은 MYRANK==0에서만 실행한다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 57·65·69·74·83: DVEL20 수신은 IGEO=1 조건 안에 있다. DVEL2의 복사·배포와 DVEL 대입에는 IGEO 조건이 없다.
