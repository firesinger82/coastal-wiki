---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/cgadmg_s.f
lines: 50
sha256: 2744f571533bac865424ee80a21b86893bfa5003110ce6b6eb815e7b8f462763
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cgadmg_s.f — 판독 구간 기록

구간은 1행부터 50행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–31 | CGADMG_S의 암시적 형·배열 선언. 요소 상삼각 저장 순서의 IC를 센다. INDOP가 양수인 자유도만 처리한다. ISLV=1이면 큰 행 번호를 먼저 두고 ISLV=2:4이면 작은 행 번호를 먼저 둔다. 원문: `      SUBROUTINE CGADMG_S(STF,ELHM,KN,ND,IDSK,IDCG,INDOP,ISLV,ITO)` (1); `      IMPLICIT REAL*8 (A-H,O-Z)` (3); `      DIMENSION  STF(*),ELHM(*),KN(ND),IDSK(*),INDOP(*),IDCG(*)` (4); `      IC = 0` (6); `      DO I = 1, ND` (7); `        L1 = INDOP( KN(I) )` (8); `        IF( L1 > 0 ) THEN` (9); `          DO J = I, ND` (10); `            IC = IC + 1` (11); `            L2 = INDOP( KN(J) )` (12); `            IF( L2 <= 0 ) CYCLE` (13); `            SELECT CASE( ISLV )` (14); `            CASE( 1 )` (15); `              IF( L1 >= L2 ) THEN` (16); `                M1 = L1` (17); `                M2 = L2` (18); `              ELSE` (19); `                M1 = L2` (20); `                M2 = L1` (21); `              ENDIF` (22); `            CASE( 2:4 )` (23); `              IF( L1 <= L2 ) THEN` (24); `                M1 = L1` (25); `                M2 = L2` (26); `              ELSE` (27); `                M1 = L2` (28); `                M2 = L1` (29); `              ENDIF` (30); `            END SELECT` (31). |
| 32–50 | 시작 시 `DO I = 1, ND` (7, 종료 43), `IF( L1 > 0 ) THEN` (9, ELSE 40, 종료 42), `DO J = I, ND` (10, 레이블 10의 종료 39) 안. IDSK 구간에서 M2를 찾아 ELHM(IC)를 STF에 누적한다. 찾지 못하면 `GOTO 90` (38)으로 47행에 이동한다. 47행은 ITO에 오류 메시지를 쓴다. 48행은 ERRSTP(90,ITO)를 호출한다. L1이 양수가 아니면 남은 상삼각 항목 수만큼 IC를 건너뛴다. 원문: `            DO K = IDSK(M1), IDSK(M1+1) - 1` (32); `              IF( IDCG(K) == M2 ) THEN` (33); `                STF(K) = STF(K) + ELHM(IC)` (34); `                GOTO 10` (35); `              ENDIF` (36); `            ENDDO` (37); `            GOTO 90` (38); `   10     ENDDO` (39); `        ELSE` (40); `          IC = IC + ND - I + 1` (41); `        ENDIF` (42); `      ENDDO` (43); `      RETURN` (45); `   90 WRITE(ITO,*) 'NO ADRESS FOR [K], PROGRAM STOPPED.'` (47); `      CALL ERRSTP(90,ITO)` (48); `      END` (50). [11-04 전수 검증 정정] [11-04 전수 검증 보완] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 14–31: ISLV SELECT CASE에 1과 2:4만 있고 CASE DEFAULT는 없다.
