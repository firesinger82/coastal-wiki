---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/rmsh_init0.f
lines: 115
sha256: 9c18f2de5526c473e39a2674783d71964643afc0522956763a59c8fa677eef5d
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# rmsh_init0.f — 판독 구간 기록

구간은 1행부터 115행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | MPI_PARAM·M_VAL·M_PART와 암시적 배정밀도를 사용한다(3–8). 작업 포인터와 IDZ 포인터를 담는 WRK 형식을 선언한다(9–14). NNOD·NPFC·NPECG를 정하고 IRF 양수 표면 수 NRFACE를 세어 IRFACE(10,NRFACE)·RFACE(3,4,NRFACE)를 할당한다(16–30). 원문: `      SUBROUTINE RMSH_INIT0(KK,ICHK)` (1); `      USE MPI_PARAM` (3); `      USE M_VAL` (4); `      USE M_PART` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (7); `      DIMENSION KK(*)` (8); `      INTEGER, POINTER :: IRFACE(:,:),IRMSHW(:,:),IFIL(:),IDZR(:)` (9); `      REAL(8), POINTER :: RFACE(:,:,:)` (10); `      TYPE WRK` (11); `        INTEGER, POINTER :: IDZ(:)` (12); `      END TYPE WRK` (13); `      TYPE(WRK), POINTER :: WK(:)` (14); `      NNOD = KK(8)` (16); `      NPFC = KK(81)` (17); `      NPECG = NPROCS - 1` (19); `      IC = 0` (21); `      DO I = 1, NPFC` (23); `        IF( IRF(I) > 0 ) IC = IC + 1` (24); `      ENDDO` (25); `      NRFACE = IC` (27); `      ALLOCATE( IRFACE(10,NRFACE) )` (29); `      ALLOCATE( RFACE(3,4,NRFACE) )` (30). |
| 32–54 | 시작 시 1행 rmsh_init0 루틴 안. IRF 양수 표면만 순서대로 IRFACE에 표지·표면 정보를 복사하고 GRID에서 해당 절점 좌표를 RFACE에 저장한다(32–42). ICHK=0이면 GRID, ICHK<2이면 IPFC를 해제하며 IRF는 무조건 해제한다(44–46). 표면 수와 두 표면 배열을 방송한 뒤 표면 작업 배열을 해제한다(48–53). 원문: `      IC = 0` (32); `      DO I = 1, NPFC` (34); `        IF( IRF(I) > 0 ) THEN` (35); `          IC = IC + 1` (36); `          IRFACE(1,IC) = IRF(I)` (37); `          IRFACE(2:10,IC) = IPFC(2:10,I)` (38); `          N = IPFC(2,I)` (39); `          RFACE(:,1:N,IC) = GRID(:,IPFC(3:2+N,I))` (40); `        ENDIF` (41); `      ENDDO` (42); `      IF( ICHK == 0 ) DEALLOCATE( GRID )` (44); `      IF( ICHK < 2 ) DEALLOCATE( IPFC )` (45); `      DEALLOCATE( IRF )` (46); `      CALL M_MPI_BCAST_I(NRFACE,1)` (48); `      CALL M_MPI_BCAST_I(IRFACE,10*NRFACE)` (49); `      CALL M_MPI_BCAST_D(RFACE,12*NRFACE)` (50); `      DEALLOCATE( IRFACE )` (52); `      DEALLOCATE( RFACE )` (53). |
| 55–81 | 시작 시 1행 rmsh_init0 루틴 안. IRMSHW(6,MAXVAL(NN_EXT))·IFIL(NNOD)·NDZ·WK·IDZR를 할당한다(55–59). IP 루프에서 재격자화(remeshing) 참조 목록 IRMSHW를 받는다(61–63). 참조된 전역 절점에 IFIL=1을 표시하고 표시된 절점 수를 NDZ(IP)로 정해 WK(IP)%IDZ를 할당한다(65–80). 원문: `      ALLOCATE( IRMSHW(6,MAXVAL(NN_EXT)) )` (55); `      ALLOCATE( IFIL(NNOD) )` (56); `      ALLOCATE( NDZ(NPECG) )` (57); `      ALLOCATE( WK(NPECG) )` (58); `      ALLOCATE( IDZR(NNOD) )` (59); `      DO IP = 1, NPECG` (61); `        CALL M_MPI_RECV_I(IRMSHW,6*NN_EXT(IP),IP)` (63); `        IFIL(:) = 0` (65); `        DO I = 1, NN_EXT(IP)` (67); `          N = IRMSHW(1,I)` (68); `          IFIL( IRMSHW(2:1+N,I) ) = 1` (69); `        ENDDO` (70); `        IC = 0` (72); `        DO I = 1, NNOD` (74); `          IF( IFIL(I) == 1 ) IC = IC + 1` (75); `        ENDDO` (76); `        NDZ(IP) = IC` (78); `        ALLOCATE( WK(IP)%IDZ(NDZ(IP)) )` (80). |
| 82–103 | 시작 시 1행 rmsh_init0 루틴 안. 시작 시 61행 `DO IP = 1, NPECG` 안이며 이 루프는 102행 `ENDDO`에서 닫힌다. 표시된 전역 절점 번호를 WK(IP)%IDZ에 모은다(82–89). IDZR로 역매핑을 만들고 IRMSHW의 참조 절점을 그 압축 번호로 치환한다(91–98). 변환된 6*NN_EXT(IP) 정수를 보내고 IP 루프를 닫는다(100–102). 원문: `        IC = 0` (82); `        DO I = 1, NNOD` (84); `          IF( IFIL(I) == 1 ) THEN` (85); `            IC = IC + 1` (86); `            WK(IP)%IDZ(IC) = I` (87); `          ENDIF` (88); `        ENDDO` (89); `        DO I = 1, NDZ(IP)` (91); `          IDZR( WK(IP)%IDZ(I) ) = I` (92); `        ENDDO` (93); `        DO I = 1, NN_EXT(IP)` (95); `          N = IRMSHW(1,I)` (96); `          IRMSHW(2:1+N,I) = IDZR( IRMSHW(2:1+N,I) )` (97); `        ENDDO` (98); `        CALL M_MPI_SEND_I(IRMSHW,6*NN_EXT(IP),IP)` (100); `      ENDDO` (102). [11-04 전수 검증 보완] |
| 104–115 | 시작 시 1행 rmsh_init0 루틴 안. IRMSHW·IFIL·IDZR를 해제한다(104–106). IDZ(MAXVAL(NDZ),NPECG)를 할당하고 각 프로세스의 유효 목록을 복사한 뒤 WK(IP)%IDZ를 해제한다(108–113). 원문: `      DEALLOCATE( IRMSHW )` (104); `      DEALLOCATE( IFIL )` (105); `      DEALLOCATE( IDZR )` (106); `      ALLOCATE( IDZ(MAXVAL(NDZ),NPECG) )` (108); `      DO IP = 1, NPECG` (110); `        IDZ(1:NDZ(IP),IP) = WK(IP)%IDZ(:)` (111); `        DEALLOCATE( WK(IP)%IDZ )` (112); `      ENDDO` (113); `      END` (115). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–14·58·110–115: WK는 POINTER이며 ALLOCATE(WK(NPECG))를 수행한다. 각 WK(IP)%IDZ는 해제하지만 WK 자체의 DEALLOCATE는 이 파일에 없다.
- 30·39–40: RFACE의 둘째 차원은 4이다. RFACE(:,1:N,IC)에 사용하는 N은 IPFC(2,I)에서 오며 이 파일에 N<=4 검사는 없다.
