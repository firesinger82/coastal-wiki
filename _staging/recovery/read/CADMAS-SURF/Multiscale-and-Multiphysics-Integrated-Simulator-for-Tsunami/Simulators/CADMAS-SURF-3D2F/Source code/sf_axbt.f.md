---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_axbt.f
lines: 23
sha256: 69e3df2aec86f2e65b724b85556cc2b3d7139867261f1a8edfc67a9bfc7ce494
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_axbt.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–12 | 전치 행렬(transposed matrix)을 사용하는 C=A×BT의 입구·주석·암시적 배정밀도(double precision)·배열 C(N1,N3)·A(N1,N2)·B(N3,N2)를 선언한다. 원문: `      SUBROUTINE  SF_AXBT( C,A,B,N1,N2,N3 )` (2); `C  CALCULATE  C = A X BT` (4); `C  C      = C MATRIX   ( N1 X N3 )                        --- ( O )` (6); `C  A      = A MATRIX   ( N1 X N2 )                        --- ( I )` (7); `C  B      = B MATRIX   ( N3 X N2 )                        --- ( I )` (8); `      IMPLICIT REAL*8 (A-H,O-Z)` (10); `      DIMENSION  C(N1,N3),A(N1,N2),B(N3,N2)` (11) |
| 13–23 | 시작 시 2행 SF_AXBT 루틴 안이다. I=1..N1·J=1..N3 루프에서 C(I,J)를 0으로 초기화하고 K=1..N2에서 A(I,K)*B(J,K)를 누적한다. 세 루프 뒤 반환한다. 원문: `      DO 3000 I=1,N1` (13); `      DO 2000 J=1,N3` (14); `        C(I,J) = 0.0D0` (15); `        DO 1000 K=1,N2` (16); `          C(I,J) = C(I,J) + A(I,K)*B(J,K)` (17); ` 1000   CONTINUE` (18); ` 2000 CONTINUE` (19); ` 3000 CONTINUE` (20); `      RETURN` (22); `      END` (23) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
