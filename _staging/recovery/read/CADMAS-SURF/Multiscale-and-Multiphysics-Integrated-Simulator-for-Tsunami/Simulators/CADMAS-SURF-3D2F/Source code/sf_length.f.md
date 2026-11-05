---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_length.f
lines: 15
sha256: 0ffc2dc6b82fe1a5cc8414dd1e9533766d3f4827fed86dba4a536f4c3412a9de
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_length.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | SF_LENGTH 선언과 GRID1(N)·GRID2(N) 범위, 구분 주석(1–5). RLEN=0에서 N개 좌표 차이의 제곱을 누적한다(6–10). 제곱근을 취하여 유클리드 거리(Euclidean distance)를 반환한다(12–14). 원문: `      SUBROUTINE SF_LENGTH(RLEN,GRID1,GRID2,N)` (1)<br>`      IMPLICIT REAL*8(A-H,O-Z)` (3)<br>`      DIMENSION GRID1(N),GRID2(N)` (4)<br>`C----&------------------------------------------------------------------` (5)<br>`      RLEN = 0.` (6)<br>`      DO 100 I=1,N` (8)<br>`        RLEN = RLEN + ( GRID1(I)-GRID2(I) ) * ( GRID1(I)-GRID2(I) )` (9)<br>`  100 CONTINUE` (10)<br>`      RLEN = DSQRT( RLEN )` (12)<br>`      RETURN` (14)<br>`      END` (15) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
