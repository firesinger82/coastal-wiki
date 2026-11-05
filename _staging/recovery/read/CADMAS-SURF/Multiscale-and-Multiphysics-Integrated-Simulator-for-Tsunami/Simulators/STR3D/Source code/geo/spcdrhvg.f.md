---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/geo/spcdrhvg.f
lines: 39
sha256: 2a258290c65fb4f86a28e11ee3465602af4eb19fc5c870b8dc53c49810ce3e7b
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# spcdrhvg.f — 판독 구간 기록

구간은 1행부터 39행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | SPCDRHVG는 FT를 보정한다. 실수 IMPLICIT와 행렬·배열 범위는 아래와 같다. J=1,NCR에서 `JJ = INDOF(IDCR(2,J),IDCR(1,J))`를 계산한다. JJ=-1이면 I=1,ND에서 `II = INDOP(KN(I))`를 계산한다. II>0일 때 FT(II)에서 ELHM21(I,J)*UG(IDCR(2,J),IDCR(1,J))를 뺀다. 해석: 이 연산은 지정 변위 자유도에 따른 압력 방정식 우변 보정으로 보인다. 13–14행은 하나의 조건부 대입문이다. 원문: `      SUBROUTINE SPCDRHVG(FT,ELHM12,ELHM21,ELHM22,UG,PG,KN,ND,IDCR,NCR` (1); `     &                   ,INDOF,INDOP)` (2); `      IMPLICIT REAL*8(A-H,O-Z)` (4); `      DIMENSION FT(*),ELHM12(NCR,ND),ELHM21(ND,NCR),ELHM22(ND,ND)` (5); `     &         ,UG(6,*),PG(*),KN(ND),IDCR(2,NCR),INDOF(6,*),INDOP(*)` (6); `      DO J = 1, NCR` (8); `        JJ = INDOF(IDCR(2,J),IDCR(1,J))` (9); `        IF( JJ == -1 ) THEN` (10); `          DO I = 1, ND` (11); `            II = INDOP(KN(I))` (12); `            IF( II > 0 ) ` (13); `     &        FT(II) = FT(II) - ELHM21(I,J) * UG(IDCR(2,J),IDCR(1,J))` (14); `          ENDDO` (15); `        ENDIF` (16); `      ENDDO` (17) [11-04 전수 검증 정정] |
| 19–28 | J=1,ND에서 `JJ = INDOP(KN(J))`를 계산한다. JJ=-1이면 I=1,NCR에서 `II = INDOF(IDCR(2,I),IDCR(1,I))`를 계산한다. II>0일 때 FT(II)에서 ELHM12(I,J)*PG(KN(J))를 뺀다. 해석: 이 연산은 지정 압력(pressure)에 따른 변위 방정식 우변 보정으로 보인다. 원문: `      DO J = 1, ND` (19); `        JJ = INDOP(KN(J))` (20); `        IF( JJ == -1 ) THEN` (21); `          DO I = 1, NCR` (22); `            II = INDOF(IDCR(2,I),IDCR(1,I))` (23); `            IF( II > 0 ) FT(II) = FT(II) - ELHM12(I,J) * PG(KN(J))` (24); `          ENDDO` (25); `        ENDIF` (26); `      ENDDO` (27) [11-04 전수 검증 정정] |
| 29–39 | J=1,ND에서 `JJ = INDOP(KN(J))`를 계산한다. JJ=-1이면 I=1,ND에서 `II = INDOP(KN(I))`를 계산한다. II>0일 때 FT(II)에서 ELHM22(I,J)*PG(KN(J))를 뺀다. 해석: 이 연산은 지정 압력에 따른 압력 방정식 우변 보정으로 보인다. 세 번째 루프와 루틴을 끝낸다. 원문: `      DO J = 1, ND` (29); `        JJ = INDOP(KN(J))` (30); `        IF( JJ == -1 ) THEN` (31); `          DO I = 1, ND` (32); `            II = INDOP(KN(I))` (33); `            IF( II > 0 ) FT(II) = FT(II) - ELHM22(I,J) * PG(KN(J))` (34); `          ENDDO` (35); `        ENDIF` (36); `      ENDDO` (37); `      END` (39) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
