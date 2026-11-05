---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/spcdrhv.f
lines: 24
sha256: 450de658e5841c325e72259324931e96808bee2e19a404d21ca40a8c96e2be6f
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# spcdrhv.f — 판독 구간 기록

구간은 1행부터 24행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–24 | SPCDRHV 입구와 배열 선언이다(1–4). JJ==-1인 J에 대해 II>0인 I의 FT(II)를 보정한다(6–21). J>=I 여부로 IAD를 계산하고 ESTF(IAD)와 UG(IDCR(2,J),IDCR(1,J))의 곱을 FT(II)에서 뺀다(12–17). 해석: JJ==-1을 구속 자유도, FT를 우변, ESTF를 압축 대칭행렬로 보는 것은 이 인덱스와 계산식에 따른 해석이다. 원문: `      SUBROUTINE SPCDRHV(FT,ESTF,IDCR,NCR,INDOF,UG)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION UG(6,*),ESTF(*),IDCR(2,NCR),INDOF(6,*),FT(*)` (4); `      DO 100 J=1,NCR` (6); `        JJ=INDOF(IDCR(2,J),IDCR(1,J))` (7); `        IF(JJ .EQ. -1) THEN` (8); `          DO 200 I=1,NCR` (9); `            II=INDOF(IDCR(2,I),IDCR(1,I))` (10); `            IF(II .GT. 0) THEN` (11); `              IF(J.GE.I) THEN` (12); `                IAD=(2*NCR-I+2)*(I-1)/2+J-I+1` (13); `              ELSE` (14); `                IAD=(2*NCR-J+2)*(J-1)/2+I-J+1` (15); `              ENDIF` (16); `              FT(II)=FT(II)-ESTF(IAD)*UG(IDCR(2,J),IDCR(1,J))` (17); `            ENDIF` (18); `  200     CONTINUE` (19); `        ENDIF` (20); `  100 CONTINUE` (21); `      RETURN` (23); `      END` (24) [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
