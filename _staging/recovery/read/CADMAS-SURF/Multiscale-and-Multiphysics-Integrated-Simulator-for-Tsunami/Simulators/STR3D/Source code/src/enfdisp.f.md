---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/enfdisp.f
lines: 16
sha256: 2900e94a4f760753c34c595c7e9c9b7955e8fff974c833b46b85a507987132ba
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# enfdisp.f — 판독 구간 기록

구간은 1행부터 16행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–6 | ENFDISP의 암시적 형을 선언한다. DT1과 DT2의 평균 DT12를 계산한다. 해석: DT1과 DT2는 시간 간격이다. 원문: `      SUBROUTINE ENFDISP(DUG,SPCD,F,ITYP,UG1,UG2,DT1,DT2)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); 주석 원문 `C-----------------------------------------------------------------------` (4); `      DT12 = .5D0 * ( DT1 + DT2 )` (5). [11-04 전수 검증 정정] |
| 7–16 | 시작 시 1행 ENFDISP 루틴 안. ITYP 1·2·3에 따라 인용된 세 식으로 DUG를 계산한다. 해석: UG1·UG2는 이전 변위이며 DT1·DT2는 시간 간격이다. SELECT와 루틴 끝을 포함한다. 원문: `      SELECT CASE( ITYP )` (7); `      CASE( 1 )` (8); `        DUG = SPCD * F - UG2` (9); `      CASE( 2 )` (10); `        DUG = UG1 + 2.D0 * DT12 * SPCD * F - UG2` (11); `      CASE( 3 )` (12); `        DUG = DT2 * ( DT12 * SPCD * F + ( UG2 - UG1 ) / DT1 )` (13); `      END SELECT` (14); `      END` (16). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 7–14: SELECT CASE에는 1·2·3만 있고 CASE DEFAULT가 없다. 다른 ITYP에서는 DUG 대입이 없다.
- 13: DT1으로 나누는 계산 앞에 DT1=0 검사는 없다.
