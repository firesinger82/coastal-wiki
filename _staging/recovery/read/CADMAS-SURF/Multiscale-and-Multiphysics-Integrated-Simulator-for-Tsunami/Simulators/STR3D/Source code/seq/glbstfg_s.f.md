---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/glbstfg_s.f
lines: 42
sha256: 3d0ac3db4ba979447f3bc2f7bcf858c903250079d57cb2b9e4cb701abaedccd9
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# glbstfg_s.f — 판독 구간 기록

구간은 1행부터 42행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–16 | GLBSTFG_S의 연속 인수·암시적 형·배열 선언. RR(7)에서 ALP를 얻고 DT1과 DT2의 산술평균 DT12를 계산한다. STF의 1:KK(20) 구간을 0으로 초기화한다. 원문: 연속문(1–2): `      SUBROUTINE GLBSTFG_S(STF,RHV,KK,RR,GRID,IELM,NM,AMAT,INDOP,IDSK` <br> `     &                    ,IDCG,DPG,DT1,DT2,IDYN,ITO)`; `      IMPLICIT REAL*8(A-H,O-Z)` (4); 연속문(5–7): `      DIMENSION KK(*),RR(*),IELM(NM,*),EKPP(210),ECPP(210),GRID(3,*)` <br> `     &         ,AMAT(33,*),ELHM(210),RHV(*),DPG(*),INDOP(*),STF(*)` <br> `     &         ,IDSK(*),IDCG(*)`; `      NELM = KK(12)` (9); `      ALP = RR(7)` (11); `      DT12 = .5D0 * ( DT1 + DT2 )` (13); `      STF(1:KK(20)) = 0.` (15). [11-04 전수 검증 정정] |
| 17–42 | GLBSTFG_S 루틴 안. 유형 6 요소만 처리한다. 상삼각 길이를 계산하고 GEOMTX_S를 호출한다. IDYN=1이면 ECPP/DT12*.5D0와 ALP*EKPP를 더한다. IDYN=0이면 EKPP를 사용한다. IF/ELSEIF 사슬에는 ELSE가 없다. SPCDRHVG_S로 경계 우변을 처리하고 CGADMG_S로 전역 조립한다. 원문: `      DO I = 1, NELM` (17); `        ITYP = IELM(2,I)` (19); `        IF( ITYP /= 6 ) CYCLE` (21); `        ND = IELM(3,I)` (23); `        IMAT = IELM(4,I)` (24); `        NN = ( ND + 1 ) * ND / 2` (26); `        CALL GEOMTX_S(EKPP,ECPP,ND,NN,IELM(8,I),GRID,AMAT(1,IMAT),ITO)` (28); `        IF( IDYN == 1 ) THEN` (30); `          ELHM(1:NN) = ECPP(1:NN) / DT12 * .5D0 + ALP * EKPP(1:NN)` (31); `        ELSEIF( IDYN == 0 ) THEN` (32); `          ELHM(1:NN) = EKPP(1:NN)` (33); `        ENDIF` (34); `        CALL SPCDRHVG_S(RHV,ELHM,IELM(8,I),ND,INDOP,DPG)` (36); `        CALL CGADMG_S(STF,ELHM,IELM(8,I),ND,IDSK,IDCG,INDOP,KK(21),ITO)` (38); `      ENDDO` (40); `      END` (42). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 30–38: ELHM 대입 분기는 IDYN=1과 IDYN=0뿐이다. 그 뒤 두 조립 호출은 조건 밖에 있다.
- 13·31: DT12를 계산하고 동적 경로에서 분모로 사용한다. 이 파일에는 DT12=0 검사문이 없다.
