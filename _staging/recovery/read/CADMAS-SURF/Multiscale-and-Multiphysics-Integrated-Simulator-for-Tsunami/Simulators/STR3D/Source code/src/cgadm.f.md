---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/cgadm.f
lines: 79
sha256: e89592fc36764885635055e34415c1749d4d26ffda0d0b1acfd8aefaf6df064f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cgadm.f — 판독 구간 기록

구간은 1행부터 79행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | CGADM의 암시적 형과 배열 크기를 선언한다. 해석: STF·ESTF는 각각 전역·요소 행렬이며 INDOF는 자유도 인덱스이다. 원문: `      SUBROUTINE CGADM(STF,ESTF,IDCR,NCR,IDSK,IDCG,INDOF,ISLV,ITO)` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      DIMENSION  STF(*),ESTF(*),IDCR(2,NCR),IDSK(*),INDOF(6,*),IDCG(*)` (4). [11-04 전수 검증 정정] |
| 6–47 | 시작 시 1행 CGADM 루틴 안. I·J 루프에서 ESTF의 상삼각 순번 IC를 진행한다. 양의 자유도만 조립(assembly)하며 ISLV의 1, 2:4, 11: 분기에 따라 M1·M2 순서를 정한다. 해당 저장 열을 찾으면 STF에 ESTF를 더하고 다음 J로 이동한다. 저장 위치를 찾지 못하면 76행 레이블 90으로 이동한다. 14–34행의 SELECT CASE에는 CASE DEFAULT가 없다. 비활성 I에서는 IC를 행 길이만큼 넘긴다. 원문: `      IC = 0` (6); `      DO I = 1, NCR` (7); `        L1 = INDOF( IDCR(2,I), IDCR(1,I) )` (8); `        IF( L1 > 0 ) THEN` (9); `          DO J = I, NCR` (10); `            IC = IC + 1` (11); `            L2 = INDOF( IDCR(2,J), IDCR(1,J) )` (12); `            IF( L2 <= 0 ) CYCLE` (13); `            SELECT CASE( ISLV )` (14); `            CASE( 1 )` (15); `              IF( L1 >= L2 ) THEN` (16); `                M1 = L1` (17); `                M2 = L2` (18); `              ELSE` (19); `                M1 = L2` (20); `                M2 = L1` (21); `              ENDIF` (22); `            CASE( 2:4 )` (23); `              IF( L1 <= L2 ) THEN` (24); `                M1 = L1` (25); `                M2 = L2` (26); `              ELSE` (27); `                M1 = L2` (28); `                M2 = L1` (29); `              ENDIF` (30); `            CASE( 11: )` (31); `              M1 = L1` (32); `              M2 = L2` (33); `            END SELECT` (34); `            DO K = IDSK(M1), IDSK(M1+1) - 1` (35); `              IF( IDCG(K) == M2 ) THEN` (36); `                STF(K) = STF(K) + ESTF(IC)` (37); `                GOTO 10` (38); `              ENDIF` (39); `            ENDDO` (40); `            GOTO 90` (41); `   10     ENDDO` (42); `        ELSE` (43); `          IC = IC + NCR - I + 1` (44); `        ENDIF` (45); `      ENDDO` (46). [11-04 전수 검증 보완] |
| 48–79 | 시작 시 1행 CGADM 루틴 안. ISLV가 4 이하이면 반환한다. 그 외에는 IC를 다시 시작하고 대각 다음 항부터 반대쪽 성분을 STF에 더한다. 저장 위치를 찾지 못하면 오류 메시지와 ERRSTP(90,ITO)를 실행한다. 반환문과 루틴 끝을 포함한다. 원문: `      IF( ISLV <= 4 ) RETURN` (48); `      IC = 0` (50); `      DO I = 1, NCR` (51); `        L1 = INDOF( IDCR(2,I), IDCR(1,I) )` (52); `        IF( L1 > 0 ) THEN` (53); `          IC = IC + 1` (54); `          DO J = I + 1, NCR` (55); `            IC = IC + 1` (56); `            L2 = INDOF( IDCR(2,J), IDCR(1,J) )` (57); `            IF( L2 <= 0 ) CYCLE` (58); `            M1 = L2` (59); `            M2 = L1` (60); `            DO K = IDSK(M1), IDSK(M1+1) - 1` (61); `              IF( IDCG(K) == M2 ) THEN` (62); `                STF(K) = STF(K) + ESTF(IC)` (63); `                GOTO 20` (64); `              ENDIF` (65); `            ENDDO` (66); `            GOTO 90` (67); `   20     ENDDO` (68); `        ELSE` (69); `          IC = IC + NCR - I + 1` (70); `        ENDIF` (71); `      ENDDO` (72); `      RETURN` (74); `   90 WRITE(ITO,*) 'NO ADRESS FOR [K], PROGRAM STOPPED.'` (76); `      CALL ERRSTP(90,ITO)` (77); `      END` (79). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–34: SELECT CASE에는 ISLV의 1, 2:4, 11: 분기만 있다. CASE DEFAULT는 없다.
