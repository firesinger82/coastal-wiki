---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/remesh0.f
lines: 53
sha256: 04a1526ccc458e0de5c683074fdcdebdf1de970fcd80fbb1862f88761e8c6bdc
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# remesh0.f — 판독 구간 기록

구간은 1행부터 53행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–26 | M_VAL·M_PART·MPI_PARAM과 암시적 배정밀도·포인터 범위를 선언한다(3–10). NNOD=KK(8), NPECG=NPROCS-1로 정한다(12–14). DELZ·IFIX는 NNOD, 작업 버퍼는 MAXVAL(NDZ) 크기로 할당한다(16–19). IROOTC에서 DELZ·IFIX를 받는다(21–23). IFIX를 절점 분배한다(25). 해석: DELZ는 변위이고 IFIX는 고정 표시이다. 원문: `      SUBROUTINE REMESH0(KK)` (1); `      USE M_VAL` (3); `      USE M_PART` (4); `      USE MPI_PARAM` (5); `      IMPLICIT REAL*8(A-H,O-Z)` (7); `      DIMENSION KK(*)` (8); `      REAL(8), POINTER :: DELZ1W(:)` (9); `      INTEGER, POINTER :: IFIX(:), IFIX1W(:)` (10); `      NNOD = KK(8)` (12); `      NPECG = NPROCS - 1` (14); `      ALLOCATE( DELZ(NNOD) )` (16); `      ALLOCATE( DELZ1W(MAXVAL(NDZ)) )` (17); `      ALLOCATE( IFIX(NNOD) )` (18); `      ALLOCATE( IFIX1W(MAXVAL(NDZ)) )` (19); `      CALL C_MPI_RECV_D(DELZ,NNOD,IROOTC)` (21); `      CALL C_MPI_RECV_I(IFIX,NNOD,IROOTC)` (23); `      CALL SCATTER_NODAL_I(IFIX,1)` (25). [11-04 전수 검증 정정] |
| 27–40 | 시작 시 1행 remesh0 루틴 안. 프로세스별 NDZ를 보낸다(27–29). IFIX1W를 받아 IDZ 위치의 IFIX에 더한다(31–35). IFIX 양수 절점은 DELZ=0.D0으로 만든다(37–39). 원문: `      DO IP = 1, NPECG` (27); `        CALL M_MPI_SEND_I(NDZ(IP),1,IP)` (28); `      ENDDO` (29); `      DO IP = 1, NPECG` (31); `        CALL M_MPI_RECV_I(IFIX1W,NDZ(IP),IP)` (32); `        IFIX( IDZ(1:NDZ(IP),IP) ) = IFIX( IDZ(1:NDZ(IP),IP) )` (33); `     &                            + IFIX1W(1:NDZ(IP))` (34); `      ENDDO` (35); `      DO I = 1, NNOD` (37); `        IF( IFIX(I) > 0 ) DELZ(I) = 0.D0` (38); `      ENDDO` (39). [11-04 전수 검증 정정] |
| 41–53 | 시작 시 1행 remesh0 루틴 안. DELZ를 절점 분배한다(41). 각 프로세스의 IDZ 목록으로 DELZ1W를 채워 보낸다(43–46). 네 배열을 해제하고 종료한다(48–53). 원문: `      CALL SCATTER_NODAL_D(DELZ,1)` (41); `      DO IP = 1, NPECG` (43); `        DELZ1W(1:NDZ(IP)) = DELZ( IDZ(1:NDZ(IP),IP) )` (44); `        CALL M_MPI_SEND_D(DELZ1W,NDZ(IP),IP)` (45); `      ENDDO` (46); `      DEALLOCATE( DELZ )` (48); `      DEALLOCATE( DELZ1W )` (49); `      DEALLOCATE( IFIX )` (50); `      DEALLOCATE( IFIX1W )` (51); `      END` (53). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
