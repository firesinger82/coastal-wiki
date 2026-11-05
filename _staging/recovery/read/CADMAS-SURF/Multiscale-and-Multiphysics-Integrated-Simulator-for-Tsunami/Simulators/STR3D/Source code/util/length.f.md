---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/length.f
lines: 15
sha256: dd7a99413fd4cf4b82a2d05b85f1fd29f6fbf275a76edc4bd05084d1adffa4a0
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# length.f — 판독 구간 기록

구간은 1행부터 15행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | LENGTH의 인수와 암시적 형, GRID1(N)·GRID2(N)을 선언한다(1–4). RLEN을 0으로 두고 I=1..N에서 GRID1(I)와 GRID2(I)의 차이 제곱을 누적한다(6–10). 제곱근으로 유클리드 거리(Euclidean distance)를 구한다(12). 구분 주석·RETURN·END까지 포함한다. 원문: `      SUBROUTINE LENGTH(RLEN,GRID1,GRID2,N)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION GRID1(N),GRID2(N)` (4); `      RLEN = 0.` (6); `      DO 100 I=1,N` (8); `        RLEN = RLEN + ( GRID1(I)-GRID2(I) ) * ( GRID1(I)-GRID2(I) )` (9); `  100 CONTINUE` (10); `      RLEN = DSQRT( RLEN )` (12); `      RETURN` (14); `      END` (15). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
