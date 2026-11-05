---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/main/elem_init.f
lines: 79
sha256: 6c64fa25967a8c6cbf44122d52a1e0769a8d4b2d950863589b45bd285c3f4c20
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# elem_init.f — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–48 | ELEM_INIT은 요소 유형별로 D를 설정하여 DMT에 복사한다(12–31). 해석: D는 초기 구성 행렬(constitutive matrix)의 성분으로 읽는다. 유형 2·6은 DSOL0 및 N=21, 유형 3은 AMAT 첫 성분 및 N=1, 유형 4는 DBEAM0 및 N=6을 사용한다(15–25). MGP마다 D를 DMT에 연속 복사한다(26–30). 재료 IYLD>0 또는 ST>0이면 KK(80)=1을 설정한다(33–41). MYRANK > 0이면 CG_MPI_ALLREDUCE_I(KK(80),MAX,1,1)를 호출하고 KK(80) = MAX를 대입한다(43–45). MYRANK == 1일 때만 SEND_KK(KK,80)를 호출한다(46). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      SUBROUTINE ELEM_INIT(KK)` (1) <br> `      USE M_VAL` (3) <br> `      USE MPI_PARAM` (4) <br> `      IMPLICIT REAL*8(A-H,O-Z)` (6) <br> `      DIMENSION KK(*),D(21)` (7) <br> `      NELM = KK(12)` (9) <br> `      MGP = KK(36)` (10) <br> `      DO I = 1, NELM` (12) <br> `        ITYP = IELM(2,I)` (13) <br> `        IMAT = IELM(4,I)` (14) <br> `        SELECT CASE( ITYP )` (15) <br> `        CASE( 2, 6 )` (16) <br> `          CALL DSOL0(D,AMAT(1,IMAT),AMAT(2,IMAT))` (17) <br> `          N = 21` (18) <br> `        CASE( 3 )` (19) <br> `          D(1) = AMAT(1,IMAT)` (20) <br> `          N = 1` (21) <br> `        CASE( 4 )` (22) <br> `          CALL DBEAM0(D,AMAT(1,IMAT),AMAT(2,IMAT))` (23) <br> `          N = 6` (24) <br> `        END SELECT` (25) <br> `        IE = 0` (26) <br> `        DO J = 1, MGP` (27) <br> `          DMT(IE+1:IE+N,I) = D(1:N)` (28) <br> `          IE = IE + N` (29) <br> `        ENDDO` (30) <br> `      ENDDO` (31) <br> `      DO I = 1, NELM` (33) <br> `        IMAT = IELM(4,I)` (34) <br> `        IYLD = MAT(2,IMAT)` (35) <br> `        ST = AMAT(14,IMAT)` (36) <br> `        IF( IYLD > 0 .OR. ST > 0. ) THEN` (37) <br> `          KK(80) = 1` (38) <br> `          EXIT` (39) <br> `        ENDIF` (40) <br> `      ENDDO` (41) <br> `      IF( MYRANK > 0 ) THEN` (43) <br> `        CALL CG_MPI_ALLREDUCE_I(KK(80),MAX,1,1)` (44) <br> `        KK(80) = MAX` (45) <br> `        IF( MYRANK == 1 ) CALL SEND_KK(KK,80)` (46) <br> `      ENDIF` (47) [11-04 전수 검증 정정] |
| 49–79 | 시작 시 ELEM_INIT(1) 안이며 앞 조건·루프 밖이다. KK(80)=1이면 IST·SIGY를 (MGP,NELM)로 할당하고 IST를 0으로 채운다(49–54). SIGY는 AMAT(11,IMAT)를 복사하며 유형 3이면 SIGY(2,I)를 AMAT(1,IMAT)로 나눈다(56–61). KK(16)>0이면 유형 4에서 DIRINIT을 호출하고 VG0를 VG로 복사한다(65–77). 원문(고정형식 연속행은 아래 인접 행을 하나의 문장으로 읽음): `      IF( KK(80) == 1 ) THEN` (49) <br> `        ALLOCATE( IST(MGP,NELM) )` (51) <br> `        ALLOCATE( SIGY(MGP,NELM) )` (52) <br> `        IST(:,:) = 0` (54) <br> `        DO I = 1, NELM` (56) <br> `          ITYP = IELM(2,I)` (57) <br> `          IMAT = IELM(4,I)` (58) <br> `          SIGY(:,I) = AMAT(11,IMAT)` (59) <br> `          IF( ITYP == 3 ) SIGY(2,I) = SIGY(2,I) / AMAT(1,IMAT)` (60) <br> `        ENDDO` (61) <br> `      ENDIF` (63) <br> `      IF( KK(16) > 0 ) THEN` (65) <br> `        DO I = 1, NELM` (67) <br> `          ITYP = IELM(2,I)` (68) <br> `          IF( ITYP == 4 ) THEN` (69) <br> `            ID = IELM(7,I)` (70) <br> `            CALL DIRINIT(VG0(1,1,1,ID),IELM(8,I),BVEC(1,ID),GRID)` (71) <br> `          ENDIF` (72) <br> `        ENDDO` (73) <br> `        VG = VG0` (75) <br> `      ENDIF` (77) <br> `      END` (79) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–30: SELECT CASE에 CASE DEFAULT가 없으며 유형 1·5에서 D와 N을 설정하는 분기가 없다.
- 33–41: 이 루틴은 조건을 만족할 때 KK(80)=1을 대입한다. 검사 전 KK(80)=0 초기화는 이 파일에 없다.
