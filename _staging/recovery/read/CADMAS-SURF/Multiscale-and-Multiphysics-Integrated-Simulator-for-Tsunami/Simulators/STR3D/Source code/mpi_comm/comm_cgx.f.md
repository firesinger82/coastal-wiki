---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/comm_cgx.f
lines: 58
sha256: 68a1e7610e8496bd012d6efc76c2b12ac155b03597f04a919e6671177fdee80a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# comm_cgx.f — 판독 구간 기록

구간은 1행부터 58행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | COMM_CGX는 M_PART와 REAL*8 암묵 선언을 사용한다(1–5). X(*)와 INDF(NDF,*)를 선언하고, 송수신 배열과 요청 배열을 NEXPX/NIMPX/NPEXPX/NPIMPX에 맞게 할당한다(7–15). WS를 0으로 초기화한다(17). `ND = NODEXPX(I)`와 `IFR = INDF(J,ND)`로 인덱스를 얻는다(20–22). `IF( IFR > 0 ) WS(J,I) = X(IFR)`로 양수 인덱스에 해당하는 값만 채운다(23). 해석: ND는 절점 번호이고 J는 자유도 번호로 읽힌다. 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE COMM_CGX(X,INDF,NDF)` (1); `      USE M_PART` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION X(*),INDF(NDF,*)` (7); `      REAL(8), POINTER :: WS(:,:),WR(:,:)` (9); `      INTEGER, POINTER :: IREQ1(:),IREQ2(:)` (10); `      ALLOCATE( WS(NDF,NEXPX) )` (12); `      ALLOCATE( WR(NDF,NIMPX) )` (13); `      ALLOCATE( IREQ1(NPEXPX) )` (14); `      ALLOCATE( IREQ2(NPIMPX) )` (15); `      WS(:,:) = 0.D0` (17); `      DO I = 1, NEXPX` (19); `        ND = NODEXPX(I)` (20); `        DO J = 1, NDF` (21); `          IFR = INDF(J,ND)` (22); `          IF( IFR > 0 ) WS(J,I) = X(IFR)` (23); `        ENDDO` (24); `      ENDDO` (25) [11-04 전수 검증 정정] |
| 26–58 | 시작 시 1행 COMM_CGX 루틴 안. NPEXPX 송신 대상의 IDXEXPX 구간을 CG_MPI_ISEND_D로 보내고, NPIMPX 수신 대상의 IDXIMPX 구간을 CG_MPI_IRECV_D로 받는다(27–39). 각 메시지 크기는 NDF*(IE-IS+1)이다. C_MPI_WAITALL로 양쪽 요청을 기다린다(41–43). NODIMPX에 대해 INDF가 양수인 X 성분만 WR로 갱신하고 임시 배열을 해제한다(45–58). 원문(연속행은 앞 문장에 이어짐): `      DO IP = 1, NPEXPX` (27); `        IS = IDXEXPX(1,IP)` (28); `        IE = IDXEXPX(2,IP)` (29); `        NS = NDF * ( IE - IS + 1 )` (30); `        CALL CG_MPI_ISEND_D(WS(1,IS),NS,IPEXPX(IP)-1,IREQ1(IP))` (31); `      ENDDO` (32); `      DO IP = 1, NPIMPX` (34); `        IS = IDXIMPX(1,IP)` (35); `        IE = IDXIMPX(2,IP)` (36); `        NR = NDF * ( IE - IS + 1 )` (37); `        CALL CG_MPI_IRECV_D(WR(1,IS),NR,IPIMPX(IP)-1,IREQ2(IP))` (38); `      ENDDO` (39); `      CALL C_MPI_WAITALL(NPEXPX,IREQ1)` (41); `      CALL C_MPI_WAITALL(NPIMPX,IREQ2)` (43); `      DO I = 1, NIMPX` (45); `        ND = NODIMPX(I)` (46); `        DO J = 1, NDF` (47); `          IFR = INDF(J,ND)` (48); `          IF( IFR > 0 ) X(IFR) = WR(J,I)` (49); `        ENDDO` (50); `      ENDDO` (51); `      DEALLOCATE( WS )` (53); `      DEALLOCATE( WR )` (54); `      DEALLOCATE( IREQ1 )` (55); `      DEALLOCATE( IREQ2 )` (56); `      END` (58) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
