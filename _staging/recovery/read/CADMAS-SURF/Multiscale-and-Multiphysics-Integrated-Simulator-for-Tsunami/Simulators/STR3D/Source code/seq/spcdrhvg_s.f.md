---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/seq/spcdrhvg_s.f
lines: 23
sha256: 50a0d1e25dc1b082d0ecfb54c17a9204f3f4c1e68b466bef27dec053bd4dcbe4
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# spcdrhvg_s.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–23 | SPCDRHVG_S의 암시적 형·배열 선언. INDOP(KN(J))=-1인 절점 J와 INDOP(KN(I))>0인 절점 I에 대해 상삼각 배열 위치 IP를 계산한다. J>=I 여부에 따라 인덱스 식을 나누고 RHV에서 ELHM(IP)*PG(KN(J))를 뺀다. 원문: `      SUBROUTINE SPCDRHVG_S(RHV,ELHM,KN,ND,INDOP,PG)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION PG(*),ELHM(*),KN(ND),INDOP(*),RHV(*)` (4); `      DO J = 1, ND` (6); `        JJ = INDOP( KN(J) )` (7); `        IF( JJ == -1 ) THEN` (8); `          DO I = 1, ND` (9); `            II = INDOP( KN(I) )` (10); `            IF( II > 0 ) THEN` (11); `              IF( J >= I ) THEN` (12); `                IP = ( 2*ND - I + 2 ) * ( I - 1 ) / 2 + J - I + 1` (13); `              ELSE` (14); `                IP = ( 2*ND - J + 2 ) * ( J - 1 ) / 2 + I - J + 1` (15); `              ENDIF` (16); `              RHV(II) = RHV(II) - ELHM(IP) * PG( KN(J) )` (17); `            ENDIF` (18); `          ENDDO` (19); `        ENDIF` (20); `      ENDDO` (21); `      END` (23). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
