---
file: models/CADMAS-SURF/raw/source_code/Multiscale-and-Multiphysics-Integrated-Simulator-for-Tsunami/Simulators/STR3D/Source code/util/mean4.f
lines: 14
sha256: 47ad1ba703149408db89aa53e99c34f9d258adb1046906d26485cfcd9d798c01
reader: codex gpt-6.1-sol
read_date: 2026-11-04
---

# mean4.f — 판독 구간 기록

구간은 1행부터 14행까지 빈틈없이 이어진다.

| 구간 | 내용 |
|---|---|
| 1–14 | MEAN4의 인수와 암시적 형(implicit typing), A(N)·B(N,*)·IDX(M)을 선언한다(1–4). A 전체를 0으로 두고 I=1..M에서 선택 열 B(:,IDX(I))를 더한다(6–10). DBLE(M)으로 나누어 선택 열의 산술평균(arithmetic mean) 벡터를 구한다(12). 빈 줄·END까지 포함한다. 원문: `      SUBROUTINE MEAN4(A,B,N,IDX,M)` (1); `      IMPLICIT REAL*8(A-H,O-Z)` (3); `      DIMENSION A(N),B(N,*),IDX(M)` (4); `      A(:) = 0.` (6); `      DO I = 1, M` (8); `        A(:) = A(:) + B(:,IDX(I))` (9); `      ENDDO` (10); `      A(:) = A(:) / DBLE(M)` (12); `      END` (14). |

## 판독 중 확인된 코드 사실 (판단 아님, 후속 검토 대상)

- 8–12: DBLE(M)으로 나누기 전에 M이 0인지 검사하는 문장은 없다.
