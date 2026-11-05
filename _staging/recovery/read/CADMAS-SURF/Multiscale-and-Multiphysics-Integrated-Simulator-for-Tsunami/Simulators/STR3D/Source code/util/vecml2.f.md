---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/vecml2.f
lines: 13
sha256: 1967d7d8692b0229ac46b3e120fac36d13dc9bf503cd04cb372000d340edc239
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vecml2.f — 판독 구간 기록

구간은 1행부터 13행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–13 | VECML2의 인수와 암시적 형(implicit typing), V(N)을 선언한다(1–4). A를 0으로 두고 I=1..N에서 V(I)의 제곱합을 누적한다(6–9). 제곱근으로 유클리드 노름(Euclidean norm)을 구한다(10). 구분 주석·RETURN·END까지 포함한다. 원문: `      SUBROUTINE VECML2(A,V,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION V(N)` (4); `      A=0.` (6); `      DO I=1,N` (7); `        A=A+V(I)*V(I)` (8); `      ENDDO` (9); `      A=DSQRT(A)` (10); `      RETURN` (12); `      END` (13). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
