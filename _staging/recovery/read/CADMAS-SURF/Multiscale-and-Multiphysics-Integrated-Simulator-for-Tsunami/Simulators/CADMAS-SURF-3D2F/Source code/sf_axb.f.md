---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/CADMAS-SURF-3D2F/Source code/sf_axb.f
lines: 29
sha256: 08b64c11c0027a42eb121593ced561de1659e5fb46fe60159304641037960747
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# sf_axb.f — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | 행렬 곱(matrix multiplication) C=A×B의 입구·인수 설명·암시적 배정밀도(double precision)와 배열 C(N1,N3)·A(N1,N2)·B(N2,N3)를 선언한다. 원문: `      SUBROUTINE SF_AXB( C,A,B,N1,N2,N3 )` (2); `C  CALCULATE  C = A X B` (4); `C  C      = C MATRIX   ( N1 X N3 )                        --- ( O )` (6); `C  A      = A MATRIX   ( N1 X N2 )                        --- ( I )` (7); `C  B      = B MATRIX   ( N2 X N3 )                        --- ( I )` (8); `C  N1     = NUMBER OF COLUMN                              --- ( I )` (9); `C  N2     = NUMBER OF COLUMN,ROWS                         --- ( I )` (10); `C  N3     = NUMBER OF ROWS                                --- ( I )` (11); `      IMPLICIT REAL*8 (A-H,O-Z)` (13); `      DIMENSION  C(N1,N3),A(N1,N2),B(N2,N3)` (14); `C--- CALCULATE MATRIX ---` (17) |
| 18–29 | 시작 시 2행 SF_AXB 루틴 안이다. I=1..N3·J=1..N1 루프에서 C(J,I)를 0으로 초기화하고 K=1..N2 곱을 누적한다. 세 루프 뒤 RETURN·END로 끝낸다. 원문: `      DO 3000 I=1,N3` (18); `      DO 2000 J=1,N1` (19); `         C(J,I) = 0.0D0` (20); `         DO 1000 K=1,N2` (22); `            C(J,I) = C(J,I) + A(J,K)*B(K,I)` (23); ` 1000    CONTINUE` (24); ` 2000 CONTINUE` (25); ` 3000 CONTINUE` (26); `      RETURN` (28); `      END` (29) |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
