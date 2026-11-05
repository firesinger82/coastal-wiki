---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/cgadmg.f
lines: 61
sha256: 3854a4838bd330bef63efda88ce6668bc4c81e65cc11e22357f368db646d82b3
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# cgadmg.f — 판독 구간 기록

구간은 1행부터 61행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | CGADMG는 결합 요소 행렬(element matrix)을 전역 희소 행렬(sparse matrix) STF에 더한다. IMPLICIT·연속 DIMENSION 선언을 아래에 그대로 적었다. 첫 블록은 INDOF로 얻은 행과 INDOP로 얻은 열에 ELHM12를 더한다. 자유도(degree of freedom) 번호가 0 이하이면 건너뛴다. IDSK의 행 범위에서 IDCG가 열 번호와 일치하면 누적하고 다음 J로 이동한다. 찾지 못하면 오류 레이블 90으로 이동한다. 원문: `      SUBROUTINE CGADMG(STF,ELHM12,ELHM21,ELHM22,KN,ND,IDCR,NCR,INDOF` (1); `     &                 ,INDOP,IDSK,IDCG,ITO)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION INDOF(6,*),IDCR(2,NCR),INDOP(*),KN(ND),IDSK(*),IDCG(*)` (5); `     &         ,STF(*),ELHM12(NCR,ND),ELHM21(ND,NCR),ELHM22(ND,ND)` (6); `      DO I = 1, NCR` (8); `        II = INDOF(IDCR(2,I),IDCR(1,I))` (9); `        IF( II <= 0 ) CYCLE` (10); `        DO J = 1, ND` (11); `          JJ = INDOP(KN(J))` (12); `          IF( JJ <= 0 ) CYCLE` (13); `          DO K = IDSK(II), IDSK(II+1) - 1` (14); `            IF( IDCG(K) == JJ ) THEN` (15); `              STF(K) = STF(K) + ELHM12(I,J)` (16); `              GOTO 10` (17); `            ENDIF` (18); `          ENDDO` (19); `          GOTO 90` (20); `   10   ENDDO` (21); `      ENDDO` (22) |
| 24–39 | 둘째 블록은 INDOP에서 행을, INDOF에서 열을 얻어 ELHM21을 누적한다. 두 번호의 비양수 검사, 행 저장 범위 탐색, 일치 후 레이블 20 이동, 탐색 실패 후 레이블 90 이동을 수행한다. 원문: `      DO I = 1, ND` (24); `        II = INDOP(KN(I))` (25); `        IF( II <= 0 ) CYCLE` (26); `        DO J = 1, NCR` (27); `          JJ = INDOF(IDCR(2,J),IDCR(1,J))` (28); `          IF( JJ <= 0 ) CYCLE` (29); `          DO K = IDSK(II), IDSK(II+1) - 1` (30); `            IF( IDCG(K) == JJ ) THEN` (31); `              STF(K) = STF(K) + ELHM21(I,J)` (32); `              GOTO 20` (33); `            ENDIF` (34); `          ENDDO` (35); `          GOTO 90` (36); `   20   ENDDO` (37); `      ENDDO` (38) |
| 40–61 | 셋째 블록은 양쪽 모두 INDOP 번호를 사용하여 ELHM22를 누적한다. 정상 완료는 RETURN한다. 어느 블록에서든 주소를 찾지 못하면 레이블 90의 메시지를 쓰고 ERRSTP(90,ITO)를 호출한다. 원문: `      DO I = 1, ND` (40); `        II = INDOP(KN(I))` (41); `        IF( II <= 0 ) CYCLE` (42); `        DO J = 1, ND` (43); `          JJ = INDOP(KN(J))` (44); `          IF( JJ <= 0 ) CYCLE` (45); `          DO K = IDSK(II), IDSK(II+1) - 1` (46); `            IF( IDCG(K) == JJ ) THEN` (47); `              STF(K) = STF(K) + ELHM22(I,J)` (48); `              GOTO 30` (49); `            ENDIF` (50); `          ENDDO` (51); `          GOTO 90` (52); `   30   ENDDO` (53); `      ENDDO` (54); `      RETURN` (56); `   90 WRITE(ITO,*) 'NO ADRESS FOR [K], PROGRAM STOPPED.'` (58); `      CALL ERRSTP(90,ITO)` (59); `      END` (61) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 15–20·31–36·47–52: 각 행에서 일치하는 첫 열 주소를 찾으면 해당 값만 더하고 탐색을 끝낸다.
