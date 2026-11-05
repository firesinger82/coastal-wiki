---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/harfab.f
lines: 31
sha256: 01c6c09bdfa35191d26159e6b6853340fc5913b9aa9d8c0eb68f3e32bcee6325
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# harfab.f — 판독 구간 기록

구간은 1행부터 31행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | HARFAB는 일차원 압축 저장(packed storage) 행렬 A·B와 N×N 행렬 C의 곱을 설명하는 주석을 갖는다(2–8). 암시적 형과 A(*)·B(*)·C(N,N)를 선언한다(11–12). 출력 인덱스 IC를 0으로 초기화한다(14). 원문: `      SUBROUTINE  HARFAB(A,B,C,N)` (2); `C  A = B X C  ( A & B MATRIX IS HARF MATRIX )` (4); `C  A      = A MATRIX   ( ONE DIMENSION )                  --- ( O )` (6); `C  B      = B MATRIX   ( ONE DIMENSION )                  --- ( I )` (7); `C  C      = C MATRIX   ( N X N )                          --- ( I )` (8); `      IMPLICIT REAL*8 (A-H,O-Z)` (11); `      DIMENSION  A(*),B(*),C(N,N)` (12); `      IC = 0` (14). |
| 16–31 | 시작 시 2행 HARFAB 루틴 안. I=1..N, J=I..N의 상삼각(upper triangular) 성분에서 IC를 증가시키고 A(IC)를 0으로 둔다(16–19). K=1..N에서 I<=K 여부로 압축 저장 인덱스 IP를 두 식 중 하나로 계산한다(20–25). B(IP)*C(K,J)를 누적한다(26). 세 루프 종료·주석·END를 포함한다. 원문: `      DO I = 1, N` (16); `        DO J = I, N` (17); `          IC = IC + 1` (18); `          A(IC) = 0.` (19); `          DO K = 1, N` (20); `            IF( I <= K ) THEN` (21); `              IP = ( 2*N + 2 - I )*( I - 1 ) / 2 + K + 1 - I` (22); `            ELSE` (23); `              IP = ( 2*N + 2 - K )*( K - 1 ) / 2 + I + 1 - K` (24); `            ENDIF` (25); `            A(IC) = A(IC) + B(IP)*C(K,J)` (26); `          ENDDO` (27); `        ENDDO` (28); `      ENDDO` (29); `      END` (31). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
