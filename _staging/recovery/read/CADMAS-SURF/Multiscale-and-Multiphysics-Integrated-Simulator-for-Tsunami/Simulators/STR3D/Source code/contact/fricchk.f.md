---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/contact/fricchk.f
lines: 59
sha256: 0f32b41b56d36d1e5985ed108f25c9828a8010a49dc8d7b41acf63b59306854a
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fricchk.f — 판독 구간 기록

구간은 1행부터 59행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–11 | 루틴·암시적 자료형·배열을 선언한다(1–7). IFRIC의 첫 번째·여덟 번째 행을 0으로 초기화한다(9–10). 원문: `      SUBROUTINE FRICCHK(IFRIC,FRIC,NBDY,NINDC,ICBD,INDA,IEDA,ISLV` `     &                  ,ISLVO,FRTB,EDML,ITO)` (1–2, 하나의 고정형식 연속문); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION ISLVO(2,NINDC),ISLV(2,NINDC),IFRIC(10,NINDC)` `     &         ,FRIC(10,NINDC),INDA(NBDY),IEDA(NBDY),FRTB(3,NBDY,NBDY)` `     &         ,ICBD(NBDY),EDML(NBDY)` (5–7, 하나의 고정형식 연속문); `      IFRIC(1,:) = 0` (9); `      IFRIC(8,:) = 0` (10). |
| 12–59 | 시작 시 1행 FRICCHK 루틴 안이다. 물체별 INDA 범위를 정하고 접촉점을 순회한다(12–19). 현재 상태가 2·3이면 이전 상태가 같은지에 따라 IFRIC(1,I)를 2 또는 1로, 상태 12·13이면 1로 설정한다(20–34). IFRIC가 0이면 건너뛴다(35). 모서리·면 번호의 누적 상한으로 상대 물체를 찾고 FRIC(1,I)·FRIC(2,I)·FRIC(4,I)를 FRTB와 EDML로 계산한다(36–50). FRIC(1,I)가 0이면 IFRIC(1,I)를 0으로 설정하고 이전 상태가 0인 활성 접촉에는 IFRIC(8,I)=1을 둔다(47–48). 상대 물체를 찾지 못하면 오류 메시지를 쓴다(54). 이어서 ERRSTP(90,ITO)를 호출한다(55). 루프·루틴을 닫는다(56–59). 원문: `      DO IBDY = 1, NBDY` (12); `        IF( IBDY == 1 ) THEN` (13); `          IS = 1` (14); `        ELSE` (15); `          IS = INDA(IBDY-1) + 1` (16); `        IE = INDA(IBDY)` (18); `        DO 10 I = IS, IE` (19); `          IF( ISLV(1,I) == 2 ) THEN` (20); `            IF( ISLVO(1,I) == 2 ) THEN` (21); `              IFRIC(1,I) = 2` (22); `            ELSE` (23); `              IFRIC(1,I) = 1` (24); `          ELSEIF( ISLV(1,I) == 3 ) THEN` (26); `            IF( ISLVO(1,I) == 3 ) THEN` (27); `              IFRIC(1,I) = 2` (28); `            ELSE` (29); `              IFRIC(1,I) = 1` (30); `          ELSEIF( ISLV(1,I) == 12 .OR. ISLV(1,I) == 13 ) THEN` (32); `            IFRIC(1,I) = 1` (33); `          IF( IFRIC(1,I) == 0 ) GOTO 10` (35); `          MA = ISLV(2,I)` (36); `          DO JBDY = 1, NBDY` (37); `            IF( ISLV(1,I) == 2 .OR. ISLV(1,I) == 12 ) THEN` (38); `              MAE = IEDA(JBDY)` (39); `            ELSEIF( ISLV(1,I) == 3 .OR. ISLV(1,I) == 13 ) THEN` (40); `              MAE = ICBD(JBDY)` (41); `            IF( MA <= MAE ) THEN` (43); `              IFRIC(5,I) = IBDY` (44); `              IFRIC(6,I) = JBDY` (45); `              FRIC(1,I) = FRTB(1,IBDY,JBDY)` (46); `              IF( FRIC(1,I) == 0.D0 ) IFRIC(1,I) = 0` (47); `              IF( IFRIC(1,I) > 0 .AND. ISLVO(1,I) == 0 ) IFRIC(8,I) = 1` (48); `              FRIC(2,I) = EDML(JBDY) * 1.D-2 * FRTB(2,IBDY,JBDY)` (49); `              FRIC(4,I) = FRTB(3,IBDY,JBDY)` (50); `              GOTO 10` (51); `          WRITE(ITO,'(/X,A)') 'STOP IN SUB. FRICCHK!'` (54); `          CALL ERRSTP(90,ITO)` (55). 20·26·32행 분기 사슬은 ELSE 없이 34행 ENDIF로 닫힌다. 38·40행 분기 사슬은 ELSE 없이 42행 ENDIF로 닫힌다. 두 `GOTO 10`의 대상은 `   10   CONTINUE`(56)이며 19행 `DO 10 I = IS, IE`의 종료점이다. [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 49: FRIC(2,I)는 EDML(JBDY)에 1.D-2와 FRTB(2,IBDY,JBDY)를 곱한다.
