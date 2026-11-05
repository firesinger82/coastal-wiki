---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/bctset.f
lines: 81
sha256: 66b9216ed6fa1229d648918b5661005ead46e5fb39ab6756d15656e882931063
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# bctset.f — 판독 구간 기록

구간은 1행부터 81행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–28 | BCTSET의 MPI_PARAM 사용과 인수 배열 범위를 선언한다(1–8). NICPA=KK(88)·NICPR=KK(90)를 읽고 I_BCT와 같은 ICPA(1,I)를 찾는다(10–23). 일치하면 ADDSET3로 IS/IE를 정한다(20). ICTB·FRTB 전체를 0으로 초기화한다(25–27). 원문(연속 표시는 같은 문장의 이어지는 행이다): `      SUBROUTINE BCTSET(ICTB,FRTB,I_BCT,KK,NICRG,ICPA,NCPA,ICPR,NCPR,CPR` (1); `     &                 ,ICRG,ITO)` (2); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION KK(*),ICTB(NICRG,NICRG),FRTB(3,NICRG,NICRG),ICPR(2,*)` (7); `     &         ,NCPR(2,*),CPR(2,*),ICRG(2,NICRG),ICPA(2,*),NCPA(*)` (8); `      NICPA = KK(88)` (10); `      NICPR = KK(90)` (11); `      IADD = 0` (13); `      IS = 1` (14); `      IE = 1` (15); `      DO I = 1, NICPA` (17); `        IF( ICPA(1,I) == I_BCT ) THEN` (18); `          IADD = 1` (19); `          CALL ADDSET3(IS,IE,ICPA,I)` (20); `          EXIT` (21); `        ENDIF` (22); `      ENDDO` (23); `      ICTB(:,:) = 0` (25); `      FRTB(:,:,:) = 0.` (27). [11-04 전수 검증 정정] |
| 29–54 | 시작 시 1–2행 BCTSET 루틴 안. I 루프(29)의 SELECT CASE(31–36)로 경계 ID를 고른다. ICPR에서 ID를 찾아 ADDSET3의 KS:KE 범위에 걸쳐 노예면(slave)·주면(master) 표와 FRTB를 채운다(38–51). 원문(연속 표시는 같은 문장의 이어지는 행이다): `      DO I = IS, IE` (29); `        SELECT CASE( IADD )` (31); `        CASE( 1 )` (32); `          ID = NCPA(I)` (33); `        CASE( 0 )` (34); `          ID = I_BCT` (35); `        END SELECT` (36); `        DO J = 1, NICPR` (38); `          IF( ICPR(1,J) == ID ) THEN` (39); `            CALL ADDSET3(KS,KE,ICPR,J)` (40); `            DO K = KS, KE` (41); `              ISLAVE = NCPR(1,K)` (42); `              MASTER = NCPR(2,K)` (43); `              ICTB(ISLAVE,MASTER) = 1` (44); `              FRTB(1,ISLAVE,MASTER) = CPR(1,J)` (45); `              FRTB(2,ISLAVE,MASTER) = 1.D0` (46); `              FRTB(3,ISLAVE,MASTER) = CPR(2,J)` (47); `            ENDDO` (48); `            EXIT` (49); `          ENDIF` (50); `        ENDDO` (51); `      ENDDO` (53). |
| 55–81 | 시작 시 1–2행 BCTSET 루틴 안. `FRTB(1,I,J) > 0.D0` 조건으로 KK(96)=2를 정한다(55–62). 양방향 주면·노예면 관계가 있으면 진단과 ERRSTP(52,ITO)를 호출한다(64–72). MYRANK=1이면 조작 코드 20과 ICTB·FRTB·KK(96)를 순서대로 M_MPI_SEND_I/D로 보낸다(74–79). 원문(연속 표시는 같은 문장의 이어지는 행이다): `      DO I = 1, NICRG` (55); `        DO J = 1, NICRG` (56); `          IF( FRTB(1,I,J) > 0.D0 ) THEN` (57); `            KK(96) = 2` (58); `            EXIT` (59); `          ENDIF` (60); `        ENDDO` (61); `      ENDDO` (62); `      DO I = 1, NICRG` (64); `        DO J = I + 1, NICRG` (65); `          IF( ICTB(I,J) == 1 .AND. ICTB(J,I) == 1 ) THEN` (66); `            WRITE(ITO,'(A,2I3)') 'BIDIRECTIONAL MASTER-SLAVE :'` (67); `     &                          ,ICRG(1,I),ICRG(1,J)` (68); `            CALL ERRSTP(52,ITO)` (69); `          ENDIF` (70); `        ENDDO` (71); `      ENDDO` (72); `      IF( MYRANK == 1 ) THEN` (74); `        CALL M_MPI_SEND_I(20,1,0)  ! SEND IOP=20 TO GLB_COMM` (75); `        CALL M_MPI_SEND_I(ICTB,NICRG*NICRG,0)` (76); `        CALL M_MPI_SEND_D(FRTB,3*NICRG*NICRG,0)` (77); `        CALL M_MPI_SEND_I(KK(96),1,0)` (78); `      ENDIF` (79); `      END` (81). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 55–62: FRTB(1,I,J)>0이면 KK(96)=2를 설정한다. 해당 조건이 거짓인 경우 KK(96)를 초기화하는 문장은 이 루틴에 없다.
- 57–62: `FRTB(1,I,J) > 0.D0`일 때 수행하는 EXIT는 안쪽 J 루프에 있다. 바깥 I 루프는 계속 진행한다. [11-04 전수 검증 정정]
