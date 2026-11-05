---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/glb_comm/fricchk0.f
lines: 66
sha256: 84c0134e5e7c8c1ebc1d6498359c9535fa0d78599ee7b790d183c263173f3ca5
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# fricchk0.f — 판독 구간 기록

구간은 1행부터 66행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 암시적 배정밀도와 접촉·마찰·요소 변환 배열의 첨자 범위를 선언한다(1–8). IFRIC의 첫째·여덟째 행만 0으로 초기화한다(10–11). 원문: `      SUBROUTINE FRICCHK0(IFRIC,FRIC,NBDY,NINDC,ICBD,INDA,IEDA,ISLV` (1); `     &                   ,ISLVO,FRTB,EDML,ISLVP,IEG,MIEG,IEC,MIEC,ITO)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION ISLVO(2,NINDC),ISLV(2,NINDC),IFRIC(10,NINDC)` (5); `     &         ,FRIC(10,NINDC),INDA(NBDY),IEDA(NBDY),FRTB(3,NBDY,NBDY)` (6); `     &         ,ICBD(NBDY),EDML(NBDY),ISLVP(NINDC),IEG(MIEG,*)` (7); `     &         ,IEC(MIEC,*)` (8); `C----&------------------------------------------------------------------` (9); `      IFRIC(1,:) = 0` (10); `      IFRIC(8,:) = 0` (11). |
| 13–43 | 시작 시 1행 fricchk0 루틴 안. 물체 IBDY의 INDA 누적 범위로 IS·IE를 정한다(13–20). 현재 상태 2·3에서는 이전 상태가 같으면 IFRIC(1,I)=2, 다르면 1로 설정한다(21–32). 상태 12·13은 IFRIC(1,I)를 1로 설정한다(33–34). `IF( IFRIC(1,I) == 0 ) GOTO 10`은 IFRIC(1,I)가 0일 때 63행 `10 CONTINUE`로 이동한다(36). 상태 종류에 따라 IEG·IEC로 MA를 변환한다(37–43). 21–35행과 39–43행의 IF 사슬에는 ELSE가 없다. 원문: `      DO IBDY = 1, NBDY` (13); `        IF( IBDY == 1 ) THEN` (14); `          IS = 1` (15); `        ELSE` (16); `          IS = INDA(IBDY-1) + 1` (17); `        ENDIF` (18); `        IE = INDA(IBDY)` (19); `        DO 10 I = IS, IE` (20); `          IF( ISLV(1,I) == 2 ) THEN` (21); `            IF( ISLVO(1,I) == 2 ) THEN` (22); `              IFRIC(1,I) = 2` (23); `            ELSE` (24); `              IFRIC(1,I) = 1` (25); `            ENDIF` (26); `          ELSEIF( ISLV(1,I) == 3 ) THEN` (27); `            IF( ISLVO(1,I) == 3 ) THEN` (28); `              IFRIC(1,I) = 2` (29); `            ELSE` (30); `              IFRIC(1,I) = 1` (31); `            ENDIF` (32); `          ELSEIF( ISLV(1,I) == 12 .OR. ISLV(1,I) == 13 ) THEN` (33); `            IFRIC(1,I) = 1` (34); `          ENDIF` (35); `          IF( IFRIC(1,I) == 0 ) GOTO 10` (36); `          MA = ISLV(2,I)` (37); `          IP = ISLVP(I)` (38); `          IF( ISLV(1,I) == 2 .OR. ISLV(1,I) == 12 ) THEN` (39); `            MA = IEG(MA,IP)` (40); `          ELSEIF( ISLV(1,I) == 3 .OR. ISLV(1,I) == 13 ) THEN` (41); `            MA = IEC(MA,IP)` (42); `          ENDIF` (43). [11-04 전수 검증 정정] |
| 44–66 | 시작 시 1행 fricchk0 루틴 안. 시작 시 13행 `DO IBDY = 1, NBDY` 안이며 이 루프는 64행 `ENDDO`에서 닫힌다. 시작 시 20행 `DO 10 I = IS, IE` 안이며 이 루프는 63행 `10 CONTINUE`에서 닫힌다. 45–49행 IF 사슬에는 ELSE가 없다. JBDY 루프에서 상태 2·12는 IEDA, 상태 3·13은 ICBD 경계를 사용한다(44–49). MA가 경계 이하이면 물체 쌍과 FRTB 계수를 기록한다(50–57). FRIC(1,I)가 0이면 마찰 상태를 끄며 이전 상태 0과 양수 마찰 상태 조합이면 IFRIC(8,I)=1이다(54–55). FRIC(2,I)는 EDML·1.D-2·FRTB의 곱이다(56). 대응 경계를 찾으면 표지 10으로 이동하고 찾지 못하면 ERRSTP(90,ITO)를 호출한다(58–64). 원문: `          DO JBDY = 1, NBDY` (44); `            IF( ISLV(1,I) == 2 .OR. ISLV(1,I) == 12 ) THEN` (45); `              MAE = IEDA(JBDY)` (46); `            ELSEIF( ISLV(1,I) == 3 .OR. ISLV(1,I) == 13 ) THEN` (47); `              MAE = ICBD(JBDY)` (48); `            ENDIF` (49); `            IF( MA <= MAE ) THEN` (50); `              IFRIC(5,I) = IBDY` (51); `              IFRIC(6,I) = JBDY` (52); `              FRIC(1,I) = FRTB(1,IBDY,JBDY)` (53); `              IF( FRIC(1,I) == 0.D0 ) IFRIC(1,I) = 0` (54); `              IF( IFRIC(1,I) > 0 .AND. ISLVO(1,I) == 0 ) IFRIC(8,I) = 1` (55); `              FRIC(2,I) = EDML(JBDY) * 1.D-2 * FRTB(2,IBDY,JBDY)` (56); `              FRIC(4,I) = FRTB(3,IBDY,JBDY)` (57); `              GOTO 10` (58); `            ENDIF` (59); `          ENDDO` (60); `          WRITE(ITO,'(/X,A)') 'STOP IN SUB. FRICCHK!'` (61); `          CALL ERRSTP(90,ITO)` (62); `   10   CONTINUE` (63); `      ENDDO` (64); `      END` (66). [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 10–11·21–35·53–57: IFRIC의 첫째·여덟째 행은 전체 초기화한다. FRIC의 계수 대입은 대응 JBDY를 찾은 분기에서만 실행한다.
