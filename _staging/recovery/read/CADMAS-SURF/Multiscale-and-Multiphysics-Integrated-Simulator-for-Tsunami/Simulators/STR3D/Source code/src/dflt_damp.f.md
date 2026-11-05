---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/dflt_damp.f
lines: 78
sha256: a7ec47897cbfc3e1e1442af0bd31888f280463ac9abd1e08579be171b88b050b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# dflt_damp.f — 판독 구간 기록

구간은 1행부터 78행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | DFLT_DAMP에서 MPI_PARAM을 사용한다. 배열 크기와 포인터 RLB를 선언한다. RLB를 NELM 크기로 할당한다. 해석: AMAT·GRID·IELM은 재료·좌표·요소 자료이며 RLB는 요소별 길이 척도이다. 원문: `      SUBROUTINE DFLT_DAMP(AMAT,NMAT,GRID,IELM,NM,NELM,W4,ITO)` (1); `      USE MPI_PARAM` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION GRID(3,*),IELM(NM,NELM),AMAT(33,NMAT),NP(20),X(3,20)` (7); `      REAL(8), POINTER :: RLB(:)` (9); `      ALLOCATE( RLB(NELM) )` (11). [11-04 전수 검증 정정] |
| 13–49 | 시작 시 1행 DFLT_DAMP 루틴 안. 각 요소의 좌표를 모은다. ITYP 2·6에서는 절점 수 4, 10, 6·15, 8·20에 따라 TETVOL·EVOLTE2·EVOLPN2·EVOLHX2를 호출한다. NNP가 4 또는 10이면 호출 뒤 V에 6을 곱한다. NNP가 6 또는 15이면 호출 뒤 V에 2를 곱한다. NNP가 8 또는 20이면 호출 뒤 V 배수 대입은 없다. 이후 V의 세제곱근을 RLB에 둔다. 해석: 이 V 배수 연산은 체적에 대한 보정이다. ITYP 3·4에서는 VECML2를 호출하고 결과에 0.1을 곱한다. 원문: `      DO I = 1, NELM` (13); `        ITYP = IELM(2,I)` (15); `        NNP = IELM(3,I)` (16); `        NP(1:NNP) = IELM(8:7+NNP,I)        ` (18); `        X(:,1:NNP) = GRID(:,NP(1:NNP))` (20); `        SELECT CASE( ITYP )` (22); `        CASE( 2, 6 )` (23); `          SELECT CASE( NNP )` (25); `          CASE( 4 )` (26); `            CALL TETVOL(X,V)` (27); `            V = V * 6.D0` (28); `          CASE( 10 )` (29); `            CALL EVOLTE2(V,X,ITO)` (30); `            V = V * 6.D0` (31); `          CASE( 6, 15 )` (32); `            CALL EVOLPN2(V,X,NNP,ITO)` (33); `            V = V * 2.D0` (34); `          CASE( 8, 20 )` (35); `            CALL EVOLHX2(V,X,NNP,ITO)` (36); `          END SELECT` (37); `          RLB(I) = V ** ( 1.D0 / 3.D0 )` (39); `        CASE( 3, 4 )` (41); `          CALL VECML2(RLB(I),X,3)` (43); `          RLB(I) = RLB(I) * 1.D-1` (44); `        END SELECT` (46); `      ENDDO` (48). [11-04 전수 검증 정정] |
| 50–78 | 시작 시 1행 DFLT_DAMP 루틴 안. 각 재료에서 GE가 양수이면 건너뛴다. 그 외에는 RLB_MIN을 1.D20으로 시작해 해당 재료 요소의 최솟값을 구한다. MYRANK가 양수이면 CG_MPI_ALLREDUCE_D(RLB_MIN,DMIN,1,2)를 호출한다. CK와 W4로 AMAT(4,IMAT)를 설정한다. RLB 해제와 루틴 끝을 포함한다. 원문: `      DO IMAT = 1, NMAT` (50); `        E   = AMAT(1,IMAT)` (52); `        RHO = AMAT(3,IMAT)` (53); `        GE  = AMAT(4,IMAT)` (54); `        IF( GE > 0.D0 ) CYCLE` (56); `        RLB_MIN = 1.D20` (58); `        DO I = 1, NELM` (60); `          IF( IELM(4,I) == IMAT .AND. RLB(I) < RLB_MIN ) `<br>`     &      RLB_MIN = RLB(I)` (61–62); `        ENDDO` (63); `        IF( MYRANK > 0 ) THEN` (65); `          CALL CG_MPI_ALLREDUCE_D(RLB_MIN,DMIN,1,2)` (66); `          RLB_MIN = DMIN` (67); `        ENDIF` (68); `        CK = RLB_MIN * DSQRT( RHO / E )` (70); `        AMAT(4,IMAT) = CK * W4` (72); `      ENDDO` (74); `      DEALLOCATE( RLB )` (76); `      END` (78). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 22–46: ITYP와 NNP의 SELECT CASE에 CASE DEFAULT가 없다. ITYP가 2·6·3·4가 아닌 요소에는 RLB(I) 대입이 없다.
- 58–70: 재료에 대응하는 요소가 없을 때 RLB_MIN은 지역 계산에서 초기값 1.D20을 유지한다.
- 65–68: CG_MPI_ALLREDUCE_D 호출은 MYRANK>0 조건 안에 있다.
