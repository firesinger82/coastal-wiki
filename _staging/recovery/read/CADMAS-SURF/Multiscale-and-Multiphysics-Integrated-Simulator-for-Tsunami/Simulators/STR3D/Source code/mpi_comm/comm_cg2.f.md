---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/mpi_comm/comm_cg2.f
lines: 71
sha256: 6f95a9b5f3760ffa161ff82420824e7c171b951c6d69bd7fa7faf7a8f70791eb
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# comm_cg2.f — 판독 구간 기록

구간은 1행부터 71행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–30 | COMM_CG2는 M_PART와 REAL*8 암묵 선언을 사용하며 X(*), INDF(6,*), INDP(*)를 선언한다(1–7). 6성분과 1성분 송수신 배열 및 2열 요청 배열을 할당한다(9–17). 송신 배열을 0으로 초기화한다(19–20). `ND = NODEXP(I)`를 거쳐 INDF/INDP에서 얻은 IFR가 양수일 때 X(IFR)를 복사한다(23–29). 해석: ND는 절점 번호로 읽힌다. 원문(연속행은 앞 문장에 이어짐): `      SUBROUTINE COMM_CG2(X,INDF,INDP)` (1); `      USE M_PART` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION X(*),INDF(6,*),INDP(*)` (7); `      REAL(8), POINTER :: WS1(:,:),WR1(:,:),WS2(:),WR2(:)` (9); `      INTEGER, POINTER :: IREQS(:,:),IREQR(:,:)` (10); `      ALLOCATE( WS1(6,NEXP) )` (12); `      ALLOCATE( WR1(6,NIMP) )` (13); `      ALLOCATE( WS2(NEXP) )` (14); `      ALLOCATE( WR2(NIMP) )` (15); `      ALLOCATE( IREQS(NPE,2) )` (16); `      ALLOCATE( IREQR(NPE,2) )` (17); `      WS1(:,:) = 0.D0` (19); `      WS2(:) = 0.D0` (20); `      DO I = 1, NEXP` (22); `        ND = NODEXP(I)` (23); `        DO J = 1, 6` (24); `          IFR = INDF(J,ND)` (25); `          IF( IFR > 0 ) WS1(J,I) = X(IFR)` (26); `        ENDDO` (27); `        IFR = INDP(ND)` (28); `        IF( IFR > 0 ) WS2(I) = X(IFR)` (29); `      ENDDO` (30) [11-04 전수 검증 정정] |
| 31–52 | 시작 시 1행 COMM_CG2 루틴 안. 송신 루프는 NPE, 수신 루프는 NPE를 사용한다. IDXEXP/IDXIMP 구간에 대해 6*(IE-IS+1)개와 IE-IS+1개 자료를 순서대로 CG_MPI_ISEND_D/CG_MPI_IRECV_D로 교환한다(32–48). C_MPI_WAITALL에 NPE*2 요청을 넘긴다(50–52). 원문(연속행은 앞 문장에 이어짐): `      DO IP = 1, NPE` (32); `        IS = IDXEXP(1,IP)` (33); `        IE = IDXEXP(2,IP)` (34); `        NS = 6 * ( IE - IS + 1 )` (35); `        CALL CG_MPI_ISEND_D(WS1(1,IS),NS,IPE(IP)-1,IREQS(IP,1))` (36); `        NS = IE - IS + 1` (37); `        CALL CG_MPI_ISEND_D(WS2(IS),NS,IPE(IP)-1,IREQS(IP,2))` (38); `      ENDDO` (39); `      DO IP = 1, NPE` (41); `        IS = IDXIMP(1,IP)` (42); `        IE = IDXIMP(2,IP)` (43); `        NR = 6 * ( IE - IS + 1 )` (44); `        CALL CG_MPI_IRECV_D(WR1(1,IS),NR,IPE(IP)-1,IREQR(IP,1))` (45); `        NR = IE - IS + 1` (46); `        CALL CG_MPI_IRECV_D(WR2(IS),NR,IPE(IP)-1,IREQR(IP,2))` (47); `      ENDDO` (48); `      CALL C_MPI_WAITALL(NPE*2,IREQS)` (50); `      CALL C_MPI_WAITALL(NPE*2,IREQR)` (52) |
| 53–71 | 시작 시 1행 COMM_CG2 루틴 안. `DO I = 1, NIMP`에서 `ND = NODIMP(I)`로 수신 자료를 배치할 인덱스를 얻는다(54–55). 해석: ND는 수신 절점 번호로 읽힌다. INDF/INDP가 양수인 X 성분을 WR1/WR2로 갱신하고 여섯 임시 배열을 해제한다(54–69). 원문(연속행은 앞 문장에 이어짐): `      DO I = 1, NIMP` (54); `        ND = NODIMP(I)` (55); `        DO J = 1, 6` (56); `          IFR = INDF(J,ND)` (57); `          IF( IFR > 0 ) X(IFR) = WR1(J,I)` (58); `        ENDDO` (59); `        IFR = INDP(ND)` (60); `        IF( IFR > 0 ) X(IFR) = WR2(I)` (61); `      ENDDO` (62); `      DEALLOCATE( WS1 )` (64); `      DEALLOCATE( WR1 )` (65); `      DEALLOCATE( WS2 )` (66); `      DEALLOCATE( WR2 )` (67); `      DEALLOCATE( IREQS )` (68); `      DEALLOCATE( IREQR )` (69); `      END` (71) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7·12–13·24·35·44·56: INDF의 첫 차원과 관련 자료 교환 성분 수는 6으로 고정되어 있다.
