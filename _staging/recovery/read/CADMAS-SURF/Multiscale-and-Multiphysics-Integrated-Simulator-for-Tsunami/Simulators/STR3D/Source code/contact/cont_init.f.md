---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/cont_init.f
lines: 92
sha256: f5da201b2504f449317f6d7b17abacd30d63d86663013cbe5e01af4ea3d66125
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cont_init.f — 판독 구간 기록

구간은 1행부터 92행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–25 | CONT_INIT의 인수·배정밀도·배열 범위를 선언한다(1–10). KK에서 크기를 읽고 GRID를 POS에 복사한다(12–17). `CALL GSURF(POS(1,NNOD+1),POS,IELM,KK(37),NELM,IBEL,3)`을 호출한다(19). POS(:,1:NNOD+NIGSF)를 POSO에 복사한다(21). ISLV·RSLV의 1:NINDC 범위를 0으로 초기화한다(23–24). 원문(연속 표시는 같은 문장의 이어지는 행이다): `      SUBROUTINE CONT_INIT(ISLV,RSLV,POS,POSO,EDML,IFRIC,KK,NBDY,ICBD` (1); `     &                    ,IELC,INDA,INDC,IEDA,IEDG,IELQ,IFCQ,IEDQ,IVRQ` (2); `     &                    ,ICTB,GRID,IELM,IBEL,ISLVG,EPS)` (3); `      IMPLICIT REAL*8(A-H,O-Z)` (5); `      DIMENSION KK(*),ISLV(2,*),RSLV(3,*),INDA(NBDY),INDC(*)` (6); `     &         ,ICTB(NBDY,NBDY),GRID(3,*),POS(3,*),POSO(3,*),IELM(*)` (7); `     &         ,IBEL(*),EDML(NBDY),IEDA(NBDY),IEDG(6,*),IFRIC(10,*)` (8); `     &         ,ICBD(NBDY),IELC(3,*),ISLVG(3,*),IELQ(4,*),IFCQ(*)` (9); `     &         ,IEDQ(*),IVRQ(*)` (10); `      NNOD  = KK(8)` (12); `      NELM  = KK(12)` (13); `      NIGSF = KK(94)` (14); `      NINDC = KK(95)` (15); `      POS(:,1:NNOD) = GRID(:,1:NNOD)` (17); `      CALL GSURF(POS(1,NNOD+1),POS,IELM,KK(37),NELM,IBEL,3)` (19); `      POSO(:,1:NNOD+NIGSF) = POS(:,1:NNOD+NIGSF)` (21); `      ISLV(:,1:NINDC) = 0` (23); `      RSLV(:,1:NINDC) = 0.` (24). [11-04 전수 검증 정정] |
| 26–58 | 시작 시 1–3행 CONT_INIT 루틴 안. IBDY·I·JBDY 루프에서 `ICTB(IBDY,JBDY) == 0`이면 JBDY를 건너뛴다(26–36). ADDSET4 범위별 VRTXSTK·EDGESTK 호출 뒤 ISLV(1,I)>0이면 10 레이블로 나간다(38–57). 원문(연속 표시는 같은 문장의 이어지는 행이다): `      DO IBDY = 1, NBDY` (26); `        CALL ADDSET4(IS,IE,INDA,IBDY)` (28); `        DO I = IS, IE` (30); `          IND = INDC(I)` (32); `          DO JBDY = 1, NBDY` (34); `            IF( ICTB(IBDY,JBDY) == 0 ) CYCLE` (36); `            CALL ADDSET4(JS,JE,INDA,JBDY)` (38); `            DO J = JS, JE` (40); `              CALL VRTXSTK(ISLV(1,I),POS(1,IND),INDC(J),POS,EPS)` (42); `              IF( ISLV(1,I) > 0 ) GOTO 10` (44); `            ENDDO` (46); `            CALL ADDSET4(JS,JE,IEDA,JBDY)` (48); `            DO J = JS, JE` (50); `              CALL EDGESTK(ISLV(1,I),RSLV(1,I),POS(1,IND),J,IEDG(1,J)` (52); `     &                    ,POS,EPS)` (53); `              IF( ISLV(1,I) > 0 ) GOTO 10` (55); `            ENDDO` (57). [11-04 전수 검증 정정] |
| 59–92 | 시작 시 `DO IBDY = 1, NBDY`(26), `DO I = IS, IE`(30), `DO JBDY = 1, NBDY`(34) 안이다. 루프는 각각 74·72·70행 `ENDDO`에서 닫힌다. `GOTO 10`의 대상은 72행 I 루프의 `ENDDO`이다. ADDSET4가 넘긴 JS:JE 범위에서 FACESTK를 호출한다(59–64). `ISLV(1,I) > 0`이면 10 레이블로 간다(66). 루프 종료 후 CIRCHK를 호출한다(76–77). LENGTH 호출의 DIST를 누적한 뒤 `IE - IS + 1`로 나누어 EDML에 저장한다(79–87). IFRIC(:,1:NINDC)를 0으로 초기화한다(89). 그 뒤 IFRIC(3,1:NINDC)를 1로 정한다(90). 해석: LENGTH 호출의 인수는 모서리 양 끝점의 거리를 구하는 형태이다. 원문(연속 표시는 같은 문장의 이어지는 행이다): `            CALL ADDSET4(JS,JE,ICBD,JBDY)` (59); `            DO J = JS, JE` (61); `              CALL FACESTK(ISLV(1,I),RSLV(1,I),POS(1,IND),J,IELC(1,J)` (63); `     &                    ,POS,EPS)` (64); `              IF( ISLV(1,I) > 0 ) GOTO 10` (66); `            ENDDO` (68); `          ENDDO` (70); `   10   ENDDO` (72); `      ENDDO` (74); `      CALL CIRCHK(ISLV,ISLVG,NNOD,NINDC,INDC,IEDG,IELC,IELQ,IFCQ,IEDQ` (76); `     &           ,IVRQ)` (77); `      DO IBDY = 1, NBDY` (79); `        CALL ADDSET4(IS,IE,IEDA,IBDY)` (80); `        EDML(IBDY) = 0.` (81); `        DO J = IS, IE` (82); `          CALL LENGTH(DIST,POS(1,IEDG(1,J)),POS(1,IEDG(2,J)),3)` (83); `          EDML(IBDY) = EDML(IBDY) + DIST` (84); `        ENDDO` (85); `        EDML(IBDY) = EDML(IBDY) / ( IE - IS + 1 )` (86); `      ENDDO` (87); `      IFRIC(:,1:NINDC) = 0` (89); `      IFRIC(3,1:NINDC) = 1` (90); `      END` (92). [11-04 전수 검증 보완] [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 79–86: EDML은 IE-IS+1로 나눈다. 이 루틴 안에는 그 분모가 0인지 검사하는 분기가 없다.
- 42–66: 초기 접촉 탐색은 꼭짓점, 모서리, 면 순서이다. 각 탐색에서 ISLV(1,I)>0이 되면 나머지 후보를 건너뛴다.
