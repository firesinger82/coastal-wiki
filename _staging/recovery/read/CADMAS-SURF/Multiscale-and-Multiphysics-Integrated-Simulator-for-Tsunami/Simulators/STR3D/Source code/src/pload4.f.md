---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/pload4.f
lines: 69
sha256: 989bf19dcd0a04dfa2bad2e6de13215afb24be4dfcc705c3973776e4a4aad2de
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# pload4.f — 판독 구간 기록

구간은 1행부터 69행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | PLOAD4 입구와 암시적 형·배열 선언이다(1–5). 원문: `      SUBROUTINE PLOAD4(NN,NPL4,PLD4,IELM,NM,ICRD,TR,GRID,SI,FT,ITO)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION NPL4(4,NN),IELM(NM,*),GRID(3,*),PLD4(4,NN),FC(3,9)`<br>`     &         ,NOD(9),FT(6,*),ICRD(*),TR(*),PRESS(9)` (4–5) |
| 7–69 | 시작 시 PLOAD4 루틴(1) 안이다. 하중별로 균일 PRESS를 설정한다(7–11). ITYPE==1이면 SHIFT0과 면 절점 수별 하중 루틴을 호출한다(12–21). 그 외에는 요소 절점 수와 NODOP에 따라 NODSET1·NODSET2·NODSET3·NODSET5 및 LOADTR1·LOADTR2·LOADQU2를 호출한다(22–64). 각 하중의 FC를 FRCADD로 조립한다(65–66). 원문: `      DO 100 I=1,NN` (7); `        IENO=NPL4(1,I)` (8); `        ITYPE=IELM(2,IENO)` (9); `        ID=NPL4(4,I)` (10); `        PRESS=PLD4(1,I)` (11); `        IF(ITYPE.EQ.1)THEN` (12); `          ND=IELM(3,IENO)` (13); `          CALL SHIFT0(NOD,IELM(8,IENO),ND)` (14); `          IF(ND.EQ.3) THEN` (15); `            CALL LOADTR1(GRID,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC,ITO)` (16); `          ELSEIF(ND.EQ.6) THEN` (17); `            CALL LOADTR2(GRID,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC,ITO)` (18); `          ELSE` (19); `            CALL LOADQU2(GRID,ND,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC,ITO)` (20); `          ENDIF` (21); `        ELSE` (22); `          NODCOR=NPL4(2,I)` (23); `          NODOP=NPL4(3,I)` (24); `          IF(IELM(3,IENO).EQ.4) THEN` (25); `            ND=3` (26); `            CALL NODSET1(IELM(8,IENO),NODOP,NOD,ITO)` (27); `            CALL LOADTR1(GRID,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC,ITO)` (28); `          ELSEIF(IELM(3,IENO).EQ.10) THEN` (29); `            ND=6` (30); `            CALL NODSET2(IELM(8,IENO),NODOP,NOD,ITO)` (31); `            CALL LOADTR2(GRID,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC,ITO)` (32); `          ELSEIF(IELM(3,IENO).EQ.6) THEN` (33); `            IF(NODOP.EQ.0) THEN` (34); `              ND=3` (35); `              CALL NODSET5(ND,IELM(8,IENO),NODCOR,NODOP,NOD,ITO)` (36); `              CALL LOADTR1(GRID,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC,ITO)` (37); `            ELSE` (38); `              ND=4` (39); `              CALL NODSET5(ND,IELM(8,IENO),NODCOR,NODOP,NOD,ITO)` (40); `              CALL LOADQU2(GRID,ND,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC`<br>`     &                    ,ITO)` (41–42); `            ENDIF` (43); `          ELSEIF(IELM(3,IENO).EQ.15) THEN` (44); `            IF(NODOP.EQ.0) THEN` (45); `              ND=6` (46); `              CALL NODSET5(ND,IELM(8,IENO),NODCOR,NODOP,NOD,ITO)` (47); `              CALL LOADTR2(GRID,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC,ITO)` (48); `            ELSE` (49); `              ND=8` (50); `              CALL NODSET5(ND,IELM(8,IENO),NODCOR,NODOP,NOD,ITO)` (51); `              CALL LOADQU2(GRID,ND,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC`<br>`     &                    ,ITO)` (52–53); `            ENDIF` (54); `          ELSEIF(IELM(3,IENO).EQ.8) THEN` (55); `            ND=4` (56); `            CALL NODSET3(ND,IELM(8,IENO),NODCOR,NODOP,NOD,ITO)` (57); `            CALL LOADQU2(GRID,ND,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC,ITO)` (58); `          ELSEIF(IELM(3,IENO).EQ.20) THEN` (59); `            ND=8` (60); `            CALL NODSET3(ND,IELM(8,IENO),NODCOR,NODOP,NOD,ITO)` (61); `            CALL LOADQU2(GRID,ND,NOD,PRESS,PLD4(2,I),ID,ICRD,TR,FC,ITO)` (62); `          ENDIF` (63); `        ENDIF` (64); `        CALL FRCADD(ND,FC,NOD,SI,FT)` (65); `  100 CONTINUE` (66); `      RETURN` (68); `      END` (69) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 25–65: 체적 요소의 절점 수 분기는 4·10·6·15·8·20을 처리한다. 그 밖의 절점 수를 처리하는 ELSE는 없으며, FRCADD는 이 분기 뒤에 있다.
