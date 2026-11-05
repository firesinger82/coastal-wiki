---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/outnod0.f
lines: 116
sha256: 8e7e602a0cf9f746b74e1f42da1642443530f820dca3181d121e02404b420791
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# outnod0.f — 판독 구간 기록

구간은 1행부터 116행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | M_VAL·파일 단위 배열과 결과 포인터를 선언한다(3–6). UG(6,NNOD)·VEL(3,NNOD)·ACC(3,NNOD)·RFCO(6,NNOD)를 할당하여 수집한다(8–17). IGEO 양수일 때 PG3(NNOD)도 할당·수집한다(12·18). 원문: `      SUBROUTINE OUTNOD0( NNOD, IGEO, IFL )` (1); `      USE M_VAL` (3); `      DIMENSION IFL(*)` (5); `      REAL(8),POINTER :: UG(:,:),VEL(:,:),ACC(:,:)` (6); `      ALLOCATE( UG(6,NNOD) )` (8); `      ALLOCATE( VEL(3,NNOD) )` (9); `      ALLOCATE( ACC(3,NNOD) )` (10); `      ALLOCATE( RFCO(6,NNOD) )` (11); `      IF( IGEO > 0 ) ALLOCATE( PG3(NNOD) )` (12); `      CALL GATHER_NODAL_D(UG,6)` (14); `      CALL GATHER_NODAL_D(VEL,3)` (15); `      CALL GATHER_NODAL_D(ACC,3)` (16); `      CALL GATHER_NODAL_D(RFCO,6)` (17); `      IF( IGEO > 0 ) CALL GATHER_NODAL_D(PG3,1)` (18). |
| 20–53 | 시작 시 1행 outnod0 루틴 안. 변위(displacement)는 IFL(20), 속도(velocity)는 IFL(21)에 출력한다(20·37). 각 IP 파트(part)에서 J=1..3 성분과 NG_ENS(IP) 절점을 순회하고 IG_ENS로 전역 절점 번호를 얻는다(22–35·39–52). 원문: `      WRITE(IFL(20),'(A)') 'displacement'` (20); `      DO IP = 1, N_PART` (22); `        WRITE(IFL(20),'(A)') 'part'` (24); `        WRITE(IFL(20),'(I10)') IP` (25); `        WRITE(IFL(20),'(A)') 'coordinates'` (26); `        DO J = 1, 3` (28); `          DO I = 1, NG_ENS(IP)` (29); `            IG = IG_ENS(I,IP)` (30); `            WRITE(IFL(20),'(1PE12.4)') UG(J,IG)` (31); `          ENDDO` (32); `        ENDDO` (33); `      ENDDO` (35); `      WRITE(IFL(21),'(A)') 'velocity'` (37); `      DO IP = 1, N_PART` (39); `        WRITE(IFL(21),'(A)') 'part'` (41); `        WRITE(IFL(21),'(I10)') IP` (42); `        WRITE(IFL(21),'(A)') 'coordinates'` (43); `        DO J = 1, 3` (45); `          DO I = 1, NG_ENS(IP)` (46); `            IG = IG_ENS(I,IP)` (47); `            WRITE(IFL(21),'(1PE12.4)') VEL(J,IG)` (48); `          ENDDO` (49); `        ENDDO` (50); `      ENDDO` (52). |
| 54–87 | 시작 시 1행 outnod0 루틴 안. 가속도(acceleration)는 IFL(22), 반력(reaction force)은 IFL(23)에 출력한다(54·71). 두 결과 모두 파트·성분·절점 루프를 사용한다(56–69·73–86). 원문: `      WRITE(IFL(22),'(A)') 'acceleration'` (54); `      DO IP = 1, N_PART` (56); `        WRITE(IFL(22),'(A)') 'part'` (58); `        WRITE(IFL(22),'(I10)') IP` (59); `        WRITE(IFL(22),'(A)') 'coordinates'` (60); `        DO J = 1, 3` (62); `          DO I = 1, NG_ENS(IP)` (63); `            IG = IG_ENS(I,IP)` (64); `            WRITE(IFL(22),'(1PE12.4)') ACC(J,IG)` (65); `          ENDDO` (66); `        ENDDO` (67); `      ENDDO` (69); `      WRITE(IFL(23),'(A)') 'reactive force'` (71); `      DO IP = 1, N_PART` (73); `        WRITE(IFL(23),'(A)') 'part'` (75); `        WRITE(IFL(23),'(I10)') IP` (76); `        WRITE(IFL(23),'(A)') 'coordinates'` (77); `        DO J = 1, 3` (79); `          DO I = 1, NG_ENS(IP)` (80); `            IG = IG_ENS(I,IP)` (81); `            WRITE(IFL(23),'(1PE12.4)') RFCO(J,IG)` (82); `          ENDDO` (83); `        ENDDO` (84); `      ENDDO` (86). |
| 88–109 | 시작 시 1행 outnod0 루틴 안. IGEO 양수 분기에서 간극수압(pore water pressure)을 출력한다(88–90). NP_ENS(2)·(3)·(4)의 합에 1을 더한 IPS부터 그 합에 NP_ENS(6)을 더한 IPE까지 파트를 순회한다(92–106). 각 파트 절점의 PG3를 기록한다(101–104). 원문: `      IF( IGEO > 0 ) THEN` (88); `        WRITE(IFL(24),'(A)') 'pore water pressure'` (90); `        IPS = NP_ENS(2) + NP_ENS(3) + NP_ENS(4) + 1` (92); `        IPE = NP_ENS(2) + NP_ENS(3) + NP_ENS(4) + NP_ENS(6)` (93); `        DO IP = IPS, IPE` (95); `          WRITE(IFL(24),'(A)') 'part'` (97); `          WRITE(IFL(24),'(I10)') IP` (98); `          WRITE(IFL(24),'(A)') 'coordinates'` (99); `          DO I = 1, NG_ENS(IP)` (101); `            IG = IG_ENS(I,IP)` (102); `            WRITE(IFL(24),'(1PE12.4)') PG3(IG)` (103); `          ENDDO` (104); `        ENDDO` (106); `      ENDIF` (108). |
| 110–116 | 시작 시 1행 outnod0 루틴 안. UG·VEL·ACC·RFCO를 해제한다(110–113). PG3 해제 조건은 IGEO 양수이다(114). 원문: `      DEALLOCATE( UG )` (110); `      DEALLOCATE( VEL )` (111); `      DEALLOCATE( ACC )` (112); `      DEALLOCATE( RFCO )` (113); `      IF( IGEO > 0 ) DEALLOCATE( PG3 )` (114); `      END` (116). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·11·28·79: UG와 RFCO의 첫 차원은 6이며 출력 성분 루프는 1..3이다.
