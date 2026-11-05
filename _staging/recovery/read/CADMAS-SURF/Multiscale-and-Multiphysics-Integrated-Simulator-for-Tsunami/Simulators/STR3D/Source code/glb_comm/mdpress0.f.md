---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/mdpress0.f
lines: 105
sha256: 811b9d42aa71eaffb9b662eaa21506031485e420357289387532d81c3c53cc32
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mdpress0.f — 판독 구간 기록

구간은 1행부터 105행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–33 | M_VAL·MPI_PARAM과 암시적 배정밀도를 사용한다(3–9). NNOD=KK(8), NPECG=NPROCS-1로 정한다(11–13). IPND·POS를 수집하고 IPND 음수 절점 수 NPM을 세어 방송한다(15–27). NPM=0이면 두 배열을 해제하고 반환한다(29–33). 원문: `      SUBROUTINE MDPRESS0(KK)` (1); `      USE M_VAL` (3); `      USE MPI_PARAM` (4); `      IMPLICIT REAL*8(A-H,O-Z)` (6); `      DIMENSION KK(*)` (7); `      INTEGER, POINTER :: IPM(:),IFD(:),IFND(:)` (8); `      REAL(8), POINTER :: PPM(:,:),PFD(:),RFD(:),PFND(:),RMAX(:)` (9); `      NNOD = KK(8)` (11); `      NPECG = NPROCS - 1` (13); `      ALLOCATE( IPND(NNOD) )` (15); `      ALLOCATE( POS(3,NNOD) )` (16); `      CALL GATHER_NODAL_I(IPND,1)` (18); `      CALL GATHER_NODAL_D(POS,3)` (19); `      NPM = 0` (21); `      DO I = 1, NNOD` (23); `        IF( IPND(I) < 0 ) NPM = NPM + 1` (24); `      ENDDO` (25); `      CALL M_MPI_BCAST_I(NPM,1)` (27); `      IF( NPM == 0 ) THEN` (29); `        DEALLOCATE( IPND )` (30); `        DEALLOCATE( POS )` (31); `        RETURN` (32); `      ENDIF` (33). |
| 34–63 | 시작 시 1행 mdpress0 루틴 안. IPM(NPM)·PPM(3,NPM)을 할당한다(35–36). IPND 음수 절점의 전역 번호와 위치를 압축 저장하고 원래 두 배열을 해제한다(38–49). 위치를 방송한 뒤 수신·선택 배열을 할당한다(51–59). IFND=0, RMAX=-1.D0으로 초기화한다(61–62). 원문: `      ALLOCATE( IPM(NPM) )` (35); `      ALLOCATE( PPM(3,NPM) )` (36); `      J = 0` (38); `      DO I = 1, NNOD` (40); `        IF( IPND(I) < 0 ) THEN` (41); `          J = J + 1` (42); `          IPM(J) = I` (43); `          PPM(:,J) = POS(:,I)` (44); `        ENDIF` (45); `      ENDDO` (46); `      DEALLOCATE( IPND )` (48); `      DEALLOCATE( POS )` (49); `      CALL M_MPI_BCAST_D(PPM,3*NPM)` (51); `      ALLOCATE( IFD(NPM) )` (53); `      ALLOCATE( PFD(NPM) )` (54); `      ALLOCATE( RFD(NPM) )` (55); `      ALLOCATE( IFND(NNOD) )` (57); `      ALLOCATE( PFND(NNOD) )` (58); `      ALLOCATE( RMAX(NNOD) )` (59); `      IFND(:) = 0` (61); `      RMAX(:) = -1.D0` (62). |
| 64–89 | 시작 시 1행 mdpress0 루틴 안. 각 프로세스에서 IFD·PFD·RFD를 수신한다(64–68). 대상 절점이 이미 상태 2이면 건너뛴다(70–74). IFD(I)가 2이면 IFND(J)=2와 PFND(J)=PFD(I)를 대입한다(76–78). IFD(I)가 1이면 RFD(I)가 RMAX(J)보다 클 때 RMAX(J)·IFND(J)·PFND(J)를 갱신한다(79–85). 76–85행 IF 사슬에는 ELSE가 없다. 해석: PFD·PFND는 압력 값이다. 두 루프를 닫는다(87–89). 원문: `      DO IP = 1, NPECG` (64); `        CALL M_MPI_RECV_I(IFD,NPM,IP)` (66); `        CALL M_MPI_RECV_D(PFD,NPM,IP)` (67); `        CALL M_MPI_RECV_D(RFD,NPM,IP)` (68); `        DO I = 1, NPM` (70); `          J = IPM(I)` (72); `          IF( IFND(J) == 2 ) CYCLE` (74); `          IF( IFD(I) == 2 ) THEN` (76); `            IFND(J) = 2` (77); `            PFND(J) = PFD(I)` (78); `          ELSEIF( IFD(I) == 1 ) THEN` (79); `            IF( RFD(I) > RMAX(J) ) THEN` (80); `              RMAX(J) = RFD(I)` (81); `              IFND(J) = 1` (82); `              PFND(J) = PFD(I)` (83); `            ENDIF` (84); `          ENDIF` (85); `        ENDDO` (87); `      ENDDO` (89). [11-04 전수 검증 정정] |
| 90–105 | 시작 시 1행 mdpress0 루틴 안. IFND와 PFND를 각 프로세스 절점에 분배(scatter)한다(91–92). 압축 목록·수신·선택 배열을 모두 해제하고 종료한다(94–105). 원문: `      CALL SCATTER_NODAL_I(IFND,1)` (91); `      CALL SCATTER_NODAL_D(PFND,1)` (92); `      DEALLOCATE( IPM )` (94); `      DEALLOCATE( PPM )` (95); `      DEALLOCATE( IFD )` (97); `      DEALLOCATE( PFD )` (98); `      DEALLOCATE( RFD )` (99); `      DEALLOCATE( IFND )` (101); `      DEALLOCATE( PFND )` (102); `      DEALLOCATE( RMAX )` (103); `      END` (105). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 57–62·74–85·91–92: IFND와 RMAX는 전체 초기화한다. PFND의 대입은 선택된 상태 1·2 분기 안에만 있으며 PFND 전체는 SCATTER_NODAL_D에 전달한다.
- 62·79–83: 상태 1 결과는 RFD가 초기 -1.D0보다 큰 경우부터 선택된다.
