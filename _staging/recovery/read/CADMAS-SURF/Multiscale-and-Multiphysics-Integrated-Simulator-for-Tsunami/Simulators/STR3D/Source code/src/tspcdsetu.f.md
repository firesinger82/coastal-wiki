---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/tspcdsetu.f
lines: 101
sha256: cee5a34b6cecc860e19aaf73e94a48091ad40028dc50e32c260103a64ccfcf5e
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# tspcdsetu.f — 판독 구간 기록

구간은 1행부터 101행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | TSPCDSETU 입구와 배열 선언이다(1–8). IDLOAD와 일치하는 IDLD를 찾아 ADDSET으로 펼치고 조합 계수 S를 가져온다(10–22). 원문: `      SUBROUTINE TSPCDSETU(DUG,IDLOAD,KK,IDLD,SDLD,SIDL,LIDL,ITL1,ITD1`<br>`     &                    ,TBD1,ISPD,NSPD,SPCD,UG1,UG2,TIM3,DT1,DT2`<br>`     &                    ,IDYN)` (1–3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION KK(*),IDLD(2,*),SDLD(*),SIDL(*),LIDL(*),ITL1(4,*)`<br>`     &         ,ISPD(2,*),NSPD(7,*),SPCD(6,*),ITD1(*),TBD1(2,*),UG1(6,*)`<br>`     &         ,UG2(6,*),DUG(6,*)` (6–8); `      NDLD  = KK(66)` (10); `      NTLD1 = KK(77)` (11); `      IDLFLG=0` (13); `      DO 100 I=1,NDLD` (15); `        IF( IDLD(1,I) .EQ. IDLOAD ) THEN` (16); `          CALL ADDSET(I,IDLD,IS,NN)` (17); `          S=SDLD(I)` (18); `          IDLFLG=1` (19); `          GOTO 200` (20); `        ENDIF` (21); `  100 CONTINUE` (22) `GOTO 200`(20)의 대상은 24행이다. [11-04 전수 검증 보완] |
| 24–64 | 시작 시 TSPCDSETU 루틴(1) 안이다. IDLFLG==1이면 하위 LI·SI를 순회한다(24–34). IDYN==0이고 ITYPE>=2이면 현재 J 반복을 건너뛴다(36). 일치하는 ITYPE>0에서 ITYPE==1이면 TIM3, 그 외에는 TIM3-DT2를 사용한다(38–46). ADDSET2·INTPL로 계수를 구해 S·SI를 곱하고 SPCDSETDU를 호출한다(48–63). 원문: `  200 IF(IDLFLG .EQ. 1) THEN` (24); `        DO 300 I=1,NN` (26); `          LI=LIDL(IS-1+I)` (28); `          SI=SIDL(IS-1+I)` (29); `          DO 310 J=1,NTLD1` (31); `            ID=ITL1(1,J)` (33); `            ITYPE=ITL1(3,J)` (34); `            IF( IDYN .EQ. 0 .AND. ITYPE .GE. 2 ) CYCLE` (36); `            IF( ID .EQ. LI .AND. ITYPE .GT. 0 ) THEN` (38); `              IEX=ITL1(2,J)` (40); `              IF( ITYPE .EQ. 1 ) THEN` (42); `                TIM=TIM3` (43); `              ELSE` (44); `                TIM=TIM3-DT2` (45); `              ENDIF` (46); `              ITF=ITL1(4,J)` (48); `              CALL ADDSET2(ITF,ITD1,IP,N)` (49); `              CALL INTPL(FAC,TIM,TBD1(1,IP),N)` (51); `              FAC=FAC*S*SI` (52); `              CALL SPCDSETDU(IEX,DUG,KK,ISPD,NSPD,SPCD,FAC,ITYPE,UG1,UG2`<br>`     &                      ,DT1,DT2)` (54–55); `              GOTO 300` (57); `            ENDIF` (59); `  310     CONTINUE` (61); `  300   CONTINUE` (63) `GOTO 300`(57)의 대상은 63행이다. [11-04 전수 검증 정정] |
| 65–101 | 시작 시 TSPCDSETU 루틴(1)·IDLFLG 분기(24) 안이다. ELSE(65)는 직접 IDLOAD에 일치하는 시간 하중을 찾는다(67–74). ITYPE별 평가 시각을 정하고 ADDSET2·INTPL·SPCDSETDU를 호출한 뒤 반환한다(76–101). 원문: `      ELSE` (65); `        DO 410 J=1,NTLD1` (67); `          ID=ITL1(1,J)` (69); `          ITYPE=ITL1(3,J)` (70); `          IF( IDYN .EQ. 0 .AND. ITYPE .GE. 2 ) CYCLE` (72); `          IF( ID .EQ. IDLOAD .AND. ITYPE .GT. 0 ) THEN` (74); `            IEX=ITL1(2,J)` (76); `            IF( ITYPE .EQ. 1 ) THEN` (78); `              TIM=TIM3` (79); `            ELSE` (80); `              TIM=TIM3-DT2` (81); `            ENDIF` (82); `            ITF=ITL1(4,J)` (84); `            CALL ADDSET2(ITF,ITD1,IP,N)` (85); `            CALL INTPL(FAC,TIM,TBD1(1,IP),N)` (87); `            CALL SPCDSETDU(IEX,DUG,KK,ISPD,NSPD,SPCD,FAC,ITYPE,UG1,UG2`<br>`     &                    ,DT1,DT2)` (89–90); `            GOTO 500` (92); `          ENDIF` (94); `  410   CONTINUE` (96); `      ENDIF` (98); `  500 RETURN` (100); `      END` (101) 바깥 블록은 `IF(IDLFLG .EQ. 1) THEN`(24)이며 98행에서 닫힌다. `GOTO 500`(92)의 대상은 100행의 RETURN이다. [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
