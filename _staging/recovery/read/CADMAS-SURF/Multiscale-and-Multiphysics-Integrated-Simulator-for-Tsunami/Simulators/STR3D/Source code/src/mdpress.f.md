---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/mdpress.f
lines: 74
sha256: 65ca7df3fabcded6b2acbd8dba0d89f3558f18a7cd2c5b057d8b91dbb31cc668
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mdpress.f — 판독 구간 기록

구간은 1행부터 74행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–27 | MDPRESS의 배열·논리 함수 선언과 G의 DATA이다. 해석: G는 중력가속도(gravitational acceleration)이다. IPND >= 0인 절점은 내부에서 IPND == 2일 때만 압력을 갱신하고 다음 절점으로 이동한다. 초기 시퀀스·시간 조건이면 수위 식을 사용하고 ELSE에서는 PG를 복사한다. 나머지 절점은 RL_MIN과 위치를 준비한다. 원문: 연속문(1–2): `      SUBROUTINE MDPRESS(IPND,PRESS,NNOD,NIELG,GRID,POS,PG,IELC,GELC` (1)； `     &                  ,IELG,TIM,WLEVEL,ALEVEL,ISEQ)` (2)； `      IMPLICIT REAL*8 (A-H,O-Z)` (4)； `      LOGICAL AREAIN` (5)； 연속문(6–7): `      DIMENSION IPND(NNOD),PRESS(NNOD),POS(3,*),PG(*),IELC(3,*),GELC(*)` (6)； `     &         ,IELG(NIELG),X(3,4),XG(3),RL(3),RN(3),GRID(3,NNOD)` (7)； `      DATA G /9.8D0/` (8)； `      DO I = 1, NNOD` (10)； `        IF( IPND(I) >= 0 ) THEN` (12)； `          IF( IPND(I) == 2 ) THEN` (13)； `            IF( ISEQ == 0 .AND. TIM == 0.D0 ) THEN` (14)； 연속문(15–16): `              PRESS(I) = ( WLEVEL - GRID(3,I) ) * G * 1.D3` (15)； `     &                 + ( ALEVEL - WLEVEL ) * G` (16)； `            ELSE` (17)； `              PRESS(I) = PG(I)` (18)； `            ENDIF` (19)； `          ENDIF` (20)； `          CYCLE` (21)； `        ENDIF` (22)； `        RL_MIN = -1.D0` (24)； `        X(:,4) = POS(:,I)` (26)。 [11-04 전수 검증 정정] |
| 28–43 | 시작 시 1행 MDPRESS 루틴과 10행 `DO I = 1, NNOD` 안이다. 이 루프는 72행 ENDDO에서 닫힌다. 12행 `IF( IPND(I) >= 0 ) THEN`의 21행 CYCLE을 실행하지 않아 탐색 진입 시 IPND(I) < 0이다. IELG를 순회한다. MEAN3·LENGTH 호출 뒤 `DIST > 2.D0*GELC(JP)`이면 CYCLE한다. AREACD 호출 뒤 `DABS(H) >= GELC(JP)`이면 CYCLE한다. 해석: DIST는 거리이고 H는 높이이다. 원문: `        DO J = 1, NIELG` (28)； `          JP = IELG(J)` (30)； `          X(:,1:3) = POS(:,IELC(:,JP))` (32)； `          CALL MEAN3(XG,X,3,3)` (34)； `          CALL LENGTH(DIST,X(1,4),XG,3)` (36)； `          IF( DIST > 2.D0*GELC(JP) ) CYCLE` (38)； `          CALL AREACD(RL,RN,H,X)` (40)； `          IF( DABS(H) >= GELC(JP) ) CYCLE` (42)。 [11-04 전수 검증 정정] |
| 44–74 | 시작 시 1행 MDPRESS 루틴과 10행 `DO I = 1, NNOD` 및 28행 `DO J = 1, NIELG` 안이다. J 루프는 70행에서 닫히고 I 루프는 72행에서 닫힌다. `AREAIN(RL,1.D-2)`가 참이면 IPND=2로 한다. `ISEQ == 0 .AND. TIM == 0.D0`이면 WLEVEL·GRID·ALEVEL 식을 쓴다. ELSE에서는 RL로 가중한 PG 합을 쓴다. 이어서 54행 EXIT로 J 루프를 벗어난다. 첫 AREAIN이 거짓이고 `AREAIN(RL,1.D-1)`이 참인 경우에는 `MINVAL(RL) > RL_MIN`일 때만 RL_MIN·IPND·PRESS를 갱신한다. AREAIN 분기 사슬에는 마지막 ELSE가 없다. 해석: 두 AREAIN 인수는 엄격한 허용범위와 넓은 허용범위에 대응한다. 원문: `          IF( AREAIN(RL,1.D-2) ) THEN` (44)； `            IPND(I) = 2` (45)； `            IF( ISEQ == 0 .AND. TIM == 0.D0 ) THEN` (46)； 연속문(47–48): `              PRESS(I) = ( WLEVEL - GRID(3,I) ) * G * 1.D3` (47)； `     &                 + ( ALEVEL - WLEVEL ) * G` (48)； `            ELSE` (49)； 연속문(50–52): `              PRESS(I) = RL(1) * PG( IELC(1,JP) )` (50)； `     &                 + RL(2) * PG( IELC(2,JP) )` (51)； `     &                 + RL(3) * PG( IELC(3,JP) )` (52)； `            ENDIF` (53)； `            EXIT` (54)； `          ELSEIF( AREAIN(RL,1.D-1) ) THEN` (55)； `            IF( MINVAL(RL) > RL_MIN ) THEN` (56)； `              RL_MIN = MINVAL(RL)` (57)； `              IPND(I) = 2` (58)； `              IF( ISEQ == 0 .AND. TIM == 0.D0 ) THEN` (59)； 연속문(60–61): `                PRESS(I) = ( WLEVEL - GRID(3,I) ) * G * 1.D3` (60)； `     &                   + ( ALEVEL - WLEVEL ) * G` (61)； `              ELSE` (62)； 연속문(63–65): `                PRESS(I) = RL(1) * PG( IELC(1,JP) )` (63)； `     &                   + RL(2) * PG( IELC(2,JP) )` (64)； `     &                   + RL(3) * PG( IELC(3,JP) )` (65)； `              ENDIF` (66)； `            ENDIF` (67)； `          ENDIF` (68)； `        ENDDO` (70)； `      ENDDO` (72)； `      END` (74)。 [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8·15–16·47–48·60–61: G는 9.8D0로 고정한다. 초기 압력식의 첫 수위 항에는 1.D3를 곱하고 두 번째 수위 항에는 곱하지 않는다.
- 12–22: IPND가 0 이상이면서 2가 아닌 절점의 PRESS에는 이 분기에서 대입하지 않는다.
- 24–70: 후보가 조건을 만족하지 않을 때 PRESS를 초기화하는 문장은 해당 탐색 구간에 없다.
