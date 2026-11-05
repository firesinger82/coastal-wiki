---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/comm_dblx.f
lines: 44
sha256: 2c014636bc7efca2d0e0b28173de75004da71896c3413d62e75d0ae824a16364
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# comm_dblx.f — 판독 구간 기록

구간은 1행부터 44행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | COMM_DBLX는 M_PART와 REAL*8 암묵 선언을 사용한다(1–5). X(NDF,*)와 REAL(8) 송수신 배열, 정수 요청 배열을 선언한다(7–10). NEXPX/NIMPX/NPEXPX/NPIMPX에 맞게 임시 배열을 할당하고 송신 배열에 X(:,NODEXPX(:))를 복사한다(12–17). 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE COMM_DBLX(X,NDF)` (1); `      USE M_PART` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION X(NDF,*)` (7); `      REAL(8), POINTER :: WS(:,:),WR(:,:)` (9); `      INTEGER, POINTER :: IREQ1(:),IREQ2(:)` (10); `      ALLOCATE( WS(NDF,NEXPX) )` (12); `      ALLOCATE( WR(NDF,NIMPX) )` (13); `      ALLOCATE( IREQ1(NPEXPX) )` (14); `      ALLOCATE( IREQ2(NPIMPX) )` (15); `      WS(:,:) = X(:,NODEXPX(:))` (17) |
| 18–44 | 시작 시 1행 COMM_DBLX 루틴 안. 송신·수신 대상별 인덱스 구간에서 NDF*(IE-IS+1)개 자료를 CG_MPI_ISEND_D/CG_MPI_IRECV_D로 교환한다(19–31). 상대 프로세스 번호에서 1을 빼서 넘긴다. 두 C_MPI_WAITALL 호출 뒤 수신 자료를 X(:,NODIMPX(:))에 복사하고 모든 임시 배열을 해제한다(33–44). 원문(연속행은 앞 문장에 이어짐): `      DO IP = 1, NPEXPX` (19); `        IS = IDXEXPX(1,IP)` (20); `        IE = IDXEXPX(2,IP)` (21); `        NS = NDF * ( IE - IS + 1 )` (22); `        CALL CG_MPI_ISEND_D(WS(1,IS),NS,IPEXPX(IP)-1,IREQ1(IP))` (23); `      ENDDO` (24); `      DO IP = 1, NPIMPX` (26); `        IS = IDXIMPX(1,IP)` (27); `        IE = IDXIMPX(2,IP)` (28); `        NR = NDF * ( IE - IS + 1 )` (29); `        CALL CG_MPI_IRECV_D(WR(1,IS),NR,IPIMPX(IP)-1,IREQ2(IP))` (30); `      ENDDO` (31); `      CALL C_MPI_WAITALL(NPEXPX,IREQ1)` (33); `      CALL C_MPI_WAITALL(NPIMPX,IREQ2)` (35); `      X(:,NODIMPX(:)) = WR(:,:)` (37); `      DEALLOCATE( WS )` (39); `      DEALLOCATE( WR )` (40); `      DEALLOCATE( IREQ1 )` (41); `      DEALLOCATE( IREQ2 )` (42); `      END` (44) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
