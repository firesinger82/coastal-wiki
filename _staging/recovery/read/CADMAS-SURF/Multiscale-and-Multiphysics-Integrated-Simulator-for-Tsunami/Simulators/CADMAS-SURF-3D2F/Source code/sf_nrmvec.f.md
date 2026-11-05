---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_nrmvec.f
lines: 19
sha256: 0f98ec8e8a76931851eabfea1f67d71832b59c24cb12b34e52a7cae4bd0c13a1
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_nrmvec.f — 판독 구간 기록

구간은 1행부터 19행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–19 | GRID에서 NP가 지정하는 열의 값을 X(:,1:N)에 복사한다(4–6). N=3이면 두 변 벡터(vector)를 만든다(8–11). N=4이면 계수 .25D0의 좌표 조합으로 R·S를 만든다(12–14). SF_CROSS2(R,S,E)를 호출한다(17). 원문(연속 표시는 앞 문장에 이어짐): `      SUBROUTINE SF_NRMVEC(E,NP,N,GRID)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION X(3,4),GRID(3,*),NP(N),R(3),S(3),E(3)` (4); `      X(:,1:N) = GRID(:,NP(:))` (6); `      SELECT CASE( N )` (8); `      CASE( 3 )` (9); `        R(:) = X(:,2) - X(:,1)` (10); `        S(:) = X(:,3) - X(:,1)` (11); `      CASE( 4 )` (12); `        R(:) = .25D0 * ( -X(:,1) + X(:,2) + X(:,3) - X(:,4) )` (13); `        S(:) = .25D0 * ( -X(:,1) - X(:,2) + X(:,3) + X(:,4) )` (14); `      END SELECT` (15); `      CALL SF_CROSS2(R,S,E)` (17); `      END` (19). [11-04 전수 검증 정정] |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 4·6·8–15: X의 두 번째 차원은 4이며 N에 대한 SELECT CASE에는 3·4만 있고 CASE DEFAULT가 없다.
