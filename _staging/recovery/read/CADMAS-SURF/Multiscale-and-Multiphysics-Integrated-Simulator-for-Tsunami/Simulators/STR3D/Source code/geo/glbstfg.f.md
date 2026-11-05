---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/glbstfg.f
lines: 64
sha256: fdbf09dddd3f53f741055b1376f709a642eaf2b5331a30a1160f836f4675c191
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# glbstfg.f — 판독 구간 기록

구간은 1행부터 64행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–21 | GLBSTFG는 전역 결합 행렬을 조립(assembly)한다. IMPLICIT와 6–11행 연속 DIMENSION을 아래에 적었다. KK(12)·KK(29)·KK(32)를 각각 NELM·NELMC·NELMX에 대입한다. 해석: 각 값은 기본·접촉·추가 요소 수로 보인다. RR(4)·RR(7)에서 BETA·ALP를 얻고 두 시간 간격의 평균 DT12를 계산한다. 원문: `      SUBROUTINE GLBSTFG(STF,RHV,KK,NCRMAX,NRAMAX,RR,GRID,IELM,NM` (1); `     &                  ,AMAT,INDOF,INDMPC,MPCF,RMPC,INDOP,IDSK,IDCG` (2); `     &                  ,DUG,DPG,DT1,DT2,ITER,ITER2,IMPC,IDYN,ITO)` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION KK(*),RR(*),IELM(NM,*),EKUP(1200),EKPP(400),ECPU(1200)` (6); `     &         ,ECPP(400),EMPU(1200),GRID(3,*),AMAT(33,*)` (7); `     &         ,ELHM12(NCRMAX*20),ELHM21(20*NCRMAX),ELHM22(400)` (8); `     &         ,RAMBDA(NRAMAX),INDOF(6,*),INDMPC(2,6,*),MPCF(*),RMPC(*)` (9); `     &         ,IDCR(2,NCRMAX),RHV(*),DUG(6,*),DPG(*),INDOP(*),STF(*)` (10); `     &         ,IDSK(*),IDCG(*)` (11); `      NELM = KK(12)` (13); `      NELMC = KK(29)` (14); `      NELMX = KK(32)` (15); `      BETA = RR(4)` (17); `      ALP = RR(7)` (18); `      DT12 = .5D0 * ( DT1 + DT2 )` (20) [11-04 전수 검증 정정] |
| 22–40 | 전체 요소 범위에서 NELM 다음 NELMC개 구간은 건너뛴다. 유형 ITYP=6만 처리한다. ND·재료 번호 IMAT를 읽고 ND3·N12·N21·N22 크기를 계산한다. GEOMTX로 다섯 요소 행렬을 구한다. 38–39행은 한 호출문이다. 원문: `      DO I = 1, NELM + NELMC + NELMX` (22); `        IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE` (24); `        ITYP = IELM(2,I)` (26); `        IF( ITYP /= 6 ) CYCLE` (28); `        ND = IELM(3,I)` (30); `        IMAT = IELM(4,I)` (31); `        ND3 = ND * 3` (33); `        N12 = ND3 * ND` (34); `        N21 = ND * ND3` (35); `        N22 = ND * ND` (36); `        CALL GEOMTX(EKUP,EKPP,ECPU,ECPP,EMPU,ND,ND3,IELM(8,I),GRID` (38); `     &             ,AMAT(1,IMAT),ITO)` (39) |
| 41–64 | 시작 시 22행 `DO I = 1, NELM + NELMC + NELMX` 안이다. 이 루프는 62행 `ENDDO`에서 닫힌다. 이 구간에 도달하려면 24행 `IF( I > NELM .AND. I <= NELM + NELMC ) CYCLE`과 28행 `IF( ITYP /= 6 ) CYCLE`을 모두 통과해야 한다. IDYN=1은 BETA·ALP·DT2·DT12로 ELHM12·ELHM21·ELHM22를 구성한다. ELSEIF IDYN=0은 정적(static) 행렬을 설정한다. MPCTRNSG로 다점 구속(multipoint constraint) 변환을 수행한다. ITER=1이며 ITER2=1일 때 SPCDRHVG로 우변을 보정한다. CGADMG로 전역 행렬에 더한다. 연속 계산식·조건·호출은 아래와 같다. 원문: `        IF( IDYN == 1 ) THEN` (41); `          ELHM12(1:N12) = -BETA * EKUP(1:N12)` (42); `          ELHM21(1:N21) = EMPU(1:N21) / ( DT2 * DT12 )` (43); `     &                    + ECPU(1:N21) / DT12 * .5D0` (44); `          ELHM22(1:N22) = ECPP(1:N22) / DT12 * .5D0 + ALP * EKPP(1:N22)` (45); `        ELSEIF( IDYN == 0 ) THEN` (46); `          ELHM12(1:N12) = -EKUP(1:N12)` (47); `          ELHM21(1:N21) = 0.` (48); `          ELHM22(1:N22) = EKPP(1:N22)` (49); `        ENDIF` (50); `        CALL MPCTRNSG(IMPC,IELM(8,I),ND,3,ND3,RAMBDA,NRAMAX,INDOF,INDMPC` (52); `     &               ,MPCF,RMPC,ELHM12,ELHM21,IDCR,NCR)` (53); `        IF( ITER == 1 .AND. ITER2 == 1 ) ` (55); `     &    CALL SPCDRHVG(RHV,ELHM12,ELHM21,ELHM22,DUG,DPG,IELM(8,I),ND` (56); `     &                 ,IDCR,NCR,INDOF,INDOP)` (57); `        CALL CGADMG(STF,ELHM12,ELHM21,ELHM22,IELM(8,I),ND,IDCR,NCR,INDOF` (59); `     &             ,INDOP,IDSK,IDCG,ITO)` (60); `      ENDDO` (62); `      END` (64) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6–8: EKUP·ECPU·EMPU 작업 배열은 1200, EKPP·ECPP·ELHM22 작업 배열은 400 원소로 고정되어 있다.
- 41–50: IDYN=1·0 이외에 ELHM12·ELHM21·ELHM22를 대입하는 ELSE는 없다.
- 43–45: 동적(dynamic) 식에 DT2·DT12 분모가 있다. 이 루틴에는 분모의 0 검사문이 없다.
