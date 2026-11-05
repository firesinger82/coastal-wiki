---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/axb.f
lines: 29
sha256: e80926008b347dd53a07901fffdc9b6b06462d5e6ab110d827f60cf9f85521bd
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# axb.f — 판독 구간 기록

구간은 1행부터 29행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–17 | AXB는 행렬(matrix) 곱 C=A*B의 출력·입력 크기를 주석에 적는다(2–11). 암시적 형과 C(N1,N3)·A(N1,N2)·B(N2,N3)를 선언한다(13–14). 구분·계산 시작 주석을 포함한다. 원문: `      SUBROUTINE  AXB( C,A,B,N1,N2,N3 )` (2); `C  CALCULATE  C = A X B` (4); `C  C      = C MATRIX   ( N1 X N3 )                        --- ( O )` (6); `C  A      = A MATRIX   ( N1 X N2 )                        --- ( I )` (7); `C  B      = B MATRIX   ( N2 X N3 )                        --- ( I )` (8); `C  N1     = NUMBER OF COLUMN                              --- ( I )` (9); `C  N2     = NUMBER OF COLUMN,ROWS                         --- ( I )` (10); `C  N3     = NUMBER OF ROWS                                --- ( I )` (11); `      IMPLICIT REAL*8 (A-H,O-Z)` (13); `      DIMENSION  C(N1,N3),A(N1,N2),B(N2,N3)` (14); `C--- CALCULATE MATRIX ---` (17). |
| 18–29 | 시작 시 2행 AXB 루틴 안. I=1..N3, J=1..N1의 출력 성분을 0으로 초기화한다(18–20). 그 안 K=1..N2에서 A(J,K)*B(K,I)를 누적한다(22–24). 세 루프 종료·주석·RETURN·END를 포함한다. 원문: `      DO 3000 I=1,N3` (18); `      DO 2000 J=1,N1` (19); `         C(J,I) = 0.0D0` (20); `         DO 1000 K=1,N2` (22); `            C(J,I) = C(J,I) + A(J,K)*B(K,I)` (23); ` 1000    CONTINUE` (24); ` 2000 CONTINUE` (25); ` 3000 CONTINUE` (26); `      RETURN` (28); `      END` (29). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
