---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/vecml3.f
lines: 23
sha256: da583145e12f584f0b78899c0272421e6891d556437421ee741a2a9b2b628ce7
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# vecml3.f — 판독 구간 기록

구간은 1행부터 23행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–18 | VECML3는 대각 행렬(diagonal matrix)과 벡터(vector)의 곱, 인수와 작성자·일자를 주석으로 설명한다(1–15). 암시적 형(implicit typing)과 D1(N)·D2(N)·D3(N)을 선언한다(16–17). 빈 주석을 포함한다. 원문: `      SUBROUTINE VECML3(D3,D1,D2,N)` (1); `C FOR SUBROUTINE VECML3` (2); `C 1.PURPOSE` (4); `C         VECTOR PRODUCT FOR DIAGNAL MATRIX AND VECTOR` (5); `C 3.ARGUMENT` (7); `C   I D1      D VECTOR FOR DIAGNAL MATRIX` (8); `C   I D2      D VECTOR` (9); `C   O D3      D CALCULATED VECTOR` (10); `C   I N       I DIMENSION FOR VECTOR (=3)` (11); `C 8.PROGRAM` (13); `C    KITAGAWA KAZUSHI (1988-03-10)  MI(910708)` (14); `      IMPLICIT REAL*8(A-H,O-Z)` (16); `      DIMENSION D1(N),D2(N),D3(N)` (17). |
| 19–23 | 시작 시 1행 VECML3 루틴 안. I=1..N 루프에서 D1(I)*D2(I)를 D3(I)에 대입한다(19–21). RETURN·END를 포함한다. 원문: `      DO  100   I  =  1 , N` (19); `          D3(I)    =  D1(I)  *  D2(I)` (20); `  100 CONTINUE` (21); `      RETURN` (22); `      END` (23). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 11·19: 주석의 벡터 차원은 (=3)으로 쓰였지만 루프 상한은 인수 N이다.
