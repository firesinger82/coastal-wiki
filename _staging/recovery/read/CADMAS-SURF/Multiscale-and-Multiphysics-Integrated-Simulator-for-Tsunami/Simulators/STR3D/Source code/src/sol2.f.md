---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/sol2.f
lines: 40
sha256: 7490aa355814d56514e0b938f424f1759cde36d6ec575f5fb0655383d6afc2b0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sol2.f — 판독 구간 기록

구간은 1행부터 40행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–40 | SOL2 입구와 배열 선언이다(1–5). YFUNC 뒤 F>=SY이면 SY를 갱신하고 DSOL0·DFDSG·HARFC·AXB·HARFAB으로 D를 계산한다(7–28). ELSE에서는 IST=0과 SY=F를 설정하고 DSOL0으로 D를 계산한다(30–36). 원문: `      SUBROUTINE SOL2(IST,SY,S,D,E,ANU,IYLD,HD,ALP)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION S(6),WK2(6),WK3(21),D(21),DE(21),DFDS(6),DRDE(6)`<br>`     &         ,DEPDE(6,6)` (4–5); `      CALL YFUNC(F,S,IYLD,ALP)` (7); `      IF( F >= SY ) THEN` (9); `        SY = F` (11); `        CALL DSOL0(DE,E,ANU)` (13); `        CALL DFDSG(DFDS,S,IYLD,ALP)` (14); 주석: `C       ----- [DRAM/DEPS] -----` (16); `        CALL HARFC(WK2,DFDS,DE,1,6)` (18); `        DRDE(:) = WK2(:) / ( HD + DOT_PRODUCT(WK2,DFDS) )` (19); 주석: `C       ----- [DEPS_P/DEPS] -----` (21); `        CALL AXB(DEPDE,DFDS,DRDE,6,1,6)` (23); 주석: `C       ----- [Dp] -----` (25); `        CALL HARFAB(WK3,DE,DEPDE,6)` (27); `        D(:) = DE(:) - WK3(:)` (28); `      ELSE` (30); `        IST = 0` (32); `        SY = F` (34); `        CALL DSOL0(D,E,ANU)` (36); `      ENDIF` (38); `      END` (40) 해석: D를 접선행렬로 보는 설명은 호출과 `[Dp]` 주석(25)에 따른 해석이다. [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 9–28·30–36: F>=SY 분기에는 IST 대입이 없다. ELSE에는 IST=0 대입이 있다.
- 19: DRDE 계산은 HD+DOT_PRODUCT(WK2,DFDS)로 나눈다. 이 식 앞에 분모 0 검사가 없다.
