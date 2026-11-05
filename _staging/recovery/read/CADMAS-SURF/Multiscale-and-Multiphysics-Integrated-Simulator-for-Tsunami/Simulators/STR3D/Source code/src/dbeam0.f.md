---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/src/dbeam0.f
lines: 14
sha256: 6d90bc0d0ab8ec9c795077a6c992f9760f7c7cfdb2e13c84a204e6220b5b6347
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# dbeam0.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–5 | DBEAM0의 암시적 형(implicit typing)과 길이 6인 D 배열을 선언한다. 원문: `      SUBROUTINE DBEAM0(D,E,RNU)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION D(6)` (4). |
| 6–14 | 시작 시 1행 DBEAM0 루틴 안. E와 RNU로 G를 계산한다. 해석: E를 탄성계수로 보고 RNU를 포아송비로 보면 G는 전단계수이다. D 전체를 0으로 초기화한 뒤 1번에 E, 4·6번에 G를 둔다. 루틴 끝을 포함한다. 원문: `      G = .5D0 * E / ( 1.D0 + RNU )` (6); `      D(:) = 0.` (8); `      D(1) = E` (10); `      D(4) = G` (11); `      D(6) = G` (12); `      END` (14). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 6: G 계산에서 1.D0+RNU로 나눈다. 이 파일에는 분모가 0인지 확인하는 조건문이 없다.
