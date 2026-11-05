---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_mdlndh.f
lines: 88
sha256: b10ba6fa118e3fc7cb3c65ca19d16eac09cdb9e1bbfdd1b99594d9a602ea6dfa
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_mdlndh.f — 판독 구간 기록

구간은 1행부터 88행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–38 | SF_MDLNDH 선언, INCLUDE 네 개와 배열 범위(1–11). DATA EPS=1.D-1을 둔다(13). IELM(3,IEL)=2인 요소의 절점(node)을 순회한다(15–21). I=MYIS이고 MYMIS=1일 때 XS에서 XX(2,I)*EPS를 뺀다(25–29). I=MYIE이고 MYMIE=1일 때 XE에 XX(2,I)*EPS를 더한다(31–35). GRID(1,IG)를 반열린 구간 XS<=GRID(1,IG)<XE로 검사한다(37). 해석: XX(2,I)는 셀 폭이고 이 보정은 해당 외곽 경계를 확장한다. 원문: `      SUBROUTINE SF_MDLNDH(LNDH,XX,YY,ZZ,IELM,GRID)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      INCLUDE 'VF_A0PRM.h'` (5)<br>`      INCLUDE 'VF_ANUMBI.h'` (6)<br>`      INCLUDE 'VF_APARAI.h'` (7)<br>`      INCLUDE 'SF_STRUCT.h'` (8)<br>연속문: `      DIMENSION XX(MAXG1,NUMI),YY(MAXG1,NUMJ),ZZ(MAXG1,NUMK)` (10); `     &         ,IELM(24,NELM),GRID(3,NNOD),LNDH(NUMI,NUMJ)` (11)<br>`      DATA EPS / 1.D-1 /` (13)<br>`      DO IEL = 1, NELM` (15)<br>`        IF( IELM(3,IEL) /= 2 ) CYCLE` (17)<br>`        DO 50 L = 1, IELM(4,IEL)` (19)<br>`          IG = IELM(4+L,IEL)` (21)<br>`          DO I = MYIS, MYIE` (23)<br>`            IF( I == MYIS .AND. MYMIS == 1 ) THEN` (25)<br>`              XS = XX(1,I) - XX(2,I) * EPS` (26)<br>`            ELSE` (27)<br>`              XS = XX(1,I)` (28)<br>`            ENDIF` (29)<br>`            IF( I == MYIE .AND. MYMIE == 1 ) THEN` (31)<br>`              XE = XX(1,I+1) + XX(2,I) * EPS` (32)<br>`            ELSE` (33)<br>`              XE = XX(1,I+1)` (34)<br>`            ENDIF` (35)<br>`            IF( GRID(1,IG) >= XS .AND. GRID(1,IG) < XE ) THEN` (37) [11-04 전수 검증 정정] |
| 39–88 | 시작 시 15행 `DO IEL = 1, NELM`, 19행 `DO 50 L = 1, IELM(4,IEL)`, 23행 `DO I = MYIS, MYIE`, 37행 `IF( GRID(1,IG) >= XS .AND. GRID(1,IG) < XE ) THEN` 안이다. 이 블록들은 역순으로 80행 `ENDIF`, 82행 `ENDDO`, 84행 `50 CONTINUE`, 86행 `ENDDO`에서 닫힌다. 71행 `GOTO 50`의 대상은 84행이다. J 루프에서 y 외곽 경계를 같은 방식으로 확장하고 YS<=y<YE를 검사한다(39–53). K=2:NUMK-1에서 위·아래 외곽을 확장하고 ZS<=z<ZE이면 LNDH(I,J)를 기존 값과 K의 최댓값으로 바꾼 뒤 GOTO 50으로 다음 절점으로 이동한다(55–84). 원문: `              DO J = MYJS, MYJE` (39)<br>`                IF( J == MYJS .AND. MYMJS == 1 ) THEN` (41)<br>`                  YS = YY(1,J) - YY(2,J) * EPS` (42)<br>`                ELSE` (43)<br>`                  YS = YY(1,J)` (44)<br>`                ENDIF` (45)<br>`                IF( J == MYJE .AND. MYMJE == 1 ) THEN` (47)<br>`                  YE = YY(1,J+1) + YY(2,J) * EPS` (48)<br>`                ELSE` (49)<br>`                  YE = YY(1,J+1)` (50)<br>`                ENDIF` (51)<br>`                IF( GRID(2,IG) >= YS .AND. GRID(2,IG) < YE ) THEN` (53)<br>`                  DO K = 2, NUMK - 1` (55)<br>`                    IF( K == 2 ) THEN` (57)<br>`                      ZS = ZZ(1,K) - ZZ(2,K) * EPS` (58)<br>`                    ELSE` (59)<br>`                      ZS = ZZ(1,K)` (60)<br>`                    ENDIF` (61)<br>`                    IF( K == NUMK - 1 ) THEN` (63)<br>`                      ZE = ZZ(1,K+1) + ZZ(2,K) * EPS` (64)<br>`                    ELSE` (65)<br>`                      ZE = ZZ(1,K+1)` (66)<br>`                    ENDIF` (67)<br>`                    IF( GRID(3,IG) >= ZS .AND. GRID(3,IG) < ZE ) THEN` (69)<br>`                      LNDH(I,J) = MAX0( K, LNDH(I,J) )` (70)<br>`                      GOTO 50` (71)<br>`                    ENDIF` (72)<br>`                  ENDDO` (74)<br>`                ENDIF` (76)<br>`              ENDDO` (78)<br>`            ENDIF` (80)<br>`          ENDDO` (82)<br>`   50   CONTINUE` (84)<br>`      ENDDO` (86)<br>`      END` (88) [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 70: LNDH는 MAX0(K,LNDH(I,J))로 갱신한다. 이 루틴에는 LNDH 전체의 초기화 대입이 없다.
