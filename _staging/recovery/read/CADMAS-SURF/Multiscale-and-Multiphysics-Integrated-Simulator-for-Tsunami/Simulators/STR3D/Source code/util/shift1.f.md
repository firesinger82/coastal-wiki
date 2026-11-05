---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/shift1.f
lines: 22
sha256: 5119463003f99563fc8b38b168101d14139e5d1d56f1d27cd8e802e6b9b3ae0c
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# shift1.f — 판독 구간 기록

구간은 1행부터 22행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–15 | SHIFT1는 실수 배열(real array)의 복사 A=B와 입력·출력·개수 N을 주석으로 설명한다(2–8). 암시적 형(implicit typing)과 A(N)·B(N)을 선언한다(11–12). 구분·복사 시작 주석을 포함한다. 원문: `      SUBROUTINE  SHIFT1( A,B,N )` (2); `C  A = B  ---  DATA SHIFT` (4); `C  A      = SHIFT AREA                                    --- ( O )` (6); `C  B      = SHIFT DATA                                    --- ( I )` (7); `C  N      = NUMBER OF SHIFT DATA                          --- ( I )` (8); `      IMPLICIT REAL*8 (A-H,O-Z)` (11); `      DIMENSION  A(N),B(N)` (12); `C--- SHIFT ---` (15). |
| 16–22 | 시작 시 2행 SHIFT1 루틴 안. I=1..N에서 B(I)를 A(I)에 복사한다(16–18). 빈 주석·RETURN·END를 포함한다. 원문: `      DO 1000 I=1,N` (16); `         A(I) = B(I)` (17); ` 1000 CONTINUE` (18); `      RETURN` (21); `      END` (22). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

없음
