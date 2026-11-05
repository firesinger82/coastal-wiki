---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/wtsol.f
lines: 89
sha256: 536a0a5e33ed2469bd0e2f40dd576cd7e2b603763d3ce2193da9e606dfd7543a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# wtsol.f — 판독 구간 기록

구간은 1행부터 89행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–34 | WTSOL 입구와 선언이다(1–6). ICW==0이면 응력 헤더를 쓴다(8). IPS부터 IPE까지 각 파트의 여섯 응력 성분을 출력하며 다섯째와 여섯째 성분의 순서를 교환한다(10–33). 원문: `      SUBROUTINE WTSOL( SIGG, EPSG, PRNSIGG, NNOD, IPS, IPE, NG_ENS,`<br>`     &                  IG_ENS, IFL, ICW )` (1–2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION SIGG(6,NNOD), EPSG(6,NNOD), PRNSIGG(3,NNOD), NG_ENS(*),`<br>`     &          IG_ENS(NNOD,*), IFL(*)` (5–6); `      IF( ICW == 0 ) WRITE(IFL(20),'(A)') 'solid stress'` (8); `      DO IP = IPS, IPE` (10); `        WRITE(IFL(20),'(A)') 'part'` (12); `        WRITE(IFL(20),'(I10)') IP` (13); `        WRITE(IFL(20),'(A)') 'coordinates'` (14); `        DO J = 1, 6` (16); `          IF( J == 5 ) THEN` (18); `            JJ = 6` (19); `          ELSEIF( J == 6 ) THEN` (20); `            JJ = 5` (21); `          ELSE` (22); `            JJ = J` (23); `          ENDIF` (24); `          DO I = 1, NG_ENS(IP)` (26); `            IG = IG_ENS(I,IP)` (27); `            WRITE(IFL(20),'(1PE12.4)') SIGG(JJ,IG)` (28); `          ENDDO` (29); `        ENDDO` (31); `      ENDDO` (33) |
| 35–67 | 시작 시 WTSOL 루틴(1) 안이다. ICW==0이면 변형률(strain) 헤더를 쓴다(35). 파트별 여섯 성분을 출력한다. 다섯째·여섯째 순서를 교환하며 JJ>=4에는 0.5 계수를 곱한다(37–66). 원문: `      IF( ICW == 0 ) WRITE(IFL(21),'(A)') 'solid strain'` (35); `      DO IP = IPS, IPE` (37); `        WRITE(IFL(21),'(A)') 'part'` (39); `        WRITE(IFL(21),'(I10)') IP` (40); `        WRITE(IFL(21),'(A)') 'coordinates'` (41); `        DO J = 1, 6` (43); `          IF( J == 5 ) THEN` (45); `            JJ = 6` (46); `          ELSEIF( J == 6 ) THEN` (47); `            JJ = 5` (48); `          ELSE` (49); `            JJ = J` (50); `          ENDIF` (51); `          IF( JJ >= 4 ) THEN` (53); `            FAC = .5D0` (54); `          ELSE` (55); `            FAC = 1.D0` (56); `          ENDIF` (57); `          DO I = 1, NG_ENS(IP)` (59); `            IG = IG_ENS(I,IP)` (60); `            WRITE(IFL(21),'(1PE12.4)') EPSG(JJ,IG) * FAC` (61); `          ENDDO` (62); `        ENDDO` (64); `      ENDDO` (66) |
| 68–89 | 시작 시 WTSOL 루틴(1) 안이다. ICW==0이면 주응력(principal stress) 헤더를 쓴다(68). 파트별 세 성분을 출력하고 ICW를 1로 설정한다(70–87). 원문: `      IF( ICW == 0 ) WRITE(IFL(22),'(A)') 'solid principal stress'` (68); `      DO IP = IPS, IPE` (70); `        WRITE(IFL(22),'(A)') 'part'` (72); `        WRITE(IFL(22),'(I10)') IP` (73); `        WRITE(IFL(22),'(A)') 'coordinates'` (74); `        DO J = 1, 3` (76); `          DO I = 1, NG_ENS(IP)` (78); `            IG = IG_ENS(I,IP)` (79); `            WRITE(IFL(22),'(1PE12.4)') PRNSIGG(J,IG)` (80); `          ENDDO` (81); `        ENDDO` (83); `      ENDDO` (85); `      ICW = 1` (87); `      END` (89) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 18–24·45–61: 응력·변형률 출력은 다섯째와 여섯째 성분을 교환한다. 변형률의 JJ>=4 성분에는 .5D0를 곱한다.
